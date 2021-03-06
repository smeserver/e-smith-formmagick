# $Id: e-smith-formmagick.spec,v 1.21 2010/10/19 17:51:27 snetram Exp $

Summary: e-smith-formmagick Perl modules for web manager i18n
%define name e-smith-formmagick
Name: %{name}
%define version 2.2.0
%define release 4
Version: %{version}
Release: %{release}%{?dist}
License: Artistic
Group: Applications/CPAN
Source0: %{name}-%{version}.tar.gz
Patch1: e-smith-formmagick-2.2.0-lib64.patch
Patch2: e-smith-formmagick-2.2.0-ip-fqdn-new.patch
BuildRoot: /var/tmp/%{name}-{%version}-%{release}-buildroot/
Requires: perl-CGI-FormMagick >= 0.92-16.el4.sme
Requires: perl(WWW::Automate) >= 0.20
Requires: perl(Crypt::Cracklib)
Requires: perl(I18N::LangTags) >= 0.27
Requires: e-smith-lib >= 1.18.0-21
BuildRequires: e-smith-devtools >= 1.6.6
BuildArchitectures: noarch

%changelog
* Tue Oct 19 2010 Jonathan Martens <smeserver-contribs@snetram.nl> 2.2.0-4.sme
- Revert previous change as it might cause regression in contribs [SME: 6296]
- Add additional locale string [SME: 6296]

* Sun Oct 17 2010 Jonathan Martens <smeserver-contribs@snetram.nl> 2.2.0-3.sme
- Update textbox description to also reflect the option of a FQDN [SME: 6296]

* Thu Feb 4 2010 Shad L. Lords <slords@mail.com> 2.2.0-2.sme
- Update path for 64-bit compatibility [SME: 5756]

* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 2.2.0-1.sme
- Roll new stream to separate sme7/sme8 trees [SME: 4633]

* Thu Aug  7 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.4.0-20
- Move RESET_PASSWORD_TITLE to general [SME: 4475]
- Reverting all *PASSWORD_NO_MATCH to *PASSWORD_VERIFY_ERROR locale keys [SME: 4476]
- Add YOUR_ACCOUNT_INVALID to general [SME: 4478]

* Tue Aug  5 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.4.0-19
- Revert previous invalid locale changes (reverting to 1.4.0-17) [SME: 4472]

* Mon Aug  4 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.4.0-18
- Reverting some locale changes

* Sun Jul 27 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.4.0-17
- Revert patch here and fix in e-smith-ibays instead because of multiple 
  dependencies and incorrect naming scheme

* Sun Jul 27 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.4.0-16
- Fix password verify entry text box description in ibays panel entry 
  in e-smith-formmagick's general [SME: 4460]

* Tue Jul 8 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.4.0-15
- Moving single occurence for HOSTTYPE back to e-smith-hosts

* Sat Jul 5 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.4.0-14
- Added missing entry to general [SME: 4289]

* Mon Apr 28 2008 Shad L. Lords <slords@mail.com> 1.4.0-13
- Bump release to allow rebuild

* Fri Apr 25 2008 Shad L. Lords <slords@mail.com> 1.4.0-12
- Update requires to really pull in perl-CGI-FormMagick [SME: 4269]

* Wed Apr 23 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.4.0-11
- And more common <base> entries to general [SME: 4289]

* Mon Mar 10 2008 Shad L. Lords <slords@mail.com> 1.4.0-10
- Default charset to UTF-8 unless specified [SME: 3858]

* Wed Feb 13 2008 Stephen Noble <support@dungog.net> 1.4.0-9
- And more common <base> entries to general [SME: 3886]

* Sun Feb 10 2008 Stephen Noble <support@dungog.net> 1.4.0-8
- Added more common <base> entries to general [SME: 3886]

* Sun Feb 10 2008 Stephen Noble <support@dungog.net> 1.4.0-7
- Added header <base> entries to general [SME: 3886]

