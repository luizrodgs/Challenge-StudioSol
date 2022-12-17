# Studio Sol - Back-End Challenge

### Desafio Proposto:
- Desenvolver uma API que receba um JSON contendo uma senha e regras para sua validação (Tamanho mínimo, qtd de caracteres especiais, qtd de números, etc).
- Linguagem escolhida: Python
- Framework escolhido: DjangoREST

<br>

### Readme:
##### - 1: **Executando com Docker**
 - 1.1) Após o download do projeto, execute o comando "docker up ." via terminal;
 - 1.2) Com o app online, execute o Postman e configure a requisição conforme informado na etapa 3.
  
##### - 2: **Executando manualmente**
 - 2.1) Após o download do projeto, crie e ative um ambiente virtual;
 - 2.2) Execute o comando "pip install -r requirements.txt" via terminal para instalar as dependências do projeto;
 - 2.3) Execute o comando "python manage.py runserver" via terminal para subir o servidor;
 - 2.4) Com o app online, execute o Postman e configure a requisição conforme informado na etapa 3.

##### - 3: **Fazendo a requisição**
 - 3.1) Com o Postman aberto, selecione o método "POST" e preencha o campo URL com o endereço do método verify (Default: http://127.0.0.1:8000/verify/);
 - 3.2) No campo Body, configura como "RAW" e "JSON";
 - 3.3) Digite o JSON a ser enviado contendo a senha para validação e as regras desejadas.

##### - 4 **Regras para a requisição**
 - 4.1) É permitido utilizar qualquer combinação desejada de regras.
 - 4.2) No campo "noRepeated", considera-se: 0 para PODE REPETIR / 1 para NÃO PODE REPETIR.
 - 4.3) Nos demais campos, considera-se sempre o valor como o mínimo exigido daquela categoria.
  
<br>

  Segue código base:
  
```
{
"password": "aCorint@hians12!",
"rules": [
{"rule": "minSize","value": 8},
{"rule": "minSpecialChars","value": 1},
{"rule": "noRepeated","value": 1},
{"rule": "minDigit","value": 1},
{"rule": "minUpperCase","value": 1},
{"rule": "minLowerCase","value": 1}
]
}
```

A requisição deve ficar similar a foto abaixo:

![request](https://user-images.githubusercontent.com/101483219/208268040-b7fff1e3-f19e-40dc-b998-bf2b31848aca.png)

#### Requirements
- Django==4.1.4
- djangorestframework==3.14.0
- dataclasses-json==0.5.7
