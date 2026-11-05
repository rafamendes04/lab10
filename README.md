# Laboratório 10: TDD

Cada exercício é um projeto numa pasta (ex1, ex2, ex3), com src/ e tests/. Todas as fases estão no Git, um commit por fase. Cada exercício tem um commit "setup" no começo (pyproject e, no ex3, o carrinho da teoria), que não é fase do ciclo.

Rodei tudo com pytest 9.1.1, pytest-cov 7.1.0 e mutmut 3.8.0. Pra conferir: `cd ex1` e `pytest -q`, `mutmut run`, `mutmut results`.

Obs: quando um teste já passava de primeira, não dava pra fazer um RED só pra ele. Esses testes entraram no commit RED seguinte, e a mensagem do commit diz quais são.

## Exercício 1: contador de palavras

### a) Ordem da lista

1. "" dá {}
2. "teste" dá {"teste": 1}
3. "bom dia" dá dois itens
4. "bom\ndia" dá dois itens
5. três espaços entre bom e dia dão dois itens
6. "guarda-chuva" dá um item
7. "dia a dia" dá dia 2 e a 1
8. "Dia dia DIA" dá {"dia": 3}
9. "fim. Fim!" dá {"fim": 2}
10. ",dia, ;dia;" dá {"dia": 2}
11. ":dia: ?dia?" dá {"dia": 2}
12. "... !" dá {}

Primeira posição, "": é o caso mais simples que existe, sem palavra nenhuma. Só obriga a função a existir e devolver um dicionário, sem lógica nenhuma.

Segunda posição, "teste": é o menor texto com uma palavra, sem maiúscula nem sinal. É o primeiro que faz o resultado depender do texto, então derruba o {} constante.

### b) Desenvolvimento

Feito em ex1/src/contador.py e ex1/tests/test_contador.py, seguindo a ordem acima. O 1 foi feito com um retorno constante, o 2 com Fake It, e o 3 obrigou a usar split. O código final ficou assim:

    def contar_palavras(texto):
        resultado = {}
        for p in texto.lower().split():
            p = p.strip(".,;:!?")
            if p != "":
                resultado[p] = resultado.get(p, 0) + 1
        return resultado

No fim teve um REFACTOR que juntou os 12 testes num parametrize.

### c) git log --oneline

    2e0f606 setup: estrutura do ex1
0e48752 RED: texto vazio devolve dicionario vazio
48904cb GREEN: devolve dicionario vazio
5c5caae RED: uma palavra conta 1
253d7af GREEN: constante para o texto teste (Fake It)
3c3ea2f RED: duas palavras separadas por espaco
f88521a GREEN: separa o texto com split
0b28ae2 RED: palavra repetida soma (e quebra de linha, espacos e hifen que ja passavam)
0f97404 GREEN: soma as ocorrencias
78ce863 RED: maiuscula conta como minuscula
7145d0d GREEN: texto em minusculo
0ab099d RED: ponto e exclamacao nas bordas sao ignorados
e86a50a GREEN: tira sinais das bordas
fa31e34 RED: texto so com sinais devolve vazio (e virgula, ponto e virgula, dois pontos que ja passavam)
3057b02 GREEN: ignora palavra que fica vazia
8d1f649 REFACTOR: testes viram um parametrize

Nenhum GREEN veio sem um RED antes. Todo GREEN tem um RED na linha de cima. Os logs aqui estão do commit mais antigo pro mais novo (git log --oneline --reverse), e filtrados por pasta.

### d) Testes que passaram de primeira

Cinco testes:

- "bom\ndia", três espaços e "guarda-chuva": passaram porque o split() sem argumento já separa por qualquer espaço em branco (inclusive quebra de linha e espaços repetidos), e o hífen não é separador. Entraram no commit RED do "dia a dia".
- ",dia, ;dia;" e ":dia: ?dia?": passaram porque o strip(".,;:!?") já tira qualquer combinação desses sinais das bordas. Entraram no commit RED do "... !".

