%define module	isort
  
Summary:	A Python utility / library to sort imports
Name:		python-isort
Version:	5.10.1
Release:	1
Group:		Development/Python
License:	Python
Url:		https://github.com/timothycrosley/isort
Source0:	https://files.pythonhosted.org/packages/ab/e9/964cb0b2eedd80c92f5172f1f8ae0443781a9d461c1372a3ce5762489593/isort-5.10.1.tar.gz
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
