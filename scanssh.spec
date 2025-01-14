%define _disable_lto 1

Summary:	Scans the given addresses and networks for running SSH servers
Name:		scanssh
Version:	2.1.2
Release:	2
License:	BSD
Group:		Networking/Other
Url:		https://www.monkey.org/~provos/scanssh/
Source0:	http://www.monkey.org/~provos/scanssh/%{name}-%{version}.tar.gz
Patch0:		scanssh-no-locincpth.patch
BuildRequires:	pcap-devel >= 0.9.5
BuildRequires:	libdnet-devel >= 1.7
BuildRequires:	pkgconfig(libevent)

%description
Scanssh scans the given addresses and networks for running SSH servers. It will
query their version number and displays the results in a list.

This program was originally written under OpenBSD as a personal measurement
tool. However, besides gathering statistics, it's also useful for other
purposes such as ensuring that all machines on your network run the latest SSH
versions, etc...

%prep
%autosetup -p2

%build
export CC=gcc
%configure

# work around --recheck
touch *

%make CFLAGS="%{optflags} -fPIC"

%install
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man1

install -m755 scanssh %{buildroot}%{_sbindir}
install -m644 scanssh.1 %{buildroot}%{_mandir}/man1
  
%files
%doc README.md
%{_sbindir}/scanssh
%{_mandir}/*/*

