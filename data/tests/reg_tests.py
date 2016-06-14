# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:31 2016

@author: daphnehb
"""

rcs1 = "PARIS B 582028833"
rcs2 = "Paris 356 000 000"
rsc3 = "Paris B. 423 093 459"
not_rcs2 = "FR 81 423 093 459"
not_rcs1 = "3 8000 000 000 €"

import re

reg_rcs = '([[0-9]{3} *]{3})'

compiler_rcs = re.compile(reg_rcs)

print "compiler test"
print compiler_rcs.match(rcs2)
print "search test"
print re.findall(reg_rcs,rcs2)