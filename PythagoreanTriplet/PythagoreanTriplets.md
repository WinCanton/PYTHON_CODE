#Special Pythagorean Triplets

```
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
```

#Approach to Solution
The following approach is used:
- Although unlikely, the maximum for each variable to be is 1000. Therefore, iteration up to 1000 for each variable will be used
- Assign sqrt(a**2+b**2) to variable c
- Check if a + b + c = 1000
- If so, calculate a * b * c

# The Solution

Math python library needs to be imported in order to use `sqrt()' function.

```python
import math

for a in range(1,1000,1):
    for b in range(1,1000,1):
        c = math.sqrt(a**2+b**2)
        if a + b +c == 1000:
            print a, b, c
            print a * b * c
        else:
            pass
```

The output shows:

```
200 375 425.0
31875000.0
375 200 425.0
31875000.0
[Finished in 0.9s]
```

It displays two possible answers, which actually centres around the same solution:

a (or b) = 200
b (or a) = 375
c = 425

And the product of abc = `31875000`