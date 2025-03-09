# CSharp - Criando sua primeira aplicação

## Primeiro programa

Guilherme: Com o Visual Studio aberto, inicialmente temos o primeiro programa feito com C#: o Hello World (arquivo Program.cs). Ao executá-lo, é aberto apenas o terminal com a seguinte mensagem:

Terminal na máquina do instrutor Guilherme:

Hello, World!

O C:\Users\guilherme\source\repos\PrimeiroProjeto\PrimeiroProjeto\bin\Debug\net7.0\PrimeiroProjeto.exe (processo 26844) foi encerrado com o código 0.
Pressione qualquer tecla para fechar esta janela…
Nosso objetivo é desenvolver uma aplicação back-end para um sistema de músicas. Criaremos então uma aplicação de streaming com diversos artistas, bandas e músicas, mas o foco não será a parte visual, e sim o back-end da aplicação.

Dito isso, aprenderemos a armazenar músicas e a manipular determinados conteúdos, como registrar ou avaliar bandas… Faremos tudo isso com o C#!

Retornando ao Visual Studio, temos o código do programa "Hello, World!". Ele é formado apenas por uma primeira linha de comentário e por uma segunda linha contendo o comando Console.WriteLine(), adicionado quando iniciamos o programa.

Vamos remover ambas as linhas e começar a desenvolver a nossa aplicação.

Daniel: O nome do nosso projeto será Screen Sound, correto?

Guilherme: Exatamente. Começaremos o código com um comentário contendo o nome da aplicação de músicas. Para isso, utilizamos o sinal //.

// Screen Sound
O primeiro ponto importante que precisamos entender em relação ao C# é que se trata de uma linguagem fortemente tipada. O que isso significa, Daniel?

Daniel: Significa que precisamos sempre declarar o tipo das variáveis criadas. Podemos iniciar declarando uma variável que represente uma mensagem de boas-vindas ao nosso projeto.

Guilherme: Legal! Quando vamos escrever um texto, geralmente usamos aspas duplas.

Em JavaScript e algumas outras linguagens, podemos escolher entre aspas simples ou aspas duplas. Em C#, existe a possibilidade de usar aspas simples, mas não é esse o caso.

Escreveremos a seguinte mensagem entre as aspas:

// Screen Sound
"Boas vindas ao Screen Sound"
Porém, não é somente dessa forma que criamos uma variável. Precisaremos adicionar algumas outras informações, certo, Daniel?

Daniel: Sim, a informação com a mensagem de boas-vindas precisa estar armazenada em uma variável. Criaremos a nossa primeira variável do tipo string (que representa um texto) e a chamaremos de mensagemDeBoasVindas. Vamos adicionar então ambos os elementos seguidos de um sinal de =, separando a declaração da variável e a mensagem de fato.

// Screen Sound
string mensagemDeBoasVindas = "Boas vindas ao Screen Sound"
Guilherme: Feito isso, ainda aparenta existir um problema no fechamento das aspas duplas. Ao posicionar o cursor sobre ela, temos a seguinte informação:

CS1002: ; esperado

O que esse último dado significa, Daniel?

Daniel: Significa que toda instrução no C# precisa ser terminada com ponto e vírgula. Essa é a indicação feita pelo computador.

// Screen Sound
string mensagemDeBoasVindas = "Boas vindas ao Screen Sound";
Guilherme: Colocamos o ponto e vírgula e a notificação do erro desapareceu. Porém, a variável mensagemDeBoasVindas também está marcada com um sublinhado. Posicionando o cursor sobre ela, temos a mensagem abaixo:

CS0219: A variável "mensagemDeBoasVindas" é atribuída, mas seu valor nunca é usado

Ou seja, temos um espaço na memória para a variável, mas não usamos o conteúdo.

Daniel: Perceba que no compilador, o Visual Studio dá feedbacks visuais imediatos. No fechamento das aspas, havia um indicador vermelho que representa um erro. No caso acima, o indicador visual (isto é, o sublinhado) é verde, representando que a variável foi declarada, mas não utilizada.

Guilherme: Antes de começar a usar a variável, vamos deixar a nossa tela um pouco mais limpa em relação aos conteúdos, para focar apenas no código.

Podemos, por exemplo, fechar o Gerenciador de Soluções na lateral direita do Visual Studio. Temos a opção de clicar no botão "X" ou de usar o atalho "Shift + Esc". Além disso, podemos fechar a aba inferior "Saída", onde está selecionada a opção "Mostrar saída de: Compilação".

Dessa forma, teremos somente o código exibido na tela.

Daniel:

No caso da aba "Saída", quando executarmos novamente o programa, o processo de compilação também será executado, então pode ser que essa aba volte a aparecer.

Guilherme: Agora vamos usar o comando Console.WriteLine(). Entre parênteses, vamos passar o nome da variável mensagemDeBoasVindas.

