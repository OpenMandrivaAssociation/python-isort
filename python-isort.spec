%define module	isort
  
Summary:	A Python utility / library to sort imports
Name:		python-isort
Version:	5.6.4
Release:	1
Group:		Development/Python
License:	Python
Url:		https://github.com/timothycrosley/isort
Source0:	https://files.pythonhosted.org/packages/7b/b5/19e828baf02d3e441cd287a3f3cc172bec2d1210c0210294debeddbd3550/%{module}-%{version}.tar.gz
BuildArch:	noarch 
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
 
%description 
A Python utility / library to sort imports

%prep
%setup -qn %{module}-%{version}
  
%build
%__python setup.py build

%install 
%__python setup.py install --root=%{buildroot} --record=FILE_LIST

%files
%{_bindir}/*
%{py_sitedir}/isort
%{py_sitedir}/isort*.egg-info
