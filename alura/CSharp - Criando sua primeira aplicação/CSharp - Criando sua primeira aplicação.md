# **C# - Criando sua Primeira Aplicação: Screen Sound**

## Sumário

1. [Visão Geral](#visão-geral)
2. [Estrutura Básica do Projeto](#estrutura-básica-do-projeto)
3. [Primeiro Programa: Hello World](#primeiro-programa-hello-world)
4. [Tipos de Variáveis em C#](#tipos-de-variáveis-em-c)
   1. [Variáveis Texto (string)](#variáveis-texto-string)
   2. [Variáveis Inteiras (int)](#variáveis-inteiras-int)
5. [Depuração Rápida e Layout do Console](#depuração-rápida-e-layout-do-console)
6. [Isolando Código em Funções](#isolando-código-em-funções)
7. [Menu Interativo com Switch/Case](#menu-interativo-com-switchcase)
8. [Trabalhando com Listas](#trabalhando-com-listas)
   1. [Estrutura de Repetição `for`](#estrutura-de-repetição-for)
   2. [Estrutura de Repetição `foreach`](#estrutura-de-repetição-foreach)
9. [Refatorando Cabeçalhos Dinâmicos](#refatorando-cabeçalhos-dinâmicos)
10. [Dicionário para Avaliações](#dicionário-para-avaliações)
    1. [Registrando Bandas](#registrando-bandas)
    2. [Mostrando Bandas Registradas](#mostrando-bandas-registradas)
    3. [Avaliando uma Banda](#avaliando-uma-banda)
    4. [Exibindo Média de Avaliações](#exibindo-média-de-avaliações)
11. [Boas Práticas e Tratamento de Erros](#boas-práticas-e-tratamento-de-erros)
12. [Exemplo Completo do `Program.cs`](#exemplo-completo-do-programcs)

---

## Visão Geral

Este tutorial guia o desenvolvedor pela criação de uma aplicação de console em C# chamada **Screen Sound**, focada no back-end de um sistema de streaming musical. Serão abordados desde o clássico "Hello World" até conceitos avançados como coleções genéricas, dicionários e funções de extensão para padronização de layout.

## Estrutura Básica do Projeto

Antes de começar a escrever código, crie um novo projeto de **Console App** no Visual Studio ou via CLI:

```bash
# Pelo .NET CLI
dotnet new console -n ScreenSound
cd ScreenSound
```

No Visual Studio, selecione **"Aplicativo de Console"** (.NET 7 ou superior) e nomeie como `ScreenSound`.

## Primeiro Programa: Hello World

O arquivo gerado por padrão é `Program.cs`. Ele contém:

```csharp
using System;

Console.WriteLine("Hello, World!");
```

Execute com `Ctrl+F5` ou `dotnet run`. A saída no terminal será:

```
Hello, World!
```

Este é o ponto de partida para qualquer aplicação C# de console.

## Tipos de Variáveis em C#

C# é **fortemente tipada**, ou seja, cada variável deve ser declarada com um tipo que define o formato de dados que ela armazenará.

### Variáveis Texto (string)

```csharp
string mensagem = "Bem-vindo ao Screen Sound";
Console.WriteLine(mensagem);
```

- Use **aspas duplas** para `string`.
- É possível usar verbatim string (`@"texto"`) para incluir quebras de linha ou barras sem escape.

### Variáveis Inteiras (int)

```csharp
int ano = 2025;
int soma = 5 + 3;
Console.WriteLine($"Ano atual: {ano}, soma: {soma}");
```

- Para converter `string` em `int`, prefira `int.TryParse` para evitar exceções:
  ```csharp
  if (!int.TryParse(Console.ReadLine(), out int opcao)) {
      Console.WriteLine("Opção inválida.");
  }
  ```

## Depuração Rápida e Layout do Console

- **Atalhos úteis** no Visual Studio:  
  • `Shift+Esc`: fecha painéis laterais.  
  • `Ctrl+F5`: iniciar sem depurar.
- Use `Console.Clear()` para limpar a tela entre operações.
- Combine `Console.Write` e `Console.WriteLine` para controlar quebras de linha.

## Isolando Código em Funções

Organize seu código em métodos **void** que não retornam valor:

```csharp
void ExibirMensagem(string texto) {
    Console.WriteLine(texto);
}

// Chamada:
ExibirMensagem("Olá, mundo!");
```

A nomenclatura em C# segue:

- **CamelCase**: variáveis (e.g., `mensagemDeBoasVindas`)
- **PascalCase**: métodos, classes e propriedades (e.g., `ExibirMensagem`)

## Menu Interativo com Switch/Case

Utilize `switch` para tratar múltiplas opções de forma clara:

```csharp
switch (opcao) {
    case 1:
        RegistrarBanda();
        break;
    case 2:
        MostrarBandasRegistradas();
        break;
    case -1:
        Console.WriteLine("Tchau tchau :)");
        break;
    default:
        Console.WriteLine("Opção inválida");
        break;
}
```

## Trabalhando com Listas

Coleções genéricas permitem armazenar múltiplos itens:

```csharp
using System.Collections.Generic;

List<string> listaDeBandas = new List<string> { "U2", "The Beatles", "Calypso" };
```

### Estrutura de Repetição `for`

```csharp
for (int i = 0; i < listaDeBandas.Count; i++) {
    Console.WriteLine($"Banda {i+1}: {listaDeBandas[i]}");
}
```

### Estrutura de Repetição `foreach`

```csharp
foreach (var banda in listaDeBandas) {
    Console.WriteLine($"Banda: {banda}");
}
```

## Refatorando Cabeçalhos Dinâmicos

Para não repetir linhas de asteriscos manualmente, crie um método:

```csharp
void ExibirTitulo(string titulo) {
    int len = titulo.Length;
    string asteriscos = string.Empty.PadLeft(len, '*');
    Console.WriteLine(asteriscos);
    Console.WriteLine(titulo);
    Console.WriteLine(asteriscos + "\n");
}
```

Uso:

```csharp
ExibirTitulo("Registro de Bandas");
```

## Dicionário para Avaliações

Permite mapear cada banda a uma lista de notas:

```csharp
using System.Collections.Generic;

Dictionary<string, List<int>> bandasRegistradas = new Dictionary<string, List<int>>();
```

### Registrando Bandas

```csharp
void RegistrarBanda() {
    Console.Clear();
    ExibirTitulo("Registro de Bandas");
    Console.Write("Digite o nome da banda: ");
    string nome = Console.ReadLine()!;
    bandasRegistradas.Add(nome, new List<int>());
    Console.WriteLine($"Banda '{nome}' registrada com sucesso!");
    Thread.Sleep(2000);
    ExibirMenu();
}
```

### Mostrando Bandas Registradas

```csharp
void MostrarBandasRegistradas() {
    Console.Clear();
    ExibirTitulo("Bandas Registradas");
    foreach (var nome in bandasRegistradas.Keys) {
        Console.WriteLine($"- {nome}");
    }
    Console.WriteLine("\nPressione qualquer tecla para voltar...");
    Console.ReadKey();
    ExibirMenu();
}
```

### Avaliando uma Banda

```csharp
void AvaliarBanda() {
    Console.Clear();
    ExibirTitulo("Avaliar Banda");
    Console.Write("Nome da banda: ");
    string nome = Console.ReadLine()!;
    if (!bandasRegistradas.ContainsKey(nome)) {
        Console.WriteLine($"\nBanda '{nome}' não encontrada.");
    } else {
        Console.Write($"Qual nota (0–10) para '{nome}'? ");
        if (int.TryParse(Console.ReadLine(), out int nota)) {
            bandasRegistradas[nome].Add(nota);
            Console.WriteLine($"\nNota {nota} registrada para '{nome}'.");
        } else {
            Console.WriteLine("\nValor de nota inválido.");
        }
    }
    Console.WriteLine("\nPressione qualquer tecla para voltar...");
    Console.ReadKey();
    ExibirMenu();
}
```

### Exibindo Média de Avaliações

```csharp
void ExibirMedia() {
    Console.Clear();
    ExibirTitulo("Média de Avaliações");
    Console.Write("Nome da banda: ");
    string nome = Console.ReadLine()!;
    if (bandasRegistradas.TryGetValue(nome, out var notas)) {
        if (notas.Count > 0) {
            double media = notas.Average();
            Console.WriteLine($"\nA média da banda '{nome}' é {media:F2}.");
        } else {
            Console.WriteLine("\nAinda não há notas registradas para esta banda.");
        }
    } else {
        Console.WriteLine($"\nBanda '{nome}' não encontrada.");
    }
    Console.WriteLine("\nPressione qualquer tecla para voltar...");
    Console.ReadKey();
    ExibirMenu();
}
```

## Boas Práticas e Tratamento de Erros

- Utilize `int.TryParse` e `Dictionary.TryGetValue` para evitar exceções.
- Separe responsabilidades: cada método deve fazer apenas uma ação.
- Considere `using System.Linq;` para métodos como `Average`, `Sum`, etc.
- Indente corretamente e comente trechos complexos.

## Exemplo Completo do `Program.cs`

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;

class Program {
    static Dictionary<string, List<int>> bandasRegistradas = new();

    static void Main() {
        ExibirMenu();
    }

    static void ExibirMenu() {
        Console.Clear();
        ExibirTitulo("Screen Sound - Menu Principal");
        Console.WriteLine("1 - Registrar Banda");
        Console.WriteLine("2 - Mostrar Bandas");
        Console.WriteLine("3 - Avaliar Banda");
        Console.WriteLine("4 - Exibir Média");
        Console.WriteLine("-1 - Sair\n");
        Console.Write("Opção: ");

        if (int.TryParse(Console.ReadLine(), out int opcao)) {
            switch (opcao) {
                case 1: RegistrarBanda(); break;
                case 2: MostrarBandasRegistradas(); break;
                case 3: AvaliarBanda(); break;
                case 4: ExibirMedia(); break;
                case -1: Console.WriteLine("Tchau tchau :)"); break;
                default: Console.WriteLine("Opção inválida."); Thread.Sleep(1500); ExibirMenu(); break;
            }
        } else {
            Console.WriteLine("Entrada inválida.");
            Thread.Sleep(1500);
            ExibirMenu();
        }
    }

    // ... (insira aqui todos os métodos mostrados acima)
}
```
