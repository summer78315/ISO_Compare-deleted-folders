import os
# 已轉的PDF需先掛載\\192.168.1.86\d$\BPM\wildfly-15.0.0.Final\modules\NaNa\DocServer\document\ISO
# 原始檔案\\192.168.1.86\d$\BPM\wildfly-15.0.0.Final\modules\NaNa\DocServer\document\ISOSOURCE
rootdir = 'Z:\\'
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)

    if os.path.isdir(d):
        print(d)
        # 逐一寫入用a，開啟編碼模式為UTF-8(內含中文適用)
        with open('./data.txt', 'a', encoding='UTF-8') as f:  #
            # 寫入txt從第3字元開始
            print((d[3:20]), file=f)
