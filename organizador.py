import os
import shutil
import argparse


class FileOrganizer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.arquivos_movidos = 0
        self.pastas_ignoradas = 0

    def get_files(self):
        """Retorna a lista de arquivos e pastas na pasta."""
        return os.listdir(self.folder_path)

    def is_file(self, item):
        """Verifica se o item é um arquivo."""
        return os.path.isfile(os.path.join(self.folder_path, item))

    def get_extension(self, filename):
        """Retorna a extensão do arquivo."""
        return os.path.splitext(filename)[1]

    def get_folder_name(self, ext):
        """Retorna o nome da pasta baseado na extensão."""
        return ext[1:] if ext else "sem_extensao"

    def create_folder(self, folder_name):
        """Cria a pasta se não existir."""
        folder_path = os.path.join(self.folder_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        return folder_path

    def move_file(self, src, dst):
        """Move o arquivo para o destino."""
        shutil.move(src, dst)

    def organize_files(self):
        """Organiza os arquivos na pasta."""
        print(f"Iniciando organização de arquivos na pasta {self.folder_path}...\n")

        files = self.get_files()
        for file in files:
            file_path = os.path.join(self.folder_path, file)
            if self.is_file(file_path):
                ext = self.get_extension(file)
                folder_name = self.get_folder_name(ext)
                if ext:
                    print(f"📁 Organizando: {file} -> pasta '{folder_name}'")
                else:
                    print(f"📄 Arquivo sem extensão: {file} -> pasta '{folder_name}'")

                folder_path = self.create_folder(folder_name)
                dst = os.path.join(folder_path, file)
                self.move_file(file_path, dst)
                self.arquivos_movidos += 1
            else:
                print(f"⏭️  Ignorando pasta: {file}")
                self.pastas_ignoradas += 1

        print(f"\n✅ Organização concluída!")
        print(
            f"📊 Resumo: {self.arquivos_movidos} arquivo(s) movido(s), {self.pastas_ignoradas} pasta(s) ignorada(s)."
        )


# Uso do organizador
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organiza arquivos por extensão.")
    parser.add_argument(
        "folder",
        nargs="?",
        default=os.path.join(os.path.expanduser("~"), "Downloads"),
        help="Pasta a organizar (padrão: Downloads do usuário)",
    )
    args = parser.parse_args()
    organizer = FileOrganizer(args.folder)
    organizer.organize_files()
