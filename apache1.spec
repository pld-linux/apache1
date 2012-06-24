# TODO
# - move DocumentRoot and cgi-dir out of /home/services
#
# Conditional build:
%bcond_with	rewrite_ldap	# enable ldap map support for mod_rewrite (alpha)
%bcond_without	ipv6		# disable IPv6 support
%bcond_with	minimal		# minimal apache, without any modules
#
%include	/usr/lib/rpm/macros.perl
Summary:	The most widely used Web server on the Internet
Summary(cs):	Nejroz���en�j�� WWW server v Internetu
Summary(da):	Den mest brugte web-tjener p� Internet
Summary(de):	Der am h�ufigsten verwendete Web-Server im Internet
Summary(es):	El servidor web m�s conocido y usado en Internet
Summary(fr):	Le serveur Web le plus utilis� sur Internet
Summary(id):	Web server yang paling banyak digunakan di Internet
Summary(is):	Vins�lasti vef�j�nninn � Netinu
Summary(it):	Il web server pi� diffuso su Internet
Summary(ja):	���󥿡��ͥåȾ�ǺǤ����Ū�˻��Ѥ���Ƥ��� Web �����С�
Summary(nb):	Den mest utbredte web-tjeneren p� Internett
Summary(pl):	Serwer WWW (World Wide Web)
Summary(pt):	O servidor Web mais largamente utilizado em toda a Internet
Summary(pt_BR):	Servidor HTTPD para prover servi�os WWW
Summary(ru):	����� ���������� Web-Server
Summary(sk):	Najviac pou��van� Web server na Internete
Summary(sl):	Najbolj uporabljani spletni stre�nik interneta
Summary(sv):	Den mest anv�nda webbservern p� Internet
Summary(tr):	Lider WWW taray�c�
Summary(uk):	����������Φ��� Web-Server
Summary(zh_CN):	Internet ��Ӧ����㷺�� Web �������
Name:		apache1
Version:	1.3.34
Release:	2
License:	Apache Group
Group:		Networking/Daemons
Source0:	http://www.apache.org/dist/httpd/apache_%{version}.tar.gz
# Source0-md5:	9978cc552b423f0015c1052d23ab619e
Source1:	%{name}.init
Source2:	%{name}.logrotate
Source3:	apache-icons.tar.gz
# Source3-md5:	2b085cbc19fd28536dc883f0b864cd83
Source4:	%{name}.sysconfig
Source5:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/apache-non-english-man-pages.tar.bz2
# Source5-md5:	74ff6e8d8a7b365b48ed10a52fbeb84e
Source6:	%{name}.monitrc
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
Patch0:		%{name}-PLD.patch
Patch1:		%{name}-suexec.patch
Patch2:		%{name}-errordocs.patch
Patch3:		%{name}-apxs.patch
Patch4:		%{name}-mod_ssl-addon.patch
Patch5:		%{name}-mod_ssl-eapi.patch
Patch6:		%{name}-EAPI_MM_CORE_PATH-correction.patch
Patch7:		%{name}-EAPI_MM=SYSTEM.patch
Patch8:		%{name}-ipv6-PLD.patch
Patch9:		%{name}-modules_symbols.patch
Patch10:	%{name}-apxs_force_rm_cp.patch
Patch11:	%{name}-db3.patch
Patch12:	%{name}-lookup_map_ldap.patch
Patch13:	%{name}-man.patch
Patch14:	%{name}-fpic.patch
Patch15:	%{name}-buff.patch
Patch16:	%{name}-mkstemp.patch
Patch17:	%{name}-EAPI-missing_files.patch
Patch18:	%{name}-PLD-nov6.patch
Patch19:	%{name}-configdir_skip_backups.patch
Patch20:	%{name}-apxs-quiet.patch
Patch21:	%{name}-db4.patch
URL:		http://httpd.apache.org/
BuildRequires:	db-devel >= 4.1
BuildRequires:	mm-devel >= 1.3.0
%{?with_rewrite_ldap:BuildRequires:	openldap-devel}
BuildRequires:	rpmbuild(macros) >= 1.247
BuildRequires:	rpm-build >= 4.4.0
BuildRequires:	rpm-perlprov
BuildRequires:	perl-base
Requires:		mm
Requires:		rc-scripts
%if %{without minimal}
# essental modules (maybe remove these in future if all Requires in
# place for other packages).
Requires:	%{name}-mod_access = %{version}-%{release}
Requires:	%{name}-mod_alias = %{version}-%{release}
Requires:	%{name}-mod_log_config = %{version}-%{release}
Requires:	%{name}-mod_mime = %{version}-%{release}
%endif
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getent
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(pre):	/usr/sbin/usermod
Requires(pre):	textutils
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(triggerpostun):	sed >= 4.0
Requires:	/etc/mime.types
Requires:	mailcap
Requires:	psmisc >= 20.1
Provides:	%{name}(EAPI) = %{version}-%{release}
Provides:	group(http)
Provides:	httpd = %{version}
Provides:	user(http)
Provides:	webserver = apache
Provides:	apache = %{version}-%{release}
%{?with_ipv6:Provides:	apache1(ipv6)}
Obsoletes:	apache < 2.0.0
Obsoletes:	apache-extra
Obsoletes:	apache6
# for the posttrans scriptlet, conflicts because in vserver environment rpm package is not installed.
Conflicts:	rpm < 4.4.2-0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/apache
%define		_includedir	%{_prefix}/include/apache1
%define		_libexecdir	%{_prefix}/%{_lib}/apache1
%define		_datadir	%{httpdir}
%define		apxs		/usr/sbin/apxs1
%define		httpdir		/home/services/apache
%define		manualdir	%{_prefix}/share/apache1-manual

%description
Apache is a powerful, full-featured, efficient and freely-available
Web server. Apache is also the most popular Web server on the
Internet.

%description -l cs
Apache je v�konn� pln� funk�n� efektivn� a voln� dostupn� WWW server.
Je to nejpopul�rn�j�� WWW server v Internetu.

%description -l da
Apache er en st�rk, funktionsrig, effektiv og frit tilg�ngelig
web-tjener. Apache er ogs� den mest popul�re web-tjener p� Internet.

%description -l de
Apache ist ein leistungsf�higer, frei verf�gbarer und effizienter
Web-Server mit umfassenden Funktionen. Apache ist zudem der popul�rste
Web-Server im Internet.

%description -l es
El servidor web Apache es el mejor servidor gratuito disponible en el
mundo UNIX hoy. Usa HTTP (HyperText Transfer Protocol) para permitir
que browsers web vean documentos y sometan datos remotamente. Puede
ejecutar varias funciones diferentes, incluyendo funciones de proxy y
cach�, y nos ofrece caracter�sticas como monitor de estado, conversi�n
din�mica de tipo, y otras m�s.

%description -l fr
Apache est un serveur Web puissant, efficace, gratuit et complet.
Apache est aussi le serveur Web le plus populaire sur Internet.

%description -l id
Apache adalah Web server yang powerful, efisien, kaya akan feature,
dan tersedia dengan free. Apache juga merupakan Web server yang paling
populer di Internet.

%description -l is
Apache er mj�g �flugur og h��r�a�ur vef�j�nn sem er �keypis. Apache er
einnig mest nota�i vef�j�nninn � Internetinu.

%description -l it
Apache � un Web server potente, dotato di tutte le caratteristiche,
efficiente e gratuito. Ed � anche il web server pi� diffuso su
Internet.

