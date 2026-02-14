"""
============================================================
 AI-BusinessPulse - Plateforme d'Intelligence de Réputation
 ============================================================
  Auteur  : Thierry Maesen
   Version : 1.0.0
    Licence : MIT

      Description :
       Plateforme IA qui analyse les avis clients en temps réel,
        détecte les émotions, génère des réponses automatiques,
         compare la réputation avec les concurrents et prédit les
          tendances futures de satisfaction client.

            5 Fonctionnalités Originales :
             1. Multi-Source Review Aggregator (Agrégateur Multi-Sources)
              2. Deep Sentiment & Emotion AI (Analyse Profonde des Émotions)
               3. Smart Auto-Response Generator (Générateur de Réponses IA)
                4. Competitive Reputation Radar (Radar Concurrentiel)
                 5. Predictive Reputation Forecasting (Prédiction de Tendances)
                 ============================================================
                 """

# ============================================================
# IMPORTS - Bibliothèques nécessaires
# ============================================================
import streamlit as st          # Framework d'interface web
import pandas as pd             # Manipulation de données
import numpy as np              # Calculs numériques
import plotly.express as px     # Graphiques interactifs
import plotly.graph_objects as go  # Graphiques avancés
from textblob import TextBlob   # Analyse de sentiment NLP
from datetime import datetime, timedelta  # Gestion des dates
import random                   # Génération aléatoire
import json                     # Gestion JSON
from collections import Counter # Comptage d'éléments
import re                       # Expressions régulières

# ============================================================
# CONFIGURATION STREAMLIT - Paramètres de la page
# ============================================================
st.set_page_config(
        page_title="AI-BusinessPulse | Intelligence de Réputation",
        page_icon="🧠",
        layout="wide",                    # Utilise toute la largeur
        initial_sidebar_state="expanded"  # Barre latérale ouverte
)

# ============================================================
# CONSTANTES & CONFIGURATION GLOBALE
# ============================================================
# Liste des émotions détectables par notre IA
EMOTIONS = ["😊 Joie", "😠 Colère", "😢 Tristesse", "😨 Peur", 
                        "🤢 Dégoût", "😲 Surprise", "🤔 Neutre"]

# Couleurs associées à chaque émotion pour les graphiques
EMOTION_COLORS = {
        "😊 Joie": "#2ecc71", "😠 Colère": "#e74c3c", 
        "😢 Tristesse": "#3498db", "😨 Peur": "#9b59b6",
        "🤢 Dégoût": "#f39c12", "😲 Surprise": "#1abc9c", 
        "🤔 Neutre": "#95a5a6"
}

# Sources simulées d'avis clients
REVIEW_SOURCES = ["Google Reviews", "Trustpilot", "Facebook", 
                                    "Yelp", "TripAdvisor"]

# Catégories d'entreprises
BUSINESS_CATEGORIES = [
        "Restaurant", "Hôtel", "E-commerce", "SaaS / Tech",
        "Agence Marketing", "Cabinet Médical", "Salon de Coiffure"
]

# ============================================================
# CLASSE PRINCIPALE : BusinessPulseEngine
# ============================================================
# Cette classe contient toute la logique métier de l'application.
# Elle gère la génération de données de démo, l'analyse de 
# sentiment, la détection d'émotions, et les prédictions.
# ============================================================

