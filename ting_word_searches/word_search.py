from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    data = []

    for index in range(len(instance)):
        file = instance.search(index)
        founds = []
        for index, row in enumerate(file['linhas_do_arquivo']):
            if word.lower() in row.lower():
                founds.append({'linha': index + 1})
        if founds:
            data.append({
                "palavra": word,
                "arquivo": file['nome_do_arquivo'],
                "ocorrencias": founds
            })

    return data


def search_by_word(word, instance):
    data = []

    for index in range(len(instance)):
        file = instance.search(index)
        founds = []
        for index, row in enumerate(file['linhas_do_arquivo']):
            if word.lower() in row.lower():
                founds.append({
                    'linha': index + 1,
                    'conteudo': row
                })
        if founds:
            data.append({
                "palavra": word,
                "arquivo": file['nome_do_arquivo'],
                "ocorrencias": founds
            })

    return data
