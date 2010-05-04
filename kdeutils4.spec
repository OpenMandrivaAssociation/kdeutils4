%define branch 0
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define kde_snapshot svn1053190
%endif

%define with_printer_applet 0
%{?_with_printer_applet: %{expand: %%global with_printer_applet 1}}

Name: kdeutils4
Summary: Various desktop utilities for KDE
Version: 4.4.3
Release: %mkrel 1
Group: Graphical desktop/KDE
License: GPL
URL: http://utils.kde.org/
%if %branch
Source0: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeutils-%{version}%kde_snapshot.tar.bz2
%else
Source0: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeutils-%{version}.tar.bz2
%endif
Patch0:	kdeutils-4.2.70-printer-applet-manager-entry.patch
Patch1: kdeutils-4.0.98-fix-autostart.patch
Patch2: kdeutils-4.0.84-disable-printer-applet.patch
Patch3: kdeutils-4.3.90-customize-menu-entries.patch
Buildroot:	%_tmppath/%name-%version-%release-root
BuildRequires: X11-devel
BuildRequires: openssl-devel
BuildRequires: libnet-snmp-devel
BuildRequires: gmp-devel
BuildRequires: plasma-devel
BuildRequires: kdepimlibs4-devel
BuildRequires: libzip-devel
BuildRequires: kde4-macros
BuildRequires: qimageblitz-devel 
BuildRequires: libarchive-devel
%if %with_printer_applet 
BuildRequires: python-kde4
BuildRequires: system-config-printer
BuildRequires: python-cups
%endif
%ifarch %{ix86}
BuildRequires: tpctl-devel
%endif
BuildRequires:  kdebase4-devel
BuildConflicts: libxmms-devel
Requires: kcalc
Requires: kcharselect
Requires: kdf
Requires: kfloppy
Requires: kgpg
Requires: ktimer
Requires: kwallet
Requires: superkaramba
Requires: sweeper

%description
The KDE Utilities are a compilation of various desktop utilities.

%files
%defattr(-,root,root,-)
%doc README

#----------------------------------------------------------------------

%package     core
Summary:     %name core files
Group:       Graphical desktop/KDE
Requires:    kdelibs4-core
%if %mdkversion >= 201000
Obsoletes:   kdeutils-common < 3.5.10-3
Obsoletes:   kdeutils-kmilo < 3.5.10-3
Obsoletes:   kdeutils4-kmilo < 4.0.74-1
Obsoletes:   kmilo < 4.0.74-1
Obsoletes:   kdeutils4-kedit
%else
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
%endif
%description core
Core files for %{name}.

%files core
%defattr(-,root,root)
%_kde_iconsdir/*/*/*/*

#----------------------------------------------------------------------

%package -n     kcalc
Summary:        Do scientific calculations
Group:          Graphical desktop/KDE
URL:		http://utils.kde.org/projects/kcalc
Requires:       %name-core = %version
Obsoletes:      %name-kcalc < 3.93.0-0.714053.1
Obsoletes:      kde4-kcalc < 4.0.68
Provides:       kde4-kcalc = %version
%if %mdkversion >= 201000 
Obsoletes:      kdeutils-kcalc < 3.5.10-3
%else
Conflicts:      kdeutils-kcalc < 3.5.10-3
%endif

%description -n kcalc
KCalc is a calculator which offers many more mathematical functions
than meet the eye on a first glance. Please study the section on
keyboard accelerators and modes in the handbook to learn more about
the many functions available.

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

%if %{with_printer_applet}
%package printer-applet
Summary: View current print jobs and configure new printers
Group: Graphical desktop/KDE
URL: http://utils.kde.org/projects/printer-applet
Requires: %name-core = %version
Requires: python-kde4 >= 1:4.1.0
Requires: python-cups
Requires: python-qt4
Requires: python-dbus
Requires: system-config-printer

%description printer-applet
Printer Applet is a system tray utility that shows current print jobs,
shows printer warnings and errors and shows when printers that have
been plugged in for the first time are being auto-configured by
hal-cups-utils.

%files printer-applet
%defattr(-,root,root)
%_kde_bindir/printer-applet
%_kde_appsdir/printer-applet
%_kde_datadir/autostart/printer-applet.desktop
%doc %_kde_docdir/HTML/en/printer-applet
%endif

#---------------------------------------------


%package -n kcharselect
Summary: Select special characters from any font
Group: Graphical desktop/KDE
URL: http://utils.kde.org/projects/kcharselect
Requires: %name-core = %version
Obsoletes: %name-kcharselect < 3.93.0-0.714053.1
Obsoletes:      kde4-kcharselect < 4.0.68
Provides:       kde4-kcharselect = %version
%if %mdkversion >= 201000
Obsoletes:      kdeutils-kcharselect < 3.5.10-3
%endif

%description -n kcharselect
KCharSelect is a tool to select special characters from all installed
fonts and copy them into the clipboard.

%files -n kcharselect
%defattr(-,root,root)
%_kde_appsdir/kconf_update
%_kde_appsdir/kcharselect
%_kde_bindir/kcharselect
%_kde_datadir/applications/kde4/KCharSelect.desktop
%_kde_docdir/HTML/*/kcharselect