class BusinessPulseEngine:
        """
            Moteur principal d'AI-BusinessPulse.

                    Cette classe orchestre les 5 fonctionnalités principales :
                        - Agrégation multi-sources des avis
                            - Analyse de sentiment et détection d'émotions
                                - Génération automatique de réponses
                                    - Benchmark concurrentiel
                                        - Prédiction de tendances de réputation
                                            """

    def __init__(self, business_name="Mon Entreprise", category="Restaurant"):
                """
                        Initialise le moteur avec le nom et la catégorie de l'entreprise.

                                        Args:
                                                    business_name (str): Nom de l'entreprise à analyser
                                                                category (str): Catégorie d'activité de l'entreprise
                                                                        """
                self.business_name = business_name
                self.category = category
                # Génère automatiquement des données de démonstration
                self.reviews = self._generate_demo_reviews()
        # Noms de concurrents générés selon la catégorie
        self.competitors = self._generate_competitors()

    # --------------------------------------------------------
    # FONCTIONNALITÉ 1 : Agrégateur Multi-Sources d'Avis
    # --------------------------------------------------------
    # Simule la collecte d'avis depuis différentes plateformes
    # (Google, Trustpilot, Facebook, Yelp, TripAdvisor)
    # En production, cette méthode se connecterait aux APIs réelles.
    # --------------------------------------------------------

    def _generate_demo_reviews(self):
                """
                        Génère un jeu de données réaliste de 200 avis clients.

                                        Chaque avis contient :
                                                - Le texte de l'avis (en français, réaliste)
                                                        - La source (plateforme d'origine)
                                                                - La note (1-5 étoiles)
                                                                        - La date de publication
                                                                                - Le nom du client

                                                                                                Returns:
                                                                                                            pd.DataFrame: DataFrame contenant tous les avis générés
                                                                                                                    """
                # Banque d'avis positifs réalistes en français
                positive_reviews = [
                                "Service impeccable ! L'équipe est très professionnelle et à l'écoute.",
                                "Excellent rapport qualité-prix, je recommande vivement à tous.",
                                "Expérience fantastique du début à la fin, bravo à toute l'équipe !",
                                "Je suis client depuis 3 ans et la qualité ne faiblit jamais.",
                                "Réponse rapide et solution efficace à mon problème. Top !",
                                "Un accueil chaleureux et un service personnalisé. Parfait !",
                                "Largement au-dessus de la concurrence en termes de qualité.",
                                "Très satisfait, c'est rare de trouver un tel niveau de service.",
                                "Innovation constante et écoute du client, c'est ce qui fait la différence.",
                                "Je recommande les yeux fermés, une entreprise d'exception !",
                                "Livraison rapide et produit conforme à la description. Très bien.",
                                "L'interface est intuitive et le support client réactif.",
                                "Qualité irréprochable, je suis un client fidèle désormais.",
                                "Service après-vente exceptionnel, problème résolu en 24h.",
                                "Ambiance agréable et personnel souriant. On reviendra !"
                ]

        # Banque d'avis négatifs réalistes en français
        negative_reviews = [
                        "Très déçu du service, temps d'attente beaucoup trop long.",
                        "Qualité en baisse depuis quelques mois, c'est vraiment dommage.",
                        "Service client inexistant, impossible de joindre quelqu'un.",
                        "Le produit ne correspond pas du tout à la description. Déception.",
                        "Prix trop élevés pour la qualité proposée. Je ne reviendrai pas.",
                        "Expérience catastrophique, aucun suivi après l'achat.",
                        "Erreur de commande non résolue après 3 relances. Inadmissible.",
                        "Personnel désagréable et peu professionnel. À éviter.",
                        "Problème récurrent jamais résolu malgré mes signalements.",
                        "Rapport qualité-prix catastrophique, je suis très mécontent."
        ]

        # Banque d'avis neutres/mitigés
        neutral_reviews = [
                        "Correct sans plus, rien d'exceptionnel mais pas mal non plus.",
                        "Service moyen, il y a du potentiel mais aussi des points à améliorer.",
                        "Première visite, impression mitigée. Je reviendrai pour confirmer.",
                        "Bon produit mais livraison un peu lente. Peut mieux faire.",
                        "Globalement satisfait mais quelques détails à revoir."
        ]

        # Prénoms réalistes pour les clients fictifs
        first_names = ["Marie", "Jean", "Sophie", "Pierre", "Isabelle",
                                              "Thomas", "Nathalie", "François", "Julie", "Laurent",
                                              "Céline", "Nicolas", "Émilie", "David", "Claire",
                                              "Marc", "Aurélie", "Philippe", "Camille", "Antoine"]

        reviews_data = []  # Liste pour stocker tous les avis

        # Génère 200 avis avec une distribution réaliste
        for i in range(200):
                        # Choix pondéré : 55% positif, 25% négatif, 20% neutre
                        sentiment_roll = random.random()
                        if sentiment_roll < 0.55:
                                            text = random.choice(positive_reviews)
                                            rating = random.choice([4, 5])      # Note 4-5 étoiles
elif sentiment_roll < 0.80:
                text = random.choice(negative_reviews)
                rating = random.choice([1, 2])      # Note 1-2 étoiles
else:
                text = random.choice(neutral_reviews)
                    rating = 3                           # Note 3 étoiles

            # Génère une date aléatoire sur les 12 derniers mois
            days_ago = random.randint(0, 365)
            review_date = datetime.now() - timedelta(days=days_ago)

            reviews_data.append({
                                "client": random.choice(first_names),
                                "text": text,
                                "rating": rating,
                                "source": random.choice(REVIEW_SOURCES),
                                "date": review_date.strftime("%Y-%m-%d"),
                                "emotion": None  # Sera rempli par l'analyse IA
            })

        return pd.DataFrame(reviews_data)

    def _generate_competitors(self):
                """
                        Génère une liste de concurrents fictifs selon la catégorie.

                                        Returns:
                                                    list: Liste de noms de concurrents fictifs
                                                            """
        # Dictionnaire de concurrents par catégorie d'entreprise
        competitors_db = {
                        "Restaurant": ["Le Bistrot Parisien", "La Table Dorée", "Chez Marcel"],
                        "Hôtel": ["Grand Hôtel Royal", "Suite & Spa Prestige", "L'Étoile Palace"],
                        "E-commerce": ["ShopExpress", "MegaStore Online", "QuickBuy Pro"],
                        "SaaS / Tech": ["CloudFlow", "DataSync Pro", "SmartPlatform"],
                        "Agence Marketing": ["DigitalBoost", "CreativeMinds", "GrowthFactory"],
                        "Cabinet Médical": ["MédiCenter Plus", "SantéPro Clinic", "VitaCare"],
                        "Salon de Coiffure": ["StyleMaster", "BeautyHair Pro", "CoiffÉlégance"]
        }
        return competitors_db.get(self.category, ["Concurrent A", "Concurrent B", "Concurrent C"])

    # --------------------------------------------------------
    # FONCTIONNALITÉ 2 : Analyse Profonde des Sentiments & Émotions
    # --------------------------------------------------------
    # Utilise TextBlob pour l'analyse de polarité et un système
    # de règles avancé pour la détection d'émotions spécifiques.
    # --------------------------------------------------------

    def analyze_sentiment(self, text):
                """
                        Analyse le sentiment d'un texte avec TextBlob.

                                        TextBlob attribue un score de polarité entre -1 (très négatif)
                                                et +1 (très positif). On convertit ce score en catégorie.

                                                                Args:
                                                                            text (str): Texte de l'avis à analyser

                                                                                                Returns:
                                                                                                            dict: Dictionnaire contenant polarité, subjectivité et label
                                                                                                                    """
        # Analyse avec TextBlob (fonctionne mieux en anglais,
        # mais donne des résultats utilisables en français)
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity        # -1 à +1
        subjectivity = analysis.sentiment.subjectivity # 0 à 1

        # Classification en catégorie de sentiment
        if polarity > 0.3:
                        label = "🟢 Positif"
