import requests, json
from  valid_user import Valida

class Search:
    def __init__(self):
        self.nome_filme = input('\nescreva o nome do filme: ')
    
    
    def movie_search(self):    
        movies = []
        users = []
        valida_dois = False
        valida = Valida()
        users = valida.user_read()
      
           
        
        params = {
            'apikey':'58a0eaad',
            't':self.nome_filme    
        }

        url = 'http://www.omdbapi.com/'

        requests_filme = requests.get(url, params)
        request = requests_filme.json()
        
        
        date = valida.date()
        
        print(request['Title'])
        print(request['Year'])
        print(request['Genre'])
        
        escolha = int(input('\ndeseja acrescentar aos favoritos \n0 não 1 sim:\n '))
        if(escolha == 1):
            email = input('escreva seu email: ')
            password = input('escreva seu password: ')
            
            for i in users:
                
                
                if i['email'] == email :
                    if i['password'] == password:
                        status = valida.status()
                        

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
                
            
                
        elif(escolha == 0):
            print("\nAté logo")
        
        else:
            print('\nnão tem essa opção') 
        
        