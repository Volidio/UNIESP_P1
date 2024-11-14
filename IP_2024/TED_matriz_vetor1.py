VET = []
posicoes = set()

def receive_numbers():
    for _ in range(10):
        number = int(input("Enter a number: "))
        
        if number in VET:
            for i, x in enumerate(VET):
                if x == number:
                    posicoes.add(i)
            posicoes.add(len(VET))
        VET.append(number)

receive_numbers()

print(VET)
print(posicoes)
