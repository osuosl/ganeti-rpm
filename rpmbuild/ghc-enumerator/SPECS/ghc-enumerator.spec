# generated by cabal-rpm-0.13.3
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name enumerator
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.4.20
Release:        1%{?dist}
Summary:        Reliable, high-performance processing with left-fold enumerators

License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
# End cabal-rpm deps

%description
Typical buffer&#x2013;based incremental I/O is based around a single loop,
which reads data from some source (such as a socket or file), transforms it,
and generates one or more outputs (such as a line count, HTTP responses, or
modified file). Although efficient and safe, these loops are all
single&#x2013;purpose; it is difficult or impossible to compose
buffer&#x2013;based processing loops.

Haskell&#x2019;s concept of &#x201C;lazy I/O&#x201D; allows pure code to
operate on data from an external source. However, lazy I/O has several
shortcomings. Most notably, resources such as memory and file handles can be
retained for arbitrarily long periods of time, causing unpredictable
performance and error conditions.

Enumerators are an efficient, predictable, and safe alternative to lazy I/O.
Discovered by Oleg Kiselyov, they allow large datasets to be processed in
near&#x2013;constant space by pure code. Although somewhat more complex to
write, using enumerators instead of lazy I/O produces more correct programs.

This library contains an enumerator implementation for Haskell, designed to be
both simple and efficient. Three core types are defined, along with numerous
helper functions:

* /Iteratee/: Data sinks, analogous to left folds. Iteratees consume a sequence
of /input/ values, and generate a single /output/ value. Many iteratees are
designed to perform side effects (such as printing to 'stdout'), so they can
also be used as monad transformers.

* /Enumerator/: Data sources, which generate input sequences. Typical
enumerators read from a file handle, socket, random number generator, or other
external stream. To operate, enumerators are passed an iteratee, and provide
that iteratee with input until either the iteratee has completed its
computation, or EOF.

* /Enumeratee/: Data transformers, which operate as both enumerators and
iteratees. Enumeratees read from an /outer/ enumerator, and provide the
transformed data to an /inner/ iteratee.


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
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
cp -bp %{SOURCE1} %{pkg_name}.cabal
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
%license license.txt
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc examples


%changelog
* Thu Feb 20 2020 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.4.20-1
- spec file generated by cabal-rpm-0.13.3
