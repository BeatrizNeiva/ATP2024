## Data: 30-10-2024
## Resumo:
Consolidação e aferição de tudo o que foi feito até ao momento. 
## Trabalho de casa:
A Rede Social

Considere que a informação sobre uma rede social está armazenada numa lista de dicionários.

Cada dicionário, correspondente a um _post_ e tem chaves `id`, `conteudo`, `autor`, `dataCriacao` e `comentarios`.
Por sua vez, `comentarios` é uma lista de dicionários com chaves `comentario` e `autor`.

Considere o seguinte exemplo:

``` 
    MyFaceBook = [{
        'id': 'p1', 
        'conteudo': 'A tarefa de avaliação é talvez a mais ingrata das tarefas que um professor
    tem de realizar...', 
        'autor': 'jcr', 
        'dataCriacao': '2023-07-20', 
        'comentarios': [
            {
                'comentario': 'Completamente de acordo...',
                'autor': 'prh'
            },
            {
                'comentario': 'Mas há quem goste...',
                'autor': 'jj'
            }
        ]},
        {
            'id': 'p2',
            ...
        },
        ...
        ]
```
Defina varias funções para esta rede
