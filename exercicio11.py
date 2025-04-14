import random

#defesa e ataque de quem ta jogando
ataque_user = random.randint(1, 50)
defesa_user = random.randint(1, 50)

#defesa e ataque do pc/inimigo
ataque_pc = random.randint(1, 50)
defesa_pc = random.randint(1, 50)
#definindo a escola da vida
vida = random.randint(200, 1000)

#separando a vida do jogador e do pc
vida_user = vida
vida_pc = vida

# menu :)
input("""
========================================
             🗡️  RPG  🛡️
========================================
      Aperte enter ↳ para continuar!
========================================
""")

print(f"\n=== DUELO DE HERÓIS ===\n\n===      Você       ===\nHP:  {vida}    \nATQ: {ataque_user}      DEF: {defesa_user}")

print(f"\n===      Inimigo       ===\nHP:  {vida}    \nATQ: {ataque_pc}      DEF: {defesa_pc}")

input("\nAperte enter ↳ para continuar")

#definindo o turno pra ir contando conforme for passando
turno = 1

#loop pro jogo rolar enquanto os jogadores não tiverem o hp menor que 0
while vida_user > 0 and vida_pc > 0:
    escolha = input(f"\n\n--- Turno {turno} ---\nSeu HP: {vida_user} | Inimigo HP: {vida_pc}\nSua vez: [1] Atacar ou [2] Curar?")
    #Ataque user
    if escolha == "1":
        print("\nVocê escolheu atacar!")
        dano = ataque_user - defesa_pc
        if dano <0:
            dano = 0
        vida_pc -= dano
        print(f"Você causou {dano} de dano!\n")
    #Defesa user
    elif escolha == "2":
        print("\nVocê escolheu se curar!")
        cura_user = random.randint(10,50)
        vida_user += cura_user
        print(f"Você recebeu {cura_user} pontos de cura!\n")

    #Isso aqui pq não sei limitar a escolha e nem voltar pra vez do jogador, ent ele só vai perder a vez mesmo
    else:
        print("Escolha inválida. Você perdeu o turno")
    #se conseguiu zerar a vida do oponente é vitoria
    if vida_pc <= 0:
        print("\n🏆 Você derrotou o inimigo!")
        break

    #Escolha do pc
    pc = random.choice(["atacar", "curar"])

    #Ataque pc
    if pc == "atacar":
        print("\nO inimigo escolheu atacar")
        dano_pc = ataque_pc - defesa_user
        if dano_pc < 0:
            dano_pc = 0
        vida_user -= dano_pc
        print(f"O inimigo causou {dano_pc} de dano!\n")
    #Defesa pc
    elif pc == "curar":
        print("\nO inimigo escolheu se curar")
        cura_pc = random.randint(10,50)
        vida_pc += cura_pc
        print(f"O inimigo recebeu {cura_pc} pontos de cura!\n")
    #Se o pc zerar a vida do jogador é derrota
    if vida_user <= 0:
        print("\n💀 Você foi derrotado...")
        break

    #contagem do turno
    turno += 1
    #Aqui só pra controlar inicio de cada turno
    input("\nAperte Enter ↳ para ir para o próximo turno")

#não consegui fazer os desafios :(






