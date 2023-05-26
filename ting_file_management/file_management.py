import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        return sys.stderr.write('Formato inválido\n')

    try:
        with open(path_file) as file:
            rows = file.read().split('\n')
            new_list = []
            for row in rows:
                new_list.append(row)
            return new_list
    except (FileNotFoundError):
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
