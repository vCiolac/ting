from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    txt_list = txt_importer(path_file)
    for data in instance.queue:
        if data["nome_do_arquivo"] == path_file:
            print(f"Arquivo {path_file} já foi processado.")
            return

    dict_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_list),
        "linhas_do_arquivo": txt_list,
    }

    instance.enqueue(dict_data)
    print(f"Dados processados do arquivo {path_file}:\n{dict_data}")


def remove(instance):
    if not instance.queue:
        print("Não há elementos")
        return
    rmv_data = instance.dequeue()
    if rmv_data:
        print(f"Arquivo {rmv_data['nome_do_arquivo']} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
