FROM node:20.17.0 AS build

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o package.json e o package-lock.json para instalar as dependências
COPY package*.json ./

# Instale as dependências do projeto
RUN npm install

# Copie o restante do código da aplicação para o diretório de trabalho no container
COPY . .

# Construa a aplicação Angular para produção
RUN npm run build --prod

# Use uma imagem do Nginx para servir a aplicação
FROM nginx:alpine

# Copie os arquivos construídos do estágio anterior para o diretório padrão do Nginx
COPY --from=build /app/dist/frontend /usr/share/nginx/html

# Copie o arquivo de configuração customizado do Nginx, se necessário (opcional)
# COPY nginx.conf /etc/nginx/nginx.conf

# Exponha a porta 80
EXPOSE 80

# Comando para iniciar o Nginx
CMD ["nginx", "-g", "daemon off;"]