#---------------------------------------------

%package -n kdf
Summary: View free disk space
Group: Graphical desktop/KDE
URL: http://utils.kde.org/projects/kdf
Requires: %name-core = %version
Obsoletes: %name-kdf < 3.93.0-0.714053.1
Obsoletes:      kde4-kdf < 4.0.68
Provides:       kde4-kdf = %version
%if %mdkversion >= 201000
Obsoletes:      kdeutils-kdf < 3.5.10-3
%endif

%description -n kdf
KDiskFree displays the available file devices (hard drive partitions,
floppy and CD/DVD drives, etc.) along with information on their capacity,
free space, type and mount point. It also allows you to mount and unmount
drives and view them in a file manager.

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
%_kde_docdir/HTML/*/kcontrol/blockdevices

#---------------------------------------------

%package -n kfloppy
Summary: Format floppy disks
Group: Graphical desktop/KDE
URL: http://utils.kde.org/projects/kfloppy
Requires: %name-core = %version
Obsoletes: %name-kfloppy < 3.93.0-0.714053.1
Obsoletes:      kde4-kfloppy < 4.0.68
Provides:       kde4-kfloppy = %version
%if %mdkversion >= 201000
Obsoletes:      kdeutils-kfloppy < 3.5.10-3
%endif

%description -n kfloppy
KFloppy is a utility that provides a straightforward graphical means to
format 3.5" and 5.25" floppy disks.

%files -n kfloppy
%defattr(-,root,root)
%_kde_bindir/kfloppy
%_kde_datadir/applications/kde4/KFloppy.desktop
%_kde_docdir/HTML/*/kfloppy

#---------------------------------------------

%package -n     kgpg
Summary:        Control your GPG keys
Group:          Graphical desktop/KDE
URL: http://utils.kde.org/projects/kgpg
Requires:       %name-core = %version
Obsoletes:      %name-kgpg < 3.93.0-0.714053.1
Obsoletes:      kde4-kgpg < 4.0.68
Provides:       kde4-kgpg = %version
%if %mdkversion >= 201000
Obsoletes:      kdeutils-kpgp < 3.5.10-3
%endif

%description -n kgpg
KGpg is a simple interface for GnuPG, a powerful encryption utility.

%files -n kgpg
%defattr(-,root,root)
%_kde_appsdir/kgpg
%_kde_bindir/kgpg
%_kde_datadir/applications/kde4/kgpg.desktop
%_kde_datadir/kde4/services/ServiceMenus/encryptfile.desktop
%_kde_datadir/kde4/services/ServiceMenus/encryptfolder.desktop
%_kde_datadir/kde4/services/ServiceMenus/viewdecrypted.desktop
%_kde_datadir/autostart/kgpg.desktop
%_kde_datadir/config.kcfg/kgpg.kcfg
%_kde_datadir/dbus-1/interfaces/org.kde.kgpg.Key.xml
%_kde_docdir/HTML/*/kgpg

#---------------------------------------------

%package -n     ktimer
Summary:        Execute programs after some time
Group:          Graphical desktop/KDE
URL: http://utils.kde.org/projects/ktimer
Requires:       %name-core = %version
Obsoletes:      %name-ktimer < 3.93.0-0.714053.1
Obsoletes:      kde4-ktimer < 4.0.68
Provides:       kde4-ktimer = %version
%if %mdkversion >= 201000
Obsoletes:      kdeutils-ktimer < 3.5.10-3
%endif

%description -n ktimer
KTimer is a little tool to execute programs after some time.

%files -n ktimer
%defattr(-,root,root)
%_kde_bindir/ktimer
%_kde_datadir/applications/kde4/ktimer.desktop
%_kde_docdir/HTML/*/ktimer

