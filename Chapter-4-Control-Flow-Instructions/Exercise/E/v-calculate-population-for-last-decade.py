# Population of a town today is 100,000. Population increased steadily at the rate of 10% every year
# determine the population at the end of each year in the last decade
# If X is population of city in 9th year and Z is population in 10th year
# Population in 10th year, X + (10/100)X = Z
# => X + 0.1X = X(1+0.1) = 1.1X = Z
# => X = Z/1.1

population = 100000
n = 10
for i in range(1,10):
    population = int(population/1.1)
    print('Population in ', n-1,'th year = ', population)
    n = n - 1