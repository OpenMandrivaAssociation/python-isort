%define module	isort
  
Summary:	A Python utility / library to sort imports
Name:		python-isort
Version:	7.0.0
Release:	1
Group:		Development/Python
License:	Python
Url:		https://github.com/timothycrosley/isort
Source0:	https://pypi.python.org/packages/source/i/isort/isort-%{version}.tar.gz
BuildArch:	noarch 
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	pkgconfig(python3)
BuildSystem:    python
 
%description 
A Python utility / library to sort imports


%files
%{_bindir}/*
%{py_sitedir}/isort
%{py_sitedir}/isort*.egg-info
