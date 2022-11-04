#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.08.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kfind
Summary:	kfind
Name:		ka5-%{kaname}
Version:	22.08.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	06d44d145180abeb473409c5fb73a598
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-karchive-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kfilemetadata-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KFind can be used as a standalone search tool, launched by KRunner or
from your menu. It is also integrated into Konqueror as "Find File" in
the "Tools" menu. It allows you to find files by name, type or
content.

%description -l pl.UTF-8
KFind może używany jako samodzielny program, uruchamiany przez KRunnera
lub z menu. Jest też zintegrowany z Konquerorem jak "Find File" w menu
"Tools". Pozwala wyszukiwać pliki według nazwy, typu lub treści.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{lt,sr}
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfind
%{_desktopdir}/org.kde.kfind.desktop
%{_iconsdir}/hicolor/128x128/apps/kfind.png
%{_iconsdir}/hicolor/16x16/apps/kfind.png
%{_iconsdir}/hicolor/22x22/apps/kfind.png
%{_iconsdir}/hicolor/32x32/apps/kfind.png
%{_iconsdir}/hicolor/48x48/apps/kfind.png
%{_iconsdir}/hicolor/64x64/apps/kfind.png
%{_iconsdir}/hicolor/scalable/apps/kfind.svgz
%lang(ca) %{_mandir}/ca/man1/kfind.1*
%lang(de) %{_mandir}/de/man1/kfind.1*
%lang(es) %{_mandir}/es/man1/kfind.1*
%lang(fr) %{_mandir}/fr/man1/kfind.1*
%lang(it) %{_mandir}/it/man1/kfind.1*
%lang(lt) %{_mandir}/lt/man1/kfind.1*
%lang(C) %{_mandir}/man1/kfind.1*
%lang(nb) %{_mandir}/nb/man1/kfind.1*
%lang(nl) %{_mandir}/nl/man1/kfind.1*
%lang(pl) %{_mandir}/pl/man1/kfind.1*
%lang(pt) %{_mandir}/pt/man1/kfind.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kfind.1*
%lang(ru) %{_mandir}/ru/man1/kfind.1*
%lang(sr) %{_mandir}/sr/man1/kfind.1*
%lang(sv) %{_mandir}/sv/man1/kfind.1*
%lang(uk) %{_mandir}/uk/man1/kfind.1*
%{_datadir}/metainfo/org.kde.kfind.appdata.xml
%{_datadir}/qlogging-categories5/kfind.categories
