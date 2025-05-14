# Resumo da hístoria inicial
historia = """O Reino de Libertália era um símbolo de equilíbrio e poder, onde magos e guerreiros viviam em paz, protegendo suas terras sob a liderança justa do Império Libertália — uma cidade majestosa localizada no centro do reino.
Porém, essa paz foi quebrada quando Sephiroth, um ser sombrio de imenso poder, surgiu do desconhecido e iniciou um ataque devastador. Ele destruiu o Vilarejo de Ludwig, corrompeu antigos protetores, e tomou a cidade imperial, mergulhando-a em trevas.
Agora, os últimos heróis se erguem: magos da Floresta Encantada de Nack e guerreiros do Vulcão Legondi embarcam em uma jornada para enfrentar os lacaios de Sephiroth e libertar o coração do reino."""
print(f"{historia}\n")
input("Pressione ENTER para escolher o seu personagem \n")

#Escolha do personagem
print("Escolha seu personagem para continuar sua jornada\n")

escolha = ""

while escolha not in ["mago", "guerreiro"]:

    print("Mago da Floresta de Nack")
    print("Nascido entre raízes encantadas, o mago canaliza a energia da natureza.")
    print("Vida: 4 | Ataque: 5 | Especial: Bola de Fogo (1 a 5 de dano)\n")

    print("Guerreiro do Vulcão Legondi")
    print("Forjado no calor das batalhas, domina a espada com coragem.")
    print("Vida: 5 | Ataque: 4 | Especial: Fincada de Carneiro (1 a 4 de dano)\n")

    escolha = input("Digite 'mago' ou 'guerreiro' para escolher seu herói: ").strip().lower()

    if escolha == "mago":
        print("Você escolheu o Mago da Floresta de Nack. Que os espíritos antigos guiem seus passos!\n")
    elif escolha == "guerreiro":
        print("Você escolheu o Guerreiro do Vulcão Legondi. Que sua espada arda como a lava!\n")
                
input ("Pressione ENTER para escolher o primeiro destino de sua jornada...\n")

# Escolha do primeiro destino
local = ""
while local not in["canyon", "vilarejo","libertália","libertalia"]:
    print("\nAgora, sua jornada começa. Você deve escolher para onde ir: \n")
    print("1. Canyon Cozz: lugar árido e perigoso, onde um ninja sombrio protege segredos antigos.")
    print("2. Vilarejo de Ludwig: ruínas silenciosas, dominadas pelo Guardião Caído.")
    print("3. Império Libertália: terra devastada e corrompida por Sephiroth. Um destino mortal.\n")

    local  = input("Digite 'canyon' para ir ao Canyon Cozz, digite 'vilarejo' se deseja que seu destino seja o Vilarejo destruído de Ludwig ou digite 'libertália' se deseja ir ao reino destruído...Leve em consideração que a probabilidade de vitória é muito pequena: ").strip().lower()

    if local == "canyon":
        print("Você decide seguir para o Canyon Cozz, onde mistérios aguardam e o ambiente desolado esconde segredos antigos.\n")
    elif local == "vilarejo": 
        print("Você decide ir ao Vilarejo de Ludwig, onde os ecos de uma cidade destruída chamam por respostas que podem mudar tudo.\n")
    elif local == "libertália" or "libertalia":
        print("Você decide seguir para Libertália, um reino em ruínas tomado pela escuridão. Algo ali é forte demais — você pareceque não estar pronto... mas que a sorte esteja com você.\n")
            
    input("Pressione ENTER para começar sua viagem\n") 

    if local == "canyon":
        print("\nO caminho até o Canyon Cozz começa sutil, entre campos ressecados e árvores retorcidas pelo calor. Aos poucos, a vegetação desaparece, substituída por colinas áridas, onde o vento levanta poeira como se varresse os restos de algo esquecido. Você passa por restos de construções tomadas pela areia, pilares caídos e símbolos esculpidos em pedra que ninguém mais parece lembrar. Mais adiante, surgem formações rochosas afiadas, como lanças cravadas no chão por mãos colossais. A cada passo, o silêncio aumenta — e o horizonte começa a se abrir num corte profundo: o início do canyon. O ar ali parece mais pesado, como se algo observasse de longe... esperando.")
    elif  local == "vilarejo":
        print("\nO caminho até Ludwig é envolto por névoa e silêncio. Árvores secas cercam a trilha, e pequenas ruínas esquecidas surgem entre as sombras. Cruzes tortas e casas despedaçadas anunciam o fim de algo que já foi vivo. No horizonte, envolto em bruma, o vilarejo aparece — quieto, quebrado, e à espera.") 
    else:
        print ("\nO caminho até Libertália é sombrio e traiçoeiro. A estrada parece se desfazer sob seus pés, tomada por rachaduras, neblina e ecos de batalhas antigas. Estruturas quebradas surgem entre colinas escuras, como fantasmas de um reino que desabou sobre si mesmo. O ar é pesado, difícil de respirar — como se o próprio mundo avisasse que você não está pronto. E, ao longe, envolta em trevas, Libertália o observa. A chance de vitória é mínima... mas ainda assim, você continua.")