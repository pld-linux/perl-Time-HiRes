%include	/usr/lib/rpm/macros.perl
Summary:	Time-HiRes perl module
Summary(pl):	Modu³ perla Time-HiRes
Name:		perl-Time-HiRes
Version:	01.20
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Time/Time-HiRes-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Time/HiRes/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Time/HiRes
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,TODO}.gz

%{perl_sitearch}/Time/HiRes.pm

%dir %{perl_sitearch}/auto/Time/HiRes
%{perl_sitearch}/auto/Time/HiRes/.packlist
%{perl_sitearch}/auto/Time/HiRes/HiRes.bs
%attr(755,root,root) %{perl_sitearch}/auto/Time/HiRes/HiRes.so

%{_mandir}/man3/*
