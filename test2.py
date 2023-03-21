path = r"D:\MyGames\Games\Tools\assassin-s-creed-localization-texts\DataPC_ac2\aclocalizationpackagetool\0-LocalizationPackage_English_Subtitles.Localization_Package.txt.header"
f = open(path, "rb")  # 打开要读取的十六进制文件
strs = f.read()
print(strs)
print(strs.decode())
# hex_list = ["{:02X}".format(int(c)) for c in f.read()]  # 定义变量接受文件内容
# print(hex_list)
# data_mes = bytes().fromhex(hex_list).decode('gb18030',"ignore")  # 将十六进制转为字符信息方法
# f.close()  # 关闭文件 好习惯！
# buflist = list(hex_list)  # 用列表保存信息，方便后续操作
# print(buflist)
# index_num = '{:d}'.format(int(('0x' + ''.join(buflist[12:16])), 16))  # 此处提取想要的文本信息
# print(index_num)