// Screen Sound
string mensagemDeBoasVindas = "Boas vindas ao Screen Sound";
Console.WriteLine(mensagemDeBoasVindas);
Lembre-se: não colocamos a variável entre aspas, pois queremos exibir seu próprio conteúdo, e não de fato o texto "mensagemDeBoasVindas".

Note que a variável é composta por 4 palavras, sendo que as 3 últimas são iniciadas com letra maiúscula. Quando trabalhamos com variáveis, seguimos o padrão Camel Case.

Daniel: Nesse padrão, a primeira palavra começa com letra minúscula e o restante com letra maiúscula.

Guilherme: Agora vamos executar o código! Para isso, temos o botão "Iniciar Sem Depurar" (ícone ▶), localizado na barra superior do Visual Studio. Caso prefira, você pode usar o atalho "Ctrl + F5".

Após a execução, é aberta novamente a aba "Saída", exibindo a saída de compilação. Finalizado o processo, o programa será aberto em outra janela chamada "Console de Depuração do Microsoft Visual Studio", onde teremos a mensagem de boas-vindas:

Terminal na máquina do instrutor Guilherme:

Boas vindas ao Screen Sound

O C:\Users\guilherme\source\repos\PrimeiroProjeto\PrimeiroProjeto\bin\Debug\net7.0\PrimeiroProjeto.exe (processo 22548) foi encerrado com o código 0.
Pressione qualquer tecla para fechar esta janela…
Temos um programa melhor, com conceitos que fazem sentido para todo o desenvolvimento a seguir.

Conforme dito anteriormente, a C# é uma linguagem fortemente tipada, então definimos o tipo, o nome da variável com a qual vamos trabalhar, e depois passamos o valor do conteúdo para o comando Console.WriteLine(). Dessa forma, conseguimos utilizar nossas variáveis!

## Isolando o código com funções

Guilherme: O programa ficou interessante, pois conseguimos alterar o texto do "Hello, World" utilizando uma variável, resultando na seguinte mensagem no console:

Boas vindas ao Screen Sound

Apesar de ser uma aplicação de console que será exibida apenas no terminal, seria interessante melhorar sua aparência. Vamos adicionar asteriscos acima e abaixo da frase para deixá-la mais agradável visualmente.

Na linha 4 do arquivo Program.cs, adicionamos um Console.WriteLine("") contendo vários asteriscos. Vamos copiar e colar essa linha logo abaixo da mensagem de boas-vindas.

Program.cs

// Screen Sound

string mensagemDeBoasVindas = "Boas vindas ao Screen Sound";
Console.WriteLine("************\*\*************");
Console.WriteLine(mensagemDeBoasVindas);
Console.WriteLine("************\*\*************");
Copiar código
Depois clicamos no botão "▶" na parte superior.

No console, obtemos:

---

Boas vindas ao Screen Sound

---

Copiar código
Agora está mais interessante.

Uma observação relevante é que, ao executarmos o programa com esses asteriscos, ele adquire uma nova aparência. No entanto, essa aparência ainda não é visualmente atraente. Essa mensagem de boas-vindas será exibida em diferentes momentos da nossa aplicação, e um conceito bem conhecido na programação é a capacidade de isolar um código para ser reutilizado em outros momentos, evitando a necessidade de copiá-lo.

Uma abordagem que podemos utilizar para isolar nosso código é criar uma função.

Daniel: A fim de aproveitar o código de forma mais eficiente, é importante notar que vamos mencionar bastante a importância do reuso de código, evitando repetições e tornando o código mais conciso. Isso nos permite utilizá-lo em diferentes momentos, sem a necessidade de recriá-lo constantemente.

Guilherme: Criaremos uma função para reutilizar as três instruções do nosso código. Para começar, precisamos determinar se a função terá ou não um valor de retorno.

Quando a função não tem um valor de retorno, ou seja, realiza ações sem retornar um resultado, usamos a palavra reservada void (em português, "vazio").

Program.cs

// Screen Sound

string mensagemDeBoasVindas = "Boas vindas ao Screen Sound";

void
Console.WriteLine("************\*\*************");
Console.WriteLine(mensagemDeBoasVindas);
Console.WriteLine("************\*\*************");
Copiar código
Daniel: Apenas um adendo, Gui. É importante observar que, ao mencionarmos a palavra reservada, o compilador nos fornece uma indicação visual por meio da cor azul. Observe que as palavras "string" e "void" estão em azul, o que significa que são palavras reservadas.

Guilherme: Legal, Daniel.

Prosseguindo, utilizamos o void para indicar que a função terá um comportamento específico, mas não esperamos que ela retorne algum valor. Nomearemos essa função como ExibirMensagemDeBoasVindas(). Para encapsular as três linhas de código, utilizamos as chaves de abertura e fechamento: {}.

