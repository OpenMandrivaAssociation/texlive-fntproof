%global tl_name fntproof
%global tl_revision 20638

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A programmable font test pattern generator
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/fntproof
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fntproof.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fntproof.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package implements all the font testing commands of Knuth's
testfont.tex, but arranges that information necessary for each command
is supplied as arguments to that command, rather than prompted for. This
makes it possible to type all the tests in one command line, and easy to
input the package in a file and to use the commands there. A few
additional commands supporting this last purpose are also made
available.

