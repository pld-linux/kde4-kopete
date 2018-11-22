# TODO:
# - add missing obsoletes and such

%define		_state		stable
%define		orgname		kopete
%define		qtver		4.8.3

Summary:	Multi-protocol plugin-based instant messenger
Summary(pl.UTF-8):	Komunikator obsługujący wiele protokołów
Name:		kde4-kopete
Version:	4.14.3
Release:	11
License:	GPL v2+
Group:		X11/Applications
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	d05e478101292ebb08da2af00d1329ab
Patch0:		%{name}-FindLibgadu.patch
Patch1:		linphone-fix.patch
Patch2:		mediastreamer.patch
Patch3:		gcc6.patch
Patch4:		macros.patch
URL:		http://www.kde.org/
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	kde4-kdepim-devel >= 4.14.0-2
BuildRequires:	kde4-kdepimlibs-devel >= 4.14.0-2
BuildRequires:	jsoncpp-devel
BuildRequires:	libgadu-devel >= 1.8.0
BuildRequires:	libktorrent-devel >= 1.0.2
BuildRequires:	libmms-devel
BuildRequires:	libmsn-devel >= 4.1
BuildRequires:	libotr-devel >= 4.0.0
BuildRequires:	mediastreamer-devel >= 2.3.0
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	ortp-devel >= 0.16.1-3
BuildRequires:	qimageblitz-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	speex-devel
BuildRequires:	telepathy-qt4-devel >= 0.9.0
BuildRequires:	xmms-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXtst-devel
Obsoletes:	kde4-kdenetwork-kopete
Obsoletes:	kde4-kdenetwork-kopete-protocol-aim
Obsoletes:	kde4-kdenetwork-kopete-protocol-bonjour
Obsoletes:	kde4-kdenetwork-kopete-protocol-gg
Obsoletes:	kde4-kdenetwork-kopete-protocol-groupwise
Obsoletes:	kde4-kdenetwork-kopete-protocol-icq
Obsoletes:	kde4-kdenetwork-kopete-protocol-jabber
Obsoletes:	kde4-kdenetwork-kopete-protocol-meanwhile
Obsoletes:	kde4-kdenetwork-kopete-protocol-skype
Obsoletes:	kde4-kdenetwork-kopete-protocol-sms
Obsoletes:	kde4-kdenetwork-kopete-protocol-winpopup
Obsoletes:	kde4-kdenetwork-kopete-protocol-wlm
Obsoletes:	kde4-kdenetwork-kopete-protocol-yahoo
Obsoletes:	kde4-kdenetwork-kopete-tool-autoreplace
Obsoletes:	kde4-kdenetwork-kopete-tool-avdeviceconfig
Obsoletes:	kde4-kdenetwork-kopete-tool-contactnotes
Obsoletes:	kde4-kdenetwork-kopete-tool-highlight
Obsoletes:	kde4-kdenetwork-kopete-tool-history
Obsoletes:	kde4-kdenetwork-kopete-tool-latex
Obsoletes:	kde4-kdenetwork-kopete-tool-nowlistening
Obsoletes:	kde4-kdenetwork-kopete-tool-texteffect
Obsoletes:	kde4-kdenetwork-kopete-tool-translator
Obsoletes:	kde4-kdenetwork-kopete-tool-webpresence
Obsoletes:	kde4-kdenetwork-libkopete
Obsoletes:	kde4-kdenetwork-libkopete_oscar
Obsoletes:	kde4-kdenetwork-libkopete_otr
Obsoletes:	kde4-kdenetwork-libkopete_videodevice
Obsoletes:	kopete
Obsoletes:	kopete-plugin-protocols-aim
Obsoletes:	kopete-plugin-protocols-gg
Obsoletes:	kopete-plugin-protocols-icq
Obsoletes:	kopete-plugin-protocols-irc
Obsoletes:	kopete-plugin-protocols-jabber
Obsoletes:	kopete-plugin-protocols-msn
Obsoletes:	kopete-plugin-protocols-oscar
Obsoletes:	kopete-plugin-protocols-sms
Obsoletes:	kopete-plugin-protocols-winpopup
Obsoletes:	kopete-plugin-protocols-yahoo
Obsoletes:	kopete-plugin-tools-autoaway
Obsoletes:	kopete-plugin-tools-autoreplace
Obsoletes:	kopete-plugin-tools-conectionstatus
Obsoletes:	kopete-plugin-tools-contactnotes
Obsoletes:	kopete-plugin-tools-cryptography
Obsoletes:	kopete-plugin-tools-highlight
Obsoletes:	kopete-plugin-tools-history
Obsoletes:	kopete-plugin-tools-importer
Obsoletes:	kopete-plugin-tools-motionaway
Obsoletes:	kopete-plugin-tools-nowlistening
Obsoletes:	kopete-plugin-tools-spellcheck
Obsoletes:	kopete-plugin-tools-texteffect
Obsoletes:	kopete-plugin-tools-translator
Obsoletes:	kopete-plugin-tools-webpresence
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kopete is a flexible and extendable multiple protocol instant
messaging system designed as a plugin-based system. All protocols are
plugins and allow modular installment, configuration, and usage
without the main application knowing anything about the plugin being
loaded. The goal of Kopete is to provide users with a standard and
easy to use interface between all of their instant messaging systems,
but at the same time also providing developers with the ease of
writing plugins to support a new protocol. The core Kopete development
team provides a handful of plugins that most users can use, in
addition to templates for new developers to base a plugin off of.