Eles não guiaram código, mas ficam na suíte. Documentam o contrato e avisam se alguém trocar o split() por split(" ") ou mexer nos sinais do strip.

### e) Cobertura e mutação

Cobertura de ramos (pytest --cov=contador --cov-branch --cov-report=term-missing):

    Name              Stmts   Miss Branch BrPart  Cover   Missing
    -------------------------------------------------------------
    src/contador.py       7      0      4      0   100%

Mutação: o mutmut gerou 15 mutantes, 14 morreram e 1 sobreviveu (contador.x_contar_palavras__mutmut_5).

O vivo troca ".,;:!?" por "XX.,;:!?XX" no strip. É equivalente: o texto já passou por lower() antes, então nunca tem X maiúsculo, e tirar X das bordas não muda nada. Procurei uma entrada que matasse e não existe.

Escore: 14 / (15 - 1 equivalente) = 100%. Sem descontar o equivalente, 14/15 ≈ 93%.

## Exercício 2: fila de atendimento

### a) Lista de testes (16 itens, na ordem de uso)

1. fila nova tem aguardando 0
2. emitir("normal") devolve N1
3. duas normais dão N1 e N2
4. emitir("prioritaria") devolve P1
5. numeração por tipo: normal, prioritaria, normal dão N1, P1, N2
6. tipo inválido lança ValueError
7. aguardando conta as senhas emitidas
8. chamar com fila vazia lança IndexError
9. chamar devolve a senha emitida
10. chamar reduz o aguardando
11. normais saem na ordem de chegada
12. prioritária emitida depois da normal é chamada primeiro
13. prioritárias saem na ordem de chegada
14. N1 e depois P1, P2, P3: sai P1, P2, N1
15. duas normais e quatro prioritárias: sai P1, P2, N1, P3, P4, N2
16. só prioritárias (P1, P2, P3): saem as três, sem erro

### b) Desenvolvimento

Feito em ex2/src/fila.py e ex2/tests/test_fila.py. Os testes 5, 10, 11 e 13 passaram de primeira e entraram no commit RED seguinte.

    796f666 setup: estrutura do ex2
eb79f84 RED: fila nova nao tem ninguem aguardando
db247f3 GREEN: aguardando devolve 0
908a2d7 RED: emitir normal devolve N1
5548f1b GREEN: emitir devolve N1 (Fake It)
b96f768 RED: segunda normal vira N2
bf53507 GREEN: contador de senhas normais
12fae3c RED: emitir prioritaria devolve P1
0ed451d GREEN: contador proprio das prioritarias
84b2838 RED: tipo invalido lanca ValueError (e numeracao por tipo que ja passava)
2cf4391 GREEN: valida o tipo
7aff615 RED: aguardando conta as senhas emitidas
2e83318 GREEN: guarda as senhas em uma lista
eb8c406 RED: chamar com fila vazia lanca IndexError
15ce7b5 GREEN: chamar lanca IndexError (Fake It)
7efc89c RED: chamar devolve a senha emitida
2b1441a GREEN: chamar tira a primeira senha da lista
964d3ca RED: prioritaria passa na frente (e chamar reduz aguardando, normais em ordem que ja passavam)
f87fed8 GREEN: duas listas, prioritarias primeiro
3d8fd2b RED: depois de 2 prioritarias seguidas chama normal (e prioritarias em ordem que ja passava)
5f49611 GREEN: conta as prioritarias seguidas
4c0ab67 RED: chamar normal zera a contagem
edff61a GREEN: zera as seguidas ao chamar normal
7813f6b RED: limite de 2 nao vale sem normal esperando
c7e7630 GREEN: so passa pra normal se tiver normal esperando

### c) Contar e zerar

O teste 14 (test_depois_de_duas_prioritarias_vem_normal) obrigou a contar as prioritárias seguidas. Sem o contador, a fila sempre chamava P1, P2, P3 antes da normal.

