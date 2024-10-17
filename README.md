## Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (para usuários de Windows e Mac)

## Instruções para subir o ambiente


1. **Clone o repositório**:

   ```bash
   git clone https://github.com/gabrielsdw/challenge.git
   cd seu-repositorio
   ```


2. **Inicie o Docker Desktop** (necessário para usuários de Windows e Mac):

   Certifique-se de que o Docker Desktop esteja aberto e rodando antes de executar o próximo passo. Caso contrário, podem ocorrer erros de conexão.

   Possivel erro se o docker desktop não estiver iniciado: 
      error during connect: Get "http://%2F%2F.%2Fpipe%2FdockerDesktopLinuxEngine/v1.46/containers/json?all=1&filters=%7B%22label%22%3A%7B%22com.docker.compose.config-hash%22%3Atrue%2C%22com.docker.compose.project%3Dchallenge%22%3Atrue%7D%7D": open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.


3. **Suba o ambiente usando o Docker Compose**:

   Execute o comando abaixo para iniciar os serviços definidos no arquivo `docker-compose.yml`:

   ```bash
   docker-compose up
   ```

   Este comando irá baixar as imagens necessárias, criar os contêineres e iniciar os serviços configurados.


4. **Acesse os serviços**:

   Após o `docker-compose` terminar de subir os contêineres, os serviços estarão disponíveis conforme as portas configuradas no `docker-compose.yml`. Verifique os logs para confirmar que tudo foi iniciado corretamente.


5. **Documentação Postman**
   link: https://grey-station-179118.postman.co/workspace/f8775229-998d-455b-8f08-18adc28f9386/collection/30592972-91dfaa2f-ef4d-48a3-b997-b87208a09f7c

   Obs: A documentação também está presente no envio do email anexada como json.


6. **Sobre a parte de edição do HTML**
   Eis a explanação do caminho que tomei nessa parte mais ampla do desafio.

   A criação das lições (Lessons) são feitas a partir de um envio de o id de um template (Uma estrutura html), 
   juntamente com suas preferências (preferences).

   O que são preferences?
      - As preferences são um campo de dados que recebem um dicionário com um element_id, propriety e um value, onde
      o element_id é uma tag html que está presente no html do template (um template pode ter mais de um lugar para fazer modificações), tal tag será modificada a partir de uma propriedade qualquer, como por exemplo: color, background-color, display com o seu respectivo valor (value).

      Exemplo:
         <html>
            <div id="{{blog}}">
               content
            </div>
         </html>
         
         request:
            "preferences": {
               "blog" {
                  "property": "color"
                  "value": "blue"
               }
            }
         
         resultado:
            <html>
               <div id="blog">
                  content
               </div>
            </html>
            <script>document.getElementById('blog').style.color = "blue"</script>


7. **Adendos**
   Ao rodar o docker-compose up, os seguintes usuários e Templates já são criados automaticamente:

      Usuários: 
       - Email: admin@gmail.com; Username: admin; Password: "123".

      Templates:
       - Name: Hello Word; Id: 1
       - Name: Contact Page; Id: 2
       - Name: About Us; Id: 3 


   Exemplos de requisições e todas as rotas estão no postman (que está como json no email e como link no README),
   basta apenas substituir as informações no body.

   O Token é do tipo Bearer, insira em -> Autorization -> Selecione Bearer -> Cole o token sem as aspas duplas.

   Sanarei todas as dúvidas durante a reunião sobre a solução. 