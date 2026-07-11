%global tl_name musixtnt
%global tl_revision 69742

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A MusiXTeX extension library that enables transformations of the effect of no...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/musixtnt
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/musixtnt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/musixtnt.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(musixtex)
Requires:	texlive(musixtnt.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package includes an archive containing a MusiXTeX extension library
musixtnt and C source code, binaries for Windows (32 bit and 64 bit) and
MacOSX, and documentation for two programs: fixmsxpart and msxlint.
musixtnt.tex provides a macro \TransformNotes that enables
transformations of the effect of notes commands such as \notes. In
general, the effect of \TransformNotes{input}{output} is that notes
commands in the source will expect their arguments to match the input
pattern, but the notes will be typeset according to the output pattern.
An example is extracting single-instrument parts from a multi-instrument
score. fixmsxpart corrects note spacing in a single-part MusiXTeX source
(possibly derived from a multi-instrument score and as a result having
irregular note spacing). msxlint detects incorrectly formatted notes
lines in a MusiXTeX source file. This should be used before using
\TransformNotes.

