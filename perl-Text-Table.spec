#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Table
Summary:	Text::Table - Organize Data in Tables
Summary(pl.UTF-8):	Text::Table - organizowanie danych w tabelach
Name:		perl-Text-Table
Version:	1.124
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ea52bf0a1ca109c6612b42113c1d9142
BuildRequires:	perl-Text-Aligner
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Organization of data in table form is a time-honored and useful method
of data representation. While columns of data are trivially generated
by computer through formatted output, even simple tasks like keeping
titles aligned with the data columns are not trivial, and the one-shot
solutions one comes up with tend to be particularly hard to maintain.
Text::Table allows you to create and maintain tables that adapt to
alignment requirements as you use them.

%description -l pl.UTF-8
Organizowanie danych w postaci tabel jest szanującą czas i przydatną
metodą reprezentacji danych. Kiedy kolumny danych są trywialnie
wygenerowane przez komputer poprzez sformatowane wyjście, nawet proste
zadania, takie jak utrzymywanie tytułów wyrównanych z kolumnami
danych, nie są trywialne, a doraźne rozwiązania stają się trudne do
utrzymania. Text::Table pozwala na tworzenie i utrzymywanie tabel
adaptujących się podczas używania do wymagań dotyczących wyrównania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Text/Table.pm
%{_mandir}/man3/*
