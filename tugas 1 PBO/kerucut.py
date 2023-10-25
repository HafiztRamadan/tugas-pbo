print("aplikasi menghitung luas dan volume kerucut")

#atur nilai
phi = 3.14
r = 6
s = 7
T = 9

#rumus
luas_selimut = phi* r * s
luas_permukaan = (phi * r * s)+(phi * r**2)
volume = 1/3 * phi * r**2 * T

#output
print("hasil luas seilmut:", luas_selimut)
print("hasil luas permukaan:", luas_permukaan)
print("hasil volume:", volume)