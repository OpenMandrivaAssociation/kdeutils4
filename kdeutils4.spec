%define revision 706641

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%if %unstable
%define dont_strip 1
%endif

Name: kdeutils4
Summary: K Desktop Environment
Version: 3.92.0
Release: %mkrel 0.%revision.1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
%if %branch
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeutils-%version.%revision.tar.bz2
%else
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeutils-%version.tar.bz2
%endif
Buildroot:	%_tmppath/%name-%version-%release-root
BuildRequires: X11-devel
BuildRequires: openssl-devel
BuildRequires: libnet-snmp-devel
BuildRequires: gmp-devel
BuildRequires: kdelibs4-devel
BuildRequires: kdepimlibs4-devel
BuildRequires: libzip-devel
BuildRequires: kde4-macros
%py_requires -d
BuildConflicts: libxmms-devel
Requires: kde4-kcalc
Requires: kde4-kcharselect
Requires: kde4-kdessh
Requires: kde4-kdf
Requires: kde4-kfloppy
Requires: kde4-kgpg
Requires: kde4-khexedit
Requires: kde4-kjots
Requires: kde4-kmilo
Requires: kde4-kregexpeditor
Requires: kde4-ktimer
Requires: kde4-kwallet
Requires: kde4-superkaramba
Requires: kde4-sweeper

%description
%{name} metapackage.

%files
%defattr(-,root,root,-)
%doc README

#----------------------------------------------------------------------

%package core
Summary: %name core files
Group: Graphical desktop/KDE
Requires: kdelibs4-core

%description core
Core files for %{name}.

%files core
%defattr(-,root,root)
%_kde_iconsdir/*/*/*/*

#----------------------------------------------------------------------

%package -n kde4-kcalc
Summary: %{name} kcalc
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kcalc

%description -n kde4-kcalc
%{name} kcalc.

%files -n kde4-kcalc
%defattr(-,root,root)
%_kde_appsdir/kcalc
%_kde_appsdir/kconf_update
%_kde_bindir/kcalc
%_kde_datadir/applications/kde4/kcalc.desktop
%_kde_datadir/config.kcfg/kcalc.kcfg
%_kde_docdir/HTML/*/kcalc

#---------------------------------------------

%package -n kde4-kcharselect
Summary: %{name} kcharselect
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kcharselect

%description -n kde4-kcharselect
%{name} kcharselect.

%files -n kde4-kcharselect
%defattr(-,root,root)
%_kde_appsdir/kconf_update
%_kde_appsdir/kcharselect
%_kde_bindir/kcharselect
%_kde_datadir/applications/kde4/KCharSelect.desktop
%_kde_docdir/HTML/*/kcharselect

#---------------------------------------------

%package -n kde4-kdessh
Summary: %{name} kdessh
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kdessh

%description -n kde4-kdessh
%{name} kdessh.

%files -n kde4-kdessh
%defattr(-,root,root)
%_kde_bindir/kdessh

#---------------------------------------------

%package -n kde4-kdf
Summary: %{name} kdf
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kdf

%description -n kde4-kdf
%{name} kdf.

%files -n kde4-kdf
%defattr(-,root,root)
%_kde_appsdir/kdf
%_kde_bindir/kdf
%_kde_bindir/kwikdisk
%_kde_libdir/kde4/kcm_kdf.so
%_kde_datadir/applications/kde4/kdf.desktop
%_kde_datadir/applications/kde4/kwikdisk.desktop
%_kde_datadir/kde4/services/kcmdf.desktop
%_kde_docdir/HTML/*/kdf

#---------------------------------------------

%package -n kde4-kfloppy
Summary: %{name} kfloppy
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kfloppy

%description -n kde4-kfloppy
%{name} kfloppy.

%files -n kde4-kfloppy
%defattr(-,root,root)
%_kde_appsdir/konqueror
%_kde_bindir/kfloppy
%_kde_datadir/applications/kde4/KFloppy.desktop
%_kde_docdir/HTML/*/kfloppy

#---------------------------------------------

%package -n kde4-kgpg
Summary: %{name} kgpg
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kgpg

%description -n kde4-kgpg
%{name} kgpg.

%files -n kde4-kgpg
%defattr(-,root,root)
%_kde_appsdir/kgpg
%_kde_appsdir/konqueror
%_kde_bindir/kgpg
%_kde_datadir/applications/kde4/kgpg.desktop
%_kde_datadir/autostart/kgpg.desktop
%_kde_datadir/config.kcfg/kgpg.kcfg
%_datadir/dbus-1/interfaces/org.kde.kgpg.Key.xml
%_kde_docdir/HTML/*/kgpg

