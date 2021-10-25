# Desafio programação - para vaga desenvolvedor

Por favor leiam este documento do começo ao fim, com muita atenção.
O intuito deste teste é avaliar seus conhecimentos técnicos em programação.
O teste consiste em parsear [este arquivo de texto(CNAB)](https://github.com/ByCodersTec/desafio-ruby-on-rails/blob/master/CNAB.txt) e salvar suas informações(transações financeiras) em uma base de dados a critério do candidato.
Este desafio deve ser feito por você em sua casa. Gaste o tempo que você quiser, porém normalmente você não deve precisar de mais do que algumas horas.

# Instruções de entrega do desafio

1. Primeiro, faça um fork deste projeto para sua conta no Github (crie uma se você não possuir).
2. Em seguida, implemente o projeto tal qual descrito abaixo, em seu clone local.
3. Por fim, envie via email o projeto ou o fork/link do projeto para seu contato Bycoders_ com cópia para rh@bycoders.com.br.

# Descrição do projeto

Você recebeu um arquivo CNAB com os dados das movimentações finanaceira de várias lojas.
Precisamos criar uma maneira para que estes dados sejam importados para um banco de dados.

Sua tarefa é criar uma interface web que aceite upload do [arquivo CNAB](https://github.com/ByCodersTec/desafio-ruby-on-rails/blob/master/CNAB.txt), normalize os dados e armazene-os em um banco de dados relacional e exiba essas informações em tela.

**Sua aplicação web DEVE:**

1. Ter uma tela (via um formulário) para fazer o upload do arquivo(pontos extras se não usar um popular CSS Framework )
2. Interpretar ("parsear") o arquivo recebido, normalizar os dados, e salvar corretamente a informação em um banco de dados relacional, **se atente as documentações** que estão logo abaixo.
3. Exibir uma lista das operações importadas por lojas, e nesta lista deve conter um totalizador do saldo em conta
4. Ser escrita na sua linguagem de programação de preferência
5. Ser simples de configurar e rodar, funcionando em ambiente compatível com Unix (Linux ou Mac OS X). Ela deve utilizar apenas linguagens e bibliotecas livres ou gratuitas.
6. Git com commits atomicos e bem descritos
7. PostgreSQL, MySQL ou SQL Server
8. Ter testes automatizados
9. Docker compose (Pontos extras se utilizar)
10. Readme file descrevendo bem o projeto e seu setup
11. Incluir informação descrevendo como consumir o endpoint da API

**Sua aplicação web não precisa:**

1. Lidar com autenticação ou autorização (pontos extras se ela fizer, mais pontos extras se a autenticação for feita via OAuth).
2. Ser escrita usando algum framework específico (mas não há nada errado em usá-los também, use o que achar melhor).
3. Documentação da api.(Será um diferencial e pontos extras se fizer)

# Documentação do CNAB

| Descrição do campo  | Inicio | Fim | Tamanho | Comentário
| ------------- | ------------- | -----| ---- | ------
| Tipo  | 1  | 1 | 1 | Tipo da transação
| Data  | 2  | 9 | 8 | Data da ocorrência
| Valor | 10 | 19 | 10 | Valor da movimentação. *Obs.* O valor encontrado no arquivo precisa ser divido por cem(valor / 100.00) para normalizá-lo.
| CPF | 20 | 30 | 11 | CPF do beneficiário
| Cartão | 31 | 42 | 12 | Cartão utilizado na transação 
| Hora  | 43 | 48 | 6 | Hora da ocorrência atendendo ao fuso de UTC-3
| Dono da loja | 49 | 62 | 14 | Nome do representante da loja
| Nome loja | 63 | 81 | 19 | Nome da loja

# Documentação sobre os tipos das transações

| Tipo | Descrição | Natureza | Sinal |
| ---- | -------- | --------- | ----- |
| 1 | Débito | Entrada | + |
| 2 | Boleto | Saída | - |
| 3 | Financiamento | Saída | - |
| 4 | Crédito | Entrada | + |
| 5 | Recebimento Empréstimo | Entrada | + |
| 6 | Vendas | Entrada | + |
| 7 | Recebimento TED | Entrada | + |
| 8 | Recebimento DOC | Entrada | + |
| 9 | Aluguel | Saída | - |

# Avaliação

Seu projeto será avaliado de acordo com os seguintes critérios.

1. Sua aplicação preenche os requerimentos básicos?
2. Você documentou a maneira de configurar o ambiente e rodar sua aplicação?
3. Você seguiu as instruções de envio do desafio?
4. Qualidade e cobertura dos testes unitários.

Adicionalmente, tentaremos verificar a sua familiarização com as bibliotecas padrões (standard libs), bem como sua experiência com programação orientada a objetos a partir da estrutura de seu projeto.

# Referência

Este desafio foi baseado neste outro desafio: https://github.com/lschallenges/data-engineering

---

Boa sorte!


---
---
---

# Como rodar


Primeiro é necessário instalar as dependências do projeto através do arquivo Pipfile, similar ao requirements.txt.

Em seguida basta entrar no diretório app e rodar o comando:


<code>flask run</code>


Com o flask iniciado, basta abrir um navegador no localhost:5000 e explorar a aplicação.


# Sobre o projeto

## Front-End

O formato, padrão e cores foram baseados no site da <a href='https://www.bycoders.com.br/'>bycoders</a>. Para um melhor
manuseio de navegação, foi introduzido um navbar superior, agilizando assim o posicionamento do usuário ao navegar no site.

Foi utilizado o Bootstrap 4, um framework o qual sempre uso em meus projetos por sua agilidade e facilidade em desenvolver o front-end, principalmente pois meu conhecimento em HTML/CSS não é tão avançado e certamente, caso não usasse o framework, não iria conseguir entregar o projeto como gostaria.

Há algumas nuâncias as quais gostaria de ter alterado, mas por conta de tempo finalizei ele dessa maneira. Dentre esses pontos, pode-se citar o footer, o qual eu gostaria de ter trabalhado melhor. Um outro ponto o qual gostaria de melhorar é o card central das lojas localizado na página index quando o usuário realiza o login.

No geral, acredito que o front-end poderia estar muito melhor mas creio que consegui realizar ele minimamente como imaginava no contexto da ideia do projeto e segundo a estética da <a href='https://www.bycoders.com.br/'>bycoders</a>.


## Back-End


### Banco de Dados

Na parte de back-end tive uma dificuldade grande em conseguir enviar o banco de dados que criei no PostgreSQL. Já desenvolvi outras vezes utilizando este banco de dados mas todos pessoais, não tendo a necessidade de ter algum registro prévio de dados e nem tendo que compartilhar o mesmo, armazenando na minha própria máquina local. Com isso, realizei um backup do database da minha máquina e o coloquei dentro da pasta Documents/Database caso tenha algum problema em confirmar a funcionalidade da integração do banco de dados e o projeto. Além disso, foi inserido também algumas screenshots do PgAdmin4 do PostgreSQL no diretório Documents/Database/PgAdmin4, o qual facilita o manuseio e gerenciamento dos databases e servers.

Para a aplicação funcionar corretamente, é necessário executar previamente os tipos de dados de transação na tabela Transacao, o qual pode ser encontrado no diretório Documents/Database/tb_Transacao_script.txt. Isso é necessário pois há uma relação de chaves primárias e estrangeiras para as informações dos arquivos enviados pelos usuários através do upload serem corretamente salvos nas tabelas.

Foi realizado tambem um diagrama UML através do framework DrawIo, localizado na pasta Documents/PDF e Documents/drawio. Ao ler e reler diversas vezes o escopo do desafio, fui imaginando, criando e recriando as tabelas e como poderia realizar suas interações, dependências e cardinalidades, sendo essa imagem('Documents/PDF') o seu formato final o qual parecia fazer mais sentido para o projeto.

Caso seja necessário criar um database no PostgreSQL na máquina de quem clonar o projeto, deve-se alterar os devidos campos de username, password e database_name para o recém-criado para rodar o projeto, localizado no arquivo 'app/__init__.py' na linha 25.

Normalmente, quando realizo um projeto que deve ser entregue, uso banco de dados SQLite3, por ser mais simples e ser salvo localmente ao definir sua URL em 'app/__init__.py', porém como foi delimitado os bancos permitidos, não vi outra solução a não ser essa e compartilhar as imagens do banco em funcionamento. Espero que dê certo e me desculpe previamente ^^'

### Estrutura

A estrutura de arquivos usada no desafio foi a Factory Pattern, um padrão recomendado pelo Flask em sua documentação. Essa estrutura, a qual constitui basicamente de um config, templates e blueprints, facilita as importações internas dos arquivos e classes, evitando e muito as famosas e tão irritantes circular imports.

Além disso, dentro da pasta principal do projeto('/app'), existe um diretório chamado uploads, o qual os arquivos enviados pelos usuários são salvos lá caso não exista algum com o mesmo nome.

Ainda tem o diretório tests, o qual possui um arquivo .py com alguns testes unitários utilizados no decorrer do projeto.


### Git

Nunca tinha realizado um fork e trabalho dessa maneira, achei bem interessante e inclusive sempre tive um receio de realizar um fork, desenvolver um projeto e gerar o pull request e apesar de essa não ser a proposta do desafio, certamente esse detalhe me incentivou e familiarizou com contribuições, certamente irei me envolver mais por ter mais segurança e entender mais o funcionamento e comportamento do git ao realizar um fork.

Tentei descrever da melhor forma os commits e trabalhei muito com branches, as quais facilitaram muito o andar do projeto, sem bagunçar e misturar o código de acordo com a evolução do código.


### Feedback

Eu achei muito legal realizar este desafio e para mim o que mais diferenciou ele dos outros que já realizei foi seu escopo ser voltado para algo mais voltado para o mundo real e o mercado de trabalho. A maioria dos testes de empresas possuem ideias bem legais mas as vezes muito fictícias, o qual certamente esse não é.

Ao ler a primeira vez a documentação me familiarizei com algumas características exigidas, como integração com banco de dados, testes unitários, e até a sugestão de ser realizado um sistema de login. Porém, muitos pontos eu nunca tinha realizado algo parecido, como arquivos financeiros do tipo CNAB, UPLOAD de arquivos e implementar o docker(um dos principais pontos os quais desejo estudar posteriormente).

Para conseguir entregar o projeto como imaginava, tracei uma rota a qual foi trabalhada diariamente para atingir o meu objetivo, entregar um trabalho funcional e com um front-end que fizesse sentido com a empresa e sem desviar do escopo. Tive diversas dificuldades as quais me atrasaram no decorrer da semana, prazo limite para entrega do desafio. Uma das maiores dificuldades que tive foi na parte de compartilhamento do banco de dados do PostgreSQL da minha máquina, como citado anteriormente. Estudei diversos assuntos, como backup do banco de dados, criar um novo Tablespaces, mas em tudo que tentei não consegui salvar o arquivo como gostaria, a não ser esse formato. Espero que as screenshots possam comprovar o funcionamento da aplicação e que isso não seja um problema muito grande.

Gostaria de ter desenvolvido outras funcionalidades, como um arquivo de log com as atividades de registro, login, envio de arquivos e pesquisa por lojas, mas devido ao deadline decidi deixar como um bônus caso sobrasse tempo, me dedicando ao core do escopo. Além disso, tentei disponibilizar os dados em formato de tabela ao pesquisar os dados de uma loja em específico, mas novamente o tempo me limitou e decidi disponibilizar em formato JSON. Enquanto pesquisava sobre upload de arquivos na linguagem Python, tive a ideia de desenvolver um download dos arquivos e pesquisas das lojas para os usuários. Por fim, gostaria de ter realizado também uma página de administrador a parte para manusear e gerenciar os componentes da aplicação, como usuários, arquivos e lojas mas ficou apenas no desejo devido o tempo.

Gostei muito de ter realizado o desafio, me agregou infinitamente na minha jornada de me tornar um programador back-end e agradeço muito pela oportunidade de poder realizar. A característica dele de ser uma ideia prática e voltada para o mundo real foi incrível e como participante de processos seletivos espero que continuem com essa linha de testes pois além de eles serem mais ricos, o conhecimento obtido ao realizar eles é imensurável. Fiquei muito contente e até impressionado em como algumas funcionalidades relativamente simples, como o upload, podem ser extremamente eficazes e uma carta na manga para se ter sempre disponível.

---

Espero que a estética do front-end e a lógica do back-end(e toda a saga do banco de dados) estejam de acordo.
Obrigado novamente pela oportunidade e conhecimento compartilhado e espero que você encontre o que busca nesse desafio-dev!
=]

