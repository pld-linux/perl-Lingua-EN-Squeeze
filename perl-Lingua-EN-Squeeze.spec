%define		pdir	Lingua
%define		pnam	EN-Squeeze
Summary:	Lingua::EN::Squeeze perl module
Summary(pl.UTF-8):	Moduł perla Lingua::EN::Squeeze
Name:		perl-Lingua-EN-Squeeze
Version:	2006.0704
Release:	1
# same as perl or GPL v2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1428d6e2fdce88b625bba291d5619096
URL:		http://search.cpan.org/dist/Lingua-EN-Squeeze/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua::EN::Squeeze - Shorten text to minimum syllables.

%description -l pl.UTF-8
Lingua::EN::Squeeze - skraca tekst w języku angielskim do jak
najmniejszej liczby sylab tak, by pozostawał wciąż czytelny.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} \
	install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Lingua/EN/Squeeze.pm
%{_mandir}/man3/*
