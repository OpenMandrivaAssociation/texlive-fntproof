# revision 20638
# category Package
# catalog-ctan /macros/generic/fntproof
# catalog-date 2010-12-01 01:24:27 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-fntproof
Version:	20101201
Release:	9
Summary:	A programmable font test pattern generator
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/fntproof
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fntproof.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fntproof.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package implements all the font testing commands of Knuth's
testfont.tex, but arranges that information necessary for each
command is supplied as arguments to that command, rather than
prompted for. This makes it possible to type all the tests in
one command line, and easy to input the package in a file and
to use the commands there. A few additional commands supporting
this last purpose are also made available.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20101201-2
+ Revision: 752004
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20101201-1
+ Revision: 718474
- texlive-fntproof
- texlive-fntproof
- texlive-fntproof
- texlive-fntproof

