Name: debhelper
Version: 9.20120909
Summary: debhelper

Group: devel
License: gpl
BuildRequires: po4a
Source0: debhelper.tar.gz

Requires: po4a

%description
debhelper


%prep
export PATH=$PATH:$RPM_BUILD_DIR
tar zxf $RPM_SOURCE_DIR/*tar.gz -C $RPM_BUILD_DIR

%build
cd $RPM_BUILD_DIR
debian/rules clean
debian/rules build
debian/rules binary

ls -lR $RPM_BUILD_DIR

%clean
rm -rf $RPM_BUILD_ROOT
