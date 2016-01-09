%define		pkg	fstream
Summary:	Advanced file system stream things
Name:		nodejs-%{pkg}
Version:	0.1.29
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/fstream/-/%{pkg}-%{version}.tgz
# Source0-md5:	fa9862a8ba9c8d27c06b2ce0565d5b47
URL:		https://github.com/isaacs/fstream
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-graceful-fs < 3.1
Requires:	nodejs-graceful-fs >= 3.0.2
Requires:	nodejs-inherits < 2.1.0
Requires:	nodejs-inherits >= 2.0.0
Requires:	nodejs-mkdirp < 0.4
Requires:	nodejs-mkdirp >= 0.3
Requires:	nodejs-rimraf < 3
Requires:	nodejs-rimraf >= 2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Advanced file system stream things.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr lib %{pkg}.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
%{_examplesdir}/%{name}-%{version}
