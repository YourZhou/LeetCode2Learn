import sys

if __name__ == '__main__':
    res = str(sys.stdin.readline.strip())
    fin = ''
    for i in res:
        if i not in fin:
            fin+=i
    print(fin)