%define module isort

Name:		python-isort
Version:	8.0.0
Release:	1
Summary:	A Python utility / library to sort imports
License:	MIT
Group:		Development/Python
URL:		https://github.com/timothycrosley/isort
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(hatchling)

%description 
A Python utility / library to sort imports

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%{_bindir}/%{module}
%{_bindir}/%{module}-identify-imports
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
