
import cv2
print(cv2.__version__)

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def preprocess_image(image_path):
    # Charger une image à partir du chemin spécifié
    image = cv2.imread(image_path)
    # Conversion en format RGB si nécessaire
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Redimensionner l'image à la taille attendue par le modèle (224x224)
    image_resized = cv2.resize(image, (224, 224))
    # Normaliser les valeurs de pixel (entre 0 et 1)
    image_normalized = np.array(image_resized) / 255.0
    return image_normalized


# Tester la fonction avec une image locale existante
image_path = "/Users/lua/wild_IA/projet_fil_rouge/src/img/donut_1.jpg"  # Remplacez par le chemin réel d'une image
preprocessed_image = preprocess_image(image_path)
print(f"Preprocessed image shape: {preprocessed_image.shape}")
print(f"Preprocessed image type: {type(preprocessed_image)}")
print(f"Pixel values range: {preprocessed_image.min()} - {preprocessed_image.max()}")

# Visualiser l'image d'origine et l'image prétraitée
original_image = Image.open(image_path)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(original_image)
plt.title("Image Originale")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(preprocessed_image)
plt.title("Image Prétraitée (normalized)")
plt.axis("off")
plt.show()