Name:          gssdp
Version:       1.3.0
Release:       1
Summary:       Resource discovery and announcement over SSDP

License:       LGPLv2+
URL:           http://www.gupnp.org/
Source0:       %{name}-%{version}.tar.xz

BuildRequires: pkgconfig
BuildRequires: meson
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 1.36
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(libvala-0.46)

%description
GSSDP implements resource discovery and announcement over SSDP and is part 
of gUPnP.  GUPnP is an object-oriented open source framework for creating 
UPnP devices and control points, written in C using GObject and libsoup. The 
GUPnP API is intended to be easy to use, efficient and flexible.

%package devel
Summary: Development package for gssdp
Requires: %{name} = %{version}-%{release}

%description devel
Files for development with gssdp.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
%meson -Dexamples=false -Dsniffer=false
%meson_build

%install

%meson_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/libgssdp-*.so.*
%{_libdir}/girepository-1.0/GSSDP-*.typelib

%files devel
%{_libdir}/libgssdp-*.so
%{_libdir}/pkgconfig/gssdp-*.pc
%{_includedir}/gssdp-*
%{_datadir}/gir-1.0/GSSDP-*.gir
%{_datadir}/vala/vapi/gssdp*