* Thu Nov 08 2007 Gavin Weight <gweight@gmail.com> 1.4.0-6
- Remove/Fix Formmagick.pm.orig file. [SME: 3526]

* Fri Jun 1 2007 Shad L. Lords <slords@mail.com> 1.4.0-5
- pam_unix requires passwords >= 6 [SME: 3039]

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Wed Apr 5 2006 Gordon Rowell <gordonr@gormand.com.au> 1.4.0-03
- Revert last change [SME: 1193]

* Wed Apr 5 2006 Gordon Rowell <gordonr@gormand.com.au> 1.4.0-02
- Restrict passwords to 14 characters [SME: 1193]

* Wed Mar 15 2006 Charlie Brady <charlie_brady@mitel.com> 1.4.0-01
- Roll stable stream version. [SME: 1016]

* Thu Dec 15 2005 Gordon Rowell <gordonr@gormand.com.au> 1.3.2-03
- 'strong' passwords must meet both Cracklib and the standard password
   mantra: Upper Case AND Lower Case AND Digits AND Special characters
   AND at least seven characters long [SME: 161]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.3.2-02
- Bump release number only

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.3.2-01]
- Remove L10Ns from base packages [SF: 1309520]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.3.1-01]
- New dev stream before relocating L10Ns

* Fri Sep 30 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-13]
- Added Italian L10N - Thanks Filippo Carletti [SF: 1309266]

* Fri Sep 30 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-12]
- Added tag for unlocalised string - thanks Filippo Carletti [SF: 1309284]

* Mon Sep 26 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-11]
- Added German L10N - Thanks Dietmar Berteld [SF: 1293325]

* Mon Sep  5 2005 Tony Clayton <apc@e-smith.com>
- [1.3.0-10]
- Update requires to CGI::FormMagick >= 0.91-28
- Fix esmith::FormMagick constructor brokenness for IbayPlugin compatibility

* Mon Jul 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-09]
- Add english tags for formmagick validation [SF: 1157116 (Shad)]

* Wed Nov 10 2004 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-08]
- Don't try to read lexicon files which aren't there. [charlieb MN00056737]

* Tue Nov  9 2004 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-07]
- Move changelog to top of spec file. [charlieb]
- Don't try to read from unopened file handle in _lexicon_read()
  [charlieb MN00056701]
- Replace deprecated Copyright header with License header. [charlieb]

* Fri Oct  1 2004 Michael Soulier <msoulier@e-smith.com>
- [1.3.0-06]
- Added an error to the top of all pages with errors in them, instructing the
  user to scroll down for specifics. So far localised in English only.
  [msoulier MN00046857]

* Tue Sep 28 2004 Michael Soulier <msoulier@e-smith.com>
- [1.3.0-05]
- Updated requires with new perl dependencies. [msoulier MN00040240]

* Thu Aug  5 2004 Michael Soulier <msoulier@e-smith.com>
- [1.3.0-04]
- Added patch to permit "permitpipes" in validation, to turn off automagick
  addition of "nopipes". Thanks to Pascal Schirrmann <schirrms@schirrms.net>
  for the idea and the preliminary patch. 
  [msoulier MN00044774]

* Wed Oct 22 2003 Michael Soulier <msoulier@e-smith.com>
- [1.3.0-03]
- Updated _lexicon_filename_list to return lexicon from the preferred
  languages that exists, instead of referencing non-existant files.
  [msoulier 10397]

* Fri Oct 10 2003 Michael Soulier <msoulier@e-smith.com>
- [1.3.0-02]
- Added display_error and display_success methods. [msoulier 9652]

* Fri Oct 10 2003 Michael Soulier <msoulier@e-smith.com>
- [1.3.0-01]
- roll to dev stream - 1.3.0

* Wed Sep  3 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.2.1-01]
- Rebuild [gordonr 1305]

* Wed Sep  3 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.2.0-03]
- Rebuild [gordonr 1305]

* Wed Sep  3 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.2.0-02]
- Adjusted Copyright [gordonr 1305]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-01]
- Changing version to stable stream number - 1.2.0

