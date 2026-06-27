def palind(r):
    e = len(r) -1
    s = 0
    while (s<e):
        if (r[s]!= r[e]):
            return False
        s += 1
        e -= 1
    return True

r = (5,6,7,7,6,5,8)

if palind(r):
    print("The tuple is Flip-Flop")
else:
    print("The tuple is not Flip-Flop")

    