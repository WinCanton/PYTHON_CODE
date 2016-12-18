# Finding the Maximum Prime Factor

Project Euler (http://www.projecteuler.net) has a variety of intriguing problems to solve for people with computer and some time to spare. One of the problems is finding the maximum prime factor of a number.

The problem goes like this:

```
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
```

My solution to this problem consists of the utilisation of two routines: 
1. Generate Prime Factors
2. Finding Prime Factors for the `number` in question.

The first routine goes as follows:

```
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
```

The output produced is a list of prime factors between 1 and 100,000. It takes quite sometime to produce this output on my 3 years old mac computer. 

The second takes a number and find all of its  prime factors, utilising the output produced by the first routine. 

```
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
```

The following code invokes the prifac function:

```
factors = prifac(600851475143)
print("The prime factors of %d are: ", factors)
print("The largest prime factors: ", max(factors))

```

which then produces the following output:

```
('The prime factors of %d are: ', [71, 839, 1471, 6857])
('The largest prime factors: ', 6857)
[Finished in 157.0s]
```
