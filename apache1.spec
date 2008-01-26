# TODO:
# - update errordocs to use MultiViews (like Apache 2) instead of dual language pages
# - replace linux_pwd.gif by e.g. http://pl.docs.pld-linux.org/zrzuty_ekr/logo_04.png
# - then drop Source3
#
# Conditional build:
%bcond_with	rewrite_ldap	# enable ldap map support for mod_rewrite (alpha)
%bcond_without	ipv6		# disable IPv6 support
%bcond_without	lingerd		# don't build lingerd support
#
%include	/usr/lib/rpm/macros.perl
Summary:	The most widely used Web server on the Internet
Summary(cs.UTF-8):	Nejrozšířenější WWW server v Internetu
Summary(da.UTF-8):	Den mest brugte web-tjener på Internet
Summary(de.UTF-8):	Der am häufigsten verwendete Web-Server im Internet
Summary(es.UTF-8):	El servidor web más conocido y usado en Internet
Summary(fr.UTF-8):	Le serveur Web le plus utilisé sur Internet
Summary(id.UTF-8):	Web server yang paling banyak digunakan di Internet
Summary(is.UTF-8):	Vinsælasti vefþjónninn á Netinu
Summary(it.UTF-8):	Il web server più diffuso su Internet
Summary(ja.UTF-8):	インターネット上で最も一般的に使用されている Web サーバー
Summary(nb.UTF-8):	Den mest utbredte web-tjeneren på Internett
Summary(pl.UTF-8):	Serwer WWW (World Wide Web)
Summary(pt.UTF-8):	O servidor Web mais largamente utilizado em toda a Internet
Summary(pt_BR.UTF-8):	Servidor HTTPD para prover serviços WWW
Summary(ru.UTF-8):	Самый популярный Web-Server
Summary(sk.UTF-8):	Najviac používaný Web server na Internete
Summary(sl.UTF-8):	Najbolj uporabljani spletni strežnik interneta
Summary(sv.UTF-8):	Den mest använda webbservern på Internet
Summary(tr.UTF-8):	Lider WWW tarayıcı
Summary(uk.UTF-8):	Найпопулярніший Web-Server
Summary(zh_CN.UTF-8):	Internet 上应用最广泛的 Web 服务程序。
Name:		apache1
Version:	1.3.41
Release:	1
License:	Apache Group
Group:		Networking/Daemons
Source0:	http://www.apache.org/dist/httpd/apache_%{version}.tar.gz
# Source0-md5:	f7f00b635243f03a787ca9f4d4c85651
Source1:	%{name}.init
Source2:	%{name}.logrotate
Source3:	apache-icons.tar.gz
# Source3-md5:	2b085cbc19fd28536dc883f0b864cd83
Source4:	%{name}.sysconfig
Source5:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/apache-non-english-man-pages.tar.bz2
# Source5-md5:	74ff6e8d8a7b365b48ed10a52fbeb84e
Source6:	%{name}-defaultindex.conf
Source7:	%{name}-httpd.conf
Source8:	%{name}-common.conf
Source9:	%{name}-mod_status.conf
Source10:	%{name}-mod_proxy.conf
Source11:	%{name}-mod_autoindex.conf
Source12:	%{name}-mod_dir.conf
Source13:	%{name}-mod_info.conf
Source14:	%{name}-mod_log_config.conf
Source15:	%{name}-mod_userdir.conf
Source16:	%{name}-mod_mime_magic.conf
Source17:	%{name}-mod_alias.conf
Source18:	%{name}-mod_negotiation.conf
Source19:	%{name}-mod_mime.conf
Source20:	%{name}-mod_actions.conf
Source21:	%{name}-mod_cern_meta.conf
Source22:	%{name}-mod_setenvif.conf
Source23:	%{name}-mod_vhost_alias.conf
Source24:	%{name}-errordocs.conf
# http://www.iagora.com/about/software/lingerd/
Source25:	http://images.iagora.com/media/software/lingerd/lingerd-0.94.tar.gz
# Source25-md5:	6401015bafad4f44fdf8a9a1795d9258
Source26:	%{name}-manual.conf
Patch0:		%{name}-PLD.patch
Patch1:		%{name}-suexec.patch
Patch2:		%{name}-errordocs.patch
Patch3:		%{name}-apxs.patch
Patch4:		%{name}-mod_ssl-addon.patch
Patch5:		%{name}-mod_ssl-eapi.patch
# http://allafrica.com/tools/apache/mod_proxy/mod_proxy-khk_1.3.26-patch.diff with eapi duplicates removed
Patch6:		%{name}-mod_proxy-khk.patch
Patch7:		%{name}-EAPI_MM_CORE_PATH-correction.patch
Patch8:		%{name}-EAPI_MM=SYSTEM.patch
Patch9:		%{name}-ipv6-PLD.patch
Patch10:	%{name}-modules_symbols.patch
Patch11:	%{name}-apxs_force_rm_cp.patch
Patch12:	%{name}-db3.patch
Patch13:	%{name}-lookup_map_ldap.patch
Patch14:	%{name}-man.patch
Patch15:	%{name}-fpic.patch
Patch16:	%{name}-buff.patch
Patch17:	%{name}-mkstemp.patch
Patch18:	%{name}-EAPI-missing_files.patch
Patch19:	%{name}-PLD-nov6.patch
Patch20:	%{name}-configdir_skip_backups.patch
Patch21:	%{name}-apxs-quiet.patch
Patch22:	%{name}-db4.patch
Patch23:	%{name}-less-libs.patch
Patch24:	%{name}-rwrite-debug.patch
Patch25:	%{name}-apxs-DESTDIR.patch
# from debian apache_1.3.34-2.diff.gz
Patch26:	%{name}-regex_must_conform_to_posix_for_LFS_to_work.patch
Patch27:	%{name}-suexec_of_death.patch
Patch28:	%{name}-suexec_reopenlog.patch
Patch29:	%{name}-autoindex_studly.patch
Patch30:	%{name}-autoindex_indexes.patch
Patch31:	%{name}-autoindex_generator.patch
Patch32:	%{name}-ab.8_formatting_error.patch
Patch33:	%{name}-proxy_content_base.patch
Patch34:	%{name}-inetdfix.patch
Patch35:	%{name}-configure_hashbang.patch
Patch36:	%{name}-log_files_permission.patch
Patch37:	%{name}-htpasswd_do_not_trash_extra_fields.patch
Patch38:	%{name}-GNU_xargs.patch
Patch39:	%{name}-security_htdigest_local_buffer_overflow.patch
Patch40:	%{name}-security_htpasswd_user_buffer_overflow.patch
Patch41:	%{name}-security_check_forensic_tempfiles.patch
Patch42:	%{name}-lingerd.patch
URL:		http://httpd.apache.org/
BuildRequires:	bash
BuildRequires:	db-devel >= 4.1
BuildRequires:	mm-devel >= 1.3.0
%{?with_rewrite_ldap:BuildRequires:	openldap-devel >= 2.4.6}
BuildRequires:	perl-base
BuildRequires:	rpm-build >= 4.4.0
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	%{name}-mod_access = %{version}-%{release}
Requires:	%{name}-mod_alias = %{version}-%{release}
Requires:	%{name}-mod_dir = %{version}-%{release}
Requires:	%{name}-mod_log_config = %{version}-%{release}
Requires:	%{name}-mod_mime = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/apache
%define		_includedir	%{_prefix}/include/%{name}
%define		_libexecdir	%{_prefix}/%{_lib}/%{name}
%define		apxs		/usr/sbin/apxs1
%define		httpdir		/home/services/apache
%define		docroot		%{_datadir}/%{name}/html
%define		manualdir	%{_datadir}/%{name}/manual
%define		cgibindir	%{_prefix}/lib/cgi-bin/%{name}

%description
Apache is a powerful, full-featured, efficient and freely-available
Web server. Apache is also the most popular Web server on the
Internet.

%{?with_lingerd:This version of Apache includes lingerd support:}
%{?with_lingerd:<http://www.iagora.com/about/software/lingerd/>.}

%description -l cs.UTF-8
Apache je výkonný plně funkční efektivní a volně dostupný WWW server.
Je to nejpopulárnější WWW server v Internetu.

%description -l da.UTF-8
Apache er en stærk, funktionsrig, effektiv og frit tilgængelig
web-tjener. Apache er også den mest populære web-tjener på Internet.

%description -l de.UTF-8
Apache ist ein leistungsfähiger, frei verfügbarer und effizienter
Web-Server mit umfassenden Funktionen. Apache ist zudem der populärste
Web-Server im Internet.

%description -l es.UTF-8
El servidor web Apache es el mejor servidor gratuito disponible en el
mundo UNIX hoy. Usa HTTP (HyperText Transfer Protocol) para permitir
que browsers web vean documentos y sometan datos remotamente. Puede
ejecutar varias funciones diferentes, incluyendo funciones de proxy y
caché, y nos ofrece características como monitor de estado, conversión
dinámica de tipo, y otras más.

%description -l fr.UTF-8
Apache est un serveur Web puissant, efficace, gratuit et complet.
Apache est aussi le serveur Web le plus populaire sur Internet.

%description -l id.UTF-8
Apache adalah Web server yang powerful, efisien, kaya akan feature,
dan tersedia dengan free. Apache juga merupakan Web server yang paling
populer di Internet.

%description -l is.UTF-8
Apache er mjög öflugur og háþróaður vefþjónn sem er ókeypis. Apache er
einnig mest notaði vefþjónninn á Internetinu.

%description -l it.UTF-8
Apache è un Web server potente, dotato di tutte le caratteristiche,
efficiente e gratuito. Ed è anche il web server più diffuso su
Internet.

%description -l ja.UTF-8
Apache は強力で充実した機能を持つ無償の Web サーバー
です。また、apache はインターネット上で最も一般的に使用 されている Web
サーバーです。

%description -l nb.UTF-8
Apache er en kraftig, funksjonsrik, effektiv og fritt tilgjengelig
web-tjener. Apache er også den mest populære web-tjeneren på Internet.

%description -l pl.UTF-8
Apache jest serwerem WWW (World Wide Web). Instalując ten pakiet
będziesz mógł prezentować własne strony WWW w sieci internet.

%description -l pt.UTF-8
O Apache é um servidor de Web poderoso, cheio de potencialidades,
eficiente e gratuito. O Apache é também o servidor Web mais conhecido
na Internet.

%description -l pt_BR.UTF-8
O servidor web Apache é o melhor servidor gratuito disponível no mundo
UNIX hoje. Ele usa HTTP (HyperText Transfer Protocol) para permitir
que browsers web vejam documentos e submetam dados remotamente. Ele
pode executar várias funções diferentes, incluindo funções de proxy e
cache, e oferece características como monitor de status, conversão
dinâmica de tipo, e mais.

%description -l ru.UTF-8
Apache - это мощный, полнофункциональный, эффективный, свободно
распространяемый и самый популярный в Internet WWW-сервер.

%description -l sk.UTF-8
Apache je výkonný, efektívny a voľne dostupný Web server, bohatý na
funkcie. Apache je tiež najpopulárnejším Web serverom na Internete.

%description -l sv.UTF-8
Apache är en kraftfull, finessrik, effektiv och fritt tillgänglig
webbserver. Apache är också den populäraste webbservern på Internet.

%description -l tr.UTF-8
Apache serbest dağıtılan ve çok kullanılan yetenekli bir web
sunucusudur.

%description -l zh_CN.UTF-8
Apache 是功能强劲齐全、高效且免费提供的 Web 服务程序， 同时也是
Internet 上最流行的 Web 服务程序。

如果您需要 Web 服务程序，请安装 apache 软件包。

%package base
Summary:	The most widely used Web server on the Internet
Summary(pl.UTF-8):	Serwer WWW (World Wide Web)
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getent
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(pre):	/usr/sbin/usermod
Requires(pre):	textutils
Requires(triggerpostun):	sed >= 4.0
Requires:	/etc/mime.types
Requires:	mailcap
Requires:	psmisc >= 20.1
Requires:	rc-scripts
Requires:	webapps
Provides:	%{name}(EAPI) = %{version}-%{release}
%{?with_ipv6:Provides:	apache1(ipv6)}
%{?with_lingerd:Provides:	apache1(lingerd)}
Provides:	group(http)
Provides:	user(http)
Provides:	webserver = apache
Obsoletes:	apache < 2.0.0
Obsoletes:	apache-extra
Obsoletes:	apache6
Conflicts:	apache1 < 1.3.37-4
Conflicts:	apache1-mod_ssl < 2.8.30_1.3.39-3
Conflicts:	logrotate < 3.7-4
# for the posttrans scriptlet, conflicts because in vserver environment rpm package is not installed.
Conflicts:	rpm < 4.4.2-0.2

%description base
Apache is a powerful, full-featured, efficient and freely-available
Web server. Apache is also the most popular Web server on the
Internet.

%description base -l pl.UTF-8
Apache jest potężnym, w pełni funkcjonalnym, wydajnym i wolnodostępnym
serwerem WWW (World Wide Web). Jest także najbardziej popularnym
serwerem WWW w Internecie.

%package suexec
Summary:	Apache suexec wrapper
Summary(pl.UTF-8):	Suexec wrapper do serwera WWW Apache
Summary(ru.UTF-8):	Apache suEXEC CGI wrapper
Summary(uk.UTF-8):	Apache suEXEC CGI wrapper
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Obsoletes:	apache-suexec < 2.0.0

%description suexec
The suEXEC feature provides Apache users the ability to run CGI and
SSI programs under user IDs different from the user ID of the calling
web-server. Normally, when a CGI or SSI program executes, it runs as
the same user who is running the web server.

%description suexec -l pl.UTF-8
SuEXEC umożliwia serwerowi Apache uruchamianie programów CGI i SSI z
innym UID niż wywołujący je serwer. Normalnie programy CGI i SSI są
wykonywane jako taki sam użytkownik jak serwer WWW.

%description suexec -l ru.UTF-8
Пакет suEXEC позволяет запускать CGI-программы под user-id, отличными
от того, под которым работает вызывающий их web-сервер. Будучи
правильно использованным, этот пакет позволяет заметно снизить риск
нарушения системной безопасности, вызванный разрешением запуска
пользователям CGI-программ. Вместе с тем, будучи неправильно
сконфигурированным, этот пакет может разрушить вашу систему, сжечь ваш
дом и украсть деньги из вашего пенсионного фонда :)). Если вы не
имеете опыта работы с setuid root программами и проблемами системной
безопасности, порожденными их применением, настоятельно рекомендуем не
использовать этого пакета...

