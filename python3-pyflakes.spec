#
# Conditional build:
%bcond_without	tests	# test target

%define 	module	pyflakes
Summary:	Passive checker of Python programs
Summary(pl.UTF-8):	Pasywny program do sprawdzania programów w Pythonie
Name:		python3-%{module}
Version:	3.3.2
Release:	1
License:	MIT
Group:		Development/Tools
#Source0Download: https://pypi.org/simple/pyflakes/
Source0:	https://files.pythonhosted.org/packages/source/p/pyflakes/%{module}-%{version}.tar.gz
# Source0-md5:	9bdc5cda9ddfa547e1e1def7a78b08f6
URL:		https://github.com/PyCQA/pyflakes
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.9
# default binary moved
Conflicts:  python-pyflakes < 2.1.1-4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyflakes is a simple program which checks Python source files for
errors. It is similar to PyChecker in scope, but differs in that it
does not execute the modules to check them. This is both safer and
faster, although it does not perform as many checks. Unlike PyLint,
Pyflakes checks only for logical errors in programs; it does not
perform any checks on style.

%description -l pl.UTF-8
Pyflakes to prosty program sprawdzający pliki źródłowe Pythona pod
kątem błędów. Jest podobny do PyCheckera jeśli chodzi o zakres
działania, ale różni się tym, że nie wykonuje modułów przy sprawdzaniu
ich. Jest to zarówno bardziej bezpieczne, jak i szybze, choć nie
sprawdza tak wielu rzeczy. W przeciwieństwie do PyLinta Pyflakes szuka
tylko błędów logicznych w programach; nie sprawdza stylu.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s pyflakes/test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/pyflakes{,-3}
ln -sf pyflakes-3 $RPM_BUILD_ROOT%{_bindir}/pyflakes

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/pyflakes/test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE NEWS.rst README.rst
%attr(755,root,root) %{_bindir}/pyflakes
%attr(755,root,root) %{_bindir}/pyflakes-3
%{py3_sitescriptdir}/pyflakes
%{py3_sitescriptdir}/pyflakes-%{version}-py*.egg-info
