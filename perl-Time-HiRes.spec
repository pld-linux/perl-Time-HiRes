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
Version:	1.59
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	60ebc9d277108577d7e2a3a15ce65fd6
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
# remove the line below if you *really* have newer version than one
# available in perl-modules
BuildRequires:	this-must-be-newer-version-than-in-perl-modules
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
%{perl_vendorarch}/%{pdir}
%dir %{perl_vendorarch}/auto/%{pdir}
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/%{pnam}.bs
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/%{pnam}.so
%{_mandir}/man3/*
