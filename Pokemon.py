import random

class Pokemon:
    
    def __init__(self , especie , nivel=None , nome = None ,xp=None):
        self.especie = especie
        self.nivel = nivel
        if nivel:
            self.nivel = nivel
        else:
            self.nivel = random.randint(1 , 100)
        if nome:
            self.nome = nome
        else:
            self.nome = especie
        if xp:
            self.xp = xp
        else:
            self.xp = 0
        
        self.ataque = self.nivel * 2.5
        self.vida = self.nivel * 5

    def __str__(self):
        return str(self.nome) +' '+ str(self.nivel)


    def atacar(self, alvo):
        ataque_efetivo =  int((self.ataque * random.random() * 1.3))
        alvo.vida -= ataque_efetivo
        print('{} perdeu {} pontos de vida'.format(alvo, ataque_efetivo))

        if alvo.vida <= 0:
            print('{} foi derrotado'.format(alvo))
            return True
        else:
            return False

class PokemonEletrico(Pokemon):
    tipo = 'Eletrico'
    def atacar(self, alvo):
        print(str(self.nome) + ' deu um raio no ' + str(alvo.nome))
        return super().atacar(alvo)
    def dar_choque(self, alvo):
        print(str(self.nome) + ' deu um choque no ' + str(alvo.nome))
        return super().atacar(alvo)


class PokemonFogo(Pokemon):
    tipo = 'Fogo'
    def atacar(self, alvo):
        print(str(self.nome) + ' laçou fogo no ' + str(alvo.nome))
        return super().atacar(alvo)
    def bola_de_fogo(self, alvo):
        print(str(self.nome) + ' lançou uma bola de fogo na cabeça do ' + str(alvo.nome))
        return super().atacar(alvo)


class PokemonAgua(Pokemon):
    tipo = 'Agua'
    def atacar(self, alvo):
        print(str(self.nome) + ' laçou agua no ' + str(alvo.nome))
        return super().atacar(alvo)
    def jato_de_agua(self, alvo):
        print(str(self.nome) + " lançou um jato d'agua no " + str(alvo.nome))
        return super().atacar(alvo)


class PokemonGrama(Pokemon):
    tipo = 'Grama'
    def atacar(self, alvo):
        print(str(self.nome) + ' lançou mato no ' + str(alvo.nome))
        return super().atacar(alvo)
    def bater_com_cipo(self, alvo):
        print(str(self.nome) + " bateu com cipó no " + str(alvo.nome))
        return super().atacar(alvo)
