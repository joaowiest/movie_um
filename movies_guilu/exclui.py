import json


class Exclu:
    def __init__(self):
        self.name_movie = input("What is the name of the movie(Qual é o nome do filme):").lower().strip()
    
    def excluir(self):
        exclui_movie = []
        vai = False
        foi = True
        
        try:
            with open('movie.json') as file:
                exclui_movie = json.load(file)
                
        except:
            print('movie not found(filme não encontrado)')
            foi = False     
        
        print(exclui_movie)       
        if(foi == True):
            for i in exclui_movie:  
                if(i['nome'] == self.name_movie):
                    exclui_movie.remove(i) 
                    vai = True
                    break
                
                else:
                    vai = False
            
            if(vai == True):
                print('filme apagado')
                with open('movie.json', 'w') as file:
                    json.dump(exclui_movie, file, indent = 2)
            else:
                print('não foi kkkk')