# Mensageria com Apache Kafka
## Kafka: produtores, consumidores e streams
### Introdução
Vamos analisar os diferenciais de Kafka em relação a outros sistemas de mensageria e entender porque o sistema de streams (fluxos) consegue, de uma maneira inteligente e interessante, paralelizar e distribuir o nosso processamento em diversos serviços e sistemas, e, ao mesmo tempo, serializá-lo quando for necessário e interessante para nós.

Vamos aprender como funcionam as partições, os tópicos, e o broker em execução. Além de criar diversos consumidores, grupos de consumidores, paralelizar e executá-los em paralelo.

Também executar produtores que geram diversas mensagens que são consumidas e que geram feedback, para entender como um sistema tradicional pode ser dividido em vários serviços de uma forma que utilize uma comunicação através de mensagens em que adquirimos certas independências entre os sistemas.

O sistema não é completamente independente, pois existe um esquema que tenta colar o que está acontecendo e a semântica das mensagens, que também é importante. Vamos entender como tudo isso se conecta dentro do Kafka e colocar em prática.

Então, vamos produzir o código, levantar servidor, derrubar servidor, acompanhar o que acontece quando está ativo, quando está inativo, quando está caído, seja o serviço, seja o produtor, seja o broker da Kafka. Enfim, vamos explorar tudo isso durante o curso.

### Mensageria e Kafka

Imagine um sistema de e-commerce. Nesse sistema, teremos uma pessoa usuária acessando o sistema online. Portanto, dentro do perfil de usuários, temos o navegador, que vamos referir como usuário. No OmniGraffle, vamos criar um retângulo e escrever:

navegador (usuário)

O cliente, através do navegador, acessa a web e, por meio dela, um servidor HTTP. Em outro retângulo, escreveremos:

servidor http

O acesso a esse servidor é feito e funciona. Para representar esse acesso, vamos desenhar uma seta do retângulo de "navegador (usuário)" para "servidor http" (esquerda para direita).

O servidor HTTP precisa realizar diversas tarefas, porque está envolvido em um processo de compra. A pessoa usuária está efetuando uma compra. Portanto, nós precisamos verificar se é uma fraude. Antes de verificar se é uma fraude, temos que enviar um e-mail informando que a compra está sendo processada. Caso seja identificada uma fraude, notificamos sistemas de segurança.

Sendo assim, complementamos o texto do retângulo de "servidor http":

servidor http

email, fraude? Notifico sistemas de segurança.

Se não for fraude, precisamos efetuar a compra e o pagamento. Se o pagamento for bem-sucedido, precisamos liberar o produto:

servidor http

email, fraude? Notifico sistemas de segurança. Compra/pagamento. Liberar.

Por exemplo, se é um produto online, como um e-book, precisamos gerar o e-book com a versão personalizada para aquela pessoa usuária, que contenha o nome da pessoa, o CPF, etc. E, finalmente, enviamos o produto para o e-mail.

Portanto, perceba que vai ficando cada vez mais complexo, com um passo após o outro. Vamos separar isso com setas e quadrados para facilitar a visualização. O servidor envia um e-mail. Nós poderíamos verificar a fraude após o e-mail e colocar todo esse código dentro de um único sistema. Funcionaria.

Interface do OmniGraffle. Fluxograma em fundo quadriculado contendo quatro caixas retangulares conectadas por setas que indicam a sequência de um processo. A primeira caixa à esquerda tem a inscrição "navegador (usuário)" e uma seta apontando para a segunda caixa com a inscrição "servidor http". Uma segunda seta conduz à terceira caixa intitulada "email", e uma terceira seta aponta para a quarta caixa com a interrogação "fraude?".
Primeiro, o servidor HTTP envia um e-mail, verifica se é fraude e segue um caminho conforme a resposta. Tudo dentro de um grande programa, uma linha após a outra. Um problema direto para os sistemas é que, por exemplo, esperar o e-mail significa esperar a resposta de um sistema externo: o servidor SMTP, que envia e-mails.

Pode ser que esse servidor esteja fora do ar ou lento. Portanto, vamos demorar para iniciar o processo de detecção de fraude, porque estamos esperando o e-mail. É muito comum que em sistemas web queiramos dar uma resposta para a pessoa usuária o mais rápido possível. Por isso, é muito comum que esse tipo de tarefa seja feita em paralelo.

Então, disparamos o e-mail e o sistema de verificação de fraude ao mesmo tempo. Quer dizer que podemos ter no mesmo computador duas threads (linhas de execução). Ou pode ser que estejamos nos comunicando com dois computadores diferentes e indicando que um deles envie um e-mail, uma requisição HTTP, via REST, ou algo do tipo.

Enquanto isso, já fornecemos uma resposta para nossa pessoa cliente dizendo "sua compra está sendo processada". E, então, vamos processando tudo isso em paralelo, na mesma máquina ou em máquinas distintas. São várias as opções.

Essa comunicação pode ser feita via HTTP, via REST, ou outro tipo de mensageria. O tradicional seria utilizar primeiro a mesma máquina com várias threads e depois máquinas distintas, se comunicando via HTTP.

Vamos prosseguir agora com esse sistema, levando em conta os apontamentos realizados agora. Independentemente de ser fraude ou não, precisamos fazer algo. Por exemplo, se não for fraude, temos que realizar o pagamento.

Depois de efetuar o pagamento, precisamos preparar o envio. Vamos pensar em um bem digital, como um PDF, um e-book. Nesse caso, teríamos que gerar o PDF. E, por fim, teríamos que enviar o e-mail do PDF.

Esta parte parece sequencial, porque não vamos gerar o PDF antes de efetuar o pagamento. Ou, pelo menos, não vamos enviar o e-mail antes de confirmar o pagamento. Agora temos várias setas: uma seta da detecção de fraude para a próxima etapa; do sistema de efetuar pagamento para gerar o PDF. E assim sucessivamente.

Isso é no caso de sucesso, onde efetuamos o pagamento. E no caso de falha? Também gostaríamos de enviar um e-mail.

Fluxograma de processo de pagamento com caixas retangulares de texto e setas. Este fluxograma é parte do que foi construído anteriormente, Começa com "servidor http", conectando a "email" que se bifurca para "fraude?", levando a "efetuar o pagamento". Há saídas de "efetuar o pagamento" para "enviar o email do fracasso" ou "gerar o pdf" e, em seguida, para "enviar o email do pdf".
Além disso, gostaríamos de ter suporte para produtos físicos. Portanto, se é um produto físico, temos estoque. E quando a pessoa solicita a compra, já precisamos reservar esse produto. Portanto, logo de início, precisamos reservar o estoque.

Temos três serviços diferentes, cada um rodando em uma máquina diferente. Três requisições HTTPs. Uma requisição HTTP, outra requisição, outra, e assim por diante.

A compra foi confirmada, efetuamos o pagamento. Se ela for digital, o que precisamos fazer? Precisamos confirmar o estoque. Reservamos, agora precisamos confirmar o estoque. E se houve uma falha, possivelmente cancelaremos o estoque. Só se for um produto físico.

