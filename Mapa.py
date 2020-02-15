class Mapa:


    def __init__(self ,nome):
        self.nome = nome


    def __str__(self):
        return str(self.nome)    
    

    def centro_pokemon(self,player):
        print('')
        print('você foi no centro pokemon')
        print('')
        while True:
            print('O que deseja fazer ?')
            print('1 - Curar um pokemon')
            print('2 - Ir embora')
            escolha = input('escolha : ')
            if escolha == '1':
                print('qual pokemon deseja curar?')
                player.mostrar_pokemon()
                pokemon = player.escolher_pokemon()
                pokemon.vida = pokemon.nivel * 5
            elif escolha == '2':
                print('Até mais volte quando precisar o/')
                break
            else:
                print('escolha inválida')

    
    def loja(self,player):
        print('')
        print('você foi na loja')
        print('')
        while True:
            print('O que você deseja jovem aventureiro ? ')
            print('1 - pokeball preço R$50')
            print('2 - greatball preço R$100')
            print('3 - ultraball preço R$200')
            print('4 - Ir embora')
            escolha = input('escolha : ')
            if escolha == '1':
                if player.dinheiro >= 50:
                    print('1 - Sim')
                    print('2 - Não')
                    while True:
                        confirma = input('Deseja comprar ? ')
                        if confirma == '1':
                            player.dinheiro -= 50
                            player.pokeball += 1
                            print('aqui está sua pokeball jovem !')
                            break

                        elif confirma == '2':
                            print('está bem jovem aventureiro ')
                            break
                        
                        else:
                            print('escolha inválida')
                else:
                    print('dinheiro insuficiente')

            elif escolha == '2':
                if player.dinheiro >= 100:
                    print('1 - Sim')
                    print('2 - Não')
                    while True:
                        confirma = input('Deseja comprar ? ')
                        if confirma == '1':
                            player.dinheiro -= 100
                            player.greatball += 1
                            print('aqui está sua greatball jovem !')
                            break

                        elif confirma == '2':
                            print('está bem jovem aventureiro ')
                            break
                        
                        else:
                            print('escolha inválida')
                else:
                    print('dinheiro insuficiente')
            elif escolha == '3':
                if player.dinheiro >= 200:
                    print('1 - Sim')
                    print('2 - Não')
                    while True:
                        confirma = input('Deseja comprar ? ')
                        if confirma == '1':
                            player.dinheiro -= 200
                            player.ultraball += 1
                            print('aqui está sua ultraball jovem !')
                            break

                        elif confirma == '2':
                            print('está bem jovem aventureiro ')
                            break
                        
                        else:
                            print('escolha inválida')
                else:
                    print('dinheiro insuficiente')
            elif escolha =='4':
                print('Até mais volte quando precisar o/')
                break
            else:
                print('escolha inválida')

