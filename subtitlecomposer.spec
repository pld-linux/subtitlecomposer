Summary:	subtitlecomposer - a text subtitles editor
Summary(pl.UTF-8):	subtitlecomposer - edytor napisów tekstowych
Name:		subtitlecomposer
Version:	0.3
Release:	0.9
License:	GPL
Group:		X11/Applications
#Source0:	http://dl.sourceforge.net/subtitlecomposer/%{name}-%{version}.tar.bz2
Source0:	http://heanet.dl.sourceforge.net/sourceforge/subcomposer/subtitlecomposer-0.3.tar.bz2
# Source0-md5:	bca75b9c6679a6ed9cc2e802adfabdc5
URL:		http://kde-apps.org/content/show.php?content=69822
BuildRequires:	automake
BuildRequires:	gstreamer-devel
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
Suggests:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Subtitle Composer is a KDE3 text subtitle editor with
gstreamer/mplayer preview.

%description -l pl.UTF.8
Subtitle Composer to edytor tekstowych napisów z podglądem
przy użyciu gstreamera/mplayera.

%prep
%setup -q -n %{name}

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
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/config/subtitlecomposerrc
%{_datadir}/mimelnk/subtitle/
%{_desktopdir}/kde/subtitlecomposer.desktop
