import ephem

jup = ephem.Jupiter()
jup.compute('1230/1/1')
dist_ = jup.sun_distance
dist_km = dist_ * 149597870.691
print(dist_km)
