#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname childprocess
Summary:	A simple and reliable gem for controlling external programs
Name:		ruby-%{pkgname}
Version:	5.1.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	https://rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	8ca074e79409523c3c699648d7432303
URL:		https://github.com/enkessler/childprocess
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
BuildRequires:	ruby-rspec >= 3.0
BuildRequires:	ruby-yard
%endif
Requires:	ruby-ffi < 2
Requires:	ruby-ffi >= 1.0.11
Obsoletes:	ruby-childprocess-doc < %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This gem aims at being a simple and reliable solution for controlling
external programs running in the background on any Ruby / OS
combination.

%prep
%setup -q -n %{pkgname}-%{version}

rm lib/childprocess/windows.rb
rm -r lib/childprocess/windows

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
%doc README.md LICENSE CHANGELOG.md
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
