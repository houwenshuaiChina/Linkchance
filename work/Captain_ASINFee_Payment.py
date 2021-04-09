# -*- coding:utf-8 -*-
import os
import sys
import re
import pandas as pd
import numpy as np
import datetime

common_dir = './common'
data_dir = './data'
operators_file = 'Amazon_operators.xlsx'
df_ASINFeePayment_original = pd.DataFrame()
df_ASINFeePayment_benchmark = pd.DataFrame()
df_operators = pd.DataFrame()
# dict_operators = {}

report_date = ''

currency_sign = {"US":"USD","UK":"GBP","CA":"CAD","AU":"AUD","DE":"EUR","JP":"JPY"}
exchange_rate = {"USD":1,"GBP":1.28,"CAD":0.744,"AUD":0.685,"EUR":1.15,"JPY":0.00936}
# exchange_rate = {"US":1,"UK":1.28,"CA":0.744,"AU":0.685,"DE":1.15,"JP":0.00936}

replace_columns = ['销售总额', '退款', '亚马逊销售佣金', 'FBA代发货费用', '多渠道配送费', '退款扣除佣金', 'FBA退货处理费',
                   '返还亚马逊销售佣金', 'FBA月仓储费用', '其他', 'promote折扣', '退款返还promote折扣', 'CPC直接商品销售额',
                   'CPC花费', '采购成本', '物流/头程', '运营费用', 'VAT', '结算费', '返还运费', '测评费用', '毛利润']
float_columns = ['销售量', '退款量', '多渠道数量', 'CPC直接销量']
percentage_columns = ['退款率', '亚马逊费用占比', 'CPC直接销量占比', 'CPC花费占比', '成本/物流费用占比', '运营费用占比', '测评费用占比', '毛利率']
digit_columns = replace_columns + float_columns + percentage_columns

#重命名并提取csv文件
def rename_csv(dir_args):
    try:
        # data_dir = '.\data'
        dir_list = os.listdir(dir_args)  # 列出文件夹下所有的目录与文件
        rename_count = 0  # 重命名的文件数量

        for i in range(0, len(dir_list)):
            csv_dir = os.path.join(dir_args, dir_list[i])
            if os.path.isdir(csv_dir):
                csv_file_list = os.listdir(csv_dir)  # 列出文件夹下所有的目录与文件
                for csv_file in  csv_file_list:

                    csv_file_path = os.path.join(csv_dir, csv_file)
                    if os.path.isfile(csv_file_path):
                        # os.rename(csvpath, os.path.join(csv_dir, data_dir_list[i]) + '.csv')  # 在原来目录中重命名csv文件
                        os.rename(csv_file_path, csv_dir + '.csv')  # 重命名csv文件并移动到./data目录中
                        rename_count += 1
        print('csv文件：总共重命名了 ' + str(rename_count) + ' 个文件！')
    except:
        print('Rename_csv error！')

#遍历所有的csv并返回DataFrame
def open_csv(dir_args):

    df_ASINFee_Payment = pd.DataFrame()
    try:
        file_list = os.listdir(dir_args)  # 列出文件夹下所有的目录与文件

        for file in file_list:
            csv_file = os.path.join(dir_args,file)
            if os.path.isfile(csv_file) and csv_file[-3:]=='csv':
                df_dict = pd.read_csv(csv_file,sep=',',encoding='utf-8')

                # df_dict['商品名称'] = ''
                df_dict['store_Name'] = file[:10]
                df_dict['Period'] = file[-21:].replace('.csv','')
                df_dict['currency_Sign'] = currency_sign[file[:10][-2:]]
                df_dict['exchange_Rate'] = df_dict['currency_Sign'].map(exchange_rate)

                df_frames = [df_ASINFee_Payment,df_dict]
                df_ASINFee_Payment = pd.concat(df_frames)

        return df_ASINFee_Payment
    except:
        print("open csv file failed!")


#替换数据中的货币符号
def replace_currency_sign(df_args):

    # Index(['SKU', '商品名称', 'ASIN', '父asin', '发货类型', '销售总额', '销售量', '多渠道数量', '退款量', '退款率',
    #        '退款', '亚马逊销售佣金', 'FBA代发货费用', '多渠道配送费', '退款扣除佣金', 'FBA退货处理费',
    #        '返还亚马逊销售佣金', 'FBA月仓储费用', '其他', 'promote折扣', '退款返还promote折扣', 'CPC直接销量',
    #        'CPC直接商品销售额', 'CPC花费', '采购成本', '物流/头程', '运营费用', 'VAT', '结算费', '返还运费',
    #        '亚马逊费用占比', 'CPC直接销量占比', 'CPC花费占比', '成本/物流费用占比', '运营费用占比', '测评费用',
    #        '测评费用占比', '毛利润', '毛利率', 'store_Name', 'Period', 'currency_Sign',
    #        'exchange_Rate'],
    # for column in df_args.columns:
    #     try:
    #         if column in replace_columns_list:
    #             # df_args[column] = df_args[column].str.replace('[^0-9\-\.+]','').astype(dtype='float')
    #             df_args[column] = df_args[column].str.replace('[HK$]|[A$]|[C$]|[$]|[€]|[£]|[¥]', '').astype(dtype='float')
    #         elif column in float_columns_list:
    #             df_args[column] = df_args[column].astype(dtype = 'float')
    #             # df_args[column] = df_args[column].to_numpy()
    #         elif column in percentage_columns_list:
    #             # df_args[column] = df_args[column].str.replace('%','').astype(dtype='float') / 100
    #             df_args[column] = df_args[column].str.strip('%').astype(dtype='float')/100
    #     except:
    #         pass
    global dict_operators
    for column in df_args.columns:
        global dict_operators
        try:
            if column in digit_columns:

                df_args[column] = df_args[column].str.replace('[HK$]|[A$]|[C$]|[$]|[€]|[£]|[¥]', '')
                if column in percentage_columns:
                    df_args[column] = df_args[column].str.strip('%').astype(dtype='float') / 100
                else:
                    df_args[column] = df_args[column].astype(dtype='float')
        except:
            print(' replace_currency_sign ' + column + ' error!')
            # pass
    df_args['new测评费用'] = df_args['销售总额'] * 0.01 * -1
    df_args['new毛利润'] = df_args['毛利润'] + df_args['new测评费用']
    df_args['new毛利率'] = df_args['new毛利润'] / df_args['销售总额']
    df_args['store_ASIN_Assistance'] = df_args['store_Name'] + ":" + df_args['ASIN']
    df_args['product_Grouping'] = ''

    df_args = pd.merge(df_args, df_operators, how='left',on='store_ASIN_Assistance')  #,loc[:,['store_ASIN_Assistance'=df_args['store_ASIN_Assistance'] ]],)
    # df_args['product_Grouping'] = df_args['store_ASIN_Assistance']  #.map(dict_operators)
    # df_dict['exchange_Rate'] = df_dict['currency_Sign'].map(exchange_rate)
    # result = pd.merge(df1, df2.loc[:, ['学号', '分数']], how='left', on='学号')

    print (df_args)  #(df_args['store_ASIN_Assistance']  + df_args['product_Grouping'] )
    return df_args


