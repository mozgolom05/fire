#1 задание с Leetcode

nums = [3, 5, 76, 12, 4]
target = 8
"""
num_d = {}
l = []
for i, j in enumerate(nums):
    num_d[i] = j
    if target - j in nums:
        if i!=nums.index(target - j):
            l.append((i, nums.index(target - j)))
print(l)
"""
num_d = {}
        for i, j in enumerate(nums):
            if target - j in num_d:
                return [num_d[target - j], i]
            num_d[j] = i
