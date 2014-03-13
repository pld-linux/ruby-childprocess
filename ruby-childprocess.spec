# TODO
# - maybe clean wrong platform files?
#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname childprocess
Summary:	A simple and reliable gem for controlling external programs
Name:		ruby-%{pkgname}
Version:	0.5.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	195ada0b8ac5264be9b3df3416f3462a
URL:		http://github.com/jarib/childprocess
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
BuildRequires:	ruby-rake < 0.10
BuildRequires:	ruby-rake >= 0.9.2
BuildRequires:	ruby-rspec >= 2.0.0
BuildRequires:	ruby-yard
%endif
Requires:	ruby-ffi < 2
Requires:	ruby-ffi >= 1.0.11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This gem aims at being a simple and reliable solution for controlling
external programs running in the background on any Ruby / OS
combination.

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%__gem_helper spec

%if %{with tests}
rspec spec
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
