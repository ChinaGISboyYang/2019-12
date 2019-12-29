# coding = utf-8
import os
import xlwt


def readTxt_toExcel(value_list_1, value_list_2):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('data_process_out', cell_overwrite_ok=True)  # Excel单元格名字
    # style = xlwt.XFStyle()
    title = ["ID", "time", "lon", "lat"]

    '''写入title 信息'''
    col = 0  # 控制列
    for head in title:
        sheet.write(0, col, head)
        col += 1
    '''写入 value值'''
    hang = 1
    for i in value_list_1:
        lie = 0
        for value in i:
            sheet.write(hang, lie, value)
            lie += 1
        hang += 1

    for i in value_list_2:
        lie = 0
        for value in i:
            sheet.write(hang, lie, value)
            lie += 1
        hang += 1

    workbook.save("./data_process_out.xls")


max_lon1 = 22.23232
max_lat1 = 114.1111
min_lon1 = 21.1111
min_lat1 = 111.1111

max_lon2 = 23.23232
max_lat2 = 112.1111
min_lon2 = 22.1111
min_lat2 = 110.1111


def get_txt_content(file_path):  # 获取文件内容
    value_list_1 = []  # value 列表
    value_list_2 = []  # value 列表
    num = 1
    for path, d, file_list in os.walk(file_path):  # path原路径下的文件遍历    flie_list 文件下的所有文件
        # print(path)
        for filename in file_list:
            if filename.endswith(".txt"):
                with open(path + '/' + filename, 'r', encoding="utf-8") as f:  # 打开文件 文本的全部路径
                    items = f.readlines()  # 读取文件，列表格式

                    # print(items_01)
                    # print(value_list_1)
                    for value in items[2:]:
                        value_list = value.split()
                        lon = float(value_list[0])
                        lat = float(value_list[1])
                        if min_lat1 <= lon <= max_lat1 and min_lon1 <= lat <= max_lon1:
                            value_list_1.append(lon)
                            value_list_1.append(lat)
                            items_01 = items[0].split()
                        elif min_lat2 <= lon <= max_lat2 and min_lon2 <= lat <= max_lon2:
                            value_list_2.append(lon)
                            value_list_2.append(lat)
                            items_01 = items[0].split()
                    # print(valueList)
                    num += 1
                    print("已处理文件：" + str(num))
                    readTxt_toExcel(value_list_1, value_list_2)  # 处理txt文件


def main():
    file_path = "./20170611"
    get_txt_content(file_path)


if __name__ == '__main__':
    main()
