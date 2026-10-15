class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        seen = {}  # Create an empty dictionary to store numbers and their indices

        for i in range(len(nums)):  # Go through each index in nums
            need = target - nums[i]  # Calculate the number needed to reach the target
            print(need)

            if need in seen:  # Check if we have already seen the number we need
                return [seen[need], i]  # Return the indices of both numbers

            seen[nums[i]] = i  # Store the current number and its index


          