class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        max_sum = max(nums)
        cur_sum = 0 
        
        for i in nums:
            
            cur_sum = cur_sum + i
            max_sum = max(max_sum, cur_sum)
            
            if cur_sum < 0:
                cur_sum = 0
                
        return max_sum
            
        