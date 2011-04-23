%define upstream_name    Module-Install-CheckConflicts
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Notify users of possible conflicts with the distribution they're installing
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


