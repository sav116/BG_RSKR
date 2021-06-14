file_1 = "C:\\Users\\Artem\\PycharmProjects\\BG_RSKR\\SPO\\10.19.88.1\\iis_log_findstr\\iisLog-20210415-0000(7_days)_Error.txt"

file_2 = "C:\\Users\\Artem\\PycharmProjects\\BG_RSKR\\SPO\\10.19.88.2\\iis_log_findstr\\iisLog-20210415-0000(7_days)_Error.txt"

file_3 = "C:\\Users\\Artem\\PycharmProjects\\BG_RSKR\\SPO\\10.19.88.5\\iis_log_findstr\\iisLog-20210415-0000(7_days)_Error.txt"
with open(file_3, encoding='UTF-16 LE') as f:
    errors = []
    for line in f:
        err = line.split(' ')[-4]
        if err not in errors:
            errors.append(err)
    print(errors)