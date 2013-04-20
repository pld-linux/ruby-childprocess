# TODO
# - maybe clean wrong platform files?
%define	gem_name childprocess
Summary:	A simple and reliable gem for controlling external programs
Name:		ruby-%{gem_name}
Version:	0.3.7
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Source0-md5:	95c048433fefa1823cec8d913f7cdddf
URL:		http://github.com/jarib/childprocess
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	ruby-rspec
Requires:	ruby-ffi < 2
Requires:	ruby-ffi >= 1.0.6
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
Documentation for %{name}

%prep
%setup -q -n %{gem_name}-%{version}

%build
%if %{with tests}
rspec spec
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{ruby_vendorlibdir}/childprocess.rb
%{ruby_vendorlibdir}/childprocess
