# 🖼️ Conversão de Imagens: Colorida → Cinza → Binarizada

Este projeto implementa, em Python, a leitura de uma imagem e sua conversão para escala de cinza e para binário (preto e branco), **sem utilizar bibliotecas externas** para o processamento da imagem. Apenas bibliotecas como `matplotlib` e `numpy` são utilizadas **para exibir os resultados**.

---

> Resultados disponível abaixo:

<h3>Resultados das Imagens</h3>

<p float="left">
  <figure style="display: inline-block; margin-right: 10px;">
    <figcaption>Foto Original</figcaption>
    <img src="yuri_temp.jpg" alt="Foto Original" width="200"/>
  </figure>

  <figure style="display: inline-block; margin-right: 10px;">
    <figcaption>Foto Binarizada</figcaption>
    <img src="binaria_temp.png" alt="Foto Binarizada" width="200"/> 
  </figure>

  <figure style="display: inline-block;">
    <figcaption>Foto Cinza</figcaption>
    <img src="cinza_temp.png" alt="Foto Cinza" width="200"/>
  </figure>
</p>


## 🚀 Funcionalidades

- 📥 Leitura de imagem colorida
- 🌑 Conversão para **tons de cinza**
- ⚫⚪ Binarização da imagem (preto e branco) com limiar ajustável
- 💾 Salvamento das imagens resultantes (`cinza.ppm`, `binaria.ppm`)
- 👁️ Visualização das imagens com `matplotlib`

---