%description -l ja
Apache �϶��Ϥǽ��¤�����ǽ�����̵���� Web �����С�
�Ǥ����ޤ���apache �ϥ��󥿡��ͥåȾ�ǺǤ����Ū�˻��� ����Ƥ��� Web
�����С��Ǥ���

%description -l nb
Apache er en kraftig, funksjonsrik, effektiv og fritt tilgjengelig
web-tjener. Apache er ogs� den mest popul�re web-tjeneren p� Internet.

%description -l pl
Apache jest serwerem WWW (World Wide Web). Instaluj�c ten pakiet
b�dziesz m�g� prezentowa� w�asne strony WWW w sieci internet.

%description -l pt
O Apache � um servidor de Web poderoso, cheio de potencialidades,
eficiente e gratuito. O Apache � tamb�m o servidor Web mais conhecido
na Internet.

%description -l pt_BR
O servidor web Apache � o melhor servidor gratuito dispon�vel no mundo
UNIX hoje. Ele usa HTTP (HyperText Transfer Protocol) para permitir
que browsers web vejam documentos e submetam dados remotamente. Ele
pode executar v�rias fun��es diferentes, incluindo fun��es de proxy e
cache, e oferece caracter�sticas como monitor de status, convers�o
din�mica de tipo, e mais.

%description -l ru
Apache - ��� ������, �������������������, �����������, ��������
���������������� � ����� ���������� � Internet WWW-������.

%description -l sk
Apache je v�konn�, efekt�vny a vo�ne dostupn� Web server, bohat� na
funkcie. Apache je tie� najpopul�rnej��m Web serverom na Internete.

%description -l sv
Apache �r en kraftfull, finessrik, effektiv och fritt tillg�nglig
webbserver. Apache �r ocks� den popul�raste webbservern p� Internet.

%description -l tr
Apache serbest da��t�lan ve �ok kullan�lan yetenekli bir web
sunucusudur.

%description -l zh_CN
Apache �ǹ���ǿ����ȫ����Ч������ṩ�� Web ������� ͬʱҲ��
Internet �������е� Web �������

�������Ҫ Web ��������밲װ apache �������

%package suexec
Summary:	Apache suexec wrapper
Summary(pl):	Suexec wrapper do serwera WWW Apache
Summary(ru):	Apache suEXEC CGI wrapper
Summary(uk):	Apache suEXEC CGI wrapper
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Obsoletes:	apache-suexec < 2.0.0

%description suexec
The suEXEC feature provides Apache users the ability to run CGI and
SSI programs under user IDs different from the user ID of the calling
web-server. Normally, when a CGI or SSI program executes, it runs as
the same user who is running the web server.

%description suexec -l pl
SuEXEC umo�liwia serwerowi Apache uruchamianie program�w CGI i SSI z
innym UID ni� wywo�uj�cy je serwer. Normalnie programy CGI i SSI s�
wykonywane jako taki sam u�ytkownik jak serwer WWW.

%description suexec -l ru
����� suEXEC ��������� ��������� CGI-��������� ��� user-id, ���������
�� ����, ��� ������� �������� ���������� �� web-������. ������
��������� ��������������, ���� ����� ��������� ������� ������� ����
��������� ��������� ������������, ��������� ����������� �������
������������� CGI-��������. ������ � ���, ������ �����������
������������������, ���� ����� ����� ��������� ���� �������, ����� ���
��� � ������� ������ �� ������ ����������� ����� :)). ���� �� ��
������ ����� ������ � setuid root ����������� � ���������� ���������
������������, ������������ �� �����������, ������������ ����������� ��
������������ ����� ������...

%description suexec -l uk
����� suEXEC ������Ѥ ��������� CGI-�������� Ц� user-id, צ�ͦ����
צ� ����, Ц� ���� ������ ������. ��� ����������� ����������Φ, ���
����� ������Ѥ ��ͦ��� ������� ����� ��������� �������ϧ �������,
���������� �������� ������� ������������� CGI-�������. ����� � ���,
��� ��צ����� ���Ʀ�������Φ, ��� ����� ���� ���������� ���� �������,
������� ��� Ħ� � ������� ���ۦ � ������ ���Ӧ����� ����� :)). ���� ��
�� ����� ���צ�� ������ � setuid root ���������� �� ����������
�������ϧ �������, ���Ҧ �������Φ ������������� ����� �������,
���Ԧ����� ������ �� ��������������� ����� ������...

%package apxs
Summary:	APache eXtenSion tool
Summary(pl):	Narz�dzie do rozszerzania Apache'a
Group:		Development/Tools

%description apxs
APache eXtenSion tool.

%description apxs -l pl
Narz�dzie do rozszerzania Apache'a.

%package tools
Summary:	Apache tools
Summary(pl):	Narz�dzia Apache'a
Group:		Development/Tools

%description tools
Apache tools.

%description tools -l pl
Narz�dzia Apache'a.

%package index
Summary:	Apache index.html* files
Summary(pl):	Pliki Apache index.html*
Group:		Documentation
Requires:	%{name} = %{version}-%{release}
Obsoletes:	indexhtml

%description index
Apache index.html* files.

%description index -l pl
Pliki Apache index.html*.

%package doc
Summary:	Apache 1.3.x manual
Summary(pl):	Podr�cznik do Apache'a 1.3.x
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Apache 1.3.x manual.

%description doc -l pl
Podr�cznik do Apache'a 1.3.x.

%package errordocs
Summary:	Apache 1.3.x HTTP error documents
Summary(pl):	Dokumenty opisuj�ce b��dy HTTP dla Apache'a 1.3.x
Group:		Applications/WWW
Requires:	%{name}-mod_include = %{version}-%{release}

%description errordocs
Apache 1.3.x HTTP error documents. Currently in English and Polish
only.

%description errordocs -l pl
Dokumenty opisuj�ce b��dy HTTP dla Apache'a 1.3.x. Aktualnie tylko po
angielsku i polsku.

%package devel
Summary:	Module development tools for the Apache web server
Summary(cs):	Hlavi�kov� soubory pro Apache Web server
Summary(da):	Header-filer for Apache webserveren
Summary(de):	Include-Dateien f�r den Apache Web-Server
Summary(es):	Archivos de inclusi�n del Apache para desarrollo de m�dulos
Summary(fr):	Fichiers � inclure pour le serveur Web Apache
Summary(id):	File header untuk Apache Web server
Summary(is):	Hausaskr�r me� Apache vef�j�ninum
Summary(it):	File include per il web server Apache
Summary(ja):	Apache Web �����С��Ѥγ�ȯ�ġ���
Summary(nb):	Headerfiler for webtjeneren Apache
Summary(pl):	Pliki nag��wkowe do tworzenia modu��w rozszerze� do serwera WWW Apache
Summary(pt):	Ficheiros de inclus�o para o servidor Web Apache
Summary(pt_BR):	Arquivos de inclus�o do Apache para desenvolvimento de m�dulos
Summary(ru):	����� ���������� ��� web server'� Apache
Summary(sk):	Hlavi�kov� s�bory pre Apache Web server
Summary(sl):	Glave za spletni stre�nik Apache
Summary(sv):	Huvudfiler f�r webbservern Apache
Summary(uk):	������ ��������� ����̦� ��� web server'� Apache
Summary(zh_CN):	���� Apache Web �������Ŀ������ߡ�
Group:		Networking/Utilities
Requires:	%{name}-apxs = %{version}-%{release}
Provides:	%{name}(EAPI)-devel = %{version}-%{release}
Provides:	apache(EAPI)-devel = %{version}-%{release}
%{?with_ipv6:Provides:	apache1(ipv6)-devel}
Obsoletes:	apache-devel < 2.0.0

