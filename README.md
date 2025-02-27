# MeioAuto 🤖

O **MeioAuto** é uma ferramenta desenvolvida em Python para extração automática de códigos de barras de arquivos DARF em formato PDF. O sistema monitora a pasta de entrada e gera um novo arquivo PDF consolidando os códigos extraídos.

## 📌 Funcionalidades
- Extração automática de códigos de barras de documentos PDF 📄
- Monitoramento contínuo da pasta de entrada 🕵️
- Geração de um PDF consolidado com os códigos extraídos 🖨️

## ⚙️ Tecnologias Utilizadas
- **PyMuPDF** (Manipulação de PDFs)
- **ReportLab** (Geração de PDFs)
- **Watchdog** (Monitoramento de arquivos)
- **Expressões Regulares** (Extração de dados)

## 🚀 Como rodar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/meioauto.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd meioauto
   ```
3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute o programa:
   ```bash
   python main.py
   ```

## 🛠️ Como utilizar o MeioAuto

1. Após realizar o download da ferramenta, extraia o conteúdo do arquivo ZIP para uma pasta de sua preferência.
2. Navegue até a pasta **"dist"** e localize o arquivo executável denominado **"codigo"**.
3. Execute o arquivo **"codigo"**. Caso seu sistema operacional exiba um aviso de segurança, selecione **"Mais informações"** e em seguida **"Executar mesmo assim"**.
4. Aguarde até que a mensagem **"Aguardando novos arquivos"** seja exibida na janela do programa. ⏳
5. Insira todos os arquivos **DARF** que deseja processar na pasta **"pdfs"** de uma só vez.
6. O sistema processará automaticamente os arquivos. Após a conclusão, dirija-se à pasta **"arquivo"** para visualizar o PDF gerado com os códigos de barras extraídos. ✅
***Observação:** O **MeioAuto** continuará monitorando a pasta **"pdfs"** para novos arquivos. Para encerrar o programa, feche a janela do executável.*

## 📩 Contribuições
Sinta-se à vontade para abrir issues e enviar PRs com melhorias! 💡

## 📜 Licença
Este projeto está sob a licença MIT.

