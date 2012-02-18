%global packname  vsn
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          3.22.0
Release:          1
Summary:          Variance stabilization and calibration for microarray data
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/vsn.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/vsn_3.22.0.tar.gz
Requires:         R-Biobase 
Requires:         R-methods R-affy R-limma R-lattice 
Requires:         R-affydata R-hgu95av2cdf 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-Biobase
BuildRequires:    R-methods R-affy R-limma R-lattice 
BuildRequires:    R-affydata R-hgu95av2cdf 

%description
The package implements a method for normalising microarray intensities,
both between colours within array, and between arrays. The method uses a
robust variant of the maximum-likelihood estimator for the stochastic
model of microarray data described in the references (see vignette). The
model incorporates data calibration (a.k.a. normalization), a model for
the dependence of the variance on the mean intensity, and a variance
stabilizing data transformation. Differences between transformed
intensities are analogous to "normalized log-ratios". However, in contrast
to the latter, their variance is independent of the mean, and they are
usually more sensitive and specific in detecting differential

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/scripts
