Name: kdeutils4
Summary: K Desktop Environment
Version: 4.0.82
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
Release: %mkrel 1
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeutils-%version.tar.bz2
Buildroot:	%_tmppath/%name-%version-%release-root
BuildRequires: X11-devel
BuildRequires: openssl-devel
BuildRequires: libnet-snmp-devel
BuildRequires: gmp-devel
BuildRequires: kdebase4-workspace-devel
BuildRequires: kdepimlibs4-devel
BuildRequires: libzip-devel
BuildRequires: kde4-macros
BuildRequires: qimageblitz-devel 
BuildRequires: libarchive-devel 
BuildRequires: kdepim4-devel
%ifarch %{ix86}
BuildRequires: tpctl-devel
%endif
%py_requires -d
BuildConflicts: libxmms-devel
Requires: kcalc
Requires: kcharselect
Requires: kdessh
Requires: kdf
Requires: kfloppy
Requires: kgpg
Requires: ktimer
Requires: kwallet
Requires: superkaramba
Requires: sweeper
Obsoletes: kde4-kjots < 4.0.68
Obsoletes: kjots < 4.0.80

%description
%{name} metapackage.

%files
%defattr(-,root,root,-)
%doc README

#----------------------------------------------------------------------

%package     core
Summary:     %name core files
Group:       Graphical desktop/KDE
Requires:    kdelibs4-core
Conflicts:   kdeutils-kcalc < 3.5.9-3
Conflicts:   kdeutils-kgpg  < 3.5.9-3
Conflicts:   kdeutils-kwalletmanager < 3.5.9-3
Conflicts:   kdeutils-ktimer < 3.5.9-3
Conflicts:   kdeutils-kfloppy < 3.5.9-3
Obsoletes:   kde4-kmilo < 4.0.74-1
Obsoletes:   %{_lib}kmilo4 < 4.0.74-1
Obsoletes:   kdeutils4-kmilo < 4.0.74-1
Obsoletes:   kmilo < 4.0.74-1
Obsoletes:   kdeutils4-kedit

%description core
Core files for %{name}.

%files core
%defattr(-,root,root)
%_kde_iconsdir/*/*/*/*

#----------------------------------------------------------------------

%package -n     kcalc
Summary:        %{name} kcalc
Group:          Graphical desktop/KDE
Requires:       %name-core = %version
Obsoletes:      %name-kcalc < 3.93.0-0.714053.1
Obsoletes:      kde4-kcalc < 4.0.68
Provides:       kde4-kcalc = %version
Conflicts:      kdeutils-kcalc < 3.5.9-3

%description -n kcalc
%{name} kcalc.

%files -n kcalc
%defattr(-,root,root)
%_kde_appsdir/kcalc
%_kde_appsdir/kconf_update
%_kde_bindir/kcalc
%_kde_datadir/applications/kde4/kcalc.desktop
%_kde_datadir/config.kcfg/kcalc.kcfg
%_kde_docdir/HTML/*/kcalc
%_kde_libdir/libkdeinit4_kcalc.so

#---------------------------------------------

%package printer-applet
Summary: Printer applet for KDE4
Group: Graphical desktop/KDE
Requires: %name-core = %version
Requires: system-config-printer
Requires: python-kde4
Requires: python-cups
Requires: python-qt4
Requires: hal-cups-utils

%description    printer-applet
Printer applet for KDE4

%files printer-applet
%defattr(-,root,root)
%_kde_bindir/printer-applet
%_kde_appsdir/printer-applet
%_kde_datadir/autostart/printer-applet.desktop

#---------------------------------------------


%package -n kcharselect
Summary: %{name} kcharselect
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kcharselect < 3.93.0-0.714053.1
Obsoletes:      kde4-kcharselect < 4.0.68
Provides:       kde4-kcharselect = %version

%description -n kcharselect
%{name} kcharselect.

