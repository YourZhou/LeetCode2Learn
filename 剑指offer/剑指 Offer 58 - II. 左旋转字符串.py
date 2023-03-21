class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        if s == "": return s
        s_left, s_right = s[:n], s[n:]
        return s_right + s_left


if __name__ == '__main__':
    s = "abcdefg"
    solution = Solution()
    print(solution.reverseLeftWords(s, 2))
