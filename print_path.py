import os

g = os.walk("/media/wuchenxi/TF/ubuntudownload/部队技术标证照")

for path,dir_list,file_list in g:
    for dir_name in dir_list:
        print(os.path.join(path, dir_name))