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
Console.WriteLine("\***\*\*\*\*\*\*\***\*\*\***\*\*\*\*\*\*\***");
Console.WriteLine(mensagemDeBoasVindas);
Console.WriteLine("\***\*\*\*\*\*\*\***\*\*\***\*\*\*\*\*\*\***");
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
Console.WriteLine("\***\*\*\*\*\*\*\***\*\*\***\*\*\*\*\*\*\***");
Console.WriteLine(mensagemDeBoasVindas);
Console.WriteLine("\***\*\*\*\*\*\*\***\*\*\***\*\*\*\*\*\*\***");
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
Console.WriteLine("\***\*\*\*\*\*\*\***\*\*\***\*\*\*\*\*\*\***");
Console.WriteLine(mensagemDeBoasVindas);
Console.WriteLine("\***\*\*\*\*\*\*\***\*\*\***\*\*\*\*\*\*\***");
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
Console.WriteLine("\***\*\*\*\*\*\*\***\*\*\***\*\*\*\*\*\*\***");
Console.WriteLine(mensagemDeBoasVindas);
Console.WriteLine("\***\*\*\*\*\*\*\***\*\*\***\*\*\*\*\*\*\***");
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

## Variáveis do tipo inteiro

Guilherme: Nosso programa está legal em partes. Vamos executá-lo, clicando no botão "Play" da aba do arquivo Program.cs. Com isso, é exibido no terminal o título "SCREEN SOUND" com letras em caixa alta estilizadas, uma mensagem de boas-vindas e as opções do menu.

Mas, se pressionamos qualquer tecla, não acontece mais nada — nosso programa acaba. Mostramos as opções, mas não deixamos a pessoa selecionar a desejada pelas teclas.

Daniel: Portanto, não há opção nenhuma.

Guilherme: Então, de alguma forma, precisamos capturar a opção que a pessoa digitou, certo? Seja para registrar uma banda, mostrar a média e assim por diante.

Daniel: Acho que podemos fazer uma pergunta primeiro, com um texto do tipo "qual é a sua escolha?".

Guilherme: Excelente. Então, na linha 26 do código, dentro da função ExibirOpcoesDoMenu() vamos escrever essa mensagem com o Console.WriteLine, pulando uma linha no programa usando \n e inserindo um espaço ao final do texto para a pessoa digitar:

Program.cs

Console.WriteLine("\nDigite a sua opção: ");Copiar código
Esse código vai exibir a mensagem "Digite a sua opção", mas, teoricamente, só isso vai acontecer. Precisamos, de alguma forma, pegar o valor que a pessoa vai digitar nesse menu. Como fazemos isso?

Capturando o comando da pessoa usuária
Daniel: Usamos o método Console.WriteLine() para escrever mensagens, e usaremos o Console.ReadLine() para ler esse valor. Usando o ReadLine(), esperamos que a pessoa usuária digite a opção e aperte "Enter" também.

Guilherme: Escrevendo Console.Read, recebemos algumas opções diferentes, como apenas Read e ReadKey. Vamos selecionar ReadLine():

Console.WriteLine("\nDigite a sua opção: ");
Console.ReadLine();Copiar código
Mas, precisamos armazenar em algum lugar o que a pessoa digitar. Vamos executar o programa agora em seu estado atual, pressionando "Ctrl + F5", para entender o que está acontecendo.

No terminal aberto com o programa, podemos notar que a mensagem "Digite a sua opção: " está sendo exibida abaixo do menu, e o cursor para digitar está posicionado abaixo da frase. Queríamos que o cursor estivesse na mesma linha da frase, afinal, deixamos um espaço para isso depois dos dois pontos.

Daniel: Nesse caso, ao invés de usar o WriteLine(), podemos usar apenas o Write(). Assim, o programa escreverá o texto que está no argumento da função sem pular linha depois.

Guilherme: Certo, então vamos apagar o Line da linha 26:

Console.Write("\nDigite a sua opção: ");
Console.ReadLine();Copiar código
Vamos executar mais uma vez para conferir. No programa, o cursor para digitar a opção está sendo exibido ao lado da frase "Digite a sua opção: ".

Vamos digitar "1" no programa, para registrar uma banda, e pressionar "Enter". Novamente, o programa é encerrado porque não criamos mais nada em relação a isso.

Daniel: Vamos armazenar essa opção digitada pela pessoa em uma variável.

Guilherme: Certo. Para isso, vamos criar uma string chamada opcaoEscolhida que receberá o Console.ReadLine():

Console.Write("\nDigite a sua opção: ");
string opcaoEscolhida = Console.ReadLine();Copiar código
Com isso, notaremos um sublinhado em verde no Console.ReadLine() que nos avisa que esse método pode retornar um valor nulo. Não queremos trabalhar com valor nulo no nosso programa, porque é necessário que esse valor seja uma string.

