%include	/usr/lib/rpm/macros.perl
%define		pdir	Time
%define		pnam	HiRes
Summary:	Time::HiRes Perl module
Summary(cs):	Modul Time::HiRes pro Perl
Summary(da):	Perlmodul Time::HiRes
Summary(de):	Time::HiRes Perl Modul
Summary(es):	Módulo de Perl Time::HiRes
Summary(fr):	Module Perl Time::HiRes
Summary(it):	Modulo di Perl Time::HiRes
Summary(ja):	Time::HiRes Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Time::HiRes ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Time::HiRes
Summary(pl):	Modu³ Perla Time::HiRes
Summary(pt):	Módulo de Perl Time::HiRes
Summary(pt_BR):	Módulo Perl Time::HiRes
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Time::HiRes
Summary(sv):	Time::HiRes Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Time::HiRes
Summary(zh_CN):	Time::HiRes Perl Ä£¿é
Name:		perl-Time-HiRes
Version:	01.20
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Time::HiRes - High resolution ualarm, usleep, and gettimeofday.

%description -l pl
Time::HiRes to interfejs perla dla funkcji systemowych: ualarm, usleep
i gettimeofday.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

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
