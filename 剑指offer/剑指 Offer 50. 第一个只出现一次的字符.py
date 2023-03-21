import collections


class Solution:
    # def firstUniqChar(self, s: str) -> str:
    #     if s == "": return ""
    #     s_list = list(s)
    #     s_list.sort()
    #     print(s_list)
    #     a = ""
    #     b = 0
    #     for i in s_list:
    #         if i == a:
    #             b += 1
    #         else:
    #             if b == 1:
    #                 return a
    #             a = i
    #             b = 1
    #     return None

    # def firstUniqChar(self, s: str) -> str:
    #     if s == "": return " "
    #     s_list = list(s)
    #     for i in s_list:
    #         if s_list.count(i) == 1:
    #             return i
    #     return " "

    def firstUniqChar(self, s: str) -> str:
        cont = collections.Counter(s)
        for i, count in enumerate(cont):
            if cont[count] == 1:
                return count
        return ' '


if __name__ == '__main__':
    s = "abaccdeff"
    solution = Solution()
    print(solution.firstUniqChar(s))
