Name:		texlive-musixtnt
Version:	40307
Release:	1
Summary:	A MusiXTeX extension library that enables transformations of the effect of notes commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/musixtnt
License:	gpl2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musixtnt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musixtnt.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package includes an archive containing a MusiXTeX extension
library musixtnt and C source code, binaries for Windows (32
bit and 64 bit) and MacOSX, and documentation for two programs:
fixmsxpart and msxlint. musixtnt.tex provides a macro
\TransformNotes that enables transformations of the effect of
notes commands such as \notes. In general, the effect of
\TransformNotes{input}{output} is that notes commands in the
source will expect their arguments to match the input pattern,
but the notes will be typeset according to the output pattern.
An example is extracting single-instrument parts from a
multi-instrument score. fixmsxpart corrects note spacing in a
single-part MusiXTeX source (possibly derived from a
multi-instrument score and as a result having irregular note
spacing). msxlint detects incorrectly formatted notes lines in
a MusiXTeX source file. This should be used before using
\TransformNotes.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/tex/generic/musixtnt
%doc %{_texmfdistdir}/texmf-dist/doc/generic/musixtnt
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/msxlint.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/msxlint.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