%description devel
The apache-devel package contains header files for Apache.

%description devel -l cs
Bal��ek apache-devel obsahuje hlavi�kov� soubory pro Apache.

%description devel -l da
Apache-devel pakken indeholder headerfiler for Apache.

%description devel -l de
Das Paket apache-devel enth�lt Header-Dateien f�r Apache.

%description devel -l es
Este paquete contiene los archivos de inclusi�n para el Apache.

%description devel -l fr
Le package apache-devel contient le code source pour le serveur Web
Apache.

%description devel -l id
Package apache-devel berisi source code dari Apache Web server.

%description devel -l is
Apache-devel pakkinn inniheldur frumk��a Apache vef�j�nsins.

%description devel -l it
Il pacchetto apache-devel contiene i file header per Apache.

%description devel -l nb
Apache-devel pakken inneholder headerfiler for Apache.

%description devel -l pl
Pliki nag��wkowe dla serwera WWW Apache.

%description devel -l pt
O pacote apache-devel cont�m outros ficheiros para o Apache.

%description devel -l pt_BR
Este pacote contem os arquivos de inclus�o para o Apache.

%description devel -l ru
����� apache-devel �������� ������ ��� Web Server'�.

%description devel -l sk
Bal�k apache-devel obsahuje zdrojov� k�d Apache Web servera.

%description devel -l sv
Paketet apache-devel inneh�ller huvudfilerna f�r Apache.

%description devel -l uk
����� apache-devel ͦ����� ������ ��� Web Server'�.

%package mod_access
Summary:	Access control based on client hostname or IP address
Summary(pl):	Kontrola dost�pu w oparciu o nazw� hosta lub adres IP klienta
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_access) = %{version}-%{release}

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

%description mod_access -l pl
Dyrektyw dostarczanych przez mod_access mo�na u�ywa� w sekcjach
<Directory>, <Files> i <Location>, a tak�e plikach .htaccess w celu
kontrolowania dost�pu do poszczeg�lnych cz�ci serwera. Dost�p mo�e
by� kontrolowany w oparciu o nazw� hosta lub adres IP klienta albo
inn� charakterystyk� ��dania klienta wychwycon� przez zmienne
�rodowiskowe. Dyrektywy Allow i Deny s� u�ywane w celu okre�lenia
kt�rzy klienci maj� dost�p do serwera, a kt�rzy go nie maj�, natomiast
dyrektywa Order ustawia stan domy�lny i okre�la spos�b, w jaki
dyrektywy Allow i Deny wp�ywaj� na siebie nawzajem.

%package mod_actions
Summary:	Apache module for run CGI whenever a file of a certain type is requested
Summary(pl):	Modu� dla Apache'a do uruchamiania skrypt�w cgi
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_actions) = %{version}-%{release}
Obsoletes:	apache-mod_actions < 2.0.0

%description mod_actions
This package contains mod_actions module. This module lets you run CGI
scripts whenever a file of a certain type is requested. This makes it
much easier to execute scripts that process files.

%description mod_actions -l pl
Ten modu� pozwala na uruchamianie skrypt�w CGI w momencie gdy
nadchodzi ��danie pobrania pliku okre�lonego typu. Znacznie u�atwia to
wykonywanie skrypt�w przetwarzaj�cych pliki.

%package mod_alias
Summary:	Mapping different parts of the host filesystem in the document tree, and URL redirection
Summary(pl):	Odwzorowywanie cz�ci systemu plik�w w drzewie dokument�w oraz przekierowywanie URL-i
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_alias) = %{version}-%{release}

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

%description mod_alias -l pl
Ten modu� umo�liwia odwzorowywanie r�nych cz�ci systemu plik�w
serwera w drzewie dokument�w oraz przekierowywanie URL-i. Dyrektywy
obs�ugiwane przez ten modu� umo�liwiaj� manipulowanie i kontrol� URL-i
podczas przychodzenia ��da� do serwera. Dyrektywy Alias i ScriptAlias
s�u�� do odwzorowywania pomi�dzy URL-ami i �cie�kami w systemie
plik�w. Pozwala to na udost�pnianie tre�ci nie umieszczonej
bezpo�rednio wewn�trz DocumentRoota jako cz�ci drzewa dokument�w WWW.
Dyrektywa ScriptAlias ponadto oznacza katalog docelowy jako
zawieraj�cy wy��cznie skrypty CGI.

Dyrektywy Redirect s�u�� do instruowania klient�w o konieczno�ci
wys�ania nowego ��dania z innym URL-em. S� one zwykle u�ywane w
sytuacji, kiedy zasoby zosta�y przeniesione w nowe miejsce.

Pot�niejszy i bardziej elastyczny zbi�r dyrektyw do manipulowania
URL-ami znajduje si� w module mod_rewrite.

%package mod_asis
Summary:	Sending files which contain their own HTTP headers
Summary(pl):	Wysy�anie plik�w zawieraj�cych w�asne nag��wki HTTP
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

%description mod_asis -l pl
Ten modu� dostarcza funkcj� obs�ugi send-as-is powoduj�c�, �e Apache
wysy�a dokument bez dodawania wi�kszo�ci zwykle stosowanych nag��wk�w
HTTP.

Mo�e on s�u�y� do wysy�ania z serwera dowolnego rodzaju danych,
w��cznie z przekierowaniami i innymi specjalnymi odpowiedziami HTTP
bez u�ycia skryptu CGI czy nph.

Ze wzgl�d�w historycznych ten modu� przetwarza tak�e wszelkie pliki o
typie MIME httpd/send-as-is.

%package mod_auth
Summary:	Apache module with user authentication using textual files
Summary(pl):	Modu� uwierzytelniania u�ytkownika przy u�yciu plik�w tekstowych dla Apache
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Requires:	htpasswd
Provides:	apache(mod_auth) = %{version}-%{release}
Obsoletes:	apache-mod_auth < 2.0.0

%description mod_auth
This package contains mod_auth module. It provides for user
authentication using textual files.

%description mod_auth -l pl
Ten pakiet zawiera modu� mod_auth. S�u�y on do uwierzytelniania przy
u�yciu plik�w tekstowych.

%package mod_auth_anon
Summary:	Apache module with "anonymous" user access authentication
Summary(pl):	Modu� apache oferuj�cy anonimow� autoryzacj� u�ytkownia
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

%description mod_auth_anon -l pl
Ten modu� oferuje anonimow� autoryzacj� u�ytkownia podobnie do
anonimowych serwer�w FTP (u�ytkownik "anonymous" oraz has�o w postaci
adresu pocztowego u�ytkownika). Podawane adresy mog� by� logowane. W
po��czeniu z innymi (opartymi o bazy danych) metodami kontroli dost�pu
umo�liwia efektywne �ledzenie u�ytkownik�w i dostosowywanie w
zale�no�ci od profilu u�ytkownika, jednocze�nie zachowuj�c stron�
otwart� dla "niezarejestrowanych" u�ytkownik�w. Jedn� z zalet u�ywania
�ledzenia u�ytkownik�w opartego o uwierzytelnienie nad ciasteczkami i
�miesznymi prze-/przyrostkami URL-i jest ca�kowita niezale�no�� od
przegl�darki i umo�liwienie u�ytkownikom wsp�dzielenia URL-i.

