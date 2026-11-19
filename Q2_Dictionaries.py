import copy

# Store Bus stops using tuple keys
stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T Nagar",
    (13.0674, 80.2376): "Kodambakkam",
}

print("Bus Stop:", stops[(13.0418, 80.2341)])

# Incorrect grid
rows, cols = 3, 4

bad = [[0] * cols] * rows
bad[0][1] = 7

print("Bad Grid:", bad)

# Correct grid
good = [[0 for _ in range(cols)] for _ in range(rows)]
good[0][1] = 7

print("Good Grid:", good)

# Aliasing and copying
original = [[1, 2], [3, 4]]

alias = original
shallow = copy.copy(original)
slice_copy = original[:]
deep = copy.deepcopy(original)

original[0][0] = 99
original[1][0] = 88

print("Original:", original)
print("Alias:", alias)
print("Shallow Copy:", shallow)
print("Slice Copy:", slice_copy)
print("Deep Copy:", deep)

print("Bad rows same:", bad[0] is bad[1])
print("Good rows same:", good[0] is good[1])