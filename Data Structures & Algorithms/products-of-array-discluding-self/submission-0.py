class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        pre, post = 1, 1
        for num in nums:
            ans.append(pre)
            pre *= num
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= post
            post *= nums[i]
        return ans