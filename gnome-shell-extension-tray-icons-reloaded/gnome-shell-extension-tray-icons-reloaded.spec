Name:           gnome-shell-extension-tray-icons-reloaded
Version:        25
Release:        1%{?dist}
Summary:        GNOME Shell extension which bring back Tray Icons to top panel, with additional features
License:        GPLv3
Source0:        %{NAME}.tar.gz
BuildArch:      noarch

%description
GNOME Shell extension which bring back Tray Icons to top panel, with additional features

%prep
%setup -q -n %{NAME}

%install
uuid=$(grep -Po '(?<="uuid": ")[^"]*' src/metadata.json)
mkdir -p \
    %{buildroot}/usr/share/gnome-shell/extensions/$uuid
cp -rf src/* "%{buildroot}/usr/share/gnome-shell/extensions/$uuid"

%files
/usr/share/gnome-shell/extensions/*