%package mod_auth_db
Summary:	Apache module with user authentication which uses Berkeley DB files
Summary(pl):	Modu� Apache'a z mechanizmem uwierzytelniania u�ywaj�cym plik�w Berkeley DB
Group:		Networking/Daemons
Requires(triggerpostun):	sed >= 4.0
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_auth_db) = %{version}-%{release}
Obsoletes:	apache-mod_auth_db < 2.0.0

%description mod_auth_db
This package contains mod_auth_db module. It provides for user
authentication using Berkeley DB files.

%description mod_auth_db -l pl
Ten pakiet zawiera modu� mod_auth_db. Modu� ten s�u�y do
uwierzytelniania, ale jako plik�w danych u�ywa Berkeley DB.

%package mod_auth_digest
Summary:	Apache user authentication module using MD5 Digest Authentication
Summary(pl):	Modu� Apache'a do uwierzytelniania metod� MD5 Digest Authentication
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Obsoletes:	%{name}-mod_digest
Provides:	apache(mod_auth_digest) = %{version}-%{release}
Obsoletes:	apache-mod_auth_digest < 2.0.0

%description mod_auth_digest
This package contains mod_digest module. It provides user
authentication using MD5 Digest Authentication.

%description mod_auth_digest -l pl
Modu� ten dostarcza metod� uwierzytelniania przy u�yciu MD5 Digest
Authentication.

%package mod_autoindex
Summary:	Apache module - display index of files
Summary(pl):	Modu� apache do wy�wietlania indeksu plik�w
Group:		Networking/Daemons
Requires(triggerpostun):	sed >= 4.0
Provides:	apache(mod_autoindex) = %{version}-%{release}
Requires:	%{name}(EAPI) = %{version}-%{release}

%description mod_autoindex
This package contains mod_autoindex module. It provides generation
index of files.

%description mod_autoindex -l pl
Ten pakiet dostarcza modu� autoindex, kt�ry generuje indeks plik�w.

%package mod_cern_meta
Summary:	Support for HTTP header metafiles
Summary(pl):	Obs�uga metaplik�w nag��wk�w HTTP
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

%description mod_cern_meta -l pl
Modu� emuluj�cy semantyk� metaplik�w CERN HTTPD. Metapliki to nag��wki
HTTP, kt�re mog� by� wysy�ane opr�cz normalnego zestawu nag��wk�w dla
ka�dego przetwarzanego pliku. Zachowuj� si� bardziej jak pliki .asis
Apache'a i mog� dawa� brutalny spos�b wp�ywania na nag��wek Expires:,
a tak�e dostarcza� inne ciekawostki. Jest wiele sposob�w zarz�dzania
metainformacjami, ta zosta�a wybrana poniewa� istnieje ju� wielu
u�ytkownik�w CERN wykorzystuj�cych ten modu�.

%package mod_cgi
Summary:	Invoking CGI scripts
Summary(pl):	Wywo�ywanie skrypt�w CGI
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_cgi) = %{version}-%{release}

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

%description mod_cgi -l pl
Ten modu� powoduje, �e dowolny plik o typie MIME
application/x-httpd-cgi albo procedurze obs�ugi cgi-script (w Apache'u
1.1 lub nowszym) b�dzie traktowany jako skrypt CGI i uruchamiany przez
serwer, a jego wyj�cie b�dzie zwracane klientowi. Pliki uzyskuj� ten
typ przez posiadanie nazwy zawieraj�cej rozszerzenie okre�lone
dyrektyw� AddType lub b�d�c w katalogu ScriptAlias. Pliki nie b�d�ce w
katalogu ScriptAlias, ale maj�ce typ application/x-httpd-cgi dzi�ki
dyrektywie AddType nie b�d� jednak wykonywane, chyba �e w��czona
zostanie opcja ExecCGI - wi�cej szczeg��w w dyrektywie Options.

%package mod_define
Summary:	Apache module - definition variables for arbitrary directives
Summary(pl):	Modu� Apache'a do definiowania zmiennych
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_define) = %{version}-%{release}
Obsoletes:	apache-mod_define < 2.0.0

%description mod_define
It provides the definition variables for arbitrary directives, i.e.
variables which can be expanded on any(!) directive line.

%description mod_define -l pl
Modu� ten umo�liwia definicj� zmiennych dla dowolnych dyrektyw, tzn.
zmiennych, kt�re mog� by� rozwijane w dowolnej linii dyrektywy.

%package mod_digest
Summary:	Older version of apache user authentication module using MD5 Digest Authentication
Summary(pl):	Starsza wersja modu�u apache do autoryzacji MD5
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

%description mod_digest -l pl
Modu� ten dostarcza metod� autoryzacji bazuj�c� na MD5 Digest
Authentication. Implementuje on jedynie starsz� wersj� specyfikacji
uwierzytelniania MD5, i mo�e nie dzia�a� z nowoczesnymi
przegl�darkami. Lepiej u�y� modu�u mod_auth_digest implementuj�cego
najnowsz� wersj� standardu.

%package mod_dir
Summary:	Apache module for "trailing slash" redirects and serving directory index files
Summary(pl):	Modu� oferuj�cy przekierowania i serwowanie indeksu katalogu
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_dir) = %{version}-%{release}
Obsoletes:	apache-mod_dir < 2.0.0

%description mod_dir
This package contains mod_dir which provides "trailing slash"
redirects and serving directory index files.

%description mod_dir -l pl
Modu� oferuj�cy przekierowania o "ko�cowy slash" oraz przekierowania i
udost�pnianie indeksu katalogu.

%package mod_env
Summary:	Passing of environments to CGI scripts
Summary(pl):	Przekazywanie �rodowiska do skrypt�w CGI
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_env) = %{version}-%{release}

%description mod_env
This module allows for control of the environment that will be
provided to CGI scripts and SSI pages. Environment variables may be
passed from the shell which invoked the httpd process. Alternatively,
environment variables may be set or unset within the configuration
process.

%description mod_env -l pl
Ten modu� pozwala na kontrol� �rodowiska udost�pnianego skryptom CGI i
stronom SSI. Zmienne �rodowiskowe mog� by� przekazywane z pow�oki w
czasie uruchamiania procesu httpd, albo - alternatywnie - ustawiane i
usuwane w procesie konfiguracji.

%package mod_expires
Summary:	Apache module which generates Expires HTTP headers
Summary(pl):	Modu� generuj�cy nag��wki HTTP Expires
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_expires) = %{version}-%{release}
Obsoletes:	apache-mod_expires < 2.0.0

%description mod_expires
This module controls the setting of the Expires HTTP header in server
responses. The expiration date can set to be relative to either the
time the source file was last modified, or to the time of the client
access.

%description mod_expires -l pl
Modu� kontroluje ustawianie nag��wka HTTP Expires. Data wyga�ni�cia
wa�no�ci mo�e by� ustalana w zale�no�ci od czasu modyfikacji plik�w
�r�d�owych lub odwo�ania klienta.

%package mod_headers
Summary:	Apache module allows for the customization of HTTP response headers
Summary(pl):	Modu� pozwalaj�cy na modyfikacj� nag��wk�w HTTP
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_headers) = %{version}-%{release}
Obsoletes:	apache-mod_headers < 2.0.0

%description mod_headers
This package contains mod_headers module. The module allows for the
customization of HTTP response headers. Headers can be merged,
replaced or removed.

%description mod_headers -l pl
Modu� pozwalaj�cy na ��czenie, usuwania, zamian� nag��wk�w HTTP
wysy�anych do przegl�darki. Nag��wki mog� by� ��czone, zast�powane lub
usuwane.

