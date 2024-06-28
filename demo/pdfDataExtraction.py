import pandas as pd
import pdfquery
import re
import os

# 提取字符串中的数值
def extract_numbers(text):
    # 定义正则表达式模式，匹配整数或小数
    pattern = r"[-+]?\d*\.\d+|[-+]?\d+"
    # 使用findall函数查找所有匹配的数值
    numbers = re.findall(pattern, text)
    # 将找到的字符串转换为浮点数或整数
    numbers = [float(num) if '.' in num else int(num) for num in numbers]
    return numbers

# 获取目录下所有文件名称
def get_all_files(directory):
    file_list = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_list.append(filename)
    return file_list

# 遍历指定目录，获取目录下的所有文件
directory_path = 'E:/test'
files = get_all_files(directory_path)
print(files)
print('文件个数:', len(files))



jbsjList = []
# 遍历files，读取pdf文件
for filename in files:
    # 读取 PDF
    pdf = pdfquery.PDFQuery(directory_path + '/' + filename)
    pdf.load()
    #将 pdf 转换为 XML
    pdf.tree.write(filename + '.XML', pretty_print = True)
    # 使用坐标读取数据
    jbsc = pdf.pq('LTTextLineHorizontal:in_bbox("142.0, 621.17, 298.0, 641.42")').text()

    # 提取数值
    extracted_numbers = extract_numbers(jbsc)
    jbsjList.append(extracted_numbers[0])



print('加班总时间：', sum(jbsjList))

