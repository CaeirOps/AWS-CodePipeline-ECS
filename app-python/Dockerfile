#Imagem referência do Docker
FROM python:3.7-slim

#Selecionando o diretório de trabalho
WORKDIR /app

#Copia os arquivos locais para o container
COPY . /app

#Adicionando pacotes de resquisitos
RUN pip install -r requisitos.txt ; apt update ; apt install firefox-esr -y ; cp geckodriver /usr/bin

#Expondo a porta 80 do container
EXPOSE 80

#Definindo algumas variáveis de ambiente
ENV NAME World

#Processo principal
CMD ["python","app.py"]

