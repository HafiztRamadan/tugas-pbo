print("aplikasi menghitung luas dan volume prisma segitiga")

#atur nilai
s1 =20
s2 =25
s3 =30
T =25
t = 40
a = 10

#rumus 
luas_segitiga = (s1+s2+s3)*T
luas_prisma = (s1+s2+s3)*T + a *t
volume = 1/2*a*t*T

#output
print("hasil luas segitiga:",luas_segitiga)
print("hasil luas prisma:",luas_prisma)
print("hasil volume:",volume)