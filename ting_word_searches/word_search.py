from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    result = list()

    for index in range(len(instance)):
        ocorrenias = list()
        queueSearch = instance.search(index)
        txt_file = txt_importer(queueSearch)

        for i in range(len(txt_file)):
            if word in txt_file[i].lower():
                ocorrenias.append({"linha": i + 1})

        if len(ocorrenias) == 0:
            return []

        result.append({
                "palavra": word,
                "arquivo": queueSearch,
                "ocorrenias": ocorrenias
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