%files -n kcharselect
%defattr(-,root,root)
%_kde_appsdir/kconf_update
%_kde_appsdir/kcharselect
%_kde_bindir/kcharselect
%_kde_datadir/applications/kde4/KCharSelect.desktop
%_kde_docdir/HTML/*/kcharselect

#---------------------------------------------

%package -n kdessh
Summary: %{name} kdessh
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kdessh < 3.93.0-0.714053.1
Obsoletes:      kde4-kdessh < 4.0.68
Provides:       kde4-kdessh = %version

%description -n kdessh
%{name} kdessh.

%files -n kdessh
%defattr(-,root,root)
%_kde_bindir/kdessh

#---------------------------------------------

%package -n kdf
Summary: %{name} kdf
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kdf < 3.93.0-0.714053.1
Obsoletes:      kde4-kdf < 4.0.68
Provides:       kde4-kdf = %version

%description -n kdf
%{name} kdf.

%files -n kdf
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

%package -n kfloppy
Summary: %{name} kfloppy
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kfloppy < 3.93.0-0.714053.1
Obsoletes:      kde4-kfloppy < 4.0.68
Provides:       kde4-kfloppy = %version

%description -n kfloppy
%{name} kfloppy.

%files -n kfloppy
%defattr(-,root,root)
%_kde_bindir/kfloppy
%_kde_datadir/applications/kde4/KFloppy.desktop
%_kde_datadir/kde4/services/ServiceMenus/floppy_format.desktop
%_kde_docdir/HTML/*/kfloppy

#---------------------------------------------

%package -n     kgpg
Summary:        %{name} kgpg
Group:          Graphical desktop/KDE
Requires:       %name-core = %version
Obsoletes:      %name-kgpg < 3.93.0-0.714053.1
Obsoletes:      kde4-kgpg < 4.0.68
Provides:       kde4-kgpg = %version
Obsoletes:      kdeutils-kgpg < 3.5.9-3

%description -n kgpg
%{name} kgpg.

%files -n kgpg
%defattr(-,root,root)
%_kde_appsdir/kgpg
%_kde_bindir/kgpg
%_kde_datadir/applications/kde4/kgpg.desktop
%_kde_datadir/kde4/services/ServiceMenus/encryptfile.desktop
%_kde_datadir/kde4/services/ServiceMenus/encryptfolder.desktop
%_kde_datadir/autostart/kgpg.desktop
%_kde_datadir/config.kcfg/kgpg.kcfg
%_kde_datadir/dbus-1/interfaces/org.kde.kgpg.Key.xml
%_kde_docdir/HTML/*/kgpg
#---------------------------------------------

%package -n     ktimer
Summary:        %{name} ktimer
Group:          Graphical desktop/KDE
Requires:       %name-core = %version
Obsoletes:      %name-ktimer < 3.93.0-0.714053.1
Obsoletes:      kde4-ktimer < 4.0.68
Provides:       kde4-ktimer = %version
Conflicts:      kdeutils-ktimer < 3.5.9-3

%description -n ktimer
%{name} ktimer.

%files -n ktimer
%defattr(-,root,root)
%_kde_bindir/ktimer
%_kde_datadir/applications/kde4/ktimer.desktop
%_kde_docdir/HTML/*/ktimer

#---------------------------------------------

%package -n     kwallet
Summary:        %{name} kwallet
Group:          Graphical desktop/KDE
Requires:       %name-core = %version
Obsoletes:      %name-kwallet < 3.93.0-0.714053.1
Obsoletes:      kde4-kwallet < 4.0.68
Provides:       kde4-kwallet = %version
Conflicts:      kdeutils-kwalletmanager < 3.5.9-3

%description -n kwallet
%{name} kwallet.

%files -n kwallet
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

%package -n superkaramba
Summary: %{name} superkaramba
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-superkaramba < 3.93.0-0.714053.1
Obsoletes: kdeutils4-devel
Obsoletes:      kde4-superkaramba < 4.0.68
Provides:       kde4-superkaramba = %version

%description -n superkaramba
%{name} superkaramba.