%description suexec -l uk.UTF-8
Пакет suEXEC дозволяє запускати CGI-програми під user-id, відмінним
від того, під яким працює сервер. При правильному використанні, цей
пакет дозволяє помітно знизити ризик порушення системної безпеки,
викликаний дозволом запуску користувачами CGI-програм. Разом з тим,
при невірному конфігуруванні, цей пакет може зруйнувати ваши систему,
спалити ваш дім і вкрасти гроші з вашого пенсійного фонду :)). Якщо ви
не маєте досвіду роботи з setuid root програмами та проблемами
системної безпеки, котрі породжені використанням таких програм,
настійливо радимо не використовувати цього пакету...

%package tools
Summary:	Apache tools
Summary(pl.UTF-8):	Narzędzia Apache'a
Group:		Development/Tools

%description tools
Apache tools.

%description tools -l pl.UTF-8
Narzędzia Apache'a.

%package defaultindex
Summary:	Apache index.html* files
Summary(pl.UTF-8):	Pliki Apache index.html*
Group:		Documentation
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_alias = %{version}-%{release}
Requires:	%{name}-mod_dir = %{version}-%{release}
Provides:	apache1-index
Obsoletes:	apache1-index < 1.3.39-7.9
Obsoletes:	indexhtml

%description defaultindex
Apache index.html* files.

%description defaultindex -l pl.UTF-8
Pliki Apache index.html*.

%package manual
Summary:	Apache 1.3.x manual
Summary(pl.UTF-8):	Podręcznik do Apache'a 1.3.x
Group:		Documentation
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_alias = %{version}-%{release}
Requires:	%{name}-mod_negotiation = %{version}-%{release}
Provides:	apache1-doc
Obsoletes:	apache1-doc < 1.3.39-7.9

%description manual
Apache 1.3.x manual.

%description manual -l pl.UTF-8
Podręcznik do Apache'a 1.3.x.

%package errordocs
Summary:	Apache 1.3.x HTTP error documents
Summary(pl.UTF-8):	Dokumenty opisujące błędy HTTP dla Apache'a 1.3.x
Group:		Applications/WWW
Requires:	%{name}-mod_include = %{version}-%{release}

%description errordocs
Apache 1.3.x HTTP error documents. Currently in English and Polish
only.

%description errordocs -l pl.UTF-8
Dokumenty opisujące błędy HTTP dla Apache'a 1.3.x. Aktualnie tylko po
angielsku i polsku.

%package devel
Summary:	Module development tools for the Apache web server
Summary(cs.UTF-8):	Hlavičkové soubory pro Apache Web server
Summary(da.UTF-8):	Header-filer for Apache webserveren
Summary(de.UTF-8):	Include-Dateien für den Apache Web-Server
Summary(es.UTF-8):	Archivos de inclusión del Apache para desarrollo de módulos
Summary(fr.UTF-8):	Fichiers à inclure pour le serveur Web Apache
Summary(id.UTF-8):	File header untuk Apache Web server
Summary(is.UTF-8):	Hausaskrár með Apache vefþjóninum
Summary(it.UTF-8):	File include per il web server Apache
Summary(ja.UTF-8):	Apache Web サーバー用の開発ツール
Summary(nb.UTF-8):	Headerfiler for webtjeneren Apache
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia modułów rozszerzeń do serwera WWW Apache
Summary(pt.UTF-8):	Ficheiros de inclusão para o servidor Web Apache
Summary(pt_BR.UTF-8):	Arquivos de inclusão do Apache para desenvolvimento de módulos
Summary(ru.UTF-8):	Файлы заголовков для web server'а Apache
Summary(sk.UTF-8):	Hlavičkové súbory pre Apache Web server
Summary(sl.UTF-8):	Glave za spletni strežnik Apache
Summary(sv.UTF-8):	Huvudfiler för webbservern Apache
Summary(uk.UTF-8):	Засоби створення модулів для web server'у Apache
Summary(zh_CN.UTF-8):	用于 Apache Web 服务程序的开发工具。
Group:		Networking/Utilities
Provides:	%{name}(EAPI)-devel = %{version}-%{release}
Provides:	apache(EAPI)-devel = %{version}-%{release}
%{?with_ipv6:Provides:	apache1(ipv6)-devel}
Obsoletes:	apache-devel < 2.0.0
Obsoletes:	apache1-apxs

%description devel
The apache-devel package contains header files for Apache.

%description devel -l cs.UTF-8
Balíček apache-devel obsahuje hlavičkové soubory pro Apache.

%description devel -l da.UTF-8
Apache-devel pakken indeholder headerfiler for Apache.

%description devel -l de.UTF-8
Das Paket apache-devel enthält Header-Dateien für Apache.

%description devel -l es.UTF-8
Este paquete contiene los archivos de inclusión para el Apache.

%description devel -l fr.UTF-8
Le package apache-devel contient le code source pour le serveur Web
Apache.

%description devel -l id.UTF-8
Package apache-devel berisi source code dari Apache Web server.

%description devel -l is.UTF-8
Apache-devel pakkinn inniheldur frumkóða Apache vefþjónsins.

%description devel -l it.UTF-8
Il pacchetto apache-devel contiene i file header per Apache.

%description devel -l nb.UTF-8
Apache-devel pakken inneholder headerfiler for Apache.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla serwera WWW Apache.

%description devel -l pt.UTF-8
O pacote apache-devel contém outros ficheiros para o Apache.

%description devel -l pt_BR.UTF-8
Este pacote contem os arquivos de inclusão para o Apache.

%description devel -l ru.UTF-8
Пакет apache-devel содержит хедеры для Web Server'а.

%description devel -l sk.UTF-8
Balík apache-devel obsahuje zdrojový kód Apache Web servera.

%description devel -l sv.UTF-8
Paketet apache-devel innehåller huvudfilerna för Apache.

%description devel -l uk.UTF-8
Пакет apache-devel містить хедери для Web Server'а.

%package mod_access
Summary:	Access control based on client hostname or IP address
Summary(pl.UTF-8):	Kontrola dostępu w oparciu o nazwę hosta lub adres IP klienta
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_access) = %{version}-%{release}
Provides:	webserver(access)

%description mod_access
The directives provided by mod_access are used in <Directory>,
<Files>, and <Location> sections as well as .htaccess files to control
access to particular parts of the server. Access can be controlled
based on the client hostname, IP address, or other characteristics of
the client request, as captured in environment variables. The Allow
and Deny directives are used to specify which clients are or are not
allowed access to the server, while the Order directive sets the
default access state, and configures how the Allow and Deny directives
interact with each other.

%description mod_access -l pl.UTF-8
Dyrektyw dostarczanych przez mod_access można używać w sekcjach
<Directory>, <Files> i <Location>, a także plikach .htaccess w celu
kontrolowania dostępu do poszczególnych części serwera. Dostęp może
być kontrolowany w oparciu o nazwę hosta lub adres IP klienta albo
inną charakterystykę żądania klienta wychwyconą przez zmienne
środowiskowe. Dyrektywy Allow i Deny są używane w celu określenia
którzy klienci mają dostęp do serwera, a którzy go nie mają, natomiast
dyrektywa Order ustawia stan domyślny i określa sposób, w jaki
dyrektywy Allow i Deny wpływają na siebie nawzajem.

%package mod_actions
Summary:	Apache module for run CGI whenever a file of a certain type is requested
Summary(pl.UTF-8):	Moduł dla Apache'a do uruchamiania skryptów cgi
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_actions) = %{version}-%{release}
Obsoletes:	apache-mod_actions < 2.0.0

%description mod_actions
This package contains mod_actions module. This module lets you run CGI
scripts whenever a file of a certain type is requested. This makes it
much easier to execute scripts that process files.

%description mod_actions -l pl.UTF-8
Ten moduł pozwala na uruchamianie skryptów CGI w momencie gdy
nadchodzi żądanie pobrania pliku określonego typu. Znacznie ułatwia to
wykonywanie skryptów przetwarzających pliki.

%package mod_alias
Summary:	Mapping different parts of the host filesystem in the document tree, and URL redirection
Summary(pl.UTF-8):	Odwzorowywanie części systemu plików w drzewie dokumentów oraz przekierowywanie URL-i
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_alias) = %{version}-%{release}
Provides:	webserver(alias)

%description mod_alias
This module provides for mapping different parts of the host
filesystem in the document tree, and for URL redirection. The
directives contained in this module allow for manipulation and control
of URLs as requests arrive at the server. The Alias and ScriptAlias
directives are used to map between URLs and filesystem paths. This
allows for content which is not directly under the DocumentRoot to be
served as part of the web document tree. The ScriptAlias directive has
the additional effect of marking the target directory as containing
only CGI scripts.

The Redirect directives are used to instruct clients to make a new
request with a different URL. They are often used when a resource has
moved to a new location.

A more powerful and flexible set of directives for manipulating URLs
is contained in the mod_rewrite module.

%description mod_alias -l pl.UTF-8
Ten moduł umożliwia odwzorowywanie różnych części systemu plików
serwera w drzewie dokumentów oraz przekierowywanie URL-i. Dyrektywy
obsługiwane przez ten moduł umożliwiają manipulowanie i kontrolę URL-i
podczas przychodzenia żądań do serwera. Dyrektywy Alias i ScriptAlias
służą do odwzorowywania pomiędzy URL-ami i ścieżkami w systemie
plików. Pozwala to na udostępnianie treści nie umieszczonej
bezpośrednio wewnątrz DocumentRoota jako części drzewa dokumentów WWW.
Dyrektywa ScriptAlias ponadto oznacza katalog docelowy jako
zawierający wyłącznie skrypty CGI.

