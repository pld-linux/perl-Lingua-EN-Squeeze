%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	EN-Squeeze
Summary:	Lingua::EN::Squeeze perl module
Summary(pl):	Modu� perla Lingua::EN::Squeeze
Name:		perl-Lingua-EN-Squeeze
Version:	1998.1204
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a7860f69fcae17ee2ef311730599480e
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua::EN::Squeeze - Shorten text to minimum syllables.

%description -l pl
Lingua::EN::Squeeze - skraca tekst w j�zyku angielskim do jak
najmniejszej liczby sylab tak, by pozostawa� wci�� czytelny.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Lingua/EN/Squeeze.pm
%{_mandir}/man3/*
