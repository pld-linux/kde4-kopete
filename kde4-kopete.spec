# TODO:
# - add missing obsoletes and such

%define		_state		stable
%define		orgname		kopete
%define		qtver		4.8.3

Summary:	Multi-protocol plugin-based instant messenger
Summary(pl.UTF-8):	Komunikator obsługujący wiele protokołów
Name:		kde4-kopete
Version:	4.14.3
Release:	12
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
BuildRequires:	meanwhile-devel
BuildRequires:	mediastreamer-devel >= 2.3.0
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	ortp-devel >= 0.16.1-3
BuildRequires:	qca2-devel >= 2.0.0
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
