#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Time
%define	pnam	HiRes
Summary:	Time::HiRes - high resolution alarm, sleep, gettimeofday, interval timers
Summary(pl):	Time::HiRes - wysokiej rozdzielczo¶ci funkcje alarm, sleep, gettimeofday i liczniki
Name:		perl-Time-HiRes
Version:	1.52
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0816f8707cacaeccb9051d19850f8330
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Time::HiRes - High resolution ualarm, usleep, and gettimeofday.

%description -l pl
Time::HiRes to interfejs perla dla funkcji systemowych: ualarm, usleep
i gettimeofday.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorarch}/Time
%dir %{perl_vendorarch}/auto/Time
%dir %{perl_vendorarch}/auto/Time/HiRes
%{perl_vendorarch}/auto/Time/HiRes/HiRes.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Time/HiRes/HiRes.so
%{_mandir}/man3/*
