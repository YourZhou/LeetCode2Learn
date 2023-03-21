import sys
import collections

while True:
    try:
        filedic = collections.OrderedDict()
        while True:
            inFile = str(input())
            if not inFile:
                break
            if inFile not in filedic:
                filedic[inFile] = 1
            else:
                filedic[inFile] += 1
        i = 0
        for k, v in sorted(filedic.items(), key=lambda k: k[1], reverse=True):
            outpath, outlis = str(k).split('\\')[-1].split(' ')
            if len(outpath) > 16:
                outpath = outpath[-16:]
            print(outpath, outlis, v)
            i += 1
            if i == 8:
                break
        # print(filedic)

    except:
        break
