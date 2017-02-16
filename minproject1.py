import pynbody
import pynbody.plot.sph as sph
import matplotlib.pylab as plt
from os import environ
import numpy
import pylab

s = pynbody.load('data/g15784.lr.01024.gz')

print '---------------'
print 'STATS FOR ALL TEST DATA'
print '---------------'
print 'Number of particles %d' % (len(s))
print 'Dark Matter %d' % (len(s.dm))
print 'Gas %d' % (len(s.gas))
print 'Stars %d' % (len(s.s))
print '--'

print 'Halos can be considered galaxies'
h = s.halos()
print 'halos %d' % (len(h))
print '-------------'
print '-------------'

# center the largest halo

print '--------------------------'
pynbody.analysis.halo.center(h[1])

# more precise centering using the retcen command


raw_input("")
# convert to physical units

s.physical_units()


print '-----------'
print 'LARGE SCALE STRUCTURE '
print '------------------'

print 'dark matter'
pynbody.plot.image(s.d[pynbody.filt.Sphere('10 Mpc')], width='10 Mpc', units = 'Msol kpc^-2', cmap='Greys');
raw_input("Show plot: Dark matter structure?")
plt.show()

# center on the largest halo and align the disk face on
print '---------------------------'
print 'LARGEST HALO'
pynbody.analysis.angmon.faceon(h[1])
