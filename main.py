import os
from PIL import Image

pastaOriginal = 'EXEMPLO/'
pastaDestino = 'EXEMPLO_COMPRIMIDO/'

fotos = os.listdir(pastaOriginal)

quantidadeFotos = len(fotos)

for i in range(0, quantidadeFotos):
    foto = fotos[i]

    imagem = Image.open(pastaOriginal+foto)
    
    imagem = imagem.resize((imagem.size[0]//4, imagem.size[1]//4), Image.LANCZOS)
    
    imagem.save(pastaDestino+foto, optimize=True, quality=80)
    
    print(f'{round((i / quantidadeFotos) * 100, 2)}% - {i} de {quantidadeFotos}')