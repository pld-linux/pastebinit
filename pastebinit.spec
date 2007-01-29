Summary:	Command line pastebin
Name:		pastebinit
Version:	0.6
Release:	0.1
License:	GPL v2+
Group:		Applications
Source0:	http://www.stgraber.org/download/projects/pastebin/%{name}-%{version}.py
# Source0-md5:	9e8702cd1beac3218c357c0ea08f6ab3
URL:		http://www.stgraber.org/?cat=5
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pastebinit is a really small piece of Python that acts as a Pastebin
client, you simply tell it a file or to read from the stdin and it
will paste the information on a Pastebin.

%prep
%setup -qcT
cp -a %{SOURCE0} %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pastebinit
