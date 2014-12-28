Summary:	Command line Pastebin
Summary(pl.UTF-8):	Pastebin działający z linii poleceń
Name:		pastebinit
Version:	1.4.1
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://launchpad.net/pastebinit/trunk/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	cfa3337ee9acb1f0b02e952b879f63a7
Patch0:		env-pastebin.patch
URL:		https://launchpad.net/pastebinit
BuildRequires:	gettext-tools
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
%patch0 -p1

%{__sed} -i -e '1s,^#!.*python,#!%{__python},' pastebinit

%build
%{__make} -C po

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/pastebin.d,%{_bindir},%{_datadir}/locale}
install -p pastebinit $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -p pastebin.d/*.conf $RPM_BUILD_ROOT%{_sysconfdir}/pastebin.d
cp -a po/mo/* $RPM_BUILD_ROOT%{_datadir}/locale

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pastebinit
%dir %{_sysconfdir}/pastebin.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pastebin.d/*.conf
