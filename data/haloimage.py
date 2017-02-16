import pynbody
s = pynbody.load('g15784.lr.01024.gz')

# center the galaxy

# h = s.halos()

#h1 = h[1]
s.physical_units()

#pynbody.analysis.halo.center(s,mode='hyb')

#print s['star']

pynbody.plot.image(s, width=100, cmap='Blues');
