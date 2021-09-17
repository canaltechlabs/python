class bola:
    def __init__(self,material, formato, tamanho, cor):
        self.material = material
        self.formato = formato
        self.tamanho = tamanho
        self.cor = cor

print("Usando uma Classe")

futebol = bola('couro', 'redonda', '40cm', 'branca')
ping_pong = bola('pvc', 'redonda', '1,5cm', 'amarela') 

print(f'Objeto: Bola de futebol - {futebol.material}-{futebol.cor} ')
print(f'Objeto: Bola de ping pong - {ping_pong.material}-{ping_pong.cor} ')

print(futebol)
print(f'Conteudo do OBJETO: {futebol.__dict__}')