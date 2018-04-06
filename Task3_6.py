# Task3
y = 1988
if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
    print('NO')
else:
    print('YES')

# Task4
a, b, c = 3, 4, 5
if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")

# Task 5
q, w, e = 4, 5, 9
if q >= w >= e:
    print('q:' + str(q), 'w:' + str(w), 'e:' + str(e))
elif w >= q >= e:
    print('w:' + str(w), 'q:' + str(q), 'e:' + str(e))
elif e >= q >= w:
    print('e:' + str(e), 'q:' + str(q), 'w:' + str(w))
elif e >= w >= q:
    print('e:' + str(e), 'w:' + str(w), 'q:' + str(q))
elif w >= e >= q:
    print('w:' + str(w), 'e:' + str(e), 'q:' + str(q))
else:
    print('q:' + str(q), 'e:' + str(e), 'w:' + str(w))

# Task 6
z, x, c = 8, 8, 2
if z == x == c:
    print('3')
elif z == x != c or z == c != x or x == c != z:
    print('2')
else:
    print('0')
