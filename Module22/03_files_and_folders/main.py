# E:\PycharmProjects\python_basic\Module14
# Размер каталога (в Кб): 8.373046875
# Количество подкаталогов: 7
# Количество файлов: 15


# python_basic\Module14
import os


def info_catalog(dir_path):
    path = os.scandir(dir_path)
    files = 0
    folders = 0
    size = 0
    for i_elem in path:
        size += os.path.getsize(i_elem)
        if os.path.isfile(i_elem):
            files += 1
        elif os.path.isdir(i_elem):
            folders += 1
            size_count, file_count, folder_count = info_catalog(i_elem)
            size += size_count
            files += file_count
            folders += folder_count

    return size, files, folders


info_path = input('Введите путь: ')
info_size, info_files, info_dir = info_catalog(info_path)
print('Размер каталога (в Кб):', info_size / 1024)
print('Количество подкаталогов:', info_dir)
print('Количество файлов:', info_files)

# C:\Users\Rainbow4\PycharmProjects\Python_Basic2.5\Module14              У меня стоит такой путь. Залажал вначале по итогу все с костылями