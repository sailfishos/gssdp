Name:          gssdp
Version:       0.14.7
Release:       1%{?dist}
Summary:       Resource discovery and announcement over SSDP

Group:         System Environment/Libraries
License:       LGPLv2+
URL:           http://www.gupnp.org/
Source0:       http://download.gnome.org/sources/%{name}/0.14/%{name}-%{version}.tar.xz

BuildRequires: dbus-glib-devel
BuildRequires: glib2-devel
BuildRequires: libsoup-devel
BuildRequires: libxml2-devel
BuildRequires: pkgconfig

Requires: dbus

%description
GSSDP implements resource discovery and announcement over SSDP and is part 
of gUPnP.  GUPnP is an object-oriented open source framework for creating 
UPnP devices and control points, written in C using GObject and libsoup. The 
GUPnP API is intended to be easy to use, efficient and flexible.

%package devel
Summary: Development package for gssdp
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libsoup-devel
Requires: glib2-devel
Requires: pkgconfig

%description devel
Files for development with gssdp.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
autoreconf -v --install
%configure --disable-static

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libgssdp-1.0.so.*

%files devel
%{_libdir}/libgssdp-1.0.so
%{_libdir}/pkgconfig/gssdp-1.0.pc
%{_includedir}/gssdp-1.0
