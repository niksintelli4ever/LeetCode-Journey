class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        q=deque()
        while l<=r:
            ls=nums[l]*nums[l]
            rs=nums[r]*nums[r]
            
            if ls>rs:
                q.appendleft(ls)
                l+=1
            else:
                q.appendleft(rs)
                r-=1
            
        return q
                
        