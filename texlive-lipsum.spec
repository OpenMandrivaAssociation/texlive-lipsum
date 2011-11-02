Name:		texlive-lipsum
Version:	v1.2
Release:	1
Summary:	Easy access to the Lorem Ipsum dummy text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lipsum
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lipsum.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lipsum.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lipsum.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package gives you easy access to the Lorem Ipsum dummy
text; an option is available to separate the paragraphs of the
dummy text into TeX-paragraphs. All the paragraphs are taken
with permission from http://lipsum.com/.

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
%{_texmfdistdir}/tex/latex/lipsum/lipsum.sty
%doc %{_texmfdistdir}/doc/latex/lipsum/README
%doc %{_texmfdistdir}/doc/latex/lipsum/lipsum.pdf
#- source
%doc %{_texmfdistdir}/source/latex/lipsum/lipsum.dtx
%doc %{_texmfdistdir}/source/latex/lipsum/lipsum.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
