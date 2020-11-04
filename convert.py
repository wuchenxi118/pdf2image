from pdf2image import convert_from_path
import os
import sys


def createFolderAndSaveImage(path,folder_path):
    single_path = os.path.join(path, folder_path)
    os.chdir(single_path)
    print(single_path)
    pdf_list = []
    for file in os.listdir(single_path):
        if file.endswith('.pdf'):
            pdf_list.append(file)
    # print(pdf_list)
    for pdf_path in pdf_list:
        pages = convert_from_path(pdf_path, 300)
        new_image_folder = pdf_path[:-4] + '_image'
        os.mkdir(new_image_folder)
        os.chdir(os.path.join(single_path, new_image_folder))
        index = 0
        for page in pages:
            page.save(pdf_path + '_' + str(index) + '.jpg', 'JPEG')
            index += 1
        os.chdir(single_path)
def convertJpg2image(top_path):
    g = os.walk(top_path)
    for path, dir_list, file_list in g:

        # dir_list.append('')
        # print(dir_list)
        for dir_name in dir_list:
            createFolderAndSaveImage(path,dir_name)
        #     single_path = os.path.join(path, dir_name)
        #     os.chdir(single_path)
        #     print(single_path)
        #     pdf_list = []
        #     for file in os.listdir(single_path):
        #         if file.endswith('.pdf'):
        #             pdf_list.append(file)
        #     # print(pdf_list)
        #     for pdf_path in pdf_list:
        #         pages = convert_from_path(pdf_path,300)
        #         new_image_folder = pdf_path[:-4]+'_image'
        #         os.mkdir(new_image_folder)
        #         os.chdir(os.path.join(single_path, new_image_folder))
        #         index = 0
        #         for page in pages:
        #             page.save(pdf_path+'_'+str(index)+'.jpg','JPEG')
        #             index+=1
        #         os.chdir(single_path)
        if len(dir_list) == 0:
            createFolderAndSaveImage(path, "")
            # single_path = os.path.join(path, '')
            # os.chdir(single_path)
            # print(single_path)
            # pdf_list = []
            # for file in os.listdir(single_path):
            #     if file.endswith('.pdf'):
            #         pdf_list.append(file)
            # # print(pdf_list)
            # for pdf_path in pdf_list:
            #     pages = convert_from_path(pdf_path, 300)
            #     new_image_folder = pdf_path[:-4] + '_image'
            #     os.mkdir(new_image_folder)
            #     os.chdir(os.path.join(single_path, new_image_folder))
            #     index = 0
            #     for page in pages:
            #         page.save(pdf_path + '_' + str(index) + '.jpg', 'JPEG')
            #         index += 1
            #     os.chdir(single_path)
            break

if __name__ == '__main__':
    convertJpg2image(str(sys.argv[1]))
