'''
Wypisz zawartosc katalogu oraz podkatalogow
'''

import os

def list_content(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            list_content(item_path)
        else:
            print(item_path)

list_content(input())
