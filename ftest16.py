def reverseList(nums: list[int]) -> list[int]:
    rev = [0] * len(nums)

    j = 0

    for i in range(len(nums) - 1, -1, -1):
        rev[j] = nums[i]
        j += 1

    return rev


nums = [1, 2, 3, 4, 5]

result = reverseList(nums)

print(result)