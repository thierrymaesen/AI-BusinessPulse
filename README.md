<div align="center">

# 🧠 AI-BusinessPulse

### Plateforme d'Intelligence de Réputation d'Entreprise propulsée par l'IA

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with AI](https://img.shields.io/badge/Made%20with-AI%20%F0%9F%A4%96-purple.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

*Analysez vos avis clients, détectez les émotions, générez des réponses automatiques, comparez-vous à la concurrence et prédisez vos tendances de réputation — le tout propulsé par l'Intelligence Artificielle.*

[🚀 Démarrage Rapide](#-démarrage-rapide) • [📖 Fonctionnalités](#-5-fonctionnalités-originales) • [📸 Captures d'écran](#-captures-décran) • [🤝 Contribuer](#-contribuer)

---

</div>

## 🎯 Problème Résolu

Les entreprises reçoivent des **centaines d'avis clients** chaque mois sur **différentes plateformes** (Google, Trustpilot, Facebook, Yelp...). Gérer manuellement cette masse de retours est :

- ⏰ **Chronophage** : Lire et analyser chaque avis prend des heures
- - 😵 **Complexe** : Difficile de dégager des tendances à partir de données dispersées
  - - 💬 **Frustrant** : Répondre individuellement à chaque avis de manière professionnelle est épuisant
    - - 🔍 **Aveugle** : Impossible de se comparer objectivement aux concurrents
      - - 🔮 **Réactif** : Les entreprises réagissent aux problèmes au lieu de les anticiper
       
        - **AI-BusinessPulse** résout tous ces problèmes en une seule plateforme intelligente ! 🚀
       
        - ---

        ## ✨ 5 Fonctionnalités Originales

        ### 1. 📊 Agrégateur Multi-Sources d'Avis
        > *Centralisez tous vos avis clients en un seul tableau de bord*
        >
        > - Collecte les avis de **5 plateformes** : Google Reviews, Trustpilot, Facebook, Yelp, TripAdvisor
        > - - Dashboard interactif avec graphiques en temps réel
        >   - - Visualisation de la répartition par source (donut chart)
        >     - - Distribution des notes avec histogramme coloré
        >       - - Timeline du volume d'avis sur 12 mois
        >        
        >         - ### 2. 🎭 Analyse Profonde de Sentiment & Détection d'Émotions
        >         - > *Comprenez ce que ressentent vraiment vos clients*
        >           >
        >           > - Analyse de sentiment via **TextBlob NLP** (polarité -1 à +1)
        >           > - - Détection de **7 émotions** : Joie 😊, Colère 😠, Tristesse 😢, Peur 😨, Dégoût 🤢, Surprise 😲, Neutre 🤔
        >           >   - - Carte interactive des sentiments (scatter plot Polarité vs Subjectivité)
        >           >     - - **Zone de test en direct** : entrez n'importe quel texte et voyez l'analyse en temps réel !
        >           >      
        >           >       - ### 3. 💬 Générateur de Réponses Automatiques IA
        >           >       - > *Répondez professionnellement à chaque avis en un clic*
        >           >         >
        >           >         > - Génération de réponses **personnalisées** selon le sentiment détecté
        >           >         > - - Ton adapté : remerciement (positif), empathie + solution (négatif), encouragement (neutre)
        >           >         >   - - Inclut le nom du client et de l'entreprise automatiquement
        >           >         >     - - Boutons d'action : Approuver ✅, Modifier ✏️, Régénérer 🔄
        >           >         >       - - Priorisation des avis négatifs (réponse urgente)
        >           >         >        
        >           >         >         - ### 4. 🎯 Radar Concurrentiel de Réputation
        >           >         >         - > *Comparez-vous objectivement à vos concurrents*
        >           >         >           >
        >           >         >           > - **Spider chart** interactif sur 6 axes : Satisfaction, Réactivité, Qualité-Prix, Fidélité, Présence Online, Innovation
        >           >         >           > - - Concurrents générés automatiquement selon votre secteur d'activité
        >           >         >           >   - - Tableau comparatif avec gradient de couleurs (heatmap)
        >           >         >           >     - - Analyse IA de vos **forces** 🏆 et **faiblesses** ⚠️
        >           >         >           >      
        >           >         >           >       - ### 5. 🔮 Prédiction de Tendances de Réputation
        >           >         >           >       - > *Anticipez l'avenir de votre réputation*
        >           >         >           >         >
        >           >         >           >         > - **Régression linéaire** sur les données historiques
        >           >         >           >         > - - Prédiction sur **3 à 12 mois** (configurable via slider)
        >           >         >           >         >   - - Intervalle de confiance visualisé (zone ombrée)
        >           >         >           >         >     - - Indicateurs de tendance : 📈 Hausse, 📉 Baisse, ➡️ Stable
        >           >         >           >         >       - - **Recommandations IA personnalisées** selon la tendance détectée
        >           >         >           >         >        
        >           >         >           >         >         - ---
        >           >         >           >         >
        >           >         >           >         > ## 📸 Captures d'écran
        >           >         >           >         >
        >           >         >           >         > > L'interface est construite avec **Streamlit** et utilise un thème sombre professionnel avec des graphiques **Plotly** interactifs.
        >           >         >           >         > >
        >           >         >           >         > > ### Dashboard Principal
        >           >         >           >         > > ```
        >           >         >           >         > > ┌─────────────────────────────────────────────────┐
        >           >         >           >         > > │  🧠 AI-BusinessPulse                            │
        >           >         >           >         > > │  ⭐ 3.8/5  📝 200 avis  😊 55%  😟 25%  🌐 5   │
        >           >         >           >         > > ├─────────────────────────────────────────────────┤
        >           >         >           >         > > │  [Dashboard] [Sentiment] [Réponses] [Radar] [🔮]│
        >           >         >           >         > > ├──────────────────────┬──────────────────────────┤
        >           >         >           >         > > │   🌐 Répartition     │   ⭐ Distribution des    │
        >           >         >           >         > > │   des Sources        │   Notes (1-5 étoiles)    │
        >           >         >           >         > > │   ┌───────────┐      │   ┌──────────────────┐   │
        >           >         >           >         > > │   │  Donut    │      │   │  ████             │   │
        >           >         >           >         > > │   │  Chart    │      │   │  ██████           │   │
        >           >         >           >         > > │   └───────────┘      │   │  ████████████     │   │
        >           >         >           >         > > │                      │   └──────────────────┘   │
        >           >         >           >         > > ├──────────────────────┴──────────────────────────┤
        >           >         >           >         > > │   📅 Volume d'Avis par Mois                      │
        >           >         >           >         > > │   ┌─────────────────────────────────────────┐   │
        >           >         >           >         > > │   │  Area Chart Timeline                     │   │
        >           >         >           >         > > │   └─────────────────────────────────────────┘   │
        >           >         >           >         > > └─────────────────────────────────────────────────┘
        >           >         >           >         > > ```
        >           >         >           >         > >
        >           >         >           >         > > ### Radar Concurrentiel
        >           >         >           >         > > ```
        >           >         >           >         > > ┌─────────────────────────────────────────────────┐
        >           >         >           >         > > │  🎯 Radar Concurrentiel de Réputation           │
        >           >         >           >         > > │                                                  │
        >           >         >           >         > > │            Satisfaction                          │
        >           >         >           >         > > │               /\                                 │
        >           >         >           >         > > │        Innovation  Réactivité                    │
        >           >         >           >         > > │             |    \/    |                         │
        >           >         >           >         > > │       Présence  /\  Qualité-Prix                 │
        >           >         >           >         > > │               \/                                 │
        >           >         >           >         > > │            Fidélité                              │
        >           >         >           >         > > │                                                  │
        >           >         >           >         > > │  🏆 Point fort : Satisfaction (87/100)           │
        >           >         >           >         > > │  ⚠️ À améliorer : Innovation (62/100)            │
        >           >         >           >         > > └─────────────────────────────────────────────────┘
        >           >         >           >         > > ```
        >           >         >           >         > >
        >           >         >           >         > > ---
        >           >         >           >         > >
        >           >         >           >         > > ## 🚀 Démarrage Rapide
        >           >         >           >         > >
        >           >         >           >         > > ### Prérequis
        >           >         >           >         > >
        >           >         >           >         > > - **Python 3.9+** installé sur votre machine
        >           >         >           >         > > - - **pip** (gestionnaire de paquets Python)
        >           >         >           >         > >   - - **Git** pour cloner le repository
        >           >         >           >         > >    
        >           >         >           >         > >     - ### Installation en 3 étapes
        >           >         >           >         > >    
        >           >         >           >         > >     - ```bash
        >           >         >           >         > >       # 1. Cloner le repository
        >           >         >           >         > >       git clone https://github.com/thierrymaesen/AI-BusinessPulse.git
        >           >         >           >         > >       cd AI-BusinessPulse
        >           >         >           >         > >
        >           >         >           >         > >       # 2. Installer les dépendances
        >           >         >           >         > >       pip install -r requirements.txt
        >           >         >           >         > >
        >           >         >           >         > >       # 3. Lancer l'application
        >           >         >           >         > >       streamlit run app.py
        >           >         >           >         > >       ```
        >           >         >           >         > >
        >           >         >           >         > > L'application s'ouvre automatiquement dans votre navigateur à l'adresse : `http://localhost:8501`
        >           >         >           >         > >
        >           >         >           >         > > ### 🐳 Alternative avec Docker (optionnel)
        >           >         >           >         > >
        >           >         >           >         > > ```bash
        >           >         >           >         > > # Construire l'image Docker
        >           >         >           >         > > docker build -t ai-businesspulse .
        >           >         >           >         > >
        >           >         >           >         > > # Lancer le conteneur
        >           >         >           >         > > docker run -p 8501:8501 ai-businesspulse
        >           >         >           >         > > ```
        >           >         >           >         > >
        >           >         >           >         > > ---
        >           >         >           >         > >
        >           >         >           >         > > ## 🏗️ Structure du Projet
        >           >         >           >         > >
        >           >         >           >         > > ```
        >           >         >           >         > > AI-BusinessPulse/
        >           >         >           >         > > ├── 📄 app.py                # Application principale Streamlit (toutes les fonctionnalités)
        >           >         >           >         > > ├── 📄 requirements.txt      # Dépendances Python avec commentaires détaillés
        >           >         >           >         > > ├── 📄 README.md             # Documentation complète du projet
        >           >         >           >         > > ├── 📄 LICENSE               # Licence MIT
        >           >         >           >         > > ├── 📄 .gitignore            # Fichiers à ignorer (Python)
        >           >         >           >         > > └── 📁 .streamlit/
        >           >         >           >         > >     └── config.toml          # Configuration du thème Streamlit
        >           >         >           >         > > ```
        >           >         >           >         > >
        >           >         >           >         > > ---
        >           >         >           >         > >
        >           >         >           >         > > ## 🛠️ Technologies Utilisées
        >           >         >           >         > >
        >           >         >           >         > > | Technologie | Usage | Pourquoi ? |
        >           >         >           >         > > |-------------|-------|------------|
        >           >         >           >         > > | **Python 3.9+** | Langage principal | Écosystème IA/ML riche |
        >           >         >           >         > > | **Streamlit** | Interface web | Prototypage rapide, interactif |
        >           >         >           >         > > | **TextBlob** | Analyse de sentiment | NLP simple et efficace |
        >           >         >           >         > > | **Plotly** | Graphiques interactifs | Graphiques professionnels |
        >           >         >           >         > > | **Pandas** | Manipulation de données | Standard de l'industrie |
        >           >         >           >         > > | **NumPy** | Calculs numériques | Régression linéaire |
        >           >         >           >         > >
        >           >         >           >         > > ---
        >           >         >           >         > >
        >           >         >           >         > > ## 🧪 Comment Vérifier que ça Marche
        >           >         >           >         > >
        >           >         >           >         > > ### Test 1 : Analyse de Sentiment en Direct
        >           >         >           >         > > 1. Allez dans l'onglet **"🎭 Sentiment & Émotions"**
        >           >         >           >         > > 2. 2. Dans la zone **"Testez l'Analyse de Sentiment"**, tapez un avis positif : *"Service excellent, je suis ravi !"*
        >           >         >           >         > >    3. 3. Cliquez sur **"🔍 Analyser ce texte"**
        >           >         >           >         > >       4. 4. ✅ Vérifiez que la polarité est **positive** (> 0) et le label est **🟢 Positif**
        >           >         >           >         > >         
        >           >         >           >         > >          5. ### Test 2 : Génération de Réponses IA
        >           >         >           >         > >          6. 1. Allez dans l'onglet **"💬 Réponses IA"**
        >           >         >           >         > >             2. 2. Ouvrez un avis négatif (🔴)
        >           >         >           >         > >                3. 3. ✅ Vérifiez que la réponse générée contient de **l'empathie**, une **solution** et une **proposition de compensation**
        >           >         >           >         > >                  
        >           >         >           >         > >                   4. ### Test 3 : Radar Concurrentiel
        >           >         >           >         > >                   5. 1. Allez dans l'onglet **"🎯 Radar Concurrentiel"**
        >           >         >           >         > >                      2. 2. ✅ Vérifiez que le spider chart affiche votre entreprise et 3 concurrents
        >           >         >           >         > >                         3. 3. ✅ Vérifiez les forces/faiblesses en bas de page
        >           >         >           >         > >                           
        >           >         >           >         > >                            4. ### Test 4 : Prédictions
        >           >         >           >         > >                            5. 1. Allez dans l'onglet **"🔮 Prédictions"**
        >           >         >           >         > >                               2. 2. Déplacez le slider pour changer l'horizon de prédiction
        >           >         >           >         > >                                  3. 3. ✅ Vérifiez que la courbe de prédiction (pointillés rouges) prolonge les données historiques (bleu)
        >           >         >           >         > >                                    
        >           >         >           >         > >                                     4. ---
        >           >         >           >         > >                                    
        >           >         >           >         > >                                     5. ## 📈 Cas d'Usage pour les Entreprises
        >           >         >           >         > >                                    
        >           >         >           >         > >                                     6. | Secteur | Problème | Solution AI-BusinessPulse |
        > |---------|----------|--------------------------|
        > | **Restaurant** | 200+ avis/mois sur 5 plateformes | Dashboard centralisé + alertes |
        > | **E-commerce** | Taux de réponse aux avis < 30% | Réponses IA automatiques = 95% |
        > | **Hôtel** | Pas de vision concurrentielle | Radar 6 axes vs concurrents |
        > | **SaaS** | Churn imprévisible | Prédiction de tendance = anticipation |
        > | **Cabinet Médical** | Avis négatifs non traités | Détection d'émotions + priorité |
        >
        > ---
        >
        > ## 🤝 Contribuer
        >
        > Les contributions sont les bienvenues ! Voici comment participer :
        >
        > 1. **Fork** le projet
        > 2. 2. Créez votre branche (`git checkout -b feature/NouvelleFeature`)
        >    3. 3. Committez vos changements (`git commit -m 'Ajout NouvelleFeature'`)
        >       4. 4. Pushez sur la branche (`git push origin feature/NouvelleFeature`)
        >          5. 5. Ouvrez une **Pull Request**
        >            
        >             6. ### Idées de contributions
        >             7. - 🌍 Support multilingue (Anglais, Néerlandais, Allemand)
        >                - - 🔌 Intégration API Google Reviews / Trustpilot réelles
        >                  - - 📧 Alertes email automatiques pour avis négatifs
        >                    - - 📊 Export PDF des rapports
        >                      - - 🤖 Intégration GPT pour des réponses encore plus naturelles
        >                       
        >                        - ---
        >
        > ## 👨‍💻 Auteur
        >
        > **Thierry Maesen**
        > Consultant IA & Automatisation | n8n & Agents IA | WordPress
        >
        > - 🌐 [GitHub](https://github.com/thierrymaesen)
        > - - 📍 Belgique
        >  
        >   - ---
        >
        > ## 📄 Licence
        >
        > Ce projet est sous licence **MIT** — voir le fichier [LICENSE](LICENSE) pour plus de détails.
        >
        > ---
        >
        > <div align="center">

        **⭐ Si ce projet vous plaît, n'hésitez pas à lui donner une étoile !**

        *Fait avec ❤️ et 🧠 par Thierry Maesen*

        </div>
