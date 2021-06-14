# ------------------------------------------------
# -*- coding: utf-8 -*-
# Script by Artem.S.
# Version   Date          Info
# 1.0       15/04/2021
# ------------------------------------------------

import docx, os, shutil, datetime, openpyxl
from settings.config  import ppo_d, spo_d


def parsing_log(file):
    #This function returns a description of the error
    #:param file: 'C:\Users\Artem\PycharmProjects\RSKR\PPO\10.19.88.2\MongoDB_findstr\MongoDB-20210415-0000(7_days)_Error.txt'
    #:return: 'ERROR:  syntax error at or near "as" at character 35 ... '
    errors=[]
    with open(file, encoding='utf-8') as f:
        for line in f:
            if 'error' in line.lower():
                start = line.find('ERROR')
            elif 'fatal' in line.lower():
                start = line.find('FATAL')
            elif '[Warning]' in line:
                start = line.find('[Warning]')
            errors.append(line[start:])
    return ''.join(errors)

def find_service_name(str):
    #This function returns service name from the string:
    #:param str: '\\PPO\\10.19.88.2\\MongoDB_findstr\\'
    #:return: 'MongoDB' or ''
    index1=None
    index2=None
    for i in range(len(str)):
        if index1 != None and index2 != None:
            return ' - '+ str[index1+2:index2].title() + '.'
        elif str[i].isdigit() and str[i+1] == '\\':
            index1=i
        elif str[i]=='_':
            index2=i
    return ''

def run_ppo():
    current_path = os.getcwd()
    doc_ppo=docx.Document()
    doc_ppo.add_heading('ППО', 0) # add tittle for type document
    for ip in ppo_d:
        doc_ppo.add_heading(ip + find_service_name(ppo_d[ip]), 1)
        if 'нет' in ppo_d[ip]:
            p = doc_ppo.add_paragraph(ppo_d[ip] + '\n')
            p.add_run().bold = True
        elif 'ошибки' in ppo_d[ip]:
            p = doc_ppo.add_paragraph(ppo_d[ip] + '\n')
            p.add_run().bold = True
        else:
            try:
                abs_path_to_err_log = current_path+ppo_d[ip]+os.listdir(current_path+ppo_d[ip])[0]
                if os.path.getsize(abs_path_to_err_log) > 0:  # select not empty files
                    p = doc_ppo.add_paragraph(parsing_log(abs_path_to_err_log) + '\n')
                    p.add_run().bold = True
                elif os.path.getsize(abs_path_to_err_log) == 0:
                    p = doc_ppo.add_paragraph('Ошибок не обнаружено' + '\n')
                    p.add_run().bold = True
            except:
                p = doc_ppo.add_paragraph('Лог файл не найден' + '\n')
                p.add_run().bold = True
    return doc_ppo


def get_discription_id(sheet, errors=None):
    print(errors)
    result = ''
    temp_dict = {}
    for error in errors:
        for row in range(2, sheet.max_row+1):
            id = str(sheet.cell(row=row, column=1).value)
            if ',' in id:
                id = [i.strip() for i in id.split(',')]
            if error in id:
                description = sheet.cell(row=row, column=2).value
                if description not in result:
                    result += f"EventID {id} - {description}\n"
                    break
    return result

def get_win_err_id(current_path, ip, sheet_id=None):
    win_app_log_file = current_path + spo_d[ip]['win_app'] + os.listdir(current_path + spo_d[ip]['win_app'])[0] # absolute path to log file win_app
    win_sys_log_file = current_path + spo_d[ip]['win_sys'] + os.listdir(current_path + spo_d[ip]['win_sys'])[0] # absolute path to log file win_sys
    temp_id_list = [] # list for unique id
    with open(win_app_log_file, encoding='UTF-16 LE') as f:
        for line in f:
            if 'EventID' in line:
                id = ''.join([i for i in line if i.isdigit()])
                if id not in temp_id_list:
                    temp_id_list.append(id)

    with open(win_sys_log_file, encoding='UTF-16 LE') as f:
        for line in f:
            if 'EventID' in line:
                id = ''.join([i for i in line if i.isdigit()])
                if id not in temp_id_list:
                    temp_id_list.append(id)

    if temp_id_list == []:
        return 'Ошибок не обнаружено'
    else:
        result = get_discription_id(sheet_id, temp_id_list)
        return result

def run_spo():
    now = datetime.datetime.now() # object datetime.datetime 2021-06-10 11:14:10.166054
    current_path = os.getcwd() # absolute path to scripts
    new_table = f"SPO_{now.day}_{now.month}_{now.year}.xlsx" # name for the new file
    shutil.copyfile(current_path+'\\settings\\table_default.xlsx', current_path + "\\" + new_table) # copy template table file from folder 'settings' like new SPO table
    tab_spo = openpyxl.load_workbook(filename=new_table)
    tab_id_bd = openpyxl.load_workbook(filename=f"settings\\event_id.xlsx")
    sheet_tab_spo = tab_spo.active # open active book in which we will write the results
    sheet_tab_id_bd = tab_id_bd.active # open active book of table with description by event id
    # iterate over all lines
    for row in range(2, 22):
        component = sheet_tab_spo.cell(row=row, column=5).value.lower() # cell value is equal to the lower case
        if 'window' in component:
            ip = sheet_tab_spo.cell(row=row, column=3).value.strip()
            sheet_tab_spo.cell(row=row, column=6).value = get_win_err_id(current_path, ip, sheet_tab_id_bd)
        #elif 'iis' in component:
         #   ip = sheet_tab_spo.cell(row=row, column=3).value.strip()


    tab_spo.save(new_table)

if __name__ == '__main__':
    # run PowerShell script and waiting when it stopped
    now = datetime.datetime.now()
    doc_ppo = run_ppo()
    doc_ppo.save(f'PPO_{now.day}_{now.month}_{now.year}.doc')
    doc_spo = run_spo()
    #doc_spo.save(f'PPO_{now.day}{now.month}{now.year}.doc')
    #tab_id_bd = openpyxl.load_workbook(filename=f"settings\\event_id.xlsx")
    #sheet_tab_id_bd = tab_id_bd.active  # open active book of table with description by event id
    #current_path = os.getcwd()
    #for ip in ['10.19.88.1', '10.19.88.2', '10.19.88.5', '10.19.88.6']:
    #get_err_id(current_path, '10.19.88.1', sheet_tab_id_bd)