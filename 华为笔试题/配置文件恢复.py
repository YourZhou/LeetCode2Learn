while True:
    try:
        lis = list(input().split())
        print(lis)
        if lis[0][0] == 'r':
            if lis[0] in "reset":
                print('ok1')
                try:
                    if lis[1] is not None:
                        print('ok2')
                        if lis[1] in "board":
                            print("board fault")
                        else:
                            print("unkown command")
                except:
                    print("reset what")
            elif lis[0] in "reboot":
                if lis[1] is not None:
                    if lis[1] in "backplane":
                        print("impossible")
                    else:
                        print("unkown command")
                else:
                    print("unkown command")
            else:
                print("unkown command")
        elif lis[0][0] == 'b':
            if lis[0] in "board":
                try:
                    if lis[1] is not None:
                        if lis[1] in "add":
                            print("where to add")
                        elif lis[1] in "delet":
                            print("no board at all")
                        else:
                            print("unkown command")
                except:
                    print("unkown command")
            elif lis[0] in "backplane":
                if lis[1] is not None:
                    if lis[1] in "abort":
                        print("install first")
                    else:
                        print("unkown command")
                else:
                    print("unkown command")
            else:
                print("unkown command")
        else:
            print("unkown command")
    except:
        break
