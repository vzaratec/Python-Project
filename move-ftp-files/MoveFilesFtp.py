from SendMail import sendEmailFn
from ZipFiles import zipFileFn
from DeleteLocalFiles import deleteLocalFilesFn

import ftplib, re, os
from datetime import date, datetime, timedelta

###########################################
################PARAMETERS#################
host='host_value'
username='username_value'
password='password_value'
directory='main_path_value'
###########################################

#actual date
now = datetime.now()
print ("###########################################")
print ("Current date and time : " + now.strftime("%Y-%m-%d %H:%M:%S"))
print ("###########################################")

# obtain files from FTP
with ftplib.FTP(host, username, password) as ftp:
    try:
        ftp.cwd(directory)
        files = ftp.nlst()
        #print(ftp.dir()) #print files from the directory
   
        zipFiles = []
        # iterate files from the directory  
        for file in files:
            #today=str(date.today()-timedelta(days=1)).replace('-','')
            today=str(date.today()).replace('-','')
            reg='_la_asr_{}_*'.format(today)
            pattern = re.compile(reg)
            matches = pattern.finditer(file)
            for fileMatch in matches:
                #print('File Match {}'.format(file))
                ftp.retrbinary('RETR {}'.format(file), open(file, 'wb').write)#download file from ftp to a local path
                directory=os.getcwd()+'\\'
                zipName = zipFileFn(file, directory)
                zipFiles.insert(0,zipName)

        if len(zipFiles) > 0 :
            if sendEmailFn('','','',zipFiles, directory) == 0 :
                deleteLocalFilesFn(zipFiles)
            print('Process ended OK')
        else:
            print('No files Found')
    except Exception as e:
        print('Process Error ', e)
      
