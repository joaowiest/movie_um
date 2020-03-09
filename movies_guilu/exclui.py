import json
from  valid_user import Valida

class Exclu:
    def excluir_movie(self):
        valida = Valida()
        users = valida.user_read()
        exclui_movie = []
        vai = False
        foi = True
        name_movie = input("Qual é o nome do filme: ").lower().strip()
        email = input('escreva seu email: ')
        password = input('escreva seu password: ')
            
        for i in users:
            if i['email'] == email :
                if i['password'] == password:        
                    for j in i['favorites']:
                        if j['nome'] == self.name_movie:
                            print(j)
                            i['favorites'].remove(j) 
                            print('\nfilme apagado')
                            valida_dois = True
                            valida.user_write(users)
                            break
                
                        else:
                            valida_dois = False
                   
                else:
                    pass    
                
            else:
                pass

    def  excluir_user(self):
        valida = Valida()
        users = valida.user_read()
        
        email = input('escreva seu email: ')
        password = input('escreva seu password: ')
            
        for i in users:    
            if i['email'] == email :
                if i['password'] == password:        
                    users.remove(i)
                    valida.user_write(users)
                
                else:
                    pass
            else:
                pass