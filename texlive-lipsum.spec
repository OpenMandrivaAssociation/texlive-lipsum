# revision 22098
# category Package
# catalog-ctan /macros/latex/contrib/lipsum
# catalog-date 2011-04-15 00:51:19 +0200
# catalog-license lppl
# catalog-version v1.2
Name:		texlive-lipsum
Version:	v1.2
Release:	5
Summary:	Easy access to the Lorem Ipsum dummy text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lipsum
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lipsum.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lipsum.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lipsum.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package gives you easy access to the Lorem Ipsum dummy
text; an option is available to separate the paragraphs of the
dummy text into TeX-paragraphs. All the paragraphs are taken
with permission from http://lipsum.com/.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v1.2-2
+ Revision: 753314
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v1.2-1
+ Revision: 718864
- texlive-lipsum
- texlive-lipsum
- texlive-lipsum
- texlive-lipsum

