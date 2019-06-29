## SubsetSum com algoritmo de força bruta

Esse repositório apresenta um algoritmo de força bruta desenvolvido em Python a fim de solucionar o problema de decisão para o SubsetSum. O algoritmo desenvolvido apresenta a complexidade presente neste problema NP-Completo.

### O problema

Dados números p1, p2, …, pn e um subconjunto X de {1,2,…,n}, denotaremos por p(X) a soma ∑i∈X pi. Considere o seguinte problema:

Problema subset-sum: Dados números naturais p1, p2,…, pn e c, decidir se existe um subconjunto X de {1,2,…,n} tal que p(X) = c.

Diremos que os números p1,p2,…,pn são os pesos e c  é a capacidade do problema.  (A ordem em que os pesos são dados é, obviamente, irrelevante.)  O problema só admite duas soluções, "sim" e "não", que podemos representar por 1 e 0 respectivamente.

Por exemplo:
A instância do problema definida por p = (30, 40, 10, 15, 10, 60, 54)  e  c = 55  tem solução "sim" pois o conjunto {2,4} tem a propriedade desejada. 

A explicação acima foi retirada de https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/mochila-subsetsum.html.