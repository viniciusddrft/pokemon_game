import random
import pickle
import time

from Pokemon import *
from Mapa import *





MAPA = [Mapa('Centro Pokemon'),
		Mapa('Loja')
]


NOMES = ['João','Vinicius','Aline','Bianca','Amanda','Mateus','Kadu'
,'Ruben','Patricia','Allan','Jonathas','warley','Maria','Fernanda','Beatriz'
,'Vitoria','Livia','Gary','Leo','riquelme','Anônimo']

POKEMONS = [
	PokemonFogo('Charmander'),
	PokemonFogo('Flarion'),
	PokemonFogo('Charmilion'),
	PokemonEletrico('Pikachu'),
	PokemonEletrico('Raichu'),
	PokemonAgua('Squirtle'),
	PokemonAgua('Magicarp')
]
class Pessoa:


	def __init__(self, nome=None, pokemons=[], dinheiro = 100, pokeball=10, greatball=0, ultraball=0, lugares=[]):
		if nome:
			self.nome = nome
		else:
			self.nome = random.choice(NOMES)

		self.pokemons = pokemons

		self.dinheiro = dinheiro

		self.pokeball = pokeball

		self.greatball = greatball

		self.ultraball = ultraball

		self.lugares = lugares

	def __str__(self):
		return self.nome

	
	def mostrar_pokemon(self):
		if self.pokemons:
			print('')
			print('pokemons de ' + str(self.nome))
			for index,pokemon in enumerate(self.pokemons):
				print('')
				print( str(index) +')-' + str(pokemon.nome) +' nivel : '+ str(pokemon.nivel))
				print('pontos de ataque -> ' + str(pokemon.ataque))
				print('pontos de vida -> ' + str(pokemon.vida))
				print('___________________________')
		else:
			print('você não tem pokemons :/ ')


	def escolher_pokemon(self):
		if self.pokemons:
			pokemon_escolhido = random.choice(self.pokemons)
			print(str(self) + ' escolheu ' + str(pokemon_escolhido))
			return pokemon_escolhido
		else:
			print('Este jogador não possui pokemon para ser escolhido')	


	def mostrar_dinheiro(self):
		print('')
		print('você tem $ {}'.format(self.dinheiro))


	def ganhar_dinheiro(self, quantidade):
		self.dinheiro += quantidade
		print('você ganhou $ {}'.format(quantidade))
		self.mostrar_dinheiro()

	def batalhar(self, oponente):
		print(str(self) + ' entrou em batalha com ' + str(oponente))
		oponente.mostrar_pokemon()
		pokemon_inimigo = oponente.escolher_pokemon()
		self.mostrar_pokemon()
		pokemon_player = self.escolher_pokemon()
		if pokemon_player and pokemon_inimigo:
			while True:
				vitoria = pokemon_player.atacar(pokemon_inimigo)
				time.sleep(2)
				if vitoria:
					print('{} ganhou a batalha'.format(self))
					self.ganhar_dinheiro(pokemon_inimigo.nivel * 3)
					pokemon_player.xp += 1
					if pokemon_player.xp >= pokemon_player.nivel:
						print('parabens seu pokemon subiu de nivel!!!')
						pokemon_player.nivel += 1
						pokemon_player.ataque = pokemon_player.nivel * 2.5
						pokemon_player.vida = pokemon_player.nivel * 5

					break
				vitoria_inimiga = pokemon_inimigo.atacar(pokemon_player)
				time.sleep(2)
				if vitoria_inimiga:
					print('{} ganhou a batalha'.format(oponente))
					break
		else:
			print('essa batalha não pode ocorrer')



