#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-cli-core
Version  : 2.5.1
Release  : 1
URL      : https://files.pythonhosted.org/packages/66/cc/a01f7837274ef9be79b2c4e1ba03a072bc7f3885a7567e1d9e68204e0ea1/azure-cli-core-2.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/66/cc/a01f7837274ef9be79b2c4e1ba03a072bc7f3885a7567e1d9e68204e0ea1/azure-cli-core-2.5.1.tar.gz
Summary  : Microsoft Azure Command-Line Tools Core Module
Group    : Development/Tools
License  : MIT
Requires: azure-cli-core-python = %{version}-%{release}
Requires: azure-cli-core-python3 = %{version}-%{release}
Requires: PyJWT
Requires: colorama
Requires: humanfriendly
Requires: jmespath
Requires: msrest
Requires: msrestazure
Requires: paramiko
Requires: pkginfo
Requires: pyasn1
BuildRequires : PyJWT
BuildRequires : buildreq-distutils3
BuildRequires : colorama
BuildRequires : humanfriendly
BuildRequires : jmespath
BuildRequires : msrest
BuildRequires : msrestazure
BuildRequires : paramiko
BuildRequires : pkginfo
BuildRequires : pyasn1

%description
==================================

%package python
Summary: python components for the azure-cli-core package.
Group: Default
Requires: azure-cli-core-python3 = %{version}-%{release}

%description python
python components for the azure-cli-core package.


%package python3
Summary: python3 components for the azure-cli-core package.
Group: Default
Requires: python3-core
Provides: pypi(azure_cli_core)
Requires: pypi(adal)
Requires: pypi(argcomplete)
Requires: pypi(azure_cli_nspkg)
Requires: pypi(azure_cli_telemetry)
Requires: pypi(azure_mgmt_core)
Requires: pypi(azure_mgmt_resource)
Requires: pypi(colorama)
Requires: pypi(humanfriendly)
Requires: pypi(jmespath)
Requires: pypi(knack)
Requires: pypi(msal)
Requires: pypi(msal_extensions)
Requires: pypi(msrest)
Requires: pypi(msrestazure)
Requires: pypi(paramiko)
Requires: pypi(pkginfo)
Requires: pypi(pyjwt)
Requires: pypi(pyopenssl)
Requires: pypi(requests)
Requires: pypi(six)

%description python3
python3 components for the azure-cli-core package.


%prep
%setup -q -n azure-cli-core-2.5.1
cd %{_builddir}/azure-cli-core-2.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588624046
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
