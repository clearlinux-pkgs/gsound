#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : gsound
Version  : 1.0.3
Release  : 11
URL      : https://download.gnome.org/sources/gsound/1.0/gsound-1.0.3.tar.xz
Source0  : https://download.gnome.org/sources/gsound/1.0/gsound-1.0.3.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: gsound-bin = %{version}-%{release}
Requires: gsound-data = %{version}-%{release}
Requires: gsound-lib = %{version}-%{release}
Requires: gsound-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(libcanberra)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
GSound
======
What is it?
-----------
GSound is a small library for playing system sounds. It's designed to be
used via GObject Introspection, and is a thin wrapper around the [libcanberra](http://0pointer.de/lennart/projects/libcanberra/) C library.

%package bin
Summary: bin components for the gsound package.
Group: Binaries
Requires: gsound-data = %{version}-%{release}
Requires: gsound-license = %{version}-%{release}

%description bin
bin components for the gsound package.


%package data
Summary: data components for the gsound package.
Group: Data

%description data
data components for the gsound package.


%package dev
Summary: dev components for the gsound package.
Group: Development
Requires: gsound-lib = %{version}-%{release}
Requires: gsound-bin = %{version}-%{release}
Requires: gsound-data = %{version}-%{release}
Provides: gsound-devel = %{version}-%{release}
Requires: gsound = %{version}-%{release}

%description dev
dev components for the gsound package.


%package lib
Summary: lib components for the gsound package.
Group: Libraries
Requires: gsound-data = %{version}-%{release}
Requires: gsound-license = %{version}-%{release}

%description lib
lib components for the gsound package.


%package license
Summary: license components for the gsound package.
Group: Default

%description license
license components for the gsound package.


%prep
%setup -q -n gsound-1.0.3
cd %{_builddir}/gsound-1.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680033487
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gsound
cp %{_builddir}/gsound-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gsound/070409dd4c0816a175241e6b8c7d9d5649222cce || :
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gsound-play

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GSound-1.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/gsound.deps
/usr/share/vala/vapi/gsound.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/gsound-attr.h
/usr/include/gsound-context.h
/usr/include/gsound.h
/usr/lib64/libgsound.so
/usr/lib64/pkgconfig/gsound.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgsound.so.0
/usr/lib64/libgsound.so.0.0.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gsound/070409dd4c0816a175241e6b8c7d9d5649222cce
