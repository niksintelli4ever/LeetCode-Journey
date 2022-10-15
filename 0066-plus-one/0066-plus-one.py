class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        index=0
        digits=digits[::-1]
        while carry:
            if index<len(digits):
                if digits[index]==9:
                    digits[index]=0
                else:
                    digits[index]+=1
                    carry=0
            else:
                digits.append(1)
                carry=0
            index+=1
        return digits[::-1]
                
                
                    
        