# Use uma imagem oficial do Node.js como base
FROM node:20.17.0

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o package.json e o package-lock.json para instalar as dependências
COPY package*.json ./

# Instale as dependências do projeto
RUN npm install

# Copie o restante do código da aplicação para o diretório de trabalho no container
COPY . .

# Exponha a porta padrão do Angular CLI
EXPOSE 4200

# Comando para iniciar a aplicação Angular em modo de desenvolvimento
CMD ["npm", "start", "--", "--host", "0.0.0.0"]
