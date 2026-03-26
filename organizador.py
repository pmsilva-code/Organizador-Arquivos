import os
import shutil

download_folder = r"C:\Users\plati\Downloads"
files = os.listdir(download_folder)

# Contadores para resumo
arquivos_movidos = 0
pastas_ignoradas = 0

print("Iniciando organização de arquivos na pasta Downloads...\n")

# validador de extenção de arquivos e organizador:
for file in files:
    file_path = os.path.join(download_folder, file)
    if os.path.isfile(file_path):  # só processar arquivos, não pastas
        ext = os.path.splitext(file)[1]
        if ext:
            folder_name = ext[1:]  # remove o ponto
            print(f"📁 Organizando: {file} -> pasta '{folder_name}'")
        else:
            folder_name = "sem_extensao"
            print(f"📄 Arquivo sem extensão: {file} -> pasta '{folder_name}'")

        # Criar pasta se não existir
        folder_path = os.path.join(download_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Mover arquivo
        src = file_path
        dst = os.path.join(folder_path, file)
        shutil.move(src, dst)
        arquivos_movidos += 1
    else:
        print(f"⏭️  Ignorando pasta: {file}")
        pastas_ignoradas += 1

print(f"\n✅ Organização concluída!")
print(
    f"📊 Resumo: {arquivos_movidos} arquivo(s) movido(s), {pastas_ignoradas} pasta(s) ignorada(s)."
)
