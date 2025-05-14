import random
import unicodedata

def normalizar(texto):
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII').lower().strip()

# Introducao
descricao = """O Reino de Libertália era um símbolo de equilíbrio e poder, onde magos e guerreiros viviam em paz, protegendo suas terras sob a liderança justa do Império Libertália — uma cidade majestosa localizada no centro do reino.
Porém, essa paz foi quebrada quando Sephiroth, um ser sombrio de imenso poder, surgiu do desconhecido e iniciou um ataque devastador. Ele destruiu o Vilarejo de Ludwig, corrompeu antigos protetores, e tomou a cidade imperial, mergulhando-a em trevas.
Agora, os últimos heróis se erguem: magos da Floresta Encantada de Nack e guerreiros do Vulcão Legondi embarcam em uma jornada para enfrentar os lacaios de Sephiroth e libertar o coração do reino."""

print(f"{descricao}\n")
input("Pressione ENTER para escolher o seu personagem \n")

# Escolha do personagem
print("Escolha seu personagem para continuar sua jornada\n")
escolha = ""
personagem = {}

while escolha not in ["mago", "guerreiro"]:
    print("Mago da Floresta de Nack")
    print("Nascido entre raízes encantadas, o mago canaliza a energia da natureza.")
    print("Vida: 4 | Ataque: 5 | Especial: Bola de Fogo (1 a 5 de dano)\n")

    print("Guerreiro do Vulcão Legondi")
    print("Forjado no calor das batalhas, domina a espada com coragem.")
    print("Vida: 5 | Ataque: 4 | Especial: Fincada de Carneiro (1 a 4 de dano)\n")

    escolha = input("Digite 'mago' ou 'guerreiro': ").strip().lower()

    if escolha == "mago":
        personagem = {
            "classe": "mago",
            "vida": 4,
            "ataque": 5,
            "especial": "Bola de Fogo",
            "especial_dano": (1, 5)
        }
        print("Você escolheu o Mago da Floresta de Nack.\n")
    elif escolha == "guerreiro":
        personagem = {
            "classe": "guerreiro",
            "vida": 5,
            "ataque": 4,
            "especial": "Fincada de Carneiro",
            "especial_dano": (1, 4)
        }
        print("Você escolheu o Guerreiro do Vulcão Legondi.\n")

input("Pressione ENTER para escolher o primeiro destino da sua jornada...\n")

# Escolha de destino
local = ""
while local not in ["canyon", "vilarejo", "libertalia"]:
    print("Agora, sua jornada começa. Para onde deseja ir?\n")
    print("1. Canyon Cozz: lugar árido e perigoso, onde um ninja sombrio protege segredos antigos.")
    print("2. Vilarejo de Ludwig: ruínas silenciosas, dominadas pelo Guardião Caído.")
    print("3. Império Libertália: terra devastada e corrompida por Sephiroth. Um destino mortal.\n")

    entrada = input("Digite 'canyon', 'vilarejo' ou 'libertália': ")
    local = normalizar(entrada)

# Função de batalha

def batalha(nome_inimigo, vida_inimigo, ataque_inimigo):
    print(f"\nUm inimigo surge: {nome_inimigo}!")

    while vida_inimigo > 0 and personagem["vida"] > 0:
        dano_especial = random.randint(*personagem["especial_dano"])
        print(f"Você ataca com {personagem['especial']} e causa {dano_especial} de dano!")
        vida_inimigo -= dano_especial

        if vida_inimigo <= 0:
            print(f"{nome_inimigo} foi derrotado!\n")
            return True

        print(f"{nome_inimigo} revida e causa {ataque_inimigo} de dano!")
        personagem["vida"] -= ataque_inimigo
        print(f"Sua vida atual: {personagem['vida']}, Vida do inimigo: {vida_inimigo}\n")

    if personagem["vida"] <= 0:
        print("Você foi derrotado...")
        exit()

# Lógica de cada local
if local == "canyon":
    print("Você segue para o Canyon Cozz...")
    venceu = batalha("Ninja das Ruínas", 6, 3)
elif local == "vilarejo":
    print("Você caminha pelas ruínas do Vilarejo de Ludwig...")
    venceu = batalha("Guardião Caído", 7, 2)
elif local == "libertalia":
    print("Você se dirige ao coração corrompido de Libertália...")
    print("A energia do local é forte demais. Sephiroth sente sua presença e te destrói facilmente.")
    exit()

# Recompensa por vitória
if venceu:
    personagem["vida"] += 3
    personagem["ataque"] += 3
    print("Você se fortaleceu! Vida e Ataque aumentaram em +3.\n")

# Batalha final
print("\nVocê agora está pronto para enfrentar Sephiroth, o destruidor do Império!")
venceu_final = batalha("Sephiroth", 15, 8)

if venceu_final:
    print("\nCom um último golpe, você derrota Sephiroth. A paz pode finalmente retornar ao Reino de Libertália!")