* Fri Jun 20 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.1.2-02]
- Bring the icon and message closer (IE fix) [gordonr 9084]

* Thu Jun 19 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.1.2-01]
- Add icon for success/error [gordonr 9055]

* Fri May  9 2003 Tony Clayton <apc@e-smith.com>
- [1.1.1-17]
- Remove duplicate status message from print_status_message [tonyc 8289]

* Fri May  9 2003 Tony Clayton <apc@e-smith.com>
- [1.1.1-16]
- Updated Spanish lexicon - thanks Alejandro [gordonr 3793]

* Tue May  6 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.1.1-15]
- Fixed syntax error in WIP code, and hid it [gordonr 3793]

* Tue May  6 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.1.1-14]
- Replaced "MDP" with mot de passe in FormMagick general lexicon [gordonr 3793]
- Added Spanish FM general lexicon [gordonr 3793]

* Thu May  1 2003 Tony Clayton <apc@e-smith.com>
- [1.1.1-13]
- print a sectionbar (hr) after status_message if not decorated [tonyc 8289]

* Thu Apr 17 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.1.1-12]
- Default status message to undecorated until we modify everyone to
  using $fm->error() and $fm->success() [gordonr 8289]

* Tue Apr  8 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.1.1-11]
- Default status message to error type, not success type [gordonr 7919]

* Thu Apr  3 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.1.1-10]
- Added default error string of "ERROR" in error() method [gordonr 7919]

* Thu Apr  3 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.1.1-09]
- Apply div.success and div.error automatically around the status
  message in print_status_message as long as panels calls
  $self->error() or $self->success() [gordonr 7919]

* Thu Apr  3 2003 Lijie Deng <lijied@e-smith.com>
- [1.1.1-08]
- Added sub routine to validate the description [lijied 5054]

* Fri Mar 28 2003 Lijie Deng <lijied@e-smith.com>
- [1.1.1-07]
- Modified French lexicon to use lang="fr", rename the lexicon
  directory to fr [lijied 6787] 

* Fri Mar 14 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.1.1-06]
- Suppress missing languages line if none missing [gordonr 7677]

* Fri Mar 14 2003 Mark Knox <markk@e-smith.com>
- [1.1.1-05]
- Fixed a missing quote, and a subtle circular dependency in lexicon
  loader [markk 7677]

* Fri Mar 14 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.1.1-04]
- Ensure that the fallback_language is in the list of languages back from
  get_languages(). Log one "missing languages" line [gordonr 7677]

* Tue Mar 11 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.1.1-03]
- Override get_languages() to only return languages for which we have 
  lexica [gordonr 6787]

* Thu Mar  6 2003 Mike Dickson <miked@e-smith.com>
- [1.1.1-02]
- reverted to old cron system for this server package [miked 6734]

* Thu Mar  6 2003 Mike Dickson <miked@e-smith.com>
- [1.1.1-01]
- moved cron job to crontab [miked6724]

* Tue Feb 25 2003 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-08]
- Added success and error methods to standardize panels. [msoulier 5517]

* Thu Jan 16 2003 Mark Knox <markk@e-smith.com>
- [1.1.0-07]
- Moved locale-specific date generation code into esmith::FormMagick as
  gen_locale_date_string [markk 3357]

* Wed Jan 15 2003 Mark Knox <markk@e-smith.com>
- [1.1.0-06]
- Removed globs from lexicon file finder [markk 6574]

* Fri Dec 27 2002 Mike Dickson <miked@e-smith.com>
- [1.1.0-05]
- removed debugging messages inserted during UI update [miked 5494]

* Mon Dec  9 2002 Mike Dickson <miked@e-smith.com>
- [1.1.0-04]
- ui update {miked 5494]