elif polarity > 0.05:
            label = "🟡 Légèrement Positif"
elif polarity > -0.05:
            label = "⚪ Neutre"
elif polarity > -0.3:
            label = "🟠 Légèrement Négatif"
else:
            label = "🔴 Négatif"

        return {
                        "polarity": round(polarity, 3),
                        "subjectivity": round(subjectivity, 3),
                        "label": label
        }

    def detect_emotion(self, text, rating):
                """
                        Détecte l'émotion dominante dans un avis client.

                                        Combine l'analyse du texte (mots-clés émotionnels) avec
                                                la note attribuée pour une détection plus précise.

                                                                Args:
                                                                            text (str): Texte de l'avis
                                                                                        rating (int): Note de 1 à 5 étoiles
                                                                                                    
                                                                                                            Returns:
                                                                                                                        str: Émotion détectée (avec emoji)
                                                                                                                                """
        text_lower = text.lower()

        # Dictionnaire de mots-clés associés à chaque émotion
        emotion_keywords = {
                        "😊 Joie": ["excellent", "fantastique", "bravo", "parfait", 
                                                           "recommande", "exception", "top", "merci", "super"],
                        "😠 Colère": ["inadmissible", "catastrophique", "inacceptable",
                                                              "scandaleux", "honteux", "furieux", "révolté"],
                        "😢 Tristesse": ["déçu", "dommage", "triste", "regret", 
                                                                    "malheureusement", "déception", "décevant"],
                        "😨 Peur": ["inquiet", "peur", "angoisse", "danger", 
                                                          "risque", "méfiance", "crainte"],
                        "🤢 Dégoût": ["horrible", "dégueulasse", "immonde", 
                                                              "dégoûté", "répugnant", "éviter"],
                        "😲 Surprise": ["surprise", "inattendu", "étonnant", 
                                                                  "incroyable", "impressionnant", "wow"]
        }

        # Score d'émotion basé sur les mots-clés trouvés
        emotion_scores = {}
        for emotion, keywords in emotion_keywords.items():
                        score = sum(1 for kw in keywords if kw in text_lower)
                        emotion_scores[emotion] = score

        # Vérifie si une émotion a été détectée par mots-clés
        max_emotion = max(emotion_scores, key=emotion_scores.get)
        if emotion_scores[max_emotion] > 0:
                        return max_emotion

        # Si aucun mot-clé trouvé, se base sur la note
        if rating >= 4:
                        return "😊 Joie"
elif rating <= 2:
            return random.choice(["😠 Colère", "😢 Tristesse"])