#---------------------------------------------

%package -n kde4-khexedit
Summary: %{name} khexedit
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-khexedit

%description -n kde4-khexedit
%{name} khexedit.

%files -n kde4-khexedit
%defattr(-,root,root)
%_kde_appsdir/khexedit
%_kde_appsdir/oktetapart
%_kde_bindir/khexedit
%_kde_libdir/kde4/libkbytearrayedit.so
%_kde_libdir/kde4/liboktetapart.so
%_kde_datadir/applications/kde4/khexedit.desktop
%_kde_datadir/kde4/services/kbytearrayedit.desktop
%_kde_datadir/kde4/services/oktetapart.desktop
%_kde_docdir/HTML/*/khexedit

#---------------------------------------------

%define liboktetagui %mklibname oktetagui 4

%package -n %liboktetagui
Summary: KDE 4 library
Group: System/Libraries

%description -n %liboktetagui
KDE 4 library

%post -n %liboktetagui -p /sbin/ldconfig
%postun -n %liboktetagui -p /sbin/ldconfig

%files -n %liboktetagui
%defattr(-,root,root)
%_kde_libdir/liboktetagui.so.*

#---------------------------------------------

%define liboktetacore %mklibname oktetacore 4

%package -n %liboktetacore
Summary: KDE 4 library
Group: System/Libraries

%description -n %liboktetacore
KDE 4 library

%post -n %liboktetacore -p /sbin/ldconfig
%postun -n %liboktetacore -p /sbin/ldconfig

%files -n %liboktetacore
%defattr(-,root,root)
%_kde_libdir/liboktetacore.so.*

#---------------------------------------------

%package -n kde4-kjots
Summary: %{name} kjots
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kjots

%description -n kde4-kjots
%{name} kjots.

%files -n kde4-kjots
%defattr(-,root,root)
%_kde_appsdir/kjots
%_kde_bindir/kjots
%_kde_datadir/applications/kde4/Kjots.desktop
%_kde_datadir/config.kcfg/kjots.kcfg
%_kde_docdir/HTML/*/kjots

#---------------------------------------------

%package -n kde4-kmilo
Summary: %{name} kmilo
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kmilo

%description -n kde4-kmilo
%{name} kmilo.

%files -n kde4-kmilo
%defattr(-,root,root)
%_kde_libdir/kde4/kcm_thinkpad.so
%_kde_libdir/kde4/kded_kmilod.so
%_kde_libdir/kde4/kmilo_asus.so
%_kde_libdir/kde4/kmilo_kvaio.so
%_kde_libdir/kde4/kmilo_thinkpad.so
%_kde_datadir/kde4/services/kded/kmilod.desktop
%_kde_datadir/kde4/services/kmilo/kmilo_asus.desktop
%_kde_datadir/kde4/services/kmilo/kmilo_kvaio.desktop
%_kde_datadir/kde4/services/kmilo/kmilo_thinkpad.desktop
%_kde_datadir/kde4/services/thinkpad.desktop
%_kde_datadir/kde4/servicetypes/kmilo/kmilopluginsvc.desktop
%_datadir/dbus-1/interfaces/org.kde.kmilod.xml

#---------------------------------------------

%define libkmilo %mklibname kmilo 4

%package -n %libkmilo
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkmilo
KDE 4 library

%post -n %libkmilo -p /sbin/ldconfig
%postun -n %libkmilo -p /sbin/ldconfig

%files -n %libkmilo
%defattr(-,root,root)
%_kde_libdir/libkmilo.so.*

#---------------------------------------------

%package -n kde4-kregexpeditor
Summary: %{name} kregexpeditor
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kregexpeditor

%description -n kde4-kregexpeditor
%{name} kregexpeditor.

%files -n kde4-kregexpeditor
%defattr(-,root,root)
%_kde_appsdir/kregexpeditor
%_kde_bindir/kregexpeditor
%_kde_libdir/kde4/libkregexpeditorgui.so
%_kde_datadir/applications/kde4/kregexpeditor.desktop
%_kde_datadir/kde4/services/kregexpeditorgui.desktop
%_kde_docdir/HTML/*/KRegExpEditor

#---------------------------------------------

%define libkregexpeditorcommon %mklibname kregexpeditorcommon 4

%package -n %libkregexpeditorcommon
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkregexpeditorcommon
KDE 4 library

%post -n %libkregexpeditorcommon -p /sbin/ldconfig
%postun -n %libkregexpeditorcommon -p /sbin/ldconfig

%files -n %libkregexpeditorcommon
%defattr(-,root,root)
%_kde_libdir/libkregexpeditorcommon.so.*

#---------------------------------------------

%package -n kde4-ktimer
Summary: %{name} ktimer
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-ktimer

%description -n kde4-ktimer
%{name} ktimer.

%files -n kde4-ktimer
%defattr(-,root,root)
%_kde_bindir/ktimer
%_kde_datadir/applications/kde4/ktimer.desktop
%_kde_docdir/HTML/*/ktimer

