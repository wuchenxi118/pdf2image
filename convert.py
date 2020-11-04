from pdf2image import convert_from_path
import os
import sys

def convertJpg2image(top_path):
    g = os.walk(top_path)
    for path, dir_list, file_list in g:
        for dir_name in dir_list:
            single_path = os.path.join(path, dir_name)
            os.chdir(single_path)
            print(single_path)
            pdf_list = []
            for file in os.listdir(single_path):
                if file.endswith('.pdf'):
                    pdf_list.append(file)
            print(pdf_list)
            for pdf_path in pdf_list:
                pages = convert_from_path(pdf_path,300)
                os.mkdir(pdf_path[:-4])
                os.chdir(single_path+'/'+pdf_path[:-4])
                index = 0
                for page in pages:
                    page.save(pdf_path+'_'+str(index)+'.jpg','JPEG')
                    index+=1
                os.chdir(single_path)

if __name__ == '__main__':
    convertJpg2image(sys.argv[1])
