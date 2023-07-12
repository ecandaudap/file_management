import files

files.create_file('sample1.txt', 'Crea contenido del archivo')
#files.create_file('sample2.txt')

files.modify_file('sample1.txt', "Este contenido fue sobreescrito", overwrite = True)
#files.modify_file('sample2.txt', "Este contenido fue adicionado", overwrite = False)

files.read_file('sample1.txt')

files.delete_file('sample1.txt')
#files.delete_file('sample2.txt')