%package mod_imap
Summary:	Apache module with imap-file handler
Summary(pl):	Modu� Apache'a z obs�ug� imap-file
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_imap) = %{version}-%{release}
Obsoletes:	apache-mod_imap < 2.0.0

%description mod_imap
This package contains mod_imap module. It provides for .map files,
replacing the functionality of the imagemap CGI program. Any directory
or document type configured to use the handler imap-file.

%description mod_imap -l pl
Modu� umo�liwiaj�cy obs�ug� plik�w .map, zast�puj�cy funkcjonalno��
programu CGI imagemap.

%package mod_include
Summary:	Server-parsed documents
Summary(pl):	Dokumenty przetwarzane po stronie serwera
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_include) = %{version}-%{release}

%description mod_include
This module provides a handler which will process files before they
are sent to the client. The processing is controlled by specially
formated SGML comments, referred to as elements. These elements allow
conditional text, the inclusion other files or programs, as well as
the setting and printing of environment variables.

%description mod_include -l pl
Ten modu� dostarcza procedur� obs�ugi przetwarzaj�c� pliki przed
wys�aniem ich do klienta. Przetwarzanie jest sterowane specjalnie
sformatowanymi komentarzami SGML, nazywanymi elementami. Elementy te
pozwalaj� na tekst warunkowy, do��czanie innych plik�w lub program�w,
a tak�e ustawianie i wypisywanie zmiennych �rodowiskowych.

%package mod_info
Summary:	Apache module with comprehensive overview of the server configuration
Summary(pl):	Modu� dostarczaj�cy informacji na temat serwera
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_info) = %{version}-%{release}
Obsoletes:	apache-mod_info < 2.0.0

%description mod_info
This package contains mod_info module. It provides a comprehensive
overview of the server configuration including all installed modules
and directives in the configuration files.

%description mod_info -l pl
Modu� dostarczaj�cy wyczerpuj�cych informacji o konfiguracji serwera,
w tym zainstalowanych modu�ach oraz dyrektywach w plikach
konfiguracyjnych.

%package mod_log_agent
Summary:	Logging of User Agents
Summary(pl):	Logowanie nazw klient�w (User Agent)
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_log_agent) = %{version}-%{release}

%description mod_log_agent
This module is provided strictly for compatibility with NCSA httpd,
and is deprecated. We recommend you use mod_log_config instead.

%description mod_log_agent -l pl
Ten modu� jest dostarczony wy��cznie dla kompatybilno�ci z NCSA httpd
i jest niezalecany. Zamiast niego lepiej u�ywa� mod_log_config.

%package mod_log_config
Summary:	User-configurable logging replacement for mod_log_common
Summary(pl):	Konfigurowalny loguj�cy zamiennik dla mod_log_common
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

%description mod_log_config -l pl
Ten modu� umo�liwia elastyczne logowanie ��da� klient�w. Logi s�
zapisywane w konfigurowalnym formacie i mog� by� zapisywane
bezpo�rednio do pliku lub przekazywane do zewn�trznego programu.
Dost�pne jest logowanie warunkowe polegaj�ce na w��czeniu lub
wy��czeniu poszczeg�lnych ��da� z logowania na podstawie
charakterystyki ��dania.

Ten modu� udost�pnia trzy dyrektywy: TransferLog tworz�cy plik logu,
LogFormat ustawiaj�cy w�asny format logowania i CustomLog okre�laj�cy
plik logu i format jednocze�nie. Dyrektywy TransferLog i CustomLog
mog� by� u�ywane wielokrotnie w ka�dym serwerze powoduj�c logowanie
ka�dego ��dania do wielu plik�w.

%package mod_log_forensic
Summary:	Apache module for forensic logging of the requests
Summary:	Modu� Apache'a do logowania ��da� w celu p�niejszej analizy
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_log_forensic) = %{version}-%{release}
Obsoletes:	apache-mod_log_forensic < 2.0.0

%description mod_log_forensic
This module provides for forensic logging of client requests. Logging
is done before and after processing a request.

%description mod_log_forensic -l pl
Ten modu� pozwala na logowanie ��da� w celu p�niejszej analizy.
Logowanie jest wykonywane przed i po przetworzeniu ��dania.

%package mod_log_referer
Summary:	User-configurable logging replacement for mod_log_common
Summary(pl):	Konfigurowalny loguj�cy zamiennik dla mod_log_common
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_log_referer) = %{version}-%{release}

%description mod_log_referer
This module is provided strictly for compatibility with NCSA httpd,
and is deprecated. We recommend you use mod_log_config instead.

%description mod_log_referer -l pl
Ten modu� jest dostarczony wy��cznie dla kompatybilno�ci z NCSA httpd
i jest niezalecany. Zamiast niego lepiej u�ywa� mod_log_config.

%package mod_mime
Summary:	Determining document types using file extensions
Summary(pl):	Okre�lanie typ�w dokument�w przy u�yciu rozszerze� plik�w
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_mime) = %{version}-%{release}

%description mod_mime
This module is used to determine various bits of "meta information"
about documents. This information relates to the content of the
document and is returned to the browser or used in content-negotiation
within the server. In addition, a "handler" can be set for a document,
which determines how the document will be processed within the server.

%description mod_mime -l pl
Ten modu� s�u�y do okre�lania r�nych fragment�w metainformacji
dotycz�cych dokument�w. Informacja ta odnoszi si� do zawarto�ci
dokumentu i jest zwracana przegl�darce albo u�ywana przy negocjacji
tre�ci wewn�trz serwera. Ponadto dla dokumentu mo�na ustawi� procedur�
obs�ugi, okre�laj�c� w jaki spos�b dokument b�dzie przetwarzany
wewn�trz serwera.

%package mod_mime_magic
Summary:	Determining document types using "magic numbers"
Summary(pl):	Okre�lanie typ�w dokument�w przy u�yciu "liczb magicznych"
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

%description mod_mime_magic -l pl
Ten modu� okre�la typ MIME plik�w w ten sam spos�b, co polecenie
file(1): sprawdza pierwsze kilka bajt�w pliku. Ma by� "drug� lini�
obrony" dla przypadk�w, kt�rych nie mo�e rozwi�za� mod_mime. Aby mie�
pewno��, �e mod_mime dostaje pierwsz� pr�b� okre�lenia typu MIME,
nale�y upewni� si�, �e mod_mime_magic jest umieszczony w konfiguracji
przed mod_mime.

Ten modu� wywodzi si� z wolnodost�pnej wersji polecenia file(1) dla
uniks�w, u�ywaj�cej "liczb magicznych" i innych podpowiedzi z
zawarto�ci plik�w w celu rozpoznania zawarto�ci. Modu� jest aktywny
tylko je�li plik magic zosta� okre�lony dyrektyw� MimeMagicFile.

%package mod_mmap_static
Summary:	Apache module for mmap()ing statically configured list files
Summary(pl):	Modu� s�u��cy do mmap()owania plik�w
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_mmap_static) = %{version}-%{release}
Obsoletes:	apache-mod_mmap_static < 2.0.0

%description mod_mmap_static
This package contains mod_mmap_static module. It provides mmap()ing of
a statically configured list of frequently requested but not changed
files.

%description mod_mmap_static -l pl
Modu� umo�liwia mmap()owanie statycznie skonfigurowanych plik�w
(cz�sto u�ywanych, ale nie ulegaj�cych zmianom).

