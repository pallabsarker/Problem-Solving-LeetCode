List = list
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex += 1
        output = [[1]]
        for i in range(2, rowIndex + 1):
            element = [1]
            for j in range(1, i - 1):
                element.append(output[-1][j] + output[-1][j- 1])
            element.append(1)
            output.append(element)
        return output[-1]

print(Solution().getRow(3))


# List = list
# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
        
#         output = [1]
#         for i in range(rowIndex):
#             line = [0] * (len(output) + 1)
#             for j in range(len(output)):
#                 line[j] += output[j]
#                 line[j + 1] = output[j]
#             output = line
#         return output
    
# print(Solution().getRow(4))
