Epoch: 1
Name: null
Version: 2.1
Release: 80
Summary: A dummy package for bs testing purpose
Group: Development/Other
License: GPL

%description
Dummy package.

%package dummy
Group: Development/Other
Summary: Test package

%description dummy
A dummy subpackage.

%prep
%setup -D -T -n .

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

%post -p /bin/csh
echo "csh sux"

%files
%files dummy

