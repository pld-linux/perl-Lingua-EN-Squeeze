%define	pdir	Lingua
%define	pnam	EN-Squeeze
%include	/usr/lib/rpm/macros.perl
Summary:	Lingua-EN-Squeeze perl module
Summary(pl):	Modu� perla Lingua-EN-Squeeze
Name:		perl-Lingua-EN-Squeeze
Version:	1998.1204
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua-EN-Squeeze - Shorten text to minimum syllables.

%description -l pl
Lingua-EN-Squeeze - skraca tekst w j�zyku angielskim do jak
najmniejszej liczby sylab tak, by pozostawa� wci�� czytelny.

%prep
%setup -q -n Lingua-EN-Squeeze-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Lingua/EN/Squeeze.pm
%{_mandir}/man3/*