%files -n superkaramba
%defattr(-,root,root)
%_kde_appsdir/superkaramba
%_kde_bindir/superkaramba
%_kde_datadir/applications/kde4/superkaramba.desktop
%_kde_libdir/kde4/plasma_package_superkaramba.so
%_kde_libdir/kde4/plasma_scriptengine_superkaramba.so
%_kde_datadir/kde4/services/plasma-package-superkaramba.desktop
%_kde_datadir/kde4/services/plasma-scriptengine-superkaramba.desktop
%_kde_datadir/config/superkaramba.knsrc
%_kde_datadir/dbus-1/interfaces/org.kde.superkaramba.xml
%_kde_docdir/HTML/*/superkaramba
# Should not be installed
%exclude %_kde_libdir/libsuperkaramba.so

#---------------------------------------------

%package -n ark
Summary: %{name} ark
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-ark < 3.93.0-0.714053.1
Obsoletes: kdeutils4-devel
Obsoletes:      kde4-ark < 4.0.68
Provides:       kde4-ark = %version

%description -n ark
%{name} ark.

%files -n ark
%defattr(-,root,root)
%_kde_bindir/ark
%_kde_libdir/kde4/libarkpart.so
%_kde_libdir/kde4/kerfuffle_*
%_kde_datadir/applications/kde4/ark.desktop
%_kde_appsdir/ark
%_kde_datadir/config.kcfg/ark.kcfg
%_kde_datadir/kde4/services/ark_part.desktop
%_kde_datadir/kde4/services/kerfuffle_*
%_kde_datadir/kde4/servicetypes/kerfufflePlugin.desktop
%_kde_docdir/HTML/*/ark

# Should not be installed
%exclude %_kde_libdir/libkerfuffle.so

#---------------------------------------------

%define libkerfuffle %mklibname kerfuffle 4

%package -n %libkerfuffle
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkerfuffle
KDE 4 library

%if %mdkversion < 200900
%post -n %libkerfuffle -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkerfuffle -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libsuperkaramba -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libsuperkaramba -p /sbin/ldconfig
%endif

%files -n %libsuperkaramba
%defattr(-,root,root)
%_kde_libdir/libsuperkaramba.so.*

#---------------------------------------------

%package -n sweeper
Summary: %{name} sweeper
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-sweeper < 3.93.0-0.714053.1
Obsoletes:      kde4-sweeper < 4.0.68
Provides:       kde4-sweeper = %version

%description -n sweeper
%{name} sweeper.

%files -n sweeper
%defattr(-,root,root)
%_kde_appsdir/sweeper
%_kde_bindir/sweeper
%_kde_datadir/applications/kde4/sweeper.desktop
%_kde_datadir/dbus-1/interfaces/org.kde.sweeper.xml

#---------------------------------------------

%package -n okteta
Summary: %{name} okteta
Group: Graphical desktop/KDE
Requires: %name-core = %version

%description -n okteta
%{name} okteta.

%files -n okteta
%defattr(-,root,root)
%_kde_bindir/okteta
%_kde_libdir/kde4/libkbytearrayedit.so
%_kde_libdir/kde4/liboktetapart.so
%_kde_datadir/applications/kde4/okteta.desktop
%dir %_kde_appsdir/okteta
%_kde_appsdir/okteta/oktetaui.rc
%dir %_kde_appsdir/oktetapart
%_kde_appsdir/oktetapart/oktetapartui.rc
%_kde_datadir/kde4/services/kbytearrayedit.desktop
%_kde_datadir/kde4/services/oktetapart.desktop
%_kde_docdir/HTML/en/okteta

%exclude %_kde_libdir/liboktetagui.so
%exclude %_kde_libdir/liboktetacore.so

#---------------------------------------------

%define liboktetacore_major 4
%define liboktetacore %mklibname oktetacore %{liboktetacore_major}

%package -n %liboktetacore
Summary: KDE 4 library
Group: System/Libraries

%description -n %liboktetacore
KDE 4 library

%if %mdkversion < 200900
%post -n %liboktetacore -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %liboktetacore -p /sbin/ldconfig
%endif

%files -n %liboktetacore
%defattr(-,root,root)
%_kde_libdir/liboktetacore.so.%{liboktetacore_major}*

#---------------------------------------------

%define liboktetagui_major 4
%define liboktetagui %mklibname oktetagui %{liboktetagui_major}

%package -n %liboktetagui
Summary: KDE 4 library
Group: System/Libraries

%description -n %liboktetagui
KDE 4 library

%if %mdkversion < 200900
%post -n %liboktetagui -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %liboktetagui -p /sbin/ldconfig
%endif

%files -n %liboktetagui
%defattr(-,root,root)
%_kde_libdir/liboktetagui.so.%{liboktetagui_major}*

#---------------------------------------------


%prep
%setup -q -n kdeutils-%version

%build
%cmake_kde4 \
	-DINSTALL_PRINTER_APPLET=TRUE

%make

%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install

%clean
rm -fr %buildroot