Está ficando cada vez mais complexo. Podemos dizer que temos:

um serviço de estoque, com três URIs;
um serviço de fraude, com uma URI;
um serviço de pagamento, com uma URI;
um serviço de PDF, com uma URI;
um serviço de e-mail, com três URIs.
Mas todas essas comunicações, essas setas, somos nós quem programamos. Nós fazemos todas elas. Nós sabemos quem está na outra ponta e enviamos uma mensagem HTTP — podemos definir outro termo, de acordo com como essa requisição é feita — notificando o que gostaríamos que fosse feito, ou algo do gênero.

Vamos complicar mais ainda, como no mundo real. Para tudo isso, precisamos de log. Portanto, toda vez que dispararmos um e-mail, precisamos registrar em algum lugar que um e-mail foi disparado, isto é, precisamos de um sistema de log ou algum registro. Então, tudo que acontece deve ir para o sistema de log.

Se quisermos fazer uma auditoria, saber a ordem em que aconteceram as coisas ou algo do gênero, as informações devem ir para o sistema de log. Nem terminamos o sistema e já há tantas setas ligando todos os retângulos ao retângulo de "log" que não é possível entender nada. O motivo é que vários sistemas conhecem vários sistemas, gerando um emaranhado de passos.

Além do log, existem outros concerns (preocupações) que transpassam nossa aplicação inteira, que são os cross-cutting concerns (preocupações transversais). Por exemplo, os dados com analytics (análise). Precisamos saber como estamos em termos de fraude.

Vamos supor que estamos com 10%. Este valor é a nossa média histórica. Se hoje está 20%, então algo aconteceu com o nosso sistema de fraude ou com as pessoas que cometem fraude. Então, há algo estranho com o sistema, ou realmente as pessoas que cometem fraude estão fazendo um ataque, tentando fraudar o meu sistema.

Precisamos de um analytics para acompanhar as métricas, para saber se tem algo fora do ar, se tem algo que não está dando conta, se tem algo que começou a dar mais erro do que o comum. Precisamos ter controle não só das fraudes, mas também do pagamento.

A taxa de pagamento está como a taxa histórica de sucesso? A taxa de e-mails que são enviados com sucesso, que não dão bounce, que não batem e voltam, estão com taxa normal ou batendo e voltando mais? Ou seja, os servidores de e-mails estão considerando que nossos e-mails são spams. Tudo isso envolve Analytics.

Os arquivos PDF estão sendo gerados no ritmo esperado ou não? Estamos gerando muito mais? Deu algum bug e entrou num loop infinito. Ou não, estamos gerando vendas a menos, ou o sistema está lento e está acumulando arquivos PDF a serem gerados. Tudo envolve análise.

A implementação não é simples. Se o sistema de detecção de fraude falha, onde anotamos para notificar o Analytics daqui a um tempo? Para isso, existem sistemas de polling, de watchers, de observers. São várias estruturas complexas que nos ajudam a lidar com a dificuldade do processo interno.

O que antes era sequencial, passou a ser paralelo com o fim de potencializarmos o desempenho de nossa aplicação. Sendo assim, podemos executar 10 máquinas de detecção de fraude e somente uma de e-mail. Caso a efetuação de pagamentos também demandar muitos recursos, podemos contar com 5 máquinas.

Assim, conseguimos dimensionar cada um desses serviços com máquinas distintas, com a vantagem de ter tudo distribuído e “paralelizado”. Perceba a complexidade que é trabalhar com esse tipo de sistema. Existem sistemas e formas de trabalhar mais inteligentes ou, pelo menos, diferentes, que podem trazer certas vantagens nessas abordagens.

Vamos copiar todo o sistema que construímos e colar embaixo. A ideia é repensar todas as conexões (setas). Por exemplo, quando a pessoa usuária (poderia ser um aplicativo) acessa o servidor HTTP, o servidor recebe um pedido de compra. Então, ele simplesmente envia uma mensagem que se chama "novo pedido de compra".

Então, precisamos representar o broker (corretor), que é quem recebe mensagens. Assim, simplesmente enviamos uma mensagem para o broker e especificamos que ela é de nova compra, por exemplo. Não sabemos quem vai recebê-la e não importa, porque o e-mail disparado, quando há um novo pedido de compra, está captando a mensagem, cujo assunto é a nova compra.

O tema de "fraude", também está captando, assim como o "reservar o estoque", o "analytics" e o "log". O servidor HTTP sabe algo sobre isso? A resposta é não. Ele simplesmente envia uma mensagem avisando que há um novo pedido de compra e mostra as informações. Todos os temas estão captando o tópico "broker" e cada um realizará sua tarefa de forma assíncrona, na mesma máquina ou em máquinas distribuídas.

Então, para simplificar, nem precisamos adicionar as setas. Basta dizer que o serviço que está rodando em uma máquina, capta o tema "nova compra". O sistema de detecção de fraude, o sistema de reserva de estoque, o analytics e o log estão captando a nova compra.

Quando o e-mail é enviado, 'o serviço de e-mail, envia uma mensagem para o broker avisando que sua parte foi finalizada: enviar um e-mail. Tanto o log, quanto o analytics estão captando o e-mail enviado. Se não há fraude, vamos querer validar o pagamento.

O "fraude" envia a mensagem: "compra sem fraude". Captam esse tópico o "log" e o "analytics". Da maneira que estamos projetando os sistemas, indicamos que não importa quem captará a atualização de status, uma situação que ocorreu no sistema. Ocorreu um pedido de nova compra, um e-mail enviado e a compra foi validada sem fraude.

Além disso, o pagamento foi efetuado com sucesso e o PDF foi gerado. Quem está captando isso para agir não me importa. Esse é o conceito de mensageria. O conceito de mensageria, de troca de mensagens, aparece em diversos sistemas e implementações. O Kafka tem certos recursos, alguns comuns à mensageria e outros especiais, particulares dele.

Um dos recursos de mensageria é a possibilidade de ter rodando a quantidade de servidores e serviços de e-mail que quisermos. É como funcionava com o próprio HTTP. Se o sistema de fraude é um sistema que consome muita CPU e pouca memória, podemos ter várias máquinas com CPUs potentes rodando.

Se o sistema de gerar PDF consome pouco CPU, mas muita memória, podemos ter algumas máquinas com CPU mediano e bastante memória. É possível escalar de acordo com o necessário. Além disso, eliminamos um ponto de falha: se tivéssemos apenas uma máquina rodando e ela caísse, seria problemático. Se temos 10 máquinas rodando e uma cai, ainda temos 9. Desta maneira, vamos eliminando os pontos de falha.

O broker também pode ser replicado. Não é necessário ter um único broker rodando. Podemos ter um cluster de brokers, por exemplo, um cluster com 3 ou 30 brokers rodando 30 instâncias do Kafka. Quando enviamos uma mensagem, ela vai parar possivelmente em mais de um broker. Se um deles desligar, o outro receberá essa mensagem.

