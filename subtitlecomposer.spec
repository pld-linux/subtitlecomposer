Summary:	subtitlecomposer - a text subtitles editor
Summary(pl.UTF-8):	subtitlecomposer - edytor napisów tekstowych
Name:		subtitlecomposer
Version:	0.4.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/subcomposer/%{name}-%{version}.tar.bz2
# Source0-md5:	453faf628f25e97bde270759f75afd84
URL:		http://kde-apps.org/content/show.php?content=69822
BuildRequires:	automake
BuildRequires:	gstreamer-plugins-base-devel >= 0.10
BuildRequires:	kdelibs-devel
BuildRequires:	pkgconfig
BuildRequires:	xine-lib-devel
BuildRequires:	rpmbuild(macros) >= 1.129
Suggests:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Subtitle Composer is a KDE 3 text subtitle editor with
gstreamer/mplayer preview.

%description -l pl.UTF.8
Subtitle Composer to edytor tekstowych napisów do filmów dla KDE 3 z
podglądem przy użyciu gstreamera/mplayera.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/%{name}
%{_datadir}/config/subtitlecomposerrc
%{_datadir}/mimelnk/subtitle
%{_desktopdir}/kde/subtitlecomposer.desktop
%{_iconsdir}/hicolor/*/apps/*.png
