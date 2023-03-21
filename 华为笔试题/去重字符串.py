# 去除重复数
if __name__ == '__main__':
    string = input("输入数据是一个字符串（不包含空格）")
    # final_str = set(string)
    # print(final_str)

    final_str = ""
    for i in string:
        if i not in final_str:
            final_str += i
    print(final_str)