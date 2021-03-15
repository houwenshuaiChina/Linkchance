import pandas as pd
import numpy as np

'''
    连接数据库
    args：db_name（数据库名称）
    returns:db
'''

def mysql_link(de_name):
    try:
        db = pymysql.connect(host="127.0.0.1", user="xxx", passwd="xxx", db=xxx, charset='utf8')
        return db
    except:
        print("could not connect to mysql server")

'''
    读取csv函数
    args：csv_file（excel文件，目录在py文件同目录）
    returns：book
'''

def read_csv(csv_file):
    try:
        df_csv=pd.read_csv(csv_file,sep='\t',encoding="utf-8")
        print(type(df_csv))
        return df_csv
    except:
        print("open csv file failed!")

def write_excel(excel_file,df_toexcel):
    try:
        df_toexcel.to_excel(excel_file,sheet_name='sheet1')
        print(excel_file)
        # return excel_file
    except:
        print("write excel file failed!")
    finally:
        pass
        # excel_file.save()
#
#
# '''
#     读取excel函数
#     args：excel_file（excel文件，目录在py文件同目录）
#     returns：book
# '''
#
# def open_excel(excel_file):
#     try:
#         book = xlrd.open_workbook(excel_file)  # 文件名，把文件与py文件放在同一目录下
#         print(sys.getsizeof(book))
#         return book
#     except:
#         print("open excel file failed!")


if __name__ == '__main__':
    # store_to("Linkchance", 'AMA_AllPayments', r'C:\Users\Administrator\Desktop\20211月MonthlyUnifiedTransaction (1).csv')
    # mysql_link("Linkchance")
    # read_csv(r'C:\Users\Administrator\Desktop\test_NA_US-20210101-20210131.txt')
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
    print(dict['Name'])  # 删除键是'Name'的条目
    print(dict)  # 删除键是'Name'的条目



    dfbook=read_csv(r'D:\Users\Python\PythonProjects\Linkchance\test_NA_US-20210101-20210131.txt')
    print(dfbook)
    to_excel_name='test_abc.xlsx'
    write_excel('test_abc.xlsx',dfbook)
