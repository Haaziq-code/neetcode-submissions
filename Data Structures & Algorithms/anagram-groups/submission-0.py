
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Maps each letter-count pattern to its group of anagrams
        res = defaultdict(list) # this creates a dictionary that stores the groups

        for s in strs:
            # 26 counters representing a through z
            count = [0] * 26

            for c in s:
                # Finds the letter's index:
                # a = 0, b = 1, c = 2, ..., z = 25
                index = ord(c) - ord("a")
                count[index] += 1

            # Words with the same counts use the same dictionary key
            res[tuple(count)].append(s)

        return list(res.values())

        # Time complexity: O(m * n)
