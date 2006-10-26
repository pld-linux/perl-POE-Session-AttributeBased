#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Session-AttributeBased
Summary:	POE::Session::AttributeBased - POE::Session using attributes marking state handlers
Summary(pl):	POE::Session::AttributeBased - POE::Session przy u�yciu atrybut�w z obs�ug� stan�w
Name:		perl-POE-Session-AttributeBased
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0f9b8de1dfce9f32a1607459414d5cb5
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

%description -l pl
Ten modu� Perla jest we wczesnym stadium alpha. Pakiet ten obudowuje
POE::Sessino i pozwala u�ywa� atrybut�w stan�w ('state') do okre�lania
obs�ugi stan�w. Podobn� funkcjonalno�� udost�pnia modu� Perla
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
