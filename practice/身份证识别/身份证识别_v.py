#!/usr/bin/python3
# coding=utf-8

import re


def idarea():
    stream = open(r'F:\python\实践\身份证地址码', 'rb')
    idlist = {}
    for line in stream.readlines():
        rule = re.compile(r'\S+')
        res = re.findall(rule, line.decode('utf-8'))
        idlist[res[0]] = res[1]
    return idlist


def idparse(id):
    code_prov = id[0:2]
    code_city = id[2:4]
    code_county = id[4:6]
    code_year = id[6:10]
    code_month = id[10:12]
    code_day = id[12:14]
    code_sex = id[14:17]
    code_crc = id[17:18]

    idict = idarea()
    try:
        prov = idict[code_prov + "0000"]
        city = idict[code_prov + code_city + "00"]
        county = idict[code_prov + code_city + code_county]
        birth = (code_year, code_month, code_day)
        sex = ["女", "男"][int(code_sex) % 2]
        crc = id_check(id)
    except Exception as e:
        return str(e)

    return (prov, city, county, birth, sex, crc,)


def id_check(id):
    serial = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    sum = 0
    for n in range(len(id) - 1):
        if n < 17:
            sum = sum + int(id[n]) * serial[n]
        else:
            break
    result = (12 - (sum % 11)) % 11
    if result == 10:
        crc = "X"
    else:
        crc = result
    if int(id[17]) == crc:
        res = True
    else:
        res = False
    return res


def main(ID):
    if len(id) != 18 and len(id) != 15:
        print("非法身份证号码, 请核对")
        exit(1)
    elif len(id) == 15:
        print("暂不支持15位身份证查询")
        exit(2)
    info = idparse(ID)
    print("居民信息")
    print("省    : %s" % info[0])
    print("市/区 : %s" % info[1])
    print("县    : %s" % info[2])
    print("出生  : %s年%s月%s日" % info[3])
    print("性别  : %s" % info[4])
    print("合法性: %s" % info[5])


id = str(input("请输入身份证号码: \n"))

# mod = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# end = (1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2)
if __name__ == '__main__':
    main(id)
