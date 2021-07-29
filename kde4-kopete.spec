#
# Conditional build:
%bcond_with	npapi	# NPAPI browser plugin (skypebuttons)

%define		orgname		kopete
%define		qt_ver		4.8.3

Summary:	Multi-protocol plugin-based instant messenger
Summary(pl.UTF-8):	Komunikator obsługujący wiele protokołów
Name:		kde4-kopete
Version:	4.14.3
Release:	12
License:	GPL v2+ with OpenSSL exception (kopete), LGPL v2+ (libkopete)
Group:		X11/Applications
Source0:	https://download.kde.org/Attic/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	d05e478101292ebb08da2af00d1329ab
Patch0:		%{name}-FindLibgadu.patch
Patch2:		mediastreamer.patch
Patch3:		gcc6.patch
Patch4:		macros.patch
Patch5:		%{name}-qt.patch
URL:		https://kde.org/
BuildRequires:	automoc4
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
BuildRequires:	meanwhile-devel
BuildRequires:	mediastreamer-devel >= 2.3.0
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	ortp-devel >= 0.16.1-3
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qimageblitz-devel
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	speex-devel
BuildRequires:	telepathy-qt4-devel >= 0.9.0
BuildRequires:	xmms-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXtst-devel
Obsoletes:	kde4-kdenetwork-kopete < 4.11
Obsoletes:	kde4-kdenetwork-kopete-protocol-aim < 4.11
Obsoletes:	kde4-kdenetwork-kopete-protocol-bonjour < 4.11
Obsoletes:	kde4-kdenetwork-kopete-protocol-gg < 4.11
Obsoletes:	kde4-kdenetwork-kopete-protocol-groupwise < 4.11
Obsoletes:	kde4-kdenetwork-kopete-protocol-icq < 4.11
Obsoletes:	kde4-kdenetwork-kopete-protocol-jabber < 4.11
Obsoletes:	kde4-kdenetwork-kopete-protocol-meanwhile < 4.11
Obsoletes:	kde4-kdenetwork-kopete-protocol-msn < 4.11
Obsoletes:	kde4-kdenetwork-kopete-protocol-skype < 4.11
Obsoletes:	kde4-kdenetwork-kopete-protocol-sms < 4.11
Obsoletes:	kde4-kdenetwork-kopete-protocol-testbed < 4.11
Obsoletes:	kde4-kdenetwork-kopete-protocol-winpopup < 4.11
Obsoletes:	kde4-kdenetwork-kopete-protocol-wlm < 4.11
Obsoletes:	kde4-kdenetwork-kopete-protocol-yahoo < 4.11
Obsoletes:	kde4-kdenetwork-kopete-tool-alias < 4.11
Obsoletes:	kde4-kdenetwork-kopete-tool-autoaway < 4.11
Obsoletes:	kde4-kdenetwork-kopete-tool-autoreplace < 4.11
Obsoletes:	kde4-kdenetwork-kopete-tool-avdeviceconfig < 4.11
Obsoletes:	kde4-kdenetwork-kopete-tool-contactnotes < 4.11
Obsoletes:	kde4-kdenetwork-kopete-tool-highlight < 4.11
Obsoletes:	kde4-kdenetwork-kopete-tool-history < 4.11
Obsoletes:	kde4-kdenetwork-kopete-tool-importer < 4.11
Obsoletes:	kde4-kdenetwork-kopete-tool-latex < 4.11
Obsoletes:	kde4-kdenetwork-kopete-tool-motionaway < 4.11
Obsoletes:	kde4-kdenetwork-kopete-tool-nowlistening < 4.11
Obsoletes:	kde4-kdenetwork-kopete-tool-spellcheck < 4.11
Obsoletes:	kde4-kdenetwork-kopete-tool-texteffect < 4.11
Obsoletes:	kde4-kdenetwork-kopete-tool-translator < 4.11
Obsoletes:	kde4-kdenetwork-kopete-tool-webpresence < 4.11
Obsoletes:	kde4-kdenetwork-libkopete < 4.11
Obsoletes:	kde4-kdenetwork-libkopete_oscar < 4.11
Obsoletes:	kde4-kdenetwork-libkopete_otr < 4.11
Obsoletes:	kde4-kdenetwork-libkopete_videodevice < 4.11
Obsoletes:	kdenetwork-libkopete < 10:4
Obsoletes:	kdenetwork-libkopete_msn < 10:4
Obsoletes:	kdenetwork-libkopete_videodevice < 10:4
Obsoletes:	kdenetwork-libkopete_oscar < 10:4
Obsoletes:	kdenetwork-kopete < 10:4
Obsoletes:	kdenetwork-kopete-protocol-aim < 10:4
Obsoletes:	kdenetwork-kopete-protocol-gg < 10:4
Obsoletes:	kdenetwork-kopete-protocol-groupwise < 10:4
Obsoletes:	kdenetwork-kopete-protocol-icq < 10:4
Obsoletes:	kdenetwork-kopete-protocol-irc < 10:4
Obsoletes:	kdenetwork-kopete-protocol-jabber < 10:4
Obsoletes:	kdenetwork-kopete-protocol-meanwhile < 10:4
Obsoletes:	kdenetwork-kopete-protocol-msn < 10:4
Obsoletes:	kdenetwork-kopete-protocol-skype < 10:4
Obsoletes:	kdenetwork-kopete-protocol-sms < 10:4
Obsoletes:	kdenetwork-kopete-protocol-winpopup < 10:4
Obsoletes:	kdenetwork-kopete-protocol-yahoo < 10:4
Obsoletes:	kdenetwork-kopete-protocol-testbed < 10:4
Obsoletes:	kdenetwork-kopete-tool-alias < 10:4
Obsoletes:	kdenetwork-kopete-tool-autoaway < 10:4
Obsoletes:	kdenetwork-kopete-tool-autoreplace < 10:4
Obsoletes:	kdenetwork-kopete-tool-avdeviceconfig < 10:4
Obsoletes:	kdenetwork-kopete-tool-conectionstatus < 10:4
Obsoletes:	kdenetwork-kopete-tool-contactnotes < 10:4
Obsoletes:	kdenetwork-kopete-tool-cryptography < 10:4
Obsoletes:	kdenetwork-kopete-tool-highlight < 10:4
Obsoletes:	kdenetwork-kopete-tool-history < 10:4
Obsoletes:	kdenetwork-kopete-tool-importer < 10:4
Obsoletes:	kdenetwork-kopete-tool-latex < 10:4
Obsoletes:	kdenetwork-kopete-tool-motionaway < 10:4
Obsoletes:	kdenetwork-kopete-tool-nowlistening < 10:4
Obsoletes:	kdenetwork-kopete-tool-smpppdcs < 10:4
Obsoletes:	kdenetwork-kopete-tool-spellcheck < 10:4
Obsoletes:	kdenetwork-kopete-tool-texteffect < 10:4
Obsoletes:	kdenetwork-kopete-tool-translator < 10:4
Obsoletes:	kdenetwork-kopete-tool-webpresence < 10:4
Obsoletes:	kopete < 1
Obsoletes:	kopete-designer < 1
Obsoletes:	kopete-libkopete < 1
Obsoletes:	kopete-libkopete_msn < 1
Obsoletes:	kopete-libkopete_videodevice < 1
Obsoletes:	kopete-libkopete_oscar < 1
Obsoletes:	kopete-plugin-protocols-aim < 1
Obsoletes:	kopete-plugin-protocols-gg < 1
Obsoletes:	kopete-plugin-protocols-icq < 1
Obsoletes:	kopete-plugin-protocols-irc < 1
Obsoletes:	kopete-plugin-protocols-jabber < 1
Obsoletes:	kopete-plugin-protocols-msn < 1
Obsoletes:	kopete-plugin-protocols-oscar < 1
Obsoletes:	kopete-plugin-protocols-sms < 1
Obsoletes:	kopete-plugin-protocols-winpopup < 1
Obsoletes:	kopete-plugin-protocols-yahoo < 1
Obsoletes:	kopete-plugin-tools-autoaway < 1
Obsoletes:	kopete-plugin-tools-autoreplace < 1
Obsoletes:	kopete-plugin-tools-conectionstatus < 1
Obsoletes:	kopete-plugin-tools-contactnotes < 1
Obsoletes:	kopete-plugin-tools-cryptography < 1
Obsoletes:	kopete-plugin-tools-highlight < 1
Obsoletes:	kopete-plugin-tools-history < 1
Obsoletes:	kopete-plugin-tools-importer < 1
Obsoletes:	kopete-plugin-tools-motionaway < 1
Obsoletes:	kopete-plugin-tools-nowlistening < 1
Obsoletes:	kopete-plugin-tools-spellcheck < 1
Obsoletes:	kopete-plugin-tools-texteffect < 1
Obsoletes:	kopete-plugin-tools-translator < 1
Obsoletes:	kopete-plugin-tools-webpresence < 1
Obsoletes:	kopete-protocol-aim < 1
Obsoletes:	kopete-protocol-gg < 1
Obsoletes:	kopete-protocol-groupwise < 1
Obsoletes:	kopete-protocol-icq < 1
Obsoletes:	kopete-protocol-irc < 1
Obsoletes:	kopete-protocol-jabber < 1
Obsoletes:	kopete-protocol-meanwhile < 1
Obsoletes:	kopete-protocol-msn < 1
Obsoletes:	kopete-protocol-sms < 1
Obsoletes:	kopete-protocol-winpopup < 1
Obsoletes:	kopete-protocol-yahoo < 1
Obsoletes:	kopete-tool-alias < 1
Obsoletes:	kopete-tool-autoaway < 1
Obsoletes:	kopete-tool-autoreplace < 1
Obsoletes:	kopete-tool-avdeviceconfig < 1
Obsoletes:	kopete-tool-connectionstatus < 1
Obsoletes:	kopete-tool-contactnotes < 1
Obsoletes:	kopete-tool-cryptography < 1
Obsoletes:	kopete-tool-highlight < 1
Obsoletes:	kopete-tool-history < 1
Obsoletes:	kopete-tool-importer < 1
Obsoletes:	kopete-tool-latex < 1
Obsoletes:	kopete-tool-motionaway < 1
Obsoletes:	kopete-tool-nowlistening < 1
Obsoletes:	kopete-tool-smpppdcs < 1
Obsoletes:	kopete-tool-spellcheck < 1
Obsoletes:	kopete-tool-texteffect < 1
Obsoletes:	kopete-tool-translator < 1
Obsoletes:	kopete-tool-webpresence < 1
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
License:	LGPL v2+
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{version}
Obsoletes:	kopete-devel < 1