else:
            return "🤔 Neutre"

    def analyze_all_reviews(self):
                """
                        Lance l'analyse de sentiment et la détection d'émotions
                                sur TOUS les avis du dataset.

                                                Enrichit le DataFrame self.reviews avec de nouvelles colonnes :
                                                        - sentiment_polarity : score de polarité (-1 à +1)
                                                                - sentiment_label : label de sentiment (Positif/Négatif/Neutre)
                                                                        - subjectivity : score de subjectivité (0 à 1)
                                                                                - emotion : émotion dominante détectée
                                                                                        """
        # Applique l'analyse de sentiment à chaque avis
        sentiments = self.reviews["text"].apply(self.analyze_sentiment)
        self.reviews["sentiment_polarity"] = sentiments.apply(lambda x: x["polarity"])
        self.reviews["sentiment_label"] = sentiments.apply(lambda x: x["label"])
        self.reviews["subjectivity"] = sentiments.apply(lambda x: x["subjectivity"])

        # Détecte l'émotion pour chaque avis
        self.reviews["emotion"] = self.reviews.apply(
                        lambda row: self.detect_emotion(row["text"], row["rating"]), axis=1
        )

    # --------------------------------------------------------
    # FONCTIONNALITÉ 3 : Générateur Automatique de Réponses IA
    # --------------------------------------------------------
    # Génère des réponses professionnelles et personnalisées
    # basées sur le sentiment détecté et le contenu de l'avis.
    # --------------------------------------------------------

    def generate_smart_response(self, review_text, sentiment_label, client_name):
                """
                        Génère une réponse professionnelle adaptée au sentiment de l'avis.

                                        Le système adapte le ton, le contenu et la structure de la réponse
                                                en fonction du sentiment détecté :
                                                        - Positif : remerciement + fidélisation
                                                                - Négatif : empathie + solution + compensation
                                                                        - Neutre  : reconnaissance + amélioration

                                                                                        Args:
                                                                                                    review_text (str): Texte original de l'avis client
                                                                                                                sentiment_label (str): Label de sentiment détecté
                                                                                                                            client_name (str): Prénom du client
                                                                                                                                        
                                                                                                                                                Returns:
                                                                                                                                                            str: Réponse professionnelle générée par l'IA
                                                                                                                                                                    """
        # Templates de réponses pour avis POSITIFS
        positive_templates = [
                        f"Cher(e) {client_name}, merci infiniment pour votre retour enthousiaste ! "
                        f"Votre satisfaction est notre plus belle récompense. Toute l'équipe de "
                        f"{self.business_name} est ravie de savoir que vous avez apprécié notre service. "
                        f"Au plaisir de vous revoir très bientôt ! 🌟",

                        f"Bonjour {client_name}, quel plaisir de lire votre avis ! "
                        f"Chez {self.business_name}, nous mettons tout en oeuvre pour offrir "
                        f"la meilleure expérience possible. Votre fidélité nous honore. "
                        f"À très bientôt ! 💫",

                        f"Merci beaucoup {client_name} ! Votre retour positif motive toute "
                        f"notre équipe à continuer d'innover et d'exceller. "
                        f"Nous avons hâte de vous accueillir à nouveau chez {self.business_name} ! 🙏"
        ]

        # Templates de réponses pour avis NÉGATIFS
        negative_templates = [
                        f"Cher(e) {client_name}, nous sommes sincèrement désolés pour cette "
                        f"expérience décevante. Ce n'est pas le standard de qualité que nous "
                        f"visons chez {self.business_name}. Nous souhaitons comprendre ce qui "
                        f"s'est passé et y remédier. Pourriez-vous nous contacter directement "
                        f"à support@{self.business_name.lower().replace(' ', '')}.com ? "
                        f"Nous vous offrirons une compensation adaptée. 🤝",

                        f"Bonjour {client_name}, merci d'avoir pris le temps de partager votre "
                        f"expérience. Nous prenons votre retour très au sérieux. Notre responsable "
                        f"qualité va étudier votre cas personnellement. Nous nous engageons à "
                        f"faire mieux et espérons regagner votre confiance. 💪",

                        f"{client_name}, nous comprenons votre frustration et nous vous présentons "
                        f"nos excuses les plus sincères. Votre avis est crucial pour nous améliorer. "
                        f"Notre équipe travaille déjà sur les points que vous avez soulevés. "
                        f"Nous serions honorés de vous offrir une seconde chance. 🙏"
        ]

        # Templates de réponses pour avis NEUTRES
        neutral_templates = [
                        f"Bonjour {client_name}, merci pour votre retour honnête. "
                        f"Nous apprécions votre franchise et prenons note de vos observations. "
                        f"Chez {self.business_name}, chaque avis est une opportunité d'amélioration. "
                        f"Nous espérons vous surprendre positivement lors de votre prochaine visite ! 😊",

                        f"Merci {client_name} pour ce retour constructif. Nous travaillons "
                        f"constamment à améliorer notre service. Vos suggestions sont précieuses "
                        f"et seront prises en compte. À bientôt chez {self.business_name} ! 🔄"
        ]

        # Sélection du template selon le sentiment
        if "Positif" in sentiment_label:
                        return random.choice(positive_templates)
elif "Négatif" in sentiment_label:
            return random.choice(negative_templates)
else:
            return random.choice(neutral_templates)

    # --------------------------------------------------------
    # FONCTIONNALITÉ 4 : Radar Concurrentiel de Réputation
    # --------------------------------------------------------
    # Compare les métriques de réputation de l'entreprise avec
    # ses concurrents sur plusieurs axes d'évaluation.
    # --------------------------------------------------------

    def generate_competitive_benchmark(self):
                """
                        Génère un benchmark comparatif avec les concurrents.

                                        Évalue 6 axes stratégiques :
                                                - Satisfaction globale
                                                        - Réactivité du service
                                                                - Rapport qualité-prix
                                                                        - Fidélité client
                                                                                - Présence en ligne
                                                                                        - Innovation

                                                                                                        Returns:
                                                                                                                    dict: Scores par entreprise et par axe d'évaluation
                                                                                                                            """
        # Les 6 axes d'évaluation stratégique
        axes = ["Satisfaction", "Réactivité", "Qualité-Prix", 
                                "Fidélité", "Présence Online", "Innovation"]

        benchmark_data = {}

        # Score de l'entreprise principale (basé sur les avis analysés)
        avg_rating = self.reviews["rating"].mean()
        # Normalisation du score moyen sur une échelle 0-100
        base_score = (avg_rating / 5) * 100

        # Génère les scores de l'entreprise avec une variation réaliste
        benchmark_data[self.business_name] = [
                        min(100, max(20, base_score + random.uniform(-10, 15)))
                        for _ in axes
        ]

        # Génère les scores des concurrents (légèrement inférieurs)
        for competitor in self.competitors:
                        benchmark_data[competitor] = [
                                            min(100, max(20, base_score + random.uniform(-25, 10)))
                                            for _ in axes
                        ]

        return {"axes": axes, "data": benchmark_data}

    # --------------------------------------------------------
    # FONCTIONNALITÉ 5 : Prédiction de Tendances de Réputation
    # --------------------------------------------------------
    # Analyse l'évolution temporelle des avis pour prédire
    # la tendance future de la satisfaction client.
    # --------------------------------------------------------

    def predict_reputation_trend(self, months_ahead=6):
                """
                        Prédit l'évolution de la réputation sur les prochains mois.

                                        Utilise une régression linéaire simple sur les données 
                                                historiques pour projeter la tendance future.

                                                                Algorithme :
                                                                        1. Calcule la moyenne mensuelle des notes passées
                                                                                2. Applique une régression linéaire
                                                                                        3. Projette la tendance sur N mois
                                                                                                4. Ajoute un intervalle de confiance
                                                                                                        
                                                                                                                Args:
                                                                                                                            months_ahead (int): Nombre de mois à prédire (défaut: 6)
                                                                                                                                        
                                                                                                                                                Returns:
                                                                                                                                                            dict: Données historiques et prédictions avec intervalles
                                                                                                                                                                    """
        # Conversion de la colonne date en format datetime
        self.reviews["date_dt"] = pd.to_datetime(self.reviews["date"])

        # Calcul de la moyenne mensuelle des notes
        monthly = self.reviews.set_index("date_dt").resample("M")["rating"].mean()
        monthly = monthly.dropna()

        # Préparation des données pour la régression
        x_values = np.arange(len(monthly))           # Index numérique
        y_values = monthly.values                     # Notes moyennes

        # Régression linéaire simple (y = ax + b)
        if len(x_values) > 1:
                        coefficients = np.polyfit(x_values, y_values, 1)  # Degré 1
            slope = coefficients[0]      # Pente de la tendance
            intercept = coefficients[1]  # Ordonnée à l'origine
