# 📚 Cours Streamlit - Formation Interactive

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Ce dépôt contient un cours interactif complet pour apprendre Streamlit, une bibliothèque Python permettant de créer rapidement des applications web pour la science des données et le machine learning.

## ✨ À propos de Streamlit

Streamlit est un framework open source qui simplifie la création d'applications web interactives pour l'analyse et la visualisation de données. Avec quelques lignes de code Python, vous pouvez transformer vos scripts en applications web professionnelles. 
## 👨‍🏫 Auteur
**Abraham KOLOBOE**
* 📧 Email : <abklb27@gmail.com>
* 📱 WhatsApp : +229 91 83 84 21
* 💼 LinkedIn : [Abraham KOLOBOE](https://www.linkedin.com/in/abraham-zacharie-koloboe-data-science-ia-generative-llms-machine-learning)

## 📋 Contenu du Cours

Le cours est structuré en plusieurs sections progressives :

### 🏠 Home - Introduction Générale
- Présentation de Streamlit et ses avantages
- Vue d'ensemble des fonctionnalités
- Plan du cours détaillé
- Ressources utiles

### 👨🏽‍🏫 1. Introduction
- Installation de Streamlit
- Lancement de votre première application
- Configuration de l'environnement de développement

### 🚼 2. Fondamentaux
- Première application "Hello World"
- Affichage de texte (markdown, HTML)
- Widgets interactifs (boutons, sliders, inputs, etc.)
- Layouts et organisation (colonnes, containers, expanders)
- Formulaires et états de session

### 📊 3. Traitement et Visualisation des Données
- Chargement et upload de données
- Manipulation de DataFrames
- Métriques et KPIs
- Graphiques avec Matplotlib
- Visualisations interactives avec Plotly
- Cartographie avec st.map

### 🧐 4. Applications Avancées
- Applications multi-pages
- Gestion d'état avec session_state
- Barres de progression et spinners
- Configuration de pages
- Caching pour optimisation des performances
- Déploiement d'applications

## 🎯 Fonctionnalités Couvertes

Ce cours couvre les widgets et fonctionnalités Streamlit les plus récents :

- **Affichage** : st.write, st.markdown, st.title, st.header, st.subheader, st.text
- **Widgets** : st.button, st.checkbox, st.radio, st.selectbox, st.multiselect, st.slider, st.text_input, st.number_input, st.date_input, st.time_input
- **Formulaires** : st.form, st.form_submit_button
- **Données** : st.dataframe, st.table, st.metric
- **Graphiques** : st.line_chart, st.bar_chart, st.area_chart, st.scatter_chart, st.pyplot, st.plotly_chart
- **Médias** : st.image, st.audio, st.video
- **Layouts** : st.columns, st.tabs, st.expander, st.container, st.sidebar
- **État** : st.session_state
- **Performance** : st.cache_data, st.cache_resource
- **Contrôle** : st.progress, st.spinner, st.status
- **Upload** : st.file_uploader

## 📂 Structure du Projet

```
Cours-Streamlit/
├── 🏡Home.py                 # Page d'accueil principale
├── pages/                    # Pages de l'application multi-pages
│   ├── 1_👨🏽‍🏫_Introduction.py
│   ├── 2_🚼_Fondamentaux.py
│   ├── 3_📊_Traitement_et_Visualisation_des_données.py
│   └── 4_🧐_Applications_avancées.py
├── images/                   # Ressources images
├── requirements.txt          # Dépendances Python
└── README.md                # Ce fichier
```

## 🚀 Installation et Utilisation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation

1. **Clonez le dépôt** :
   ```bash
   git clone https://github.com/abrahamkoloboe27/Cours-Streamlit.git
   cd Cours-Streamlit
   ```

2. **Créez un environnement virtuel** (recommandé) :
   ```bash
   python -m venv venv
   
   # Sur Windows
   venv\Scripts\activate
   
   # Sur macOS/Linux
   source venv/bin/activate
   ```

3. **Installez les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

### Lancement de l'Application

Exécutez la commande suivante depuis le répertoire racine du projet :

```bash
streamlit run 🏡Home.py
```

L'application s'ouvrira automatiquement dans votre navigateur par défaut à l'adresse `http://localhost:8501`.

## 💡 Comment Utiliser ce Cours

1. **Navigation** : Utilisez le menu latéral pour naviguer entre les différentes sections
2. **Interactivité** : Testez tous les exemples de code interactifs
3. **Code Source** : Consultez le code des pages pour voir l'implémentation
4. **Pratique** : Modifiez le code et observez les résultats en temps réel

## 📚 Ressources Complémentaires

- 🌐 [Site officiel de Streamlit](https://streamlit.io/)
- 📖 [Documentation officielle](https://docs.streamlit.io/)
- ☁️ [Streamlit Cloud](https://streamlit.io/cloud) - Déploiement gratuit
- 🎨 [Galerie Streamlit](https://streamlit.io/gallery) - Exemples d'applications
- 💬 [Forum de la communauté](https://discuss.streamlit.io/)
- 🐙 [GitHub Streamlit](https://github.com/streamlit)
- 🎥 [Chaîne YouTube Streamlit](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)

## 🎓 Objectifs Pédagogiques

À la fin de ce cours, vous serez capable de :

- ✅ Créer des applications web interactives avec Streamlit
- ✅ Intégrer et visualiser des données efficacement
- ✅ Utiliser les widgets pour l'interactivité utilisateur
- ✅ Créer des applications multi-pages
- ✅ Gérer l'état de l'application avec session_state
- ✅ Optimiser les performances avec le caching
- ✅ Déployer vos applications en production

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commiter vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📝 License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🙏 Remerciements

- Merci à l'équipe Streamlit pour cet excellent framework
- Merci à la communauté Streamlit pour son support
- Merci à John R. AOGA pour sa contribution au cours

---

**⭐ Si ce cours vous a été utile, n'hésitez pas à lui donner une étoile sur GitHub !**

Pour plus d'informations, visitez le [dépôt GitHub](https://github.com/abrahamkoloboe27/Cours-Streamlit/).