* Mon Dec  2 2002 Mike Dickson <miked@e-smith.com>
- [1.1.0-03]
- ui update  [miked 5494

* Thu Nov 21 2002 Mike Dickson <miked@e-smith.com>
- [1.1.0-02]
- update to new UI system [miked 5494]

* Wed Nov 20 2002 Mike Dickson <miked@e-smith.com>
- [1.1.0-01]
- Changing to development stream to 1.1.0

* Tue Oct 15 2002 Charlie Brady <charlieb@e-smith.com>
- [1.0.1-01]
- Roll new version to fix tagging problem

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.0.0-01]
- Roll to maintained version number to 1.0.0

* Wed Sep 25 2002 Mark Knox <markk@e-smith.com>
- [0.3.3-01]
- Rolling version to fix patching problems

* Wed Sep 25 2002 Mark Knox <markk@e-smith.com>
- [0.3.2-05]
- Don't export methods we don't provide [markk 4909]

* Fri Sep  6 2002 Mark Knox <markk@e-smith.com>
- [0.3.2-04]
- Added French localisation of NO_PIPES_ALLOWED [markk 3807]

* Thu Sep  5 2002 Mark Knox <markk@e-smith.com>
- [0.3.2-03]
- Corrected a broken test. All tests now pass. [markk 3807]

* Wed Sep  4 2002 Charlie Brady <charlieb@e-smith.com>
- [0.3.2-02]
- Add setting of $ENV{'HOME'} to BEGIN in esmith::FormMagick, specifically
  so that mysql can find ~root/.my.cnf. [charlieb 4778]

* Mon Jun 24 2002 Kirrily Robert <skud@e-smith.com>
- [0.3.2-01]
- Removed now-superfluous nonblank() validation routine (it checked for 
  nopipes as well, but that's now automatic) [skud 3807]

* Mon Jun 24 2002 Kirrily Robert <skud@e-smith.com>
- [0.3.1-01]
- Nopipes validation is now forced for all fields [skud 3807]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [0.3.0-01]
- Changing version to development stream number to 0.3.0

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [0.2.0-01]
- Changing version to maintained stream number to 0.2.0

* Fri May 31 2002 Mark Knox <markk@e-smith.com>
- [0.1.30-01]
- Forgot to export the new sub [markk 3752]

* Fri May 31 2002 Mark Knox <markk@e-smith.com>
- [0.1.29-01]
- Override nonblank to not allow pipes in field data [markk 3752]

* Mon May 27 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.28-01]
- Fix filelist generation for access restriction [gordonr 2187]

* Mon May 27 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.27-01]
- Restrict access to FormMagick session cache [gordonr 2187]

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.26-01]
- RPM rebuild forced by cvsroot2rpm

* Thu May 23 2002 Mark Knox <markk@e-smith.com>
- [0.1.25-01]
- Change test to expect correct results [markk 3618]

* Wed May 22 2002 Charlie Brady <charlieb@e-smith.com>
- [0.1.24-01]
- Set PATH to /bin:/usr/bin:/usr/local/bin rather than to empty.

* Wed May 22 2002 Mark Knox <markk@e-smith.com>
- [0.1.23-01]
- Localise "it's WAY too short" cracklib message -> fr-ca [markk 3592]

* Wed May 22 2002 Mark Knox <markk@e-smith.com>
- [0.1.22-01]
- Added validate_password method: checks a password using one of cracklib,
  FormMagick validator, or none. [markk 3592]
- Added localisations for password validation messages [markk 3592]

* Thu May 16 2002 Kirrily Robert <skud@e-smith.com>
- [0.1.21-01]
- Renamed en and fr locale directories to en-us and fr-ca [skud 3446]

* Thu May 16 2002 Kirrily Robert <skud@e-smith.com>
- [0.1.20-01]
- Added OPERATION_STATUS_REPORT localisation [skud 3446]

* Tue May 14 2002 Tony Clayton <apc@e-smith.com>
- [0.1.19-01]
- grrr.. fix typo in charset fix [tonyc 3027/3462]

* Tue May 14 2002 Tony Clayton <apc@e-smith.com>
- [0.1.18-01]
- Re-add fix from 0.1.13-01: pass charset option to fm constructor
  [tonyc 3027]