else:
            slope = 0
            intercept = y_values[0] if len(y_values) > 0 else 3.5

        # Génération des prédictions futures
        future_x = np.arange(len(monthly), len(monthly) + months_ahead)
        predictions = slope * future_x + intercept

        # Bornage des prédictions entre 1 et 5
        predictions = np.clip(predictions, 1.0, 5.0)

        # Calcul de l'intervalle de confiance (± écart-type)
        std_dev = np.std(y_values) if len(y_values) > 1 else 0.3
        confidence_upper = np.clip(predictions + std_dev, 1.0, 5.0)
        confidence_lower = np.clip(predictions - std_dev, 1.0, 5.0)

        # Génération des dates futures
        last_date = monthly.index[-1] if len(monthly) > 0 else datetime.now()
        future_dates = [
                        last_date + timedelta(days=30 * (i + 1)) 
                        for i in range(months_ahead)
        ]

        return {
                        "historical_dates": monthly.index.tolist(),
                        "historical_values": y_values.tolist(),
                        "predicted_dates": future_dates,
                        "predicted_values": predictions.tolist(),
                        "confidence_upper": confidence_upper.tolist(),
                        "confidence_lower": confidence_lower.tolist(),
                        "trend": "📈 Hausse" if slope > 0.01 else ("📉 Baisse" if slope < -0.01 else "➡️ Stable"),
                        "slope": round(slope, 4)
        }


# ============================================================
# INTERFACE STREAMLIT - Affichage et Interaction
# ============================================================
# Cette section construit l'interface utilisateur avec Streamlit.
# Chaque onglet correspond à une fonctionnalité du projet.
# ============================================================

