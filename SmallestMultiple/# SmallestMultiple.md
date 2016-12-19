# Smallest Multiple

Problem:

```
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
```

In order to select a starting point for calculation, 2521 is selected as it is a known point in the number range.

A counter is used to keep track the number of consecutive even divisible in the range. When the counter identified that 20 consecutive number has been reached, it will print the number to stdout.

A rough and ready version is as follows:

```
starting_number = 2521
for j in range(starting_number, 10000000000, 1):
    counter = 1
    for i in range(1, 21, 1):
        if j % i == 0:
            counter +=1
            if counter == 20:
                print j
                break
        else:
            break
```

The smallest multiple found is '232,792,560'