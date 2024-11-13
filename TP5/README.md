## Data: 9-10-2024
## Resumo:
Algoritmos e modelação de problemas com listas e listas de listas.

## Trabalho de casa:

Suponha que está a desenvolver uma aplicacão para gestão de um conjunto de salas de cinema de um centro comercial. 
Nesse centro comercial existem algumas salas de cinema (que poderão estar a exibir filmes ou não), cada sala tem uma determinada 
lotação, uma lista com a referência dos bilhetes vendidos (lugares ocupados; cada lugar é identificado por um número inteiro), e cada sala tem um filme associado.

Considera a seguinte sugestão para o modelo dos cinemas:
```
Cinema = [Sala]
Sala = [nlugares, Vendidos, filme]
nlugares = Int
filme = String 
Vendidos = [Int]
```
  
Que poderá ser usado num programa da seguinte forma:
```
sala1 = (150, [], "Twilight")
sala2 = (200, [], "Hannibal")
cinema1 = []
...
cinema1 = inserirSala(cinema1,sala1)
cinema1 = inserirSala(cinema1,sala2)
...
listar(cinema1)
...

if(disponivel(cinema1, "Twilight", 17 )):
  cinema1 = vendebilhete(cinema1, "Twilight", 17 )
...
listardisponibilidades(cinema1)
...
```

Especifique as funções utilizadas no exemplo:

1. `listar( cinema )` - que lista no monitor todos os filmes que estão em exibição nas salas do cinema passado como argumento;
2. `disponivel( cinema, filme, lugar )` - que dá como resultado **False** se o lugar lugar já estiver ocupado na sala onde o filme está a ser exibido e dará como resultado **True** se o inverso acontecer;
3. `vendebilhete( cinema, filme, lugar )` - que dá como resultado um novo cinema resultante de acrescentar o lugar à lista dos lugares ocupados, na sala onde está a ser exibido o filme;
4. `listardisponibilidades( cinema )` - que, para um dado cinema, lista no monitor para cada sala, o filme que está a ser exibido e o total de lugares disponíveis nessa sala (número de lugares na sala menos o número de lugares ocupados);
5. `inserirSala( cinema, sala )` - que acrescenta uma sala nova a um cinema (devendo verificar se a sala já existe);
6. Acrescente todas as outras funcionalidades que achar necessárias;
7. À semelhança do exercício 3, construa uma aplicação com um menu de interface para as operações.
