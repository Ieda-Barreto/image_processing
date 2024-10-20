from skimage.transform import resize  # Função para redimensionar imagens

# Função para redimensionar uma imagem com base em uma proporção
def resize_image(image, proportion):
    # Verifica se a proporção está entre 0 e 1
    assert 0 <= proportion <= 1, "Specify a valid proportion between 0 and 1"
    
    height = round(image.shape[0] * proportion)  # Calcula a nova altura com base na proporção
    width = round(image.shape[1] * proportion)  # Calcula a nova largura com base na proporção
    
    image_resized = resize(image, (height, width), anti_aliasing=True)  # Redimensiona a imagem com anti-aliasing
    
    return image_resized  # Retorna a imagem redimensionada