def main():
        """
            Fonction principale qui construit l'interface Streamlit.

                    Structure de l'interface :
                        - Barre latérale : Configuration de l'entreprise
                            - Onglet 1 : Dashboard & Agrégation d'avis
                                - Onglet 2 : Analyse de Sentiment & Émotions
                                    - Onglet 3 : Générateur de Réponses IA
                                        - Onglet 4 : Radar Concurrentiel
                                            - Onglet 5 : Prédictions de Tendances
                                                """

    # ---- EN-TÊTE DE L'APPLICATION ----
    st.markdown("""
        <div style='text-align: center; padding: 1rem;'>
                <h1>🧠 AI-BusinessPulse</h1>
                        <p style='font-size: 1.2rem; color: #888;'>
                                    Plateforme d'Intelligence de Réputation propulsée par l'IA
                                            </p>
                                                    <hr style='border: 1px solid #333;'>
                                                        </div>
                                                            """, unsafe_allow_html=True)

    # ---- BARRE LATÉRALE : CONFIGURATION ----
    with st.sidebar:
                st.image("https://img.icons8.com/fluency/96/brain.png", width=80)
        st.title("⚙️ Configuration")
        st.markdown("---")

        # Champ de saisie pour le nom de l'entreprise
        business_name = st.text_input(
                        "🏢 Nom de votre entreprise",
                        value="TeamOne Be",
                        help="Entrez le nom de votre entreprise à analyser"
        )

        # Sélection de la catégorie d'activité
        category = st.selectbox(
                        "📂 Catégorie d'activité",
                        BUSINESS_CATEGORIES,
                        help="Sélectionnez votre secteur d'activité"
        )

        st.markdown("---")

        # Bouton pour lancer l'analyse
        analyze_btn = st.button(
                        "🚀 Lancer l'Analyse Complète",
                        use_container_width=True,
                        type="primary"
        )

        st.markdown("---")
        st.markdown("### 📊 Statistiques Rapides")
        st.info("Cliquez sur 'Lancer l'Analyse' pour voir les résultats")

    # ---- INITIALISATION DU MOTEUR ----
    # Utilise le cache Streamlit pour éviter de recalculer à chaque refresh
    if "engine" not in st.session_state or analyze_btn:
                engine = BusinessPulseEngine(business_name, category)
        engine.analyze_all_reviews()
        st.session_state.engine = engine

    engine = st.session_state.engine

    # ---- MÉTRIQUES CLÉS (EN HAUT DE PAGE) ----
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
                avg_rating = engine.reviews["rating"].mean()
        st.metric("⭐ Note Moyenne", f"{avg_rating:.1f}/5",
                                    delta=f"+{random.uniform(0.1, 0.3):.1f} vs mois dernier")
    with col2:
                total_reviews = len(engine.reviews)
        st.metric("📝 Total Avis", total_reviews,
                                    delta=f"+{random.randint(5, 20)} nouveaux")
    with col3:
                positive_pct = len(engine.reviews[engine.reviews["rating"] >= 4]) / total_reviews * 100
        st.metric("😊 Avis Positifs", f"{positive_pct:.0f}%")
    with col4:
                negative_pct = len(engine.reviews[engine.reviews["rating"] <= 2]) / total_reviews * 100
        st.metric("😟 Avis Négatifs", f"{negative_pct:.0f}%")
    with col5:
                sources_count = engine.reviews["source"].nunique()
        st.metric("🌐 Sources", f"{sources_count} plateformes")

    # ---- ONGLETS PRINCIPAUX ----
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
                "📊 Dashboard & Avis",
                "🎭 Sentiment & Émotions", 
                "💬 Réponses IA",
                "🎯 Radar Concurrentiel",
                "🔮 Prédictions"
    ])

    # ============================================================
    # ONGLET 1 : Dashboard & Agrégation Multi-Sources
    # ============================================================
    with tab1:
                st.header("📊 Dashboard - Agrégation Multi-Sources")
        st.markdown("Vue d'ensemble de tous vos avis clients provenant de différentes plateformes.")

        # Graphique : Distribution des avis par source
        col_a, col_b = st.columns(2)

        with col_a:
                        # Camembert de la répartition par source
                        source_counts = engine.reviews["source"].value_counts()
                        fig_sources = px.pie(
                            values=source_counts.values,
                            names=source_counts.index,
                            title="🌐 Répartition des Avis par Source",
                            color_discrete_sequence=px.colors.qualitative.Set3,
                            hole=0.4  # Donut chart
                        )
                        fig_sources.update_layout(template="plotly_dark")
                        st.plotly_chart(fig_sources, use_container_width=True)

        with col_b:
                        # Histogramme des notes
                        fig_ratings = px.histogram(
                                            engine.reviews, x="rating",
                                            title="⭐ Distribution des Notes (1-5 étoiles)",
                                            color="rating",
                                            color_discrete_sequence=["#e74c3c", "#e67e22", "#f1c40f", "#2ecc71", "#27ae60"],
                                            nbins=5
                        )
                        fig_ratings.update_layout(template="plotly_dark", showlegend=False)
                        st.plotly_chart(fig_ratings, use_container_width=True)

        # Évolution temporelle des avis
        reviews_timeline = engine.reviews.copy()
        reviews_timeline["date"] = pd.to_datetime(reviews_timeline["date"])
        reviews_timeline = reviews_timeline.sort_values("date")
        monthly_counts = reviews_timeline.set_index("date").resample("M").size()

        fig_timeline = px.area(
                        x=monthly_counts.index, y=monthly_counts.values,
                        title="📅 Volume d'Avis par Mois (12 derniers mois)",
                        labels={"x": "Date", "y": "Nombre d'avis"}
        )
        fig_timeline.update_layout(template="plotly_dark")
        st.plotly_chart(fig_timeline, use_container_width=True)

        # Tableau détaillé des derniers avis
        st.subheader("📋 Derniers Avis Reçus")
        st.dataframe(
                        engine.reviews[["client", "text", "rating", "source", "date", "emotion"]]
                        .sort_values("date", ascending=False)
                        .head(20),
                        use_container_width=True,
                        height=400
        )

    # ============================================================
    # ONGLET 2 : Analyse de Sentiment & Détection d'Émotions
    # ============================================================
    with tab2:
                st.header("🎭 Analyse de Sentiment & Détection d'Émotions")
        st.markdown("Notre IA analyse chaque avis pour détecter le sentiment et l'émotion dominante.")

        col_s1, col_s2 = st.columns(2)

        with col_s1:
                        # Graphique des émotions détectées
                        emotion_counts = engine.reviews["emotion"].value_counts()
                        fig_emotions = px.bar(
                            x=emotion_counts.index, y=emotion_counts.values,
                            title="🎭 Émotions Détectées dans les Avis",
                            labels={"x": "Émotion", "y": "Nombre d'avis"},
                            color=emotion_counts.index,
                            color_discrete_map=EMOTION_COLORS
                        )
                        fig_emotions.update_layout(template="plotly_dark", showlegend=False)
                        st.plotly_chart(fig_emotions, use_container_width=True)

        with col_s2:
                        # Graphique de la distribution des sentiments
                        sentiment_counts = engine.reviews["sentiment_label"].value_counts()
                        fig_sentiment = px.pie(
                            values=sentiment_counts.values,
                            names=sentiment_counts.index,
                            title="🔍 Distribution des Sentiments",
                            color_discrete_sequence=["#2ecc71", "#27ae60", "#95a5a6", "#e67e22", "#e74c3c"]
                        )
                        fig_sentiment.update_layout(template="plotly_dark")
                        st.plotly_chart(fig_sentiment, use_container_width=True)

        # Scatter plot : Polarité vs Subjectivité
        fig_scatter = px.scatter(
                        engine.reviews, x="sentiment_polarity", y="subjectivity",
                        color="emotion", size="rating",
                        title="🔬 Carte des Sentiments (Polarité vs Subjectivité)",
                        labels={"sentiment_polarity": "Polarité (-1 à +1)", 
                                                    "subjectivity": "Subjectivité (0 à 1)"},
                        hover_data=["client", "text"]
        )
        fig_scatter.update_layout(template="plotly_dark")
        st.plotly_chart(fig_scatter, use_container_width=True)

        # Test interactif de sentiment
        st.subheader("🧪 Testez l'Analyse de Sentiment en Direct")
        test_text = st.text_area(
                        "Entrez un avis à analyser :",
                        value="Le service était vraiment excellent, je suis très satisfait de mon expérience !",
                        height=100
        )
        if st.button("🔍 Analyser ce texte"):
                        result = engine.analyze_sentiment(test_text)
                        col_r1, col_r2, col_r3 = st.columns(3)
                        with col_r1:
                                            st.metric("Polarité", f"{result['polarity']:.3f}")
                                        with col_r2:
                            st.metric("Subjectivité", f"{result['subjectivity']:.3f}")
                                                        with col_r3:
                                                            st.metric("Sentiment", result["label"])

    # ============================================================
    # ONGLET 3 : Générateur de Réponses IA
    # ============================================================
    with tab3:
                st.header("💬 Générateur de Réponses Automatiques IA")
        st.markdown("L'IA génère des réponses personnalisées et professionnelles pour chaque avis client.")

        # Sélection d'avis à répondre
        st.subheader("📬 Avis en attente de réponse")

        # Filtre les avis négatifs en priorité (ceux qui nécessitent une réponse urgente)
        negative_reviews = engine.reviews[engine.reviews["rating"] <= 2].head(5)
        positive_reviews_sample = engine.reviews[engine.reviews["rating"] >= 4].head(3)
        priority_reviews = pd.concat([negative_reviews, positive_reviews_sample])

        for idx, row in priority_reviews.iterrows():
                        # Affiche chaque avis dans une carte expandable
                        with st.expander(
                                            f"{'🔴' if row['rating'] <= 2 else '🟢'} {row['client']} - "
                                            f"{'⭐' * row['rating']} - {row['source']}"
                        ):
                                            st.markdown(f"**Avis :** {row['text']}")
                                            st.markdown(f"**Date :** {row['date']} | **Émotion :** {row['emotion']}")

                # Génère et affiche la réponse IA
                response = engine.generate_smart_response(
                                        row["text"], row.get("sentiment_label", "Neutre"), row["client"]
                )
                st.markdown("---")
                st.markdown("**🤖 Réponse générée par l'IA :**")
                st.success(response)

                # Boutons d'action
                col_btn1, col_btn2, col_btn3 = st.columns(3)
                with col_btn1:
                                        st.button(f"✅ Approuver", key=f"approve_{idx}")
                                    with col_btn2:
                                                            st.button(f"✏️ Modifier", key=f"edit_{idx}")
                                                        with col_btn3:
                                                                                st.button(f"🔄 Régénérer", key=f"regen_{idx}")

        # Statistiques des réponses
        st.markdown("---")
        st.subheader("📊 Statistiques de Réponse")
        col_stat1, col_stat2, col_stat3 = st.columns(3)
        with col_stat1:
                        st.metric("Taux de réponse", "94%", delta="+5%")
        with col_stat2:
                        st.metric("Temps moyen de réponse", "2.3h", delta="-1.2h")
        with col_stat3:
                        st.metric("Satisfaction post-réponse", "87%", delta="+12%")

    # ============================================================
    # ONGLET 4 : Radar Concurrentiel
    # ============================================================
    with tab4:
                st.header("🎯 Radar Concurrentiel de Réputation")
        st.markdown("Comparez votre réputation avec vos concurrents sur 6 axes stratégiques.")

        # Génère les données de benchmark
        benchmark = engine.generate_competitive_benchmark()

        # Création du graphique radar (spider chart)
        fig_radar = go.Figure()

        # Couleurs pour chaque entreprise
        colors = ["#3498db", "#e74c3c", "#2ecc71", "#f39c12"]

        for i, (company, scores) in enumerate(benchmark["data"].items()):
                        fig_radar.add_trace(go.Scatterpolar(
                                            r=scores + [scores[0]],  # Ferme le polygone
                                            theta=benchmark["axes"] + [benchmark["axes"][0]],
                                            fill="toself",
                                            name=company,
                                            line_color=colors[i % len(colors)],
                                            opacity=0.7
                        ))

        fig_radar.update_layout(
                        polar=dict(
                                            radialaxis=dict(visible=True, range=[0, 100]),
                                            bgcolor="rgba(0,0,0,0)"
                        ),
                        title="🎯 Radar Comparatif Multi-Axes",
                        template="plotly_dark",
                        showlegend=True,
                        height=500
        )
        st.plotly_chart(fig_radar, use_container_width=True)

        # Tableau comparatif détaillé
        st.subheader("📊 Tableau Comparatif Détaillé")
        comparison_df = pd.DataFrame(benchmark["data"], index=benchmark["axes"])
        comparison_df = comparison_df.round(1)

        # Colore les cellules selon les scores
        st.dataframe(
                        comparison_df.style.background_gradient(cmap="RdYlGn", axis=None),
                        use_container_width=True
        )

        # Analyse des forces et faiblesses
        st.subheader("💡 Analyse IA - Forces & Faiblesses")
        own_scores = benchmark["data"][engine.business_name]
        best_axis = benchmark["axes"][own_scores.index(max(own_scores))]
        worst_axis = benchmark["axes"][own_scores.index(min(own_scores))]

        col_fw1, col_fw2 = st.columns(2)
        with col_fw1:
                        st.success(f"🏆 **Votre point fort** : {best_axis} ({max(own_scores):.0f}/100)")
        with col_fw2:
                        st.warning(f"⚠️ **À améliorer** : {worst_axis} ({min(own_scores):.0f}/100)")

    # ============================================================
    # ONGLET 5 : Prédictions de Tendances
    # ============================================================
    with tab5:
                st.header("🔮 Prédiction de Tendances de Réputation")
        st.markdown("Notre IA prédit l'évolution de votre réputation sur les prochains mois.")

        # Slider pour choisir l'horizon de prédiction
        months = st.slider("Horizon de prédiction (mois)", 3, 12, 6)

        # Calcul des prédictions
        predictions = engine.predict_reputation_trend(months_ahead=months)

        # Graphique de prédiction avec intervalle de confiance
        fig_pred = go.Figure()

        # Données historiques
        fig_pred.add_trace(go.Scatter(
                        x=predictions["historical_dates"],
                        y=predictions["historical_values"],
                        mode="lines+markers",
                        name="📊 Historique",
                        line=dict(color="#3498db", width=3),
                        marker=dict(size=8)
        ))

        # Prédictions
        fig_pred.add_trace(go.Scatter(
                        x=predictions["predicted_dates"],
                        y=predictions["predicted_values"],
                        mode="lines+markers",
                        name="🔮 Prédiction",
                        line=dict(color="#e74c3c", width=3, dash="dash"),
                        marker=dict(size=8, symbol="diamond")
        ))

        # Intervalle de confiance (zone ombrée)
        fig_pred.add_trace(go.Scatter(
                        x=predictions["predicted_dates"] + predictions["predicted_dates"][::-1],
                        y=predictions["confidence_upper"] + predictions["confidence_lower"][::-1],
                        fill="toself",
                        fillcolor="rgba(231, 76, 60, 0.15)",
                        line=dict(color="rgba(255,255,255,0)"),
                        name="📐 Intervalle de confiance"
        ))

        fig_pred.update_layout(
                        title="🔮 Évolution & Prédiction de la Note Moyenne",
                        xaxis_title="Date",
                        yaxis_title="Note Moyenne (1-5)",
                        yaxis=dict(range=[1, 5]),
                        template="plotly_dark",
                        height=500
        )
        st.plotly_chart(fig_pred, use_container_width=True)

        # Indicateurs de tendance
        col_t1, col_t2, col_t3 = st.columns(3)
        with col_t1:
                        st.metric("📈 Tendance Globale", predictions["trend"])
        with col_t2:
                        if predictions["predicted_values"]:
                                            st.metric("🎯 Note Prédite (fin)", 
                                                                               f"{predictions['predicted_values'][-1]:.2f}/5")
                                    with col_t3:
                                                    st.metric("📊 Pente de tendance", 
                                                                                   f"{predictions['slope']:+.4f}/mois")

        # Recommandations IA
        st.subheader("💡 Recommandations IA pour Améliorer votre Réputation")

        if predictions["slope"] < -0.01:
                        st.error("⚠️ **Attention : Tendance à la baisse détectée !**")
            st.markdown("""
                        **Actions recommandées par l'IA :**
                                    - 🔍 Analyser les avis négatifs récents pour identifier les problèmes récurrents
                                                - 💬 Répondre rapidement à tous les avis négatifs avec empathie
                                                            - 🎯 Lancer une enquête de satisfaction auprès de vos clients fidèles
                                                                        - 🔧 Mettre en place un plan d'action qualité immédiat
                                                                                    """)
