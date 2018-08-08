import Fuzzy as fis


f1 = fis.Triangle(20, 30, 40)
f2 = fis.Triangle(30, 40, 50)

k1 = fis.Triangle(20, 30, 40)
k2 = fis.Triangle(30, 40, 50)

input1 = 49
input2 = 44

# rendah
r1 = min(f1.fuzzification(input1), k1.fuzzification(input2))
r2 = min(f1.fuzzification(input1), k2.fuzzification(input2))
r3 = min(f2.fuzzification(input1), k1.fuzzification(input2))
r = max(r1, r2, r3)

# tinggi
t = min(f2.fuzzification(input1), k2.fuzzification(input2))

defuzzi = fis.defuzzification([30, 70])
print defuzzi.sugeno([r, t])