Se mandamos uma mensagem qualquer e ela fica armazenada em 3 máquinas, até ser recebida por quem quiser, caso uma delas cair, as outras duas ainda guardarão a mensagem. Assim, ganhamos mais reliability (confiabilidade), garantindo que as informações serão recebidas.

Mais que isso, conseguimos rodar em paralelo, como estamos fazendo. Os dados das mensagens que chegam são distribuídos para várias instâncias do detector de fraudes. Por exemplo, se recebermos 5 mensagens de novas compras, podemos enviar 2 para uma instância, 2 para outra e 1 para a terceira. Isso é possível caso tenhamos 3 instâncias de detecção de fraude.

Podemos, automaticamente, lidar com eventuais problemas do sistema. Por exemplo, se os sistemas de detecção de fraude caírem e só voltarem a funcionar no dia seguinte, não há problema. As mensagens ficam armazenadas e conseguimos executá-las um dia depois, sem maiores dificuldades.

Se por algum motivo as 10 máquinas falharem, conseguimos armazenar essa mensagem por um tempo configurável. Podemos configurar um tempo ou a quantidade de espaço em disco que queremos reservar para armazenar as mensagens sem problemas.

Podemos também definir, por exemplo, que se a compra de uma pessoa usuária foi identificada como fraude, as outras compras dessa mesma pessoa não serão executadas. Isso poderia ser uma configuração do sistema.

Mesmo que o Kafka permita a execução em paralelo, em determinados momentos, podemos definir que as compras para um usuário específico ou a mensagem de geração de PDF, seja processada em sequência.

Isso porque, se uma pessoa usuária comprou mil PDFs, não queremos que todos sejam gerados ao mesmo tempo, fazendo com que outras pessoas usuárias tenham que esperar. É preferível gerar um PDF para cada pessoa usuária. Assim, todas estarão lendo algo e ninguém ficará esperando.

Podemos, portanto, definir regras do tipo: mesmo desejando paralelização, quando pensamos em uma pessoa usuária, queremos que as ações referentes a ela sejam executadas em sequência.

Por exemplo, a reserva de estoque pode ser executada em paralelo, mas para um produto específico, provavelmente queremos que a reserva seja feita em sequência. Para o produto 5, por exemplo, queremos retirar do estoque em sequência. Mas para o produto 5 e para o produto 15, podemos processar em duas máquinas em paralelo, sem problemas.

Poderíamos usar o produto como chave para serializar a execução, ou seja, deixar em sequência. O Kafka é capaz de fazer tudo isso e nós vamos explorar essas capacidades nos cursos de Kafka da Alura.

### Instalando o Kafka localmente
Olá, pessoal! Neste vídeo, vamos aprender a instalar o Kafka e darei um primeiro exemplo via terminal, para visualizarmos tudo configurado corretamente.

Primeiramente, vamos acessar o site Apache Kafka, vamos acessar a área de "download" e baixar a última versão, 2.3.1, com uma versão mais recente de Scala, que é a 2.12. Esse é o TGZ que vamos baixar.

Após baixar o TGZ, vamos descompactá-lo, dar dois cliques, usar o terminal que preferir. No terminal, visualizaremos um problema muito comum quando executamos o Kafka.

Estamos dentro do diretório anterior, vamos entrar no diretório, acessar o Kafka no diretório de download, descompactar e acessar o diretório do kafka. Note que deixaremos um espaço entre apps\ e descompactadas/ proposital:

apps\ descompactadas/
tar zxf ../download/kafla_2.12-2.3.1.tgz
kafka_2.12-2.3.1/
pwd
/Users/alura/Documents/guilhermesilveira/1552-kafka1/apps descompactadas/kafka_2.12-2.3.1
Copiar código
No diretório do Kafka, encontraremos mais diretórios: o de scripts (bin) e o de configurações (config). Vamos acessar o diretório de scrips do Java com a configuração padrão de servidor:

bin/kafka-server-start.sh config/server.properties
Copiar código
Quando tentamos rodar, ele nos envia uma série de erros.

bin/kafka-server-start.sh config/server.properties
Copiar código
usage: dirname path

usage: dirname path

usage: dirname path

usage: dirname path

Classpath is empty. Please build the project first

// Retorno omitido.

O erro nos conduz a pensar que o projeto não está construído, mas não é isso. Mas não baixamos o código fonte, mas, sim, a versão binária, com o projeto já construído, pronto para executar.

O problema, na verdade, está no diretório path que estamos utilizando. Há um espaço entre \apps e descompactadas/. Então, o diretório que antes se chamava apps descompactadas agora se chamará apenas apps. Feita a mudança, podemos retornar ao Kafka e codar:

bin/kafka-server-start.sh config/server.properties
Copiar código
Tentamos executar, ele roda o Java 13 que já está instalado, mas aponta vários erros e desliga. Por quê? Porque o Kafka é o processador dessas mensagens, no sentido de conectar tudo. Mas, onde ele armazena essas informações? O Kafka armazena algumas informações básicas no Zookeeper. Então, vamos baixar o zookeeper, acessando Apache ZooKeeper.

Lembrando que Kafka já vem com o Zookeeper instalado, caso você não queira instalar separadamente. Porque pode haver empresas que já tem o Zookeeper rodando por outros motivos. No nosso caso, nós não temos. Então, antes de rodar o Kafka, vamos executar:

bin/zookeeper-server-start.sh config/zookeeper.properties
Copiar código
Já temos as propriedades padrão configuradas e vamos utilizá-las. Nos conectamos com 0.0.0.0/0.0.0.0, na porta 2181. O Zookeeper está rodando. Agora, sim, vamos abrir outra aba e tentar acessar o mesmo diretório:

bin/kafka-server-start.sh config/server.properties
Copiar código
Ele vai tentar se conectar ao Zookeeper. Ele se conecta, mostra uma série de propriedades padrão que está utilizando, e, ao final do retorno, está escrito "started". Significa que ele está rodando o Kafka em algum lugar.

O Kafka está em execução e conseguimos encontrar a porta padrão 9092, isto é, port = 9092, que está especificada em server properties. Portanto, temos a propriedade que está na porta 9092, operando o Kafka e, por trás, o Zookeeper para algumas configurações. Não para todos os dados, apenas algumas configurações.

Agora, vamos enviar uma mensagem de um lado para o outro e analisar o Kafka em funcionamento. Vamos testar no terminal outra vez e no mesmo diretório, Kafka. A ideia é criar um tópico para trocar mensagens:

bin/kafka-topics.sh
Copiar código
Visualizaremos tudo o que o Kafka Topics nos permite fazer e existem várias funções. O que vamos fazer é criar um tópico. Mas precisamos indicar onde o Kafka está rodando. Ele está rodando bootstrap-server, em localhost porta 9092:

bin/kafka-topics.sh --create --bootstrap-server localhost:9092
Copiar código
Então, estamos indicando uma conexão com o Kafka, localhost:9092, e definiremos duas propriedades padrão. Elas serão utilizadas durante todos os cursos. Portanto, não se preocupe, vamos nos aprofundar no estudo sobre elas aos poucos.

Por enquanto, vamos deixar fixos o replication factor e o partitions como 1:

bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 
Copiar código
Também definiremos o nome do tópico. Pode ser o padrão que quiser. Imagine que temos um novo pedido chegando na nossa loja. Então, poderíamos definir como LOJA_NOVOPEDIDO ou LOJA.NOVOPEDIDO. A sugestão do Kafka Topics é não misturar ponto com underline. Por isso, não vamos misturar. Manteremos o underline como padrão, sugerindo que a loja teve um novo pedido.

bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic LOJA_NOVO_PEDIDO 
Copiar código
Será que é o melhor padrão? Não existe muito um melhor ou pior padrãoa, apenas usar ponto e underline ao mesmo tempo não é uma recomendação do Kafka. Ao tentar criar o código, recebemos um aviso de que, por limitações nas métricas dos nomes, tópicos com período, ponto ou underscore podem colidir. Portanto, a melhor maneira é usar um ou outro, mas não ambos.

Para nos certificarmos de que o tópico foi criado, passaremos:

bin/kafka-topics.sh --list --bootstrap-server localhost:9082
Copiar código
LOJA_NOVO_PEDIDO

Esses comandos são muito úteis no dia a dia. Vamos usar várias vezes. O retorno confirma que existe sim um tópico chamado LOJA_NOVO_PEDIDO. Podemos enviar algumas mensagens para esse tópico. No Kafka, há uma indicação de criação da partição para o tópico, especificamente a partição 0. Ou seja, só existe uma partição, e ela começa com 0. Portanto, confirmamos que o tópico realmente está lá.

Em outra aba, vamos rodar um produtor de mensagens:

bin/kafka-console-producer.sh
Copiar código
Também vamos informar que os brokers Kafka estão rodando no localhost:9092:

bin/kafka-console-producer.sh -- broker-list localhost:9092
Copiar código
Em seguida, dizemos qual é o tópico:

bin/kafka-console-producer.sh -- broker-list localhost:9092 LOJA_NOVO_PEDIDO
Copiar código
Quando o console-producer na linha de comando, cada linha que escrevemos corresponde a uma mensagem. Poderíamos, por exemplo, criar uma mensagem dizendo que o pedido zero teve valor de 550 reais:

bin/kafka-console-producer.sh -- broker-list localhost:9092 LOJA_NOVO_PEDIDO
pedido0, 550
Copiar código
Que o pedido 1 foi 330 reais e o pedido 2 foi 67213:

bin/kafka-console-producer.sh -- broker-list localhost:9092 LOJA_NOVO_PEDIDO
pedido0, 550
pedido1, 330
pedido2, 67213
Copiar código
Agora, vamos consumir essas mensagens. Para isso, abriremos uma nova aba e passaremos o comando:

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic LOJA_NOVO_PEDIDO
Copiar código
Agora, surge uma pergunta. Devemos consumir a partir de quando? Desde a primeira mensagem armazenada ou a partir das mensagens que chegam agora? Se executarmos da forma como está, não recebemos nenhuma mensagem.

Vamos abrir uma nova aba e executar o comando:

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic LOJA_NOVO_PEDIDO --from-beginning
Copiar código
Assim, estamos indicando para começar da primeira mensagem armazenada no kafka. Ele vai começar da primeira mensagem, verificar quais mensagens estão armazenadas e consumi-las.

Neste ponto, ainda não recebi nada, porque não tiveram novas mensagens. No entanto, tive três mensagens do passado que estavam armazenadas esperando alguém consumir.

Agora, vamos enviar uma nova mensagem:

bin/kafka-console-producer.sh -- broker-list localhost:9092 LOJA_NOVO_PEDIDO
pedido0, 550
pedido1, 330
pedido2, 67213
pedido3, 6423
Copiar código
Recebemos o "Pedido 3" nos dois consumidores. Excelente!

Vamos discutir ao longo do curso se queremos receber em todos os consumidores, apenas em um consumidor, como receber, quantas partições, quantas repetições, ter certeza de que vai receber, ter certeza de que começou desde o início, entre outros aspectos.

Mas, por enquanto, aprendemos como instalar o Kafka e como verificar os tópicos que estão lá. Vamos explorar esse tópico mais vezes, como criar um produtor que envia strings simples e um ou mais consumidores que consomem essas strings, apenas para visualizarmos funcionando.

A partir de agora, queremos executar isso com programação e entender todas as vantagens e desvantagens que teremos com o Kafka em nossos programas. Esses são nossos próximos passos!

### Criando produtores em Java
Agora que estamos preparados para iniciar nosso projeto, vamos dar o primeiro passo: criar o projeto em si. Para isso, utilizaremos o IntelliJ, um ambiente de desenvolvimento integrado (IDE) que pode ser facilmente baixado da internet por meio do endereço https://www.jetbrains.com/idea/download/?section=windows.

Ao iniciar o IntelliJ, vamos criar um novo projeto, seguindo a abordagem baseada em Maven, utilizando a linguagem Java na versão 13, embora versões mais recentes também possam ser utilizadas sem problemas. Ao criar o projeto Maven, o IntelliJ solicitará informações como o grupo e o nome do projeto. Aqui, vamos definir o grupo como br.com.alura e nomear nosso projeto como ecommerce, indicando que estamos criando uma aplicação para uma loja virtual.

Após isso, o IntelliJ nos pedirá para selecionar o diretório onde desejamos salvar o projeto, e em seguida, finalizaremos o processo. Com isso, o projeto será criado.

É importante ressaltar que, embora esta série de cursos seja conduzida em Java, focando na utilização e compreensão do Kafka, os conceitos e desafios abordados podem ser aplicados em diversas outras linguagens de programação. O objetivo principal é explorar os problemas, vantagens e estruturas de utilização do Kafka, independente da linguagem de programação utilizada.

Durante o curso, nos concentraremos em Java, uma das linguagens mais populares do mercado para projetos desse tipo. No entanto, é importante ressaltar que os desafios enfrentados e as soluções desenvolvidas serão semelhantes, independentemente da linguagem escolhida. Então você poderá aplicar os conhecimentos adquiridos em sua linguagem de preferência no dia a dia, seja ela Clojure, C#, Ruby, Python, entre outras. Os problemas se concentram mais na área de mensageria distribuída do que na escolha da linguagem em si.

Quando criamos o arquivo pom.xml, é comum receber notificações para atualizações. No entanto, uma prática que preferimos é ativar o Auto Import, facilitando a atualização automática das dependências.

Agora que o projeto está configurado, podemos adicionar a dependência do Kafka. Para isso, no arquivo pom.xml, dentro da seção de dependências, incluiremos a dependência do Kafka, conhecida como "Kafka Clients". Você pode pesquisar por "Kafka Maven" ou "Maven Kafka Clients", dependendo da ferramenta de gerenciamento de dependências que está utilizando. Optamos pelo MVN Repository por sua facilidade de uso: basta escolher a ferramenta que estamos utilizando, copiar e colar a dependência. Ao salvar o arquivo, o Maven irá baixar automaticamente o Kafka Clients.

