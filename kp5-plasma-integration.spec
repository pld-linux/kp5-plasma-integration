# TODO:
# PackageKit qt5
#
%define		kdeplasmaver	5.15.3
%define		qtver		5.9.0
%define		kpname		plasma-integration

Summary:	KDE Plasma Integration
Name:		kp5-%{kpname}
Version:	5.15.3
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	509f18cd766b6a63de42eaf3d8d91946
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	fontconfig-devel
BuildRequires:	kf5-attica-devel
BuildRequires:	kf5-kactivities-stats-devel
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kglobalaccel-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-kpeople-devel
BuildRequires:	kf5-krunner-devel
BuildRequires:	kf5-kwallet-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xorg-driver-input-evdev-devel
BuildRequires:	xorg-driver-input-synaptics-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KDE Plasma Integration.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/platformthemes/KDEPlasmaPlatformTheme.so
%{_datadir}/kconf_update/fonts_akregator.pl
%{_datadir}/kconf_update/fonts_akregator.upd
%{_datadir}/kconf_update/fonts_global.pl
%{_datadir}/kconf_update/fonts_global.upd
%{_datadir}/kconf_update/fonts_global_toolbar.upd
%{_datadir}/kconf_update/fonts_kate.pl
%{_datadir}/kconf_update/fonts_kate.upd
