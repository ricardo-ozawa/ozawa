import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selicione a pasta")

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens":[".jpg",".jpeg"],
    "pdfs": [".pdf"],
    "rars": [".rar"],
    "zips": [".zip"]
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
