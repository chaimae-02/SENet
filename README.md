Transfer Learning – SENet for Sugarcane Leaf Disease Classification
📌 Projet

Ce projet met en œuvre une approche de Transfer Learning basée sur le modèle SENet pour la classification des maladies de la canne à sucre à partir d’images de feuilles. L’objectif est de détecter automatiquement les maladies et d’évaluer les performances du modèle à l’aide de métriques standards.

🔗 Dataset

Le dataset utilisé provient de Kaggle :
SENet Sugarcane Leaf Disease Dataset

Description : Le dataset contient des images de feuilles de canne à sucre classées selon différents types de maladies.

Prétraitement : Les images sont redimensionnées, normalisées et éventuellement augmentées pour améliorer la performance du modèle.

📂 Organisation du dépôt
├── README.md                   → Ce fichier
├── Rapport/                    
│   ├── Rapport_TransferLearning.pdf
│   └── Rapport_source.docx
├── Presentation/               
│   └── Presentation_TransferLearning.pdf
├── Code/                       
│   ├── data/                   → Données (ou liens de téléchargement)
│   ├── models/                 → Modèles pré-entraînés et scripts
│   ├── notebooks/              → Notebooks Jupyter d’expérimentation
│   ├── train.py                → Script d’entraînement principal
│   ├── evaluate.py             → Script d’évaluation et métriques
│   └── requirements.txt        → Dépendances Python
└── results/                    
    ├── confusion_matrix.png
    ├── roc_curve.png
    └── metrics_summary.csv

⚙️ Installation et utilisation

Cloner le dépôt :
https://github.com/chaimae-02/SENet.git
cd SENet

Installer les dépendances :

pip install -r Code/requirements.txt


Télécharger le dataset Kaggle et le placer dans Code/data/ (ou configurer le chemin dans le script train.py).

Entraîner le modèle :

python Code/train.py


Évaluer le modèle :

python Code/evaluate.py

🧪 Métriques d’évaluation

Les performances du modèle seront évaluées via :

Accuracy

Precision

Recall

F1-score

AUC / ROC curve

Confusion Matrix

📈 Résultats

Les résultats des simulations (graphes, matrices et métriques) seront sauvegardés dans le dossier results/.

✨ Points forts

Utilisation de Transfer Learning avec SENet pour tirer parti de modèles pré-entraînés.

Prétraitement et augmentation de données pour améliorer la généralisation.

Évaluation complète avec plusieurs métriques pour un diagnostic fiable.

📚 Références

Nirmal Sankalana. Sugarcane Leaf Disease Dataset
. Kaggle, 2023.

Hu, Jie, et al. "Squeeze-and-Excitation Networks." CVPR, 2018.
