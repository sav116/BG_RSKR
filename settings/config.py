ppo_d = {
    '10.19.88.1': 'На сервере нет бд',
    '10.19.88.2': '\\PPO\\10.19.88.2\\MongoDB_findstr\\',
    '10.19.88.3': '\\PPO\\10.19.88.3\\PostgreSQL_parsed\\',
    '10.19.88.4': '\\PPO\\10.19.88.4\\mysql_parsed\\',
    '10.19.88.5': 'На сервере нет бд',
    '10.19.88.6': 'На сервере нет бд',
    '10.19.88.7': '\\PPO\\10.19.88.7\\PostgreSQL_parsed\\',
    '10.19.88.8': '\\PPO\\10.19.88.8\\mysql_parsed\\',
    '10.19.88.10': 'Многочисленные ошибки',
    '10.19.88.11': 'На сервере нет бд',
    '10.19.88.12': '\\PPO\\10.19.88.12\\PostgreSQL_parsed\\'
}


spo_d = {
    '10.19.88.1':
        {
            'win_app': '\\SPO\\10.19.88.1\\win_application_log_findstr\\',
            'iis': '\\SPO\\10.19.88.1\\iis_log_findstr\\',
            'win_sys': '\\SPO\\10.19.88.1\\win_system_log_findstr\\'
        },
    '10.19.88.2':
        {
            'apache_tomcat': '\\SPO\\10.19.88.2\\ApacheTomcat_findstr\\',
            'iis': '\\SPO\\10.19.88.2\\iis_log_findstr\\',
            'win_app': '\\SPO\\10.19.88.2\\win_application_log_findstr\\',
            'win_sys': '\\SPO\\10.19.88.2\\win_system_log_findstr\\'
        },
    '10.19.88.3':
        {
            'red_hat': '\\SPO\\10.19.88.3\\1.RedHatEnterpriseLinux_parsed\\'
        },
    '10.19.88.4':
        {
            'httpd': '\\SPO\\10.19.88.4\\httpd_parsed\\',
            'red_hat': '\\SPO\\10.19.88.4\\RedHatEnterpriseLinux_parsed\\'
        },
    '10.19.88.5':
        {
            'win_app': '\\SPO\\10.19.88.5\\win_application_log_findstr\\',
            'iis': '\\SPO\\10.19.88.5\\iis_log_findstr\\',
            'win_sys': '\\SPO\\10.19.88.5\\win_system_log_findstr\\'
        },
    '10.19.88.6':
        {
            'apache_tomcat': '\\SPO\\10.19.88.6\\ApacheTomcat_findstr\\',
            'iis': '\\SPO\\10.19.88.6\\iis_log_findstr\\',
            'win_app': '\\SPO\\10.19.88.6\\win_application_log_findstr\\',
            'win_sys': '\\SPO\\10.19.88.6\\win_system_log_findstr\\'
        },
    '10.19.88.7':
        {
            'red_hat': '\\SPO\\10.19.88.7\\1.RedHatEnterpriseLinux_parsed\\'
        },
    '10.19.88.8':
        {
            'httpd': '\\SPO\\10.19.88.8\\httpd_parsed\\',
            'red_hat': '\\SPO\\10.19.88.8\\RedHatEnterpriseLinux_parsed\\'
        },
    '10.19.88.9':
        {
            'red_hat': '\\SPO\\10.19.88.9\\1.RedHatEnterpriseLinux_parsed\\'
        },
    '10.19.88.10':
        {
            'red_hat': '\\SPO\\10.19.88.10\\1.RedHatEnterpriseLinux_parsed\\'
        },
    '10.19.88.11':
        {
            'red_hat': '\\SPO\\10.19.88.11\\1.RedHatEnterpriseLinux_parsed\\'
        },
    '10.19.88.12':
        {
            'red_hat': '\\SPO\\10.19.88.12\\1.RedHatEnterpriseLinux_parsed\\'
        }

}

SERVER = {
    'RSKR-APP1P': {
        'ip': '10.19.88.1',
        'report_ppo': False,
        },
    'RSKR-BIP': {
        'ip': '10.19.88.2',
        'ppo': True,
        },
    'RSKR-P-DB': {
        'ip': '10.19.88.3',
        'report_ppo': True,
        },
    'RSKR-P-APP2': {
        'ip': '10.19.88.4',
        'ppo': True
        },
    'RSKR-APP1T': {
        'ip': '10.19.88.5',
        'ppo': True
        },
    'RSKR-BIT': {
        'ip': '10.19.88.6',
        'ppo': False
        },
    'RSKR-T-DB': {
        'ip': '10.19.88.7',
        'ppo': True
        },
    'RSKR-T-APP2': {
        'ip': '10.19.88.8',
        'ppo': True
        },
    'RSKR-OLAPP': {
        'ip': '10.19.88.9',
        'ppo': False
        },
    'RSKR-BI-DBP': {
        'ip': '10.19.88.10',
        'ppo': True
        },
    'RSKR-OLAPT': {
        'ip': '10.19.88.11',
        'ppo': False
        },
    'RSKR-BI-DBT': {
        'ip': '10.19.88.12',
        'ppo': True
        },
}