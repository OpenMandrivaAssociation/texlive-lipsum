Name:		texlive-lipsum
Version:	60561
Release:	2
Summary:	Easy access to the Lorem Ipsum dummy text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lipsum
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lipsum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lipsum.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lipsum.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/lipsum
%doc %{_texmfdistdir}/doc/latex/lipsum
#- source
%doc %{_texmfdistdir}/source/latex/lipsum

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
