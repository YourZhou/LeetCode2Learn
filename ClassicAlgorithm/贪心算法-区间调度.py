from typing import List


def intervalSchedule(intvs: List[List[int]]) -> int:
    if len(intvs) == 0:
        return 0
    intvs.sort(key=lambda x: x[1])
    count = 1

    x_end = intvs[0][1]
    for interval in intvs:
        start = interval[0]
        if start>=x_end:
            count +=1
            x_end = interval[1]
        else:
            print(interval)
    return count

if __name__ == '__main__':
    intervalSchedule([[1,2],[2,3],[3,4],[1,3]])