Para resolver isso, podemos inserir um sinal de exclamação ao final do método: Console.ReadLine()!. Ao fazer isso, o sublinhado verde some.

Console.Write("\nDigite a sua opção: ");
string opcaoEscolhida = Console.ReadLine()!;Copiar código
Agora temos esse valor armazenado em uma variável. Em seguida, precisamos verificar qual foi a opção digitada: se foi a opção 1, se foi a opção 2, e assim por diante.

Condição para retorno
Daniel: Então, entra agora uma condição: se a pessoa digitou "1", realizamos determinada ação; se digitou "2", outra ação, e assim vai.

Guilherme: Sim. Para isso, temos um if similar ao dos cursos de lógica de programação. Escrevemos if e, entre parênteses, inserimos a nossa condição. O VSCode até sugere a condição opcaoEscolhida == null, mas não é isso que queremos.

Na verdade, queremos dizer o seguinte: "se a opção escolhida for igual a 1, por exemplo, realizaremos a seguinte ação entre chaves". Então trocamos o null para 1 e adicionamos as chaves em seguida.

Essa ação pode ser, por exemplo, escrever a mensagem "Você digitou a opção x": ConsoleWriteLine("Você digitou a opção x"). No lugar desse x, queremos colocar o valor da variável opcaoEscolhida. Como fazer isso?

No JavaScript, colocamos um espaço entre a última palavra da frase e as aspas e depois inserimos o sinal de adição e o nome da variável, por exemplo: + opcaoEscolhida. Aqui funciona assim também:

// código omitido
if (opcaoEscolhida == 1)
{
ConsoleWriteLine("Você digitou a opção " + opcaoEscolhida)
}Copiar código
Mas, temos um problema na própria variável opcaoEscolhida que, sublinhada em vermelho, nos indica que seu valor não é nulo dentro desse if. Estamos usando o operador == para comparar uma string, que é tudo o que digitamos e recebemos com o ReadLine(), com o valor 1 que é um inteiro e não uma string. Não é possível fazer isso.

Daniel: Algum desses valores precisa ser convertido.

Guilherme: Exatamente: ou convertemos o 1 para string, o que não faz muito sentido; ou convertemos o opcaoEscolhida que digitamos, uma string, para um valor inteiro. O que você acha melhor?

Daniel: Acho melhor converter a opcaoEscolhida em uma nova variável de tipo inteiro. Em vez de colocar a palavra reservada string antes da declaração da variável, usaremos o int — outra palavra reservada que indica o tipo inteiro.

Convertendo string em inteiro
Guilherme: Abaixo da variável opcaoEscolhida e antes do if, vamos criar uma nova variável de tipo int. Vamos chamá-la de opcaoEscolhidaNumerica, por exemplo, para explicitar a conversão em número. Ela receberá a variável opcaoEscolhida convertida para inteiro.

Daniel: Há algumas funções para realizar essa conversão. Podemos usar primeiro uma função que fica dentro de um tipo chamado int, chamada Parse(), que pega um texto e tenta converter para valor inteiro. Então, escrevemos int.Parse() e passamos opcaoEscolhida como parâmetro. Nossa variável nova fica assim:

int opcaoEscolhidaNumerica = int.Parse(opcaoEscolhida);Copiar código
Guilherme: Sendo assim, precisamos mudar a variável que passamos no if. Repare que ainda temos uma marcação em vermelho nele por estar usando o valor da variável opcaoEscolhida, que é uma string. O que queremos fazer agora é usar a variável de tipo inteiro, opcaoEscolhidaNumerica:

// código omitido
if (opcaoEscolhidaNumerica == 1)
{
ConsoleWriteLine("Você digitou a opção " + opcaoEscolhida)
}Copiar código
Não temos mais nenhuma marcação de erro, parece que funcionou! Vamos executar o programa novamente e testar a opção 1, a única que criamos até agora, digitando "1" no terminal e pressionando "Enter". O retorno surge logo abaixo:

Você digitou a opção 1

Maravilha!

## Uso de if/else e switch/case

Daniel: Vamos continuar trabalhando nas opções escolhidas.

Guilherme: Como a opção 2 terá praticamente o mesmo código da opção 1, podemos copiá-lo (da linha 29 até a linha 32) e colar logo depois do fechamento do if, com um else antes para indicar "senão".

Se a opção escolhida for a 2 (opcaoEscolhidaNumerica == 2), exibimos a mensagem "Você digitou a opção 2":

Program.cs

// código omitido
if (opcaoEscolhidaNumerica == 1)
{
ConsoleWriteLine("Você digitou a opção " + opcaoEscolhida)
} else if (opcaoEscolhidaNumerica == 2)
{
ConsoleWriteLine("Você digitou a opção " + opcaoEscolhida)
}
Copiar código
Vamos executar o programa novamente para testar as duas opções. Com o programa aberto no terminal, digitamos a opção "1", que nós já testamos, ao lado da frase "Digite a sua opção" e pressionamos "Enter". Recebemos o retorno "Você digitou a opção 1". Tudo certo.

