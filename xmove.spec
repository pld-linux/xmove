Summary:	An X11 pseudoserver for moving windows between displays
Name:		xmove
%define	_beta 2
Version:	2.0
Release:	0.%{_beta}.1
Epoch:		0
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		X11/Servers
Source0:	ftp://ftp.cs.columbia.edu/pub/xmove/%{name}.%{version}beta%{_beta}.tar.gz
# Source0-md5:	d70107f7835b755bd4f57b47a8ac7b38
URL:		ftp://ftp.cs.columbia.edu/pub/xmove/
BuildRequires:	X11-imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmove lets you change which display an X Window System program renders
to - this could be a different monitor or even a different machine.

%prep
%setup -q -n %{name}

%build
cd xmove
xmkmf
%{__make} xmove
cd ..
cd xmovectrl
%{__make} xmovectrl
xmkmf
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install xmove/xmove xmovectrl/xmovectrl $RPM_BUILD_ROOT%{_bindir}
install man/man1/xmove*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
