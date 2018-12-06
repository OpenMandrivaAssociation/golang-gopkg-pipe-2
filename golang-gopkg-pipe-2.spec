# Run tests in check section
%bcond_without check

%global goipath         gopkg.in/pipe.v2
%global forgeurl        https://github.com/go-pipe/pipe
%global commit          3c2ca4d525447ec8b2f606a6974f9c9f40831f26

%global common_description %{expand:
Unix-like pipelines for Go.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Unix-like pipelines for Go
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
BuildRequires: golang(gopkg.in/check.v1)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git3c2ca4d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180419git3c2ca4d
- First package for Fedora

