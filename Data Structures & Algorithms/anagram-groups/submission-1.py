class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)  # Dictionary that creates empty lists for new groups

        for s in strs:  # Go through each word

            count = [0] * 26  # Make 26 zeros, one for each letter a-z

            for c in s:  # Go through each letter in the word

                index = ord(c) - ord("a")  # Find the letter's position (a=0, b=1...)
                count[index] += 1  # Add 1 to that letter's counter

            res[tuple(count)].append(s)  # Put the word with words that have the same counts

        return list(res.values())  # Return all the groups
