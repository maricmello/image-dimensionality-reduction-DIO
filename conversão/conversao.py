from PIL import Image

# Abrir a imagem .ppm
imagem_binaria = Image.open("binaria.ppm")
imagem_cinza = Image.open("cinza.ppm")


# Salvar como .png
imagem_binaria.save("conversão/binaria.png")
imagem_cinza.save("conversão/cinza.png")

