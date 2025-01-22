#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Convert-Bencode
Version  : 1.03
Release  : 20
URL      : https://cpan.metacpan.org/authors/id/O/OR/ORCLEV/Convert-Bencode-1.03.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OR/ORCLEV/Convert-Bencode-1.03.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-Convert-Bencode-license = %{version}-%{release}
Requires: perl-Convert-Bencode-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Convert::Bencode - Functions for converting to/from bencoded strings
SYNOPSIS
use Convert::Bencode qw(bencode bdecode);

%package dev
Summary: dev components for the perl-Convert-Bencode package.
Group: Development
Provides: perl-Convert-Bencode-devel = %{version}-%{release}
Requires: perl-Convert-Bencode = %{version}-%{release}

%description dev
dev components for the perl-Convert-Bencode package.


%package license
Summary: license components for the perl-Convert-Bencode package.
Group: Default

%description license
license components for the perl-Convert-Bencode package.


%package perl
Summary: perl components for the perl-Convert-Bencode package.
Group: Default
Requires: perl-Convert-Bencode = %{version}-%{release}

%description perl
perl components for the perl-Convert-Bencode package.


%prep
%setup -q -n Convert-Bencode-1.03
cd %{_builddir}/Convert-Bencode-1.03

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Convert-Bencode
cp %{_builddir}/Convert-Bencode-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Convert-Bencode/f235ba4160673bcb7c9d58c2f09dbc7fc0efadea || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Convert::Bencode.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Convert-Bencode/f235ba4160673bcb7c9d58c2f09dbc7fc0efadea

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
