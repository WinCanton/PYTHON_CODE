def threeSum(nums):
    solution_set = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    solution_set.append([nums[i], nums[j], nums[k]])
    print(solution_set)
    x = True
    while x:
        for i in range(len(solution_set)):
            for j in range(i+1, len(solution_set)):
                if set(solution_set[i]) == set(solution_set[j]):
                    solution_set.remove(solution_set[i])
                    break
                break
            if i == len(solution_set):
                x = False
                break
    return 