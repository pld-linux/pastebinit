Summary:	Command line Pastebin
Summary(pl.UTF-8):	Pastebin działający z linii poleceń
Name:		pastebinit
Version:	1.0
Release:	2
License:	GPL v2+
Group:		Applications
Source0:	http://launchpad.net/pastebinit/trunk/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	97c2a0b227240dcb8d6f4c66d7e3eb12
Patch0:		%{name}-configparsing.patch
Patch1:		%{name}-pastebin.com.patch
URL:		https://launchpad.net/pastebinit
BuildRequires:	gettext-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
Requires:	python-configobj
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pastebinit is a really small piece of Python that acts as a Pastebin
client, you simply tell it a file or to read from the stdin and it
will paste the information on a Pastebin.

%description -l pl.UTF-8
pastebinit to naprawdę mały kawałek kodu w Pythonie działający jako
klient Pastebin - wystarczy podać mu plik albo nakazać czytanie ze
standardowego wyjścia, a on przeklei informacje na Pastebin.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%{__sed} -i -e 's#http://pastebin.com#http://pld.pastebin.com#g' pastebinit

%build
%{__make} -C po

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/pastebin.d,%{_bindir},%{_datadir}/locale}
install -p pastebinit $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -a pastebin.d/*.conf $RPM_BUILD_ROOT%{_sysconfdir}/pastebin.d
cp -a po/mo/* $RPM_BUILD_ROOT%{_datadir}/locale

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pastebinit
%dir %{_sysconfdir}/pastebin.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pastebin.d/*.conf