elif predictions["slope"] > 0.01:
            st.success("🎉 **Excellente nouvelle : Tendance à la hausse !**")
            st.markdown("""
                        **Conseils pour maintenir la dynamique :**
                                    - ⭐ Continuez à solliciter des avis de vos clients satisfaits
                                                - 🏆 Capitalisez sur vos points forts identifiés
                                                            - 🚀 Investissez dans l'innovation pour creuser l'écart avec la concurrence
                                                                        - 📱 Renforcez votre présence sur les plateformes d'avis
                                                                                    """)
else:
            st.info("➡️ **Réputation stable - Opportunité de croissance**")
            st.markdown("""
                        **Suggestions pour passer au niveau supérieur :**
                                    - 💡 Identifiez un axe différenciateur par rapport aux concurrents
                                                - 📊 Fixez des objectifs mesurables d'amélioration de satisfaction
                                                            - 🤝 Développez un programme de fidélité pour récompenser vos ambassadeurs
                                                                        - 🎓 Formez vos équipes aux meilleures pratiques du service client
                                                                                    """)

    # ---- PIED DE PAGE ----
    st.markdown("---")
    st.markdown(
                "<div style='text-align: center; color: #888; padding: 1rem;'>"
                "🧠 AI-BusinessPulse v1.0 | Développé par Thierry Maesen | "
                "<a href='https://github.com/thierrymaesen/AI-BusinessPulse'>GitHub</a>"
                "</div>",
                unsafe_allow_html=True
    )


# ============================================================
# POINT D'ENTRÉE DE L'APPLICATION
# ============================================================
if __name__ == "__main__":
        main()
