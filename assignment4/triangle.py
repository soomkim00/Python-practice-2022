def det_triangle(a, b, c):
    tri = [a, b, c]
    tri.sort()
    if tri[2]**2 > tri[1]**2 + tri[0]**2:
        print("obtuse")
    elif tri[2]**2 == tri[1]**2 + tri[0]**2:
        print("right")
    else:
        print("acute")


A, B, C = map(int, input().split())
det_triangle(A, B, C)
