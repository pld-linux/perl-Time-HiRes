#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Time
%define	pnam	HiRes
Summary:	Time::HiRes - High resolution alarm, sleep, gettimeofday, interval timers
Summary(pl):	Time::HiRes - wysokiej rozdzielczości funkcje alarm, sleep, gettimeofday i liczniki
Name:		perl-Time-HiRes
Version:	1.35
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		perl-Time-HiRes-makefile.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Time::HiRes - High resolution ualarm, usleep, and gettimeofday.

%description -l pl
Time::HiRes to interfejs perla dla funkcji systemowych: ualarm, usleep
i gettimeofday.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_sitearch}/Time
%dir %{perl_sitearch}/auto/Time
%dir %{perl_sitearch}/auto/Time/HiRes
%{perl_sitearch}/auto/Time/HiRes/HiRes.bs
%attr(755,root,root) %{perl_sitearch}/auto/Time/HiRes/HiRes.so
%{_mandir}/man3/*
