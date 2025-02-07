#
# TODO: extend based on https://gitlab.com/redhat-crypto/fedora-crypto-policies and
#       https://src.fedoraproject.org/rpms/crypto-policies
#       We may need to create our own fork of that.
#
# Only sequoia for now to make rpm able to validate signatures.
#
Summary:	System-wide crypto policies
Name:		crypto-policies
Version:	0.1
Release:	2
License:	LGPL
Source0:	sequoia.txt
Source1:	rpm-sequoia.txt
#URL:		https://gitlab.com/redhat-crypto/fedora-crypto-policies
BuildArch:	noarch

%description
This package provides pre-built configuration files with cryptographic
policies for various cryptographic back-ends, such as SSL/TLS
libraries.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/crypto-policies/{back-ends,state,local.d,policies/modules}

cp -p %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/crypto-policies/back-ends/sequoia.config
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/crypto-policies/back-ends/rpm-sequoia.config

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/crypto-policies
%dir %{_sysconfdir}/crypto-policies/back-ends
%dir %{_sysconfdir}/crypto-policies/state
%dir %{_sysconfdir}/crypto-policies/local.d
%dir %{_sysconfdir}/crypto-policies/policies
%dir %{_sysconfdir}/crypto-policies/policies/modules

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/crypto-policies/back-ends/sequoia.config
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/crypto-policies/back-ends/rpm-sequoia.config