<dependencies>
    <!-- https://mvnrepository.com/artifact/org.apache.kafka/kafka-clients -->
    <dependency>
        <groupId>org.apache.kafka</groupId>
        <artifactId>kafka-clients</artifactId>
        <version>2.3.1</version>
    </dependency>
</dependencies>
Copiar código
Além do Kafka Clients, também adicionaremos a dependência do SLF4J, um sistema de log simples utilizado pelo Kafka. Não usaremos a versão alpha ou beta, pois optaremos pela versão estável mais recente. Removeremos o escopo de teste (<scope>test</scope>), pois queremos utilizar essas dependências em nossa aplicação de maneira definitiva.

<dependencies>
    <!-- https://mvnrepository.com/artifact/org.apache.kafka/kafka-clients -->
    <dependency>
        <groupId>org.apache.kafka</groupId>
        <artifactId>kafka-clients</artifactId>
        <version>2.3.1</version>
    </dependency>

    <!-- https://mvnrepository.com/artifact/org.slf4j/slf4j-simple -->
    <dependency>
        <groupId>org.slf4j</groupId>
        <artifactId>slf4j-simple</artifactId>
        <version>1.7.29</version>
    </dependency>
</dependencies>
Copiar código
Tudo está configurado e sincronizado, e as dependências foram baixadas com sucesso. Agora, vamos ao diretório src, onde encontramos java. Vamos criar uma classe, que será o coração do nosso projeto.

Neste projeto, queremos simular o cenário em que um cliente entra no sistema e cria um pedido de compra. Então, estamos criando uma nova ordem de compra, por isso nomearemos esta classe como NewOrderMain, para deixar claro que se trata de um método principal que executamos ocasionalmente, e que será responsável por criar um novo pedido de compra.

Para começar, vamos definir o pacote da classe como package br.com.alura.ecommerce. Depois, vamos definir o main para iniciar nossa aplicação.

package br.com.alura.ecommerce:

public class NewOrderMain {

    public static void main(String[] args) {
    
    }
}
Copiar código
Nosso objetivo é criar uma mensagem e enviá-la para o Kafka, ou seja, produzir uma mensagem. Para isso, precisaremos de um KafkaProducer. Observe que o KafkaProducer requer dois parâmetros de tipagem: o tipo da chave e o tipo da mensagem. Por enquanto, vamos utilizar o tipo String para ambos. Conforme avançarmos e explorarmos mais sobre chaves e mensagens, discutiremos os tipos adequados.

package br.com.alura.ecommerce:

public class NewOrderMain {

    public static void main(String[] args) {
        KafkaProducer<String, String>
    }
}
Copiar código
Vamos instanciar nosso produtor Kafka utilizando var producer. Ao fazer isso, aparece uma indicação de erro no var. Isso, porque, o var só foi introduzido a partir do Java 10. Então, vamos fazer a alteração no Maven. Para isso, clicamos no Quick Fix e selecionamos a opção "Set language level to 10 - Local variable type inference".

Com isso, o Maven foi alterado para o Java 10. Mas podemos especificar que queremos utilizar a partir do Java 12, por exemplo, que já é suficiente para nós. Então, vamos configurar o Maven para Java 12, o que permitirá o uso do var.

<plugins>
    <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <configuration>
            <source>12</source>
            <target>12</target>
        </configuration>
    </plugin>
</plugins>
Copiar código
Agora, o código com var está funcionando.

package br.com.alura.ecommerce:

public class NewOrderMain {

    public static void main(String[] args) {
        var producer = new KafkaProducer<String, String>
    }
}
Copiar código
Porém, observe que estamos lidando com um new KafkaProducer e este construtor requer algumas propriedades. Vamos criar essas properties manualmente. Embora pudéssemos ler essas informações de um arquivo, faremos isso programaticamente para uma melhor compreensão.

package br.com.alura.ecommerce:

public class NewOrderMain {

    public static void main(String[] args) {
        var producer = new KafkaProducer<String, String>(properties());
    }
}
Copiar código
Vamos começar criando um método estático que retorna um objeto Properties.

private static Properties properties() {
    var properties = new Properties();
    return properties;
    }
}
Copiar código
Em seguida, vamos definir algumas propriedades importantes. Primeiro, precisamos especificar onde nos conectaremos. Os servidores Kafka normalmente são configurados em ProducerConfig, que é uma configuração do produtor. Lá, especificamos os servidores de inicialização, como 127.0.0.1:9092, que representa o localhost na porta 9092.

