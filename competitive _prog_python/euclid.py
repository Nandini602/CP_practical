def euclids_algorithm(A, B):
    x1, y1, x2, y2 = 1, 0, 0, 1

    while B != 0:
        quotient = A // B
        remainder = A % B

        x = x1 - quotient * x2
        y = y1 - quotient * y2

        A = B
        B = remainder

        x1 = x2
        y1 = y2
        x2 = x
        y2 = y

    return [x1, y1, A]


A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))

result = euclids_algorithm(A, B)

print("X:", result[0])
print("Y:", result[1])
print("D:", result[2])