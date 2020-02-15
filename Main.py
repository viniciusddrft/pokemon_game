import pickle

from Pokemon import *
from Pessoa import *





def salvar_jogo(player):
    try:
        with open('database.db','wb') as arquivo:
            pickle.dump(player, arquivo)
            print('jogo salvo com sucesso!')
    except Exception as erro:
        print('algum erro ocorreu ao salvar o jogo : ' + str(erro))



def carregar_jogo():
    try:
        with open('database.db','rb') as arquivo:
            player = pickle.load(arquivo)
            print('Loading feito com sucesso')
            return player
    except Exception as erro:
        print('save não encontrado : ' + str(erro))

def escolherinicial(player):
    print('Olá aqui começa sua jornada escolha um pokemon inicial para te acompanhar nessa jornada!')

    charmander = PokemonFogo('charmander',nivel=1)
    squirtle = PokemonAgua('squirtle', nivel=1)
    bulbasaur = PokemonGrama('bulbasaur',nivel=1)

    print('1 - ' + str(charmander))
    print('2 - ' + str(squirtle))
    print('3 - ' + str(bulbasaur))

    while True:
        escolha = input('escolha o seu pokemon : ')

        if escolha == '1':
            player.capturar(charmander)
            break
        elif escolha == '2':
            player.capturar(squirtle)
            break
        elif escolha == '3':
            player.capturar(bulbasaur)
            break
        else:
            print('escolha invalida')
    


if __name__ == "__main__":
    print('___________________________________________')
    print('Bem-vindo ao jogo pokemon RPG de terminal')
    print('___________________________________________')
    player = carregar_jogo()
    if not player:
        nome = input('Qual é o seu nome? ')
        player = Player(nome)
        print('Olá {}, esse é um mundo habitado por pokemoons, a partir de agora sua missão é se tornar um mestr pokemon!'.format(player.nome))
        print('Capture o maximo de pokemons que conseguir e lute com seus inimigos')
        player.mostrar_dinheiro()
        gary = Inimigo(nome="Gary",pokemons=[PokemonAgua("Squirtle", nivel=1)])
        if player.pokemons:
            print('Observei que você já possui alguns pokemons')
            player.mostrar_pokemon()
        else:
            print('Você ainda não possui pokemons, portanto escolha seu pokemon inicial!')
            escolherinicial(player)
            print('Pronto agora que você tem pokemons, enfrente seu arqui-rival desde o jardim de infância Gary!!!')
            player.batalhar(gary)
            salvar_jogo(player)



    while True:
        print('________________________')
        print('O que deseja fazer?')
        print('1 - explorar o mapa')
        print('2 - ver pokeagenda')
        print('3 - mostrar dinheiro')
        print('4 - mostrar itens')
        print('5 - ver lugares conhecidos no mapa')
        print('0 - sair do jogo')
        print('')
        escolha = input('Sua escolha: ')

        if escolha == '0':
            salvar_jogo(player)
            print('Bye o/')
            print('fechando o jogo...')
            break
        elif escolha == '1':
            player.esplorar()
            salvar_jogo(player)
        elif escolha == '2':
            player.mostrar_pokemon()
        elif escolha == '3':
            player.mostrar_dinheiro()
        elif escolha == '4':
            player.mostrar_itens()
        elif escolha == '5':
            print(player.selecionar_lugares())  
        else:
            print('escolha invalida')
