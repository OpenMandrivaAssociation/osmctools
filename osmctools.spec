Summary:	Tools to manipulate OpenStreetMap files
Name:		osmctools
Version:	0.9
Release:	1
# Debian man pages are GPLv2+
License:	AGPLv3 and GPLv2+
Group:		File tools
URL:		https://gitlab.com/osm-c-tools/osmctools
Source0:	https://gitlab.com/osm-c-tools/osmctools/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Man pages from Debian
Source1:	osmconvert.1
Source2:	osmfilter.1
Source3:	osmupdate.1
BuildRequires:	pkgconfig(zlib)
Requires:	rsync
Requires:	wget

%description
Small collection of basic OpenStreetMap tools, include converter, filter and
updater files.

Programs include:
* osmconvert - Converter of OSM files
* osmfilter - The experimental OSM filters data
* osmupdate - Update OSM files.

%prep
%autosetup

%build
autoreconf -fvi
%configure
%make_build

%install
%make_install

# Install man pages
install -d %{buildroot}%{_mandir}/man1/
for i in %{SOURCE1} %{SOURCE2} %{SOURCE3}; do
  install -p -m 0644 ${i} %{buildroot}%{_mandir}/man1/
done

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/*
%doc %{_mandir}/man1/*.1*
