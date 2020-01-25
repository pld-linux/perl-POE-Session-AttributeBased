#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	POE
%define		pnam	Session-AttributeBased
Summary:	POE::Session::AttributeBased - POE::Session using attributes marking state handlers
Summary(pl.UTF-8):	POE::Session::AttributeBased - POE::Session przy użyciu atrybutów z obsługą stanów
Name:		perl-POE-Session-AttributeBased
Version:	0.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	82aafcc8a8add3040dae78dbfe42f107
URL:		http://search.cpan.org/dist/POE-Session-AttributeBased/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-POE
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl module is early alpha code. This package wraps POE::Session
and permits use of a 'state' attributes to designate state handlers.
Similar functionality is provided by POE::Session::Attribute Perl
module.

%description -l pl.UTF-8
Ten moduł Perla jest we wczesnym stadium alpha. Pakiet ten obudowuje
POE::Sessino i pozwala używać atrybutów stanów ('state') do określania
obsługi stanów. Podobną funkcjonalność udostępnia moduł Perla
POE::Session::Attribute.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Session/AttributeBased.pm
%{_mandir}/man3/*
