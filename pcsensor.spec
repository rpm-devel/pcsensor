Summary: PCSensor USB temperature sensor tool
Name: pcsensor
Version: 1.0.1
Release: 1%{?dist}
License: GPL-2.0-only
URL: http://casjaysdev.pro/
ExclusiveArch: x86_64 aarch64
%if 0%{?suse_version}
%global libusb_devel_pkg libusb-compat-devel
%else
%global libusb_devel_pkg libusb-devel
%endif
BuildRequires: %{libusb_devel_pkg}

Source0: pcsensor
Source1: 99-tempsensor.rules

%description
PCSensor reads temperature data from TEMPer USB sensors.

%prep
%setup -c -T
%{__cp} -a %{SOURCE0} .
%{__cp} -a %{SOURCE1} .

# %build

%install
%{__install} -Dpm 0755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}
%{__install} -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/udev/rules.d/99-tempsensor.rules

%files
%{_bindir}/%{name}
%{_sysconfdir}/udev/rules.d/99-tempsensor.rules

%changelog
* Sat Jul 05 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 1.0.1-2
- Guard libusb-devel BuildRequires: binary links libusb-0.1.so.4 (libusb
  0.1 API), whose devel package is named libusb-compat-devel on
  openSUSE/SLES vs libusb-devel on RHEL/Fedora; add suse_version guard

* Thu Jul 03 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 1.0.1-2
- SPDX: GPLv2 -> GPL-2.0-only; remove deprecated rm -rf %%{buildroot}

* Fri Apr 24 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 1.0.1-2
- Fix BuildArch for EL10 (use ExclusiveArch x86_64 aarch64)
- Remove deprecated Group, %clean, %defattr

* Tue Dec 18 2018 CasjaysDev <rpm-admin@rpm-devel.casjaysdev.pro> - 1.0.1
- Intitial Build
