# Imobiliária App

## Objetivo do Projeto

O **Imobiliária App** é uma aplicação completa para a gestão de propriedades, usuários, contratos, pagamentos, documentos e comunicações relacionadas ao setor imobiliário. Este projeto visa facilitar a administração de propriedades para proprietários, agentes imobiliários e inquilinos, fornecendo um conjunto de ferramentas abrangentes para gerenciar todos os aspectos do negócio imobiliário.


## Diagrama de Classes



## Funcionalidades Principais

### Gestão de Usuários
- **Tabelas**: `Usuario`, `PerfilCliente`, `PerfilAgenteImobiliario`, `PerfilInquilino`
- **Funcionalidades**:
  - Cadastro e login de usuários.
  - Gestão de perfis de clientes, agentes imobiliários e inquilinos.
  - Atualização de informações de contato e endereço.
  - Controle de tipos de usuários (cliente, agente imobiliário, inquilino).

### Gestão de Propriedades
- **Tabelas**: `Propriedade`
- **Funcionalidades**:
  - Cadastro de novas propriedades com detalhes completos (título, descrição, preço, endereço, etc.).
  - Atualização de informações das propriedades.
  - Visualização de lista de propriedades.
  - Filtragem e busca de propriedades com base em preferências dos clientes.

### Gestão de Contratos
- **Tabelas**: `Contrato`
- **Funcionalidades**:
  - Criação e gerenciamento de contratos de aluguel e venda.
  - Definição de datas de início e término dos contratos.
  - Controle de status dos contratos (ativo, encerrado, pendente).
  - Associação de contratos a propriedades, inquilinos e agentes imobiliários.

### Gestão de Pagamentos
- **Tabelas**: `Pagamento`
- **Funcionalidades**:
  - Registro de pagamentos de aluguel e outras despesas (água, luz, IPTU).
  - Controle de métodos de pagamento (cartão, transferência).
  - Atualização e verificação de status dos pagamentos (pago, pendente).
  - Relatórios de pagamentos efetuados.

### Gestão de Documentos
- **Tabelas**: `Documento`
- **Funcionalidades**:
  - Upload e armazenamento de documentos importantes (contratos assinados, comprovantes).
  - Visualização e download de documentos.
  - Organização de documentos por tipo e data de upload.

### Gestão de Contatos
- **Tabelas**: `Contato`
- **Funcionalidades**:
  - Envio e recepção de mensagens entre inquilinos e proprietários/agentes.
  - Registro de histórico de comunicação.
  - Notificação de novas mensagens.
  - Filtragem de mensagens por propriedade e usuário.

## Tecnologias Utilizadas

- **Backend**: Django, Django REST Framework
- **Frontend**: React, Tanstack Query, Tanstack Router
- **Banco de Dados**: PostgreSQL
- **Autenticação**: djangorestframework-simplejwt
- **Gerenciamento de Tarefas**: Celery
- **Containerização**: Docker, Docker Compose

## Como Configurar o Projeto

### Pré-requisitos
- Docker e Docker Compose instalados

### Passos para Configuração

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/imobiliaria-app.git
   cd imobiliaria-app
   ```

2. **Configure as variáveis de ambiente:**
   crie os arquivos ".django" e ".postgres" com suas variaveis de ambiente, conforme o arquivo ".env.django.sample" e "env.postgres.sample".
      - ./.envs/.local/.django
      - ./.envs/.local/.postgres

3. **Execute a aplicação com Docker Compose:**
   ```bash
   docker compose -f local.yml up --build -d
   ```

## Como Contribuir

1. Faça um fork do projeto
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Envie para o branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Sinta-se à vontade para contribuir, sugerir melhorias ou relatar problemas. Estamos abertos a colaborações e melhorias contínuas!