Dyrektywy Redirect służą do instruowania klientów o konieczności
wysłania nowego żądania z innym URL-em. Są one zwykle używane w
sytuacji, kiedy zasoby zostały przeniesione w nowe miejsce.

Potężniejszy i bardziej elastyczny zbiór dyrektyw do manipulowania
URL-ami znajduje się w module mod_rewrite.

%package mod_asis
Summary:	Sending files which contain their own HTTP headers
Summary(pl.UTF-8):	Wysyłanie plików zawierających własne nagłówki HTTP
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_asis) = %{version}-%{release}

%description mod_asis
This module provides the handler send-as-is which causes Apache to
send the document without adding most of the usual HTTP headers.

This can be used to send any kind of data from the server, including
redirects and other special HTTP responses, without requiring a
cgi-script or an nph script.

For historical reasons, this module will also process any file with
the MIME type httpd/send-as-is.

%description mod_asis -l pl.UTF-8
Ten moduł dostarcza funkcję obsługi send-as-is powodującą, że Apache
wysyła dokument bez dodawania większości zwykle stosowanych nagłówków
HTTP.

Może on służyć do wysyłania z serwera dowolnego rodzaju danych,
włącznie z przekierowaniami i innymi specjalnymi odpowiedziami HTTP
bez użycia skryptu CGI czy nph.

Ze względów historycznych ten moduł przetwarza także wszelkie pliki o
typie MIME httpd/send-as-is.

%package mod_auth
Summary:	Apache module with user authentication using textual files
Summary(pl.UTF-8):	Moduł uwierzytelniania użytkownika przy użyciu plików tekstowych dla Apache
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_auth) = %{version}-%{release}
Provides:	webserver(auth)
Obsoletes:	apache-mod_auth < 2.0.0

%description mod_auth
This package contains mod_auth module. It provides for user
authentication using textual files.

%description mod_auth -l pl.UTF-8
Ten pakiet zawiera moduł mod_auth. Służy on do uwierzytelniania przy
użyciu plików tekstowych.

%package mod_auth_anon
Summary:	Apache module with "anonymous" user access authentication
Summary(pl.UTF-8):	Moduł apache oferujący anonimową autoryzację użytkownia
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_auth_anon) = %{version}-%{release}
Obsoletes:	apache-mod_auth_anon < 2.0.0

%description mod_auth_anon
This package contains mod_auth_anon module. It allows "anonymous" user
access to authenticated areas. It does access control in a manner
similar to anonymous FTP sites; i.e. have a 'magic' user id
'anonymous' and the email address as a password. These email addresses
can be logged. Combined with other (database) access control methods,
this allows for effective user tracking and customization according to
a user profile while still keeping the site open for 'unregistered'
users. One advantage of using Auth-based user tracking is that, unlike
magic-cookies and funny URL pre/postfixes, it is completely browser
independent and it allows users to share URLs.

%description mod_auth_anon -l pl.UTF-8
Ten moduł oferuje anonimową autoryzację użytkownia podobnie do
anonimowych serwerów FTP (użytkownik "anonymous" oraz hasło w postaci
adresu pocztowego użytkownika). Podawane adresy mogą być logowane. W
połączeniu z innymi (opartymi o bazy danych) metodami kontroli dostępu
umożliwia efektywne śledzenie użytkowników i dostosowywanie w
zależności od profilu użytkownika, jednocześnie zachowując stronę
otwartą dla "niezarejestrowanych" użytkowników. Jedną z zalet używania
śledzenia użytkowników opartego o uwierzytelnienie nad ciasteczkami i
śmiesznymi prze-/przyrostkami URL-i jest całkowita niezależność od
przeglądarki i umożliwienie użytkownikom współdzielenia URL-i.

%package mod_auth_db
Summary:	Apache module with user authentication which uses Berkeley DB files
Summary(pl.UTF-8):	Moduł Apache'a z mechanizmem uwierzytelniania używającym plików Berkeley DB
Group:		Networking/Daemons
Requires(triggerpostun):	sed >= 4.0
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_auth_db) = %{version}-%{release}
Obsoletes:	apache-mod_auth_db < 2.0.0

%description mod_auth_db
This package contains mod_auth_db module. It provides for user
authentication using Berkeley DB files.

%description mod_auth_db -l pl.UTF-8
Ten pakiet zawiera moduł mod_auth_db. Moduł ten służy do
uwierzytelniania, ale jako plików danych używa Berkeley DB.

%package mod_auth_digest
Summary:	Apache user authentication module using MD5 Digest Authentication
Summary(pl.UTF-8):	Moduł Apache'a do uwierzytelniania metodą MD5 Digest Authentication
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_auth_digest) = %{version}-%{release}
Obsoletes:	apache-mod_auth_digest < 2.0.0
Obsoletes:	apache1-mod_digest

%description mod_auth_digest
This package contains mod_digest module. It provides user
authentication using MD5 Digest Authentication.

%description mod_auth_digest -l pl.UTF-8
Moduł ten dostarcza metodę uwierzytelniania przy użyciu MD5 Digest
Authentication.

%package mod_autoindex
Summary:	Apache module - display index of files
Summary(pl.UTF-8):	Moduł apache do wyświetlania indeksu plików
Group:		Networking/Daemons
Requires(triggerpostun):	sed >= 4.0
Requires:	%{name}(EAPI) = %{version}-%{release}
Requires:	%{name}-mod_alias = %{version}-%{release}
Requires:	apache-icons
Provides:	apache(mod_autoindex) = %{version}-%{release}

%description mod_autoindex
This package contains mod_autoindex module. It provides generation
index of files.

%description mod_autoindex -l pl.UTF-8
Ten pakiet dostarcza moduł autoindex, który generuje indeks plików.

%package mod_cern_meta
Summary:	Support for HTTP header metafiles
Summary(pl.UTF-8):	Obsługa metaplików nagłówków HTTP
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_cern_meta) = %{version}-%{release}

%description mod_cern_meta
Emulate the CERN HTTPD Meta file semantics. Meta files are HTTP
headers that can be output in addition to the normal range of headers
for each file accessed. They appear rather like the Apache .asis
files, and are able to provide a crude way of influencing the Expires:
header, as well as providing other curiosities. There are many ways to
manage meta information, this one was chosen because there is already
a large number of CERN users who can exploit this module.

%description mod_cern_meta -l pl.UTF-8
Moduł emulujący semantykę metaplików CERN HTTPD. Metapliki to nagłówki
HTTP, które mogą być wysyłane oprócz normalnego zestawu nagłówków dla
każdego przetwarzanego pliku. Zachowują się bardziej jak pliki .asis
Apache'a i mogą dawać brutalny sposób wpływania na nagłówek Expires:,
a także dostarczać inne ciekawostki. Jest wiele sposobów zarządzania
metainformacjami, ta została wybrana ponieważ istnieje już wielu
użytkowników CERN wykorzystujących ten moduł.

%package mod_cgi
Summary:	Invoking CGI scripts
Summary(pl.UTF-8):	Wywoływanie skryptów CGI
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_cgi) = %{version}-%{release}
Provides:	webserver(cgi)

%description mod_cgi
Any file that has the MIME type application/x-httpd-cgi or handler
cgi-script (Apache 1.1 or later) will be treated as a CGI script, and
run by the server, with its output being returned to the client. Files
acquire this type either by having a name containing an extension
defined by the AddType directive, or by being in a ScriptAlias
directory. Files that are not in a ScriptAlias directory, but which
are of type application/x-httpd-cgi by virtue of an AddType directive,
will still not be executed by the server unless Options ExecCGI is
enabled. See the Options directive for more details.

%description mod_cgi -l pl.UTF-8
Ten moduł powoduje, że dowolny plik o typie MIME
application/x-httpd-cgi albo procedurze obsługi cgi-script (w Apache'u
1.1 lub nowszym) będzie traktowany jako skrypt CGI i uruchamiany przez
serwer, a jego wyjście będzie zwracane klientowi. Pliki uzyskują ten
typ przez posiadanie nazwy zawierającej rozszerzenie określone
dyrektywą AddType lub będąc w katalogu ScriptAlias. Pliki nie będące w
katalogu ScriptAlias, ale mające typ application/x-httpd-cgi dzięki
dyrektywie AddType nie będą jednak wykonywane, chyba że włączona
zostanie opcja ExecCGI - więcej szczegółów w dyrektywie Options.

%package mod_define
Summary:	Apache module - definition variables for arbitrary directives
Summary(pl.UTF-8):	Moduł Apache'a do definiowania zmiennych
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_define) = %{version}-%{release}
Obsoletes:	apache-mod_define < 2.0.0

%description mod_define
It provides the definition variables for arbitrary directives, i.e.
variables which can be expanded on any(!) directive line.

%description mod_define -l pl.UTF-8
Moduł ten umożliwia definicję zmiennych dla dowolnych dyrektyw, tzn.
zmiennych, które mogą być rozwijane w dowolnej linii dyrektywy.

%package mod_digest
Summary:	Older version of apache user authentication module using MD5 Digest Authentication
Summary(pl.UTF-8):	Starsza wersja modułu apache do autoryzacji MD5
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_digest) = %{version}-%{release}
Obsoletes:	apache-mod_digest < 2.0.0

%description mod_digest
This package contains mod_digest module. It provides user
authentication using MD5 Digest Authentication. It implements an older
version of the MD5 Digest Authentication specification which will
probably not work with modern browsers. Please take a look at
mod_auth_digest which implements the most recent version of the
standard.

%description mod_digest -l pl.UTF-8
Moduł ten dostarcza metodę autoryzacji bazującą na MD5 Digest
Authentication. Implementuje on jedynie starszą wersję specyfikacji
uwierzytelniania MD5, i może nie działać z nowoczesnymi
przeglądarkami. Lepiej użyć modułu mod_auth_digest implementującego
najnowszą wersję standardu.

%package mod_dir
Summary:	Apache module for "trailing slash" redirects and serving directory index files
Summary(pl.UTF-8):	Moduł oferujący przekierowania i serwowanie indeksu katalogu
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_dir) = %{version}-%{release}
Provides:	webserver(indexfile)
Obsoletes:	apache-mod_dir < 2.0.0

%description mod_dir
This package contains mod_dir which provides "trailing slash"
redirects and serving directory index files.

%description mod_dir -l pl.UTF-8
Moduł oferujący przekierowania o "końcowy slash" oraz przekierowania i
udostępnianie indeksu katalogu.

%package mod_env
Summary:	Passing of environments to CGI scripts
Summary(pl.UTF-8):	Przekazywanie środowiska do skryptów CGI
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_env) = %{version}-%{release}

%description mod_env
This module allows for control of the environment that will be
provided to CGI scripts and SSI pages. Environment variables may be
passed from the shell which invoked the httpd process. Alternatively,
environment variables may be set or unset within the configuration
process.

%description mod_env -l pl.UTF-8
Ten moduł pozwala na kontrolę środowiska udostępnianego skryptom CGI i
stronom SSI. Zmienne środowiskowe mogą być przekazywane z powłoki w
czasie uruchamiania procesu httpd, albo - alternatywnie - ustawiane i
usuwane w procesie konfiguracji.

%package mod_expires
Summary:	Apache module which generates Expires HTTP headers
Summary(pl.UTF-8):	Moduł generujący nagłówki HTTP Expires
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_expires) = %{version}-%{release}
Obsoletes:	apache-mod_expires < 2.0.0

%description mod_expires
This module controls the setting of the Expires HTTP header in server
responses. The expiration date can set to be relative to either the
time the source file was last modified, or to the time of the client
access.

