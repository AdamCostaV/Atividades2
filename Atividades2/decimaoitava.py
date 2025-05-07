# Decima oitava
altura_francisco = 150
altura_sara = 110
crescimento_francisco = 2
crescimento_sara = 3

anos = 0

while altura_sara <= altura_francisco:
    altura_francisco += crescimento_francisco
    altura_sara += crescimento_sara
    anos += 1

print(f"Sara será mais alta que Francisco em {anos} anos.")