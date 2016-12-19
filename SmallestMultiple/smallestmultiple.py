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
