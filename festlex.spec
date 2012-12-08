%define name festlex
%define version 1.4.3
%define release %mkrel 10

Name:  %name
Summary: Voices for Festival - a free speech synthesizer 
Version: %{version}
Release: %release
License: BSD
Group: Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-root 
URL: http://www.cstr.ed.ac.uk/projects/festival/
BuildArch: noarch

### DICTIONARIES
# Generic English dictionary
Source100: ftp://ftp.cstr.ed.ac.uk/pub/festival/%{version}/festlex_POSLEX.tar.bz2
# American English dictionary
Source101: ftp://ftp.cstr.ed.ac.uk/pub/festival/%{version}/festlex_CMU.tar.bz2

%description
Festival is a general multi-lingual speech synthesis system developed
at CSTR. It offers a full text to speech system with various APIs, as
well as an environment for development and research of speech synthesis
techniques. It is written in C++ with a Scheme-based command interpreter
for general control.

This package contains dictionaries for use with Festival


%package POSLEX
Group:		Sound
Summary:	Festival Speech Lexicons for Engish
Provides:	festival-lexicons

%description POSLEX
Part of speech lexicons and ngram from English.  Required by all
British and American English voices.

%package CMU
Group:		Sound
Summary:	CMU dictionary in Festival form
Provides:	festival-dictionary
Provides:	festival-dictionary-en_US
Requires:	festlex-POSLEX

%description CMU
CMU dictionary in Festival form, required for American English voices.

%prep
rm -rf $RPM_BUILD_ROOT

%setup  -T -c -q -a 100 -a 101

%build

#cd festival/lib/dicts/cmu
#make
#cd ../../..

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/festival
cp -a festival/lib/dicts $RPM_BUILD_ROOT%_datadir/festival

rm -f $RPM_BUILD_ROOT/%{_datadir}/festival/dicts/COPYING.poslex

%clean
rm -rf $RPM_BUILD_ROOT

%files POSLEX
%defattr(-,root,root)
%_datadir/festival/dicts/wsj*
%doc festival/lib/dicts/COPYING.poslex

%files CMU
%defattr(-,root,root)
%_datadir/festival/dicts/cmu
%doc festival/lib/dicts/cmu/COPYING



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-9mdv2011.0
+ Revision: 664301
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-8mdv2011.0
+ Revision: 605123
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-7mdv2010.1
+ Revision: 521122
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.4.3-6mdv2010.0
+ Revision: 424432
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.4.3-5mdv2009.0
+ Revision: 220788
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.4.3-4mdv2008.1
+ Revision: 149720
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 19 2007 Adam Williamson <awilliamson@mandriva.org> 1.4.3-3mdv2008.0
+ Revision: 90204
- rebuild for 2008


* Wed Jan 31 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.4.3-2mdv2007.0
+ Revision: 115700
- Import festlex

* Wed Jan 31 2007 Götz Waschk <waschk@mandriva.org> 1.4.3-2mdv2007.1
- rebuild

* Sun Jan 08 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.4.3-2mdk
- Rebuild

