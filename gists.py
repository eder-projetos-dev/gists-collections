import requests


class Gists():

  def __init__(self, usuario):
    self._usuario = usuario

  def requisicao_api(self):
    resposta = requests.get(
      f'https://api.github.com/users/{self._usuario}/gists')
    if resposta.status_code == 200:
      return resposta.json()
    else:
      return resposta.status_code

  def get_gists(self):  # faltando forks
    lista = []
    dados_api = self.requisicao_api()
    if type(dados_api) is not int:
      for i in range(len(dados_api)):
        texto = dados_api[i]['description'].split('-')
        tag = texto[0].strip()
        description = texto[1].strip()
        autor = dados_api[i]['owner']['login']
        url = dados_api[i]['html_url']
        lista.append([tag, description, autor, url])
      return lista
    else:
      return dados_api

  """ 
  Recebe: uma lista com títulos de gists
  Retorna: lista de tags extraídas dos títulos do gists """

  def get_tags(self, lista):
    tags = []
    for i in lista:
      tags.append(i[0])
    return tags


gists = Gists('eder-projetos-dev')

gists_list = gists.get_gists()

tags = gists.get_tags(gists_list)
""" Obtendo a quantidade e o nome das tags
Recebe: lista de tags 
Retorna: dicionário com a contagem e o nome das tags """


def count_tags(tags):
  tags_set = set(tags)  # obtendo tags únicas
  tags_dic = {}  # key=contagem e value=tag
  for tag in tags_set:
    tags_dic.update({tag: tags.count(tag)})
  return tags_dic


tags_dic = count_tags(tags)
""" Menu com as tags em ordem de contagem
Recebe: tags_dic 
Retorna: menu_tags """


def menu_tags(tags_dic):
  menu_tags = []  # menu apresenta tags em ordem de contagem
  for k, v in sorted(tags_dic.items(), reverse=True):
    menu_tags.append(k)
  return menu_tags


""" Filtrar gists 
Recebe: Lista de gists e aplica filtro por tag 
Retorna: Lista com os gists encontrados """


def filtro_tag(gists_list, tag):
  resultado = []
  for gist in gists_list:
    if gist[0] == tag:
      resultado.append(gist)
  return resultado