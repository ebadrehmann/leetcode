class Solution(object):
    def dailyTemperatures(self, temperatures):
        ret = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                l = stack.pop()
                ret[l] = i - l

            stack.append(i)
        return ret        