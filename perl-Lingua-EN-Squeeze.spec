%include	/usr/lib/rpm/macros.perl
%define		pdir	Lingua
%define		pnam	EN-Squeeze
Summary:	Lingua::EN::Squeeze perl module
Summary(pl):	Modu³ perla Lingua::EN::Squeeze
Name:		perl-Lingua-EN-Squeeze
Version:	2003.1003
Release:	1
# same as perl or GPL v2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b9348fcfaa964c6879711cd223635970
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua::EN::Squeeze - Shorten text to minimum syllables.

%description -l pl
Lingua::EN::Squeeze - skraca tekst w jêzyku angielskim do jak
najmniejszej liczby sylab tak, by pozostawa³ wci±¿ czytelny.

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
