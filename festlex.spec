%define name festlex
%define version 1.4.3
%define release %mkrel 3

Name:  %name
Summary: Voices for Festival - a free speech synthesizer 
Version: %{version}
Release: %release
License: BSD
Group: Sound
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

