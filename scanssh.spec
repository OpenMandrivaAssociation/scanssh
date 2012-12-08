Summary:	Scans the given addresses and networks for running SSH servers
Name:		scanssh
Version:	2.1
Release:	%mkrel 17
License:	BSD
Group:		Networking/Other
URL:		http://www.monkey.org/~provos/scanssh/
Source0:	http://www.monkey.org/~provos/scanssh/%{name}-%{version}.tar.bz2
Patch0:		scanssh-no-locincpth.patch
BuildRequires:	libpcap >= 0.9.5
BuildRequires:	libpcap-devel >= 0.9.5
BuildRequires:	libevent-devel >= 1.3
BuildRequires:	libdnet-devel >= 1.7
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Scanssh scans the given addresses and networks for running SSH servers. It will
query their version number and displays the results in a list.

This program was originally written under OpenBSD as a personal measurement
tool. However, besides gathering statistics, it's also useful for other
purposes such as ensuring that all machines on your network run the latest SSH
versions, etc...

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0 

%build

%configure2_5x

# work around --recheck
touch *

%make CFLAGS="%{optflags} -fPIC"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man1

install -m755 scanssh %{buildroot}%{_sbindir}
install -m644 scanssh.1 %{buildroot}%{_mandir}/man1
  
%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc README
%{_sbindir}/scanssh
%{_mandir}/*/*




%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1-15mdv2011.0
+ Revision: 669960
- mass rebuild

* Wed Dec 22 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1-14mdv2011.0
+ Revision: 623869
- rebuilt against libevent 2.x

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1-13mdv2011.0
+ Revision: 607512
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1-12mdv2010.1
+ Revision: 519069
- rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.1-11mdv2010.0
+ Revision: 427045
- rebuild

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 2.1-10mdv2009.1
+ Revision: 317142
- rebuild

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 2.1-9mdv2009.1
+ Revision: 298359
- rebuilt against libpcap-1.0.0

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.1-8mdv2009.0
+ Revision: 265656
- rebuild early 2009.0 package (before pixel changes)

* Wed May 14 2008 Oden Eriksson <oeriksson@mandriva.com> 2.1-7mdv2009.0
+ Revision: 207048
- rebuilt against libevent-1.4.4

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 2.1-6mdv2008.1
+ Revision: 179492
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Mar 07 2007 Oden Eriksson <oeriksson@mandriva.com> 2.1-5mdv2007.0
+ Revision: 134460
- Import scanssh

* Wed Mar 07 2007 Oden Eriksson <oeriksson@mandriva.com> 2.1-5mdv2007.1
- fix deps

* Mon Aug 14 2006 Emmanuel Andry <eandry@mandriva.org> 2.1-4mdv2007.0
- %%mkrel
- fix x86_64 build

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.1-3mdk
- Rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1-2mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Tue May 10 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1-1mdk
- 2.1

* Mon Dec 06 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0-4mdk
- rebuilt against new libevent

* Thu Sep 23 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.0-3mdk
- Rebuild

* Tue Jun 01 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0-2mdk
- rebuilt against new libdnet

* Mon May 03 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0-1mdk
- 2.0
- fix buildrequires
- use the %%configure2_5x macro

