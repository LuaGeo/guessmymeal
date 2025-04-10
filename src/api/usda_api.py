import os
from typing import Dict, List, Optional
import requests
import pandas as pd
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

class USDAApi:
    """Classe pour interagir avec l'API USDA Food Data Central."""
    
    def __init__(self):
        """Initialise l'API USDA avec la clé API du fichier .env."""
        self.api_key = os.getenv('USDA_API_KEY')
        if not self.api_key:
            raise ValueError("USDA_API_KEY introuvable dans le fichier .env")
        
        self.base_url = "https://api.nal.usda.gov/fdc/v1/foods/search"
    
    def search_food(self, 
                  query: str, 
                  page_number: int = 1, 
                  page_size: int = 10,
                  data_types: Optional[List[str]] = None) -> Dict:
        """
        Recherche des aliments dans l'API USDA.
        
        Args:
            query: Terme de recherche
            page_number: Numéro de page (default: 1)
            page_size: Taille de la page (default: 10)
            data_types: Liste de types de données à inclure (default: ["Survey (FNDDS)", "Foundation", "Branded"])
            
        Returns:
            Dict avec les résultats de la recherche
            
        Raises:
            requests.exceptions.RequestException: S'il y a des erreurs dans la requête
        """
        if data_types is None:
            data_types = ["Survey (FNDDS)", "Foundation", "Branded"]
            
        params = {
            "api_key": self.api_key,
            "query": query,
            "pageNumber": page_number,
            "pageSize": page_size,
            "dataType": data_types,
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "message": "Erreur lors de la demande à l'API USDA"}
    
    def get_food_details(self, fdc_id: int) -> Dict:
        """
        Obtient les détails d'un aliment spécifique par identifiant.
        
        Args:
            fdc_id: ID des aliments dans la base de données de l'USDA
            
        Returns:
            Dict avec les détails de l'aliment
        """
        url = f"https://api.nal.usda.gov/fdc/v1/food/{fdc_id}"
        params = {"api_key": self.api_key}
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "message": "Erreur lors de l'obtention des détails de la nourriture"}


# Exemple d'utilisation
if __name__ == "__main__":
    try:
        # Inicialise l'API
        api = USDAApi()
        
        # Cherche par "apple"
        results = api.search_food("apple")
        
        if "error" in results:
            print(f"Erro: {results['message']}")
        else:
            print("Résultats trouvés:")
            for food in results.get("foods", []):
                print(f"- {food['description']} (ID: {food['fdcId']})")
                
                # Obtient les détails du premier résultat
                if food.get("fdcId"):
                    details = api.get_food_details(food["fdcId"])
                    if "error" not in details:
                        print(f"  Calories: {details.get('foodNutrients', [{}])[0].get('value', 'N/A')} kcal")
    except ValueError as e:
        print(f"Erreur de configuration: {e}")
    except Exception as e:
        print(f"Erreur inattendue: {e}")