#---------------------------------------------

%package -n     kwallet
Summary:        Manage your passwords
Group:          Graphical desktop/KDE
URL: http://utils.kde.org/projects/kwalletmanager
Requires:       %name-core = %version
Obsoletes:      %name-kwallet < 3.93.0-0.714053.1
Obsoletes:      kde4-kwallet < 4.0.68
Provides:       kde4-kwallet = %version
Conflicts:      kdeutils-kwalletmanager < 3.5.9-3
%if %mdkversion >= 201000
Obsoletes:      kdeutils-kwalletmanager < 3.5.10-3
%else
Conflicts:      kdeutils-kwalletmanager < 3.5.9-3
%endif

%description -n kwallet
KDE Wallet Manager is for management of the wallets installed on the
system. The KDE wallet subsystem provides a convenient and secure way
to manage all your passwords.

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
Summary: Put Karamba applets to the desktop with Python
Group: Graphical desktop/KDE
URL: http://utils.kde.org/projects/superkaramba
Requires: %name-core = %version
%py_requires -d
%if %mdkversion >= 201000
Obsoletes:      kdeutils-superkaramba < 3.5.10-3
%endif
Obsoletes: %name-superkaramba < 3.93.0-0.714053.1
Obsoletes: kdeutils4-devel
Obsoletes:      kde4-superkaramba < 4.0.68
Provides:       kde4-superkaramba = %version

%description -n superkaramba
SuperKaramba is a tool that allows you to easily create interactive
widgets on your KDE desktop.

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

#---------------------------------------------

%package -n ark
Summary: Handle file archives
Group: Graphical desktop/KDE
URL: http://utils.kde.org/projects/ark
Requires: %name-core = %version
Obsoletes: %name-ark < 3.93.0-0.714053.1
Obsoletes: kdeutils4-devel
Obsoletes: kde4-ark < 4.0.68
Provides:  kde4-ark = %version
%if %mdkversion >= 201000
Obsoletes: kdeutils-ark < 3.5.10-3
%endif
Suggests: p7zip
Suggests: unzip

%description -n ark
Ark is a program for managing various archive formats within the KDE
environment.

