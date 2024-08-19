List = list
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        output = [[1]]
        for i in range(numRows - 1):
            init = [0] + output[-1] + [0]
            element = []
            
            for j in range(len(output[-1]) + 1):
                element.append(init[j] + init[j + 1])
            output.append(element)
        return output
    
print(Solution().generate(5))
