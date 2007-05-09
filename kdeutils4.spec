
# remove it when kde4 will be official kde package
%define _prefix /opt/kde4/
%define _libdir %_prefix/%_lib
%define _datadir %_prefix/share/
%define _bindir %_prefix/bin
%define _includedir %_prefix/include/
%define _iconsdir %_datadir/icons/
%define _sysconfdir %_prefix/etc/
%define _docdir %_datadir/doc/

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch_date 20070502

%if %unstable
%define dont_strip 1
%endif

%define lib_name_orig lib%{name}
%define lib_major 1
%define lib_name %mklibname kdeutils4 %lib_major


%define tpctl_arches %{ix86}

%define apm_arches %{ix86} ppc x86_64 amd64

Name: 		kdeutils4
Summary:	K Desktop Environment - Utilities
Version: 	3.90.1
Release: 	%mkrel 0.%branch_date.1 
Group: 		Graphical desktop/KDE
URL: http://www.kde.org
Packager: Mandriva Linux KDE Team <kde@mandriva.com>
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeutils-%version-%branch_date.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeutils-%version.tar.bz2
%endif
Source1:	kdeutils-3.2.3-kcmlaptoprc
Patch0: kdeutils-3.0-ktimer_icons.patch
Patch1: kdeutils-3.4.2-floppy.patch
Patch4: kdeutils-3.5.4-klaptop-empty-file.patch
Patch5:	kdeutils-3.5.5-fix-zip.patch
Patch6:	kdeutils-3.5.5-klaptop-pmsuspend.patch
BuildRoot:	%_tmppath/%name-%version-%release-root
License:	GPL
BuildRequires: X11-devel
BuildRequires: openssl-devel
BuildRequires: libnet-snmp-devel
BuildRequires:	gmp-devel
%define mini_release %mkrel 0.%branch_date.1
BuildRequires: kdelibs4-devel >= %version-%mini_release
BuildRequires:	kdepimlibs4-devel >= %version-%mini_release
# Need by superkaramba
BuildRequires:	kdebase4-devel
%py_requires -d
%ifarch %{tpctl_arches}
#BuildRequires:	libtpctl-devel
%endif
BuildConflicts: libxmms-devel
Requires:	%name-kcalc = %version-%release
Requires:	%name-ktimer = %version-%release
Requires:	%name-kjots = %version-%release
Requires:	%name-khexedit = %version-%release
Requires:	%name-kfloppy = %version-%release
Requires:	%name-kdf = %version-%release
Requires:	%name-kcharselect = %version-%release
Requires:	%name-ark = %version-%release
Requires:	%lib_name-common = %version-%release
Requires:	%name-kdessh = %version-%release
Requires:	%name-ksim = %version-%release
Requires:	%name-common = %version-%release
Requires:	%name-klaptop = %version-%release
Requires:   %name-kwalletmanager = %version-%release
Requires:   %name-superkaramba = %version-%release

%description
Utilities for the K Desktop Environment.
	- ark: manager for compressed files and archives
	- kcalc: scientific calculator
	- kcharselect: select special characters from any fonts 
			and put them into the clipboard
	- charselectapplet: dito, but as a Kicker applet
	- kdessh: front end to ssh
	- kdf: like 'df', a graphical free disk space viewer
	- kfloppy: format a floppy disks with this app
	- khexedit: binary file editor
	- kjots: manages several "books" with a subject and notes
	- klaptopdaemon: battery and power management, including KControl plugins
	- kregexpeditor: graphical regular expression editor
	- ktimer: execute programs after some time

%files

#-----------------------------------------------------------------------------

%package klaptop
Summary:	Battery and power management
Group:		Graphical desktop/KDE
Requires:	%lib_name-klaptop = %version-%release
Provides:	klaptop4
Requires:	cpufreq
%ifarch %{tpctl_arches}
#Requires:	tpctl
%endif

%description klaptop
Battery and power management, including KControl plugins.