O teste 15 (test_normal_zera_a_contagem) obrigou a zerar. Sem o zero, depois de chamar N1 a contagem continuava em 2, e a fila chamava N2 antes de P3.

### d) Limite de 2 sem normal esperando

O teste 16 (test_limite_nao_vale_sem_normal_esperando). Com só prioritárias na fila, a terceira chamada tem que ser P3. Antes da correção a fila tentava chamar uma normal que não existia e dava IndexError.

### e) Mutmut

    mutmut run: 48/48 mutantes mortos, 0 vivos

Escore de 100%, então nenhum comportamento da especificação ficou sem teste. Um detalhe: o aguardando é @property e o mutmut 3.8.0 não muta property, então ele fica fora desse número. Os testes 1, 7 e 10 conferem o aguardando.

## Exercício 3: regras novas no carrinho

Ponto de partida: o carrinho da teoria (ex3/src/carrinho.py) com os 7 testes dela, no commit setup.

### a) Testes que contradizem as regras

Dois testes:

- test_cupom_dez: adiciona 5000, aplica DEZ e espera 4500. Pela regra nova, 5000 está abaixo do mínimo de 10000 e não tem desconto.
- test_item_depois_do_cupom: aplica DEZ, adiciona 1000 e espera 900. Mesma coisa, 1000 não chega no mínimo.

Antes de mudar o código, atualizei os dois testes pra regra nova, no commit RED. O primeiro passou a esperar 5000 (e falhou, que é o RED). O segundo passou a adicionar 10000 e esperar 9000. Deixar o teste velho ia fazer o GREEN falhar por causa de uma regra que não existe mais.

### b) Implementação

Uma regra por vez, um commit por fase:

    1f23fb7 setup: carrinho da teoria com os 7 testes
2eee093 RED: testes antigos atualizados: DEZ abaixo de 10000 nao desconta (e DEZ no minimo que ja passava)
6e4fe56 GREEN: DEZ so desconta a partir de 10000
d2f3ad5 RED: cupom VINTE em 30000 da 20% (e DEZ em 9999 que ja passava)
2b0afd9 GREEN: cupom VINTE em CUPONS
6ba2f3e RED: VINTE abaixo de 30000 nao desconta
8faae48 GREEN: minimo de cada cupom
47f741e REFACTOR: porcentagem e minimo juntos em CUPONS
4aa8dd3 RED: quantidade zero rejeitada (e segundo cupom substitui o primeiro, que ja passava)
95f5561 GREEN: quantidade tem que ser pelo menos 1
050682e RED: quantidade fracionada rejeitada (e quantidade 1 e negativa que ja passavam)
da656fc GREEN: quantidade tem que ser inteira

Os testes que já passavam foram: DEZ em 10000 e item depois do cupom com 10000 (primeiro RED), DEZ em 9999, segundo cupom substitui o primeiro (dois testes), quantidade 1 e quantidade -1. Todos entraram no commit RED seguinte.

### c) Refactor

O REFACTOR guardou a porcentagem e o mínimo juntos: CUPONS = {"DEZ": (10, 10000), "VINTE": (20, 30000)}, e o MINIMOS saiu.

O que mostra que nada mudou: a suíte estava com 11 testes passando antes (11 passed) e continuou com os mesmos 11 passando depois. O commit só mexe em src/carrinho.py, nenhum teste foi alterado.

### d) Valores de quantidade testados

- 2: já existia da teoria, caso normal.
- 1: menor valor válido, é a própria fronteira.
- 0: logo abaixo da fronteira, tem que dar ValueError.
- -1: negativo, também ValueError.
- 1.5: não é inteiro, ValueError.

Escolhi esses por valor-limite (aula 6): o limite é 1, então testei o 1, o 0 e um valor bem abaixo. O 1.5 é pra regra de ser inteira. Considerei "inteira" como tipo int, então 2.0 também seria rejeitado, mas não coloquei teste pra ele.
