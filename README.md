# GuessMyMeal

## 📝 Project Description

GuessMyMeal is a project that uses computer vision and machine learning techniques for food recognition and analysis in images, providing detailed nutritional information.

## 🎯 Features

- Food recognition from images
- Nutritional analysis of identified foods
- Integration with comprehensive nutritional databases

## 🗃️ Datasets

The following datasets are required to run this project:

1. **Food-101:**

   - Size: 5.33 GB
   - Content: 101,000 food images across 101 categories
   - [Download here](https://www.kaggle.com/datasets/dansbecker/food-101)

2. **Open Food Data (OFD):**

   - Size: 11.23 GB
   - Content: Comprehensive food products database
   - [Download here](https://fr.openfoodfacts.org/data)

3. **USDA Food Data Central:**
   - Size: 42.9 MB
   - Content: Detailed nutritional information
   - [Download here](https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_csv_2024-10-31.zip)

## 🛠️ Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/LuaGeo/guessmymeal
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment variables in the `.env` file

## �� Project Structure

guessmymeal/
├── data/ # Directory for dataset storage
├── docs/ # Project documentation
├── notebooks/ # Jupyter notebooks for analysis and experiments
├── results/ # Results and trained models
├── src/ # Source code
└── tests/ # Unit and integration tests
