import requests, json
from datetime import datetime



class Valida:        
    def valid_CPF(self, user, users):
        verifica = False
        for i in users:
            if(i['CPF'] == user['CPF']):
                verifica = True
                break
            else:
                verifica = False    
        return verifica
     
    
    def valid_user(self, users, name, CPF):
        cliente_cadastrado = False
        cpf = False
        for i in users:
            if(i['CPF'] == CPF):
                if(i['name'] == name):
                    print('usuario foi encontrado:')
                    cliente_cadastrado = True
                    break
        
                else:
                    cliente_cadastrado = False
                    
            else:
                cliente_cadastrado = False

        return cliente_cadastrado        


    def movie_read(self):
        movies = []
        try:
            with open('movie.json') as file:
                movies = json.load(file)
        except:
            print('\n\n###############################')
            print("nao tem favoritos")
            print('###############################')
            
        return movies
            
            
    def movie_write(self,movies):
        with open('movie.json','w') as file:
            json.dump(movies, file, indent = 2)


    def date(self):
        date = datetime.today()
        date = date.strftime('%m-%d-%y')       
        return date
        
    
    def status(self):
        try:
            escolha_um = int(input("\n\nstatus \n1 ja viu o filme \n2 estavendo o filme \n3 vai ver o filme:\n "))
        except:
            print('\n\n###############################')
            print('digito incorreto')
            print('###############################')

        if(escolha_um == 1):
            status = 'ja viu o filme'
            return status
        
        elif(escolha_um == 2):
            status = 'estavendo o filme'
            return status
        
        elif(escolha_um == 3):
            status = 'vai ver o filme'
            return status
      
        
    def user_write(self,users):
        with open('user.json','w') as file:
            json.dump(users, file, indent = 2)
            print('alterado')


    def user_read(self):
        try:
            with open('user.json') as file:
                users = json.load(file)
                return users
        except:
            print('\n\n###############################')
            print('não tem usuario')
            print('###############################')
    def returns_movie(self, nome_filme):
        try:
            params = {
                'apikey':'58a0eaad',
                't':nome_filme    
            }

            url = 'http://www.omdbapi.com/'

            requests_filme = requests.get(url, params)
            request = requests_filme.json()
            print(request['Title'])
            return request
        except:
            print('\n\n###############################')
            print('filme não encontrado')
            print('###############################')
            return 0