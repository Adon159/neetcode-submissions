class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dicts , dictt= {} , {}
        for idx in range(len(s)):
            dicts[s[idx]] = 1 + dicts.get(s[idx], 0)
            dictt[t[idx]] = 1 + dictt.get(t[idx], 0)

        for char in dicts:
            if dicts[char] != dictt.get(char, 0):
                return False

        return True
