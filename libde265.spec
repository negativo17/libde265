Name:       libde265
Summary:    Open H.265 video codec implementation
Version:    1.0.2
Release:    2%{?dist}
License:    LGPLv3+
URL:        http://www.libde265.org/

Source:     https://github.com/strukturag/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    libtool
BuildRequires:    pkgconfig(libswscale)
BuildRequires:    pkgconfig(QtCore)
BuildRequires:    pkgconfig(QtGui)
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

%package examples
License:    GPLv3+
Summary:    Open H.265 video codec implementation - examples
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description examples
%{name} is an open source implementation of the H.265 video codec.
It is written from scratch for simplicity and efficiency. Its simple API makes
it easy to integrate it into other software.

Sample applications using %{name} are provided by this package.

%prep
%autosetup

%build
autoreconf -vif
%configure --disable-silent-rules --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name '*.a' -delete
find %{buildroot} -type f -name '*.la' -exec rm -f {} \;
#mv %{buildroot}%{_bindir}/dec265 %{buildroot}%{_bindir}/libde265-dec265
#mv %{buildroot}%{_bindir}/sherlock265 %{buildroot}%{_bindir}/libde265-sherlock265
# Don't package internal development tools.
rm %{buildroot}%{_bindir}/bjoentegaard
rm %{buildroot}%{_bindir}/block-rate-estim
rm %{buildroot}%{_bindir}/enc265
rm %{buildroot}%{_bindir}/gen-enc-table
rm %{buildroot}%{_bindir}/hdrcopy
rm %{buildroot}%{_bindir}/rd-curves
rm %{buildroot}%{_bindir}/tests
rm %{buildroot}%{_bindir}/yuv-distortion

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS
%{_libdir}/*.so.*

%files devel
%doc README.md
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files examples
%doc README.md
%{_bindir}/dec265
%{_bindir}/sherlock265

%changelog
* Sun Jun 05 2016 Simone Caronni <negativo17@gmail.com> - 1.0.2-2
- Clan up SPEC file.

* Tue May 31 2016 Joachim Bauch <bauch@struktur.de> - 1.0.2-1
- Initial version.
