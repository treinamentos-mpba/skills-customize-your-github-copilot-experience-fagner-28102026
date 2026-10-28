# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Construa o clássico jogo da Forca em Python, praticando manipulação de strings, loops, condicionais e seleção aleatória, onde os jogadores adivinham letras para revelar uma palavra oculta antes de esgotar as tentativas.

## 📝 Tarefas

### 🛠️ Selecionar a Palavra Secreta e Inicializar o Jogo

#### Descrição
Selecione aleatoriamente uma palavra de uma lista predefinida e inicialize as variáveis que controlam o estado do jogo (letras adivinhadas, tentativas incorretas e limite de tentativas).

#### Requisitos
O programa concluído deve:

- Selecionar palavras aleatoriamente de uma lista predefinida usando o módulo `random`
- Inicializar uma estrutura para armazenar as letras já adivinhadas
- Definir o número máximo de tentativas incorretas permitidas

### 🛠️ Implementar o Loop Principal do Jogo

#### Descrição
Crie o loop principal que exibe o progresso atual da palavra, aceita palpites de letras do usuário e atualiza o estado do jogo a cada rodada.

#### Requisitos
O programa concluído deve:

- Aceitar palpites de letras e mostrar o progresso atual (formato `_ _ _`)
- Rastrear e exibir as tentativas incorretas restantes
- Verificar se a letra informada está na palavra secreta e atualizar o estado do jogo
- Exemplo de saída:
  ```
  Palavra: p _ t h o n
  Tentativas restantes: 4
  Digite uma letra: y
  ```

### 🛠️ Encerrar o Jogo com Vitória ou Derrota

#### Descrição
Implemente as condições de término do jogo, encerrando quando o jogador adivinhar a palavra completa ou esgotar as tentativas, e exibindo a mensagem apropriada.

#### Requisitos
O programa concluído deve:

- Encerrar quando a palavra for adivinhada ou as tentativas esgotarem
- Exibir uma mensagem de vitória quando o jogador adivinhar a palavra
- Exibir uma mensagem de derrota, revelando a palavra secreta, quando as tentativas esgotarem
