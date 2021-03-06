# Query Dictionary

## Instalação

````bash
> pip install qdict
````


## Sobre

Executa uma consulta em um Iterável (List[dict], dict, List[Tuple[key, value]]) e aplica o filtro. 

O filtro é aplicado horizontalmente acompanhando a iteração das chaves da query, ou seja, 
quando a query tem uma chave e essa chave não é um operador e seu valor é um dicionário, é isolado
este dicionário de dentro da query e do objeto a ser verificado.

Atenção: Caso o objeto não possua a chave especificada na query, o objeto não será retornado nos resultados finais.


## Operadores

Todos os operadores respeitam o nível dos objetos.


*$or*: lista de queries. 
````python
from qdict import find

obj = [{"a": 1, "b": {"c": "Positive"}}, {"a": 1, "b": {"c": "Negative"}},
           {"a": 1, "b": {"c": "Undefined"}}, {"a": 1}]
result = find(obj, {
    "$or": [{"b": {"c": "Positive"}},
            {"$not": {"$has": "b"}}]
})
r = list(result)
print(r)  # [{'a': 1, 'b': {'c': 'Positive'}}, {'a': 1}]
````

*$not*: negativa a expressão
```python
{"a": {"$not": 1}}
```

*$custom*: Define um método dinamicamente. (func, keyname1, keyname2, ..., keynameN). Cada keyname será um parâmetro com 
o valor da chave ou None

```python
from qdict import find
obj = [
    {"a": 1, "b": True, "c": {"a": 1}, "d": {"a": 1}},
    {"a": 3, "b": False, "c": {"a": 6}}
]

def pair(num):
    return num % 2 == 0

query = {
    "c": {"$custom": (pair, "a")}
}
print(list(find(obj, query)))  # [{"a": 3, "b": False, "c": {"a": 6}}]
```

*$has*: verifica se o objeto contém a chave

*$contains*: Se a lista (objeto) contém o item (query)

*$in*: Se o valor (objeto) está contido na lista (query)

## Exemplos

```python
from qdict import find

# simple search
obj = [{"a": 1, "b": False}, {"a": 2, "b": True}, {"b": True}]
result = find(obj, {"b": True})
print(list(result))  # [{'a': 2, 'b': True}, {'a': 3, 'b': True}]
result = find(obj, {"$has": "a"})
print(list(result))  # [{'a': 1, 'b': False}, {'a': 2, 'b': True}]
result = find(obj, {"$not": {"$has": "a"}})
print(list(result))  # [{'b': True}]

# search with subkeys
obj = [{"a": 1, "b": {"c": "Positive"}}, {"a": 1, "b": {"c": "Negative"}},
       {"a": 1, "b": {}}]
result = find(obj, {"b": {"c": "Negative"}})
print(list(result))  # [{'a': 1, 'b': {'c': 'Negative'}}]

# $or
obj = [{"a": 1, "b": {"c": "Positive"}}, {"a": 1, "b": {"c": "Negative"}},
       {"a": 1, "b": {"c": "Undefined"}}, {"a": 1}]
result = find(obj, {
    "$or": [{"b": {"c": "Positive"}},
            {"$not": {"$has": "b"}}]
})
print(list(result))  # [{'a': 1, 'b': {'c': 'Positive'}}, {'a': 1}]
```
## Releases

* 1.3.0 - Fix packages
* 1.1.0 - Fix custom char operator
         - added greater than, greater than equal, less than and less than equal
* 1.0.0 - Initial Release