Vamos fechar o terminal e rodar o programa mais uma vez. Agora vamos digitar a opção "2" e pressionar "Enter". Recebemos o retorno correto: "Você digitou a opção 2".

Então o programa está, de fato, capturando essas opções!

Agora, fazemos o mesmo para a opção 3, 4 e -1?

Daniel: Na verdade, podemos usar outro recurso. Quando temos vários condicionais associados, relacionados logicamente, nós usamos o switch.

Guilherme: Então podemos remover os ifs?

Daniel: Podemos.

Switch
Guilherme: Vamos apagar os ifs (da linha 30 até a linha 36) e, no lugar, escrever aqui switch. Ao lado, entre parênteses, colocamos o que queremos verificar — no caso, a variável opcaoEscolhidaNumerica. Abrimos e fechamos chaves em seguida e, dentro delas, vamos começar as opções.

Caso a opção escolhida seja 1, então nós colocamos um case 1 e, depois dos dois pontos (:), a mensagem de retorno com o Console.WriteLine(). Podemos inserir a mesma mensagem de antes: "Você escolheu a opção " + opcaoEscolhidaNumerica. Ao fim dessa linha, colocamos um ponto e vírgula (;).

Daniel: Também precisamos colocar a palavra reservada break na linha de baixo para finalizar esse caso, seguido de um ponto e vírgula novamente.

Guilherme: Certo. Pulando para a linha de baixo, o Visual Studio sugere o case 2 para a segunda opção. Vamos repetir o que fizemos acima para todas as outras opções — 3, 4 e -1 — copiando o mesmo método e texto:

switch (opcaoEscolhidaNumerica)
{
case 1:
Console.WriteLine("Você escolheu a opção " + opcaoEscolhidaNumerica);
break;
case 2:
Console.WriteLine("Você escolheu a opção " + opcaoEscolhidaNumerica);
break;
case 3:
Console.WriteLine("Você escolheu a opção " + opcaoEscolhidaNumerica);
break;
case 4:
Console.WriteLine("Você escolheu a opção " + opcaoEscolhidaNumerica);
break;
case -1:
Console.WriteLine("Você escolheu a opção " + opcaoEscolhidaNumerica);
break;
}
Copiar código
Temos todas as opções, de 1 a 4, e também a opção -1. Trabalhamos com case e break para cada opção.

Por enquanto estamos usando a mensagem, mas adiante vamos criar uma função que vai, de fato, executar cada opção: salvar uma nova banda, registrar a banda, exibir a média da banda e assim por diante.

Daniel: Há uma última possibilidade a adicionar dentro do switch: se o usuário não digitar nenhuma dessas opções, é necessário exibir uma mensagem de opção inválida. Para isso, usamos uma palavra reservada chamada default. Ou seja: se nenhum desses casos aconteceu, caímos nesse default.

Guilherme: Então, por exemplo, a mensagem do default pode ser "Opção inválida!". O default também leva o break:

switch (opcaoEscolhidaNumerica)
{
// código omitido
default:
Console.WriteLine("Opção inválida");
break;
}
Copiar código
Vamos testar todas essas opções agora. Para isso, executaremos nosso programa algumas vezes.

Começando, na primeira execução, vamos testar a opção 1 digitando "1" ao lado de "Digite a sua opção:" e pressionando "Enter". O retorno recebido é: "Você escolheu a opção 1". Deu certo.

Vamos fechar, executar o programa novamente e escolher a opção "2" no terminal. Retorno: "Você escolheu a opção 2". Certo novamente.

Repetindo esse processo para as opções 3 e 4, recebemos as mensagens de retorno corretas de cada um: "Você escolheu a opção 3" e "Você escolheu a opção 4", respectivamente.

A opção "-1" serve para encerrar o programa, o que teoricamente já está acontecendo. Não precisamos mudar nada nessa função, a não ser a mensagem de retorno — algo como "Obrigado. Tchau.". Vamos fazer isso daqui a pouco também.

Por fim, testamos uma opção inválida, como o "99". Com isso, recebemos a mensagem "Opção inválida" e o programa encerra também.

Então, vamos alterar a mensagem do -1, quando encerramos o programa. Queremos uma mensagem bem bonita. Pode ser um "Tchau tchau" com um emoji feliz ":)".

switch (opcaoEscolhidaNumerica)
{
// código omitido
case -1:
Console.WriteLine("Tchau tchau :)");
break;
}
// código omitido
Copiar código
Vamos testar, executando novamente o programa. Vamos digitar a opção "-1" e pressionar "Enter". Recebemos a mensagem: "Tchau tchau :)". Fechou! Ficou lindo!

