import random,time

class Jogo_pergunta:
    # sistema de amazenamento de pergunta e respostas
    def __init__(self):
        self.perguntas = [
            '_1_QUAL É A CAPITAL DA FRANÇA?',
            '_2_QUEM DESCOBRIU O BRASIL?',
            '_3_QUAL É O MAIOR PLANETA DO SISTEMA SOLAR?',
            '_4_QUAL É A FÓRMULA QUÍMICA DA ÁGUA?',
            '_5_QUANTOS CONTINENTES EXISTEM NO MUNDO?'
        ]
        self.respostas = [
            'Paris',
            'Pedro Alvares Cabral',
            'Jupiter',
            'H2O',
            'Sete'
        ]
        self.dificuldade = 0
    
    #sistema para inicialização do jogo! 
    def iniciar_jogo(self):
        print('BEM-VINDO AO JOGO DE PERGUNTA E RESPOSTA!')
        time.sleep(0.8)
        print('CADA PERGUNTA QUE VOCÊ ACERTAR, AS PRÓXIMAS FICARÃO MAIS DIFÍCEIS!')
        time.sleep(1.8)
        print('ENTÃO VAMOS COMEÇAR')
        time.sleep(0.4)
        print('CARREGANDO....')
        time.sleep(2)
        self.jogar()

    def jogar(self):
        #repetição / sistema de acertos e erros do game
        while self.dificuldade < len(self.perguntas):
            print(f'PERGUNTA {self.dificuldade + 1}: {self.perguntas[self.dificuldade]}')
            resposta = input('Sua resposta: ')
            if resposta.strip().lower() == self.respostas[self.dificuldade].strip().lower():
                print('Resposta correta!')
                self.dificuldade += 1
            else:
                print('Resposta errada. Tente novamente!')
                #quebra do loop
                
        if self.dificuldade == len(self.perguntas):
            print('Parabéns, você respondeu todas as perguntas corretamente!')
#executor do código 
if __name__ == "__main__":
    jogo = Jogo_pergunta()
    jogo.iniciar_jogo()
