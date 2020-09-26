# Ramanujam numbers
# smallest number that can be expressed as sum of two cubes in two different ways
# e.g. 1729 = (1 ^ 3) + (12 ^ 3) = (9 ^ 3) + (10 ^ 3)
# Try all numbers one by one and check if it is a taxicab number. Use two nested loops To check if a number is Ramanujam number:
# In outer loop, calculate cube root of a number.
# In inner loop, check if there is a cube-root which yield the result. [solution fom geeksforgeeks]

N = int(input('How many Ramanujam numbers do you want to find out: '))

i, count = 1, 0
while (count < N):
    int_count = 0

    # Try all possible pairs (j, k)  whose cube sums can be i.
    for j in range(1, int(pow(i, 1.0 / 3)) + 1):

        for k in range(j + 1, int(pow(i, 1.0 / 3)) + 1):
            if (j * j * j + k * k * k == i):
                int_count += 1

    # Ramanujam number found
    if (int_count == 2):
        count += 1
        print(count, " ", i)

    i += 1