import json 
from datetime import datetime
from  valid_user import Valida


class User:
    
         
    def user(self):     
        user = {}
        valida = Valida()
        date = valida.date()
        try:
            name_user = input('qual o seu nome: ')
            email_user = input('qual o seu email: ')
            CPF_user = int(input('qual o seu CPF: '))
            adress_user = input('qual é o seu endereço: ')
            password = input('escolha uma senha: ')
            if CPF_user < 100000000000 and CPF_user > 9999999999:
                pass
            else:
                print('CPF invalido')
                self.user()                
            user = {
            'name':name_user,
            'email':email_user,
            'CPF':CPF_user,
            'adress':adress_user,
            'password':password,
            'date':date,
            'favorites':[]
            }
            return user
        except:
            print('CPF invalido')
            self.user()
     
        user = {
        'name':name_user,
        'email':email_user,
        'CPF':CPF_user,
        'adress':adress_user,
        'password':password,
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