%description mod_expires -l pl.UTF-8
Moduł kontroluje ustawianie nagłówka HTTP Expires. Data wygaśnięcia
ważności może być ustalana w zależności od czasu modyfikacji plików
źródłowych lub odwołania klienta.

%package mod_headers
Summary:	Apache module allows for the customization of HTTP response headers
Summary(pl.UTF-8):	Moduł pozwalający na modyfikację nagłówków HTTP
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_headers) = %{version}-%{release}
Obsoletes:	apache-mod_headers < 2.0.0

%description mod_headers
This package contains mod_headers module. The module allows for the
customization of HTTP response headers. Headers can be merged,
replaced or removed.

%description mod_headers -l pl.UTF-8
Moduł pozwalający na łączenie, usuwania, zamianę nagłówków HTTP
wysyłanych do przeglądarki. Nagłówki mogą być łączone, zastępowane lub
usuwane.

%package mod_imap
Summary:	Apache module with imap-file handler
Summary(pl.UTF-8):	Moduł Apache'a z obsługą imap-file
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_imap) = %{version}-%{release}
Obsoletes:	apache-mod_imap < 2.0.0

%description mod_imap
This package contains mod_imap module. It provides for .map files,
replacing the functionality of the imagemap CGI program. Any directory
or document type configured to use the handler imap-file.

%description mod_imap -l pl.UTF-8
Moduł umożliwiający obsługę plików .map, zastępujący funkcjonalność
programu CGI imagemap.

%package mod_include
Summary:	Server-parsed documents
Summary(pl.UTF-8):	Dokumenty przetwarzane po stronie serwera
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_include) = %{version}-%{release}

%description mod_include
This module provides a handler which will process files before they
are sent to the client. The processing is controlled by specially
formated SGML comments, referred to as elements. These elements allow
conditional text, the inclusion other files or programs, as well as
the setting and printing of environment variables.

%description mod_include -l pl.UTF-8
Ten moduł dostarcza procedurę obsługi przetwarzającą pliki przed
wysłaniem ich do klienta. Przetwarzanie jest sterowane specjalnie
sformatowanymi komentarzami SGML, nazywanymi elementami. Elementy te
pozwalają na tekst warunkowy, dołączanie innych plików lub programów,
a także ustawianie i wypisywanie zmiennych środowiskowych.

%package mod_info
Summary:	Apache module with comprehensive overview of the server configuration
Summary(pl.UTF-8):	Moduł dostarczający informacji na temat serwera
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_info) = %{version}-%{release}
Obsoletes:	apache-mod_info < 2.0.0

%description mod_info
This package contains mod_info module. It provides a comprehensive
overview of the server configuration including all installed modules
and directives in the configuration files.

%description mod_info -l pl.UTF-8
Moduł dostarczający wyczerpujących informacji o konfiguracji serwera,
w tym zainstalowanych modułach oraz dyrektywach w plikach
konfiguracyjnych.

%package mod_log_agent
Summary:	Logging of User Agents
Summary(pl.UTF-8):	Logowanie nazw klientów (User Agent)
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_log_agent) = %{version}-%{release}

%description mod_log_agent
This module is provided strictly for compatibility with NCSA httpd,
and is deprecated. We recommend you use mod_log_config instead.

%description mod_log_agent -l pl.UTF-8
Ten moduł jest dostarczony wyłącznie dla kompatybilności z NCSA httpd
i jest niezalecany. Zamiast niego lepiej używać mod_log_config.

%package mod_log_config
Summary:	User-configurable logging replacement for mod_log_common
Summary(pl.UTF-8):	Konfigurowalny logujący zamiennik dla mod_log_common
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_log_config) = %{version}-%{release}

%description mod_log_config
This module provides for flexible logging of client requests. Logs are
written in a customizable format, and may be written directly to a
file, or to an external program. Conditional logging is provided so
that individual requests may be included or excluded from the logs
based on characteristics of the request.

Three directives are provided by this module: TransferLog to create a
log file, LogFormat to set a custom format, and CustomLog to define a
log file and format in one step. The TransferLog and CustomLog
directives can be used multiple times in each server to cause each
request to be logged to multiple files.

%description mod_log_config -l pl.UTF-8
Ten moduł umożliwia elastyczne logowanie żądań klientów. Logi są
zapisywane w konfigurowalnym formacie i mogą być zapisywane
bezpośrednio do pliku lub przekazywane do zewnętrznego programu.
Dostępne jest logowanie warunkowe polegające na włączeniu lub
wyłączeniu poszczególnych żądań z logowania na podstawie
charakterystyki żądania.

Ten moduł udostępnia trzy dyrektywy: TransferLog tworzący plik logu,
LogFormat ustawiający własny format logowania i CustomLog określający
plik logu i format jednocześnie. Dyrektywy TransferLog i CustomLog
mogą być używane wielokrotnie w każdym serwerze powodując logowanie
każdego żądania do wielu plików.

%package mod_log_forensic
Summary:	Apache module for forensic logging of the requests
Summary(pl.UTF-8):	Moduł Apache'a do logowania żądań w celu późniejszej analizy
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_log_forensic) = %{version}-%{release}
Obsoletes:	apache-mod_log_forensic < 2.0.0

%description mod_log_forensic
This module provides for forensic logging of client requests. Logging
is done before and after processing a request.

%description mod_log_forensic -l pl.UTF-8
Ten moduł pozwala na logowanie żądań w celu późniejszej analizy.
Logowanie jest wykonywane przed i po przetworzeniu żądania.

%package mod_log_referer
Summary:	User-configurable logging replacement for mod_log_common
Summary(pl.UTF-8):	Konfigurowalny logujący zamiennik dla mod_log_common
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_log_referer) = %{version}-%{release}

%description mod_log_referer
This module is provided strictly for compatibility with NCSA httpd,
and is deprecated. We recommend you use mod_log_config instead.

%description mod_log_referer -l pl.UTF-8
Ten moduł jest dostarczony wyłącznie dla kompatybilności z NCSA httpd
i jest niezalecany. Zamiast niego lepiej używać mod_log_config.

%package mod_mime
Summary:	Determining document types using file extensions
Summary(pl.UTF-8):	Określanie typów dokumentów przy użyciu rozszerzeń plików
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_mime) = %{version}-%{release}

%description mod_mime
This module is used to determine various bits of "meta information"
about documents. This information relates to the content of the
document and is returned to the browser or used in content-negotiation
within the server. In addition, a "handler" can be set for a document,
which determines how the document will be processed within the server.

%description mod_mime -l pl.UTF-8
Ten moduł służy do określania różnych fragmentów metainformacji
dotyczących dokumentów. Informacja ta odnoszi się do zawartości
dokumentu i jest zwracana przeglądarce albo używana przy negocjacji
treści wewnątrz serwera. Ponadto dla dokumentu można ustawić procedurę
obsługi, określającą w jaki sposób dokument będzie przetwarzany
wewnątrz serwera.

%package mod_mime_magic
Summary:	Determining document types using "magic numbers"
Summary(pl.UTF-8):	Określanie typów dokumentów przy użyciu "liczb magicznych"
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_mime_magic) = %{version}-%{release}

%description mod_mime_magic
This module determines the MIME type of files in the same way the Unix
file(1) command works: it looks at the first few bytes of the file. It
is intended as a "second line of defense" for cases that mod_mime
can't resolve. To assure that mod_mime gets first try at determining a
file's MIME type, be sure to list mod_mime_magic before mod_mime in
the configuration.

This module is derived from a free version of the file(1) command for
Unix, which uses "magic numbers" and other hints from a file's
contents to figure out what the contents are. This module is active
only if the magic file is specified by the MimeMagicFile directive.

%description mod_mime_magic -l pl.UTF-8
Ten moduł określa typ MIME plików w ten sam sposób, co polecenie
file(1): sprawdza pierwsze kilka bajtów pliku. Ma być "drugą linią
obrony" dla przypadków, których nie może rozwiązać mod_mime. Aby mieć
pewność, że mod_mime dostaje pierwszą próbę określenia typu MIME,
należy upewnić się, że mod_mime_magic jest umieszczony w konfiguracji
przed mod_mime.

Ten moduł wywodzi się z wolnodostępnej wersji polecenia file(1) dla
uniksów, używającej "liczb magicznych" i innych podpowiedzi z
zawartości plików w celu rozpoznania zawartości. Moduł jest aktywny
tylko jeśli plik magic został określony dyrektywą MimeMagicFile.

%package mod_mmap_static
Summary:	Apache module for mmap()ing statically configured list files
Summary(pl.UTF-8):	Moduł służący do mmap()owania plików
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_mmap_static) = %{version}-%{release}
Obsoletes:	apache-mod_mmap_static < 2.0.0

%description mod_mmap_static
This package contains mod_mmap_static module. It provides mmap()ing of
a statically configured list of frequently requested but not changed
files.

%description mod_mmap_static -l pl.UTF-8
Moduł umożliwia mmap()owanie statycznie skonfigurowanych plików
(często używanych, ale nie ulegających zmianom).

%package mod_negotiation
Summary:	Content negotiation
Summary(pl.UTF-8):	Negocjacja treści
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_negotiation) = %{version}-%{release}

%description mod_negotiation
Content negotiation, or more accurately content selection, is the
selection of the document that best matches the clients capabilities,
from one of several available documents. There are two implementations
of this.
- A type map (a file with the handler type-map) which explicitly lists
  the files containing the variants.
- A MultiViews search (enabled by the MultiViews Option, where the
  server does an implicit filename pattern match, and choose from
  amongst the results.

%description mod_negotiation -l pl.UTF-8
Negocjacja treści, albo bardziej precyzyjnie wybór treści, to wybór
dokumentu najbardziej pasującego do możliwości klienta spośród różnych
dostępnych dokumentów. Są dwie różne implementacje.
- Odwzorowanie typów (plik z obsługą type-map) wypisujący explicite
  pliki zawierające warianty.
- Wyszukiwanie MultiViews (włączane opcją MultiViews, kiedy serwer
  dopasowuje implicite wzorzec nazwy pliku i wybiera spośród wyników).

%package mod_proxy
Summary:	Apache module with Web proxy
Summary(pl.UTF-8):	Moduł dodający obsługę serwera proxy
Group:		Networking/Daemons
Requires(triggerpostun):	sed >= 4.0
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_proxy) = %{version}-%{release}
Obsoletes:	apache-mod_proxy < 2.0.0

%description mod_proxy
This package contains module with implementation a proxy/cache for
Apache. It implements proxying capability for FTP, CONNECT (for SSL),
HTTP/0.9, and HTTP/1.0. The module can be configured to connect to
other proxy modules for these and other protocols. Contains patch
from: <http://allafrica.com/tools/apache/mod_proxy/>

%description mod_proxy -l pl.UTF-8
Moduł zawiera implementację serwera proxy/cache dla Apache.
Iplementacja zawiera obsługę FTP, CONNECT (dla SSL), HTTP/0.9 i
HTTP/1.0. Ten moduł może być skonfigurowany tak, aby łączył się z
innymi modułami proxy dla tych i innych protokołów. Zawiera łatę z
<http://allafrica.com/tools/apache/mod_proxy/>.

%package mod_rewrite
Summary:	Apache module with rule-based engine for rewrite requested URLs on the fly
Summary(pl.UTF-8):	Moduł do ,,przepisywania'' adresów URL w locie
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_rewrite) = %{version}-%{release}
Obsoletes:	apache-mod_rewrite < 2.0.0

%description mod_rewrite
This package contains It provides a rule-based rewriting engine to
rewrite requested URLs on the fly.

%description mod_rewrite -l pl.UTF-8
Moduł oferujący możliwość ,,przepisywania'' adresów URL w locie.

%package mod_setenvif
Summary:	Set environment variables based on client information
Summary(pl.UTF-8):	Ustawianie zmiennych środowiskowych w oparciu o informacje o kliencie
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_setenvif) = %{version}-%{release}

