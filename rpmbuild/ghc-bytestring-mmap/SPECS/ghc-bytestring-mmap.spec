# generated by cabal-rpm-0.13.3
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name bytestring-mmap
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.2.2
Release:        1%{?dist}
Summary:        Mmap support for strict ByteStrings

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-unix-devel
# End cabal-rpm deps

%description
This library provides a wrapper to mmap(2), allowing files or devices to be
lazily loaded into memory as strict or lazy ByteStrings, using the virtual
memory subsystem to do on-demand loading. .


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development
files.


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files


%changelog
* Thu Feb 20 2020 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.2.2-1
- spec file generated by cabal-rpm-0.13.3
