import os
import shutil
# 已轉的PDF需先掛載\\192.168.1.86\d$\BPM\wildfly-15.0.0.Final\modules\NaNa\DocServer\document\ISO
# 原始檔案\\192.168.1.86\d$\BPM\wildfly-15.0.0.Final\modules\NaNa\DocServer\document\ISOSOURCE
path = "Z:\\"
os.chdir(path)
flist = open(r'C:\Users\A150401\Desktop\Python教學\ISO砍掉相關目錄資料夾\del.txt')
for f in flist:
    fname = f.rstrip()  # 去除每一行後面的空格
    shutil.rmtree(fname, ignore_errors=True)  # ignore_errors=True發生錯誤則略過