class Player(Pessoa):
	tipo = 'player'
	def capturar(self, pokemon):
		self.pokemons.append(pokemon)
		print('você capturou : ' + str(pokemon.nome))

	def tentar_capturar(self,pokemon):
		while True:
			print('escolha qual usar para capturar ')
			print('1 - pokeball -> ' + str(self.pokeball))
			print('2 - greatball -> ' + str(self.greatball))
			print('3 - ultraball -> ' + str(self.ultraball))
			escolha = input('escolha : ')
			if escolha == '1':
				if self.pokeball:
					self.pokeball -=1
					if random.random() >= 0.6:
						self.pokemons.append(pokemon)
						print('você capturou : ' + str(pokemon.nome))
						break
					else:
						print('O ' + str(pokemon.nome) + ' fugiu :/')
						break
				else:
					print('você não possui pokeball')
			elif escolha == '2':
				if self.greatball:
					self.greatball -=1
					if random.random() >= 0.4:
						self.pokemons.append(pokemon)
						print('você capturou : ' + str(pokemon.nome))
						break
					else:
						print('O ' + str(pokemon.nome) + ' fugiu :/')
						break
				else:
					print('você não tem greatball')
			elif escolha == '3':
				if self.ultraball:
					self.ultraball -=1
					if random.random() >= 0.2:
						self.pokemons.append(pokemon)
						print('você capturou : ' + str(pokemon.nome))
						break
					else:
						print('O ' + str(pokemon.nome) + ' fugiu :/')
						break
				else:
					print('você não possui ultraball')
			else:
				print('escolha invalida')

	def mostrar_itens(self):
		print('')
		print('você tem ' + str(self.pokeball) + ' pokeball(s)')
		print('você tem ' + str(self.greatball) + ' gratball(s)')
		print('você tem ' + str(self.ultraball) + ' ultraball(s)')

	def escolher_pokemon(self):
		if self.pokemons:
			while True:
				try:
					escolha = int(input('escolha o seu pokemon : '))
					pokemon_escolhido = self.pokemons[escolha]
					print(str(pokemon_escolhido) + ' eu escolho você!!!')
					return pokemon_escolhido
				except:
					print('escolha invalida')	
		else:
			print('Este jogador não possui pokemon para ser escolhido')

	def selecionar_lugares(self):
		if self.lugares:
			for index,lugar in enumerate(self.lugares):
				print( str(index) +')-' + str(lugar))	
			while True:
				try:
					escolha = int(input('escolha qual lugar você quer ir : '))
					if escolha <= len(self.lugares):
						break
					else:
						print('escolha inválida')
				except:
					pass

			escolha = self.lugares[escolha]
			if escolha in self.lugares:
				if escolha.nome == 'Centro Pokemon':
					escolha.centro_pokemon(self)#self nessa linha é o player

				elif escolha.nome == 'Loja':
					escolha.loja(self)#self nessa linha é o player
				

		else:
			print('você não conhece nenhum lugar :/ ')




	def esplorar(self):
		numero_aleatorio = random.randint(0,10)
		#print(numero_aleatorio) usado para debug
		if numero_aleatorio <= 2:
			pokemon = random.choice(POKEMONS)
			print('um pokemon selvagem apareceu!!! {} '.format(pokemon))
			escolha = input('deseja capturar o pokemon? s/n : ')
			if escolha == 's' or escolha == 'S':
				self.tentar_capturar(pokemon)
			else:
				print('ok boa viagem')

		elif numero_aleatorio > 2 and numero_aleatorio <= 7:
			if MAPA:
				lugar = random.choice(MAPA)
				#---manutenção concluida com sucesso dia 30/12/2019
				if self.lugares:
					existe = False
					if len(MAPA) == len(self.lugares) and len(self.lugares) == 2:# o numero 2 é a quantidade de mapas atualize quando por mais mapas
						existe = True
					for i in self.lugares:
						if lugar.nome != i.nome and existe == False:
							print('Você descobriu um novo lugar no mapa!!!')
							self.lugares.append(lugar)
							MAPA.remove(lugar)#removendo da lista sorteio pq já foi descoberto na linha a cima
							print(lugar.nome)
						else:
							existe = True
					
					if existe == True:
						print('essa exploração não deu em nada :(')

				else:
					print('Você descobriu um novo lugar no mapa!!!')
					self.lugares.append(lugar)
					MAPA.remove(lugar)#removendo da lista sorteio pq já foi descoberto na linha a cima
					print(lugar.nome)

			else:
				print('essa exploração não deu em nada :(')

		elif numero_aleatorio >= 8:
			print('você encontrou um inimigo no caminho tera que enfrentar ele')
			inimigo_aleatorio = Inimigo()
			self.batalhar(inimigo_aleatorio)
		else:
			print('essa exploração não deu em nada :(')



class Inimigo(Pessoa):
	tipo = 'inimigo'

	def __init__(self, nome=None, pokemons=[]):
		if not pokemons:
			pokemons_aleatorios = []
			for i in range(random.randint(1, 6)):
				pokemons_aleatorios.append(random.choice(POKEMONS))

			super().__init__(nome=nome , pokemons=pokemons_aleatorios)
		else:
			super().__init__(nome=nome , pokemons=pokemons)


