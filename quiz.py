import os 
import pyfiglet
import random
cor_vermelha = "\033[91m"
cor_verde = "\033[92m"
cor_reset = "\033[0m"

temas = [
  "ciências",
  "história",
  "geografia",
  "tecnologia",
  "games",
  "animes",
  "filmes"
  ]
def getQuiz():
  quizinfo = {
      "ciências": [
          {
              "pergunta": "Qual é o elemento químico mais abundante na crosta terrestre?",
              "opcoes_resposta": ["Ferro", "Oxigênio", "Silício", "Alumínio"],
              "resposta_correta": "B"
          },
          {
              "pergunta": "Qual é o processo pelo qual as plantas fazem seu próprio alimento?",
              "opcoes_resposta": ["Fotossíntese", "Respiração", "Digestão", "Fermentação"],
              "resposta_correta": "A"
          },
          {
              "pergunta": "Qual é o símbolo químico para o ouro?",
              "opcoes_resposta": ["Ag", "Au", "Fe", "Hg"],
              "resposta_correta": "B"
          },
          {
              "pergunta": "Qual é o planeta mais próximo do Sol?",
              "opcoes_resposta": ["Marte", "Vênus", "Mercúrio", "Terra"],
              "resposta_correta": "C"
          },
          {
              "pergunta": "O que estuda a ictiologia?",
              "opcoes_resposta": ["Pássaros", "Mamíferos", "Peixes", "Insetos"],
              "resposta_correta": "C"
          }
      ],
      "história": [
          {
              "pergunta": "Quem foi o primeiro presidente dos Estados Unidos?",
              "opcoes_resposta": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
              "resposta_correta": "A"
          },
          {
              "pergunta": "Em que ano ocorreu a Revolução Francesa?",
              "opcoes_resposta": ["1789", "1799", "1801", "1776"],
              "resposta_correta": "A"
          },
          {
              "pergunta": "Quem foi a primeira mulher a ganhar um Prêmio Nobel?",
              "opcoes_resposta": ["Marie Curie", "Rosa Parks", "Emmeline Pankhurst", "Amelia Earhart"],
              "resposta_correta": "A"
          },
          {
              "pergunta": "Qual foi a primeira civilização conhecida da história?",
              "opcoes_resposta": ["Mesopotâmia", "Egito Antigo", "Cultura Harappan", "Civilização Norte-Americana"],
              "resposta_correta": "A"
          },
          {
              "pergunta": "Quem foi o líder da Revolução Cubana?",
              "opcoes_resposta": ["Fidel Castro", "Che Guevara", "Camilo Cienfuegos", "Raul Castro"],
              "resposta_correta": "A"
          }
      ],
      "geografia": [
          {
              "pergunta": "Qual é o maior país do mundo em área territorial?",
              "opcoes_resposta": ["Rússia", "China", "Estados Unidos", "Canadá"],
              "resposta_correta": "A"
          },
          {
              "pergunta": "Qual é o rio mais longo do mundo?",
              "opcoes_resposta": ["Amazonas", "Nilo", "Yangtzé", "Mississippi"],
              "resposta_correta": "A"
          },
          {
              "pergunta": "Qual é a capital da Austrália?",
              "opcoes_resposta": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
              "resposta_correta": "C"
          },
          {
              "pergunta": "Qual é o ponto mais alto da Terra?",
              "opcoes_resposta": ["Monte Everest", "Monte Kilimanjaro", "Monte Aconcágua", "Monte McKinley"],
              "resposta_correta": "A"
          },
          {
              "pergunta": "Em quantos continentes está a Rússia?",
              "opcoes_resposta": ["1", "2", "3", "4"],
              "resposta_correta": "B"
          }
      ],
      "tecnologia": [
          {
              "pergunta": "Quando foi lançado o primeiro iPhone?",
              "opcoes_resposta": ["2007", "2005", "2009", "2008"],
              "resposta_correta": "A"
          },
          {
              "pergunta": "Qual é a empresa líder mundial em vendas de smartphones?",
              "opcoes_resposta": ["Samsung", "Apple", "Huawei", "Xiaomi"],
              "resposta_correta": "A"
          },
          {
              "pergunta": "O que é a inteligência artificial?",
              "opcoes_resposta": ["Um novo tipo de computador", "Máquinas que podem pensar como humanos", "Robôs com habilidades humanas", "Um software de edição de fotos"],
              "resposta_correta": "B"
          },
          {
              "pergunta": "Qual é o maior site de vídeos do mundo?",
              "opcoes_resposta": ["Vimeo", "Dailymotion", "YouTube", "Twitch"],
              "resposta_correta": "C"
          },
          {
              "pergunta": "Qual empresa lançou o primeiro computador pessoal?",
              "opcoes_resposta": ["IBM", "Apple", "Microsoft", "Commodore"],
              "resposta_correta": "A"
          }
      ],
      "games": [
          {
              "pergunta": "Qual é o jogo mais vendido de todos os tempos?",
              "opcoes_resposta": ["Minecraft", "Tetris", "Grand Theft Auto V", "Super Mario Bros."],
              "resposta_correta": "A"
          },
          {
              "pergunta": "Em que ano foi lançado o jogo Pac-Man?",
              "opcoes_resposta": ["1980", "1978", "1982", "1985"],
              "resposta_correta": "A"
          },
          {
              "pergunta": "Qual é o personagem principal do jogo 'The Legend of Zelda'?",
              "opcoes_resposta": ["Link", "Zelda", "Ganondorf", "Navi"],
              "resposta_correta": "A"
          },
          {
              "pergunta": "Qual é o console de videogame mais vendido de todos os tempos?",
              "opcoes_resposta": ["PlayStation 2", "Nintendo DS", "Xbox 360", "Wii"],
              "resposta_correta": "A"
          },
          {
              "pergunta": "Quem é o criador do jogo 'Minecraft'?",
              "opcoes_resposta": ["Notch", "Markus Persson", "Steve Jobs", "Elon Musk"],
              "resposta_correta": "B"
          }
      ],
      "animes": [
          {
              "pergunta": "Qual é o anime mais longo em número de episódios?",
              "opcoes_resposta": ["Naruto", "One Piece", "Dragon Ball", "Bleach"],
              "resposta_correta": "B"
          },
          {
              "pergunta": "Quem é o criador do anime 'One Piece'?",
              "opcoes_resposta": ["Masashi Kishimoto", "Eiichiro Oda", "Akira Toriyama", "Hayao Miyazaki"],
              "resposta_correta": "B"
          },
          {
              "pergunta": "Qual é o poder principal de Naruto Uzumaki em 'Naruto'?",
              "opcoes_resposta": ["Sharingan", "Byakugan", "Rasengan", "Kamehameha"],
              "resposta_correta": "C"
          },
          {
              "pergunta": "Qual é o nome da protagonista de 'Sailor Moon'?",
              "opcoes_resposta": ["Sakura", "Usagi Tsukino", "Miku", "Lucy"],
              "resposta_correta": "B"
          },
          {
              "pergunta": "Em qual cidade 'Attack on Titan' se passa?",
              "opcoes_resposta": ["Tokyo", "Nova York", "Paris", "Shiganshina"],
              "resposta_correta": "D"
          }
      ],
      "filmes": [
          {
              "pergunta": "Qual filme ganhou o Oscar de Melhor Filme em 2020?",
              "opcoes_resposta": ["1917", "Parasita", "Coringa", "Era Uma Vez em Hollywood"],
              "resposta_correta": "B"
          },
          {
              "pergunta": "Quem dirigiu o filme 'A Origem'?",
              "opcoes_resposta": ["Christopher Nolan", "Quentin Tarantino", "Steven Spielberg", "James Cameron"],
              "resposta_correta": "A"
          },
          {
              "pergunta": "Qual filme ganhou o Oscar de Melhor Animação em 2019?",
              "opcoes_resposta": ["Spider-Man: Into the Spider-Verse", "Coco", "Zootopia", "Frozen"],
              "resposta_correta": "A"
          },
          {
              "pergunta": "Qual ator interpretou Tony Stark (Homem de Ferro) no Universo Cinematográfico Marvel?",
              "opcoes_resposta": ["Chris Evans", "Chris Hemsworth", "Robert Downey Jr.", "Mark Ruffalo"],
              "resposta_correta": "C"
          },
          {
              "pergunta": "Qual é o filme de maior bilheteria de todos os tempos?",
              "opcoes_resposta": ["Avatar", "Avengers: Endgame", "Titanic", "Star Wars: The Force Awakens"],
              "resposta_correta": "B"
          }
      ]
    }
  letras_t = ["A","B","C","D"]
  for tema,perguntas in quizinfo.items():
    for pergunta in perguntas:
      pos = encontrar_posicao(pergunta["resposta_correta"].upper(),letras_t)
      pergunta["resposta_correta"] = pergunta["opcoes_resposta"][pos]
      
  return quizinfo
  
