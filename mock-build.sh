#!/bin/bash -eux

yum -y install epel-release
yum -y install rpmdevtools mock

if [ -z "${@}" ] ; then
  PACKAGES="
  ghc-base64-bytestring
  ghc-Crypto
  ghc-curl
  ghc-hinotify
  ghc-regex-pcre
  python-affinity
  python-bitarray
  ganeti"
else
  PACKAGES="${@}"
fi

GANETI_REPO="${PWD}/ganeti-repo"
GANETI_SRPMS="${PWD}/ganeti-repo-srpms"

mkdir -p $GANETI_REPO $GANETI_SRPMS
createrepo_c $GANETI_REPO
createrepo_c $GANETI_SRPMS

cat << EOF > /etc/mock/epel-7-x86_64.cfg
config_opts['root'] = 'epel-7-x86_64'
config_opts['target_arch'] = 'x86_64'
config_opts['legal_host_arches'] = ('x86_64',)
config_opts['chroot_setup_cmd'] = 'install @buildsys-build'
config_opts['dist'] = 'el7'  # only useful for --resultdir variable subst
config_opts['releasever'] = '7'

config_opts['yum.conf'] = """
[main]
keepcache=1
debuglevel=2
reposdir=/dev/null
logfile=/var/log/yum.log
retries=20
obsoletes=1
gpgcheck=0
assumeyes=1
syslog_ident=mock
syslog_device=
mdpolicy=group:primary
best=1

# repos
[base]
name=BaseOS
baseurl=http://centos.osuosl.org/7/os/x86_64/
failovermethod=priority
gpgkey=file:///usr/share/distribution-gpg-keys/centos/RPM-GPG-KEY-CentOS-7
gpgcheck=1
skip_if_unavailable=False

[updates]
name=updates
enabled=1
baseurl=http://centos.osuosl.org/7/updates/x86_64/
failovermethod=priority
gpgkey=file:///usr/share/distribution-gpg-keys/centos/RPM-GPG-KEY-CentOS-7
gpgcheck=1
skip_if_unavailable=False

[epel]
name=epel
baseurl=http://epel.osuosl.org/7/x86_64/
failovermethod=priority
gpgkey=file:///usr/share/distribution-gpg-keys/epel/RPM-GPG-KEY-EPEL-7
gpgcheck=1
skip_if_unavailable=False

[extras]
name=extras
baseurl=http://centos.osuosl.org/7/extras/x86_64/
failovermethod=priority
gpgkey=file:///usr/share/distribution-gpg-keys/centos/RPM-GPG-KEY-CentOS-7
gpgcheck=1
skip_if_unavailable=False

[ganeti-local]
baseurl=file://${GANETI_REPO}
enabled=1
gpgcheck=0
"""
EOF

cd rpmbuild

for i in $PACKAGES ; do
  mkdir -p "${i}/SOURCES"
  spectool -g -R "${i}/SPECS/${i}.spec" -C "${i}/SOURCES"
  rpmbuild -D "_topdir ${i}" -bs "${i}/SPECS/${i}.spec"
  srpm="$(ls ${i}/SRPMS)"
  mock -r epel-7-x86_64 -v --resultdir="${i}/resultdir" \
    --rebuild "${i}/SRPMS/$srpm"
  mv -v ${i}/resultdir/${i}*src.rpm $GANETI_SRPMS/
  mv -v ${i}/resultdir/${i}*rpm $GANETI_REPO/
  createrepo_c $GANETI_REPO
  createrepo_c $GANETI_SRPMS
done
