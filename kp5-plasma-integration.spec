#
# Conditional build:
%bcond_with	tests		# build with tests
# TODO:
# PackageKit qt5
#
%define		kdeplasmaver	5.27.12
%define		qtver		5.15.2
%define		kpname		plasma-integration

Summary:	KDE Plasma Integration
Name:		kp5-%{kpname}
Version:	5.27.12
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	ce7f047c882d3d06fd5aedd76d8807cf
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Quick-controls2-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
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
BuildRequires:	kf5-kwayland-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	kp5-breeze-devel
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

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest
%endif

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
%attr(755,root,root) %{_libdir}/qt5/plugins/platforminputcontexts/plasmaimplatforminputcontextplugin.so
%{_datadir}/kconf_update/fonts_akregator.pl
%{_datadir}/kconf_update/fonts_akregator.upd
%{_datadir}/kconf_update/fonts_global.pl
%{_datadir}/kconf_update/fonts_global.upd
%{_datadir}/kconf_update/fonts_global_toolbar.upd
%{_datadir}/kconf_update/fonts_kate.pl
%{_datadir}/kconf_update/fonts_kate.upd

%files devel
%defattr(644,root,root,755)
%{_includedir}/PlasmaKeyData
%{_pkgconfigdir}/plasma-key-data.pc
