import numpy as np
from skimage.color import rgb2gray  # Função para converter imagens RGB para escala de cinza
from skimage.exposure import match_histograms  # Função para ajustar o histograma de uma imagem com base em outra
from skimage.metrics import structural_similarity

# Função para encontrar diferenças entre duas imagens
def find_difference(image1, image2):
    
    # Verifica se as imagens têm o mesmo formato
    assert image1.shape == image2.shape, "Specify 2 images with the same shape"
    
    # Converte as imagens para escala de cinza
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True)
    
    # Imprime a similaridade das imagens
    print("Similarity of the images:", score)
    
    # Normaliza a imagem de diferença

    normalized_difference_image = (difference_image - np.min(difference_image)) / (np.max(difference_image) - np.min(difference_image))

# Função para transferir o histograma de uma imagem para outra
def transfer_histogram(image1, image2):
    
    # Aplica a correspondência de histogramas entre duas imagens
    matched_image = match_histograms(image1, image2, multichannel=True)
    
    return matched_image