%package mod_negotiation
Summary:	Content negotiation
Summary(pl):	Negocjacja tre�ci
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

%description mod_negotiation -l pl
Negocjacja tre�ci, albo bardziej precyzyjnie wyb�r tre�ci, to wyb�r
dokumentu najbardziej pasuj�cego do mo�liwo�ci klienta spo�r�d r�nych
dost�pnych dokument�w. S� dwie r�ne implementacje.
- Odwzorowanie typ�w (plik z obs�ug� type-map) wypisuj�cy explicite
  pliki zawieraj�ce warianty.
- Wyszukiwanie MultiViews (w��czane opcj� MultiViews, kiedy serwer
  dopasowuje implicite wzorzec nazwy pliku i wybiera spo�r�d wynik�w).

%package mod_proxy
Summary:	Apache module with Web proxy
Summary(pl):	Modu� dodaj�cy obs�ug� serwera proxy
Group:		Networking/Daemons
Requires(triggerpostun):	sed >= 4.0
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_proxy) = %{version}-%{release}
Obsoletes:	apache-mod_proxy < 2.0.0

%description mod_proxy
This package contains module with implementation a proxy/cache for
Apache. It implements proxying capability for FTP, CONNECT (for SSL),
HTTP/0.9, and HTTP/1.0. The module can be configured to connect to
other proxy modules for these and other protocols.

%description mod_proxy -l pl
Modu� zawiera implementacj� serwera proxy/cache dla Apache.
Iplementacja zawiera obs�ug� FTP, CONNECT (dla SSL), HTTP/0.9 i
HTTP/1.0. Ten modu� mo�e by� skonfigurowany tak, aby ��czy� si� z
innymi modu�ami proxy dla tych i innych protoko��w.

%package mod_rewrite
Summary:	Apache module with rule-based engine for rewrite requested URLs on the fly
Summary(pl):	Modu� do ,,przepisywania'' adres�w URL w locie
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_rewrite) = %{version}-%{release}
Obsoletes:	apache-mod_rewrite < 2.0.0

%description mod_rewrite
This package contains It provides a rule-based rewriting engine to
rewrite requested URLs on the fly.

%description mod_rewrite -l pl
Modu� oferuj�cy mo�liwo�� ,,przepisywania'' adres�w URL w locie.

%package mod_setenvif
Summary:	Set environment variables based on client information
Summary(pl):	Ustawianie zmiennych �rodowiskowych w oparciu o informacje o kliencie
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_setenvif) = %{version}-%{release}

%description mod_setenvif
The mod_setenvif module allows you to set environment variables
according to whether different aspects of the request match regular
expressions you specify. These environment variables can be used by
other parts of the server to make decisions about actions to be taken.

%description mod_setenvif -l pl
Modu� mod_setenvif pozwala na ustawianie zmiennych �rodowiskowych w
zale�no�ci od r�nych aspekt�w ��dania pasuj�cych do podanych wyra�e�
regularnych. Te zmienne �rodowiskowe mog� by� u�ywane przez inne
cz�ci serwera do podejmowania decyzji o podejmowanych akcjach.

%package mod_speling
Summary:	Automatically correct minor typos in URLs
Summary(pl):	Automatyczne poprawianie pomniejszych liter�wek w URL-ach
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

%description mod_speling -l pl
Czasami ��dania dokument�w nie mog� by� wykonane przez sam serwer
Apache, poniewa� ��danie zosta�o napisane z b��dem w znakach lub
wielko�ci liter. Ten modu� pr�buje rozwi�za� ten problem pr�buj�c
znale�� pasuj�cy dokument, nawet je�li inne modu�y si� podda�y. Dzia�a
on poprzez por�wnywanie nazwy ka�dego dokumentu w ��danym katalogu z
��dan� nazw� dokumentu bez zwracania uwagi na wielko�� liter i
pozwalaj�c na jeden b��d (dodany, pomini�ty, przestawiony lub z�y
znak). Tworzona jest lista dla wszystkich nazw dokument�w pasuj�cych
dla tej strategii.

%package mod_status
Summary:	Server status report module for apache
Summary(pl):	Modu� dostarczaj�cy informacje statystyczne o serwerze
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

%description mod_status -l pl
Modu� pozwala administratorowi na przegl�danie statystyk dotycz�cych
pracy serwera apache (w postaci strony HTML). Strona ta mo�e si�
automatycznie od�wie�a� (o ile jest to obs�ugiwane przez
przegl�dark�).

%package mod_unique_id
Summary:	Apache module which provides a magic token for each request
Summary(pl):	Modu� nadaj�cy ka�demu ��daniu unikalny token
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

%description mod_unique_id -l pl
Modu� nadaje przy ka�dym ��daniu token unikalny w ramach wszystkich
��da�, nawet w ramach poprawnie skonfigurowanego klastra z wielu
maszyn. Modu� ustawia przy ka�dym ��daniu zmienn� �rodowiskow�
UNIQUE_ID.

%package mod_userdir
Summary:	User home directories
Summary(pl):	Katalogi domowe u�ytkownik�w
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_userdir) = %{version}-%{release}

%description mod_userdir
This module provides for user-specific directories.

%description mod_userdir -l pl
Ten modu� dostarcza obs�ug� katalog�w specyficznych dla uzytkownika.

%package mod_usertrack
Summary:	Apache module for user tracking using cookies
Summary(pl):	Modu� s�u��cy do �ledzenia u�ytkownik�w przy u�yciu ciasteczek
Group:		Networking/Daemons
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_usertrack) = %{version}-%{release}
Obsoletes:	apache-mod_usertrack < 2.0.0

%description mod_usertrack
This package contains the user tracking module which did its own
logging using CookieLog directory. This module allow multiple log
files.

%description mod_usertrack -l pl
Modu� pozwalaj�cy na �ledzenie u�ytkownik�w przy pomocy ciasteczek.
Modu� ma w�asne logowanie przy u�yciu katalogu CookieLog; pozwala na
wiele plik�w log�w.

%package mod_vhost_alias
Summary:	Apache module for dynamically configured mass virtual hosting
Summary(pl):	Modu� dodaj�cy obs�ug� host�w wirtualnych
Group:		Networking/Daemons
Requires(triggerpostun):	sed >= 4.0
Requires:	%{name}(EAPI) = %{version}-%{release}
Provides:	apache(mod_vhost_alias) = %{version}-%{release}
Obsoletes:	apache-mod_vhost_alias < 2.0.0

%description mod_vhost_alias
This package contains the mod_vhost_alias. It provides support for
dynamically configured mass virtual hosting.

%description mod_vhost_alias -l pl
Modu� umo�liwia na dynamiczne konfigurowanie masowej ilo�ci serwer�w
wirtualnych.

%package -n htpasswd-%{name}
Summary:	Apache 1.x htpasswd utility
Summary(pl):	Narz�dzie htpasswd z Apache'a 1.x
Group:		Networking/Utilities
Provides:	htpasswd
Obsoletes:	htpasswd

%description -n htpasswd-%{name}
htpasswd is used to create and update the flat-files used to store
usernames and password for basic authentication of HTTP users. This
package contains htpasswd from Apache 1.x; this version supports
plaintext passwords and CRYPT (default), MD5 and SHA1 encryptions.

%description -n htpasswd-%{name} -l pl
htpasswd s�u�y do tworzenia i uaktualniania p�askich plik�w s�u��cych
do przechowywania nazw u�ytkownik�w i hase� do uwierzytelnienia basic
u�ytkownik�w HTTP. Ten pakiet zawiera htpasswd z Apache'a 1.x; ta
wersja obs�uguje has�a zapisane czystym tekstem oraz zakodowane
algorytmami CRYPT (domy�lnym), MD5 i SHA1.

