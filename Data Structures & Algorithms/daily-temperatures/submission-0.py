class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # Stores indices
        result = [0] * len(temperatures) # Default value

        for i, current_val in enumerate(temperatures):
            while stack and current_val > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
                
            stack.append(i) # Push current index
            
        return result