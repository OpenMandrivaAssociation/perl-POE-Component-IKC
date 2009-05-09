
%define realname   POE-Component-IKC
%define version    0.2200
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    POE IKC proxy session
Url:        http://search.cpan.org/dist/%{realname}
Source:     http://www.cpan.org/modules/by-module/POE/%{realname}-%{version}.tar.gz
BuildRequires: perl(POE)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(POE::API::Peek)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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



