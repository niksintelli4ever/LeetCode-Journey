class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        q=deque()
        l=0
        r=len(nums)-1
        while l<=r:
            if abs(nums[l])>=abs(nums[r]):
                q.appendleft(nums[l]*nums[l])
                l+=1
            else:
                q.appendleft(nums[r]*nums[r])
                r-=1
        
        return q
            
                