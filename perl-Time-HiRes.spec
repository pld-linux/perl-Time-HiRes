%define	pdir	Time
%define	pnam	HiRes
%include	/usr/lib/rpm/macros.perl
Summary:	Time-HiRes perl module
Summary(pl):	Modu³ perla Time-HiRes
Name:		perl-Time-HiRes
Version:	01.20
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Time-HiRes - High resolution ualarm, usleep, and gettimeofday.

%description -l pl
Time-HiRes to interfejs perla dla funkcji systemowych: ualarm, usleep
i gettimeofday.

%prep
%setup -q -n Time-HiRes-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Time/HiRes.pm
%dir %{perl_sitearch}/auto/Time/HiRes
%{perl_sitearch}/auto/Time/HiRes/HiRes.bs
%attr(755,root,root) %{perl_sitearch}/auto/Time/HiRes/HiRes.so
%{_mandir}/man3/*
