from PIL import Image

# Abrir a imagem .ppm
imagem = Image.open("binaria.ppm")
imagem = Image.open("cinza.ppm")


# Salvar como .png
imagem.save("binaria.png")
imagem.save("cinza.png")

