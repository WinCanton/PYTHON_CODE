from __future__ import division
numbers = range(100000)
primefactors = []
for number in numbers:
    for i in range(2, number+1, 1):
        if number % i != 0:
            pass
        else:
            if number == i:
                primefactors.append(number)
            else:
                break

def prifac(number):
    pf = []
    for factor in primefactors:
        if number % factor == 0:
            pf.append(factor)
            y = 1
            for i in range(len(pf)):
                y = y * pf[i]
                if number == y:
                    break
                else:
                    pass
    return pf

factors = prifac(600851475143)
print("The prime factors of %d are: ", factors)
print("The largest prime factors: ", max(factors))