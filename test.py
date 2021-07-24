# file_1 = "C:\\Users\\Artem\\PycharmProjects\\BG_RSKR\\SPO\\10.19.88.1\\iis_log_findstr\\iisLog-20210415-0000(7_days)_Error.txt"
#
# file_2 = "C:\\Users\\Artem\\PycharmProjects\\BG_RSKR\\SPO\\10.19.88.2\\iis_log_findstr\\iisLog-20210415-0000(7_days)_Error.txt"
#
# file_3 = "C:\\Users\\Artem\\PycharmProjects\\BG_RSKR\\SPO\\10.19.88.5\\iis_log_findstr\\iisLog-20210415-0000(7_days)_Error.txt"
#
# file_4 = "C:\\Users\\Artem\\PycharmProjects\\BG_RSKR\\SPO\\10.19.88.6\\iis_log_findstr\\iisLog-20210415-0000(7_days)_Error.txt"
#
# logs_list = [file_1, file_2, file_3, file_4]
#
# errors = []
#
# for log_file in logs_list:
#     with open(log_file, encoding='UTF-16 LE') as f:
#
#         for line in f:
#             err = line.split(' ')[-4]
#             if err not in errors:
#                 errors.append(err)
#
# print(errors)
#
import datetime
import openpyxl


def show_value_cell(row, colunm):
    now = datetime.datetime.now()
    new_table = f"SPO_{now.day}_{now.month}_{now.year}.xlsx"
    tab_spo = openpyxl.load_workbook(filename=new_table)
    sheet_tab_spo = tab_spo.active
    cell_value = sheet_tab_spo.cell(row=row, column=colunm).value
    print(cell_value)
    print(type(cell_value))

show_value_cell(row=2,colunm=3)