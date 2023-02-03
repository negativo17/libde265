Name:       libde265
Summary:    Open H.265 video codec implementation
Version:    1.0.11
Release:    1%{?dist}
License:    LGPLv3+
URL:        https://www.libde265.org/

Source0:    https://github.com/strukturag/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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

%{?ldconfig_scriptlets}

%files
%license COPYING
%doc AUTHORS
%{_libdir}/%{name}.so.0
%{_libdir}/%{name}.so.0.1.4

%files devel
%doc README.md
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%doc README.md
%{_bindir}/acceleration_speed
%{_bindir}/bjoentegaard
%{_bindir}/block-rate-estim
%{_bindir}/dec265
%{_bindir}/enc265
%{_bindir}/gen-enc-table
%{_bindir}/hdrcopy
%{_bindir}/rd-curves
%{_bindir}/sherlock265
%{_bindir}/tests
%{_bindir}/yuv-distortion

%changelog
* Fri Feb 03 2023 Simone Caronni <negativo17@gmail.com> - 1.0.11-1
- Update to 1.0.11.
- Move all tools/samples in the tools subpackage.

* Tue Oct 25 2022 Simone Caronni <negativo17@gmail.com> - 1.0.9-1
- Update to 1.0.9.

* Wed Apr 06 2022 Simone Caronni <negativo17@gmail.com> - 1.0.8-3
- Rebuild for updated dependencies.

* Wed Apr 06 2022 Simone Caronni <negativo17@gmail.com> - 1.0.8-2
- Rebuild for updated dependencies.

* Sat Mar 19 2022 Simone Caronni <negativo17@gmail.com> - 1.0.8-1
- Update to 1.0.8.

* Sun Jan 19 2020 Simone Caronni <negativo17@gmail.com> - 1.0.5-1
- Update to 1.0.5.
- Update SPEC file and fix build with recent Qt and FFmpeg.

* Wed Sep 26 2018 Simone Caronni <negativo17@gmail.com> - 1.0.3-2
- Add gcc as build requirement.

* Fri Jun 29 2018 Simone Caronni <negativo17@gmail.com> - 1.0.3-1
- Update to 1.0.3.
- Clean up SPEC file.

* Thu Jun 09 2016 Simone Caronni <negativo17@gmail.com> - 1.0.2-3.503af19
- Update to lates snapshot.

* Sun Jun 05 2016 Simone Caronni <negativo17@gmail.com> - 1.0.2-2
- Clan up SPEC file.

* Tue May 31 2016 Joachim Bauch <bauch@struktur.de> - 1.0.2-1
- Initial version.
