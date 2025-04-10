"""
Interface Streamlit pour tester la détection d'aliments.
"""

import streamlit as st
from PIL import Image
import sys
import os

# Ajoute le répertoire src au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.models.yolo_model import FoodDetector

def main():
    # Configuration de la page
    st.set_page_config(
        page_title="GuessMyMeal - Détection d'Aliments",
        page_icon="🍽️",
        layout="wide"
    )
    
    # Titre de l'application
    st.title("🍽️ GuessMyMeal - Détection d'Aliments")
    st.write("Téléchargez une image pour détecter les aliments présents.")
    
    # Initialisation du détecteur
    @st.cache_resource
    def load_detector():
        return FoodDetector()
    
    detector = load_detector()
    
    # Upload d'image
    uploaded_file = st.file_uploader(
        "Choisissez une image...", 
        type=["jpg", "jpeg", "png"]
    )
    
    # Colonnes pour l'affichage
    col1, col2 = st.columns(2)
    
    if uploaded_file is not None:
        # Affichage de l'image originale
        image = Image.open(uploaded_file)
        col1.header("Image Originale")
        col1.image(image, use_column_width=True)
        
        # Détection et affichage des résultats
        with st.spinner("Détection en cours..."):
            annotated_img, results = detector.detect_food(image)
            
            col2.header("Détection")
            col2.image(annotated_img, use_column_width=True)
            
            # Affichage des résultats détaillés
            st.subheader("Résultats de la détection")
            if len(results.boxes) > 0:
                for box in results.boxes:
                    confidence = box.conf.item()
                    class_id = box.cls.item()
                    class_name = results.names[int(class_id)]
                    st.write(f"- {class_name}: {confidence:.2%}")
            else:
                st.write("Aucun aliment détecté.")

if __name__ == "__main__":
    main()