%prep
%setup -q -n apache_%{version} -a3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p0
%patch6 -p1
%patch7 -p1
%{?with_ipv6:%patch8 -p1}
%patch9 -p1
%patch10 -p1
%patch11 -p1
%{?with_rewrite_ldap:%patch12 -p1}
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%{!?with_ipv6:%patch18 -p1}
%patch19 -p1
%patch20 -p1
%patch21 -p1

%build
OPTIM="%{rpmcflags} -DHARD_SERVER_LIMIT=2048" \
./configure \
	--prefix=%{_sysconfdir} \
	--exec-prefix=%{_libexecdir} \
	--bindir=%{_bindir} \
	--sbindir=%{_sbindir} \
	--sysconfdir=%{_sysconfdir} \
	--datadir=%{_datadir} \
	--includedir=%{_includedir} \
	--libexecdir=%{_sysconfdir}/modules \
	--localstatedir=/var \
	--mandir=%{_mandir} \
	--manualdir=%{manualdir} \
	--runtimedir=/var/run \
	--logfiledir=/var/log/apache \
	--with-layout=PLD \
	--without-confadjust \
	--enable-module=all \
	--enable-module=auth_digest \
	--enable-shared=max \
	--proxycachedir=/var/cache/apache \
	--with-perl=%{_bindir}/perl \
	--enable-suexec \
	--suexec-caller=http \
	--suexec-uidmin=500 \
	--suexec-gidmin=500 \
	--suexec-docroot=%{_datadir} \
	--disable-rule=WANTHSREGEX \
	--enable-rule=EAPI \
	--target=apache \
	%{?with_ipv6:--enable-rule=INET6}

%{__make} \
	LIBS1="-lm -lcrypt -lmm -ldl"

rm -f src/modules/standard/mod_auth_db.so
%{__make} -C src/modules/standard mod_auth_db.so \
	LIBS_SHLIB="-ldb"

rm -f src/modules/standard/mod_rewrite.so
%{__make} -C src/modules/standard mod_rewrite.so \
	LIBS_SHLIB="-ldb %{?with_rewrite_ldap:-lldap -llber}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{logrotate.d,rc.d/init.d,sysconfig,monit} \
	$RPM_BUILD_ROOT%{_datadir}/errordocs \
	$RPM_BUILD_ROOT%{_sysconfdir}/conf.d \
	$RPM_BUILD_ROOT%{_libexecdir} \
	$RPM_BUILD_ROOT/var/{log/{apache,archiv/apache},run/apache}

%{__make} -j1 install-quiet \
	root=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/apache1
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/apache
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/apache
bzip2 -dc %{SOURCE5} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

touch $RPM_BUILD_ROOT/var/log/apache/{access,error,agent,referer}_log