%description mod_setenvif
The mod_setenvif module allows you to set environment variables
according to whether different aspects of the request match regular
expressions you specify. These environment variables can be used by
other parts of the server to make decisions about actions to be taken.

%description mod_setenvif -l pl.UTF-8
Moduł mod_setenvif pozwala na ustawianie zmiennych środowiskowych w
zależności od różnych aspektów żądania pasujących do podanych wyrażeń
regularnych. Te zmienne środowiskowe mogą być używane przez inne
części serwera do podejmowania decyzji o podejmowanych akcjach.

%package mod_speling
Summary:	Automatically correct minor typos in URLs
Summary(pl.UTF-8):	Automatyczne poprawianie pomniejszych literówek w URL-ach
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_speling) = %{version}-%{release}

%description mod_speling
Requests to documents sometimes cannot be served by the core Apache
server because the request was misspelled or miscapitalized. This
module addresses this problem by trying to find a matching document,
even after all other modules gave up. It does its work by comparing
each document name in the requested directory against the requested
document name without regard to case, and allowing up to one
misspelling (character insertion / omission / transposition or wrong
character). A list is built with all document names which were matched
using this strategy.

%description mod_speling -l pl.UTF-8
Czasami żądania dokumentów nie mogą być wykonane przez sam serwer
Apache, ponieważ żądanie zostało napisane z błędem w znakach lub
wielkości liter. Ten moduł próbuje rozwiązać ten problem próbując
znaleźć pasujący dokument, nawet jeśli inne moduły się poddały. Działa
on poprzez porównywanie nazwy każdego dokumentu w żądanym katalogu z
żądaną nazwą dokumentu bez zwracania uwagi na wielkość liter i
pozwalając na jeden błąd (dodany, pominięty, przestawiony lub zły
znak). Tworzona jest lista dla wszystkich nazw dokumentów pasujących
dla tej strategii.

%package mod_status
Summary:	Server status report module for apache
Summary(pl.UTF-8):	Moduł dostarczający informacje statystyczne o serwerze
Group:		Networking/Daemons
Requires(triggerpostun):	sed >= 4.0
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_status) = %{version}-%{release}
Obsoletes:	apache-mod_status < 2.0.0

%description mod_status
The Status module allows a server administrator to find out how well
their server is performing. A HTML page is presented that gives the
current server statistics in an easily readable form. If required this
page can be made to automatically refresh (given a compatible
browser).

%description mod_status -l pl.UTF-8
Moduł pozwala administratorowi na przeglądanie statystyk dotyczących
pracy serwera apache (w postaci strony HTML). Strona ta może się
automatycznie odświeżać (o ile jest to obsługiwane przez
przeglądarkę).

%package mod_unique_id
Summary:	Apache module which provides a magic token for each request
Summary(pl.UTF-8):	Moduł nadający każdemu żądaniu unikalny token
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_unique_id) = %{version}-%{release}
Obsoletes:	apache-mod_unique_id < 2.0.0

%description mod_unique_id
This package contains the mod_unique_id. This module provides a magic
token for each request which is guaranteed to be unique across "all"
requests under very specific conditions. The unique identifier is even
unique across multiple machines in a properly configured cluster of
machines. The environment variable UNIQUE_ID is set to the identifier
for each request. Unique identifiers are useful for various reasons
which are beyond the scope of this document.

%description mod_unique_id -l pl.UTF-8
Moduł nadaje przy każdym żądaniu token unikalny w ramach wszystkich
żądań, nawet w ramach poprawnie skonfigurowanego klastra z wielu
maszyn. Moduł ustawia przy każdym żądaniu zmienną środowiskową
UNIQUE_ID.

%package mod_userdir
Summary:	User home directories
Summary(pl.UTF-8):	Katalogi domowe użytkowników
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_userdir) = %{version}-%{release}

%description mod_userdir
This module provides for user-specific directories.

%description mod_userdir -l pl.UTF-8
Ten moduł dostarcza obsługę katalogów specyficznych dla uzytkownika.

%package mod_usertrack
Summary:	Apache module for user tracking using cookies
Summary(pl.UTF-8):	Moduł służący do śledzenia użytkowników przy użyciu ciasteczek
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_usertrack) = %{version}-%{release}
Obsoletes:	apache-mod_usertrack < 2.0.0

%description mod_usertrack
This package contains the user tracking module which did its own
logging using CookieLog directory. This module allow multiple log
files.

%description mod_usertrack -l pl.UTF-8
Moduł pozwalający na śledzenie użytkowników przy pomocy ciasteczek.
Moduł ma własne logowanie przy użyciu katalogu CookieLog; pozwala na
wiele plików logów.

%package mod_vhost_alias
Summary:	Apache module for dynamically configured mass virtual hosting
Summary(pl.UTF-8):	Moduł dodający obsługę hostów wirtualnych
Group:		Networking/Daemons
Requires(triggerpostun):	sed >= 4.0
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_vhost_alias) = %{version}-%{release}
Obsoletes:	apache-mod_vhost_alias < 2.0.0

%description mod_vhost_alias
This package contains the mod_vhost_alias. It provides support for
dynamically configured mass virtual hosting.

%description mod_vhost_alias -l pl.UTF-8
Moduł umożliwia na dynamiczne konfigurowanie masowej ilości serwerów
wirtualnych.

%package -n htpasswd-%{name}
Summary:	Apache 1.x htpasswd utility
Summary(pl.UTF-8):	Narzędzie htpasswd z Apache'a 1.x
Group:		Networking/Utilities
Provides:	htpasswd
Obsoletes:	htpasswd

%description -n htpasswd-%{name}
htpasswd is used to create and update the flat-files used to store
usernames and password for basic authentication of HTTP users. This
package contains htpasswd from Apache 1.x; this version supports
plaintext passwords and CRYPT (default), MD5 and SHA1 encryptions.

%description -n htpasswd-%{name} -l pl.UTF-8
htpasswd służy do tworzenia i uaktualniania płaskich plików służących
do przechowywania nazw użytkowników i haseł do uwierzytelnienia basic
użytkowników HTTP. Ten pakiet zawiera htpasswd z Apache'a 1.x; ta
wersja obsługuje hasła zapisane czystym tekstem oraz zakodowane
algorytmami CRYPT (domyślnym), MD5 i SHA1.

%package cgi_test
Summary:	cgi test/demo programs
Summary(pl.UTF-8):	Programy testowe/przykładowe cgi
Group:		Networking/Utilities
Requires:	%{name}-base = %{version}-%{release}
Requires:	filesystem >= 2.0-1

%description cgi_test
Two cgi test/demo programs: test-cgi and print-env.

%description cgi_test -l pl.UTF-8
Dwa programy testowe/przykładowe cgi: test-cgi and print-env.

%prep
%setup -q -n apache_%{version} %{?with_lingerd:-a25}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p0
%patch6 -p1
%patch7 -p1
%patch8 -p1
%{?with_ipv6:%patch9 -p1}
%patch10 -p1
%patch11 -p1
%patch12 -p1
%{?with_rewrite_ldap:%patch13 -p1}
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%{!?with_ipv6:%patch19 -p1}
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1

%patch26 -p2
%patch27 -p2
%patch28 -p2
%patch29 -p2
%patch30 -p2
%patch31 -p2
%patch32 -p2
%patch33 -p2
%patch34 -p2
%patch35 -p2
%patch36 -p2
%patch37 -p2
%patch38 -p2
%patch39 -p2
%patch40 -p2
%patch41 -p2

%if %{with lingerd}
mkdir -p lingerd
cp -a lingerd-*/{README,TUNING,LICENSE,TODO,ChangeLog} lingerd
cp -a lingerd-*/{apache-1.3/ap_lingerd.c,li_config.h} src/main
%patch42 -p1
%endif

# make manual link with full path
%{__sed} -i -e 's,href="manual/,href="/manual/,i' htdocs/index.html.*

# fix libdir (at least in PLD layout; no need to care about other ones)
%{__sed} -i -e 's,/lib$,/%{_lib},' config.layout

%build
OPTIM="%{rpmcflags} -DHARD_SERVER_LIMIT=2048" \
./configure \
	--with-layout=PLD \
	--without-confadjust \
	--enable-module=all \
	--enable-module=auth_digest \
	--enable-shared=max \
	--with-perl=%{__perl} \
	--enable-suexec \
	--suexec-caller=http \
	--suexec-uidmin=500 \
	--suexec-gidmin=500 \
	--suexec-docroot=%{httpdir} \
	--disable-rule=WANTHSREGEX \
	--enable-rule=EAPI \
	--target=apache \
	%{?with_ipv6:--enable-rule=INET6}

%{__make} \
	CC="%{__cc}"
	LIBS1="-lm -lcrypt -lmm -ldl"

rm -f src/modules/standard/mod_auth_db.so
%{__make} -C src/modules/standard mod_auth_db.so \
	CC="%{__cc}"
	LIBS_SHLIB="-ldb"

rm -f src/modules/standard/mod_rewrite.so
%{__make} -C src/modules/standard mod_rewrite.so \
	CC="%{__cc}"
	LIBS_SHLIB="-ldb %{?with_rewrite_ldap:-lldap -llber}"

%if %{with lingerd}
%{__make} -C lingerd-* lingerd \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"
	LDFLAGS="%{rpmldflags}"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{logrotate.d,rc.d/init.d,sysconfig} \
	$RPM_BUILD_ROOT%{_sysconfdir}/{webapps.d,conf.d} \
	$RPM_BUILD_ROOT%{httpdir}/html \
	$RPM_BUILD_ROOT%{_libexecdir} \
	$RPM_BUILD_ROOT/var/{log/{apache,archive/apache},run/apache}

%{__make} -j1 install-quiet \
	root=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/apache1
sed -e 's,/usr/lib,%{_libdir},g' %{SOURCE1} > $RPM_BUILD_ROOT/etc/rc.d/init.d/apache
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/apache
bzip2 -dc %{SOURCE5} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
mv $RPM_BUILD_ROOT%{_mandir}/hu/man8/{httpd,apache}.8
mv $RPM_BUILD_ROOT%{_mandir}/pl/man8/{httpd,apache}.8

