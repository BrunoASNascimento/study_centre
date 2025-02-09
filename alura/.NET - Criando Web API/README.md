# .NET - Criando Web API

## Apresentação

Boas-vindas! Meu nome é Daniel Artine, serei seu instrutor neste curso de API Rest com .NET 6.

Daniel Artine é uma pessoa de pele clara, olhos castanhos escuros e cabelos pretos curtos. Usa barba e bigode, veste uma camiseta cinza escura e está sentado em uma cadeira preta. Ao fundo, há uma parede com iluminação azul.

O que vamos aprender?
Ao longo deste treinamento, estudaremos os verbos HTTP e focaremos em responder as seguintes questões:

Como se constrói uma API?
O que é uma API?
Quando e como utilizar uma API?
Por que utilizar uma API?
Construiremos nosso projeto com base em uma API de filmes, com a qual que conseguiremos cadastrar filmes, além de recuperar informações, atualizar dados de diferentes maneiras (com o verbo PUT e com verbo PATCH) e deletar filmes. Ao final do curso, também estudaremos como documentar APIs utilizando Swagger.

A nível de código, vamos:

desenvolver nosso construtor
utilizar DTOs para criar, ler e atualizar filmes
fazer conexões com banco de dados, usando Entity Framework
realizar conversões entre diferentes tipos, com o AutoMapper
Vale ressaltar que seguiremos a nova convenção do .NET 6, tendo um arquivo Program.cs e não dependendo mais de um Startup.cs. Desenvolveremos o projeto de uma maneira bem minimalista.

Espero que aproveitem o curso. Caso tenham dúvidas, não deixem de perguntar. Bons estudos!

## Preparando o ambiente

Nesta aula, vamos preparar nosso ambiente de trabalho, fazendo a instalação de todas as ferramentas necessárias para dar continuidade aos nossos estudos. Como vamos desenvolver o projeto no Windows, mostraremos as instalações e configurações nessa plataforma em específico, mas sempre que possível daremos indicações de como realizar esses processos no Linux, caso você precise trabalhar com esse sistema.

Baixando os instaladores
A primeira ferramenta necessária é o Visual Studio Community 2022. Ao acessar o site na página de downloads, basta clicar no botão roxo "Download gratuito" referente à versão "Comunidade".

Caso você esteja no Linux, você pode usar o Visual Studio Code, um editor de texto bastante poderoso que, às vezes, se compara a uma IDE.