install errordocs/* $RPM_BUILD_ROOT%{_datadir}/errordocs

mv $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf conf/apache.conf.dist
install %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf

CFG="$RPM_BUILD_ROOT%{_sysconfdir}/conf.d"

echo "LoadModule access_module      modules/mod_access.so" > $CFG/01_mod_access.conf
echo "LoadModule alias_module       modules/mod_alias.so" > $CFG/02_mod_alias.conf
echo "LoadModule asis_module        modules/mod_asis.so" > $CFG/03_mod_asis.conf
install %{SOURCE21} $CFG/04_mod_cern_meta.conf
echo "LoadModule cgi_module         modules/mod_cgi.so" > $CFG/05_mod_cgi.conf
echo "LoadModule env_module         modules/mod_env.so" > $CFG/06_mod_env.conf
echo "LoadModule include_module     modules/mod_include.so" > $CFG/07_mod_include.conf
echo "LoadModule log_agent_module   modules/mod_log_agent.so" > $CFG/08_mod_log_agent.conf
install %{SOURCE14} $CFG/09_mod_log_config.conf
echo "LoadModule log_referer_module modules/mod_log_referer.so" > $CFG/10_mod_log_referer.conf
install %{SOURCE16}	$CFG/11_mod_mime_magic.conf
install %{SOURCE19}	$CFG/12_mod_mime.conf
install %{SOURCE18} $CFG/13_mod_negotiation.conf
install %{SOURCE22}	$CFG/14_mod_setenvif.conf
echo "LoadModule speling_module     modules/mod_speling.so" > $CFG/15_mod_speling.conf
install %{SOURCE15}	$CFG/16_mod_userdir.conf

install %{SOURCE8}	$CFG/20_common.conf

install %{SOURCE23}	$CFG/20_mod_vhost_alias.conf
install %{SOURCE9}	$CFG/25_mod_status.conf
install %{SOURCE10}	$CFG/30_mod_proxy.conf
install %{SOURCE20}	$CFG/50_mod_actions.conf
echo "LoadModule auth_module	modules/mod_auth.so" > $CFG/51_mod_auth.conf
echo "LoadModule auth_anon_module	modules/mod_auth_anon.so" > $CFG/52_mod_auth_anon.conf
echo "LoadModule auth_db_module	modules/mod_auth_db.so" > $CFG/53_mod_auth_db.conf
echo "LoadModule auth_digest_module	modules/mod_auth_digest.so" > $CFG/54_mod_auth_digest.conf
install %{SOURCE11}	$CFG/57_mod_autoindex.conf
install %{SOURCE12}	$CFG/59_mod_dir.conf
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
install %{SOURCE13} $CFG/77_mod_info.conf
install %{SOURCE24}	$CFG/80_errordocs.conf
install %{SOURCE17}	$CFG/80_mod_alias.conf

install %{SOURCE6} $RPM_BUILD_ROOT/etc/monit

ln -sf index.html.en $RPM_BUILD_ROOT%{_datadir}/html/index.html

mv $RPM_BUILD_ROOT%{_sbindir}/apxs $RPM_BUILD_ROOT%{apxs}
mv $RPM_BUILD_ROOT%{_mandir}/man8/apxs.8 $RPM_BUILD_ROOT%{_mandir}/man8/apxs1.8

perl -p -i -e 's/^if ...O ne "MSWin32"./if (0)/' $RPM_BUILD_ROOT%{apxs}

mv $RPM_BUILD_ROOT%{_sysconfdir}/modules/* $RPM_BUILD_ROOT%{_libexecdir}
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/modules
ln -s %{_libexecdir} $RPM_BUILD_ROOT%{_sysconfdir}/modules
ln -s /var/log/apache $RPM_BUILD_ROOT%{_sysconfdir}/logs

ln -sf %{_bindir}/htpasswd $RPM_BUILD_ROOT%{_sbindir}

# Not packaged.
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/*.default
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/{access,srm}.conf
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/mime.types
rm -f $RPM_BUILD_ROOT%{_libexecdir}/*.exp
rm -f $RPM_BUILD_ROOT%{_libexecdir}/mod_{auth_dbm,example}.so
rm -f $RPM_BUILD_ROOT%{_datadir}/icons{,/small}/README*
rm -f $RPM_BUILD_ROOT%{_mandir}/README*

# Not for our os or for older apache
rm -f $RPM_BUILD_ROOT/usr/share/apache1-manual/{cygwin,ebcdic,install-tpf,man-template}.html \
rm -f $RPM_BUILD_ROOT/usr/share/apache1-manual/mod/mod_{auth_dbm,browser,dld,example,isapi,log_common}.html \
rm -f $RPM_BUILD_ROOT/usr/share/apache1-manual/{mpeix,netware,new_features_1_[0-2],readme-tpf,suexec_1_2,unixware,vhosts/details_1_2}.html \
rm -f $RPM_BUILD_ROOT/usr/share/apache1-manual/{win_{compiling,service}.html*,windows.html*}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 51 -r -f http
%useradd -u 51 -r -d %{httpdir} -s /bin/false -c "HTTP User" -g http http

if [ "`getent passwd http | cut -d: -f6`" = "/home/httpd" ]; then
	/usr/sbin/usermod -d %{httpdir} http
fi

%post
/sbin/chkconfig --add apache
umask 137
touch /var/log/apache/{access,error,agent,referer}_log

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/apache ]; then
		/etc/rc.d/init.d/apache stop 1>&2
	fi
	/sbin/chkconfig --del apache
fi

%postun
if [ "$1" = "0" ]; then
	%userremove http
	%groupremove http
fi

%triggerpostun -- apache < 2.0.0
%groupadd -g 51 -r -f http
%useradd -u 51 -r -d %{httpdir} -s /bin/false -c "HTTP User" -g http http
/sbin/chkconfig --add apache

%triggerpostun -- apache1 < 1.3.33-1.85
# upgrading from older version
if [ "$1" = "2" ]; then
	sed -i -e '
		# get apxs over confusion of changed ServerRoot
		s,^\(LoadModule .*\) lib/apache1/,\1 modules/,

		# update ServerRoot
		s,^ServerRoot.*,ServerRoot "/etc/apache",
	' /etc/apache/apache.conf
fi

%triggerpostun -- %{name} <= 1.3.31-5
%banner %{name} -e -a <<EOF
WARNING!!!
 Since 1.3.31-5 version autoindex module has been separated to package %{name}-mod_autoindex
 If you need previous functionality please run:
poldek -Uv %{name}-mod_autoindex

EOF

%triggerpostun -- %{name} < 1.3.33-3.4
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

%triggerpostun -- %{name} < 1.3.33-6.7
# update /etc/sysconfig/apache1 -> apache rename
if [ -f /etc/sysconfig/apache1.rpmsave ]; then
	cp -f /etc/sysconfig/apache{,.rpmnew}
	mv -f /etc/sysconfig/apache{1.rpmsave,}
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

%posttrans
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
exit 0

# macro called at module post scriptlet
%define	module_post \
if [ "$1" = "1" ]; then \
	%service -q apache restart "Apache HTTP daemon" \
fi

# macro called at module postun scriptlet
%define	module_postun \
if [ "$1" = "0" ]; then \
	%service -q apache restart "Apache HTTP daemon" \
fi

%post errordocs
if [ "$1" = "1" ]; then
	%service -q apache reload "Apache HTTP daemon"
fi

%postun errordocs
if [ "$1" = "0" ]; then
	%service -q apache reload "Apache HTTP daemon"
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

%files
%defattr(644,root,root,755)
%doc ABOUT_APACHE src/CHANGES README
%doc conf/mime.types conf/apache.conf.dist

%attr(754,root,root) /etc/rc.d/init.d/apache

%attr(750,root,root) %dir %{_sysconfdir}
%{_sysconfdir}/modules
%{_sysconfdir}/logs
%attr(750,root,root) %dir %{_sysconfdir}/conf.d
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_common.conf

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/apache
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/*
%attr(750,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/monit/*.monitrc

%dir %{_libexecdir}

%attr(755,root,root) %{_bindir}/checkgid
%attr(755,root,root) %{_bindir}/htdigest

%attr(755,root,root) %{_sbindir}/apache

%dir %attr(1773,root,http) /var/run/apache

%{_mandir}/man8/apache.8*

%attr(2750,root,logs) %dir /var/log/apache
%attr(2750,root,logs) %dir /var/log/archiv/apache
%attr(640,root,logs) %ghost /var/log/apache/*

%dir %{_datadir}
%attr(755,root,root) %dir %{_datadir}/html

%dir %{_datadir}/icons
%{_datadir}/icons/*.gif
%{_datadir}/icons/*.png
%dir %{_datadir}/icons/small
%{_datadir}/icons/small/*.gif
%{_datadir}/icons/small/*.png
%attr(755,root,root) %{_datadir}/cgi-bin

%files apxs
%defattr(644,root,root,755)
%attr(755,root,root) %{apxs}
%{_mandir}/man8/apxs1.8*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/ab
%attr(755,root,root) %{_sbindir}/apachectl
%attr(755,root,root) %{_sbindir}/logresolve
%attr(755,root,root) %{_sbindir}/rotatelogs
%{_mandir}/man1/htdigest.1*
%{_mandir}/man8/ab*
%{_mandir}/man8/apachectl*
%{_mandir}/man8/[l-z]*
%lang(hu) %{_mandir}/hu/man8/*
%lang(ko) %{_mandir}/ko/man8/*
%lang(pl) %{_mandir}/pl/man8/*

%files index
%defattr(644,root,root,755)
%config(noreplace,missingok) %{_datadir}/html/index.html
# NOTE: html extensions are not the same as (g)libc locale names
%lang(ca) %{_datadir}/html/index.html.ca
%lang(cs) %{_datadir}/html/index.html.cz
%lang(de) %{_datadir}/html/index.html.de
%lang(da) %{_datadir}/html/index.html.dk
%lang(et) %{_datadir}/html/index.html.ee
%lang(el) %{_datadir}/html/index.html.el
%{_datadir}/html/index.html.en
%lang(es) %{_datadir}/html/index.html.es
%lang(fr) %{_datadir}/html/index.html.fr
%lang(he) %{_datadir}/html/index.html.he.iso8859-8
%lang(hu) %{_datadir}/html/index.html.hu
%lang(it) %{_datadir}/html/index.html.it
%lang(ja) %{_datadir}/html/index.html.ja.jis
%lang(ko) %{_datadir}/html/index.html.kr.iso-kr
%lang(de_LU) %{_datadir}/html/index.html.lb.utf8
%lang(nl) %{_datadir}/html/index.html.nl
%lang(nn) %{_datadir}/html/index.html.nn
%lang(nb) %{_datadir}/html/index.html.no
%lang(pl) %{_datadir}/html/index.html.po.iso-pl
%lang(pt) %{_datadir}/html/index.html.pt
%lang(pt_BR) %{_datadir}/html/index.html.pt-br
%lang(ru) %{_datadir}/html/index.html.ru.cp-1251
%lang(ru) %{_datadir}/html/index.html.ru.cp866
%lang(ru) %{_datadir}/html/index.html.ru.iso-ru
%lang(ru) %{_datadir}/html/index.html.ru.koi8-r
%lang(ru) %{_datadir}/html/index.html.ru.ucs2
%lang(ru) %{_datadir}/html/index.html.ru.ucs4
%lang(ru) %{_datadir}/html/index.html.ru.utf8
%lang(sv) %{_datadir}/html/index.html.se
%lang(zh_TW) %{_datadir}/html/index.html.zh-tw.big5
%{_datadir}/html/*.gif

%files doc
%defattr(644,root,root,755)
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
%{_datadir}/errordocs

%files suexec
%defattr(644,root,root,755)
%attr(4755,root,root) %{_sbindir}/suexec

%files devel
%defattr(644,root,root,755)
%{_includedir}

%files -n htpasswd-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/htpasswd
%{_sbindir}/htpasswd
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
