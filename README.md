# Organizador de Arquivos

Este projeto é um organizador automático de arquivos para a pasta Downloads do Windows. Ele valida as extensões dos arquivos, cria pastas correspondentes e move os arquivos para essas pastas, facilitando a organização e limpeza da pasta de downloads.

## Funcionalidades

- **Validação de Extensões**: Verifica a extensão de cada arquivo na pasta Downloads.
- **Criação de Pastas**: Cria pastas automaticamente baseadas nas extensões (ex: `jpg`, `png`, `exe`).
- **Movimentação de Arquivos**: Move arquivos para as pastas apropriadas.
- **Tratamento de Arquivos sem Extensão**: Arquivos sem extensão são movidos para uma pasta chamada `sem_extensao`.
- **Ignorar Pastas**: O script ignora subpastas existentes para evitar conflitos.
- **Logs Intuitivos**: Exibe mensagens claras durante o processo, com emojis e resumo final.

## Requisitos

- **Python 3.x**: Certifique-se de ter o Python instalado.
- **Bibliotecas**: O script usa apenas bibliotecas padrão (`os` e `shutil`), então não há dependências externas.
- **Sistema Operacional**: Desenvolvido para Windows, mas compatível com outros sistemas que suportem os módulos usados.

## Instalação

1. **Clone ou Baixe o Repositório**:
   - Baixe ou clone este repositório para o seu computador.

2. **Navegue até a Pasta do Projeto**:
   - Abra o terminal e vá para a pasta onde está o arquivo `organizador.py`.

3. **Verifique o Python**:
   - Execute `python --version` para confirmar que o Python está instalado.

## Como Usar

1. **Prepare a Pasta Downloads**:
   - Certifique-se de que a pasta `C:\Users\[SeuUsuario]\Downloads` contém os arquivos a serem organizados. (O script está configurado para essa pasta por padrão.)

2. **Execute o Script**:
   - No terminal, execute: `python organizador.py`
   - O script irá:
     - Listar os arquivos na pasta Downloads.
     - Para cada arquivo:
       - Verificar se é um arquivo (ignora pastas).
       - Extrair a extensão.
       - Criar uma pasta com o nome da extensão (sem o ponto, ex: `jpg` para `.jpg`).
       - Mover o arquivo para a pasta correspondente.
     - Exibir logs em tempo real e um resumo ao final.

3. **Resultado**:
   - Arquivos serão organizados em subpastas dentro de Downloads, como:
     - `Downloads/jpg/` para imagens JPG.
     - `Downloads/exe/` para executáveis.
     - `Downloads/sem_extensao/` para arquivos sem extensão.

## Exemplo de Execução

Suponha que a pasta Downloads tenha os arquivos: `foto.jpg`, `documento.pdf`, `programa.exe` e uma pasta `old_files`.

Saída do script:
```
Iniciando organização de arquivos na pasta Downloads...

📁 Organizando: foto.jpg -> pasta 'jpg'
📁 Organizando: documento.pdf -> pasta 'pdf'
📁 Organizando: programa.exe -> pasta 'exe'
⏭️  Ignorando pasta: old_files

✅ Organização concluída!
📊 Resumo: 3 arquivo(s) movido(s), 1 pasta(s) ignorada(s).
```

Após a execução, a estrutura ficará:
```
Downloads/
├── jpg/
│   └── foto.jpg
├── pdf/
│   └── documento.pdf
├── exe/
│   └── programa.exe
└── old_files/  (pasta existente, não movida)
```

## Personalização

- **Alterar a Pasta**: Para organizar outra pasta, edite a variável `download_folder` no início do script.
- **Adicionar Validações**: Você pode modificar o código para validar extensões específicas ou adicionar regras extras.

## Como Criar um Executável

Para criar um executável (.exe) que pode ser executado em qualquer computador Windows sem instalar Python:

1. **Instale o PyInstaller** (se não tiver):
   ```
   pip install pyinstaller
   ```

2. **Execute o comando**:
   ```
   pyinstaller --onefile organizador.py
   ```

3. **Localize o executável**:
   - O arquivo `organizador.exe` será criado na pasta `dist/`.
   - Copie este arquivo para qualquer computador Windows e execute-o diretamente.

**Nota**: O executável é autossuficiente e inclui tudo necessário para rodar.

## Contribuição

Sinta-se à vontade para contribuir! Abra issues para relatar bugs ou sugestões, ou envie pull requests com melhorias.

## Licença

Este projeto é de código aberto e está sob a licença MIT. Use e modifique como quiser.