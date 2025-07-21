Summary:	Voices for Festival - a free speech synthesizer 
Name:	festlex
Version:	2.4
Release:	1
License:	BSD
Group:	Sound
Url:		https://www.cstr.ed.ac.uk/projects/festival/
### DICTIONARIES
# Generic English dictionary
Source100:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/festlex_POSLEX.tar.gz
# American English dictionary
Source101:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/festlex_CMU.tar.gz
BuildArch:	noarch

%description
Festival is a general multi-lingual speech synthesis system developed
at CSTR. It offers a full text to speech system with various APIs, as
well as an environment for development and research of speech synthesis
techniques. It is written in C++ with a Scheme-based command interpreter
for general control.
This package contains dictionaries for use with Festival

#-----------------------------------------------------------------------------

%package POSLEX
Summary:	Festival Speech Lexicons for Engish
Provides:	festival-lexicons

%description POSLEX
Part of speech lexicons and ngram from English.  Required by all
British and American English voices.

%files POSLEX
%{_datadir}/festival/dicts/wsj*
%doc festival/lib/dicts/COPYING.poslex

#-----------------------------------------------------------------------------

%package CMU
Summary:	CMU dictionary in Festival form
Provides:	festival-dictionary
Provides:	festival-dictionary-en_US
Requires:	festlex-POSLEX

%description CMU
CMU dictionary in Festival form, required for American English voices.

%files CMU
%{_datadir}/festival/dicts/cmu
%doc festival/lib/dicts/cmu/COPYING

#-----------------------------------------------------------------------------

%prep
%setup  -T -c -q -a 100 -a 101


%build
# Nothing to do

%install
mkdir -p %{buildroot}%{_datadir}/festival
cp -a festival/lib/dicts %{buildroot}%{_datadir}/festival

rm -f %{buildroot}/%{_datadir}/festival/dicts/COPYING.poslex