Daniel: Concluindo: nós conhecemos a opção condicional, o if e o if else. Em seguida aprendemos que, quando temos um cenário com muitos casos, podemos usar também o recurso switch, com a construção switch case que aplicamos.

## Criando a lista de músicas

Guilherme: Chegamos a um momento incrível da nossa aplicação, vamos trabalhar de fato em cada uma dessas opções!

Case 1 - Registro de bandas
A primeira opção é o registro de bandas. No case 1 colocamos só uma mensagem de teste. Mas agora removeremos essa mensagem para chamar uma determinada função. Podemos chamar, por exemplo, a função RegistrarBanda().

case1: RegistrarBanda();
Copiar código
O editor informou que essa função ainda não existe no contexto atual. Vamos criar a função RegistrarBanda() agora.

Na linha 47, criaremos uma função void.

void RegistrarBanda()
{

}
Copiar código
Lembre-se que a linguagem do C# é case sensitive, sensível a letras maiúsculas e minúsculas. Precisamos nos atentar a isso.

Guilherme: Então, o caso 1 vai executar a função RegistrarBanda().

O que queremos fazer? Primeiro, assim que rodamos a aplicação podíamos limpar o nosso console. Uma forma de limpar o console é com o Console.Clear(). Dessa forma, não teremos nenhum texto sendo exibido no console.

void RegistrarBanda()
{
Console.Clear();

}
Copiar código
Em seguida, podemos exibir no console o texto "Registro de bandas", por exemplo, usando um Console.WriteLine().

void RegistrarBanda()
{
Console.Clear();
Console.WriteLine("Registro de bandas");

}
Copiar código
Podemos começar dando uma mensagem como "Digite o nome da banda que você deseja registrar". Mas não usaremos o Console.WriteLine() porque queremos que fique na mesma linha da mensagem que estamos passando e não embaixo. Usaremos o Console.Write().

void RegistrarBanda()
{
Console.Clear();
Console.WriteLine("Registro de bandas");
Console.Write("Digite o nome da banda que deseja registrar: ")
}
Copiar código
Daniel: Legal que estamos aproveitando os conceitos que vimos anteriormente. Criamos função, agora escrevemos na tela e depois vamos capturar isso em uma variável.

Guilherme: Agora, precisamos pegar o nome da banda. Colocaremos uma string nomeDaBanda igual a Console.ReadLine()!. A exclamação depois dos parênteses é para indicar que não queremos trabalhar com valor nulo.

void RegistrarBanda()
{
Console.Clear();
Console.WriteLine("Registro de bandas");
Console.Write("Digite o nome da banda que deseja registrar: ")
string nomeDaBanda = Console.ReadLine()!;
}
Copiar código
Interpolação de strings
Agora, Daniel, eu quero criar uma mensagem assim, digamos que eu digitei "Pink Floyd", quero uma mensagem que diga: "A banda Pink Floyd foi registrada com sucesso".

Como colocar esse valor "Pink Floyd" no meio do texto que está sendo exibido? Quero colocar a variável nomeDaBanda no meio da frase "A banda foi registrada com sucesso!".

Daniel: Poderíamos usar a concatenação com sinal de +, porém ficaria um pouco confuso com muitos sinais de +. Vamos usar outro recurso do C# que é a interpolação de string. Inicia a string com cifrão e envolve a variável que queremos referenciar com chaves.

Console.WriteLine($"A banda {nomeDaBanda} foi registrada com sucesso!");
Copiar código
Até agora nosso código está assim:

void RegistrarBanda()
{
Console.Clear();
Console.WriteLine("Registro de bandas");
Console.Write("Digite o nome da banda que deseja registrar: ")
string nomeDaBanda = Console.ReadLine()!;
Console.WriteLine($"A banda {nomeDaBanda} foi registrada com sucesso!");
}
Copiar código
Guilherme: Legal, até muda a cor da variável quando ela está entre chaves.

Depois disso, queremos esperar um pouco para dar aquele suspense na aplicação. Colocaremos um Thread.Sleep(), essa função espera em milissegundos, vamos colocar 2000 milissegundos. Depois, queremos voltar ao menu principal.

Em seguida, vamos limpar o console e inserir um ExibirOpcoesDoMenu() para voltarmos ao menu principal.

void RegistrarBanda()
{
Console.Clear();
Console.WriteLine("Registro de bandas");
Console.Write("Digite o nome da banda que deseja registrar: ");
string nomeDaBanda = Console.ReadLine()!;
Console.WriteLine($"A banda {nomeDaBanda} foi registrada com sucesso!");
Thread.Sleep(2000);
Console.Clear();
ExibirOpcoesDoMenu();
}
Copiar código
Vamos testar a opção 1! Queremos digitar o nome da banda e visualizar a mensagem informando que ela foi registrada. Podemos executar o projeto.

Escolhemos a opção 1, pressionei "Enter".

Registro de bandas

