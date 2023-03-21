from collections import OrderedDict


def subtitle2Dict(file_path):
    subtitle_dic = OrderedDict()
    subtitle_list = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f.readlines():  # readlines(),函数把所有的行都读取进来；
            line_file = line.strip()  # 删除行后的换行符，img_file 就是每行的内容啦
            # print(line_file)
            if line_file != '':
                subtitle_list.append(line_file)
    # print(subtitle_list[0][:2])
    i = 0
    sub_key = ""
    sub_value = ""
    while (i < len(subtitle_list) - 1):
        if subtitle_list[i][:2] == "Id":
            subtitle_dic[sub_key] = sub_value
            sub_key = ""
            sub_value = ""
            sub_key = subtitle_list[i]
        else:
            sub_value += subtitle_list[i]
        # subtitle_dic[subtitle_list[i]] = subtitle_list[i + 1]
        i += 1
    return subtitle_dic


if __name__ == '__main__':
    # file_path = r"D:\MyGames\Games\Tools\assassin-s-creed-localization-texts\工具\aclocalizationpackagetool\ac2text\0-LocalizationPackage_English_Subtitles.Localization_Package.txt"
    file_one_path = r"D:\MyGames\Games\Tools\assassin-s-creed-localization-texts\DataPC_ac2\aclocalizationpackagetool\sub_eng\0-LocalizationPackage_English_Subtitles.Localization_Package.txt"
    file_two_path = r"D:\MyGames\Games\Tools\assassin-s-creed-localization-texts\DataPC_ac2\aclocalizationpackagetool\sub_span\0-LocalizationPackage_Spanish_Subtitles.Localization_Package.txt"

    writeOutPath = r"D:\MyGames\Games\Tools\assassin-s-creed-localization-texts\DataPC_ac2\aclocalizationpackagetool\0-LocalizationPackage_EngSpa_Subtitles.Localization_Package.txt"

    subtitle_one_dic = subtitle2Dict(file_one_path)
    subtitle_two_dic = subtitle2Dict(file_two_path)

    print(len(subtitle_one_dic))
    print(len(subtitle_two_dic))

    Note = open(writeOutPath, mode='w', encoding="utf-8")
    k = 0
    for i in subtitle_one_dic:
        if i in subtitle_two_dic.keys():
            Note.write(i + '\n' + subtitle_two_dic[i] + '<br>' + subtitle_one_dic[i] + '\n\n')
            k += 1
    Note.close()
    print(k)
