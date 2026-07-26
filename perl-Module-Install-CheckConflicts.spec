%define upstream_name    Module-Install-CheckConflicts
Name:		perl-%{upstream_name}
Version:	0.02
Release:	7

Summary:	Notify users of possible conflicts with the distribution they're installing
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Module-Install-CheckConflicts
Source0:	https://cpan.metacpan.org/authors/id/F/FL/FLORA/Module-Install-CheckConflicts-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildArch:	noarch

%description
Sometimes APIs need to be broken in incompatible ways. That's fine, as long
as all dependencies that relied on the old way have been updated already.
If users install install a new version of your module, but aren't aware
that they need to update other modules that might have been broken by that
new version, they'll be left with a non-functional installation of those
depending modules.

This module allows to declare modules your distribution breaks in your
'Makefile.PL'. If a user is installing your distribution, a message
explaining the situation and a list of additional modules he needs to
upgrade will presented.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 656940
- rebuild for updated spec-helper

* Fri Dec 03 2010 Shlomi Fish <shlomif@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 607077
- import perl-Module-Install-CheckConflicts

