# Largest Palindrome Number

Below is another problem to solve from project [euler](http://www.projecteuler.net):

```
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
```

The idea for solution is simple:
1. If a number is the same as its reverse, the number is palindromic.
2. As the question is about the largest palindromic can be formed by a product of two 3-digit numbers, the numbers to iterate for the multiplication should start from a minimum of 3 digit numbers, which is 100 and end at the maximum, which is 999.
3. Conversion from integer to string and back to integer is a play here in order to allow the use of list and max() function.

The solution therefore looks as follows:

```python
palinlist = []
for i in range(100, 999, 1):
    for j in range(100, 999, 1):
        x = str(i * j)
        if x == x [::-1]:
            palinlist.append(int(x))
        else:
            pass

print max(palinlist)
```

When executed, the code shows the following result:

```
906609
[Finished in 0.8s]
```