#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gsound
Version  : 1.0.2
Release  : 3
URL      : https://download.gnome.org/sources/gsound/1.0/gsound-1.0.2.tar.xz
Source0  : https://download.gnome.org/sources/gsound/1.0/gsound-1.0.2.tar.xz
Summary  : Small library for playing system sounds
Group    : Development/Tools
License  : LGPL-2.1
Requires: gsound-bin = %{version}-%{release}
Requires: gsound-data = %{version}-%{release}
Requires: gsound-lib = %{version}-%{release}
Requires: gsound-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(libcanberra)

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


%package doc
Summary: doc components for the gsound package.
Group: Documentation

%description doc
doc components for the gsound package.


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
%setup -q -n gsound-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557009431
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1557009431
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gsound
cp COPYING %{buildroot}/usr/share/package-licenses/gsound/COPYING
%make_install

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
/usr/include/*.h
/usr/lib64/libgsound.so
/usr/lib64/pkgconfig/gsound.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/gsound/GSoundContext.html
/usr/share/gtk-doc/html/gsound/annotation-glossary.html
/usr/share/gtk-doc/html/gsound/api-index-full.html
/usr/share/gtk-doc/html/gsound/ch01.html
/usr/share/gtk-doc/html/gsound/deprecated-api-index.html
/usr/share/gtk-doc/html/gsound/gsound-GSound-Attributes.html
/usr/share/gtk-doc/html/gsound/gsound.devhelp2
/usr/share/gtk-doc/html/gsound/home.png
/usr/share/gtk-doc/html/gsound/index.html
/usr/share/gtk-doc/html/gsound/index.sgml
/usr/share/gtk-doc/html/gsound/left-insensitive.png
/usr/share/gtk-doc/html/gsound/left.png
/usr/share/gtk-doc/html/gsound/object-tree.html
/usr/share/gtk-doc/html/gsound/right-insensitive.png
/usr/share/gtk-doc/html/gsound/right.png
/usr/share/gtk-doc/html/gsound/style.css
/usr/share/gtk-doc/html/gsound/up-insensitive.png
/usr/share/gtk-doc/html/gsound/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgsound.so.0
/usr/lib64/libgsound.so.0.0.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gsound/COPYING
