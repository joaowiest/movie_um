import json 
from user import User
from guilu_movies import Search
from exclui import Exclu
from ver_movie import Ver_movie
from genero import Genre


def initial():
    choice = 20

    while(choice != 0):
        print('\nescolha \n\n0 para sair \n1 ser registrado \n2 pesquisar filme\n')
        print('3 quer ver sua lista de desejos \n4 excluir o filme \n5 excluir o usuario')
        print('6 indicacao')
        
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
            exclui_movie.excluir_movie()
        
        elif(choice == 5):
            exclui_movie = Exclu()
            exclui_movie.excluir_user()
        
        elif(choice == 6):
            genre = Genre()
            genre.choice_genre()
            
        else:
            print('Carai borracha...')
            initial()     

initial()