A formatação utilizada na função ExibirMensagemDeBoasVindas() é um padrão visual amplamente adotado em C#: o nome da função seguido por parênteses vazios na mesma linha e, na linha seguinte, o uso das chaves de abertura e fechamento.

Depois podemos copiar as linhas das nossas instruções e colar dentro da função:

Program.cs

// Screen Sound

string mensagemDeBoasVindas = "Boas vindas ao Screen Sound";

void ExibirMensagemDeBoasVindas()
{
Console.WriteLine("************\*\*************");
Console.WriteLine(mensagemDeBoasVindas);
Console.WriteLine("************\*\*************");
}
Copiar código
Daniel: É importante notarmos que diferente da nomenclatura da variável mensagemDeBoasVindas o nome dessa função ExibirMensagemDeBoasVindas() utiliza outra convenção conhecida como PascalCase, em que a primeira palavra inicia com letra maiúscula.

O padrão PascalCase é adotado na nomenclatura de funções

Guilherme: Existem dois padrões a serem seguidos: o CamelCase para nomear variáveis e o PascalCase para nomear funções. Vamos executar clicando em "▶" e analisando no console nada foi exibido.

Isso ocorre porque declaramos a função, porém, não a chamamos para ser executada.

Daniel: Inclusive, há uma indiciação visual no código. Abaixo da função ExibirMensagemDeBoasVindas() há uma sublinhado na cor verde.

Guilherme: Exatamente, e colocando o mouse por cima da função, temos a seguinte mensagem:

A função local 'ExibirMensagemDeBoasVindas' está declarada, mas nunca é usada.

Para usarmos uma função, depois dela nós a chamamos pelo nome e abrimos e fechamos parênteses.

Program.cs

// Screen Sound

string mensagemDeBoasVindas = "Boas vindas ao Screen Sound";

void ExibirMensagemDeBoasVindas()
{
Console.WriteLine("************\*\*************");
Console.WriteLine(mensagemDeBoasVindas);
Console.WriteLine("************\*\*************");
}

ExibirMensagemDeBoasVindas();
Copiar código
Novamente clicamos em "▶" e analisando no console, obtemos a mensagem:

---

Boas vindas ao Screen Sound

---

Copiar código
Isso significa que a função está sendo exibida.

Vamos melhorar o visual dessa mensagem no próximo vídeo. Até mais!

Daniel: Até, pessoal!

## Variáveis do tipo texto

Transcrição
Daniel: Gui, sinceramente, o resultado não está bonito. Sei que você se esforçou, mas precisa melhorar isso.

Guilherme: Amizade é isso, pessoal, é sinceridade.

Eu confesso que tentei, tem aqui os asteriscos de boas-vindas, mas não está bonito. Posso tentar deixar mais bonito?

Vou acessar uma aplicação no navegador chamada FSymbols na seção de geradores.

Nela podemos escrever, por exemplo, Screensound, que é o nome da nossa aplicação, e ele vai mostrar diversas formas de exibir esse nome. Nós podemos escolher um desses e copiar.

Lembrando que nem todos vão funcionar. Além disso, se você quiser colocar outro nome no programa que você está desenvolvendo junto conosco, você pode.

Texto "screen sound" desenhado com caracteres especiais.

Nós temos a mensagem de boas-vindas com os asteriscos que o Daniel odiou. Acima dela, criaremos um console.WriteLine() e, dentro dos parênteses, colaremos o conteúdo copiado do FSymbols. Devido ao tamanho do "texto", ele não será exibido corretamente, se uma outra pessoa trabalhar nessa aplicação ela poderá pensar que é um erro.

Entretanto, executando a aplicação, teremos no terminal o Screen Sound sendo exibido corretamente. Acho que os asteriscos até não fazem mais sentido e podemos tirá-los.

Executando mais uma vez, o visual ficou melhor. Ficou bonito pra caramba. É assim que a gente cresce na vida, vem alguém e fala que aquilo que você fez não está bom, você melhora e continua. Momento autoajuda do curso.

Daniel: Gui, pra ajudar a próxima pessoa desenvolvedora que for pegar o código, podemos fazer uma melhoria lá naquela string.

Guilherme: É verdade. Nós melhoramos a parte do console, mas uma pessoa desenvolvedora que chega em um projeto assim provavelmente removeria esse console.Write(), pois está difícil identificar o que ele faz.

Como que nós podemos melhorar a exibição dessa string, que é muito longa, para que a próxima pessoa que for trabalhar nesse projeto saiba o que é?

Daniel: O que precisamos é exibir a string como ela vai ficar. Para isso, vamos usar um símbolo antes de começar as aspas, que é o arroba (@).

Podemos apagar tudo que está dentro da string e colar de novo, porque a partir desse momento ela será exibida literalmente como deveria ficar.