%description devel
kopete header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe kopete.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão para compilar aplicações que usem as bibliotecas
do kopete.

%package -n browser-plugin-kde4-kopete-skypebuttons
Summary:	Skypebuttons plugin for NPAPI compatible browsers
Summary(pl.UTF-8):	Wtyczka skypebuttons dla przeglądarek zgodnych z NPAPI
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description -n browser-plugin-kde4-kopete-skypebuttons
Skypebuttons plugin for NPAPI compatible browsers.

%description -n browser-plugin-kde4-kopete-skypebuttons -l pl.UTF-8
Wtyczka skypebuttons dla przeglądarek zgodnych z NPAPI.

%prep
%setup -q -n %{orgname}-%{version}
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
install -d build
cd build
%cmake .. \
	%{!?with_npapi:-DBUILD_skypebuttons=OFF} \
	-DMOZPLUGIN_INSTALL_DIR=%{_browserpluginsdir} \
	-DWITH_libjingle=OFF

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
%doc COPYING README TODO
%attr(755,root,root) %{_bindir}/kopete
%attr(755,root,root) %{_bindir}/kopete_latexconvert.sh
%attr(755,root,root) %{_bindir}/winpopup-install
%attr(755,root,root) %{_bindir}/winpopup-send
%attr(755,root,root) %{_libdir}/libkopete.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopete.so.4
%attr(755,root,root) %{_libdir}/libkopete_oscar.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopete_oscar.so.4
%attr(755,root,root) %{_libdir}/libkopete_otr_shared.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopete_otr_shared.so.1
%attr(755,root,root) %{_libdir}/libkopete_videodevice.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopete_videodevice.so.4
%attr(755,root,root) %{_libdir}/libkopeteaddaccountwizard.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopeteaddaccountwizard.so.1
%attr(755,root,root) %{_libdir}/libkopetechatwindow_shared.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopetechatwindow_shared.so.1
%attr(755,root,root) %{_libdir}/libkopetecontactlist.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopetecontactlist.so.1
%attr(755,root,root) %{_libdir}/libkopeteidentity.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopeteidentity.so.1
%attr(755,root,root) %{_libdir}/libkopeteprivacy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopeteprivacy.so.1
%attr(755,root,root) %{_libdir}/libkopetestatusmenu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopetestatusmenu.so.1
%attr(755,root,root) %{_libdir}/libkyahoo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkyahoo.so.1
%attr(755,root,root) %{_libdir}/liboscar.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboscar.so.1
%attr(755,root,root) %{_libdir}/libqgroupwise.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_accountconfig.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_addbookmarks.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_appearanceconfig.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_autoreplace.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_avdeviceconfig.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_behaviorconfig.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_chatwindowconfig.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_highlight.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_history.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_history2.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_latex.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_nowlistening.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_otr.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_pipes.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_pluginconfig.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_privacy.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_statusconfig.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_texteffect.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_translator.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_urlpicpreview.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_webpresence.so
%attr(755,root,root) %{_libdir}/kde4/kopete_addbookmarks.so
%attr(755,root,root) %{_libdir}/kde4/kopete_aim.so
%attr(755,root,root) %{_libdir}/kde4/kopete_autoreplace.so
%attr(755,root,root) %{_libdir}/kde4/kopete_bonjour.so
%attr(755,root,root) %{_libdir}/kde4/kopete_chatwindow.so
%attr(755,root,root) %{_libdir}/kde4/kopete_contactnotes.so
%attr(755,root,root) %{_libdir}/kde4/kopete_emailwindow.so
%attr(755,root,root) %{_libdir}/kde4/kopete_gadu.so
%attr(755,root,root) %{_libdir}/kde4/kopete_groupwise.so
%attr(755,root,root) %{_libdir}/kde4/kopete_highlight.so
%attr(755,root,root) %{_libdir}/kde4/kopete_history.so
%attr(755,root,root) %{_libdir}/kde4/kopete_history2.so
%attr(755,root,root) %{_libdir}/kde4/kopete_icq.so
%attr(755,root,root) %{_libdir}/kde4/kopete_jabber.so
%attr(755,root,root) %{_libdir}/kde4/kopete_latex.so
%attr(755,root,root) %{_libdir}/kde4/kopete_meanwhile.so
%attr(755,root,root) %{_libdir}/kde4/kopete_nowlistening.so
%attr(755,root,root) %{_libdir}/kde4/kopete_otr.so
%attr(755,root,root) %{_libdir}/kde4/kopete_pipes.so
%attr(755,root,root) %{_libdir}/kde4/kopete_privacy.so
%attr(755,root,root) %{_libdir}/kde4/kopete_qq.so
%attr(755,root,root) %{_libdir}/kde4/kopete_skype.so
%attr(755,root,root) %{_libdir}/kde4/kopete_sms.so
%attr(755,root,root) %{_libdir}/kde4/kopete_statistics.so
%attr(755,root,root) %{_libdir}/kde4/kopete_testbed.so
%attr(755,root,root) %{_libdir}/kde4/kopete_texteffect.so
%attr(755,root,root) %{_libdir}/kde4/kopete_translator.so
%attr(755,root,root) %{_libdir}/kde4/kopete_urlpicpreview.so
%attr(755,root,root) %{_libdir}/kde4/kopete_webpresence.so
%attr(755,root,root) %{_libdir}/kde4/kopete_wlm.so
%attr(755,root,root) %{_libdir}/kde4/kopete_wp.so
%attr(755,root,root) %{_libdir}/kde4/kopete_yahoo.so
%attr(755,root,root) %{_libdir}/kde4/libchattexteditpart.so
%attr(755,root,root) %{_libdir}/kde4/plugins/accessible/chatwindowaccessiblewidgetfactory.so
%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-*.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-*.sh
%{_datadir}/apps/kconf_update/kopete-*.upd
%{_datadir}/apps/kopete
%{_datadir}/apps/kopete_contactnotes
%{_datadir}/apps/kopete_groupwise
%{_datadir}/apps/kopete_history
%{_datadir}/apps/kopete_history2
%{_datadir}/apps/kopete_jabber
%{_datadir}/apps/kopete_latex
%{_datadir}/apps/kopete_otr
%{_datadir}/apps/kopete_privacy
%{_datadir}/apps/kopete_skype
%{_datadir}/apps/kopete_statistics
%{_datadir}/apps/kopete_translator
%{_datadir}/apps/kopete_wlm
%{_datadir}/apps/kopete_yahoo
%{_datadir}/apps/kopeterichtexteditpart
%{_datadir}/config/kopeterc
%{_datadir}/config.kcfg/history2config.kcfg
%{_datadir}/config.kcfg/historyconfig.kcfg
%{_datadir}/config.kcfg/kopete_otr.kcfg
%{_datadir}/config.kcfg/kopeteappearancesettings.kcfg
%{_datadir}/config.kcfg/kopetebehaviorsettings.kcfg
%{_datadir}/config.kcfg/kopetestatussettings.kcfg
%{_datadir}/config.kcfg/latexconfig.kcfg
%{_datadir}/config.kcfg/nowlisteningconfig.kcfg
%{_datadir}/config.kcfg/translatorconfig.kcfg
%{_datadir}/config.kcfg/urlpicpreview.kcfg
%{_datadir}/config.kcfg/webpresenceconfig.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.Kopete.xml
%{_datadir}/dbus-1/interfaces/org.kde.kopete.Client.xml
%{_datadir}/dbus-1/interfaces/org.kde.kopete.Statistics.xml
%{_datadir}/kde4/services/aim.protocol
%{_datadir}/kde4/services/callto.protocol
%{_datadir}/kde4/services/skype.protocol
%{_datadir}/kde4/services/tel.protocol
%{_datadir}/kde4/services/xmpp.protocol
%{_datadir}/kde4/services/chatwindow.desktop
%{_datadir}/kde4/services/emailwindow.desktop
%{_datadir}/kde4/services/kopete_*.desktop
%{_datadir}/kde4/services/kconfiguredialog
%{_datadir}/kde4/servicetypes/kopeteplugin.desktop
%{_datadir}/kde4/servicetypes/kopeteprotocol.desktop
%{_datadir}/kde4/servicetypes/kopeteui.desktop
%{_datadir}/sounds/Kopete_*.ogg
%{_desktopdir}/kde4/kopete.desktop
%{_iconsdir}/hicolor/*x*/apps/kopete*.png
%{_iconsdir}/hicolor/scalable/apps/kopete*.svgz
%{_iconsdir}/oxygen/*x*/actions/account_offline_overlay.png
%{_iconsdir}/oxygen/*x*/actions/contact_*_overlay.png
%{_iconsdir}/oxygen/*x*/actions/emoticon.png
%{_iconsdir}/oxygen/*x*/actions/im-status-message-edit.png
%{_iconsdir}/oxygen/*x*/actions/metacontact_unknown.png
%{_iconsdir}/oxygen/*x*/actions/status_unknown.png
%{_iconsdir}/oxygen/*x*/actions/status_unknown_overlay.png
%{_iconsdir}/oxygen/*x*/actions/view-user-offline-kopete.png
%{_iconsdir}/oxygen/*x*/actions/voicecall.png
%{_iconsdir}/oxygen/*x*/actions/webcamreceive.png
%{_iconsdir}/oxygen/*x*/actions/webcamsend.png
%{_iconsdir}/oxygen/22x22/status/object-locked-*.png
%{_iconsdir}/oxygen/32x32/actions/newmessage.mng
%{_iconsdir}/oxygen/48x48/actions/mail-encrypt.png
%{_iconsdir}/oxygen/scalable/actions/account_offline_overlay.svgz
%{_iconsdir}/oxygen/scalable/actions/im-status-message-edit.svgz
%{_iconsdir}/oxygen/scalable/actions/mail-encrypt.svgz
%{_iconsdir}/oxygen/scalable/actions/view-user-offline-kopete.svgz
%{_iconsdir}/oxygen/scalable/actions/voicecall.svgz
%{_iconsdir}/oxygen/scalable/actions/webcamreceive.svgz
%{_iconsdir}/oxygen/scalable/actions/webcamsend.svgz
%{_iconsdir}/oxygen/scalable/status/object-locked-*.svgz

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkopete*.so
%attr(755,root,root) %{_libdir}/libkyahoo.so
%attr(755,root,root) %{_libdir}/liboscar.so
%{_includedir}/kopete

%if %{with npapi}
%files -n browser-plugin-kde4-kopete-skypebuttons
%defattr(644,root,root,755)
%attr(755,root,root) %{_browserpluginsdir}/skypebuttons.so
%endif
