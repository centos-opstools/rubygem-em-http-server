# Generated from em-http-server-0.1.8.gem by gem2rpm -*- rpm-spec -*-
%global gem_name em-http-server

Name:           rubygem-%{gem_name}
Version:        0.1.8
Release:        2%{?dist}
Summary:        Simple http server for eventmachine with the same interface as evma_httpserver
Group:          Development/Languages
License:        MIT
URL:            https://github.com/alor/em-http-server
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby
BuildRequires:  rubygem(eventmachine)

Requires:       rubygem(eventmachine)

BuildArch:      noarch
%if 0%{?el7}
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
Simple http server for eventmachine.


%package doc
Summary:        Documentation for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%license %{gem_instdir}/LICENSE
%{gem_instdir}/TODO
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/em-http-server.gemspec
%{gem_instdir}/test

%changelog
* Fri Dec 16 2016 Martin Mágr <mmagr@redhat.com> - 0.1.8-2
- Added Provides for EL releases

* Fri Dec 16 2016 Martin Mágr <mmagr@redhat.com> - 0.1.8-1
- Initial package
