# src/data/prepare_food101.py

"""
Prépare le dataset Food-101 pour l'entraînement avec YOLOv8
"""

import os
import shutil
from pathlib import Path
import yaml

def prepare_food101_dataset():
    """
    Organise le dataset Food-101 dans le format attendu par YOLOv8
    """
    # Chemins des dossiers
    base_path = Path('data/raw/food101')
    processed_path = Path('data/processed/food101')
    
    # Vérifier si le dataset est présent
    if not (base_path / 'images').exists():
        raise FileNotFoundError(
            f"Dossier images non trouvé dans {base_path}. "
            "Vérifiez que le dataset Food-101 est correctement installé."
        )
    
    # Créer les dossiers de destination
    train_img_dir = processed_path / 'train' / 'images'
    train_label_dir = processed_path / 'train' / 'labels'
    test_img_dir = processed_path / 'test' / 'images'
    test_label_dir = processed_path / 'test' / 'labels'
    
    for dir_path in [train_img_dir, train_label_dir, test_img_dir, test_label_dir]:
        dir_path.mkdir(parents=True, exist_ok=True)
    
    # Lire les fichiers de métadonnées
    with open(base_path / 'meta' / 'train.txt') as f:
        train_images = [line.strip() for line in f.readlines()]
    
    with open(base_path / 'meta' / 'test.txt') as f:
        test_images = [line.strip() for line in f.readlines()]
    
    # Obtenir la liste des classes (noms des dossiers dans images/)
    classes = sorted([d.name for d in (base_path / 'images').iterdir() 
                    if d.is_dir()])
    
    # Créer le fichier data.yaml pour YOLOv8
    data_yaml = {
        'path': str(processed_path.absolute()),
        'train': str(train_img_dir.absolute()),
        'val': str(test_img_dir.absolute()),
        'names': {i: name for i, name in enumerate(classes)}
    }
    
    with open(processed_path / 'data.yaml', 'w') as f:
        yaml.safe_dump(data_yaml, f)
    
    print("Préparation des images d'entraînement...")
    for img_path in train_images:
        # Les chemins dans train.txt sont de la forme 'classe/image_name'
        class_name = img_path.split('/')[0]
        src = base_path / 'images' / f"{img_path}.jpg"
        dst = train_img_dir / f"{class_name}_{img_path.split('/')[-1]}.jpg"
        shutil.copy(src, dst)
        
        # Créer une annotation simple (juste la classe)
        class_id = classes.index(class_name)
        with open(train_label_dir / f"{class_name}_{img_path.split('/')[-1]}.txt", 'w') as f:
            # Format YOLO: class_id x_center y_center width height
            # Pour simplifier, nous considérons que l'objet occupe toute l'image
            f.write(f"{class_id} 0.5 0.5 1.0 1.0\n")
    
    print("Préparation des images de test...")
    for img_path in test_images:
        class_name = img_path.split('/')[0]
        src = base_path / 'images' / f"{img_path}.jpg"
        dst = test_img_dir / f"{class_name}_{img_path.split('/')[-1]}.jpg"
        shutil.copy(src, dst)
        
        # Créer une annotation simple
        class_id = classes.index(class_name)
        with open(test_label_dir / f"{class_name}_{img_path.split('/')[-1]}.txt", 'w') as f:
            f.write(f"{class_id} 0.5 0.5 1.0 1.0\n")
    
    print("Préparation terminée!")
    print(f"Dataset préparé dans: {processed_path}")
    print(f"Nombre de classes: {len(classes)}")
    print(f"Images d'entraînement: {len(train_images)}")
    print(f"Images de test: {len(test_images)}")

if __name__ == "__main__":
    prepare_food101_dataset()