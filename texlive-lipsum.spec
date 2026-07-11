%global tl_name lipsum
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.7
Release:	%{tl_revision}.1
Summary:	Easy access to the Lorem Ipsum and other dummy texts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lipsum
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lipsum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lipsum.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lipsum.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package gives you easy access to 150 paragraphs of the Lorem Ipsum
dummy text provided by https://lipsum.com, plus a growing list of other
dummy texts in different languages.

