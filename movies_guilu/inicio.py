import json 
from user import User
from guilu_movies import Search
from exclui import Exclu
from ver_movie import Ver_movie


def initial():
    choice = 20

    while(choice != 0):
        print('\nescolha \n\n0 para sair \n1 ser registrado \n2 pesquisar filme\n')
        print('3 quer ver sua lista de desejos \n4 excluir o filme')
        choice = int(input())
        
        if(choice == 0):
            print('obrigado por usar guiluflix até o próximo')
            break
        elif(choice == 1):
            class_user =  User() 
            user_dicio = class_user.user()
            class_user.register_user(user_dicio)       
        
        elif(choice == 2):
            movie = Search()
            movie.movie_search()
            
        elif(choice == 3):
            movie = Ver_movie()
            movie.ver_movie()
        
        elif(choice == 4):
            exclui_movie = Exclu()
            exclui_movie.excluir()
        else:
            print('Carai borracha...')
            initial()     

initial()