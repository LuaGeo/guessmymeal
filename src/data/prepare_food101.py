"""
Prépare le dataset Food-101 pour l'entraînement
"""

import os
import shutil
from pathlib import Path
import json

def prepare_food101_dataset():
    """
    Organise le dataset Food-101 dans le format attendu par YOLOv8
    """
    base_path = Path('../data/food101')
    images_path = base_path / 'images'
    meta_path = base_path / 'meta'
    
    # Créer les dossiers nécessaires
    (base_path / 'train' / 'images').mkdir(parents=True, exist_ok=True)
    (base_path / 'train' / 'labels').mkdir(parents=True, exist_ok=True)
    (base_path / 'test' / 'images').mkdir(parents=True, exist_ok=True)
    (base_path / 'test' / 'labels').mkdir(parents=True, exist_ok=True)
    
    # Lire les splits train/test
    with open(meta_path / 'train.json') as f:
        train_data = json.load(f)
    with open(meta_path / 'test.json') as f:
        test_data = json.load(f)
    
    # Fonction pour créer les annotations au format YOLO
    def create_yolo_annotation(image_data):
        # Convertir les annotations au format YOLO
        # [classe x_center y_center width height]
        pass
    
    # Copier et préparer les images et annotations
    for img_path in train_data:
        # Copier l'image
        shutil.copy(
            images_path / f"{img_path}.jpg",
            base_path / 'train' / 'images' / f"{img_path}.jpg"
        )
        # Créer l'annotation
        create_yolo_annotation(train_data[img_path])
    
    # Faire de même pour les données de test
    for img_path in test_data:
        shutil.copy(
            images_path / f"{img_path}.jpg",
            base_path / 'test' / 'images' / f"{img_path}.jpg"
        )
        create_yolo_annotation(test_data[img_path])

if __name__ == "__main__":
    prepare_food101_dataset()