
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:

#         n = len(nums)
#         output = []

#         for i in range(n):
#             product = 1

#             for j in range(n):
        
#                 if i!=j:
#                     product *= nums[j]

#             output.append(product)
    
#         return output




class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = [1] * n

        # FIRST LOOP: Go forward
        left = 1

        for i in range(n):
            answer[i] = left
            left = left * nums[i]

        # SECOND LOOP: Go backward
        right = 1

        for i in reversed(range(n)):
            answer[i] = answer[i] * right
            right = right * nums[i]

        return answer
