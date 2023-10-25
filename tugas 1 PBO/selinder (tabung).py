print("aplikasi menghitung luas dan volume selinder")

#atur nilai
phi = 3.14
r = 5
T = 6

#rumus
luas_selimut = 2 * phi * r * T
luas_permukaan = (2 * phi * r * T) + (2 * phi * r**2)
volume = phi * r**2 * T

#output
print("hasil luas selimut:", luas_selimut)
print("hasil luas permukaa:", luas_permukaan)
print("hasil volume:", volume)