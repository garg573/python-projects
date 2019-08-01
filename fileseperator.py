import os,shutil

# NOTE:- You can write every single extensions inside tuples
dic_ext={
'audio_ext':('.mp3','.m4a','.wav','.flac'),
'video_ext':('.mp4','.mkv','.flv','.mpeg'),
'doc_ext':('.doc','.pdf','.txt','.py'),
'Img_ext':('.JPG','.jpeg','.png','.ico')

}
folderpath=input("enter folder path: ")

def file_finder(folder_path,file_ext):
    '''    files=[]
    for file in os.listdir(folder_path):
        for exten in file_ext:
            if file.endswith(exten):
                files.append(file)
    return files
    '''
    return [file for file in os.listdir(folder_path) for exten in file_ext if file.endswith(exten)]
# print(file_finder(folderpath,audio_ext))

for extension_type,extension_tuple in dic_ext.items():
    folder_name=extension_type.split('_')[0]+' Files'
    folder_path=os.path.join(folderpath,folder_name)
    os.mkdir(folder_path)
    for item in file_finder(folderpath,extension_tuple):
        item_path=os.path.join(folderpath,item)
        item_new_path=os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)
    #print('calling file finder')
    #print(file_finder(folderpath,extension_tuple))

