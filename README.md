# pdf2image转换工具安装使用方法

### 1.下载本项目
### 2.安装Anaconda3/Miniconda3
### 3.打开Anaconda Prompt,输入以下两条命令，如有y/N判断，键入y并回车
#### ```conda install -c conda-forge poppler```
#### ```pip install pdf2image```
### 4.假设项目存在的路径为C:\Users\wcx\PycharmProjects\pdf2image-main，在Anaconda Prompt中键入```cd C:\Users\wcx\PycharmProjects\pdf2image-main```，进入项目目录
### 5.假设想要转换的pdf存放在C:\Users\wcx\PycharmProjects\待转换pdf，在Anaconda Prompt中键入```python convert.py C:\Users\wcx\PycharmProjects\待转换pdf```,该命令会将文件夹下所有pdf转为图片，并保存在相应pdf名称的文件夹下