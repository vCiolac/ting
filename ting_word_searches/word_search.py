def exists_word(word, instance):
    result = list()

    for index in range(len(instance)):
        ocorrenias = list()
        queueSearch = instance.search(index)
        nome = queueSearch["nome_do_arquivo"]
        txt_file = queueSearch["linhas_do_arquivo"]
        for i in range(len(txt_file)):
            if word in txt_file[i].lower():
                ocorrenias.append({"linha": i + 1})

        if len(ocorrenias) == 0:
            return []

        result.append({
                "arquivo": nome,
                "ocorrencias": ocorrenias,
                "palavra": word,
            })

    return result


def search_by_word(word, instance):
    result = list()

    for index in range(len(instance)):
        ocorrenias = list()
        queueSearch = instance.search(index)
        nome = queueSearch["nome_do_arquivo"]
        txt_file = queueSearch["linhas_do_arquivo"]
        for i in range(len(txt_file)):
            if word in txt_file[i].lower():
                ocorrenias.append({"linha": i + 1, "conteudo": txt_file[i]})

        if len(ocorrenias) == 0:
            return []

        result.append({
                "arquivo": nome,
                "ocorrencias": ocorrenias,
                "palavra": word,
            })

    return result

