%define realname   POE-Component-IKC

Name:		perl-%{realname}
Version:	0.2302
Release:	2
License:	GPL or Artistic
Group:		Development/Perl
Summary:	POE IKC proxy session
Url:		http://search.cpan.org/dist/%{realname}
Source:		http://www.cpan.org/modules/by-module/POE/%{realname}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(POE)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This is Inter-Kernel Communication for POE.  It is used to get events
from one POE kernel to another

%prep
%setup -q -n %{realname}-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.2200-2mdv2011.0
+ Revision: 655155
- rebuild for updated spec-helper

* Sat May 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.2200-1mdv2011.0
+ Revision: 373750
- new version

* Thu May 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.2102-1mdv2010.0
+ Revision: 373028
- update to new version 0.2102

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.2101-1mdv2010.0
+ Revision: 371732
- update to new version 0.2101

* Fri Nov 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.2002-1mdv2009.1
+ Revision: 307436
- update to new version 0.2002

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.2001-4mdv2009.0
+ Revision: 258271
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.2001-3mdv2009.0
+ Revision: 246325
- rebuild

* Thu Jan 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.2001-1mdv2008.1
+ Revision: 153999
- update to new version 0.2001

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 30 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.2000-1mdv2008.1
+ Revision: 114013
- update to new version 0.2000

* Mon Nov 19 2007 Jérôme Quelin <jquelin@mandriva.org> 0.1904-1mdv2008.1
+ Revision: 110499
- import perl-POE-Component-IKC


