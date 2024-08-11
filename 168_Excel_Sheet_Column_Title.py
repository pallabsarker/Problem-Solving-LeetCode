class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        output = ""
        while columnNumber > 0:
            rem = (columnNumber - 1) % 26
            output += chr(ord("A") + rem)
            columnNumber = (columnNumber - 1) // 26
        return output[::-1]
