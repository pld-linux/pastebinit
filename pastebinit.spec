Summary:	Command line Pastebin
Summary(pl.UTF-8):	Pastebin działający z linii poleceń
Name:		pastebinit
Version:	0.11
Release:	3
License:	GPL v2+
Group:		Applications
Source0:	http://www.stgraber.org/download/projects/pastebin/%{name}-%{version}.tar.gz
Patch0:		%{name}-anybin.patch
Patch1:		%{name}-configparsing.patch
# Source0-md5:	8342af2467545402922477a5710083f6
URL:		http://www.stgraber.org/category/pastebinit
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
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
%patch1 -p1
%{__sed} -i -e 's#http://pastebin.com#http://pld.pastebin.com#g' pastebinit

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install pastebinit $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pastebinit
