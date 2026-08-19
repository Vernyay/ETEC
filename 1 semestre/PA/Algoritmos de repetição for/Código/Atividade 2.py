vi1, vi2, vi3, vi4, i, vnum= 0, 0, 0, 0, 0, 0

for i in range(1, 21):
    vnum = int(input(f"Número {i}: "))
    if 0 <= vnum <= 25:
        vi1 += 1
    elif 26 <= vnum <= 50:
        vi2 += 1
    elif 51 <= vnum <= 75:
        vi3 += 1
    elif 76 <= vnum <= 100:
        vi4 += 1

print("\nContagem por intervalo:")
print(f"[0, 25]:   {vi1}")
print(f"[26, 50]:  {vi2}")
print(f"[51, 75]:  {vi3}")
print(f"[76, 100]: {vi4}")