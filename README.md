## Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (para usuários de Windows e Mac)

## Instruções para subir o ambiente

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Inicie o Docker Desktop** (necessário para usuários de Windows e Mac):

   Certifique-se de que o Docker Desktop esteja aberto e rodando antes de executar o próximo passo. Caso contrário, podem ocorrer erros de conexão.

3. **Suba o ambiente usando o Docker Compose**:

   Execute o comando abaixo para iniciar os serviços definidos no arquivo `docker-compose.yml`:

   ```bash
   docker-compose up
   ```

   Este comando irá baixar as imagens necessárias, criar os contêineres e iniciar os serviços configurados.

4. **Acesse os serviços**:

   Após o `docker-compose` terminar de subir os contêineres, os serviços estarão disponíveis conforme as portas configuradas no `docker-compose.yml`. Verifique os logs para confirmar que tudo foi iniciado corretamente.

5. **Parar os serviços**:

   Para parar e remover os contêineres criados, execute:

   ```bash
   docker-compose down
   ```

## Possíveis Problemas

- **Docker Desktop não iniciado**: Caso o Docker Desktop não esteja aberto antes de executar `docker-compose up`, é possível que ocorra o erro `Cannot connect to the Docker daemon`. Para resolver, certifique-se de iniciar o Docker Desktop antes de executar qualquer comando do Docker.
