vsomasp, vsomamg, vsomarj, vqtdsp, vqtdmg, vqtdrj, vvelhasp, vvelhamg, vvelharj, vestado, vidade= 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

while True:
    vestado= int(input("Coloque seu estado, 1:SP, 2:MG, 3:RJ, Negativo para sair:"))
    if vestado<0:
        break
    if vestado==1 or vestado==2 or vestado==3:
        vidade= int(input("Coloque sua idade:"))
        if vidade>0:
            if vestado==1:
                vsomasp+= vidade
                vqtdsp+= 1
                if vidade >vvelhasp:
                    vvelhasp=vidade
            elif vestado==2:
                vsomamg+= vidade
                vqtdmg+= 1
                if vidade >vvelhamg:
                    vvelhamg=vidade
            elif vestado==3:
                vsomarj+= vidade
                vqtdrj+= 1
                if vidade >vvelharj:
                    vvelharj=vidade
        else:
            print("Idade inválida descartada.")
    else:
        print("Estado inválido descartado.")
    
    if vqtdsp > 0: print(f"SP - Média: {vsomasp/vqtdsp:.1f} | Maior: {vvelhasp}")
    if vqtdmg > 0: print(f"MG - Média: {vsomamg/vqtdmg:.1f} | Maior: {vvelhamg}")
    if vqtdrj > 0: print(f"RJ - Média: {vsomarj/vqtdrj:.1f} | Maior: {vvelharj}")