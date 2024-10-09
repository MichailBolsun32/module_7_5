import os
import time

directory = '.'

for dirpath, dirnames, filenames in os.walk(directory):
    #"Текущий путь:", dirpath
    #"Поддиректории:", dirnames
    #"Файлы:", filenames - list
    for filenam in filenames:
        filepath = os.path.join(dirpath, filenam) #Привели в читабильный вид (dir + file_name)
        filetime = os.path.getmtime(filepath) #time create file
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime)) # format time
        filesize = os.path.getsize(filepath) # size file
        parent_dir = os.path.dirname(filepath) # dir где размещен file
        print(
            f'Обнаружен файл: {filenam},'
            f' Путь: {filepath}, '
            f'Размер: {filesize} байт, '
            f'Время изменения: {formatted_time}, '
            f'Родительская директория: {parent_dir}')