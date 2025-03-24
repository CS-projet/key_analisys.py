import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model


class KeyAnalysis:
    model_path = "key_strength_model.h5"

    try:
        model = load_model(model_path)
        print(" Modèle IA chargé avec succès.")
    except Exception as e:
        print(f"️ Erreur lors du chargement du modèle IA: {e}")
        model = None

    @staticmethod
    def predict_key_strength(key_features: np.ndarray) -> float:
        if KeyAnalysis.model is None:
            raise ValueError(" Le modèle IA n'est pas chargé !")

        key_features = np.array(key_features).reshape(1, -1)
        prediction = KeyAnalysis.model.predict(key_features)[0, 0]

        return prediction

    @staticmethod
    def analyze_key(key: str) -> str:
        key_features = np.random.rand(10)
        score = KeyAnalysis.predict_key_strength(key_features)

        return " Clé FAIBLE" if score < 0.5 else " Clé SÉCURISÉE"


if __name__ == "__main__":
    test_key = "EXEMPLE_CLE"
    verdict = KeyAnalysis.analyze_key(test_key)
    print(f" Analyse de la clé : {verdict}")
