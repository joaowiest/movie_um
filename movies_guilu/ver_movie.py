import json 
from  valid_user import Valida
import getpass


class Ver_movie:
    
    def ver_movie(self):
        movies = []
        valida = Valida()
        date = valida.date()
        users = valida.user_read()
        nao_erro = False       
        
        email = input('escreva seu email: ')
        password = getpass.getpass('escreva seu password(vai estar invisivel ):  ')
                
        for i in users:
            if i['email'] == email :
                if i['password'] == password:
                    for j in i['favorites']:
                        print('\n')
                        print(j['nome'])
                        print(j['ano'])
                        print(j['genero'])
                        print(j['diretor'])
                        print(j['status'])
                        nao_erro = True
                        
                    escolha = int(input('\nquer alterar o status do filme \n0 não 1 sim:\n'))
                    if(escolha == 1):
                        nome_movie = input('qual o filme que você deseja alterar: \n').lower().strip()
                        
                        for i in i['favorites']:
                            if(i['nome'] == nome_movie):
                                status = valida.status()
                                i['status'] = status
                                i['data_alteracao']:date
                                valida.user_write(users)
                            else:
                                pass
                
                    else:
                        print('\n\n###############################')
                        print('ate mais')
                        print('###############################')
                        
                else:
                    pass
            
            else:
                pass        
            
        if nao_erro == False:
            print('\n\n###############################')
            print('senha ou email incorreta')
            print('###############################')
            
        else:
            pass
                