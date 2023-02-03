def contagem_de_tempo(hora):
    input(int(hora))
    #substituir pelo input do usuário usando customtkinter
    
    for hora in range(hora, 24):
        if hora <= 24:
            hora += 1
        elif hora >= 24:
            print("Hora Inválida")
            break
        else:
            pass
            
        print(hora)


