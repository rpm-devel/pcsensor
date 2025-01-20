Summary: PCSensor
Name: pcsensor
Version: 1.0.1
Release: 1%{?dist}
License: GPLv2
Group: System Environment/Base
URL: http://casjaysdev.pro/
BuildArch: %BuildArch
BuildRequires: libusb-devel

Source0: pcsensor
Source1: 99-tempsensor.rules

%description
This package contains yum configuration for the casjaysdev.pro Linux Repository, as well as the public GPG keys used to sign packages.

%prep
%setup -c -T
%{__cp} -a %{SOURCE0} .
%{__cp} -a %{SOURCE1} .

# %build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dpm 0755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}
%{__install} -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/udev/rules.d/99-tempsensor.rules

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/%{name}
%{_sysconfdir}/udev/rules.d/99-tempsensor.rules

%changelog
* Tue Dec 18 2018 CasjaysDev <rpm-admin@rpm-devel.casjaysdev.pro> - 1.0.1
- Intitial Build

