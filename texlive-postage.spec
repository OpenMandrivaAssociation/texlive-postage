Name:		texlive-postage
Version:	55920
Release:	1
Summary:	Stamp letters with >>Deutsche Post<<'s service >>Internetmarke<<
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/postage
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/postage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/postage.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/postage.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The postage package is used for franking letters with
>>Deutsche Post<<'s online postage service >>Internetmarke<<.
Note that in order to print valid stamps you must point to a
valid PDF of >>Deutsche Post<<'s >>Ausdruck 4-spaltig (DIN
A4)<<.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/postage
%{_texmfdistdir}/tex/latex/postage
%doc %{_texmfdistdir}/doc/latex/postage

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
