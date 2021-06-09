# ------------------------------------------------
# -*- coding: utf-8 -*-
# Script by Artem.S.
# Version   Date          Info
# 1.0       15/04/2021
# ------------------------------------------------

import docx, os, time, shutil, datetime, openpyxl
from settings.config  import SERVER, ppo_d, spo_d


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

# def run_spo():
#     current_path = os.getcwd()
#     default_table = current_path + '\\table_default.xlsx'
#     for p in doc_spo.tables[0]:
#         print(p)

if __name__ == '__main__':
    # run PowerShell script and waiting when it stopped
    now = datetime.datetime.now()
    doc_ppo = run_ppo()
    doc_ppo.save(f'PPO_{now.day}{now.month}{now.year}.doc')
    #doc_spo = run_spo()
    #doc_spo.save(f'PPO_{now.day}{now.month}{now.year}.doc')