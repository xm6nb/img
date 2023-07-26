"""
该脚本可用于批量转换word为pdf
只需修改directory变量为word所在目录的绝对路径即可
"""
import os
import comtypes.client

def get_file_names(directory):
    """
    :param directory: word所在目录
    :return:
    """
    # 获取目录下的所有文件和文件夹
    file_names = os.listdir(directory)
    # 仅保留文件名，排除子文件夹
    file_names = [file for file in file_names if os.path.isfile(os.path.join(directory, file))]
    index = 0
    while index < len(file_names):
        file_name = file_names[index]
        if file_name.split('.')[-1] != 'doc' and file_name.split('.')[-1] != 'docx':
            file_names.remove(file_name)
            index -= 1
        index += 1
    return file_names

def doc_to_pdf(input_path,parent_directory):
    """
    :param input_path: word文件名称
    :param parent_directory: pdf存储目录
    :return: 无
    """
    #文件名更新
    output_filename = input_path.split('.')[0] + '.' + 'pdf'

    # 获取文件的绝对路径
    input_path = os.path.join(directory,input_path)
    output_path = os.path.join(parent_directory,output_filename)
    # 创建Word应用程序实例
    word_app = comtypes.client.CreateObject('Word.Application')

    try:
        # 打开Word文档
        doc = word_app.Documents.Open(input_path)
        # 将文档保存为PDF格式
        doc.SaveAs(output_path, FileFormat=17)
    except Exception as e:
        print(f"{output_filename}转换失败: {e}")
        pass
    finally:
        # 关闭Word文档和应用程序
        doc.Close()
        word_app.Quit()

def doc_to_pdf_init(directory):
    """
    :param directory: word所在目录
    :return: 无
    """
    # 调用函数获取文件名列表
    file_names = get_file_names(directory)
    # 创建存放pdf的目录
    parent_directory = os.path.join(directory, 'pdf')
    while os.path.isdir(parent_directory):
        parent_directory += 'f'
    os.mkdir(parent_directory)
    for input_file in file_names:
        doc_to_pdf(input_file,parent_directory)
        print(input_file + '--->' + input_file.split('.')[0] + '.pdf')

if __name__ == '__main__':
    # 指定目录路径
    directory = ""
    # 初始化并开始转换
    doc_to_pdf_init(directory)