Digite o nome da banda que deseja registrar:

Vamos inserir a banda "Pink Floyd" e pressionar "Enter". Ele exibiu a mensagem:

A banda Pink Floyd foi registrada com sucesso!

E volta ao menu principal.

Daniel: Faltou exibir logo do projeto.

Guilherme: De volta ao código, vamos refatorar o código e renomear a função ExibirMensagemDeBoasVindas() para ExibirLogo(). Esse ExibirLogo() vai ficar dentro do ExibirOpcoesDoMenu(). O menu sempre terá o logo.

void ExibirOpcoesDoMenu()
{
ExibirLogo();

// código omitido
Copiar código
Podemos executar o programa para testar novamente a opção 1. Agora está funcionando como esperado e voltando para o menu principal com o logo sendo exibido acima dele.

Daniel: Está legal. Mas e se tentarmos registrar uma nova banda? Aquela primeira banda que registramos sumiu, não está mais sendo exibida. Porque estamos usando uma única variável que só está existindo dentro do corpo da função RegistrarBanda(). No próximo vídeo vamos resolver isso.

## Adicionando músicas na lista

Daniel: Agora precisamos guardar as bandas que estamos registrando em algum recurso, alguma estrutura, para que consigamos fazer a opção 2, que é mostrar as bandas cadastradas.

Guilherme: E esse recurso não pode existir apenas no RegistrarBanda(), deve estar em um escopo global da nossa aplicação. O que você sugere?

Daniel: Acho que a melhor opção é uma coleção onde o nome da cada banda fique registrado. Uma lista.

Lista
Guilherme: Pensando até no mundo real. Se alguém perguntar quais as cinco bandas que você mais gosta de ouvir, você já imagina uma lista com essas cinco bandas. No nosso projeto teremos algo muito parecido com isso.

E, se no C# tudo é fortemente tipado, uma lista não é exceção. Precisaremos definir também essa lista.

Para criar uma lista no C# vamos escrever List<>. Note que temos o sinal de maior que e o sinal de menor que. Isso significa que dentro desses sinais indicaremos o tipo dessa lista, se é uma lista de inteiros, de números decimais, de string, etc.

No nosso caso, como queremos guardar o nome de diversas bandas, queremos uma lista de strings.

List<string>Copiar código
E já apareceu um autocomplete de código para lista de strings. Vamos pressionar "Tab" para aceitar essa sugestão.

List<string> strings = new List<string>();Copiar código
Vamos fazer a alteração do nome da lista, será listaDasBandas.

List<string> listaDasBandas = new List<string>();Copiar código
Daniel: Sim, precisamos dar nomes significativos para o negócio que estamos desenvolvendo. Não podem ser nomes muito genéricos. Com nomes mais específicos, como listaDasBandas, fica mais fácil para qualquer pessoa que ler esse código saber o que está acontecendo.

Mais adiante falaremos mais sobre essa sintaxe gerada para listas, o que importa agora é que criamos uma lista vazia e poderemos colocar bandas dentro dessa lista.

Guilherme: Agora, no RegistrarBanda(), a partir do momento que temos o nome da banda que a pessoa digitou, queremos adicionar esse nome na listaDasBandas. Para isso, usaremos o .Add(nomeDaBanda).

listaDasBandas.Add(nomeDaBanda);Copiar código
a função RegistrarBanda() ficou assim:

void RegistrarBanda()
{
Console.Clear();
Console.WriteLine("Registro de bandas");
Console.Write("Digite o nome da banda que deseja registrar: ")
string nomeDaBanda = Console.ReadLine()!;
listaDasBandas.Add(nomeDaBanda);
Console.WriteLine($"A banda {nomeDaBanda} foi registrada com sucesso!");
Console.Clear();
Thread.Sleep(2000);
ExibirOpcoesDoMenu();
}Copiar código
Vamos executar o programa, selecionar a opção 1 e adicionar duas bandas "Black Sabbath" e "Beatles".

Conseguimos adicionar a duas bandas, não apareceu erro. Mas o que colocaria à prova essa nossa lista, para verificar se ela está realmente funcionando, é a execução da opção 2 que exibe todas as bandas.

Então, no próximo vídeo vamos implementar o código para a opção 2 funcionar.

## Estrutura de repetição for

Guilherme: Já temos uma lista chamada listaDasBandas e registramos as bandas com a função RegistraBanda(). Porém, ainda não exibimos as bandas. Inclusive, temos a segunda opção dedicada a mostrar todas as bandas na função ExibirOpcoesDoMenu().

Mostrar bandas registradas
Guilherme: No switch(), vamos tirar o Console.WriteLine() que está após o case 2 na linha 36. No lugar, vamos digitar MostrarBandasRegistradas() que será a função do registro das bandas que vamos criar.

Program.cs:

void Exibir OpcoesDoMenu()
{

// código omitido…

    switch (opcaoEscolhidaNumerica)
    {
        case 1: RegistrarBanda();
            break;
        case 2: MostrarBandasRegistradas();
            break;
        case 3: Console.WriteLine("Você escolheu a opção " + opcaoEscolhidaNumerica);
            break;
        case 4: Console.WriteLine("Você escolheu a opção " + opcaoEscolhidaNumerica);
            break;
        case -1: Console.WriteLine("Tchau tchau :)");
            break;
        default: Console.WriteLine("Opção inválida");
            break;
    }

}Copiar código
Agora, vamos desenvolver a função MostrarBandasRegistradas() com essa responsabilidade. Vamos criar uma nova função na linha 61, após RegistrarBanda().

Também será uma função void responsável apenas por MostrarBandasRegistradas(). O Visual Studio sugeriu um Console.Clear(). Faz sentido, queremos limpar o console e ter um comportamento parecido com RegistrarBanda().

void MostrarBandasRegistradas()
{
Console.Clear();
}Copiar código
Inclusive, o Daniel comentou sobre os asteriscos anteriormente. Vamos colocar uma linha de asteriscos com Console.Write() após Console.Clear() na função RegistrarBanda()? Vai ficar visualmente mais bonito. Também vamos adicionar outra linha de asteriscos após Console.Write("Registro de bandas").

void RegistrarBanda()
{
Console.Clear();
Console.WriteLine("**********\*\***********");
Console.WriteLine("Registro de bandas");
Console.WriteLine("**********\*\***********");
Console.Write("Digite o nome da banda que deseja registrar: ");
string nomeDaBanda = Console.ReadLine()!;

// código omitido…

}Copiar código
Queremos esse mesmo comportamento para a função que vai exibir as bandas. Por isso, adicionamos em MostrarBandasRegistradas() um Console.WriteLine() de asteriscos, outro com a string Exibindo todas as bandas registradas e mais um Console.WriteLine() com a linha de asteriscos do mesmo comprimento da frase.

void MostrarBandasRegistradas()
{
Console.Clear();
Console.WriteLine("****************\*\*\*\*****************");
Console.WriteLine("Exibindo todas as bandas registradas");
Console.WriteLine("****************\*\*\*\*****************");
}Copiar código
Agora, o desafio é o seguinte: precisamos pegar a listaDasBandas e exibir na tela cada banda que temos dentro dessa lista.

Daniel: Isto é, precisamos percorrer a lista.

Estrutura de repetição for
Guilherme: Para isso, podemos usar o for. Assim, para cada banda que temos dentro da listaDasBandas, vamos exibi-las no console.

Daniel: Vamos fazer um loop, certo?

Guilherme: Exatamente. Em MostrarBandasRegistradas(), vamos escrever o for após o Console.WriteLine() de asteriscos. Esse for é muito simular ao for do JavaScript e Java. Entre parênteses, vamos declarar uma variável int chamada i que vai ser igual à 0.

Vamos percorrer toda a lista, ou seja, deve-se continuar a executar as instruções enquanto tiver bandas. Para isso, após a inicialização, colocamos a condição i menor que listaDasBandas.Count. Assim, vamos contar todas as bandas e enquanto tiver bandas, vamos continuar a executar o for.

A cada repetição que executamos, vamos incrementar 1 na variável i. Ou seja, a expressão de iteração do for será i++.

No corpo do for, vamos colocar um Console.WriteLine() com a interpolação de string. Para isso, digitamos cifrão e abrimos e fechamos aspas. Entre as aspas, escrevemos Banda: seguido do nome da banda.

Mas, vamos precisar pegar o nome de banda por banda. Por isso, entre chaves, colocamos listaDasBandas[] no índice i.

void MostrarBandasRegistradas()
{

// código omitido…

    for (int i = 0; i < listaDasBandas.Count; i++)
    {
        Console.WriteLine($"Banda: {listaDasBandas[i]}");
    }

}Copiar código
Essa forma de escrita de chaves para acessar uma determinada variável seguido dos colchetes é parecido a outras linguagens.

Daniel: Inclusive, o incremento da variável i com i++ também é similar.

Voltando ao menu principal
Guilherme: Depois que exibimos as bandas, esperamos que a pessoa digite algo para voltar ao menu principal. Para isso, após o for, vamos escrever a mensagem Digite uma tecla para voltar ao menu principal com Console.WriteLine().

Em seguida, podemos usar um conceito diferente com o Console.ReadKey().

Daniel: Assim, qualquer tecla que for digitada levará ao menu principal. Depois, vamos exibir todas as opções novamente.

Guilherme: Certo. Após a pessoa digitar, vamos limpar o console com Console.Clear() e chamar o ExibirOpcoesDoMenu().

void MostrarBandasRegistradas()
{

// código omitido…

    Console.WriteLine("Digite uma tecla para voltar ao menu principal");
    Console.ReadKey();
    Console.Clear();
    ExibirOpcoesDoMenu();

}Copiar código
Daniel: Para não ter que registrar uma banda toda hora, você já pode colocar alguns valores na lista inicial.

Guilherme: O que você acha de fazer dois testes? Vamos registrar duas bandas com a lista vazia e, logo em seguida, criar alguns elementos na lista. Conforme desenvolvemos, vamos querer testar funcionalidades com algumas bandas. Por isso, é interessante já começar com uma lista com alguns valores.

Executamos o Program.cs para abrir o Screen Sound no terminal com a mensagem de boas-vindas e as opções do menu. Como queremos registrar duas bandas, escolhemos a opção 1.

Digite a sua opção: 1

Ficou muito legal os asteriscos entre o título "Registro de bandas". Primeiro, digitamos o nome da banda U2

---

Registro de bandas

---

Digite o nome da banda que deseja registrar: U2Copiar código
Após pressionar o "Enter", recebemos o aviso que a banda foi registrada com sucesso.

A banda U2 foi registrada com sucesso!

O programa volta ao menu principal. E digitamos 1 novamente para registrar mais uma banda.

Digite a sua opção: 1

Daniel: Podemos registrar os Beatles.

---

Registro de bandas

---

Digite o nome da banda que deseja registrar: BeatlesCopiar código
A banda Beatles foi registrada com sucesso!

Guilherme: Agora, vamos para a parte crucial do teste da aplicação. No menu principal, vamos digitar o 2 para escolher a opção de mostrar todas as bandas.

Digite a sua opção: 2

Após apertar "Enter", são listadas todas as bandas que registramos, U2 e Beatles.

---

Exibindo todas as bandas registradas

---

Banda: U2
Banda: Beatles
Digite uma tecla para voltar ao menu principalCopiar código
Pressionamos a tecla "Enter" para voltar ao menu principal.

Acho que podemos ter um espaço entre o asterisco e as bandas e também entre as bandas e o Console.WriteLine() da frase "Digite uma tecla para voltar ao menu principal".

Daniel: Mas, já confirmamos que a listaDasBandas está armazenando como deveria. Pois, havíamos criado a lista, mas não conseguíamos ver o conteúdo da lista. Agora, conseguimos mostrar esse conteúdo.

Pular linhas
Guilherme: Vamos fazer esses pequenos ajustes na função MostrarBandasRegistradas(). Assim que o loop for acaba, vamos pular uma linha. Para isso, acrescentamos um \n antes da frase "Digite uma tecla para voltar ao menu principal" dentro do Console.WriteLine().

Além disso, vamos acrescentar o \n após os asteriscos do terceiro Console.WriteLine(). Assim, temos o cabeçalho e pulamos uma linha.

void MostrarBandasRegistradas()
{
Console.Clear();
Console.WriteLine("****************\*\*\*\*****************");
Console.WriteLine("Exibindo todas as bandas registradas");
Console.WriteLine("****************\*\*\*\*****************\n");

    for (int i = 0; i < listaDasBandas.Count; i++)
    {
        Console.WriteLine($"Banda: {listaDasBandas[i]}");
    }

    Console.WriteLine("\nDigite uma tecla para voltar ao menu principal");
    Console.ReadKey();
    Console.Clear();
    ExibirOpcoesDoMenu();

}Copiar código
Vamos fazer essa mesma alteração para a função de cima, RegistrarBanda(). Colocamos um \n após os asteriscos do terceiro Console.WriteLine().

void RegistrarBanda()
{
Console.Clear();
Console.WriteLine("**********\*\***********");
Console.WriteLine("Registro de bandas");
Console.WriteLine("**********\*\***********\n");
Console.Write("Digite o nome da banda que deseja registrar: ");
string nomeDaBanda = Console.ReadLine()!;
listaDasBandas.Add(nomeDaBanda);
Console.WriteLine($"A banda {nomeDaBanda} foi registrada com sucesso!");
Thread.Sleep(2000);
Console.Clear();
ExibirOpcoesDoMenu();
}Copiar código
Executar com bandas já registradas
Guilherme: Inclusive, já podemos rodar com o segundo teste. Se sempre executamos o programa com a lista vazia, não vamos ter nenhuma banda registrada e vamos sempre ter que registrar uma banda para testar.

Daniel: Para fins de testes, já podemos começar com bandas já registradas.

Guilherme: No começo do arquivo onde instanciamos listaDasBandas, vamos apagar os parênteses após new List<string>. No lugar, vamos colocar os sinais de abre e fecha chaves. Entre as chaves, colocamos o nome de cada banda entre aspas e separadas por vírgula. Colocamos U2, The Beatles e Calypso, a banda preferida do Daniel.

// Screen Sound
string mensagemDeBoasVindas = "Boas vindas ao Screen Sound";
List<string> listaDasBandas = new List<string> { "U2", "The Beatles", "Calypso"}; Copiar código
Executamos a aplicação para abrir o Screen Sound no terminal. No menu principal, colocamos a opção 2 para visualizar as bandas que temos já registradas.

Digite a sua opção: 2

Após dar "Enter", temos as bandas U2, The Beatles e Calypso.

---

Exibindo todas as bandas registradas

---

Banda: U2
Banda: The Beatles
Banda: Calypso

Digite uma tecla para voltar ao menu principalCopiar código
Digitamos qualquer tecla e voltamos ao menu principal, onde vamos registrar uma nova banda com a opção 1. Registramos a banda Iron Maiden com sucesso. No menu principal, escolhemos a opção 2 para mostrar todas as bandas e a lista foi atualizada!

Daniel: Nesse vídeo, aprendemos fazer um loop no C# com o for tradicional. No próximo, vamos conhecer outro recurso de loop.

## Foreach para cada música

Daniel: Agora vamos conhecer uma maneira diferente de escrever o for.

Guilherme: É outra função do C# não tão verbosa, sem precisar declarar um inteiro para fazer um loop como fizemos no for tradicional.

Primeiro, vamos comentar o trecho do for na função MostrarBandasRegistradas() para mantê-lo como referência. Para isso, colocamos o // antes de toda linha da instrução for.

E como fazemos essa outra manipulação, Daniel?

Daniel: O recurso se chama for each ("para cada"). Assim, conseguimos passar por cada elemento da lista. O foreach é uma palavra reserva escrita toda junta e em minúsculas.

Loop foreach
Guilherme: Após o trecho comentado do for, escrevemos foreach() em uma nova linha para começar a verificação.

Daniel: Dentro dos parênteses, vamos declarar uma variável que vai representar o elemento da lista.

Guilherme: Por exemplo, podemos escrever uma string de banda. Já que vamos verificar banda por banda.

Daniel: Após benda, colocamos a palavra reserva in seguido da variável que representa a coleção, ou seja, a lista chamada listaDasBandas.

Guilherme: Até a leitura fica mais clara: string banda in listaDasBandas seria "para cada banda na lista de bandas". Também fica mais claro visualmente para entender do que o for tradicional com sua inicialização, condição e expressão de iteração.

Queremos exibir o mesmo console no corpo do foreach. Por isso, entre colchetes, escrevemos Console.WriteLine() passando cifrão e a string Banda: seguido da {banda}. Não usamos mais a listaDasBandas, porque para cada banda vamos ter um Console.WriteLine().

Program.cs:

void MostrarBandasRegistradas()
{
Console.Clear();
Console.WriteLine("****************\*\*\*\*****************");
Console.WriteLine("Exibindo todas as bandas registradas");
Console.WriteLine("****************\*\*\*\*****************\n");

    //for (int i = 0; i < listaDasBandas.Count; i++)
    //{
        //Console.WriteLine($"Banda: {listaDasBandas[i]}");
    //}

    foreach (string banda in listaDasBandas)
    {
        Console.WriteLine($"Banda: {banda}");
    }

    Console.WriteLine("\nDigite uma tecla para voltar ao menu principal");
    Console.ReadKey();
    Console.Clear();
    ExibirOpcoesDoMenu();

}
Copiar código
Já podemos testar. Executamos o programa que se abre no terminal. No menu principal do Screen Sound, vamos colocar o número 2 para exibir todas as bandas com o foreach.

Digite a sua opção: 2

Após pressionar "Enter", temos o mesmo resultado anterior. Isto é, as bandas U2, The Beatles e Calypso.

---

Exibindo todas as bandas registradas

---

Banda: U2
Banda: Beatles
Banda: Calypso

Digite uma tecla para voltar ao menu principal
Copiar código
Podemos digitar qualquer tecla para voltar ao menu principal.

Para garantir que o código funciona, vamos registrar mais uma banda. Digitamos o número 1 para entrar na opção de registro de bandas, onde cadastramos a banda Ira.

A banda Ira foi registrada com sucesso!

Novamente no menu principal, escolhemos a opção 2 para exibir as bandas registradas.

---

Exibindo todas as bandas registradas

---

Banda: U2
Banda: Beatles
Banda: Calypso
Banda: Ira

Digite uma tecla para voltar ao menu principal
Copiar código
Temos a banda Ira na cartela de bandas registradas.

Daniel: Conhecemos mais um recurso muito utilizado: o foreach. Com ele, guardamos o valor do elemento em uma variável para conseguir percorrer a lista. A desvantagem é que não temos o índice do for tradicional, caso seja preciso usá-lo.

Por isso, você precisa considerar o que você quer fazer com o loop.

Guilherme: Visualmente, o comprimento da linha de asteriscos está maior do que a frase "Exibindo todas as bandas registradas". Podemos arrumá-lo na função MostrarBandasRegistradas(), caso queiramos.
