Name:           canokeys-udev
Version:        1.0.0
Release:        1%{?dist}
Summary:        Canokeys udev rules 
License:        UNLICENSED
Source0:        %{NAME}.tar.gz
BuildArch:      noarch


%description
In order to allow non-root user use the key

%prep
%setup -q -n %{NAME}

%install
mkdir -p \
    %{buildroot}/etc/udev/rules.d/
install -Dm 644 69-canokeys.rules %{buildroot}/etc/udev/rules.d/69-canokeys.rules

%files
/etc/udev/rules.d/69-canokeys.rules
