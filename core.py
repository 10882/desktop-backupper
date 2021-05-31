import zipfile
import os
import win32api

def backup(disk = str, zip = bool):
    dt = 'C:\\Users\\'+win32api.GetUserName()+'\\Desktop'
    if zip == False:
        os.system('mkdir '+disk+':\\bu')
        print('xcopy /e '+dt+' '+disk+ ':\\bu')
        os.system('xcopy /e '+dt+' '+disk+ ':\\bu')
    if zip == True:
        f1le = zipfile.ZipFile(disk+':\\dt.zip', mode= 'w')
        for root, dirs, files in os.walk(dt):
            for f in files:
                f1le.write(os.path.join(root, f))

def get_disk():
    l = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    res = []
    for disk in l:
        if os.system(disk+':') == 0:
            res.append(disk)
    return(res)
        

if __name__ == '__main__':
    backup('F:\\bu', True)