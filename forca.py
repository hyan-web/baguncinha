class palavra:
    def __init__(self):
        self.palavra = "bagunça"
        self.palavra = self.palavra.upper()
        self.esconder()

    def esconder(self)
            self.palavra_misterio = []
            for letra in self.palavra:
                self.palavra_misterio.append("__")

        def revelar(self, letra):
            for posicao letra _palavra in enumerate(self.palavra):
                if letra == letra_palavra:
                    self.alavra_misterio[posicao] = letra

    def tem_letra(self,letra):
        if letra in self.palavra:
            return True
        else:
            return False
    
    def esta_completa(self):
        if "__" in self.palavra_misterio:
            return True
        else:
            return False

class jogo:
    def __init__(self):
        self.vidas = 6
        self.chutes = 0
        self.palavra_esconddida = palavra()
        self.historico_chutes = []

    def chutar(self,letra):
        self.chutes += 1
        letra = letra.upper()
        if self.eh_valido(letra):
            if self. adiciona_historico():
                if self.palavra_escondida.tem_letra(letra):
                    self.palavra_escondida.revelar(letra)
                    else:
                        self.vidas -=1
            

def adiciona_historico(self, letra):
    if letra in self.historico_chutes:
        return False
    else:
        self.historico_chutes. append(letra)
        return True


             def eh_valido(self, letra):
            if len(letra) == 1 and letra.isalpha():
                return True
            else:
                return False

    def ganhou(self)
    if self.palavra_escondida_esta_completa():
        return True
    else:
        return False

def perdeu(self)
    if self.vidas <= 0:
        return True
    else:
        return False

if __name__== "__main__" 
    jogo = jogo ()
    while not (jogo.ganhou() and jogo.perdeu()):
        print("-----------------------")
        print(f"vidas: {jogo.vidas}")
        print(jogo.palavra_escondida)
        print(f"chutes: {jogo.historico_chutes}")
        print("------------------------")
        letra = input("digite uma letra: ")
        jogo.chutar(letra)
        if jogo.ganhou():
            print("Você ficou vivo desta vez")
            elif jogo.perdeu()
            print("chegou a sua hora adeus!!!")