A próxima ferramenta é o MySQL 8.0.31. Na [https://dev.mysql.com/downloads/windows/installer/8.0.html](página de download), há duas opções. Vamos baixar a segunda: o instalador completo (de 431.7 MB). Ao clicar no botão azul "Download" à direita dessa opção, seremos direcionados a uma janela sugerindo que criemos uma conta Oracle. Não é preciso criar a conta, basta clicar no link "No thanks, just start mu download" no final da página, para simplesmente baixar o instalador.

A seguir, vamos baixar do Postman. Na página de downloads do Postman, basta clicar no botão laranja "Windows 64-bit". Essa ferramenta servirá para fazermos requisições de maneira mais prática, visualizar as respostas, preencher o corpo da requisição etc.

Também precisaremos no .NET 6. Na página de downloads do .NET, faremos o download da versão 6.0.402, conforme nosso sistema (Arm64, x64 ou x86).

Caso você esteja no Linux Ubuntu, a Microsoft tem uma documentação explicando passo a passo como fazer essa instalação. Na lateral esquerda dessa página, há tutoriais de outras distribuições, como: Alpine, CentOS, Debian, Fedora e OpenSUSE.

Instalando as ferramentas
Agora que centralizamos nossos instaladores, passaremos para os processos de instalação em si. O Postman e o .NET são bem simples, basta clicar no botão "Next" diversas vezes até finalizar, você pode fazer por conta própria. Já o Visual Studio e o MySQL têm algumas peculiaridades, então focaremos neles a seguir.

Visual Studio e cargas de trabalho
Primeiramente, vamos executar o instalador do Visual Studio Community 2022. Logo de início, será aberta uma caixa de diálogo explicando que algumas atualizações são necessárias, então clicaremos no botão "Continuar" no canto direito inferior.

Em seguida, a janela de instalação será aberta. Na parte esquerda da tela, há um retângulo referente ao Visual Studio Community 2022, em que temos o botão "Instalar" à direita. Caso você já tenha o Visual Studio instalado, você terá o botão "Modificar" no lugar.

Clicando no botão "Instalar" (ou "Modificar"), precisamos definir as cargas de trabalho que queremos instalar. Vamos selecionar a opção "ASP.NET e desenvolvimento Web". No painel à direita, temos os detalhes da instalação — não vamos modificar nada nessa seção.

Para agilizar o processo e ocupar menos memória do computador, recomendamos desmarcar qualquer outra carga de trabalho, já que neste curso usaremos apenas "ASP.NET e desenvolvimento Web".

No canto inferior direito, podemos escolher entre duas opções de instalação:

Instalar durante o download
Baixar tudo, depois instalar
Marque a opção que você preferir, de acordo com a velocidade da sua internet. Por fim, clicaremos no botão "Instalar" (ou "Modificar") no canto direito inferior.

MySQL e seus componentes
Agora, vamos executar o instalador do MySQL. De início, ele pedirá permissão no sistema para continuar e depois fará a extração dos itens necessários. Em seguida, será aberta a janela do instalador.

Na primeira tela, selecionaremos a opção "Custom" para fazer uma instalação customizada e clicaremos no botão "Next" no canto direito inferior.

Na segunda tela, vamos definir os elementos que queremos instalar. No painel à esquerda, selecionaremos "MySQL Servers > MySQL Server > MySQL Server 8.0 > MySQL Server 8.0.31 - X64". Em seguida, pressionaremos a seta para a direita (na tela ou no teclado do computador) para adicionar esse componente à lista à direita.

Ainda no painel à esquerda, selecionaremos "Applications > MySQL Workbench > MySQL Workbench 8.0 > MySQL Workbench 8.0.31 - X64" e pressionaremos a seta para a direita novamente. Assim, o painel à direita terá a seguinte lista de componentes a serem instalados:

MySQL Server 8.0.31 - X64
MySQL Workbench 8.0.31 - X64
Vamos clicar no botão "Next" no canto direito inferior para prosseguir. Na próxima tela, podemos indicar o diretório de instalação e clicar em "Next". Caso o diretório já exista, o instalador mostrará um aviso, vamos clicar em "Yes".

Na próxima tela, temos a listagem do que será instalado. Basta clicar no botão "Execute" no canto direito inferior. Essa instalação pode ser um pouco demorada.

Enquanto a instalação é feita, fique à vontade para explorar o projeto no GitHub e saciar sua curiosidade sobre tudo que aprenderemos ao longo do curso.

Nós vamos estudar as novidades do .NET 6, entendendo a questão dos namespaces (file-scoped e block-scoped). Também aprenderemos a criar um controlador, modelos e DTOs.

Finalizado o processo, clicaremos em "Next". Na próxima tela, em "Next" mais uma vez para começar a configuração.

Na próxima tela, vamos manter as configurações padrões:

Config Type: Development Computer
Port: 3306
X Protocol Port: 33060
Pressionando o botão "Next", precisamos definir o método de autenticação. Para não nos preocuparmos com a questão de criptografia de senhas e afins, selecionaremos "Use Legacy Authentication Method" e clicaremos em "Next".

Agora, definiremos a nossa senha. Por ora, podemos deixá-la como "root" e clicar em "Next". Não alteraremos nada nas próximas páginas, basta clicar em "Next", "Next" e "Execute".

Caso você esteja usando o Linux, o MySQL está no repositório padrão. Você pode instalá-lo com o apt no Ubuntu.

Ao final, todas as instalações e configurações de ambientes estarão prontas!

## O que é uma API

Antes de começar a desenvolver nosso projeto, vamos entender o que são APIs e para que servem.

Primeiramente, "API" é a sigla para o termo "Application Programming Interface" — em português, interface de programação de aplicações. Mas o que isso significa?

Para entender o conceito de API, pensaremos num exemplo relacionado a filmes, já que nosso projeto terá esse tema. Vamos imaginar que o cliente 1 deseja conferir informações sobre o filme "O senhor dos anéis" pelo computador. Por exemplo, o título, o ano de lançamento, o nome do diretor, o gênero e o tempo de duração.

A máquina do cliente fará uma requisição para o servidor. O servidor, por sua vez, consultará os dados cadastrados no banco de dados e os enviará para o servidor, que mandará a resposta de volta para o cliente.

Diagrama de requisição de dados. No canto esquerdo superior, o cliente 1 é representado pela ilustração de um monitor de computador. Em sua tela, há dados do filme "O senhor do anéis". No centro do diagrama, temos um servidor representado por outro monitor. Em sua tela, temos a letra N maiúscula e vermelha, semelhante ao logotipo da empresa Netflix. À direita do diagrama, temos um banco de dados representado por um cilindro segmentado. Há 4 setas: do cliente 1 ao servidor (requisição); do servidor ao banco de dados; do banco de dados ao servidor; e do servidor ao cliente 1 (resposta)

O cliente 2 está utilizando um aplicativo no smartphone ou o próprio navegador do celular e deseja obter as mesmas informações para outros fins. Será que a resposta enviada ao cliente 1 pode ser o mesmo tipo de resposta dada ao cliente 2?

O mesmo diagrama de requisição de dados, com informações extras. No canto esquerdo inferior, o cliente 2 é representado por um smartphone. Uma seta aponta do cliente 2 ao servidor, outra seta aponta do servidor ao cliente 2. Abaixo dessa segunda seta, há vários pontos de interrogação.

Cada cliente pode estar esperando dados em determinado escopo. O servidor precisa sempre estar atento a que tipo de resposta deve ser enviado. Como podemos solucionar essa questão?

Em vez de um servidor, os clientes podem enviar requisições para uma API. Ela será responsável por resolver esse pedido e dar uma resposta que os clientes consigam utilizar os dados designados.

Mas como a API consulta os dados e os devolve para o usuário? No final das contas, isso não importa! O processo é análogo ao conceito de orientação a objetos: basta que sigamos as regras impostas pela interface para receber a resposta padronizada, que pode ser consumida pelos nossos clientes.

Diagrama do uso de uma API. A disposição dos elementos é semelhante aos diagramas anteriores. No canto esquerdo superior, temos o cliente 1 representado por um monitor. No canto esquerdo inferior, temos o cliente 2 representado por um smartphone. Os clientes estão dentro de uma área retangular denominada "Consumidores". No centro do diagrama, temos a API RESTful representada por um quadrado com a letra N maiúscula e vermelha. Na parte direita do diagrama, temos a ilustração de uma cartola com uma varinha mágica e pequenas estrelas brilhantes. Abaixo dela, está escrito "Não importa!". Há 6 setas: do cliente 1 até a API; do cliente 2 até a API; da API até a cartola; da cartola até a API; da API até o cliente 1; e da API até o cliente 2.

Em outras palavras, podemos imaginar a API como uma "casca" que contém um conjunto de regras. Cada cliente que quiser consumir da API, conseguirá interagir com esse sistema, desde que siga essas regras.

Quando implementamos determinado conjunto de regras arquiteturais, um dos mais difundidos é o REST — Representational State Tranfer. Seguindo esse padrão, sempre saberemos o que vamos receber e o que precisamos enviar nas duas pontas, de modo que a comunicação fica padronizada.

Ao segue o padrão REST, uma API é chamada de API RESTful. Ou seja, REST é o nome do conceito arquitetural e RESTful é quem implementa esse conceito.

Recapitulando: os clientes (consumidores) fazem requisições para a API RESTful e não importa como funciona a lógica por trás da API não importa. Pode ser um banco de dados (relacional ou não) ou estar em memória. Desde que os consumidores sigam as regras impostas pela API, eles receberam os dados.

Assim, a API visa disponibilizar informações para outras aplicações, seja para operações de escrita, leitura, atualização ou remoção.

Para consumir seus recursos, é necessário seguir as regras estabelecidas (que entenderemos ao longo do curso). Como as APIs abstraem detalhes de implementação, não precisamos compreender como o back-end está sendo implementado.

Além disso, APIs controlam o que pode ou deve ser acessado. Se criamos um endpoint para devolver determinada informação para o usuário, conseguimos ter um ótimo controle do que será exposto ou não a quem consome a API.

Tendo esses conceitos fixados, vamos partir para a prática na próxima aula!

## Criando um projeto .NET 6

Caso você esteja usando Linux e Visual Studio Code, mais adiante o instrutor explicará como criar um projeto com esse editor de texto também.

Criando um projeto com Visual Studio 2022
Vamos abrir o Visual Studio 2022 para criar nosso projeto. À direita da tela inicial, na seção "Introdução", clicaremos na opção "Criar um projeto".

Na barra de pesquisa (cujo atalho é "Alt + S"), vamos buscar por "api" e selecionar o modelo "API Web do ASP.NET Core" com C#. Depois, pressionaremos o botão "Próximo" no canto direito inferior.

Na próxima tela, definiremos o nome do projeto e o nome da solução. Ambos se chamarão "FilmesApi". Além disso, você pode escolher o diretório de criação do projeto, conforme sua preferência. Em seguida, clicaremos no botão "Próximo".

O passo seguinte é escolher o framework. Vamos utilizar o .NET 6.0 (Suporte de longo prazo) — ou seja, o LTS. Em seguida, clicaremos em "Criar" no canto inferior direito da tela.

O .NET 7 ainda não está na versão LTS. Não é recomendado ter projetos (seja em produção ou prontos para produção) com frameworks sem a versão LTS, pois perdemos o suporte tanto da comunidade quanto da própria empresa que desenvolveu a ferramenta.

Arquivos iniciais
O Visual Studio criará uma base para o nosso projeto, com alguns arquivos iniciais que exploraremos a seguir. Nós vamos acessá-los usando o gerenciador de soluções, à direita da IDE.

Caso o gerenciador não esteja aparecendo na sua tela, basta usar o atalho "Ctrl + Alt + L" ou clicar em "Exibir > Gerenciador de Solução" no menu superior do Visual Studio.

No gerenciador de soluções, temos:

a pasta "Properties"
a pasta "Controllers"
o arquivo appsettings.json
o arquivo appsettings.Development.json
o arquivo Program.cs
o arquivo WeatherForecast.cs
O arquivo WeatherForecast.cs é um modelo para exemplificar uma API base do .NET. Por enquanto, vamos mantê-lo no projeto, pois executaremos a aplicação para entender como interagimos com a API.

O Program.cs é onde nossa aplicação é iniciada e onde temos as definições dos serviços que utilizaremos nela, bem como as dependências necessárias, entre outras informações.

Caso você já tenha usado versões anteriores do .NET, provavelmente reparou que esse arquivo é bem minimalista — não há definição de classe nem do escopo do namespace. A partir do .NET 6, não precisamos mais fazer essas definições. Basta criar o builder, gerar a aplicação e executá-la, em linhas enfileiras. Ao longo do curso, modificaremos bastante o arquivo Program.cs e não precisaremos nos preocupar com questões de indentação. Entre outras vantagens, o código ficará mais legível.

Caso o .NET 6 seja sua primeira experiência com a criação de APIs, saiba que não é necessário ter conhecimentos de versões anteriores.

Nos arquivos appsettings.json e appsettings.Development.json, definimos informações que serão carregadas durante a execução da nossa aplicação, como o endereço do banco de dados ou as credenciais usadas em determinado serviço.

Na pasta "Controllers", temos os controladores. Como o nome sugere, trata-se de classes responsáveis pelo controle. Elas recebem e respondem às requisições dos usuários que interagem com a API. Por ora, temos apenas o arquivo WeatherForecastController.cs. O uso do sufixo "Controller" no nome é uma convenção para indicar o papel da classe. Perceba que o próprio .NET adotou essa convenção ao gerar o arquivo WeatherForecastController.cs.

Da linha 5 a 7 desse arquivo, vale notar o uso da extensão : ControllerBase e das anotações [ApiController] e [Route], importantes para o funcionamento do controlador .NET. Vamos aprender sobre elas mais adiante:

[ApiController]
[Route("[controller]")]
public class WeatherForecastController : ControllerBaseCopiar código
Ainda nesse arquivo, temos definições de atributos estáticos, como o Summaries (linha 9), \_logger (linha 14) e o construtor (linha 16). Ao final, temos um método chamado Get() que não recebe parâmetro nenhum e cujo retorno é um enumerável de WeatherForecast.

Apesar deste curso ser voltado para quem está começando a aprender sobre APIs com .NET, é importante que você já tenha uma base de conhecimento sobre C#. Por exemplo, não vamos explicar o que é uma lista, um enumerável ou como implementar uma interface. O foco do treinamento é entender a criação de APIs e conhecer os padrões a serem seguidos.

Sabemos que o controller é responsável por receber e responder requisições dos usuários, porém como ele sabe que deve chamar esse método Get()? Em breve, vamos executar nossa aplicação para entender como esse processo funciona.

Antes disso, vamos explorar o arquivo launchSettings.json, na pasta "Properties". A partir da linha 11, temos alguns profiles, perfis para a nossa aplicação. O que nos interessa é o trecho referente a "FilmesApi". Inclusive, vamos apagar o trecho do "IIS Express". O arquivo ficará assim:

{
"$schema": "https://json.schemastore.org/launchsettings.json",
"iisSettings": {
"windowsAuthentication": false,
"anonymousAuthentication": true,
"iisExpress": {
"applicationUrl": "http://localhost:23847",
"sslPort": 44335
}
},
"profiles": {
"FilmesApi": {
"commandName": "Project",
"dotnetRunMessages": true,
"launchBrowser": true,
"launchUrl": "swagger",
"applicationUrl": "https://localhost:7106;http://localhost:5106",
"environmentVariables": {
"ASPNETCORE_ENVIRONMENT": "Development"
}
}
}
}Copiar código
Para salvar as alterações, pressionaremos "Ctrl + S".

Na linha 17 desse arquivo, temos a applicationUrl. Com protocolo HTTPS, usamos o localhost, na porta 7106. Com protocolo HTTP, a porta 5106. Na linha 15, temos a configuração lauchBrowser: true, de modo que o navegador será aberto automaticamente, quando a aplicação for iniciada.

Executando a aplicação
A seguir, vamos executar a aplicação. No menu superior da IDE, temos o símbolo de uma seta para a direita com preenchimento verde claro. À sua direita, há uma pequena seta branca para baixo. Clicaremos nela e selecionaremos "FilmesApi". Não queremos WSL.

Em seguida, vamos iniciar sem depurar, clicando no símbolo de seta para a direita com o contorno verde claro, sem preenchimento. Alternativamente, podemos pressionar "Ctrl + F5". A aplicação será aberta no navegador.

Estamos trabalhando com uma API e o foco não é front-end, contudo note que nossa aplicação tem uma tela bonita, bem estruturada e interativa, com links clicáveis. Esse resultado é obtido com o Swagger. Estudaremos mais sobre ele no final deste curso.

Abaixo do título "WeatherForecast", temos a seção "GET /WeatherForecast", indicando que podemos acessar este caminho. Vamos clicar nela para expandi-la. Em seguida, clicaremos no botão "Try it out" (Testar), no canto superior direito da área expandida e, depois, em "Execute".

Mais abaixo, no tópico "Server Response", recebemos um response body com status code 200 e informações de data e temperatura. Examinando esse retorno, reparamos que ele nada mais é que um enumerável convertido em array, como conferimos no método Get() do nosso controlador.

Analisando o tópico "Curl", sabemos que a rota utilizada foi https://localhost:7106/WeatherForecast. No arquivo lauchSettings.json, verificamos há pouco que o caminho em que nossa aplicação está sendo executada é https://localhost:7106. Mas como o controlador sabe que, com /WeatherForecast, ele deve executar o método Get()?

Anteriormente, reparamos que o nome da classe WeatherForecastController segue a convenção de usar o sufixo "Controller". Na anotação [Route("[controller]")] na linha 6, os colchetes indicam que devemos selecionar o prefixo do nome da classe e colocá-lo no lugar de [controller]. Ou seja, o controlador interpretará a rota como [Route("WeatherForecast")].

A vantagem de usar a anotação [Route("[controller]")] em vez de [Route("WeatherForecast")] é que, se eventualmente alterarmos o nome da classe, não será necessário adaptar a anotação também. Assim, tudo fica mais prático e fácil.

Além disso, imediatamente acima do método Get(), temos a seguinte anotação:

[HttpGet(Name = "GetWeatherForecast")]Copiar código
O HttpGet é uma das operações que podem ser executadas em uma API. Na nossa aplicação, foi exatamente essa ação que executamos ao expandir a seção "GET /WeatherForecast" e pressionar o botão "Execute".

Dessa forma, o controlador sabe que, ao acessar a rota /WeatherForecast com o verbo GET, ele deve executar toda a lógica do método Get()!

Não se preocupe se esse processo não ficou muito claro ainda. Ao longo do curso, vamos recriar essa lógica com nossas próprias rotas e aprender mais a fundo como tudo funciona. Por enquanto, a ideia era apenas visualizar esse escopo inicial.

Namespace com escopo de arquivo
No arquivo WeatherForecastController.cs, note que todo o código está indentado para que a classe e as anotações fiquem dentro de um namespace, em um bloco de chaves. O .NET 6 oferece um recurso para aprimorar essa estrutura. Posicionando o cursor sobre o nome do namespace (linha 3), pressionaremos "Alt + Enter" e selecionaremos "Converter em namespace com escopo de arquivo". Assim, o código ficará indentado mais à esquerda e o bloco de chaves do namespace é removido. O projeto torna-se mais centralizado e legível dessa forma.

Criando um projeto com Visual Studio Code
Até agora, usamos apenas o Visual Studio 2022. Caso você tenha optado pelo Visual Studio Code, há duas extensões que recomendamos instalar para desenvolver projetos .NET. No painel à esquerda do VS Code, basta acessar a aba "Extensions" e pesquisar as seguintes extensões:

C# (da Microsoft)
C# Snippets (de Jorge Serrano)
Em seguida, vamos criar um projeto via linha de comando. No menu superior do VS Code, selecionaremos "Terminal > New Terminal". Alternativamente, podemos usar o atalho "Ctrl + Shift + '".

Um novo terminal será aberto na parte inferior da tela. Vamos criar uma pasta chamada "projetolinux", com o seguinte comando:

mkdir projetolinuxCopiar código
Em seguida, vamos acessar a pasta:

cd projetolinuxCopiar código
E abrir uma nova instância do Visual Studio Code nela:

code .Copiar código
Na nova instância, abriremos o terminal novamente, com "Ctrl + Shift + '". Para criar um projeto .NET, rodaremos o seguinte comando:

dotnet new webapi --name FilmesApiCopiar código
Assim, criaremos um modelo de Web API com o nome "FilmesApi". No painel à esquerda, temos a mesma estrutura de pastas que teríamos no Visual Studio 2022!

Para executar o projeto, basta rodar o seguinte comando no terminal:

dotnet run --project FilmesApi/FilmesApi.csprojCopiar código
Após a compilação, serão mostradas várias informações no terminal, como o endereço de execução da aplicação. No caso, no localhost, na porta 7174 com protocolo HTTPS, ou na porta 5177 com HTTP. Basta dar um "Ctrl + Clique" sobre o endereço para acessá-lo no navegador.

Inicialmente, teremos um erro, pois é preciso acessar o endereço com /swagger ao final. Portanto, usaremos o seguinte endereço:

https://localhost:7174/swagger/index.htmlCopiar código
O foco dessa aula foi apenas criar o projeto, conferir algumas particularidade do .NET 6 e entender como interagir com uma API. Caso tenha ficado alguma dúvida, não se preocupe! Na próxima aula, vamos recriar toda essa lógica do início ao fim com nossos próprios controladores e modelos. Pensaremos como apagar os elementos de weather forecast e começar a migrar para o nosso conceito de filmes.

## Recebendo os dados de um filme

Agora, vamos criar efetivamente as partes de cadastro, leitura, alteração e remoção de filmes, começando pelo cadastro.

Primeiramente, vamos apagar os arquivos WeatherForecastController.cs e WeatherForecast.cs.

Nosso objetivo será que, ao enviar uma requisição para /filme, nossa API faça uma operação de escrita. Ou seja, vamos salvar as informações de um filme na nossa aplicação.

Criando um controlador
Para expor um caminho ou endpoint para que alguém possa acessar, precisamos criar um controlador. Portanto, no gerenciador de soluções, clicaremos com o botão direito do mouse sobre a pasta "Controllers" e selecionaremos "Adicionar > Classe...".

Uma nova janela será aberta. Na parte inferior dela, nomearemos a nova classe de "FilmeController". Vale ressaltar que a palavra "Controller" possui duas letras L — usar a grafia incorreta pode causar problemas no projeto.

O resultado será a classe FilmeController, inicialmente vazia:

namespace FilmesApi.Controllers
{
public class FilmeController
{
}
}Copiar código
Vamos posicionar o cursor sobre o namespace, pressionar "Ctrl + Enter" e selecionar "Converter em namespace com escopo de arquivo". Assim, ganhamos mais espaço e centralizamos nosso conteúdo.

Para que essa classe seja um controlador e esteja hábil a lidar com requisições de usuários, precisamos adicionar alguns elementos. A primeira delas são as anotações [ApiController] e [Route], antes da definição da classe:

namespace FilmesApi.Controllers;

[ApiController]
[Route]
public class FilmeController
{

}Copiar código
Quando o usuário enviar uma requisição para /filme, queremos atingir este controlador. Portanto, indicaremos que rota é para o nome do controlador. Como aprendemos anteriormente, podemos fazer essa indicação com colchetes:

namespace FilmesApi.Controllers;

[ApiController]
[Route("[controller]")]
public class FilmeController
{

}Copiar código
Atualmente, as anotações estão sublinhadas em vermelho como uma indicação de erro, pois faltam algumas importações. Basta posicionar o cursor sobre [ApiController], pressionar "Alt + Enter" e selecionar "using Microsoft.ApsNetCore.Mvc":

using Microsoft.AspNetCore.Mvc;

namespace FilmesApi.Controllers;

[ApiController]
[Route("[controller]")]
public class FilmeController
{

}Copiar código
Além disso, é necessário que a classe FilmeController seja uma extensão do ControllerBase:

using Microsoft.AspNetCore.Mvc;

namespace FilmesApi.Controllers;

[ApiController]
[Route("[controller]")]
public class FilmeController : ControllerBase
{

}Copiar código
A seguir, vamos desenvolver um método chamado AdicionaFilme() para cadastrar um filme no sistema. A princípio, não vamos nos preocupar com o tipo de retorno, apenas usaremos o void:

using Microsoft.AspNetCore.Mvc;

namespace FilmesApi.Controllers;

[ApiController]
[Route("[controller]")]
public class FilmeController : ControllerBase
{
public void AdicionaFilme()
{

    }

}Copiar código
Ao receber uma requisição para /filme, receberemos por parâmetro as informações do filme que será cadastrado. Esse parâmetro será um objeto do tipo Filme, que chamaremos de filme:

// código anterior omitido

public class FilmeController : ControllerBase
{
public void AdicionaFilme(Filme filme)
{

    }

}Copiar código
Em seguida, adicionaremos esse filme a uma lista chamada filmes:

// ...

public class FilmeController : ControllerBase
{
public void AdicionaFilme(Filme filme)
{
filmes.Add(filme);
}
}Copiar código
No entanto, há dois pontos importantes. Nós precisamos:

criar essa lista de filmes.
criar a classe Filme, que representa um filme.
Vamos começar pelo primeiro item, que é mais simples. Antes do método AdicionaFilme(), criaremos uma lista estática e privada, chamada filmes:

// ...

public class FilmeController : ControllerBase
{

    private static List<Filme> filmes = new List<Filme>();

    public void AdicionaFilme(Filme filme)
    {
        filmes.Add(filme);
    }

}Copiar código
Na sequência, criaremos nossa classe.

Criando um modelo
A fim de manter a organização do nosso projeto, vamos inserir uma pasta que conterá nossos modelos, que mapearemos do mundo real para o mundo .NET. No gerenciador de soluções, clicaremos com o botão direito sobre "FilmesApi", selecionaremos "Adicionar > Nova Pasta" e a chamaremos de "Models".

Depois, clicaremos com o botão direito sobre a pasta "Models", selecionaremos "Adicionar > Classe...". Na parte inferior da nova janela, nomearemos a nova classe de "Filme". O resultado será a classe Filme, inicialmente vazia:

namespace FilmesApi.Models
{
public class Filme
{
}
}Copiar código
Vamos posicionar o cursor sobre o namespace, pressionar "Alt + Enter" e selecionar "Converter em namespace com escopo de arquivo".

Agora, pensaremos nas propriedades de um filme. Existem inúmeras informações relevantes de um filme — neste curso, trabalharemos com:

título
gênero
tempo de duração
Para adicionar uma propriedade, podemos digitar "prop" e pressionar a tecla "Tab" duas vezes para gerar um modelo e adaptá-lo. Nosso modelo Filme, com as três propriedades, ficará assim:

namespace FilmesApi.Models;

public class Filme
{
public string Titulo { get; set; }
public string Genero { get; set; }
public int Duracao { get; set; }
}Copiar código
Após salvar o arquivo, vamos voltar ao FilmeController.cs e fazer a importação do namespace em questão. Posicionando o cursor sobre Filme (sublinhado em vermelho), pressionaremos "Alt + Enter" e selecionaremos "using FilmeApi.Models":

using FilmesApi.Models;
using Microsoft.AspNetCore.Mvc;

namespace FilmesApi.Controllers;

[ApiController]
[Route("[controller]")]
public class FilmeController : ControllerBase
{

    private static List<Filme> filmes = new List<Filme>();

    public void AdicionaFilme(Filme filme)
    {
        filmes.Add(filme);
    }

}Copiar código
A princípio, tudo está funcionando! O Visual Studio não está mostrando mais nenhuma indicação de erro.

Anteriormente, quando fizemos uma requisição GET para WeatherForecast, estávamos recuperando e lendo uma informação do nosso sistema. Agora, nosso objetivo é escrever dados, criando algo dentro do sistema. Portanto, em lugar do verbo GET, usaremos o verbo POST.

Se em WeatherController usamos a anotação [HttpGet], dessa vez utilizaremos o [HttpPost]:

// ...

public class FilmeController : ControllerBase
{

    private static List<Filme> filmes = new List<Filme>();

    [HttpPost]
    public void AdicionaFilme(Filme filme)
    {
        filmes.Add(filme);
    }

}Copiar código
Dessa maneira, sempre que fizermos uma operação do tipo POST para o controlador de prefixo "Filme", cadastraremos o filme recebido por parâmetro. Apesar de recebê-lo por parâmetro, as informações são enviadas através do corpo da requisição e, para explicitar esse fato, usaremos a anotação [FromBody]:

// ...

public class FilmeController : ControllerBase
{

    private static List<Filme> filmes = new List<Filme>();

    [HttpPost]
    public void AdicionaFilme([FromBody] Filme filme)
    {
        filmes.Add(filme);
    }

}Copiar código
Sendo assim, definimos que o filme virá pelo corpo da requisição e conterá informações de título, gênero e tempo de duração. Com o método AdicionaFilmes(), adicionaremos esse elemento à lista filmes. Por ora, não estamos nos preocupando em como esse dado será armazenado, vamos simplesmente colocá-lo em uma lista. Mais adiante, podemos melhorar elaborar esses processos.

Como validação, vamos inserir alguns Console.WriteLine() para exibir o título e a duração do filme:

// ...

public class FilmeController : ControllerBase
{

    private static List<Filme> filmes = new List<Filme>();

    [HttpPost]
    public void AdicionaFilme([FromBody] Filme filme)
    {
        filmes.Add(filme);
        Console.WriteLine(filme.Titulo);
        Console.WriteLine(filme.Duracao);
    }

}Copiar código
Em seguida, vamos executar nossa aplicação. No menu superior do Visual Studio, basta pressionar o ícone de play com borda verde, ou usar o atalho "Ctrl + F5". Como usamos a configuração launchBrowser: true no arquivo launchSettings.json, a aplicação será executada no navegador, novamente com o Swagger.

Por enquanto, não nos interessa abrir o browser, então vamos alterar essa configuração e alterar seu valor para false:

// código anterior omitido

"profiles": {
"FilmesApi": {
"commandName": "Project",
"dotnetRunMessages": true,
"launchBrowser": false,
"launchUrl": "swagger",
"applicationUrl": "https://localhost:7106;http://localhost:5106",
"environmentVariables": {
"ASPNETCORE_ENVIRONMENT": "Development"
}
}
}Copiar código
A partir de agora, quando executarmos a aplicação, apenas um console será aberto e utilizaremos o Postman para interagir com a nossa API.

Postman
Na interface do Postman, temos um menu superior, um painel na lateral esquerda e uma grande área central denominada workbench. No canto superior esquerdo dessa área, clicaremos no símbolo de "+" para criar uma nova requisição.

Uma nova aba será criada, chamada "Untitled Request". À esquerda do método GET, vamos digitar a seguinte URL:

https://localhost:7106/filmeCopiar código
No menu seguinte, selecionaremos a aba "Body". Depois, vamos marcar "raw" e trocar a opção "Text" para "JSON". Dessa forma, enviaremos um texto no corpo da requisição no formato JSON.

Como estamos usando o padrão arquitetural REST, é comum trafegar dados através de JSON — JavaScript Object Notation. Assim, facilitamos a maneira como trafegamos a informação e sabemos como ela será recebida ou enviada entre os diferentes consumidores e servidores do nosso sistema.

Na sequência, temos a área onde criaremos o nosso JSON. Colocaremos o título, o gênero e o tempo de duração:

{
"Titulo" : "Alura Filmes",
"Genero" : "Aventura",
"Duracao" : 180
}Copiar código
Em seguida, vamos clicar no botão azul "Send", à direita da URL que definimos. No painel inferior do Postman, o resultado será o seguinte:

Status: 405 Method Not Allowed

Ou seja, "método não permitido". Enviamos um GET para https://localhost:7106/filme, mas nosso controlador está preparado para lidar com um POST. Então, à esquerda da URL que acabamos de digitar, vamos substituir o verbo GET por POST e clicar no botão "Send" novamente.

Agora, no painel inferior do Postman, temos o seguinte resultado:

Status: 200 OK

Acessando o console que foi aberto quando iniciamos a aplicação, notaremos que foram impressas as seguintes linhas:

Alura Filmes

180

Essas mensagens comprovam que passamos pelo método AdicionaFilme() e inserimos um filme na nossa lista! Mais adiante, descobriremos como ler a nossa lista de filmes.

Validação de dados
Há pouco, enviamos os seguintes dados de um filme, via Postman:

{
"Titulo" : "Alura Filmes",
"Genero" : "Aventura",
"Duracao" : 180
}Copiar código
No entanto, o usuário poderia escrever informações erradas, com caracteres inválidos, por exemplo:

{
"Titulo" : "Alura Filmes----------!@#!@#!@#",
"Genero" : "Televisão",
"Duracao" : 180000
}Copiar código
É necessário validar a entrada do usuário, verificando o que pode ou não ser enviado ao sistema. Na próxima aula, estudaremos como validar informações, por exemplo, quais são os tamanhos mínimo e máximo permitidos de um campo.

## Validando parâmetros recebidos

A seguir, vamos aprender como validar os dados enviados pelo usuário. No Postman, vamos inserir o seguinte JSON no corpo da requisição:

{
"Titulo" : "Avatar",
"Genero" : "Ação",
"Duracao" : 162
}Copiar código
Aparentemente, esses dados são válidos. Ao clicar no botão "Send", conseguimos inserir o filme no nosso sistema e obtemos o seguinte resultado no painel inferior do Postman:

Status: 200 OK

O que aconteceria se enviássemos dados inválidos? Vamos testar, informando um caractere de espaço como título do filme e gênero, e uma duração de -120 minutos:

{
"Titulo" : " ",
"Genero" : " ",
"Duracao" : -120
}Copiar código
Ao clicar no botão "Send", recebemos o mesmo resultado:

Status: 200 OK

Conseguimos inserir esses dados, sem problemas, porém essa ação não deveria ser permitida. A seguir, vamos explorar como validar essas informações para garantir algumas condições, como duração mínima ou máxima, bem como um título ou gênero que não sejam vazios.

Validação de dados: condicionais
Uma solução seria incluir algumas validações no nosso código, no método AdicionaFilme(). Por exemplo, antes de adicionar o filme, podemos inserir uma estrutura if para verificar se o título é vazio ou nulo:

// ...

[HttpPost]
public void AdicionaFilme([FromBody] Filme filme)
{
if (!string.IsNullOrEmpty(filme.Titulo))
{
filmes.Add(filme);
Console.WriteLine(filme.Titulo);
Console.WriteLine(filme.Duracao);
}
}Copiar código
Também é preciso checar se o gênero não é vazio e se a duração é de, ao menos, 70 minutos (tempo mínimo para um longa-metragem):

// ...

[HttpPost]
public void AdicionaFilme([FromBody] Filme filme)
{
if (!string.IsNullOrEmpty(filme.Titulo) &&
!string.IsNullOrEmpty(filme.Genero) &&
filme.Duracao >= 70)
{
filmes.Add(filme);
Console.WriteLine(filme.Titulo);
Console.WriteLine(filme.Duracao);
}
} Copiar código
Ainda é possível acrescentar outras validações. Por exemplo, que o título tenha o máximo de 500 caracteres:

// ...

[HttpPost]
public void AdicionaFilme([FromBody] Filme filme)
{
if (!string.IsNullOrEmpty(filme.Titulo) &&
filme.Titulo.Length <= 500 &&
!string.IsNullOrEmpty(filme.Genero) &&
filme.Duracao >= 70)
{
filmes.Add(filme);
Console.WriteLine(filme.Titulo);
Console.WriteLine(filme.Duracao);
}
}Copiar código
Essa estratégia funciona, mas não é muito prática, pois são inúmeras condições que poderíamos adicionar manualmente ao código para verificar se os dados enviados são válidos ou não. Além disso, seria bastante problemático exibir uma mensagem de erro customizada, baseada no parâmetro inválido (título, gênero ou duração). Teríamos que adicionar mais condicionais para evidenciar qual parâmetro é inválido, para então gerar um texto específico e conciso.

Concluímos que colocar validações diretamente no código não é a melhor solução, então vamos retornar o método AdicionaFilme() ao estado original:

// ...
[HttpPost]
public void AdicionaFilme([FromBody] Filme filme)
{
filmes.Add(filme);
Console.WriteLine(filme.Titulo);
Console.WriteLine(filme.Duracao);
}Copiar código
Validação de dados: data annotations
A seguir, vamos empregar uma solução mais elegante e funcional, usando as Data Annotations para fazer validações em tempo de execução. No arquivo Filme.cs, vamos adicionar as data annotations acima de cada campo que queremos validar.

Pra tornar o título obrigatório, incluiremos [Required] na linha imediatamente acima dessa propriedade:

namespace FilmesApi.Models;

public class Filme
{
[Required]
public string Titulo { get; set; }
public string Genero { get; set; }
public int Duracao { get; set; }
}Copiar código
Vamos posicionar o cursor sobre essa anotação, pressionar "Alt + Enter" e selecionar "using System.ComponentModelo.DataAnnotations" para fazer a importação do namespace necessário.

Tornaremos as demais propriedades obrigatórias também, adicionando a mesma anotação acima de cada uma delas:

using System.ComponentModel.DataAnnotations;

namespace FilmesApi.Models;

public class Filme
{
[Required]
public string Titulo { get; set; }
[Required]
public string Genero { get; set; }
[Required]
public int Duracao { get; set; }
}Copiar código
A seguir, vamos executar nossa aplicação novamente e realizar alguns testes para conferir o que acontece agora quando deixamos de inserir um campo obrigatório.

No Postman, enviaremos uma requisição POST para https://localhost:7106/filme com o seguinte JSON:

{
"Titulo" : " ",
"Genero" : " ",
"Duracao" : -120
}Copiar código
Ao pressionar o botão "Send", o resultado será:

Status: 400 Bad Request

{
"type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
"title": "One or more validation errors occurred.",
"status": 400,
"traceId": "00-4709d45b80b52de3e5d90ec002ff3f37-f5ac6af4f861ef6f-00",
"errors": {
"Genero": [
"The Genero field is required."
],
"Titulo": [
"The Titulo field is required."
]
}
}Copiar código
Ou seja, fizemos uma requisição inválida (bad request) e recebemos uma resposta em inglês, pouco precisa para o usuário, indicando que os campos "Genero" e "Titulo" são obrigatórios. Seria mais interessante elaborar uma resposta clara e concisa, como:

O título do filme é obrigatório.

Para exibir esse texto explicativo mais específico, podemos customizar a anotação [Required] e adicionar uma mensagem de erro:

// Filme.cs

using System.ComponentModel.DataAnnotations;

namespace FilmesApi.Models;

public class Filme
{
[Required(ErrorMessage = "O título do filme é obrigatório")]
public string Titulo { get; set; }
[Required(ErrorMessage = "O gênero do filme é obrigatório")]
public string Genero { get; set; }
[Required]
public int Duracao { get; set; }
}Copiar código
Com a data annotation [MaxLength], também adicionaremos uma validação referente à quantidade máxima de caracteres para o gênero. No caso, o valor máximo será 50:

using System.ComponentModel.DataAnnotations;

namespace FilmesApi.Models;

public class Filme
{
[Required(ErrorMessage = "O título do filme é obrigatório")]
public string Titulo { get; set; }
[Required(ErrorMessage = "O gênero do filme é obrigatório")]
[MaxLength(50, ErrorMessage = "O tamanho do gênero não pode exceder 50 caracteres")]
public string Genero { get; set; }
[Required]
public int Duracao { get; set; }
}Copiar código
Com [Range], é possível incluir uma validação do intervalo para a duração do filme. O intervalo válido será de 70 a 600 minutos:

using System.ComponentModel.DataAnnotations;

namespace FilmesApi.Models;

public class Filme
{
[Required(ErrorMessage = "O título do filme é obrigatório")]
public string Titulo { get; set; }
[Required(ErrorMessage = "O gênero do filme é obrigatório")]
[MaxLength(50, ErrorMessage = "O tamanho do gênero não pode exceder 50 caracteres")]
public string Genero { get; set; }
[Required]
[Range(70, 600, ErrorMessage = "A duração deve ter entre 70 e 600 minutos")]
public int Duracao { get; set; }
}Copiar código
Testando
Vamos executar nossa aplicação novamente e realizar mais testes. No Postman, enviaremos mais uma vez um JSON com dados inválidos:

{
"Titulo" : " ",
"Genero" : " ",
"Duracao" : -120
}Copiar código
Ao pressionar "Send", o resultado obtido será:

Status: 400 Bad Request

{
"type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
"title": "One or more validation errors occurred.",
"status": 400,
"traceId": "00-788b79563353a3b66442d0eb9f3dd7bd-c20022333467007b-00",
"errors": {
"Genero": [
"O gênero do filme é obrigatório"
],
"Titulo": [
"O título do filme é obrigatório"
],
"Duracao": [
"A duração deve ter entre 70 e 600 minutos"
]
}
}Copiar código
As validações estão funcionando e as mensagens de erros ficaram um pouco mais claras para o usuário. Por fim, vamos testar se o nosso sistema continua funcionando normalmente, adicionando informações válidas:

{
"Titulo" : "Avatar",
"Genero" : "Ação",
"Duracao" : 162
}Copiar código
Ao enviar, a inserção será bem-sucedida:

Status: 200 OK

Sendo assim, validamos os dados enviados pelo usuário de maneira descomplicada, sem adicionar diversos blocos if na lógica do controlador. Em vez disso, usamos as data annotations no modelo, que será recebido via parâmetro.

Agora, já conseguimos cadastrar filmes no sistema de forma parcialmente robusta. Na sequência, estudaremos as outras operações para consultar, atualizar e remover filmes da API.

## Retornando filmes da API