- Re-add export_to_level line in esmith::formmagick::import
  [tonyc 3027]

* Mon May 13 2002 Tony Clayton <apc@e-smith.com>
- [0.1.17-01]
- Fix esmith::FormMagick::new to pass empty subclass test [tonyc 3109]

* Wed May  8 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.16-01]
- left/right trim heading/description entries after localisation [gordonr 3223]

* Thu Apr 25 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.15-01]
- Moved FormMagick session cookies to /var/cache/e-smith/formmagick/sessions 
- Added added tmpwatch (daily, >8 hours old) for above directory [gordonr 3213]

* Wed Apr 24 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.14-01]
- Allow FM files in the html directory for {index,initial}.html [gordonr 3201]

* Tue Apr 23 2002 Mark Knox <markk@e-smith.com>
- [0.1.13-01]
- Allow user to specify XML charset, default to ISO-8859-1 [markk 3209]

* Fri Apr 19 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.12-01]
- Again set fallback_language("en-us") [gordonr 3031]
- fix undefined value bug in FormMagick.pm when no external lexicons exist
  [tonyc]

* Tue Apr 16 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.10-01]
- Set fallback_language("en-us") [gordonr 3031]
- Added optional filename=>"/path/to/script" to new() [gordonr 3155]
- Added parsing of navigation headers [gordonr 3155]

* Mon Apr 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.10-01]
- Re-do symlink resolution using knowledge of e-smith hierarchy. The old
  one was ugly and would break in the general case anyway [gordonr #3031]

* Fri Apr 12 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.9-01]
- Resolve $0 when it turns up as a symlink [gordonr #3031]

* Fri Apr 12 2002 Kirrily Robert <skud@e-smith.com>
- [0.1.8-01]
- Now looks for lexicons in /etc/e-smith/locale [skud #3031]
 
* Fri Mar 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.7-01]
- Changed to BuildArchitectures: to noarch 

* Wed Mar 13 2002 Kirrily Robert <skud@e-smith.com>
- [0.1.6-01]
- Fixed importing so that esmith::FormMagick exported functions are
  exported all the way out to scripts using subclasses [skud]

* Thu Feb 28 2002 Kirrily Robert <skud@e-smith.com>
- [0.1.5-01]
- Updated dependencies to more recent Perl libraries and devtools [skud]

* Tue Feb 26 2002 Kirrily Robert <skud@e-smith.com>
- [0.1.4-01]
- added print_status_message() routine

* Tue Feb 26 2002 Kirrily Robert <skud@e-smith.com>
- [0.1.3-01]
- added full path to buildtests directive

* Thu Feb 21 2002 Kirrily Robert <skud@e-smith.com>
- [0.1.2-01]
- cleanup of test scripts

* Thu Feb 21 2002 Kirrily Robert <skud@e-smith.com>
- [0.1.1-01]
- improved tests (skud)
- improved documentation (skud)
- print_button() now exported (skud)
- security settings are now automatic (skud)

* Mon Feb 18 2002 Kirrily Robert <skud@e-smith.com>
- [0.1.0-01]
- Initial release of 0.1.0.
%description
e-smith-formmagick provides a set of Perl modules containing various 
convenience functions used to create SMEServer server-manager panels.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1
%patch2 -p1

%build
# build the test suite from embedded tests
/sbin/e-smith/buildtests 20e-smith-formmagick
mkdir -p root/var/cache/e-smith/formmagick/sessions

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    | grep -v /var/cache/e-smith/formmagick/sessions \
    >%{name}-%{version}-%{release}-filelist
echo '%dir %attr(0700,root,root) /var/cache/e-smith/formmagick/sessions' \
	>>%{name}-%{version}-%{release}-filelist
echo "%doc Copying" >> %{name}-%{version}-%{release}-filelist
echo "%doc Artistic" >> %{name}-%{version}-%{release}-filelist
echo "%doc LICENSE" >> %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