#---------------------------------------------

%package -n kde4-kwallet
Summary: %{name} kwallet
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kwallet

%description -n kde4-kwallet
%{name} kwallet.

%files -n kde4-kwallet
%defattr(-,root,root)
%_kde_appsdir/kwalletmanager
%_kde_bindir/kwalletmanager
%_kde_libdir/kde4/kcm_kwallet.so
%_kde_datadir/applications/kde4/kwalletmanager-kwalletd.desktop
%_kde_datadir/applications/kde4/kwalletmanager.desktop
%_kde_datadir/kde4/services/kwalletconfig.desktop
%_kde_datadir/kde4/services/kwalletmanager_show.desktop
%_kde_docdir/HTML/*/kwallet

#---------------------------------------------

%package -n kde4-superkaramba
Summary: %{name} superkaramba
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-superkaramba

%description -n kde4-superkaramba
%{name} superkaramba.

%files -n kde4-superkaramba
%defattr(-,root,root)
%_kde_appsdir/superkaramba
%_kde_bindir/superkaramba
%_kde_libdir/kde4/plasma_applet_skapplet.so
%_kde_datadir/applications/kde4/superkaramba.desktop
%_kde_datadir/config/superkaramba.knsrc
%_kde_datadir/kde4/services/plasma-skapplet-default.desktop
%_datadir/dbus-1/interfaces/org.kde.superkaramba.xml
%_kde_docdir/HTML/*/superkaramba

#---------------------------------------------

%package -n kde4-ark
Summary: %{name} ark
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-ark

%description -n kde4-ark
%{name} ark.

%files -n kde4-ark
%defattr(-,root,root)
%_kde_bindir/ark
%_kde_libdir/kde4/kerfuffle_bk.so
%_kde_libdir/kde4/libarkpart.so
%_kde_libdir/kde4/kerfuffle_*
%_kde_datadir/applications/kde4/ark.desktop
%_kde_appsdir/ark
%_kde_datadir/config.kcfg/ark.kcfg
%_kde_datadir/kde4/services/ark_part.desktop
%_kde_datadir/kde4/services/kerfuffle_*
%_kde_datadir/kde4/servicetypes/kerfufflePlugin.desktop
%_kde_docdir/HTML/*/ark

#---------------------------------------------

%define libkerfuffle %mklibname kerfuffle 4

%package -n %libkerfuffle
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkerfuffle
KDE 4 library

%post -n %libkerfuffle -p /sbin/ldconfig
%postun -n %libkerfuffle -p /sbin/ldconfig

%files -n %libkerfuffle
%defattr(-,root,root)
%_kde_libdir/libkerfuffle.so.*

#---------------------------------------------

%define libsuperkaramba %mklibname superkaramba 4

%package -n %libsuperkaramba
Summary: KDE 4 library
Group: System/Libraries

%description -n %libsuperkaramba
KDE 4 library

%post -n %libsuperkaramba -p /sbin/ldconfig
%postun -n %libsuperkaramba -p /sbin/ldconfig

%files -n %libsuperkaramba
%defattr(-,root,root)
%_kde_libdir/libsuperkaramba.so.*

#---------------------------------------------

%package -n kde4-sweeper
Summary: %{name} sweeper
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-sweeper

%description -n kde4-sweeper
%{name} sweeper.

%files -n kde4-sweeper
%defattr(-,root,root)
%_kde_appsdir/sweeper
%_kde_bindir/sweeper
%_kde_datadir/applications/kde4/sweeper.desktop
%_datadir/dbus-1/interfaces/org.kde.sweeper.xml

#---------------------------------------------

%package devel
Summary: Devel stuff for %{name}
Group: Development/KDE and Qt
Requires: kde4-macros
Requires: kdelibs4-devel
Requires: %liboktetagui = %version
Requires: %liboktetacore = %version
Requires: %libkmilo = %version
Requires: %libkregexpeditorcommon = %version
Requires: %libsuperkaramba = %version
%description  devel
This package contains header files needed if you wish to build applications based on %{name}.

%files devel
%defattr(-,root,root)
%_kde_libdir/*.so
%_kde_prefix/include/*

%prep
%setup -q -n kdeutils-%version

%build
%cmake_kde4 

%make

%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install

%clean
rm -fr %buildroot