touch $RPM_BUILD_ROOT/var/log/apache/{access,error,agent,referer}_log

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/errordocs
cp -a errordocs/* $RPM_BUILD_ROOT%{_datadir}/%{name}/errordocs

mv $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf conf/apache.conf.dist
cp -a %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf

CFG="$RPM_BUILD_ROOT%{_sysconfdir}/conf.d"

echo "LoadModule access_module      modules/mod_access.so" > $CFG/01_mod_access.conf
echo "LoadModule alias_module       modules/mod_alias.so" > $CFG/02_mod_alias.conf
echo "LoadModule asis_module        modules/mod_asis.so" > $CFG/03_mod_asis.conf
cp -a %{SOURCE21} $CFG/04_mod_cern_meta.conf
echo "LoadModule cgi_module         modules/mod_cgi.so" > $CFG/05_mod_cgi.conf
echo "LoadModule env_module         modules/mod_env.so" > $CFG/06_mod_env.conf
echo "LoadModule include_module     modules/mod_include.so" > $CFG/07_mod_include.conf
echo "LoadModule log_agent_module   modules/mod_log_agent.so" > $CFG/08_mod_log_agent.conf
cp -a %{SOURCE14} $CFG/09_mod_log_config.conf
echo "LoadModule log_referer_module modules/mod_log_referer.so" > $CFG/10_mod_log_referer.conf
cp -a %{SOURCE16}	$CFG/11_mod_mime_magic.conf
cp -a %{SOURCE19}	$CFG/12_mod_mime.conf
cp -a %{SOURCE18} $CFG/13_mod_negotiation.conf
cp -a %{SOURCE22}	$CFG/14_mod_setenvif.conf
echo "LoadModule speling_module     modules/mod_speling.so" > $CFG/15_mod_speling.conf
cp -a %{SOURCE15}	$CFG/16_mod_userdir.conf

cp -a %{SOURCE8}	$CFG/20_common.conf
cp -a %{SOURCE6}	$CFG/30_defaultindex.conf
cp -a %{SOURCE26}	$CFG/30_manual.conf

cp -a %{SOURCE23}	$CFG/20_mod_vhost_alias.conf
cp -a %{SOURCE9}	$CFG/25_mod_status.conf
cp -a %{SOURCE10}	$CFG/30_mod_proxy.conf
cp -a %{SOURCE20}	$CFG/50_mod_actions.conf
echo "LoadModule auth_module	modules/mod_auth.so" > $CFG/51_mod_auth.conf
echo "LoadModule auth_anon_module	modules/mod_auth_anon.so" > $CFG/52_mod_auth_anon.conf
echo "LoadModule auth_db_module	modules/mod_auth_db.so" > $CFG/53_mod_auth_db.conf
echo "LoadModule auth_digest_module	modules/mod_auth_digest.so" > $CFG/54_mod_auth_digest.conf
cp -a %{SOURCE11}	$CFG/57_mod_autoindex.conf
cp -a %{SOURCE12}	$CFG/59_mod_dir.conf
echo "LoadModule expires_module	modules/mod_expires.so" > $CFG/67_mod_expires.conf
echo "LoadModule headers_module	modules/mod_headers.so" > $CFG/68_mod_headers.conf
echo "LoadModule imap_module	modules/mod_imap.so" > $CFG/69_mod_imap.conf
echo "LoadModule rewrite_module	modules/mod_rewrite.so" > $CFG/70_mod_rewrite.conf
echo "LoadModule usertrack_module	modules/mod_usertrack.so" > $CFG/71_mod_usertrack.conf
echo "LoadModule unique_id_module	modules/mod_unique_id.so" > $CFG/72_mod_unique_id.conf
echo "LoadModule define_module	modules/mod_define.so" > $CFG/73_mod_define.conf
echo "LoadModule digest_module	modules/mod_digest.so" > $CFG/74_mod_digest.conf
echo "LoadModule log_forensic_module	modules/mod_log_forensic.so" > $CFG/75_mod_log_forensic.conf
echo "LoadModule mmap_static_module	modules/mod_mmap_static.so" > $CFG/76_mod_mmap_static.conf
cp -a %{SOURCE13} $CFG/77_mod_info.conf
cp -a %{SOURCE24}	$CFG/80_errordocs.conf
cp -a %{SOURCE17}	$CFG/80_mod_alias.conf
# cgi_test: create config file with ScriptAlias
cat << 'EOF' > $CFG/09_cgi_test.conf
ScriptAlias /cgi-bin/printenv %{cgibindir}/printenv
ScriptAlias /cgi-bin/test-cgi %{cgibindir}/test-cgi
EOF

ln -sf index.html.en $RPM_BUILD_ROOT%{docroot}/index.html

mv $RPM_BUILD_ROOT%{_sbindir}/apxs $RPM_BUILD_ROOT%{apxs}
mv $RPM_BUILD_ROOT%{_mandir}/man8/apxs.8 $RPM_BUILD_ROOT%{_mandir}/man8/apxs1.8

perl -p -i -e 's/^if ...O ne "MSWin32"./if (0)/' $RPM_BUILD_ROOT%{apxs}

ln -s ../..%{_libexecdir} $RPM_BUILD_ROOT%{_sysconfdir}/modules
ln -s ../../var/log/apache $RPM_BUILD_ROOT%{_sysconfdir}/logs

ln -sf %{_bindir}/htpasswd $RPM_BUILD_ROOT%{_sbindir}

# Not packaged.
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/*.default
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/{access,srm}.conf
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/mime.types
rm -f $RPM_BUILD_ROOT%{_libexecdir}/*.exp
rm -f $RPM_BUILD_ROOT%{_libexecdir}/mod_{auth_dbm,example}.so
rm -f $RPM_BUILD_ROOT%{_mandir}/README*

rm -rf $RPM_BUILD_ROOT%{_datadir}/apache-icons
install -d $RPM_BUILD_ROOT%{_datadir}/apache-icons
%{__tar} -zxf %{SOURCE3} --strip-components=1 -C $RPM_BUILD_ROOT%{_datadir}/apache-icons

# Not for our os or for older apache
rm $RPM_BUILD_ROOT%{manualdir}/{cygwin,ebcdic,install-{z,}tpf,man-template}.html
rm $RPM_BUILD_ROOT%{manualdir}/mod/mod_{auth_dbm,browser,dld,example,isapi,log_common}.html
rm $RPM_BUILD_ROOT%{manualdir}/{mpeix,netware,new_features_1_[0-2],readme-tpf,suexec_1_2,unixware,vhosts/details_1_2}.html
rm $RPM_BUILD_ROOT%{manualdir}/{win_{compiling,service}.html*,windows.html*}

%if %{with lingerd}
install lingerd-*/lingerd $RPM_BUILD_ROOT%{_libexecdir}
install -d $RPM_BUILD_ROOT%{_localstatedir}/run/lingerd
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%pre base
%groupadd -g 51 -r -f http
%useradd -u 51 -r -d %{httpdir} -s /bin/false -c "HTTP User" -g http http
if [ "$(getent passwd http | cut -d: -f6)" = "/home/httpd" ]; then
	/usr/sbin/usermod -d %{httpdir} http
fi

%post base
/sbin/chkconfig --add apache
umask 137
touch /var/log/apache/{access,error,agent,referer}_log

%preun base
if [ "$1" = "0" ]; then
	%service apache stop
	/sbin/chkconfig --del apache
fi

%postun base
if [ "$1" = "0" ]; then
	%userremove http
	%groupremove http
fi

%triggerpostun base -- apache < 2.0.0
%groupadd -g 51 -r -f http
%useradd -u 51 -r -d %{httpdir} -s /bin/false -c "HTTP User" -g http http
/sbin/chkconfig --add apache

%triggerpostun base -- apache1 < 1.3.33-1.85
# upgrading from older version
if [ "$1" = "2" ]; then
	sed -i -e '
		# get apxs over confusion of changed ServerRoot
		s,^\(LoadModule .*\) lib/apache1/,\1 modules/,

		# update ServerRoot
		s,^ServerRoot.*,ServerRoot "/etc/apache",
	' /etc/apache/apache.conf
fi

%triggerpostun base -- %{name} <= 1.3.31-5
%banner %{name} -e -a <<EOF
WARNING!!!
 Since 1.3.31-5 version autoindex module has been separated to package %{name}-mod_autoindex
 If you need previous functionality please run:
poldek -Uv %{name}-mod_autoindex

EOF

%triggerpostun base -- %{name} < 1.3.33-3.4
%banner %{name} -e -a <<EOF
WARNING!!!
 Since 1.3.33-3.4 version following modules have been separated to subpackages
 If you need previous functionality please run:
 poldek -Uv %{name}-MODULENAME
 where MODULENAME is one (or all) of:
	mod_asis
	mod_cern_meta
	mod_cgi
	mod_env
	mod_include
	mod_log_agent
	mod_log_config
	mod_log_referer
	mod_mime
	mod_mime_magic
	mod_negotiation
	mod_setenvif
	mod_speling
	mod_userdir
EOF

%triggerpostun base -- %{name} < 1.3.33-6.7
# update /etc/sysconfig/apache1 -> apache rename
if [ -f /etc/sysconfig/apache1.rpmsave ]; then
	cp -f /etc/sysconfig/apache{,.rpmnew}
	mv -f /etc/sysconfig/apache{1.rpmsave,}
fi

