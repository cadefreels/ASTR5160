from astropy.table import Table
import astropy.units as u

# CF Get Files from /d/scratch/ASTR5160/week10

starobjs  = Table.read("/d/scratch/ASTR5160/week10/stars-ra180-dec30-rad3.fits")

qsosobjs = Table.read("/d/scratch/ASTR5160/week10/qsos-ra180-dec30-rad3.fits")

print(starobjs)
print(qsosobjs)

# CF Coordinate-match these files to Legacy Survey Files
# astropy.coordinates.search_around_sky([180, 30], [180, 30], 0.000138889*u.deg)

# CF Where do the names of the files, both the stars-ra... and the Legacy Survey sweep files come in when doing a search_around_sky?
