class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        length = len(s)
        roman = romanMap.keys()
        for i in range(len(s)):
            value = romanMap[s[i]]
            if i+1<length and value<romanMap[s[i+1]]:
                result -= value
            else:
                result += value
        return result

            


        
        