#DeleteLocalFiles.py
from os import remove
from os import path

def deleteLocalFilesFn(fullPathFiles):
    print('Init Delete Files')
    try:
        for filePath in fullPathFiles:
            print('file fullpath => ', filePath)
            if path.exists(filePath):
                remove(filePath)#remove zip file
                ziFile=filePath.replace('_extension.zip','.extension')
                print('ziFile fullpath => ', ziFile)
                remove(ziFile)#remove original extension file 

        print('End Delete Files')
    except Exception as e:
        print('Error Delete Files ', e)