def initText():
  os.system('clear')
  texto = pyfiglet.figlet_format('QUIZ')
  print(cor_vermelha + texto + cor_reset )
def initialize():
  initText()
  print("[0] Iniciar")
  print("[1] sair")
  while True:
    ac = input("Digite um número: ")
    if ac.isdigit() and int(ac) == 0:
      home()
      break
    elif ac.isdigit() and int(ac) == 1:
      os.system("clear")
      print("exit")
      break
def home():
  initText()
  print("[exit] Voltar\n")
  print("TEMAS\n\n")
  position = 0
  for lista in temas:
    print(f"[{position}] {lista}")
    position += 1
  print("\n\n")
  while True:
    tm = input("digite o número do tema: ")
    if tm == "exit":
      initialize()
      break
    if tm.isdigit() and int(tm) < len(temas):
      quiz_initialize(int(tm))
      break
def encontrar_posicao(letra, lista):
    try:
        posicao = lista.index(letra)
        return posicao
    except ValueError:
        return -1
        
def quiz_initialize(id):
  initText()
  print("digite exit para voltar")
  quiz_temp = getQuiz()[temas[id]]
  size = len(quiz_temp) - 1
  pId = random.randint(0,size)
  prc = 0
  prr = 0
  pergunta_temp = quiz_temp[pId]
  print("Pergunta: " + pergunta_temp["pergunta"])
  print("\nOpções: \n")
  options_letters = ["A","B","C","D"]
  count = 0
  random.shuffle(pergunta_temp["opcoes_resposta"])
  Resposta = options_letters[encontrar_posicao(pergunta_temp["resposta_correta"],pergunta_temp["opcoes_resposta"])]
  for options in pergunta_temp["opcoes_resposta"]:
    print(f"{options_letters[count]}) {options}")
    count += 1
  while True:
    respost = input("Resposta: ")
    if respost == "exit":
      initialize()
      break
    if respost.upper() == Resposta:
      print( cor_verde + "Correto\n\n" + cor_reset)
      Resposta = options_letters[encontrar_posicao(pergunta_temp["resposta_correta"],pergunta_temp["opcoes_resposta"])]
      quiz_temp.pop(pId)
      prc += 1
      if len(quiz_temp) == 0:
        print("\n\n\nacabou")
        if prc == len(getQuiz()[temas[id]]):
          print("\n Você acertou todas as perguntas :D \n")
        elif prc >= 1:
          if prc == 1:
            print(f"\n Você acertou o total de {prc} pergunta\n")
          else:
            print(f"\n Você acertou o total de {prc} perguntas\n")
            
          
        elif prc == 0:
          print("\n Você não acertou nenhuma pergunta :(\n")
        if prr >= 1:
          if prr == 1:
            print(f"Você errou o total de {prr} pergunta \n")
          else:
            print(f"Você errou o total de {prr} perguntas\n")
        input("aperte enter para voltar ao menu ")
        initialize()
        break
      size = len(quiz_temp) - 1
      pId = random.randint(0,size)
      count = 0
      pergunta_temp = quiz_temp[pId]
      print("Pergunta: " + pergunta_temp["pergunta"])
      print("\nOpções: \n")
      options_letters = ["A","B","C","D"]
      count = 0
      for options in pergunta_temp["opcoes_resposta"]:
        print(f"{options_letters[count]}) {options}")
        count += 1
    elif respost.upper() not in options_letters:
      print("esta resposta não esta nas opções ")
    else:
      print( cor_vermelha + "resposta incorreta\n\n" + cor_reset + Resposta)
      Resposta = options_letters[encontrar_posicao(pergunta_temp["resposta_correta"],pergunta_temp["opcoes_resposta"])]
      prr += 1
      quiz_temp.pop(pId)
      if len(quiz_temp) == 0:
        print("\n\n\nacabou")
        if prc == len(getQuiz()[temas[id]]):
          print("\n Você acertou todas as perguntas :D \n")
        elif prc >= 1:
          if prc == 1:
            print(f"\n Você acertou o total de {prc} pergunta\n")
          else:
            print(f"\n Você acertou o total de {prc} perguntas\n")
            
          
        elif prc == 0:
          print("\n Você não acertou nenhuma pergunta :(\n")
        if prr >= 1:
          if prr == 1:
            print(f"Você errou o total de {prr} pergunta \n")
          else:
            print(f"Você errou o total de {prr} perguntas\n")
        input("aperte enter para voltar ao menu ")
        initialize()
        break
      size = len(quiz_temp) - 1
      pId = random.randint(0,size)
      count = 0
      pergunta_temp = quiz_temp[pId]
      print("Pergunta: " + pergunta_temp["pergunta"])
      print("\nOpções: \n")
      options_letters = ["A","B","C","D"]
      count = 0
      for options in pergunta_temp["opcoes_resposta"]:
        print(f"{options_letters[count]}) {options}")
        count += 1      
if __name__ == "__main__":
  initialize()