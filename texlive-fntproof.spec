Name:		texlive-fntproof
Version:	20101201
Release:	1
Summary:	A programmable font test pattern generator
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/fntproof
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fntproof.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fntproof.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package implements all the font testing commands of Knuth's
testfont.tex, but arranges that information necessary for each
command is supplied as arguments to that command, rather than
prompted for. This makes it possible to type all the tests in
one command line, and easy to input the package in a file and
to use the commands there. A few additional commands supporting
this last purpose are also made available.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/fntproof/fntproof.tex
%doc %{_texmfdistdir}/doc/generic/fntproof/README
%doc %{_texmfdistdir}/doc/generic/fntproof/fntproof-doc.pdf
%doc %{_texmfdistdir}/doc/generic/fntproof/fntproof-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
