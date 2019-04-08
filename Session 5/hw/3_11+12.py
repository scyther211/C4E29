def is_inside(m,n):
    x = m[0]
    y = m[1]
    a = n[0]
    b = n[1]
    c = n[2]
    d = n[3]
    if a <= x <= a + c and b <= y <= b + d:
        return True
    else:
        return False

inside = is_inside([200, 120], [140, 60, 100, 200])
inside1 = is_inside([100, 120], [140, 60, 100, 200])
if inside == True and inside1 == False:
    print("Your function is correct")
else:
    print("Oops, there's a bug")



