# generated by cabal-rpm-0.12.3
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name reflection
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        1.5.2.1
Release:        1%{?dist}
Summary:        Reifies arbitrary terms into types that can be reflected back into terms

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-template-haskell-devel
# End cabal-rpm deps

%description
This package addresses the /configuration problem/ which is propogating
configurations that are available at run-time, allowing multible configurations
to coexist without resorting to mutable global variables or
'System.IO.Unsafe.unsafePerformIO'.

That package is an implementation of the ideas presented in the paper
"Functional Pearl: Implicit Configurations" by Oleg Kiselyov and Chung-chieh
Shan (<http://okmij.org/ftp/Haskell/tr-15-04.pdf original paper>).
However, the API has been streamlined to improve performance.

Austin Seipp's tutorial
<https://www.fpcomplete.com/user/thoughtpolice/using-reflection Reflecting
values to types and back> provides a summary of the approach taken by this
library, along with more motivating examples.


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
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkgver}


%build
%ghc_lib_build


%install
%ghc_lib_install


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc CHANGELOG.markdown README.markdown examples


%changelog
* Mon Apr 15 2019 Jun Futagawa <jfut@integ.jp> - 1.5.2.1-1
- Rebase spec file by cabal-rpm spec reflection-1.5.2.1

* Mon Apr 15 2019 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 1.5.2.1-1
- spec file generated by cabal-rpm-0.12.3