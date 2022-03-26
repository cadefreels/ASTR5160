from astropy.table import Table
# CF Get  UBVRI for PG1633+099A from the Wyocourses links page

V = 15.256
B = 0.873 + V
U = 0.320 + B
R = V - 0.505
I = R - 0.511

# CF Check values for UBVRI

print(V)
print(B)
print(U)
print(R)
print(I)

# CF Convert UBVRI to ugriz to compare g and z magnitude of PG1633+099A to SDSS Navigator Tool
# CF Use Jester et al. (2005) "All stars with Rc - Ic < 1.15" conversion, since U-B > 0 for PG 1633+099A

# CF SDSS Navigator Tool g and z magnitudes for PG1633+099A

sdssg = 15.70
sdssz = 14.55 

g = V + 0.60 * (B-V) - 0.12
r = V - 0.42 * (B-V) + 0.11
r_z = 1.72 * (R - I) - 0.41
z = r - r_z

print(sdssg)
print(g)
print(sdssz)
print(z)

# CF Yes, the converted g and z magnitudes are near the expected SDSS values

# CF Task 2

objs = Table.read("/d/scratch/ASTR5160/data/legacysurvey/dr9/south/sweep/9.0/sweep-010m010-020m005.fits")
#print(objs)

# CF Can get flux vales for PG1633+099A from the proper sweep file that includes it's RA (16:35:26) and Dec (+09:47:53)
# CF and from the FLUX_G column for the g fluxe, the FLUX_R column for the r flux,  and the FLUX_Z column for the z flux

# CF Use m(band) = 22.5 - 2.5 * log10(flux in band) to convert the grz fluxes to magnitudes, since the fluxes are given in nanomaggies

#CF Check these with PG1633+099A from SDSS Navigator Tool
