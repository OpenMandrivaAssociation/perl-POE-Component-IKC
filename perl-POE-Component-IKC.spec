
%define realname   POE-Component-IKC
%define version    0.2001
%define release    %mkrel 3

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    POE IKC proxy session
Source:     http://www.cpan.org/modules/by-module/POE/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(POE)
BuildRequires: perl(Scalar::Util)

BuildArch: noarch

%description
This is Inter-Kernel Communication for POE.  It is used to get events
from one POE kernel to another



%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*



