Name:           clash_for_windows
Version:        0.19.20
Release:        1%{?dist}
Summary:        A Windows/macOS GUI based on Clash 
License:        UNLICENSED
Source0:        %{NAME}.tar.gz
BuildArch:      x86_64


%description
A Windows/macOS GUI based on Clash 

%prep
%setup -q -n %{NAME}

%install
# make necessary directories
mkdir -p \
    %{buildroot}/opt/%{NAME} \
    %{buildroot}/usr/share/pixmaps/ \
    %{buildroot}/usr/share/applications/
pwd
pushd src
find . -type f -not \( -name "cfw" -or -name "clash-linux" -or -name "clash-core-service" -or -name "chrome-sandbox" -or -name "*.sh" \) \
    -exec install -Dm 644 {} "%{buildroot}/opt/%{NAME}"/{} \;
echo "packaging executable files as 755"
find . -type f \( -name "cfw" -or -name "clash-linux" -or -name "clash-core-service" -or -name "chrome-sandbox" -or -name "*.sh" \) \
   -exec install -Dm 755 {} "%{buildroot}/opt/%{NAME}"/{} \;
popd
install -Dm 644 clash.png %{buildroot}/usr/share/pixmaps/clash.png
install -Dm 644 clash-for-windows.desktop %{buildroot}/usr/share/applications/clash-for-windows.desktop

%files
/opt/%{NAME}
/usr/share/pixmaps/*
/usr/share/applications/*
