import requests, json
from  valid_user import Valida
import getpass


class Search:
    def __init__(self):
        self.nome_filme = input('\nescreva o nome do filme: ')
    
    
    def movie_search(self):    
        movies = []
        users = []
        nao_erro = False
        valida_dois = False
        valida = Valida()
        users = valida.user_read()
      
        request = valida.returns_movie(self.nome_filme)   
        if request == 0:
            pass
        else:
            date = valida.date()
            
            
            print(request['Year'])
            print(request['Genre'])
            
            try:
                escolha = int(input('\ndeseja acrescentar aos favoritos \n0 não 1 sim:\n '))
            except:
                print('digito incorreto')
                
            if(escolha == 1):
                email = input('escreva seu email: ')
                password = getpass.getpass('escreva seu password(vai estar invisivel ):  ')
                
                for i in users:
                    if i['email'] == email :
                        if i['password'] == password:
                            status = valida.status()
                            nao_erro = True

                            movie = {
                                'nome':request['Title'].lower().strip(),
                                'ano':request['Year'],
                                'genero':request['Genre'],
                                'diretor':request['Director'],
                                'status':status,
                                'data_favoritos':date,
                                'data_alteracao':date
                            }
                            
                            for j in i['favorites']:
                                if j['nome'] == self.nome_filme:
                                    print('\nfilme já cadastrado')
                                    valida_dois = True
                                    break
                                else:
                                    valida_dois = False
                        
                                            
                            if(valida_dois == True):
                                pass
                            
                            else:              
                                i['favorites'].append(movie)
                                valida.user_write(users)
                            
                        else:
                            pass    
                    else:
                        pass
                    
                if nao_erro == False:
                    print('\n\n###############################')
                    print('\nsenha ou email incorreta')
                    print('###############################')
                else:
                    pass
                
                    
            elif(escolha == 0):
                print('\n\n###############################')
                print("\nAté logo")
                print('###############################')
            
            else:
                print('\n\n###############################')
                print('\nnão tem essa opção') 
                print('###############################')
            
            