%files -n ark
%defattr(-,root,root)
%_kde_bindir/ark
%_kde_libdir/kde4/kerfuffle_*
%_kde_libdir/kde4/libextracthere.so
%_kde_libdir/kde4/arkpart.so
%_kde_datadir/applications/kde4/ark.desktop
%_kde_appsdir/ark
%_kde_datadir/config.kcfg/ark.kcfg
%_kde_datadir/kde4/services/ark_part.desktop
%_kde_datadir/kde4/services/kerfuffle_*
%_kde_datadir/kde4/servicetypes/kerfufflePlugin.desktop
%_kde_datadir/kde4/services/ServiceMenus/ark_*.desktop
%_kde_datadir/kde4/services/ark_dndextract.desktop
%_kde_docdir/HTML/*/ark
%_kde_mandir/man1/ark.1.*

#---------------------------------------------

%define libkerfuffle %mklibname kerfuffle 4

%package -n %libkerfuffle
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkerfuffle
KDE 4 library

%files -n %libkerfuffle
%defattr(-,root,root)
%_kde_libdir/libkerfuffle.so.*

#---------------------------------------------

%define libsuperkaramba %mklibname superkaramba 4

%package -n %libsuperkaramba
Summary: KDE 4 library
Group: System/Libraries
URL: http://utils.kde.org/projects/superkaramba

%description -n %libsuperkaramba
KDE 4 library

%files -n %libsuperkaramba
%defattr(-,root,root)
%_kde_libdir/libsuperkaramba.so.*

#---------------------------------------------

%package -n sweeper
Summary: Clean unwanted traces from your system
Group: Graphical desktop/KDE
URL: http://utils.kde.org/projects/sweeper
Requires: %name-core = %version
Obsoletes: %name-sweeper < 3.93.0-0.714053.1
Obsoletes:      kde4-sweeper < 4.0.68
Provides:       kde4-sweeper = %version

%description -n sweeper
Sweeper helps to clean unwanted traces the user leaves on the system.

%files -n sweeper
%defattr(-,root,root)
%_kde_appsdir/sweeper
%_kde_bindir/sweeper
%_kde_datadir/applications/kde4/sweeper.desktop
%_kde_datadir/dbus-1/interfaces/org.kde.sweeper.xml

#---------------------------------------------
%package -n kdelirc
Summary: Frontend for the LIRC suite
Group: Graphical desktop/KDE
URL: http://utils.kde.org/projects/sweeper
Requires: %name-core = %version

%description -n kdelirc
This is a frontend for the LIRC suite to use infrared devices with KDE.

%files -n kdelirc
%defattr(-,root,root)
%{_kde_bindir}/irkick
%{_kde_libdir}/kde4/kcm_lirc.so
%{_kde_libdir}/libkdeinit4_irkick.so
%{_kde_datadir}/applications/kde4/irkick.desktop
%{_kde_appsdir}/irkick/irkick.notifyrc
%{_kde_appsdir}/profiles/amarok.profile.xml
%{_kde_appsdir}/profiles/dragonplayer.profile.xml
%{_kde_appsdir}/profiles/klauncher.profile.xml
%{_kde_appsdir}/profiles/kmix.profile.xml
%{_kde_appsdir}/profiles/konqueror.profile.xml
%{_kde_appsdir}/profiles/okular.profile.xml
%{_kde_appsdir}/profiles/profile.dtd
%{_kde_appsdir}/profiles/shutdown.profile.xml
%{_kde_appsdir}/profiles/suspend.profile.xml
%{_kde_appsdir}/profiles/vlc.profile.xml
%{_kde_datadir}/autostart/irkick.desktop
%{_kde_datadir}/kde4/services/kcm_lirc.desktop

%doc %{_kde_docdir}/HTML/en/kcmlirc
%doc %{_kde_docdir}/HTML/en/irkick
#---------------------------------------------

%define libkdelirc_shared_major 1
%define libkdelirc_shared %mklibname kdelirc_shared %{libkdelirc_shared_major}

%package -n %libkdelirc_shared
Summary: KDE 4 library
Group: System/Libraries
URL: http://utils.kde.org/projects/okteta

%description -n %libkdelirc_shared
KDE 4 library

%files -n %libkdelirc_shared
%defattr(-,root,root)
%_kde_libdir/libkdelirc_shared.so.%{libkdelirc_shared_major}*

#---------------------------------------------
%package -n okteta
Summary: Edit raw file data as Hex values
Group: Graphical desktop/KDE
URL: http://utils.kde.org/projects/okteta
Requires: %name-core = %version
%if %mdkversion >= 201000
Obsoletes:      kdeutils-khexedit < 3.5.10-3
%endif

%description -n okteta
Okteta is a simple editor for the raw data of files. This type of
program is also called hex editor or binary editor.

%files -n okteta
%defattr(-,root,root)
%_kde_bindir/okteta
%_kde_libdir/kde4/libkbytearrayedit.so
%_kde_libdir/kde4/oktetapart.so
%_kde_datadir/applications/kde4/okteta.desktop
%_kde_appsdir/okteta
%_kde_appsdir/oktetapart
%_kde_datadir/kde4/services/kbytearrayedit.desktop
%_kde_datadir/kde4/services/oktetapart.desktop
%_kde_docdir/HTML/en/okteta

#---------------------------------------------

%define liboktetacore_major 4
%define liboktetacore %mklibname oktetacore %{liboktetacore_major}

%package -n %liboktetacore
Summary: KDE 4 library
Group: System/Libraries
URL: http://utils.kde.org/projects/okteta

%description -n %liboktetacore
KDE 4 library

%files -n %liboktetacore
%defattr(-,root,root)
%_kde_libdir/liboktetacore.so.%{liboktetacore_major}*

#---------------------------------------------

%define liboktetakastengui_major 4
%define liboktetakastengui %mklibname oktetakastengui %{liboktetakastengui_major}

%package -n %liboktetakastengui
Summary: KDE 4 library
Group: System/Libraries
URL: http://utils.kde.org/projects/okteta

%description -n %liboktetakastengui
KDE 4 library

%files -n %liboktetakastengui
%defattr(-,root,root)
%_kde_libdir/liboktetakastengui.so.%{liboktetakastengui_major}*

#---------------------------------------------

%define liboktetagui_major 4
%define liboktetagui %mklibname oktetagui %{liboktetagui_major}

%package -n %liboktetagui
Summary: KDE 4 library
Group: System/Libraries
URL: http://utils.kde.org/projects/okteta

%description -n %liboktetagui
KDE 4 library

%files -n %liboktetagui
%defattr(-,root,root)
%_kde_libdir/liboktetagui.so.%{liboktetagui_major}*

#---------------------------------------------

%define liboktetakastencore_major 4
%define liboktetakastencore %mklibname oktetakastencore %{liboktetakastencore_major}

%package -n %liboktetakastencore
Summary: KDE 4 library
Group: System/Libraries
URL: http://utils.kde.org/projects/okteta

%description -n %liboktetakastencore
KDE 4 library

%files -n %liboktetakastencore
%defattr(-,root,root)
%_kde_libdir/liboktetakastencore.so.%{liboktetakastencore_major}*

#---------------------------------------------

%define liboktetakastencontrollers_major 4
%define liboktetakastencontrollers %mklibname oktetakastencontrollers %{liboktetakastencontrollers_major}

%package -n %liboktetakastencontrollers
Summary: KDE 4 library
Group: System/Libraries
URL: http://utils.kde.org/projects/okteta

%description -n %liboktetakastencontrollers
KDE 4 library

%files -n %liboktetakastencontrollers
%defattr(-,root,root)
%_kde_libdir/liboktetakastencontrollers.so.%{liboktetakastencontrollers_major}*

#---------------------------------------------

%define libkastengui_major 4
%define libkastengui %mklibname kastengui %{libkastengui_major}

%package -n %libkastengui
Summary: KDE 4 library
Group: System/Libraries
URL: http://utils.kde.org/projects/okteta

%description -n %libkastengui
KDE 4 library

%files -n %libkastengui
%defattr(-,root,root)
%_kde_libdir/libkastengui.so.%{libkastengui_major}*

#---------------------------------------------

%define libkastencore_major 4
%define libkastencore %mklibname kastencore %{libkastencore_major}

%package -n %libkastencore
Summary: KDE 4 library
Group: System/Libraries
URL: http://utils.kde.org/projects/okteta

%description -n %libkastencore
KDE 4 library

%files -n %libkastencore
%defattr(-,root,root)
%_kde_libdir/libkastencore.so.%{libkastencore_major}*

#---------------------------------------------

%define libkastencontrollers_major 4
%define libkastencontrollers %mklibname kastencontrollers %{libkastencontrollers_major}

%package -n %libkastencontrollers
Summary: KDE 4 library
Group: System/Libraries
URL: http://utils.kde.org/projects/okteta

%description -n %libkastencontrollers
KDE 4 library

%files -n %libkastencontrollers
%defattr(-,root,root)
%_kde_libdir/libkastencontrollers.so.%{libkastencontrollers_major}*

#---------------------------------------------

%package devel
Summary: Devel stuff for %{name}
Group: Development/KDE and Qt
Requires: kdelibs4-devel >= 2:4.2.98
Requires: %name = %version-%release
Requires: %libkerfuffle = %version-%release
Requires: %libsuperkaramba = %version-%release
Requires: %libkdelirc_shared = %version-%release
Requires: %liboktetacore = %version-%release
Requires: %liboktetakastengui = %version-%release
Requires: %liboktetagui = %version-%release
Requires: %liboktetakastencore = %version-%release
Requires: %liboktetakastencontrollers = %version-%release
Requires: %libkastengui = %version-%release
Requires: %libkastencore = %version-%release
Requires: %libkastencontrollers = %version-%release

%description  devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%defattr(-,root,root)
%{_kde_libdir}/libkastencontrollers.so
%{_kde_libdir}/libkastencore.so
%{_kde_libdir}/libkastengui.so
%{_kde_libdir}/libkerfuffle.so
%{_kde_libdir}/liboktetacore.so
%{_kde_libdir}/liboktetagui.so
%{_kde_libdir}/liboktetakastencore.so
%{_kde_libdir}/liboktetakastengui.so
%{_kde_libdir}/libsuperkaramba.so
%{_kde_libdir}/libkdelirc_shared.so
%{_kde_libdir}/liboktetakastencontrollers.so

#---------------------------------------------

%prep
%if %branch
%setup -q -n kdeutils-%{version}%kde_snapshot
%else
%setup -q -n kdeutils-%{version}
%endif
%patch0 -p1 -b .add_manager_entry
%patch1 -p0 -b .onlyshow
%if ! %{with_printer_applet}
%patch2 -p1
%endif
%patch3 -p0

%build
%cmake_kde4 \
%if ! %{with_printer_applet}
    -DINSTALL_PRINTER_APPLET=FALSE
%else
    -DINSTALL_PRINTER_APPLET=TRUE
%endif

%make

%install
rm -fr %buildroot

%makeinstall_std -C build

%clean
rm -fr %buildroot

