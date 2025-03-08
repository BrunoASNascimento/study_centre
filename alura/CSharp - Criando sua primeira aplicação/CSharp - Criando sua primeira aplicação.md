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