private static Properties properties() {
    var properties = new Properties();
    properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "127.0.0.1:9092");
    return properties;
    }
}
Copiar código
Outra propriedade relevante é o tipo de serializador a ser usado para transformar a mensagem e a chave de strings para bytes. Portanto, configuramos KEY_SERIALIZER_CLASS_CONFIG, que é um serializador de strings, com StringSerializer.class.getName() para pegar o nome da classe. Depois, fazemos o mesmo processo para a mensagem com o serializador VALUE_SERIALIZER_CLASS_CONFIG, também utilizando `StringSerializer.class.getName().

private static Properties properties() {
    var properties = new Properties();
    properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "127.0.0.1:9092");
    properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
    properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
    return properties;
    }
}
Copiar código
Então, ambos usarão o StringSerializer, o que significa que as strings serão convertidas em bytes.

Agora, temos nosso produtor configurado. Com isso feito, podemos enviar algo. Uma maneira simples de fazer isso é usando producer.send(). Vamos enviar uma mensagem que será um record, ou seja, um registro, porque será armazenado no Kafka. O tempo que ficará armazenado depende das configurações do seu server properties. É importante ter em mente que o espaço em disco, por exemplo, pode acabar, dependendo das configurações de espaço máximo também definidas no server properties.

Então, vamos criar um record usando new ProducerRecord, classe que importaremos usando o Quick Fix. Este registro tem uma chave e um valor. Além disso, precisamos especificar o tópico ao qual a mensagem será enviada. No nosso caso, será "ECOMMERCE_NEW_ORDER", mantendo o padrão em inglês e indicando que temos um novo pedido de compra.

O próximo parâmetro possui diversas variações, mas queremos usar apenas a chave e o valor, que por enquanto serão os mesmos: value. Este value pode ser, por exemplo, o ID do pedido, o ID do usuário e o valor da compra. Tanto a chave quanto o valor serão os mesmos neste exemplo.

public static void main(String[] args) {
        var producer = new KafkaProducer<String, String>(properties());
        var value = "132123,67523,7894589745";
        var record = new ProducerRecord<String, String>(topic: "ECOMMERCE_NEW_ORDER", value, value);
        producer.send(record);
    }
Copiar código
Por enquanto, não estamos preocupados com detalhes como a importância da chave ou outros aspectos mais específicos. Uma observação interessante é que o IDE já percebeu que tanto a chave quanto o valor são strings, então podemos remover essa especificação, tornando o código mais simples.

public static void main(String[] args) {
        var producer = new KafkaProducer<String, String>(properties());
        var value = "132123,67523,7894589745";
        var record = new ProducerRecord<>(topic: "ECOMMERCE_NEW_ORDER", value, value);
        producer.send(record);
    }
Copiar código
Portanto, utilizamos o construtor new ProducerRecord para criar um registro e o enviamos através do método send do produtor. Agora, vamos enviar esse registro e observar o que acontece.

Este é o código completo:

package br.com.alura.ecommerce;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization. StringSerializer;

import java.util.Properties;

public class NewOrderMain {

    public static void main(String[] args) {
        var producer = new KafkaProducer<String, String>(properties());
        var value = "132123,67523,7894589745";
        var record = new ProducerRecord<>(topic: "ECOMMERCE_NEW_ORDER", value, value);
        producer.send(record);
    }

private static Properties properties() {
    var properties = new Properties();
    properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "127.0.0.1:9092");
    properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName())
    properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName())
    return properties;
    }
}
Copiar código
Vamos salvar o nosso arquivo. Agora que temos isso compilado, podemos avançar.

O tópico ECOMMERCE_NEW_ORDER é onde vamos postar uma mensagem. Vamos testar? Para fazer isso, clicamos com o botão direito do mouse e selecionamos a opção "Run 'NewOrderMain.main()'".

Ao executar, ele deveria conectar-se ao nosso Kafka e tentar enviar a mensagem, mas algo aconteceu. A aplicação está tentando enviar algo para ECOMMERCE_NEW_ORDER, mas está ocorrendo um problema.

No log, há várias mensagens registradas. Ao final, podemos ver que ele tentou enviar a mensagem, mas não encontrou nenhum líder para executar essa ação. Isso ocorreu em 127.0.0.1:9092.

Vamos verificar os tópicos. Para isso, faremos uma lista para ver todos os tópicos disponíveis utilizando --list --bootstrap-server localhost:9092. Ao fazer isso, notamos que tem mais de um tópico. Agora podemos descrevê-los com --bootstrap-server localhost:9092 --describe .

Com isso, ele vai nos fornecer informações detalhadas sobre cada tópico. No entanto, se verificarmos atentamente, veremos ECOMMERCE_NEW_ORDER e LOJA_NOVO_PEDIDO. Ou seja, temos os dois tópicos disponíveis, mas por que gerou um erro afirmando que não encontrou um líder?

Nós acabamos de criar este tópico, então vamos executar novamente. Ao fazer isso, não recebemos nenhum log de confirmação. Então, vamos executar --describe mais uma vez.

No log, vemos que ECOMMERCE_NEW_ORDER possui uma partição, um líder e uma réplica. Não conseguimos identificar se a mensagem foi ou não enviada. Isso, porque, analisando o método .send(), vemos que ele devolve um future - algo que será executado em instantes. Então o método send() é assíncrono. Se quisermos aguardar sua execução, precisamos utilizar .get()

    public static void main(String[] args) {
        var producer = new KafkaProducer<String, String>(properties());
        var value = "132123,67523,7894589745";
        var record = new ProducerRecord<>(topic: "ECOMMERCE_NEW_ORDER", value, value);
        producer.send(record).get();
    }
Copiar código
É possível que ocorram exceções durante esse processo. Enquanto aguardamos, pode ocorrer uma interrupção ou até mesmo erros na execução. Portanto, várias exceções são possíveis. Vamos tentar executar pela terceira vez.

Ao executar, ainda não recebemos uma mensagem indicando sucesso ou falha. Isso porque ainda não implementamos essa funcionalidade. O ideal seria receber notificações sobre o sucesso ou falha do envio assim que ocorresse. O método .get() pode até retornar algum feedback, mas o que realmente queremos é ser notificados em tempo real quando algo acontecer em paralelo. Portanto, queremos passar um callback para o Kafka, especificamente para o produtor de mensagens, e o método .send() possui uma variação que aceita um callback.

Então, precisamos apenas implementar essa interface callback, que possui um método chamado onCompletion(), que recebe metadados de sucesso (data) ou uma exceção em caso de falha (ex). Ele será responsável por lidar com os dados de sucesso ou a exceção de falha, dependendo do caso.

    public static void main(String[] args) {
        var producer = new KafkaProducer<String, String>(properties());
        var value = "132123,67523,7894589745";
        var record = new ProducerRecord<>(topic: "ECOMMERCE_NEW_ORDER", value, value);
        producer.send(record, (data, ex) -> {
        
        }).get();
    }
Copiar código
Se a exceção não for nula, significa que ocorreu um erro. Nesse caso, vamos imprimi-la e encerrar. Se a exceção for nula, significa que foi um sucesso. Então, vamos imprimir uma mensagem com os detalhes do tópico, partição, offset e timestamp em que a mensagem foi enviada. Assim, teremos uma confirmação de que a mensagem foi enviada com sucesso para esse tópico.

public static void main(String[] args) {
    var producer = new KafkaProducer<String, String>(properties());
    var value = "132123,67523,7894589745";
    var record = new ProducerRecord<>("ECOMMERCE_NEW_ORDER", value, value);
    producer.send(record, (data, ex) -> {
        if (ex != null) {
            ex.printStackTrace();
            return;
        }
        System.out.println("sucesso enviando " + data.topic() + ":::partition " + data.partition() + "/ offset " + data.offset() + "/ timestamp " + data.timestamp());
    }).get();
}
Copiar código
Então, estamos adicionando um observador para ser notificado quando a execução paralela terminar. Vamos executar novamente, agora pela quarta vez.

Ao fazer isso, recebemos todas as informações de log e a mensagem "sucesso enviando ECOMMERCE_NEW_ORDER::: partition 0/ offset 1/ timestamp 1574087304454". Nos dois primeiros casos, não esperamos terminar. Já na terceira e quarta vez, esperamos até que fossem enviadas. Por isso, o offset agora é 1: tivemos duas mensagens, a 0 e a 1, que foram a terceira e a quarta execução, respectivamente, em que realmente esperamos que as mensagens fossem enviadas. Funcionou! Se rodarmos novamente, este offset deve aumentar para 2, porque estaremos enviando mais uma mensagem.

Vamos voltar para o terminal. Lembre-se que temos alguns consumidores. Tínhamos um produtor simples de mensagens em um tópico que não vamos mais usar. Vamos teclar "Ctrl + C" para limpar a tela, já que não estamos mais usando.

Além disso, tínhamos dois consumidores, um deles estava consumindo do tópico LOJA_NOVO_PEDIDO, que agora será alterado para ECOMMERCE_NEW_ORDER desde o início.

--bootstrap-server localhost:9092 --topic ECOMMERCE_NEW_ORDER --from-beginning
Copiar código
Ao executar, consumiu três mensagens: a terceira, a quarta e a quinta, que enviamos agora. Ou seja, os offsets 0, 1 e 2. Agora, vamos parar o outro consumidor que também não vamos mais usar.

Produzir mensagens resume-se a isso: criar um produtor, criar mensagens, enviá-las e adicionar algum listener. Assim, ficamos ouvindo e quando a mensagem é bem-sucedida sabemos que foi realmente enviada. Enquanto não recebermos a confirmação, não podemos ter certeza.

Nós já enviamos a mensagem. Agora, quem está ouvindo essa mensagem? Quais são os consumidores? Vamos implementá-los em Java logo mais!

### Criando consumidores em Java
Quando uma nova solicitação de compra entra em nosso sistema, várias operações podem ser desencadeadas. Podemos ter múltiplos consumidores executando diversas tarefas simultaneamente. Em nosso caso, um desses consumidores será responsável por verificar se a transação é uma fraude ou não. Portanto, precisamos desenvolver um serviço dedicado a essa detecção.

Dentro de java > br.com.alura.ecommerce, criaremos uma nova classe chamada FraudDetectorService, que conterá diversas funções internas responsáveis por realizar essa verificação de fraude. Além disso, teremos uma função estática e criaremos um consumidor Kafka, que será um new KafkaConsumer. Vale ressaltar que tanto a chave quanto o valor serão strings.

package br.com.alura.ecommerce;

import org.apache.kafka.clients.consumer.KafkaConsumer;

public class Fraud DetectorService {

    public static void main(String[] args) {
        var consumer = new KafkaConsumer<String, String>()
    }
}
Copiar código
Ao criarmos o consumidor, ele receberá as propriedades (properties) do consumidor, seguindo uma abordagem semelhante ao que fizemos anteriormente. Depois, criaremos essas propriedades e configuramos. Por padrão, essas propriedades incluirão várias informações importantes, entre elas temos o ConsumerConfig ao invés de ProducerConfig, além do servidor, definido pela propriedade BOOTSTRAP_SERVERS_CONFIG, que indica onde o consumidor irá escutar, e o endereço 127.0.0.1:9092, onde ele tentará iniciar a conexão.

package br.com.alura.ecommerce;

import org.apache.kafka.clients.consumer.KafkaConsumer;

public class Fraud DetectorService {

    public static void main(String[] args) {
        var consumer = new KafkaConsumer<String, String>()
    }
    
    private static Properties properties() {
        var properties = new Properties();
        properties.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "127.0.0.1:9092");
        return properties;
    }
}
Copiar código
Além disso, teremos outras propriedades a serem configuradas. Uma delas é o deserializador, que agora será responsável por transformar os bytes em strings, já que anteriormente fizemos a serialização de strings para bytes. Portanto, as chaves (KEY_DESERIALIZER_CLASS_CONFIG) serão deserializadas utilizando o StringDeserializer e .class.getName().

Essas configurações de deserialização serão aplicadas tanto para as chaves quanto para os valores (VALUE_DESERIALIZER_CLASS_CONFIG), utilizando o mesmo deserializador de string. Embora haja mais configurações disponíveis, optaremos por abordá-las posteriormente. Por enquanto, focaremos nessas configurações.

package br.com.alura.ecommerce;

import org.apache.kafka.clients.consumer.KafkaConsumer;

public class Fraud DetectorService {

    public static void main(String[] args) {
        var consumer = new KafkaConsumer<String, String>()
    }
    
    private static Properties properties() {
        var properties = new Properties();
        properties.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "127.0.0.1:9092");
        properties.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        properties.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        return properties;
    }
}
Copiar código
Quanto ao comportamento do nosso consumidor, ele irá simplesmente solicitar a leitura de mensagens de um determinado local. Para isso, usaremos o método consumer.subscribe() para se inscrever em um tópico específico. Em seguida, passamos uma Collections e uma .singletonList(), que é uma forma simples de criar uma lista. Nesta lista, indicaremos que nosso consumidor irá subscrever o tópico "ECOMMERCE_NEW_ORDER".

package br.com.alura.ecommerce;

import org.apache.kafka.clients.consumer.KafkaConsumer;

public class Fraud DetectorService {

    public static void main(String[] args) {
        var consumer = new KafkaConsumer<String, String>()
        consumer.subscribe(Collections.singletonList("ECOMMERCE_NEW_ORDER"));
    }
    
    private static Properties properties() {
        var properties = new Properties();
        properties.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "127.0.0.1:9092");
        properties.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        properties.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        
        return properties;
    }
}
Copiar código
É possível escutar em mais de um tópico, mas isso é incomum porque se torna confuso ter um consumidor escutando em diversos tópicos simultaneamente. Geralmente, cada serviço tem uma função específica e, portanto, estará escutando em um tópico relacionado a essa função específica.

Agora, queremos verificar se há mensagens disponíveis para consumo. Para isso, criaremos uma var record e utilizaremos consumer.poll() passando Duration.ofMillis(100), o que significa que queremos fazer essa verificação por um determinado período de tempo, como 100 milissegundos, o que geralmente é suficiente.

Esse método nos retornará uma lista de registros. Esses registros são exatamente as mensagens que foram enviadas para o tópico em questão. Portanto, podemos verificar se essa lista está vazia. Se estiver vazia, significa que não há mensagens disponíveis para consumo. Em seguida, faremos um retorno (return).

    public static void main(String[] args) {
        var consumer = new KafkaConsumer<String, String>()
        consumer.subscribe(Collections.singletonList("ECOMMERCE_NEW_ORDER"));
        var record = consumer.poll(Duration.ofMillis(100));
        if(records.isEmpty()) {
            System.out.println("Não encontrei registros");
            return;
        }
    }
Copiar código
Se encontrarmos registros disponíveis, vamos iterar sobre eles utilizando um loop for. Para cada registro em nossa lista de registros, vamos realizar alguma ação. Por exemplo, podemos imprimir uma mensagem indicando que estamos verificando se há fraude na nova ordem: "Processing new order, checking for fraud".

Para isso, podemos aproveitar as informações contidas em cada registro, como a chave, o valor da mensagem, a partição à qual pertence e o offset associado a essa mensagem. Vamos incluir a impressão de um conjunto de hífens para imprimir essas informações de forma organizada, deixando claro que estamos processando uma nova mensagem a cada iteração do loop.

    public static void main(String[] args) {
        var consumer = new KafkaConsumer<String, String>()
        consumer.subscribe(Collections.singletonList("ECOMMERCE_NEW_ORDER"));
        var record = consumer.poll(Duration.ofMillis(100));
        if(records.isEmpty()) {
            System.out.println("Não encontrei registros");
            return;
        }
        for(var record: records) {
            System.out.println("---------------------");
            System.out.println("Processing new order, checking for fraud");
            System.out.println(record.key());
            System.out.println(record.value());
            System.out.println(record.partition());
            System.out.println(record.offset());
        }
    }
Copiar código
Para simular um processo de verificação de fraude mais demorado, vamos introduzir um atraso entre o processamento de cada registro utilizando a função Thread.sleep(5000), que vai fazer com que o programa aguarde por cinco segundos antes de prosseguir para o próximo registro.

Além disso, vamos adicionar um bloco try-catch para lidar com qualquer exceção que possa surgir durante o processo de espera. Apesar de não estarmos realizando nenhuma ação específica durante esse intervalo, isso nos permitirá criar uma pausa artificial.

Então, vamos adicionar uma instrução System.out.println() para indicar que a ordem foi processada com sucesso ou sem sucesso. Dessa forma, conseguiremos acompanhar o progresso do processamento de nossas ordens.

    public static void main(String[] args) {
        var consumer = new KafkaConsumer<String, String>()
        consumer.subscribe(Collections.singletonList("ECOMMERCE_NEW_ORDER"));
        var record = consumer.poll(Duration.ofMillis(100));
        if(records.isEmpty()) {
            System.out.println("Não encontrei registros");
            return;
        }
        for(var record: records) {
            System.out.println("---------------------");
            System.out.println("Processing new order, checking for fraud");
            System.out.println(record.key());
            System.out.println(record.value());
            System.out.println(record.partition());
            System.out.println(record.offset());
            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                // ignoring
                e.printStackTrace();
            }
                System.out.println("Order processed");
        }
    }
Copiar código
Agora, vamos tentar executar nosso serviço de detecção de fraude uma vez e observar o que acontece. Vale lembrar que já enviamos três mensagens, então vamos ver como nosso serviço reage a esses registros.

Ao tentar executar, recebemos uma mensagem informando a necessidade de especificar um grupo. Acontece que podemos ter o detector de fraude em execução, mas também podemos ter outras funcionalidades como o envio de e-mails de confirmação de compra ou um sistema de análise de dados que precisa acessar as mesmas mensagens.

Portanto, é importante que cada uma dessas funcionalidades receba todas as mensagens disponíveis. Isso significa que o FraudDetectorService, o Log Service e qualquer outro serviço que esteja escutando esse tópico precisam receber todas as mensagens. Cada um desses serviços é associado a um grupo diferente.

Quando criamos um consumidor, precisamos especificar a qual grupo ele pertence. Para isso, utilizaremos o ID do grupo (GROUP_ID_CONFIG), que será o nome da nossa classe.

Neste caso, para identificar nosso grupo, poderíamos usar FraudDetectorService com .class.getName(). Porém, o método .getName() retorna o nome completo da classe, incluindo o pacote. Então, optaremos pelo método .getSimpleName() para obter um nome mais simples para o ID do grupo, sendo apenas FraudDetectorService.

    private static Properties properties() {
        var properties = new Properties();
        properties.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "127.0.0.1:9092");
        properties.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        properties.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        properties.setProperty(ConsumerConfig.GROUP_ID_CONFIG, FraudDetectorService.class.getSimpleName());
        return properties;
    }
Copiar código
Portanto, nosso serviço estará associado a um grupo chamado FraudDetectorService. Isso significa que o FraudDetectorService receberá todas as mensagens do tópico. Se houver outros serviços com grupos diferentes, cada um receberá todas as mensagens. No entanto, se dois serviços estiverem no mesmo grupo, as mensagens serão distribuídas entre eles.

Ou seja, um grupo receberá todas as mensagens, mas se vários serviços estiverem no mesmo grupo, não poderemos prever quais mensagens cada serviço receberá. No final, todas as mensagens serão processadas, mas não haverá garantia sobre qual serviço receberá qual mensagem. Essa é a essência dos grupos.

Vamos executar novamente. Ao fazê-lo, não encontramos registros, pois o consumidor está configurado para buscar apenas novas mensagens e ainda não há nenhuma disponível.

Então, o próximo passo é manter o serviço continuamente escutando novas mensagens. Para isso, podemos colocar a chamada do método .poll() dentro de um loop while(true). Isso mantém o serviço em execução indefinidamente, pois ele continuará escutando caso cheguem novas mensagens.

    public static void main(String[] args) {
        var consumer = new KafkaConsumer<String, String>()
        consumer.subscribe(Collections.singletonList("ECOMMERCE_NEW_ORDER"));
        while(true) {
        var record = consumer.poll(Duration.ofMillis(100));
        if(records.isEmpty()) {
            System.out.println("Não encontrei registros");
            return;
        }
        for(var record: records) {
            System.out.println("---------------------");
            System.out.println("Processing new order, checking for fraud");
            System.out.println(record.key());
            System.out.println(record.value());
            System.out.println(record.partition());
            System.out.println(record.offset());
            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                // ignoring
                e.printStackTrace();
            }
                System.out.println("Order processed");
        }
    }
}
Copiar código
Dentro desse loop, podemos adicionar outras condições de saída, como um sinalizador para indicar quando o serviço deve ser encerrado. Por enquanto, vamos manter simplesmente em um loop while(true). Ao rodar novamente, veremos o serviço aguardando por mensagens.

No entanto, ao encontrar a condição de não haver registros, ele para. Isso, porque, atualmente, estamos usando um return, o que termina a execução do método. Em vez disso, devemos usar um continue para retornar ao início do loop e continuar ouvindo por novas mensagens.

    public static void main(String[] args) {
        var consumer = new KafkaConsumer<String, String>()
        consumer.subscribe(Collections.singletonList("ECOMMERCE_NEW_ORDER"));
        while(true) {
        var record = consumer.poll(Duration.ofMillis(100));
        if(records.isEmpty()) {
            System.out.println("Não encontrei registros");
            continue;
        }
Copiar código
Ao rodar novamente, podemos ver o serviço continuamente verificando por mensagens. No entanto, pode ser um pouco excessivo imprimir a mensagem de não encontrar registros repetidamente. Vamos ajustar para imprimir a mensagem somente quando registros forem encontrados, indicando quantos registros forem encontrados com o método records.count(). Além disso, precisamos incluir ! na condiconal if.

    public static void main(String[] args) {
        var consumer = new KafkaConsumer<String, String>()
        consumer.subscribe(Collections.singletonList("ECOMMERCE_NEW_ORDER"));
        while(true) {
        var record = consumer.poll(Duration.ofMillis(100));
        if(!records.isEmpty()) {
            System.out.println("Encontrei " + records.count() + " registros");
            continue;
        }
Copiar código
Portanto, ao encontrar registros, ele imprime quantos foram encontrados. Além disso, podemos mover o trecho de código de iteração (for) para dentro do bloco if, garantindo que a mensagem seja exibida apenas quando registros são encontrados.

    public static void main(String[] args) {
        var consumer = new KafkaConsumer<String, String>()
        consumer.subscribe(Collections.singletonList("ECOMMERCE_NEW_ORDER"));
        while(true) {
        var record = consumer.poll(Duration.ofMillis(100));
        if(records.isEmpty()) {
            System.out.println("Encontrei " + records.count() + " registros");
            for(var record: records) {
            System.out.println("---------------------");
            System.out.println("Processing new order, checking for fraud");
            System.out.println(record.key());
            System.out.println(record.value());
            System.out.println(record.partition());
            System.out.println(record.offset());
            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                // ignoring
                e.printStackTrace();
            }
                System.out.println("Order processed");
                }
            }
        }
    }
Copiar código
Ao rodar uma nova ordem de compra, o serviço detecta a ordem e a processa, fornecendo informações sobre a chave, o valor e o offset da mensagem.

Se alterarmos os valores de produção e rodarmos novamente, enviando novas ordens, podemos ver que o FraudDetectorService continua recebendo e processando as mensagens, conforme esperado. Com isso, tanto o produtor quanto o consumidor estão funcionando!