%post klaptop
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun klaptop
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%files klaptop
%defattr(-,root,root)
#%attr(-,root,nogroup) %_bindir/klaptop_acpi_helper

%_libdir/kde4/kcm_thinkpad.so
%_libdir/kde4/kded_kmilod.so
%_libdir/kde4/kmilo_asus.so
%_libdir/kde4/kmilo_kvaio.so
%_libdir/kde4/kmilo_thinkpad.so
%_datadir/applications/kde4/thinkpad.desktop


%_datadir/dbus-1/interfaces/org.kde.kmilod.xml


%_datadir/kde4/services/kded/kmilod.desktop
%_datadir/kde4/services/kmilo/kmilo_asus.desktop
%_datadir/kde4/services/kmilo/kmilo_kvaio.desktop
%_datadir/kde4/services/kmilo/kmilo_thinkpad.desktop
%_datadir/kde4/servicetypes/kmilo/kmilopluginsvc.desktop

#-----------------------------------------------------------------------------

%package -n %lib_name-klaptop
Summary:	Library for klaptop
Group:		Development/KDE and Qt	

%description -n %lib_name-klaptop
Library for klaptop.

%post -n %lib_name-klaptop -p /sbin/ldconfig
%postun -n %lib_name-klaptop -p /sbin/ldconfig

%files -n %lib_name-klaptop
%defattr(-,root,root)
%_libdir/libkmilo.so.*

#-----------------------------------------------------------------------------

%package -n %lib_name-klaptop-devel
Summary:	Devel for klaptop
Group: 		Development/KDE and Qt
Requires: %lib_name-klaptop = %version-%release

%description -n %lib_name-klaptop-devel
Devel for klaptop.

%files -n %lib_name-klaptop-devel
%defattr(-,root,root)
%_libdir/libkmilo.so

#-----------------------------------------------------------------------------

%package common
Summary:	Kdeutils common files
Group:		Graphical desktop/KDE
Requires:	%lib_name-common = %version-%release
URL:        http://www.kde.org/

%description common
Kdeutils common files

