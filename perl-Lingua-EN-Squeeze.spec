%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Lingua-EN-Squeeze perl module
Summary(pl):	Modu� perla Lingua-EN-Squeeze
Name:		perl-Lingua-EN-Squeeze
Version:	1998.1204
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Lingua/Lingua-EN-Squeeze-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Lingua-EN-Squeeze - Shorten text to minimum syllables.

%description -l pl
Lingua-EN-Squeeze - skraca tekst w j�zyku angielskim do jak najmniejszej 
liczby sylab tak, by pozostawa� wci�� czytelny.

%prep
%setup -q -n Lingua-EN-Squeeze-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Lingua/EN/Squeeze
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/Lingua/EN/Squeeze.pm
%{perl_sitearch}/auto/Lingua/EN/Squeeze

%{_mandir}/man3/*
