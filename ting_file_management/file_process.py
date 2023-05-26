from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for process in instance._queue:
        if process['nome_do_arquivo'] == path_file:
            return False
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }
    instance.enqueue(data)
    return sys.stdout.write(str(data))


def remove(instance):
    if not len(instance):
        return sys.stdout.write('Não há elementos\n')
    else:
        path_file_dequeue = instance.dequeue()
        path_file = path_file_dequeue['nome_do_arquivo']
        return sys.stdout.write(f'Arquivo {path_file} removido com sucesso\n')


def file_metadata(instance, position):
    try:
        found_position = instance.search(position)
        return sys.stdout.write(str(found_position))
    except (IndexError):
        return sys.stderr.write('Posição inválida\n')
