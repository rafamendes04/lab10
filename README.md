## Exercício 1: contador de palavras

a) Ordem dos testes:

1. "" dá {}
2. "teste" dá {"teste": 1}
3. "bom dia"
4. "bom\ndia"
5. três espaços entre bom e dia
6. "guarda-chuva"
7. "dia a dia"
8. "Dia dia DIA"
9. "fim. Fim!"
10. ",dia, ;dia;"
11. ":dia: ?dia?"
12. "... !"

O "" vem primeiro por ser o mais simples: sem palavra nenhuma, só obriga a função a existir. O "teste" vem depois porque é o menor texto com uma palavra e já derruba o retorno fixo {}.

b) Feito em ex1/src/contador.py, com os testes em ex1/tests/test_contador.py.

c) git log --oneline, do mais antigo pro mais novo:

```
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
```

Nenhum GREEN veio sem RED antes.

d) "bom\ndia", três espaços e "guarda-chuva" passaram de primeira porque o split() já separa por qualquer espaço em branco e o hífen não é separador. ",dia, ;dia;" e ":dia: ?dia?" também passaram, porque o strip já tira esses sinais das bordas. Todos ficam na suíte, porque protegem essas regras caso alguém mexa no split ou no strip.

e) Cobertura de ramos: 100%. O mutmut gerou 15 mutantes, 14 morreram e 1 sobreviveu. O vivo troca ".,;:!?" por "XX.,;:!?XX" no strip. Como o texto já está em minúsculo, nunca tem X maiúsculo, então a troca não muda o resultado e o mutante é equivalente. Escore: 14/14 = 100%.

## Exercício 2: fila de atendimento

a) Lista de testes:

1. fila nova tem aguardando 0
2. emitir normal dá N1
3. duas normais dão N1 e N2
4. emitir prioritária dá P1
5. numeração separada por tipo (N1, P1, N2)
6. tipo inválido lança ValueError
7. aguardando conta as senhas emitidas
8. chamar com fila vazia lança IndexError
9. chamar devolve a senha emitida
10. chamar diminui o aguardando
11. normais saem na ordem de chegada
12. prioritária passa na frente da normal
13. prioritárias saem na ordem de chegada
14. N1, P1, P2, P3: sai P1, P2, N1
15. duas normais e quatro prioritárias: sai P1, P2, N1, P3, P4, N2
16. só prioritárias (P1, P2, P3): saem as três

b) Feito em ex2/src/fila.py, com os testes em ex2/tests/test_fila.py.

c) O teste 14 obrigou a contar as prioritárias seguidas. O teste 15 obrigou a zerar a contagem: sem isso, depois do N1 a fila chamava o N2 antes do P3.

d) O teste 16. Com só prioritárias na fila, a terceira chamada tem que ser P3. Antes da correção a fila tentava chamar uma normal que não existia e dava IndexError.

e) O mutmut gerou 48 mutantes e os 48 morreram. Nenhum vivo, então nada da especificação ficou sem teste.

## Exercício 3: carrinho com regras novas

a) Dois testes contradizem as regras:

- test_cupom_dez espera 4500 com subtotal 5000, mas 5000 está abaixo do mínimo e agora não tem desconto.
- test_item_depois_do_cupom espera 900 com um item de 1000, pelo mesmo motivo.

Antes de mexer no código, atualizei os dois no commit RED. Se ficassem como estavam, o GREEN falharia por causa de uma regra que não existe mais.

b) Feito em ex3/src/carrinho.py, com os testes em ex3/tests/test_carrinho.py, uma regra por vez: mínimo do DEZ, cupom VINTE, segundo cupom e quantidade.

c) No Refactor, a porcentagem e o mínimo foram juntos pro CUPONS. Os mesmos 11 testes passavam antes e continuaram passando depois, sem nenhum teste alterado, e é isso que mostra que nada mudou.

d) Testei quantidade 2 (já existia), 1, 0, -1 e 1.5. O 1 e o 0 ficam na fronteira do mínimo, o -1 é um negativo e o 1.5 confere a regra de ser inteira.