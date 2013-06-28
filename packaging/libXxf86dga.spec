Name:           libXxf86dga
Version:        1.1.3
Release:        1
License:        MIT
Summary:        X.Org X11 libXxf86dga runtime library
URL:            http://www.x.org
Group:          System/Libraries
Source:         %{name}-%{version}.tar.gz
Source1001: 	libXxf86dga.manifest
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xf86dgaproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)

%description
X.Org X11 libXxf86dga runtime library

%package devel
Summary:        X.Org X11 libXxf86dga development package
Group:          Development/Libraries
Requires:       %{name} = %{version}
Provides:       libxxf86dga-devel

%description devel
X.Org X11 libXxf86dga development package

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure

make %{?_smp_mflags}

%install
%make_install

%remove_docs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%license COPYING
%{_libdir}/libXxf86dga.so.1
%{_libdir}/libXxf86dga.so.1.0.0

%files devel
%manifest %{name}.manifest
%{_libdir}/libXxf86dga.so
%{_libdir}/pkgconfig/xxf86dga.pc
%{_includedir}/X11/extensions/xf86dga1.h
%{_includedir}/X11/extensions/Xxf86dga.h