%post common
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun common
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%files common
%defattr(-,root,root)
%_datadir/applications/kde4/kregexpeditor.desktop  
%_iconsdir/*/*/*/kregexpeditor*
%_bindir/kregexpeditor
%dir %_datadir/apps/kregexpeditor/
%_datadir/apps/kregexpeditor/*
%_datadir/kde4/services/kregexpeditorgui.desktop
%_libdir/kde4/libkregexpeditorgui.*
%_bindir/sweeper
%_datadir/applications/kde4/sweeper.desktop
%_datadir/apps/sweeper/sweeperui.rc
%dir %_docdir/HTML/en/KRegExpEditor/
%doc %_docdir/HTML/en/KRegExpEditor/*.png
%doc %_docdir/HTML/en/KRegExpEditor/*.bz2
%doc %_docdir/HTML/en/KRegExpEditor/*.docbook

#-----------------------------------------------------------------------------

%package ktimer
Summary:	Ktimer program
Group:		Graphical desktop/KDE
Provides:	ktimer4
URL:        http://www.kde.org/

%description ktimer
Ktimer allows to execute programs after some time

%post ktimer
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun ktimer
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor


%files ktimer
%defattr(-,root,root)
%_bindir/ktimer
%_datadir/applications/kde4/ktimer.desktop
%_iconsdir/*/*/*/ktimer*
%dir %_docdir/HTML/en/ktimer/
%doc %_docdir/HTML/en/ktimer/*.bz2
%doc %_docdir/HTML/en/ktimer/*.docbook

#-----------------------------------------------------------------------------

%package kdessh
Summary:	Kdessh program
Group:		Graphical desktop/KDE
Provides:	kdessh4
URL:        http://www.kde.org/

%description kdessh
Front end to ssh

%files kdessh
%defattr(-,root,root)
%_bindir/kdessh

#-----------------------------------------------------------------------------

%package kjots
Summary:	Kjots program
Group:		Graphical desktop/KDE
Provides:	kjots4, Kjots4
URL:        http://www.kde.org/

%description kjots
Manages several "books" with a subject and notes

%post kjots
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun kjots
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%files kjots
%defattr(-,root,root)
%_iconsdir/*/*/*/kjots.*
%_bindir/kjots
%dir %_datadir/apps/kjots
%_datadir/apps/kjots/*
%_datadir/applications/kde4/Kjots.desktop          
%_datadir/config.kcfg/kjots.kcfg
%dir %_docdir/HTML/en/kjots/
%doc %_docdir/HTML/en/kjots/*.bz2
%doc %_docdir/HTML/en/kjots/*.docbook
#-----------------------------------------------------------------------------

%package kfloppy
Summary:	Kfloppy program
Group:		Graphical desktop/KDE
Requires:	dosfstools
Provides:	kfloppy4
URL:        http://www.kde.org/

%description kfloppy
Kfloppy allows to format a floppy disks with this app

%post kfloppy
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun kfloppy
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%files kfloppy
%defattr(-,root,root)
%_iconsdir/*/*/*/kfloppy.*
%_bindir/kfloppy
%_datadir/applications/kde4/KFloppy.desktop        
%_datadir/apps/konqueror/servicemenus/floppy_format.desktop
%dir %_docdir/HTML/en/kfloppy/
%doc %_docdir/HTML/en/kfloppy/*.bz2
%doc %_docdir/HTML/en/kfloppy/*.docbook

#-----------------------------------------------------------------------------

%package kdf
Summary:	Kdf program
Group:		Graphical desktop/KDE
Provides:	kdf4
URL:        http://www.kde.org/

%description kdf
Like 'df', a graphical free disk space viewer

%post kdf
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun kdf
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%files kdf
%defattr(-,root,root)
%_bindir/kdf
%_bindir/kwikdisk
%_iconsdir/*/*/*/kwikdisk.*
%_iconsdir/*/*/*/kdf.*
%_iconsdir/*/*/*/kcmdf.*
%dir %_datadir/apps/kdf
%_datadir/apps/kdf/*
%_datadir/applications/kde4/kdf.desktop          
%_datadir/applications/kde4/kwikdisk.desktop
%_datadir/applications/kde4/kcmdf.desktop 
%_libdir/kde4/kcm_kdf.*
%dir %_docdir/HTML/en/kdf/
%doc %_docdir/HTML/en/kdf/*.bz2
%doc %_docdir/HTML/en/kdf/*.docbook
%doc %_docdir/HTML/en/kdf/*.png
#-----------------------------------------------------------------------------

%package kcharselect
Summary:	Kcharselect program
Group:		Graphical desktop/KDE
Provides:	kcharselect4

%description kcharselect
Kcharselect allows to select special characters from any fonts and put them into the clipboard

%post kcharselect
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun kcharselect

%files kcharselect
%defattr(-,root,root)
%_bindir/kcharselect
%_iconsdir/*/*/*/kcharselect.*
%dir %_datadir/apps/kcharselect
%_datadir/apps/kcharselect/*
%_datadir/applications/kde4/KCharSelect.desktop  
%_datadir/apps/kconf_update/kcharselect.upd
%dir %_docdir/HTML/en/kcharselect/
%doc %_docdir/HTML/en/kcharselect/*.bz2
%doc %_docdir/HTML/en/kcharselect/*.docbook

#-----------------------------------------------------------------------------

%package khexedit
Summary:	Khexedit program
Group:		Graphical desktop/KDE
Provides:	khexedit4
Requires:	%lib_name-khexedit = %version
Conflicts: %lib_name-khexedit < 3.5.3-3mdv2007.0

%description khexedit
A binary file editor

%post khexedit
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun khexedit
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%files khexedit
%defattr(-,root,root)
%_bindir/khexedit
%_iconsdir/*/*/*/khexedit.*
%_datadir/kde4/services/khexedit2part.desktop
%_datadir/apps/khexedit2part/khexedit2partui.rc
%dir %_datadir/apps/khexedit
%_datadir/apps/khexedit/*
%_datadir/applications/kde4/khexedit.desktop       
%_libdir/kde4/libkhexedit2part.*
%_datadir/kde4/services/kbytearrayedit.desktop
%dir %_docdir/HTML/en/khexedit/
%doc %_docdir/HTML/en/khexedit/*.bz2
%doc %_docdir/HTML/en/khexedit/*.docbook
%doc %_docdir/HTML/en/khexedit/*.png
#-----------------------------------------------------------------------------

%package -n %lib_name-khexedit
Summary:	Khexedit library
Group:		Development/KDE and Qt
URL:        http://www.kde.org/

%description -n %lib_name-khexedit
Library for file editor

%post -n %lib_name-khexedit -p /sbin/ldconfig
%postun -n %lib_name-khexedit -p /sbin/ldconfig

%files -n %lib_name-khexedit
%defattr(-,root,root)
%_libdir/kde4/libkbytearrayedit.so
%_libdir/libkhexeditcore.so.*
%_libdir/libkhexeditgui.so.*

#-----------------------------------------------------------------------------

%package -n %lib_name-khexedit-devel
Summary:	Devel files for Khexedit
Group:		Development/KDE and Qt
URL:        http://www.kde.org/
Requires:	%lib_name-khexedit = %version

%description -n %lib_name-khexedit-devel
Devel files for file editor

%files -n %lib_name-khexedit-devel
%defattr(-,root,root)
%_libdir/libkhexeditcore.so
%_libdir/libkhexeditgui.so
#-----------------------------------------------------------------------------

%package ark
Summary:	Ark program
Group: Graphical desktop/KDE
Obsoletes: %lib_name-ark
Provides: ark4
Requires: zip	
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description ark
Manager for compressed files and archives

%post ark
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun ark
%{update_desktop_database}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%files ark
%defattr(-,root,root)
%_iconsdir/*/*/*/ark.*
%_bindir/ark
%dir %_datadir/apps/
%_datadir/apps/ark/*
%_datadir/applications/kde4/ark.desktop          
%_libdir/kde4/libarkpart.*
%_datadir/config.kcfg/ark.kcfg
%_datadir/kde4/services/ark_part.desktop
%_libdir/libkdeinit_ark.*
%dir %_docdir/HTML/en/ark/
%doc %_docdir/HTML/en/ark/*.bz2
%doc %_docdir/HTML/en/ark/*.docbook

#-----------------------------------------------------------------------------

%package kcalc
Summary:	Kcalc program
Group:		Graphical desktop/KDE
Obsoletes:	%lib_name-kcalc
Provides:	kcalc4
URL:        http://www.kde.org/

%description kcalc
A scientific calculator

%post kcalc
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun kcalc
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%files kcalc
%defattr(-,root,root)
%_bindir/kcalc
%_datadir/applications/kde4/kcalc.desktop
%_iconsdir/*/*/*/kcalc.*
%_datadir/config.kcfg/kcalc.kcfg
%dir %_datadir/apps/kcalc/
%_datadir/apps/kcalc/*
%_datadir/apps/kconf_update/kcalcrc.upd
%_libdir/libkdeinit_kcalc.*
%dir %_docdir/HTML/en/kcalc/
%doc %_docdir/HTML/en/kcalc/*.bz2
%doc %_docdir/HTML/en/kcalc/*.docbook
#-----------------------------------------------------------------------------

%package -n %lib_name-common-devel
Summary:	Header files for kdeutils
Group:		Development/KDE and Qt
Requires:	%lib_name-common
URL:        http://www.kde.org/

%description -n %lib_name-common-devel
Headers files for kdeutils.

%files -n %lib_name-common-devel
%defattr(-,root,root,-)
%_includedir/*.h
%_libdir/libkregexpeditorcommon.so

%_datadir/dbus-1/interfaces/org.kde.kgpg.Key.xml
%_datadir/dbus-1/interfaces/org.kde.sweeper.xml


#-----------------------------------------------------------------------------

%package -n %lib_name-common
Summary:	Librarie files for kdeutils
Group:		Development/KDE and Qt
Provides:	%lib_name = %version-%release
URL:        http://www.kde.org/

%description -n %lib_name-common
Libraries files for kdeutils.

%post -n %lib_name-common -p /sbin/ldconfig
%postun -n %lib_name-common -p /sbin/ldconfig

%files -n %lib_name-common
%defattr(-,root,root)
%_libdir/libkregexpeditorcommon.so.*

#-----------------------------------------------------------------------------

%package ksim
Summary:	Ksim program
Group:		Graphical desktop/KDE
Requires:	%lib_name-ksim = %version-%release
Provides:	ksim4
URL:        http://www.kde.org/
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description ksim
Ksim program

%post ksim
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun ksim
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%files ksim
%defattr(-,root,root)
#-----------------------------------------------------------------------------

%package kgpg
Summary:	Kgpg Frontend for gpg.
Group:		Graphical desktop/KDE
Provides:	kgpg4
URL:        http://www.kde.org/
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description kgpg
kgpg is a simple, free, open source KDE frontend for gpg.

%post kgpg
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun kgpg
%{clean_desktop_database}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%files kgpg
%defattr(-,root,root)
%_bindir/kgpg
%_datadir/applications/kde4/kgpg.desktop           
%_datadir/config.kcfg/kgpg.kcfg
%_iconsdir/*/*/*/kgpg.*
%dir %_datadir/apps/kgpg
%_datadir/apps/kgpg/*
%_datadir/autostart/kgpg.desktop
%_datadir/apps/konqueror/servicemenus/encryptfile.desktop
%_datadir/apps/konqueror/servicemenus/encryptfolder.desktop
%dir %_docdir/HTML/en/kgpg/
%doc %_docdir/HTML/en/kgpg/*.bz2
%doc %_docdir/HTML/en/kgpg/*.docbook
%doc %_docdir/HTML/en/kgpg/*.png

#-----------------------------------------------------------------------------

%package superkaramba
Group:      Graphical desktop/KDE
Summary:    Program that can display a lot of various information right on your desktop
Provides:	superkaramba4
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description superkaramba
Karamba is a KDE program that can display a lot of various information
right on your desktop. Karamba uses the same "fake" transparency effect
that e.g., Konsole can use. For the autor this is not a big problem as the
purpose of Karamba is sit on the background.

%post superkaramba
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun superkaramba
%{clean_desktop_database}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%files superkaramba
%defattr(-,root,root,-)
%_bindir/superkaramba
%_datadir/applications/kde4/superkaramba.desktop
%_datadir/apps/superkaramba/superkarambaui.rc
%_datadir/config/superkaramba.knsrc

%_datadir/dbus-1/interfaces/org.kde.superkaramba.xml

%dir %_docdir/HTML/en/superkaramba/
%doc %_docdir/HTML/en/superkaramba/*.bz2
%doc %_docdir/HTML/en/superkaramba/*.docbook

%_iconsdir/hicolor/128x128/apps/superkaramba.png
%_iconsdir/hicolor/16x16/apps/superkaramba.png
%_iconsdir/hicolor/22x22/apps/superkaramba.png
%_iconsdir/hicolor/32x32/apps/superkaramba.png
%_iconsdir/hicolor/48x48/apps/superkaramba.png
%_iconsdir/hicolor/64x64/apps/superkaramba.png
%_iconsdir/hicolor/scalable/apps/superkaramba.svgz
%_iconsdir/oxygen/128x128/mimetypes/superkaramba_theme.png
%_iconsdir/oxygen/16x16/mimetypes/superkaramba_theme.png
%_iconsdir/oxygen/22x22/mimetypes/superkaramba_theme.png
%_iconsdir/oxygen/32x32/mimetypes/superkaramba_theme.png
%_iconsdir/oxygen/48x48/mimetypes/superkaramba_theme.png
%_iconsdir/oxygen/64x64/mimetypes/superkaramba_theme.png
%_iconsdir/oxygen/scalable/mimetypes/superkaramba_theme.svgz

#-----------------------------------------------------------------------------

%package kwalletmanager
Summary:    kwalletmanager program
Group:      Graphical desktop/KDE
Provides:   kwalletmanager4
URL:        http://www.kde.org/
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description kwalletmanager
Kwalletmanager program

%post kwalletmanager
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor


%postun kwalletmanager
%{clean_desktop_database}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%files kwalletmanager
%defattr(-,root,root)
%_bindir/kwalletmanager
%_iconsdir/*/*/*/kwalletmanager.*
%_datadir/applications/kde4/kwalletmanager-kwalletd.desktop
%_datadir/applications/kde4/kwalletmanager.desktop
%_libdir/kde4/kcm_kwallet.*
%_datadir/kde4/services/kwalletmanager_show.desktop
%dir %_datadir/apps/kwalletmanager/
%_datadir/apps/kwalletmanager/*
%_datadir/icons/hicolor/128x128/apps/kwalletmanager2.png
%_datadir/icons/hicolor/16x16/apps/kwalletmanager2.png
%_datadir/icons/hicolor/32x32/apps/kwalletmanager2.png
%_datadir/icons/hicolor/48x48/apps/kwalletmanager2.png
%_datadir/icons/hicolor/64x64/apps/kwalletmanager2.png
%_datadir/kde4/services/kwalletconfig.desktop
%dir %_docdir/HTML/en/kwallet/
%doc %_docdir/HTML/en/kwallet/*.png
%doc %_docdir/HTML/en/kwallet/*.bz2
%doc %_docdir/HTML/en/kwallet/*.docbook
#-----------------------------------------------------------------------------

%package -n %lib_name-ksim-devel
Summary:	Header files for ksim
Group:		Development/KDE and Qt
Requires:	%lib_name-ksim = %version-%release
URL:        http://www.kde.org/

%description -n %lib_name-ksim-devel
Headers files for ksim program.

%files -n %lib_name-ksim-devel
%defattr(-,root,root,-)

#-----------------------------------------------------------------------------

%package -n %lib_name-ksim
Summary:	Librarie files for kdeutils
Group:		Development/KDE and Qt
Provides:	%lib_name_orig-ksim = 1:%version-%release
URL:        http://www.kde.org/

%post -n %lib_name-ksim -p /sbin/ldconfig
%postun -n %lib_name-ksim -p /sbin/ldconfig

%description -n %lib_name-ksim
Libraries files for ksim.

%files -n %lib_name-ksim
%defattr(-,root,root)

#-----------------------------------------------------------------------------


%prep
%setup  -q  -nkdeutils-%version-%branch_date

%build
cd $RPM_BUILD_DIR/kdeutils-%version-%branch_date
mkdir build
cd build
export QTDIR=/usr/lib/qt4/
export PATH=$QTDIR/bin:$PATH

cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=Debug \
%endif
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
        ../

%make


%install
rm -fr %buildroot
cd $RPM_BUILD_DIR/kdeutils-%version-%branch_date/build/

%makeinstall_std

mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/KEdit.desktop "More Applications/Editors" kde
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kdf.desktop System/Monitoring 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kwikdisk.desktop System/Monitoring kde 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/ark.desktop System/Archiving/Compression 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kcalc.deskto Office/Accessories 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/KCharSelect.desktop Office/Accessories 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/KFloppy.desktop System/Configuration/Hardware 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/khexedit.desktop "More Applications/Editors" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/Kjots.desktop Office/Accessories 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/ktimer.desktop Office/Time\ management kde 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kregexpeditor.desktop "More Applications/Editors" kde 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kgpg.desktop kdeutils-kgpg 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kwalletmanager-kwalletd.desktop System/Configuration/Other 

# Link KDM images directory to faces directory
rm -fr %buildroot/%_datadir/apps/kdm/pics/users/


%clean
rm -fr %buildroot/

