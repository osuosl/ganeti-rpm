# generated by cabal-rpm-0.13.3
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name bytestring-builder
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.10.8.2.0
Release:        1%{?dist}
Summary:        The new bytestring builder, packaged outside of GHC

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-deepseq-devel
# End cabal-rpm deps

%description
This is the bytestring builder that is debuting in bytestring-0.10.4.0, which
should be shipping with GHC 7.8, probably late in 2013. This builder has
several nice simplifications and improvements, and more out-of-box
functionality than the older blaze-builder.

Note that this package detects which version of bytestring you are compiling
against, and if you are compiling against bytestring-0.10.4 or later, will be
an empty package.

This package lets the new interface and implementation be used with most older
compilers without upgrading bytestring, which can be rather problematic.
In conjunction with blaze-builder-0.4 or later, which offers an implementation
of blaze-builder in terms of bytestring-builder, this should let most people
try the new interface and implementation without causing undue compatibility
problems with packages that depend on blaze-builder.

GHC 7.6 did debut an almost identical interface and implementation, but with
slightly different module names and organization. Trying to re-export/rename
the builder provided with 7.6 did not turn out to be very practical, because
this interface includes new functions that rely on Builder internals, which are
not exported in 7.6. Furthermore, these module names should be deprecated in
7.10.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
%endif

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
%license LICENSE

%files devel -f %{name}-devel.files
%doc CHANGELOG.md


%changelog
* Thu Feb 20 2020 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.10.8.2.0-1
- spec file generated by cabal-rpm-0.13.3