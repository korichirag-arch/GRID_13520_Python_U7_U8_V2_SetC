import numpy as np
print("\n")
print("SECTION C - NUMPY \n")
print("Q7. Creating arrays and slicing. \n")

print("1st question. ")
# 1. Create a = np.arange(0, 101, 10) and print it.
a = np.arange(0, 101, 10)
print(a)

print("\n2nd question. ")
# 2. Create an array of zeros with shape (4, 2) and an array of ones with shape (2, 4) (dtype=float).
#    Print the two shapes and the sum of the ones array on one line.
zeros_arr = np.zeros((4, 2))
ones_arr = np.ones((2, 4), dtype=float)
print(zeros_arr.shape, ones_arr.shape, ones_arr.sum())
print("\n3rd question. ")
# 3. Print np.eye(3) multiplied by 3.
print(np.eye(3) * 3)

print("\n4th question. ")
# 4. Create lin = np.linspace(0, 10, 50) and print its length, lin[1] rounded to 4 decimals,
#    and its last value on one line (use float()).
lin = np.linspace(0, 10, 50)
print(len(lin), round(float(lin[1]), 4), float(lin[-1]))

print("\n5th question. ")
# 5. Call np.random.seed(11) and create r = np.random.randint(1, 21, size=(4, 4)).
#    Print r; replace its first row with 100 and print that row;
#    then print the bottom-right 2 x 2 block (r[-2:, -2:]).
np.random.seed(11)
r = np.random.randint(1, 21, size=(4, 4))
print(r)

r[0] = 100
print(r[0])
print(r[-2:, -2:])


print("Q8. Boolean masks, np.where and views. \n")

# 1. Ages masking
ages = np.array([21, 34, 17, 29, 45, 16, 38])
print(ages[ages >= 18])
print(ages[(ages > 22) & (ages < 40)])
print(ages[~(ages >= 18)])

# 2. np.where for Pass/Fail
scores = np.array([82, 64, 77, 91, 58, 70])
print(np.where(scores >= 65, "Pass", "Fail"))

# 3. Mask update and count
temps = np.array([24, 38, 33, 41, 29, 36])
mask = temps > 35
temps[mask] = 36
print(temps, int(mask.sum()))

# 4. Slicing rows 1-3 and columns 2-4
mat = np.arange(6, 31).reshape(5, 5)
print(mat[1:4, 2:5])

# 5. View vs Copy
view = mat[0]
view[0] = 99
print(mat[0, 0])

copy = mat[1].copy()
copy[0] = -1
print(mat[1, 0])
# Modifying a view modifies the original array data because they share the same memory buffer,
# whereas modifying an independent copy leaves the original array unchanged.


print("Q9. Array maths and statistics. \n")

