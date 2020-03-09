import json 
from datetime import datetime
from  valid_user import Valida


class User:
    def __init__(self):
        self.name_user = input('qual o seu nome: ')
        self.email_user = input('qual o seu email: ')
        self.CPF_user = int(input('qual o seu CPF: '))
        self.adress_user = input('qual é o seu endereço: ')
        self.password = input('escolha uma senha')
         
    def user(self):     
        user = {}
        valida = Valida()
        date = valida.date()
        
        user = {
        'name':self.name_user,
        'email':self.email_user,
        'CPF':self.CPF_user,
        'adress':self.adress_user,
        'password':self.password,
        'date':date,
        'favorites':[]
        }
        return user
    
    def register_user(self, user):
        foi_cadastrado = True
        valida = Valida() 
        users = []
        try:
            with open('user.json') as file:
                users = json.load(file)
            
        except:
            print('Usuário foi registrado:')
            foi_cadastrado = False
            users.append(user)
            valida.user_write(users)

            
        
        if(foi_cadastrado == True):
            valid_user = Valida()
            verifica = valid_user.valid_CPF(user, users)
            
            if(verifica == True):
               print('cadastro não realizado')
          
            else:
                print('bem vindo')
                users.append(user)           
                valida.user_write(users)

        else:
            pass        