Guilherme: Se queremos exibir a string literal, nós abrimos aspas após o arroba, damos dois "Enter" e colamos a string copiada.

// Screen Sound
string mensagemDeBoasVindas = "Boas vindas ao Screen Sound";
List<string> listaDasBandas = new List<string> { "U2", "The Beatles", "Calypso"};

void ExibirLogo()
{
Console.WriteLine(@"

░██████╗░█████╗░██████╗░███████╗███████╗███╗░░██╗  ░██████╗░█████╗░██╗░░░██╗███╗░░██╗██████╗░
██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝████╗░██║  ██╔════╝██╔══██╗██║░░░██║████╗░██║██╔══██╗
╚█████╗░██║░░╚═╝██████╔╝█████╗░░█████╗░░██╔██╗██║  ╚█████╗░██║░░██║██║░░░██║██╔██╗██║██║░░██║
░╚═══██╗██║░░██╗██╔══██╗██╔══╝░░██╔══╝░░██║╚████║  ░╚═══██╗██║░░██║██║░░░██║██║╚████║██║░░██║
██████╔╝╚█████╔╝██║░░██║███████╗███████╗██║░╚███║  ██████╔╝╚█████╔╝╚██████╔╝██║░╚███║██████╔╝
╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚══╝  ╚═════╝░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░
");
Console.WriteLine(mensagemDeBoasVindas);
}Copiar código
Agora a pessoa que vai trabalhar sabe que se trata do logo do screen sound. Executando, nós temos o menu. Bem melhor.

Daniel: Lembrando que esse recurso com arroba que começa um texto é chamado de verbatim literal. É basicamente você colocar a string do jeito que você quer que ela apareça na função.

Guilherme: No botão de "menos" à esquerda (-), eu consigo também minimizar esse trecho no Visual Studio, para não precisar ficar exibindo toda aquela string.

Quando nós executamos o programa, ele mostra o screen sound bem bonito.

Seria legal se nós pudéssemos exibir um menu de opções. Vamos criar esse menu?

Acho que, para organizar o nosso código, faz mais sentido criarmos uma função. Será uma função void chamada ExibirOpcoesDoMenu(), seguida de parênteses e chaves.

void ExibirOpcoesDoMenu()
{

}Copiar código
Podemos colocar essas opções de maneira enumerada. Começaremos com um Console.WriteLine() com a mensagem "Digite 1 para registrar uma banda". Como nós estamos trabalhando com back-end, as pessoas vão registrar e listar bandas na nossa aplicação.

Teremos um segundo Console.WriteLine() com o texto "Digite 2 para mostrar todas as bandas", e um terceiro com "Digite 3 para avaliar uma banda"

Daniel: Também podemos exibir a média de avaliações, "Digite 4 para exibir a média de uma banda". E nós podemos fazer uma opção para sair, por exemplo "Digite -1 para sair".

void ExibirOpcoesDoMenu()
{
Console.WriteLine("Digite 1 para registrar uma banda");
Console.WriteLine("Digite 2 para mostrar todas as bandas");
Console.WriteLine("Digite 3 para avaliar uma banda");
Console.WriteLine("Digite 4 para exibir a média de uma banda");
Console.WriteLine("Digite -1 para sair");
}Copiar código
Guilherme: Essas opções do menu vamos exibir embaixo do "Boas-vindas". Na linha 28, nós executamos o ExibirMensagemDeBoasVindas() e na linha 29 eu peço para exibir as opções com ExibirOpcoesDoMenu().

ExibirMensagemDeBoasVindas();
ExibirOpcoesDoMenu();
Copiar código
Daniel: Executando, agora temos o nosso projeto definido com as suas funções específicas.

Guilherme: Repara que aqui no "Digite 1", onde de fato nós temos as opções, seria legal se nós tivéssemos um espaç para conseguir visualizar melhor.

Daniel: Para isso, podemos incluir um Console.WriteLine() com uma string vazia, ou usar o \n que inclusive utilizamos anteriormente na outra opção da logo.

Guilherme: No Console.WriteLine() da primeira opção, na linha 20, vou adicionar esse \n e executar novamente.

void ExibirOpcoesDoMenu()
{
Console.WriteLine("\nDigite 1 para registrar uma banda");
Console.WriteLine("Digite 2 para mostrar todas as bandas");
Console.WriteLine("Digite 3 para avaliar uma banda");
Console.WriteLine("Digite 4 para exibir a média de uma banda");
Console.WriteLine("Digite -1 para sair");
}Copiar código
Assim temos a mensagem de boas-vindas e em seguida as opções. Nosso próximo passo será trabalhar cada uma das opções.

Daniel: Certo, precisamos capturar a opção que a pessoa usuária digitar, esse é o próximo passo.
