from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans = []
    n = len(nums)
    for i in range(n - 2):
        x = nums[i]
        if i > 0 and x == nums[i - 1]:  # 跳过重复数字
            continue
        if x + nums[i + 1] + nums[i + 2] > 0:  # 优化一
            break
        if x + nums[-2] + nums[-1] < 0:  # 优化二
            continue
        j = i + 1
        k = n - 1
        while j < k:
            s = x + nums[j] + nums[k]
            if s > 0:
                k -= 1
            elif s < 0:
                j += 1
            else:
                ans.append([x, nums[j], nums[k]])
                j += 1
                while j < k and nums[j] == nums[j - 1]:  # 跳过重复数字
                    j += 1
                k -= 1
                while k > j and nums[k] == nums[k + 1]:  # 跳过重复数字
                    k -= 1
    return ans

nums=[-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
print(threeSum(nums))