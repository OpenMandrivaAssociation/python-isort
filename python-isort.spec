%define module	isort
  
Summary:	A Python utility / library to sort imports
Name:		python-isort
Version:	5.7.0
Release:	1
Group:		Development/Python
License:	Python
Url:		https://github.com/timothycrosley/isort
Source0:	https://files.pythonhosted.org/packages/a2/f7/f50fc9555dc0fe2dc1e7f69d93f71961d052857c296cad0fb6d275b20008/isort-5.7.0.tar.gz
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