# 输入数据所属日期input_date
def input_date():
    while True:
        try:
            input_date = input("请输入报告日期(日期格式：YYYY-MM-DD)：")
            if len(input_date) == 8:
                input_date = input_date[:4] + '-' + input_date[4:6] + '-' + input_date[-2:]

            if datetime.date.fromisoformat(input_date) <= datetime.date.today():
                input_date = input_date[:4] + input_date[5:7] + input_date[-2:]
                print('当前报告日期：' + input_date)
                break
            else:
                print("您输入的日期大于当前日期，请重新输入!")
        except:
            print("您输入的日期格式不正确，请重新输入，日期格式为YYYY-MM-DD!")
    return input_date


def original_to_benchmark():
    global df_ASINFeePayment_benchmark
    df_ASINFeePayment_benchmark = df_ASINFeePayment_original.copy()

    for column in df_ASINFeePayment_benchmark.columns:
        try:

            if column in replace_columns:
                df_ASINFeePayment_benchmark[column] = df_ASINFeePayment_benchmark[column] * df_ASINFeePayment_benchmark['exchange_Rate']
        except:
            print(' original_to_benchmark ' + column + ' error!')
            #pass
    return




#输出数据到EXCEL文件
def export_excel_file():
    try:
        excel_file_name = 'Captain_ASINFeePayment' + report_date +'.xlsx'

        if os.path.exists(excel_file_name):
            os.remove(excel_file_name)

        with pd.ExcelWriter(excel_file_name) as writer:
            df_ASINFeePayment_original.to_excel(writer, sheet_name='Original_' + report_date, index=False, header=True)
            df_ASINFeePayment_benchmark.to_excel(writer, sheet_name='Benchmark_' + report_date, index=False, header=True)

    except:
        print(' export_to_excel_file ' + '' + ' error!')
    return



def import_operators():
    global df_operators
    try:

        operators_path = os.path.join(common_dir, operators_file)
        # print(operators_path)
        df_operators = pd.read_excel(operators_path)
        df_operators.reindex()
        # df_operators = open_operators['store_ASIN_Assistance','product_Grouping']
        # print(df_operators)
        # dict_operators = df_operators.set_index(['store_ASIN_Assistance'])['product_Grouping']
        # print(dict_operators)
    # df1 = df.set_index(['name'])['age'].to_dict()
    # pandas.read_excel（io，sheet_name = 0，header = 0，names = None，index_col = None，usecols = None，squeeze = False, dtype = None, ...）

    except:
        print(' import_operators ' + '' + ' error!')
    return



if __name__ == "__main__":

    report_date = input_date()

    #定义数据存放目录
    data_dir = './data'

    rename_csv(data_dir)

    import_operators()

    df_ASINFeePayment_original = open_csv(data_dir)
    #
    replace_currency_sign(df_ASINFeePayment_original)

    original_to_benchmark()

    export_excel_file()



    # csv_file = '.\data\OMB1_EU_UK-Payment_2021-04-01_2021-04-05.csv'
    # df_dict = pd.read_csv(csv_file, sep=',', encoding="utf-8")
    # print(type(df_dict))
    # data_dir_list = os.listdir(data_dir)  # 列出文件夹下所有的目录与文件
    # for i in range(0, len(data_dir_list)):
    #     count =1
    #     csv_dir = os.path.join(data_dir, data_dir_list[i])
    #     print (csv_dir)
    #     if os.path.isdir(csv_dir):
    #         csv_file_list = os.listdir(csv_dir)  # 列出文件夹下所有的目录与文件
    #         for csvname in csv_file_list:
    #             csvpath = os.path.join(csv_dir,csvname)
    #             if os.path.isfile(csvpath):
    #                 # os.rename(csvpath, os.path.join(csv_dir, data_dir_list[i]) + '.csv')  # 在原来目录中重命名csv文件
    #                 os.rename(csvpath, csv_dir + '.csv')  # 重命名csv文件并移动到./data目录中
    #                 count += 1
