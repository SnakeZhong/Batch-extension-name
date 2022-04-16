import os
path_op=r"C:\Users\Happy\Desktop\deeplearn\change_extra_name\process_fold"
from_change=".xlsx"#更改前的扩展名
from_change_target=".CSV"#扩展名的目标
name="process_fold"#文件夹的名字
path=os.getcwd()+"\\"+name
#判断文件夹是否存在
if os.path.exists(path):
    pass
else:
    os.mkdir(path=path)
os.chdir(path_op)#修改当前工作目录
file_list=os.listdir("./")

print(file_list)

for file_name in file_list:
    file_from=os.path.splitext(file_name)
    if file_from[1]==from_change:
        new_name=file_from[0]+from_change_target
        #重命名（被修改，修改）
        os.rename(file_name,new_name)

