import requests
import time
import json
import os


 
class TelegramBot:
   def __init__(self):
       token = '1685042318:AAEv3WC7C0YG6P3PhtS0iN4wTzB6EUeLweo'
       self.url_base = f'https://api.telegram.org/bot{token}/'
 
   def Iniciar(self):
       update_id = None
       while True:
           try:
             atualizacao = self.obter_novas_mensagens(update_id)
             dados = atualizacao["result"]
           
             if dados:
                for dado in dados:
                  for dado in dados:
                      update_id = dado['update_id']
                      mensagem = str(dado["message"]["text"])
                      chat_id = dado["message"]["chat"]["id"] 
                      if mensagem == 'eu quero um tum tum pa':
                        self.TumTumpa(chat_id, update_id)          
                      resposta = self.criar_resposta(
                        mensagem)
                      self.responder(resposta, chat_id)
           except Exception:
             print("Bad response")

   # Obter mensagens
   def obter_novas_mensagens(self, update_id):
       link_requisicao = f'{self.url_base}getUpdates?timeout=2'
       if update_id:
           link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
       resultado = requests.get(link_requisicao)
       return json.loads(resultado.content)
 
   # Criar uma resposta
   def criar_resposta(self, mensagem):
       if mensagem == '42':
           return f'''VOA CALANGO VOA! NUMA NAVE ESPACIAL'''
       elif mensagem == 'mariana':
           print(mensagem)
           return f'''daldegan'''
       elif mensagem == 'batata':
           return f'''frita'''
       elif mensagem == 'eu quero um tum tum pa':
           return f'''TUM TUM PA'''
       else:
           return ''


   # Responder
   def responder(self, resposta, chat_id):
       link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
       requests.get(link_requisicao)

   def TumTumpa(self, chat_id, update_id):
     mensagem = ""
     while mensagem != 'para porra':
         resposta = self.criar_resposta('eu quero um tum tum pa')
         self.responder(resposta, chat_id)
         atualizacao = self.obter_novas_mensagens(update_id)
         dados = atualizacao["result"]
         for dado in dados:
           update_id = dado['update_id']
           mensagem = str(dado["message"]["text"])

 
 
bot = TelegramBot()
bot.Iniciar()
