import math
i = 0
while i <= 345:
    rads = (i * math.pi)/180
    print("The value of sin", i, "degrees is", math.sin(rads))
    print("The value of cos", i, "degrees is", math.cos(rads))
    i += 15