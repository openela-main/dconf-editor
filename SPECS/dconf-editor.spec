Name:           dconf-editor
Version:        3.28.0
Release:        1%{?dist}
Summary:        Configuration editor for dconf

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/dconf
Source0:        https://download.gnome.org/sources/dconf-editor/3.28/dconf-editor-%{version}.tar.xz

BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  vala

%description
Graphical tool for editing the dconf configuration database.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang dconf-editor

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/ca.desrt.dconf-editor.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/ca.desrt.dconf-editor.desktop

%files -f dconf-editor.lang
%license COPYING
%{_bindir}/dconf-editor
%{_datadir}/applications/ca.desrt.dconf-editor.desktop
%{_datadir}/bash-completion/
%{_datadir}/dbus-1/services/ca.desrt.dconf-editor.service
%{_datadir}/glib-2.0/schemas/ca.desrt.dconf-editor.gschema.xml
%{_datadir}/icons/hicolor/*/apps/ca.desrt.dconf-editor.png
%{_datadir}/icons/hicolor/scalable/apps/ca.desrt.dconf-editor-symbolic.svg
%{_datadir}/metainfo/ca.desrt.dconf-editor.appdata.xml
%{_mandir}/man1/dconf-editor.1*

%changelog
* Tue Mar 13 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Sun Mar 11 2018 Kalev Lember <klember@redhat.com> - 3.27.92-1
- Update to 3.27.92

* Tue Mar 06 2018 Kalev Lember <klember@redhat.com> - 3.27.91-1
- Update to 3.27.91
- Switch to the meson build system

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.2-2
- Remove obsolete scriptlets

* Wed Nov 01 2017 Kalev Lember <klember@redhat.com> - 3.26.2-1
- Update to 3.26.2

* Sun Oct 08 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 14 2017 Kalev Lember <klember@redhat.com> - 3.23.4-1
- Update to 3.23.4

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1

* Fri Sep 16 2016 Kalev Lember <klember@redhat.com> - 3.21.92-1
- Update to 3.21.92

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90

* Wed Jul 20 2016 Richard Hughes <rhughes@redhat.com> - 3.21.4-1
- Update to 3.21.4

* Tue May 03 2016 Kalev Lember <klember@redhat.com> - 3.21.1-1
- Update to 3.21.1

* Thu Apr 14 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Tue Mar 15 2016 Richard Hughes <rhughes@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Tue Mar 01 2016 Richard Hughes <rhughes@redhat.com> - 3.19.91-1
- Update to 3.19.91

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Kalev Lember <klember@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Tue Nov 24 2015 Kalev Lember <klember@redhat.com> - 3.19.2-1
- Update to 3.19.2

* Fri Nov 13 2015 Kalev Lember <klember@redhat.com> - 3.18.2-1
- Update to 3.18.2

* Mon Oct 12 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Tue Sep 15 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Tue Sep 01 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91

* Wed Aug 19 2015 Kalev Lember <klember@redhat.com> - 3.17.90-1
- Update to 3.17.90

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 01 2015 Kalev Lember <kalevlember@gmail.com> - 3.17.1-1
- Update to 3.17.1

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92
- Ship the man page

* Tue Mar 03 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-3
- Fix unowned HighContrast icon theme directories (#1197898)

* Tue Mar 03 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-2
- Fix appdata screenshot URL
- Validate appdata during %%check

* Mon Mar 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Initial Fedora packaging
