nums = [2, 7, 11, 15]
target = 9

sv = {}

for i in range(len(nums)):
    difference = target - nums[i]
    if difference in sv:
        print([sv[difference],i])
        break

    sv[nums[i]] = i