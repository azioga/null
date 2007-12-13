Name: null
Version: 2
Release: %mkrel 7
Summary: A dummy package for bs testing purpose
Group: Development/Other
License: GPL
Buildroot: %{_tmppath}/%{name}-%{version}-root

%description
Dummy package.

%package dummy
Group: Development/Other
Summary: Test package

%description dummy
A dummy subpackage

%prep

%build
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

%clean
rm -rf %{buildroot}

%files
%files dummy
