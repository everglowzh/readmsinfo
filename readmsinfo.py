import csv

USR_INFO = []
# csv.register_dialect('tabs', delimiter='\t')

def create_csv(msinfo):
    with open(msinfo, 'r', encoding='utf_16') as msinfo_file:
        lines = msinfo_file.readlines()
        with open('userinfo.txt', 'a', encoding='utf_8') as userinfo:
            for line in lines:
                userinfo.write(line)
        userinfo.close()
    msinfo_file.close()
    with open('userinfo.txt', 'r', encoding='utf_8') as userinfo:
        new_lines = userinfo.readlines()
        for new_line in new_lines:
            USR_INFO.append(new_line.split('\t'))
    userinfo.close()
    with open('userinfo.csv', 'w', errors='ignore', newline='') as userinfo_csv:
        # dialect = csv.get_dialect('tabs')
        writer = csv.writer(userinfo_csv)
        for usr_info in USR_INFO:
            writer.writerow(usr_info)

    return


if __name__ == '__main__':
    # print(csv.list_dialects())
    msinfo = 'msinfo.txt'
    create_csv(msinfo)
    # print(USR_INFO)