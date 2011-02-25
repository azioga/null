Epoch: 1
Name: null
Version: 2.1
Release: 38
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
%setup -D -T -n .

%build
## to allow watching packages during their build time
##sleep 10m

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

%clean
rm -rf %{buildroot}

%post -p /bin/csh
echo "csh sux"

%files
%files dummy

