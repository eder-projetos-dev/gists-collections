# Minha Coleção de Gists

[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Replit](https://img.shields.io/badge/Replit-DD1200?style=for-the-badge&logo=Replit&logoColor=white)](https://replit.com/@eder-projetos-d/gists-collections)
[![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)](https://www.figma.com/file/9qsljo5v2m6U6sqXhsfZu9/gists-collections-prototipo?node-id=0%3A1&t=FRPrbUxBgSiN9xZj-1)

Veja funcionando no [replit.com](https://replit.com/@eder-projetos-d/gists-collections)

Status: **Projeto em desenvolvimento**

## Tópicos 

:small_blue_diamond: [Descrição do projeto](#descrição-do-projeto)<br>
:small_blue_diamond: [Funcionalidades](#funcionalidades)<br>
:small_blue_diamond: [Acesso ao projeto](#acesso-ao-projeto)<br>
:small_blue_diamond: [Pré-requisitos](#pré-requisitos)<br>
:small_blue_diamond: [Abrir e rodar o projeto](#abrir-e-rodar-o-projeto)<br>
:small_blue_diamond: [Tecnologias utilizadas](#tecnologias-utilizadas)<br>

## Descrição do Projeto

Minha coleção de gists obtida pela API do GITHUB. <br>

![demonstracao](https://user-images.githubusercontent.com/117411812/221439186-7c12acd4-6ba9-42ef-a986-030ef8918efe.jpg)

## Funcionalidades

- `RF01`: Listar todos os gists de um usuário utilizando a API do GITHUB.
- `RF02`: O sistema deverá criar tags extraídas do campo description do gist.
- `RF03`: O sistema deverá permitir filtrar gists por tags selecionadas pelo usuário.
- `RF04`: O sistema deverá permitir que o usuário marque um gist como favorito.
- `RF05`: As tags com mais gists deverão aparecer primeiro.

## Acesso ao projeto

Você pode acessar o [código fonte](https://github.com/eder-projetos-dev/gists-collections/blob/master/main.py) ou [baixá-lo](https://github.com/eder-projetos-dev/gists-collections/archive/refs/heads/master.zip).

## Pré-requisitos

Baixe e instale o Python 3.10 no link abaixo: <br>
[https://www.python.org/downloads/](https://www.python.org/downloads/)<br>

Caso precise, instale o gerenciador de pacotes pip:<br>
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

Criando ambiente virtual (venv) no Windows
```bash
md projeto
cd projeto
python -m venv my_env
```

Ativando o ambiente virtual
```bash
cd my_env\Scripts
activate
```

Instalar as dependências utilizando o requirements
```bash
pip install -r requirements.txt
```


Mais informações:<br>

[Tutorial para ambientes virtuais (venv) no Linux e no Windows](https://gist.github.com/eder-projetos-dev/9ef6a61e1418b95cb4333f9133b38e69)<br> 

[Consumindo a API do Github em Python | Alura](https://www.alura.com.br/artigos/consumindo-a-api-do-github-em-python)<br>

[Documentação da API do GITHUB](https://docs.github.com/pt/rest?apiVersion=2022-11-28)<br>



## Rodar o projeto

flask --app app run --host=0.0.0.0


## Tecnologias utilizadas

- ``Python 3.10`` :snake:
- ``API do Github``

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/%C3%A9der-lu%C3%ADs-britto-garcia-803778207/
