# SumSquare Difference

```
The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385 The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 552 = 3025 Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
```

The problem is about finding the difference between the sum squares and the square of the sum, of the first 100 natural numbers.

The first 100 natural numbers can be done easily as follows:

```python
numbers = range(1,101,1)
```

To calculate the difference, a python built-in function sum() is used:

```python
diff = sum(numbers)**2 - sum([x*x for x in numbers])
```

producing the following output:

```
25164150
[Finished in 0.2s]
```