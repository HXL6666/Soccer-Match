# -*- coding : utf-8 -*-
import xlwt

workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet("NO.1")
# 乘法表1
for i in range(0, 9):
    for j in range(0, 9):
        if 9 - j > i:
            t = (9 - i) * (j + 1)
            worksheet.write(j, i, "{} * {} = {}".format(9 - i, j + 1, t))
workbook.save("spider.xls")

# 乘法表2
for i in range(0, 9):
    for j in range(11, 20):
        if j - 10 >= i + 1:
            t = (i + 1) * (j - 10)
            worksheet.write(j, i, "{} * {} = {}".format(i + 1, j - 10, t))
workbook.save("spider.xls")

# 乘法表3
for i in range(0, 9):
    for j in range(22, i+23):
        t = (i + 1) * (j - 21)
        worksheet.write(j, i, "{} * {} = {}".format(j - 21, i + 1, t))
workbook.save("spider.xls")

# 乘法表34
for i in range(0, 9):
    for j in range(34, i+35):
        t = (i + 1) * (j - 33)
        worksheet.write(75 - j, i, "%d * %d = %2d"%(j-33, i+1, t))
workbook.save("spider.xls")