%triggerpostun base -- %{name} < 1.3.34-5.9
if ! grep -q 'Include webapps.d/' /etc/apache/apache.conf; then
# make sure webapps.d is included
cp -f /etc/apache/apache.conf{,.rpmsave}
sed -i -e '
	/^Include conf.d/{
		a
		a# Include webapps config
		aInclude webapps.d/*.conf
	}
' /etc/apache/apache.conf
fi

%triggerpostun mod_auth_db -- apache-mod_auth_db <= 1.3.20-2
sed -i -e '/^\(Add\|Load\)Module.*mod_auth_dbm\.\(so\|c\)/d' /etc/apache/apache.conf

%triggerpostun mod_autoindex -- apache1-mod_autoindex < 1.3.33-1.85
sed -i -e '
	/^\(Add\|Load\)Module.*mod_autoindex\.\(so\|c\)/d
	s,^Include.*mod_autoindex.conf,Include %{_sysconfdir}/conf.d/*_mod_autoindex.conf,
' /etc/apache/apache.conf

%triggerpostun mod_proxy -- apache1-mod_proxy < 1.3.33-1.85
sed -i -e '
	/^LoadModule.*libproxy\.so/d
	/^AddModule.*mod_proxy\.c/d
	s,^Include.*mod_proxy.conf,Include %{_sysconfdir}/conf.d/*_mod_proxy.conf,
' /etc/apache/apache.conf

%triggerpostun mod_status -- apache1-mod_status < 1.3.33-1.85
sed -i -e '
	/^\(Add\|Load\)Module.*mod_status\.\(so\|c\)/d
	s,^Include.*mod_status.conf,Include %{_sysconfdir}/conf.d/*_mod_status.conf,
' /etc/apache/apache.conf

%triggerpostun mod_vhost_alias -- apache1-mod_vhost_alias < 1.3.33-1.85
sed -i -e '
	/^\(Add\|Load\)Module.*mod_vhost_alias\.\(so\|c\)/d
	s,^Include.*mod_vhost_alias.conf,Include %{_sysconfdir}/conf.d/*_mod_vhost_alias.conf,
' /etc/apache/apache.conf

%posttrans base
# minimizing apache restarts logics. we restart webserver:
#
# 1. at the end of transaction. (posttrans, feature from rpm 4.4.2)
# 2. first install of module (post: $1 = 1)
# 2. uninstall of module (postun: $1 == 0)
#
# the strict internal deps between apache modules and
# main package are very important for all this to work.

# restart webserver at the end of transaction
%service apache restart "Apache HTTP daemon"

# macro called at module post scriptlet
%define	module_post \
if [ "$1" = "1" ]; then \
	%service -q apache restart \
fi

# macro called at module postun scriptlet
%define	module_postun \
if [ "$1" = "0" ]; then \
	%service -q apache restart \
fi

%post errordocs
if [ "$1" = "1" ]; then
	%service -q apache reload
fi

%postun errordocs
if [ "$1" = "0" ]; then
	%service -q apache reload
fi

%post mod_access
%module_post

%postun mod_access
%module_postun

%post mod_actions
%module_post

%postun mod_actions
%module_postun

%post mod_alias
%module_post

%postun mod_alias
%module_postun

%post mod_asis
%module_post

%postun mod_asis
%module_postun

%post mod_auth
%module_post

%postun mod_auth
%module_postun

%post mod_auth_anon
%module_post

%postun mod_auth_anon
%module_postun

%post mod_auth_db
%module_post

%postun mod_auth_db
%module_postun

%post mod_auth_digest
%module_post

%postun mod_auth_digest
%module_postun

%post mod_autoindex
%module_post

%postun mod_autoindex
%module_postun

%post mod_cern_meta
%module_post

%postun mod_cern_meta
%module_postun

%post mod_cgi
%module_post

%postun mod_cgi
%module_postun

%post mod_define
%module_post

%postun mod_define
%module_postun

%post mod_digest
%module_post

%postun mod_digest
%module_postun

%post mod_dir
%module_post

%postun mod_dir
%module_postun

%post mod_env
%module_post

%postun mod_env
%module_postun

%post mod_expires
%module_post

%postun mod_expires
%module_postun

%post mod_headers
%module_post

%postun mod_headers
%module_postun

%post mod_imap
%module_post

%postun mod_imap
%module_postun

%post mod_include
%module_post

%postun mod_include
%module_postun

%post mod_info
%module_post

%postun mod_info
%module_postun

%post mod_log_agent
%module_post

%postun mod_log_agent
%module_postun

%post mod_log_config
%module_post

%postun mod_log_config
%module_postun

%post mod_log_forensic
%module_post

%postun mod_log_forensic
%module_postun

%post mod_log_referer
%module_post

%postun mod_log_referer
%module_postun

%post mod_mime
%module_post

%postun mod_mime
%module_postun

%post mod_mime_magic
%module_post

%postun mod_mime_magic
%module_postun

%post mod_mmap_static
%module_post

%postun mod_mmap_static
%module_postun

%post mod_negotiation
%module_post

%postun mod_negotiation
%module_postun

%post mod_proxy
%module_post

%postun mod_proxy
%module_postun

%post mod_rewrite
%module_post

%postun mod_rewrite
%module_postun

%post mod_setenvif
%module_post

%postun mod_setenvif
%module_postun

%post mod_speling
%module_post

%postun mod_speling
%module_postun

%post mod_status
%module_post

%postun mod_status
%module_postun

%post mod_unique_id
%module_post

%postun mod_unique_id
%module_postun

%post mod_userdir
%module_post

%postun mod_userdir
%module_postun

%post mod_usertrack
%module_post

%postun mod_usertrack
%module_postun

%post mod_vhost_alias
%module_post

%postun mod_vhost_alias
%module_postun

%post defaultindex
if [ "$1" = "1" ]; then
	%service -q apache reload
fi

%postun defaultindex
if [ "$1" = "0" ]; then
	%service -q apache reload
fi

%post cgi_test
if [ "$1" = "1" ]; then
	%service -q apache reload
fi

%postun cgi_test
if [ "$1" = "0" ]; then
	%service -q apache reload
fi

%files
%defattr(644,root,root,755)

%files base
%defattr(644,root,root,755)
%doc ABOUT_APACHE src/CHANGES README
%doc conf/mime.types conf/apache.conf.dist
%{?with_lingerd:%doc lingerd}
%attr(754,root,root) /etc/rc.d/init.d/apache
%attr(750,root,root) %dir %{_sysconfdir}
%{_sysconfdir}/modules
%{_sysconfdir}/logs
%attr(750,root,root) %dir %{_sysconfdir}/conf.d
%attr(750,root,root) %dir %{_sysconfdir}/webapps.d
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_common.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/apache
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/*
%dir %{_libexecdir}
%if %{with lingerd}
%attr(755,root,root) %{_libexecdir}/lingerd
%attr(770,root,http) %dir %{_localstatedir}/run/lingerd
%endif
%attr(755,root,root) %{_bindir}/checkgid
%attr(755,root,root) %{_sbindir}/apache
%dir %attr(1773,root,http) /var/run/apache
%{_mandir}/man8/apache.8*
%lang(hu) %{_mandir}/hu/man8/apache.8*
%lang(pl) %{_mandir}/pl/man8/apache.8*
%attr(2751,root,logs) %dir /var/log/apache
%attr(2750,root,logs) %dir /var/log/archive/apache
%attr(640,root,logs) %ghost /var/log/apache/*
%dir %{_datadir}/%{name}
%dir %{httpdir}
%dir %{httpdir}/html
%dir %{docroot}

%files cgi_test
%defattr(644,root,root,755)
%dir %{cgibindir}
%attr(755,root,root) %{cgibindir}/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_cgi_test.conf

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/htdigest
%attr(755,root,root) %{_sbindir}/ab
%attr(755,root,root) %{_sbindir}/apachectl
%attr(755,root,root) %{_sbindir}/logresolve
%attr(755,root,root) %{_sbindir}/rotatelogs
%lang(ko) %{_mandir}/ko/man8/ab.8*
%{_mandir}/man1/htdigest.1*
%{_mandir}/man8/ab*
%{_mandir}/man8/apachectl*
%{_mandir}/man8/logresolve.8*
%{_mandir}/man8/rotatelogs.8*

%files defaultindex
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_defaultindex.conf
%config(noreplace,missingok) %{docroot}/index.html
# NOTE: html extensions are not the same as (g)libc locale names
%lang(ca) %{docroot}/index.html.ca
%lang(cs) %{docroot}/index.html.cz
%lang(de) %{docroot}/index.html.de
%lang(da) %{docroot}/index.html.dk
%lang(et) %{docroot}/index.html.ee
%lang(el) %{docroot}/index.html.el
%{docroot}/index.html.en
%lang(es) %{docroot}/index.html.es
%lang(fr) %{docroot}/index.html.fr
%lang(he) %{docroot}/index.html.he.iso8859-8
%lang(hu) %{docroot}/index.html.hu
%lang(it) %{docroot}/index.html.it
%lang(ja) %{docroot}/index.html.ja.jis
%lang(ko) %{docroot}/index.html.kr.iso-kr
%lang(de_LU) %{docroot}/index.html.lb.utf8
%lang(nl) %{docroot}/index.html.nl
%lang(nn) %{docroot}/index.html.nn
%lang(nb) %{docroot}/index.html.no
%lang(pl) %{docroot}/index.html.po.iso-pl
%lang(pt) %{docroot}/index.html.pt
%lang(pt_BR) %{docroot}/index.html.pt-br
%lang(ru) %{docroot}/index.html.ru.cp-1251
%lang(ru) %{docroot}/index.html.ru.cp866
%lang(ru) %{docroot}/index.html.ru.iso-ru
%lang(ru) %{docroot}/index.html.ru.koi8-r
%lang(ru) %{docroot}/index.html.ru.ucs2
%lang(ru) %{docroot}/index.html.ru.ucs4
%lang(ru) %{docroot}/index.html.ru.utf8
%lang(sv) %{docroot}/index.html.se
%lang(zh_TW) %{docroot}/index.html.zh-tw.big5
%{docroot}/*.gif

%files manual
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_manual.conf
%dir %{manualdir}
%dir %{manualdir}/images
%{manualdir}/images/apache_header.gif
%{manualdir}/images/custom_errordocs.gif
%{manualdir}/images/home.gif
%{manualdir}/images/index.gif
%{manualdir}/images/pixel.gif
%{manualdir}/images/sub.gif
%{manualdir}/misc
%{manualdir}/LICENSE
%{manualdir}/bind.html.html
%{manualdir}/bind.html.en
%lang(fr) %{manualdir}/bind.html.fr
%lang(ja) %{manualdir}/bind.html.ja.jis
%{manualdir}/configuring.html.html
%{manualdir}/configuring.html.en
%lang(fr) %{manualdir}/configuring.html.fr
%lang(ja) %{manualdir}/configuring.html.ja.jis
%{manualdir}/content-negotiation.html.html
%{manualdir}/content-negotiation.html.en
%lang(ja) %{manualdir}/content-negotiation.html.ja.jis
%{manualdir}/custom-error.html.html
%{manualdir}/custom-error.html.en
%lang(fr) %{manualdir}/custom-error.html.fr
%lang(ja) %{manualdir}/custom-error.html.ja.jis
%{manualdir}/dns-caveats.html.html
%{manualdir}/dns-caveats.html.en
%lang(fr) %{manualdir}/dns-caveats.html.fr
%lang(ja) %{manualdir}/dns-caveats.html.ja.jis
%{manualdir}/dso.html
%{manualdir}/env.html.html
%{manualdir}/env.html.en
%lang(ja) %{manualdir}/env.html.ja.jis
%{manualdir}/footer.html
%{manualdir}/handler.html.html
%{manualdir}/handler.html.en
%lang(ja) %{manualdir}/handler.html.ja.jis
%{manualdir}/header.html
%{manualdir}/index.html.html
%{manualdir}/index.html.en
%lang(fr) %{manualdir}/index.html.fr
%lang(ja) %{manualdir}/index.html.ja.jis
%{manualdir}/install.html.html
%{manualdir}/install.html.en
%lang(es) %{manualdir}/install.html.es
%lang(fr) %{manualdir}/install.html.fr
%lang(ja) %{manualdir}/install.html.ja.jis
%{manualdir}/invoking.html.html
%{manualdir}/invoking.html.en
%lang(fr) %{manualdir}/invoking.html.fr
%lang(ja) %{manualdir}/invoking.html.ja.jis
%{manualdir}/keepalive.html.html
%{manualdir}/keepalive.html.en
%lang(ja) %{manualdir}/keepalive.html.ja.jis
%{manualdir}/location.html.html
%{manualdir}/location.html.en
%lang(ja) %{manualdir}/location.html.ja.jis
%{manualdir}/logs.html
%{manualdir}/multilogs.html
%{manualdir}/new_features_1_3.html.html
%{manualdir}/new_features_1_3.html.en
%lang(ja) %{manualdir}/new_features_1_3.html.ja.jis
%{manualdir}/process-model.html.html
%{manualdir}/process-model.html.en
%lang(ja) %{manualdir}/process-model.html.ja.jis
%{manualdir}/sections.html.html
%{manualdir}/sections.html.en
%lang(ja) %{manualdir}/sections.html.ja.jis
%{manualdir}/server-wide.html.html
%{manualdir}/server-wide.html.en
%lang(fr) %{manualdir}/server-wide.html.fr
%lang(ja) %{manualdir}/server-wide.html.ja.jis
%{manualdir}/sitemap.html
%{manualdir}/sourcereorg.html
%{manualdir}/stopping.html.html
%{manualdir}/stopping.html.en
%lang(fr) %{manualdir}/stopping.html.fr
%{manualdir}/upgrading_to_1_3.html
%{manualdir}/urlmapping.html
%dir %{manualdir}/howto
%{manualdir}/howto/cgi.html.html
%{manualdir}/howto/cgi.html.en
%lang(ja) %{manualdir}/howto/cgi.html.ja.jis
%{manualdir}/howto/footer.html
%{manualdir}/howto/header.html
%{manualdir}/howto/htaccess.html
%{manualdir}/howto/ssi.html.html
%{manualdir}/howto/ssi.html.en
%lang(ja) %{manualdir}/howto/ssi.html.ja.jis
%dir %{manualdir}/mod
%{manualdir}/mod/core.html.html
%{manualdir}/mod/core.html.en
%lang(fr) %{manualdir}/mod/core.html.fr
%lang(ja) %{manualdir}/mod/core.html.ja.jis
%{manualdir}/mod/directive-dict.html.html
%{manualdir}/mod/directive-dict.html.en
%lang(fr) %{manualdir}/mod/directive-dict.html.fr
%lang(ja) %{manualdir}/mod/directive-dict.html.ja.jis
%{manualdir}/mod/directives.html.html
%lang(de) %{manualdir}/mod/directives.html.de
%{manualdir}/mod/directives.html.en
%lang(fr) %{manualdir}/mod/directives.html.fr
%lang(ja) %{manualdir}/mod/directives.html.ja.jis
%{manualdir}/mod/footer.html
%{manualdir}/mod/header.html
%{manualdir}/mod/index-bytype.html.html
%{manualdir}/mod/index-bytype.html.en
%lang(fr) %{manualdir}/mod/index-bytype.html.fr
%lang(ja) %{manualdir}/mod/index-bytype.html.ja.jis
%{manualdir}/mod/index.html.html
%{manualdir}/mod/index.html.en
%lang(fr) %{manualdir}/mod/index.html.fr
%lang(ja) %{manualdir}/mod/index.html.ja.jis
%{manualdir}/mod/mod_access.html.html
%{manualdir}/mod/mod_access.html.en
%lang(ja) %{manualdir}/mod/mod_access.html.ja.jis
%{manualdir}/mod/mod_alias.html.html
%{manualdir}/mod/mod_alias.html.en
%lang(ja) %{manualdir}/mod/mod_alias.html.ja.jis
%{manualdir}/mod/mod_asis.html.html
%{manualdir}/mod/mod_asis.html.en
%lang(ja) %{manualdir}/mod/mod_asis.html.ja.jis
%{manualdir}/mod/mod_autoindex.html.html
%{manualdir}/mod/mod_autoindex.html.en
%lang(ja) %{manualdir}/mod/mod_autoindex.html.ja.jis
%{manualdir}/mod/mod_cern_meta.html
%{manualdir}/mod/mod_cgi.html.html
%{manualdir}/mod/mod_cgi.html.en
%lang(ja) %{manualdir}/mod/mod_cgi.html.ja.jis
%{manualdir}/mod/mod_env.html.html
%{manualdir}/mod/mod_env.html.en
%lang(ja) %{manualdir}/mod/mod_env.html.ja.jis
%{manualdir}/mod/mod_include.html
%{manualdir}/mod/mod_log_agent.html
%{manualdir}/mod/mod_log_config.html.html
%{manualdir}/mod/mod_log_config.html.en
%lang(ja) %{manualdir}/mod/mod_log_config.html.ja.jis
%{manualdir}/mod/mod_log_referer.html
%{manualdir}/mod/mod_mime.html.html
%{manualdir}/mod/mod_mime.html.en
%lang(ja) %{manualdir}/mod/mod_mime.html.ja.jis
%{manualdir}/mod/mod_mime_magic.html
%{manualdir}/mod/mod_negotiation.html.html
%{manualdir}/mod/mod_negotiation.html.en
%lang(ja) %{manualdir}/mod/mod_negotiation.html.ja.jis
%{manualdir}/mod/mod_setenvif.html.html
%{manualdir}/mod/mod_setenvif.html.en
%lang(ja) %{manualdir}/mod/mod_setenvif.html.ja.jis
%{manualdir}/mod/mod_so.html.html
%{manualdir}/mod/mod_so.html.en
%lang(ja) %{manualdir}/mod/mod_so.html.ja.jis
%{manualdir}/mod/mod_speling.html.html
%{manualdir}/mod/mod_speling.html.en
%lang(ja) %{manualdir}/mod/mod_speling.html.ja.jis
%{manualdir}/mod/mod_userdir.html.html
%{manualdir}/mod/mod_userdir.html.en
%lang(ja) %{manualdir}/mod/mod_userdir.html.ja.jis
%{manualdir}/mod/module-dict.html.html
%{manualdir}/mod/module-dict.html.en
%lang(ja) %{manualdir}/mod/module-dict.html.ja.jis
%dir %{manualdir}/programs
%{manualdir}/programs/ab.html
%{manualdir}/programs/apachectl.html.html
%{manualdir}/programs/apachectl.html.en
%lang(ja) %{manualdir}/programs/apachectl.html.ja.jis
%{manualdir}/programs/apxs.html
%{manualdir}/programs/dbmmanage.html
%{manualdir}/programs/footer.html
%{manualdir}/programs/header.html
%{manualdir}/programs/htdigest.html
%{manualdir}/programs/htpasswd.html.html
%{manualdir}/programs/htpasswd.html.en
%lang(ja) %{manualdir}/programs/htpasswd.html.ja.jis
%{manualdir}/programs/httpd.html.html
%{manualdir}/programs/httpd.html.en
%lang(ja) %{manualdir}/programs/httpd.html.ja.jis
%{manualdir}/programs/index.html.html
%{manualdir}/programs/index.html.en
%lang(ja) %{manualdir}/programs/index.html.ja.jis
%{manualdir}/programs/logresolve.html
%{manualdir}/programs/other.html
%{manualdir}/programs/rotatelogs.html
%dir %{manualdir}/vhosts
%{manualdir}/vhosts/details.html
%{manualdir}/vhosts/examples.html
%{manualdir}/vhosts/fd-limits.html.html
%{manualdir}/vhosts/fd-limits.html.en
%lang(ja) %{manualdir}/vhosts/fd-limits.html.ja.jis
%{manualdir}/vhosts/footer.html
%{manualdir}/vhosts/header.html
%{manualdir}/vhosts/host.html
%{manualdir}/vhosts/index.html.html
%{manualdir}/vhosts/index.html.en
%lang(ja) %{manualdir}/vhosts/index.html.ja.jis
%{manualdir}/vhosts/ip-based.html
%{manualdir}/vhosts/mass.html
%{manualdir}/vhosts/name-based.html.html
%{manualdir}/vhosts/name-based.html.en
%lang(ja) %{manualdir}/vhosts/name-based.html.ja.jis
%{manualdir}/vhosts/vhosts-in-depth.html
%{manualdir}/vhosts/virtual-host.html
# suexec
%{manualdir}/suexec.html.html
%{manualdir}/suexec.html.en
%lang(ja) %{manualdir}/suexec.html.ja.jis
%{manualdir}/programs/suexec.html.html
%{manualdir}/programs/suexec.html.en
%lang(ja) %{manualdir}/programs/suexec.html.ja.jis
# mod_actions
%{manualdir}/mod/mod_actions.html.html
%{manualdir}/mod/mod_actions.html.en
%lang(ja) %{manualdir}/mod/mod_actions.html.ja.jis
# mod_auth
%{manualdir}/howto/auth.html
%{manualdir}/mod/mod_auth.html.html
%{manualdir}/mod/mod_auth.html.en
%lang(ja) %{manualdir}/mod/mod_auth.html.ja.jis
# mod_anon
%{manualdir}/mod/mod_auth_anon.html
# mod_auth_db
%{manualdir}/mod/mod_auth_db.html
# mod_auth_digest
%{manualdir}/mod/mod_auth_digest.html
# mod_define
%{manualdir}/mod/mod_define.html
# mod_digest
%{manualdir}/mod/mod_digest.html
# mod_dir
%{manualdir}/mod/mod_dir.html.html
%{manualdir}/mod/mod_dir.html.en
%lang(ja) %{manualdir}/mod/mod_dir.html.ja.jis
# mod_expires
%{manualdir}/mod/mod_expires.html
# mod_headers
%{manualdir}/mod/mod_headers.html
# mod_imap
%{manualdir}/mod/mod_imap.html
# mod_info
%{manualdir}/mod/mod_info.html.html
%{manualdir}/mod/mod_info.html.en
%lang(ja) %{manualdir}/mod/mod_info.html.ja.jis
# mod_log_forensic
%{manualdir}/mod/mod_log_forensic.html.html
%{manualdir}/mod/mod_log_forensic.html.en
# mod_mmap_static
%{manualdir}/mod/mod_mmap_static.html
# mod_proxy
%{manualdir}/mod/mod_proxy.html
# mod_rewrite
%{manualdir}/mod/mod_rewrite.html.html
%{manualdir}/mod/mod_rewrite.html.en
%lang(ja) %{manualdir}/mod/mod_rewrite.html.ja.jis
%{manualdir}/images/mod_rewrite*
# mod_status
%{manualdir}/mod/mod_status.html
# mod_unique_id
%{manualdir}/mod/mod_unique_id.html.html
%{manualdir}/mod/mod_unique_id.html.en
%lang(ja) %{manualdir}/mod/mod_unique_id.html.ja.jis
# mod_usertrack
%{manualdir}/mod/mod_cookies.html
%{manualdir}/mod/mod_usertrack.html
# mod_vhost_alias
%{manualdir}/mod/mod_vhost_alias.html

%files errordocs
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_errordocs.conf
%{_datadir}/%{name}/errordocs

%files suexec
%defattr(644,root,root,755)
%attr(4755,root,root) %{_sbindir}/suexec
%{_mandir}/man8/suexec.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{apxs}
%{_mandir}/man8/apxs1.8*
%{_includedir}

%files -n htpasswd-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/htpasswd
%attr(755,root,root) %{_sbindir}/htpasswd
%{_mandir}/man1/htpasswd.1*

%files mod_access
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_access.conf
%attr(755,root,root) %{_libexecdir}/mod_access.so

%files mod_actions
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_actions.conf
%attr(755,root,root) %{_libexecdir}/mod_actions.so

%files mod_alias
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_alias.conf
%attr(755,root,root) %{_libexecdir}/mod_alias.so

%files mod_asis
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_asis.conf
%attr(755,root,root) %{_libexecdir}/mod_asis.so

%files mod_auth
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_auth.so

%files mod_auth_anon
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_auth_anon.conf
%attr(755,root,root) %{_libexecdir}/mod_auth_anon.so

%files mod_auth_db
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_auth_db.conf
%attr(755,root,root) %{_libexecdir}/mod_auth_db.so
%attr(755,root,root) %{_bindir}/dbmmanage
%{_mandir}/man1/dbmmanage.1*

%files mod_auth_digest
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_auth_digest.conf
%attr(755,root,root) %{_libexecdir}/mod_auth_digest.so

%files mod_autoindex
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_autoindex.conf
%attr(755,root,root) %{_libexecdir}/mod_autoindex.so
%{_datadir}/apache-icons/*.gif

%files mod_cern_meta
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_cern_meta.conf
%attr(755,root,root) %{_libexecdir}/mod_cern_meta.so

%files mod_cgi
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_cgi.conf
%attr(755,root,root) %{_libexecdir}/mod_cgi.so

%files mod_define
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_define.conf
%attr(755,root,root) %{_libexecdir}/mod_define.so

%files mod_digest
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_digest.conf
%attr(755,root,root) %{_libexecdir}/mod_digest.so

%files mod_dir
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_dir.conf
%attr(755,root,root) %{_libexecdir}/mod_dir.so

%files mod_env
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_env.conf
%attr(755,root,root) %{_libexecdir}/mod_env.so

%files mod_expires
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_expires.conf
%attr(755,root,root) %{_libexecdir}/mod_expires.so

%files mod_headers
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_headers.conf
%attr(755,root,root) %{_libexecdir}/mod_headers.so

%files mod_imap
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_imap.conf
%attr(755,root,root) %{_libexecdir}/mod_imap.so

%files mod_include
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_include.conf
%attr(755,root,root) %{_libexecdir}/mod_include.so

%files mod_info
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_info.conf
%attr(755,root,root) %{_libexecdir}/mod_info.so

%files mod_log_agent
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_log_agent.conf
%attr(755,root,root) %{_libexecdir}/mod_log_agent.so

%files mod_log_config
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_log_config.conf
%attr(755,root,root) %{_libexecdir}/mod_log_config.so

%files mod_log_forensic
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_log_forensic.conf
%attr(755,root,root) %{_libexecdir}/mod_log_forensic.so

%files mod_log_referer
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_log_referer.conf
%attr(755,root,root) %{_libexecdir}/mod_log_referer.so

%files mod_mime
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_mime.conf
%attr(755,root,root) %{_libexecdir}/mod_mime.so

%files mod_mime_magic
%defattr(644,root,root,755)
%attr(640,root,root) %{_sysconfdir}/magic
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_mime_magic.conf
%attr(755,root,root) %{_libexecdir}/mod_mime_magic.so

%files mod_mmap_static
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_mmap_static.conf
%attr(755,root,root) %{_libexecdir}/mod_mmap_static.so

%files mod_negotiation
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_negotiation.conf
%attr(755,root,root) %{_libexecdir}/mod_negotiation.so

%files mod_proxy
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_proxy.conf
%attr(755,root,root) %{_libexecdir}/libproxy.so
%dir %attr(770,root,http) /var/cache/apache

%files mod_rewrite
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_rewrite.conf
%attr(755,root,root) %{_libexecdir}/mod_rewrite.so

%files mod_setenvif
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_setenvif.conf
%attr(755,root,root) %{_libexecdir}/mod_setenvif.so

%files mod_speling
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_speling.conf
%attr(755,root,root) %{_libexecdir}/mod_speling.so

%files mod_status
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_status.conf
%attr(755,root,root) %{_libexecdir}/mod_status.so

%files mod_unique_id
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_unique_id.conf
%attr(755,root,root) %{_libexecdir}/mod_unique_id.so

%files mod_userdir
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_userdir.conf
%attr(755,root,root) %{_libexecdir}/mod_userdir.so

%files mod_usertrack
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_usertrack.conf
%attr(755,root,root) %{_libexecdir}/mod_usertrack.so

%files mod_vhost_alias
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_vhost_alias.conf
%attr(755,root,root) %{_libexecdir}/mod_vhost_alias.so