%description -l pl.UTF-8
Kopete to rozszerzalny i rozbudowywalny komunikator obsługujący wiele
protokołów, zaprojektowany w oparciu o wtyczki. Wszystkie protokoły są
wtyczkami, co pozwala na modularną instalację, konfigurację i używanie
bez potrzeby obsługi ładowanych wtyczek w głównej aplikacji. Celem
Kopete jest wyposażenie użytkowników w standardowy i łatwy w użyciu
interfejs pomiędzy wszystkimi systemami komunikatorów, a jednocześnie
zapewnienie programistom łatwości pisania wtyczek obsługujących nowe
protokoły. Załoga programistów Kopete udostępnia podręczny zestaw
wtyczek używanych przez większość użytkowników oraz szablony dla
nowych programistów, na których można opierać nowe wtyczki.

%package devel
Summary:	kopete header files
Summary(pl.UTF-8):	Pliki nagłówkowe kopete
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{version}

%description devel
kopete header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe kopete.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão para compilar aplicações que usem as bibliotecas
do kopete.

%prep
%setup -q -n %{orgname}-%{version}
%patch0 -p1
#%patch1 -p2
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
install -d build
cd build
%cmake \
	-DWITH_libjingle=OFF \
	-DMOZPLUGIN_INSTALL_DIR=%{_browserpluginsdir} \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%find_lang kopete --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_browser_plugins

%postun
/sbin/ldconfig
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%files -f kopete.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kopete
%attr(755,root,root) %{_bindir}/kopete_latexconvert.sh
%attr(755,root,root) %{_bindir}/winpopup-install
%attr(755,root,root) %{_bindir}/winpopup-send
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_*.so
%attr(755,root,root) %{_libdir}/kde4/kopete_*.so
%attr(755,root,root) %{_libdir}/kde4/libchattexteditpart.so
%attr(755,root,root) %{_libdir}/kde4/plugins/accessible/chatwindowaccessiblewidgetfactory.so
%attr(755,root,root) %{_libdir}/libkopete*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopete*.so.?
%attr(755,root,root) %{_libdir}/libkyahoo.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkyahoo.so.1
%attr(755,root,root) %{_libdir}/liboscar.so.*.*
%attr(755,root,root) %ghost %{_libdir}/liboscar.so.1
%attr(755,root,root) %{_libdir}/libqgroupwise.so
%{_desktopdir}/kde4/kopete.desktop
%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-*.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-*.sh
%{_datadir}/apps/kconf_update/kopete-*.upd
%{_datadir}/apps/kopete*
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/config/kopeterc
%{_datadir}/dbus-1/interfaces/*Kopete.xml
%{_datadir}/dbus-1/interfaces/*kopete*.xml
%{_iconsdir}/*/*/*/*.mng
%{_iconsdir}/*/*/*/*.png
%{_iconsdir}/*/*/*/*.svgz
%{_datadir}/kde4/services/*.protocol
%{_datadir}/kde4/services/*.desktop
%{_datadir}/kde4/services/kconfiguredialog
%{_datadir}/kde4/servicetypes/*.desktop
%{_datadir}/sounds/Kopete*.ogg

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkopete*.so
%attr(755,root,root) %{_libdir}/libkyahoo.so
%attr(755,root,root) %{_libdir}/liboscar.so
%{_includedir}/kopete
