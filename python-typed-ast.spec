%define module	typed_ast
  
Summary:	Modified fork of CPython's ast module that parses `#type:` comments
Name:		python-typed-ast
Version:	1.5.1
Release:	1
Group:		Development/Python
License:	Python
Url:		https://github.com/python/typed_ast
Source0:	https://github.com/python/typed_ast/archive/%{module}-%{version}.tar.gz
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
 
%description 
Modified fork of CPython's ast module that parses `#type:` comments

%prep
%autosetup -p1 -n %{module}-%{version}
  
%build
%__python setup.py build

%install 
%__python setup.py install --root=%{buildroot} --record=FILE_LIST

%files
%{py_platsitedir}/typed_ast
%{py_platsitedir}/typed_ast*.egg-info
