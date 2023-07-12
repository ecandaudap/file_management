''' Script that allows you to perform different operations on files in Python'''

def read_file(file_name):
    
    '''Function that allows you to read a file'''

    file = open(file_name, "r", encoding="utf-8")
    
    file.close()

def create_file(file_name, content=None):
    
    '''Function that allows you to create a file 
    with or without initial content'''
    
    mode = 'w' if content else 'x'

    file = open(file_name, mode, encoding="utf-8")

    if content:
        file.write(content)
    
    file.close()

def modify_file(file_name, content, overwrite=False):

    '''Function that allows you to write or overwrite 
    the content of a file'''
   
    mode = "w" if overwrite else "a"

    file = open(file_name, mode, encoding="utf-8")
    file.write(content)
    file.close()

def delete_file(file_name):

    '''Function that allows you to delete a file'''
    
    import os
    os.remove(file_name)

