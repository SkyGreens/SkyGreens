
# SkyGreen Project

Este projeto utiliza o banco de dados **MS SQL Server** em um contêiner Docker. Abaixo estão os passos para configurar o ambiente de banco de dados e estabelecer a conexão usando o **DBeaver**.

## Pré-requisitos

- **Docker**: Para criação e execução do contêiner. [Baixe o Docker para Windows aqui](https://feji.us/o3l9x2).
- **DBeaver**: Uma interface gráfica para conectar e gerenciar o banco de dados. [Baixe o DBeaver para Windows aqui](https://dbeaver.io/files/dbeaver-ce-latest-x86_64-setup.exe).

## Passo 1: Configuração do Contêiner MS SQL Server

1. Após instalar o Docker, execute o seguinte comando no terminal (CMD ou PowerShell) para baixar a imagem do **MS SQL Server** e criar o contêiner:

   ```bash
   docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=yourStrong(!)Password" -e "MSSQL_PID=Evaluation" -p 1433:1433 --name sqlpreview --hostname sqlpreview -d mcr.microsoft.com/mssql/server:2022-preview-ubuntu-22.04
   ```

2. Verifique se o contêiner está rodando usando o comando:

   ```bash
   docker ps
   ```

## Passo 2: Conectar ao Banco de Dados usando DBeaver

1. Abra o **DBeaver** e crie uma nova conexão:
   - Clique em **Nova Conexão** e selecione **SQL Server**.
   
2. Configure a autenticação:
   - **Usuário**: `SA`
   - **Senha**: `yourStrong(!)Password`

   Mantenha as demais configurações como estão.

   - **Finalize a configuração com o finish**

3. Teste a conexão para garantir que o DBeaver esteja se conectando corretamente ao SQL Server.

## Passo 3: Configuração do Banco de Dados e Permissões

Após conectar ao banco de dados no DBeaver, siga os passos abaixo para criar o login, banco de dados e usuário:

### 1. Criar o Login

   ```sql
   USE [master];
   CREATE LOGIN [sky] WITH PASSWORD = 'S3nha@F0rte!';
   ```

### 2. Criar o Banco de Dados

   ```sql
   CREATE DATABASE [Skygreen];
   ```

### 3. Criar o Usuário no Banco de Dados

   ```sql
   USE [Skygreen];
   CREATE USER [sky] FOR LOGIN [sky];
   ```

### 4. Conceder Permissões ao Usuário

   ```sql
   EXEC sp_addrolemember 'db_owner', 'sky';
   EXEC sp_addrolemember 'db_datareader', 'sky';
   EXEC sp_addrolemember 'db_datawriter', 'sky';
   ```

Esses comandos garantirão que o usuário `sky` tenha as permissões necessárias para gerenciar e acessar os dados no banco **Skygreen**.

## Observações

- Certifique-se de que a senha utilizada no comando Docker para o usuário `SA` (exemplo: `yourStrong(!)Password`) seja segura e esteja de acordo com as políticas de segurança do SQL Server.
- Caso precise reiniciar o contêiner, utilize:

  ```bash
  docker start sqlpreview
  ```

Agora, seu banco de dados **MS SQL Server** está configurado e pronto para uso no projeto **SkyGreen**.
