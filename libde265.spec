Name:       libde265
Summary:    Open H.265 video codec implementation
Version:    1.0.16
Release:    1%{?dist}
License:    LGPLv3+
URL:        https://www.libde265.org/

Source0:    https://github.com/strukturag/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    gcc
BuildRequires:    libtool
BuildRequires:    pkgconfig(libswscale)
BuildRequires:    pkgconfig(Qt5Core)
BuildRequires:    pkgconfig(Qt5Gui)
BuildRequires:    pkgconfig(sdl)

%description
%{name} is an open source implementation of the H.265 video codec.
It is written from scratch for simplicity and efficiency. Its simple API makes
it easy to integrate it into other software.

%package devel
Summary:    Open H.265 video codec implementation - development files
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
%{name} is an open source implementation of the H.265 video codec.
It is written from scratch for simplicity and efficiency. Its simple API makes
it easy to integrate it into other software.

The development headers for compiling programs that use %{name} are provided
by this package.

%package tools
License:    GPLv3+
Summary:    Open H.265 video codec implementation - examples
Obsoletes:  %{name}-samples < %{version}-%{release}
Provides:   %{name}-samples%{?_isa} = %{version}-%{release}

%description tools
%{name} is an open source implementation of the H.265 video codec.
It is written from scratch for simplicity and efficiency. Its simple API makes
it easy to integrate it into other software.

Various sample and test applications using %{name} are provided by this package.

%prep
%autosetup -p1

%build
autoreconf -vif
%configure --disable-silent-rules --disable-static --enable-encoder
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%files
%license COPYING
%doc AUTHORS
%{_libdir}/%{name}.so.0
%{_libdir}/%{name}.so.0.1.9

%files devel
%doc README.md
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%doc README.md
%{_bindir}/bjoentegaard
%{_bindir}/block-rate-estim
%{_bindir}/dec265
%{_bindir}/enc265
%{_bindir}/gen-enc-table
%{_bindir}/rd-curves
%{_bindir}/sherlock265
%{_bindir}/tests
%{_bindir}/yuv-distortion

%changelog
* Thu May 08 2025 Simone Caronni <negativo17@gmail.com> - 1.0.16-1
- Update to 1.0.16.

* Thu Mar 13 2025 Simone Caronni <negativo17@gmail.com> - 1.0.15^20250123gitb67f401-2
- Update to latest snapshot.
- Drop ldconfig_scriptlets.
- Trim changelog.

* Thu Dec 21 2023 Simone Caronni <negativo17@gmail.com> - 1.0.15-1
- Update to 1.0.15.

* Tue Nov 21 2023 Simone Caronni <negativo17@gmail.com> - 1.0.14-1
- Update to 1.0.14 even if not using CMake.

* Tue Nov 21 2023 Simone Caronni <negativo17@gmail.com> - 1.0.13-1
- Update to 1.0.13.

* Tue Jun 13 2023 Simone Caronni <negativo17@gmail.com> - 1.0.12-1
- Update to 1.0.12.

* Fri Feb 03 2023 Simone Caronni <negativo17@gmail.com> - 1.0.11-1
- Update to 1.0.11.
- Move all tools/samples in the tools subpackage.
