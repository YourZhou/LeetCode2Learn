class Solution:
    def replaceSpace(self, s: str) -> str:
        s_split = s.split(' ')
        s_result = ""
        for i in s_split[:-1]:
            s_result += i
            s_result += "%20"
        s_result += s_split[-1]
        return s_result


if __name__ == '__main__':
    s = "We are happy."
    solution = Solution()
    print(solution.replaceSpace(s))
