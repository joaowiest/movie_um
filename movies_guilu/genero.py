import json
from  valid_user import Valida


class Genre:
    def choice_genre(self):
        valida = Valida()
        users = valida.user_read()
        valida_um = 0
        não_repete = []
        valida_dois = True
        try:
            choice = int(input('escolha \n1 para drama \n2 para açao \n3 para aventura \n4 animação: \n'))
        except:
            print('digito incorreto')
            
        if choice == 1:
            valida_um = 'Drama'
        elif choice == 2:
            valida_um = 'Action'
        
        elif choice == 3:
            valida_um = 'Adventure'
        
        elif choice == 4:
            valida_um = 'Animation'
        
        else:
            pass
   
        for user in users:
            for movi in user['favorites']:
                tentativa = movi['genero'].strip()
                tentativa = tentativa.replace(',', ' ').split()
                for genre in tentativa:
                    if genre == valida_um:
                        for i in não_repete:
                            if i == movi['nome']:   
                                valida_dois = False
                                break
                            else:
                                valida_dois = True
                            
                        if valida_dois == True:
                            print()
                            não_repete.append(movi['nome'])
                            print(movi['nome'])
                            print(movi['ano'])
                            print(movi['genero'])
                        else:
                            pass
                        
                    else:
                        pass