#ZipFiles.py
import zipfile
from datetime import date

def zipFileFn(fileName, filePath):
    print('Init ZipFile')
    try: 
        filePath = filePath+'{}'.format(fileName)
        zipName=filePath.replace('.','_')+'.zip'
        
        #print('zipName => ', zipName)
        fileZipped = zipfile.ZipFile(zipName, 'w')
        fileZipped.write(filePath, compress_type=zipfile.ZIP_DEFLATED)
        fileZipped.close()
        print("End ZipFile")
        return zipName
    except Exception as e:
        print('Error Zipping files ', e)