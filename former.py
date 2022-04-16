import os
import numpy as np
name="process_fold"
path=os.getcwd()+"\\"+name
if os.path.exists(path):
    pass
else:
    os.mkdir(path=path)
#迭代器找出该路径下的所有文件(第二个为文件名)
path_list_iter=os.walk(path)
# print(path_list_iter)
path_list=[]
# print(type(path_list))
for i in path_list_iter:
    path_list.append(i[2])
    for file_name in i[2]:
        #将文件的扩展名切割成文件名和扩展名
        file_name_tur=os.path.splitext(file_name)
        file_name_tur=file_name_tur[:1]+("xlsx",)
        path_list.append(file_name_tur)

for i in path_list:
    print(i)