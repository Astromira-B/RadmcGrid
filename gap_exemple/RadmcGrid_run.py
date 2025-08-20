#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 13:09:23 2025

@author: abouikni
"""

import radmcgrid as grid
from pathlib import Path   

tstar_rstar_list = [('[4900.0]', '[1.87*rs]')]
rout   = 1.2
rdisk2 = 100
mdisk1 = 1e-10
mdisk2 = 1e-3
Inc = [0, 30]
npix = 500
sizeau = 60
nlmin = 8.
nlmax = 13
nlam = 11
Cdelt3 = 0.5
dpc = 145.0
template_dir = Path(__file__).parent.parent / "opacities"

grid.run(model = 1,
         tstar_rstar_list = tstar_rstar_list, 
         rout = rout, 
         mdisk1 = mdisk1,
         Inc = Inc, 
         npix = npix,
         sizeau = sizeau,
         nlmin = nlmin,
         nlmax = nlmax, 
         nlam = nlam,
         Cdelt3 = Cdelt3,
         dpc = dpc,
         mdisk2 = mdisk2,
         rdisk2 = rdisk2,
         composition_name = "full_astrosil_amira",
         template_dir = str(template_dir) )

