vmaioresdeidade, vidade, i= 0, 0, 0

for i in range(1, 21):
    vidade = int(input(f"Digite a vidade da {i}ª pessoa: "))
    
    if vidade >= 18:
        vmaioresdeidade += 1

print("-" * 30)
print(f"Total de pessoas maiores de vidade: {vmaioresdeidade}")