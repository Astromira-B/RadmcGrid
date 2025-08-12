#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 13:09:23 2025

@author: abouikni
"""
import RadmcGrid as grid
#import grid_test as grid

tstar_rstar_list = [('[4900.0]', '[1.87*rs]')]
rout   = 1.2
rdisk = 100
#rdisk2 = 100
mdisk1 = 1e-10
#mdisk2 = 1e-3
Inc = [0, 30]
npix = 500
sizeau = 60
nlmin = 8.
nlmax = 13
nlam = 11
Cdelt3 = 0.5
dpc = 145.0
# grid.run(tstar_rstar_list, rout, rdisk2, mdisk1, mdisk2, Inc, npix, nlmin, nlmax, nlam, Cdelt3, dpc)
grid.run(model = 2,
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
        # mdisk2 = mdisk2,
         rdisk = rdisk,
         composition_name = "full_astrosil_amira",
         template_dir = "/data/users/abo/test_radmc" )
