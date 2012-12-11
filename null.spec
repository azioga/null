Epoch: 1
Name: null
Version: 2.1
Release: 81
Summary: A dummy package for bs testing purpose
Group: Development/Other
License: GPL

%description
Dummy package.

%package dummy
Group: Development/Other
Summary: Test package

%description dummy
A dummy subpackage.

%prep
%setup -D -T -n .

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

%post -p /bin/csh
echo "csh sux"

%files
%files dummy



%changelog
* Wed Aug 29 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:2.1-81
+ Revision: 816041
- rebuild

* Wed Aug 29 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:2.1-80
+ Revision: 816012
- build test

* Sun Aug 12 2012 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-79
+ Revision: 814405
- bump to test l1

* Sun Aug 12 2012 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-78
+ Revision: 814401
- bump to test @filesize stripping

* Thu Aug 09 2012 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-77
+ Revision: 813648
- bump
- bump
- bump
- test
- bump
- bump (testing youri checks)
- test
- trying again, with a dot in the subpackage
- trolling rpmlint: ending summary with a dot
- testing bogus group in spec
- buildroot not needed anymore
- removed the texlive buildreq
- bump

* Wed Nov 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 1:2.1-67.1
+ Revision: 729376
- Test build system with build requires of new texlive

* Wed Oct 12 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-67
+ Revision: 704463
- bump

* Mon Oct 03 2011 Andrey Bondrov <abondrov@mandriva.org> 1:2.1-66
+ Revision: 702561
- Test submit

* Tue Sep 27 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-65
+ Revision: 701542
- bump

* Mon Sep 26 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-64
+ Revision: 701204
- bump

* Wed Sep 21 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-63
+ Revision: 700652
- bump

* Tue Sep 20 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-62
+ Revision: 700461
- bump

* Tue Sep 20 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-61
+ Revision: 700446
- bump
- testing new repsys version on kenobi

* Wed Sep 14 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-59
+ Revision: 699718
- test

* Mon Sep 05 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-58
+ Revision: 698312
- bump

* Sat Sep 03 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-57
+ Revision: 698180
- bump
- removed test of missing patch
- testing submit of a broken package
- bump

* Wed Jul 20 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-53
+ Revision: 690771
- bump
- bump

* Mon Jul 18 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-51
+ Revision: 690574
- Bump

* Mon Jul 18 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-50
+ Revision: 690566
- bump
- Broken spec test

* Wed Jul 06 2011 Eugeni Dodonov <eugeni@mandriva.com> 1:2.1-48
+ Revision: 688960
- Bump

* Thu May 19 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-47
+ Revision: 676191
- bump

* Thu May 12 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-46
+ Revision: 673973
- bump

* Mon May 09 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-45
+ Revision: 673013
- bump

* Mon May 09 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-44
+ Revision: 673009
- bump

* Mon May 09 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-43
+ Revision: 672681
- bump

* Fri May 06 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-42
+ Revision: 670261
- bump
- bump
- bump

* Fri Mar 11 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-39
+ Revision: 643863
- bump

* Fri Feb 25 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-38
+ Revision: 639793
- testing it without mkrel

* Sun Jan 16 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-37
+ Revision: 631144
- bump

* Tue Jan 04 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-36mdv2011.0
+ Revision: 628510
- new release

* Thu Dec 16 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-35mdv2011.0
+ Revision: 622213
- new release
- new release

* Tue Dec 07 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-34mdv2011.0
+ Revision: 614424
- new release

* Tue Nov 30 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-33mdv2011.0
+ Revision: 603996
- rebuild

* Tue Nov 16 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-32mdv2011.0
+ Revision: 598122
- new release
- new release
- new release
- new release

* Mon Aug 09 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-28mdv2011.0
+ Revision: 567830
- bump
- Hello, world!
  CCBUG: 58861
- Este ?\195?\169 um teste (sorry, testing utf8)
  CCBUG: 58861
- Simple commit testing the CCBUG feature
  CCBUG: 58861
- removed the sleep 10m, not needed anymore

* Mon Apr 19 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-26mdv2010.1
+ Revision: 536763
- added a 10m sleep to allow watching package status while building

* Fri Apr 16 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-25mdv2010.1
+ Revision: 535631
- New release

* Wed Apr 14 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-24mdv2010.1
+ Revision: 534659
- New release

* Wed Apr 14 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-23mdv2010.1
+ Revision: 534637
- New release, a huge amount of changes!

* Sun Apr 11 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-22mdv2010.1
+ Revision: 533583
- New release

* Sat Apr 10 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-21mdv2010.1
+ Revision: 533559
- New release (the gates are open)
- New release (new kenobi, new world)
- New release
- bump

* Tue Mar 02 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-17mdv2010.1
+ Revision: 513524
- bump

* Wed Feb 24 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-16mdv2010.1
+ Revision: 510790
- bump

* Tue Feb 23 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 1:2.1-15mdv2010.1
+ Revision: 510436
- testing submit from kenobiczyk

* Thu Apr 30 2009 Gustavo De Nardin <gustavodn@mandriva.com> 2-14mdv2010.0
+ Revision: 369182
- release for testing 2009.1 submission

* Tue Mar 10 2009 Gustavo De Nardin <gustavodn@mandriva.com> 2-13mdv2009.1
+ Revision: 353490
- submit test

* Wed Nov 12 2008 Oden Eriksson <oeriksson@mandriva.com> 2-12mdv2009.1
+ Revision: 302449
- rebuild

  + Gustavo De Nardin <gustavodn@mandriva.com>
    - increasing release for repository test

* Mon Jun 23 2008 Oden Eriksson <oeriksson@mandriva.com> 2-10mdv2009.0
+ Revision: 227984
- rebuild

  + Gustavo De Nardin <gustavodn@mandriva.com>
    - currently, the %%setup macro is required to be used for a package to generate
      the debug info subpackage, as it sets %%buildsubdir

* Tue Mar 04 2008 Olivier Blin <blino@mandriva.org> 2-9mdv1997.1
+ Revision: 178354
- revert to old release
- major upgrade

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 2-8mdv2008.1
+ Revision: 136633
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Anssi Hannula <anssi@mandriva.org>
    - test\ncommit

  + Pixel <pixel@mandriva.com>
    - test
    - test
    - test
    - testing

* Wed Oct 24 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 2-4mdv2008.1
+ Revision: 101775
- Do not abort anymore.
- Submit test.
- Force a failure.
- Another commit
- Commit null.

