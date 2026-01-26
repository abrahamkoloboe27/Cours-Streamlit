import streamlit as st
st.set_page_config(
    page_title="🧐 Applications avancées",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("🧐 Applications avancées")
with st.sidebar : 
    st.markdown("""
    ## Auteurs
    John R. AOGA
    * Linkedin : [John AOGA](https://www.linkedin.com/in/john-aoga-2ba6a862/)
                
""")
with st.sidebar : 
        st.markdown("""
        ## Auteur
        :blue[Abraham KOLOBOE]
        * Email : <abklb27@gmail.com>
        * WhatsApp : +229 91 83 84 21
        * Linkedin : [Abraham KOLOBOE](https://www.linkedin.com/in/abraham-zacharie-koloboe-data-science-ia-generative-llms-machine-learning)
                    """)
tab1 , tab2 , tab3, tab4, tab5, tab6, tab7 = st.tabs(["Applications multi-pages", "Session state", 
                              "Barre de progression", "Spinner", "Configuration de pages", 
                              "Cache et Performance", "Déploiement"])


with tab1 : 
    st.markdown("""
    Pour créer une application multi-pages, il vous faut creér dans le dossier racine de votre application, 
    un sous-dossier **:blue[pages]** et y créer un fichier **:red[.py]** pour chacune des pages de votre application
                """)
    with st.expander("**Utilisation**", True) : 
        st.image("images/mp.png")
        st.image("images/mp_2.png")

with tab2 : 
    st.markdown("""
        `st.session_state` est une fonctionnalité de Streamlit, une bibliothèque Python pour créer des 
                applications web de manière simple. Elle permet de stocker et de récupérer des informations 
                spécifiques à une session utilisateur, permettant ainsi de conserver des variables entre différentes 
                fonctions tout au long de la session.

        **Utilité :**

        L'utilité principale de `st.session_state` réside dans la possibilité de 
                maintenir un état persistant pendant toute la durée d'une session utilisateur. 
                Cela élimine le besoin d'utiliser des variables globales pour stocker des informations entre 
                les différentes parties de votre application Streamlit.

        **Exemple avec du code :**

        Imaginons un exemple simple où nous voulons maintenir un compteur qui s'incrémente à chaque 
                fois qu'un utilisateur interagit avec l'application. Voici comment vous pourriez utiliser
                `st.session_state` pour atteindre cela :
        """)
    with st.expander("Utilisation ", True):
        # Initialiser l'état de la session
        if 'compteur' not in st.session_state:
            st.session_state.compteur = 0

        # Fonction pour incrémenter le compteur
        def incrementer_compteur():
            st.session_state.compteur += 1

        # Afficher le bouton pour incrémenter le compteur
        if st.button('Incrémenter le compteur'):
            incrementer_compteur()

        # Afficher la valeur actuelle du compteur
        st.write('Compteur :', st.session_state.compteur)

    st.markdown("""
        ```python
        import streamlit as st

        # Initialiser l'état de la session
        if 'compteur' not in st.session_state:
            st.session_state.compteur = 0

        # Fonction pour incrémenter le compteur
        def incrementer_compteur():
            st.session_state.compteur += 1

        # Afficher le bouton pour incrémenter le compteur
        if st.button('Incrémenter le compteur'):
            incrementer_compteur()

        # Afficher la valeur actuelle du compteur
        st.write('Compteur :', st.session_state.compteur)
        ```

        Dans cet exemple :
        - Nous initialisons le compteur dans la session à 0 s'il n'est pas déjà présent.
        - Nous définissons une fonction `incrementer_compteur` qui incrémente le compteur.
        - Nous utilisons un bouton dans l'interface utilisateur pour permettre à 
        l'utilisateur d'incrémenter le compteur.
        - En utilisant `st.session_state.compteur`, nous accédons à la valeur du compteur qui 
                est mise à jour même entre différents appels de fonctions.

        Ainsi, `st.session_state` nous permet de maintenir l'état de variables à travers différentes 
        interactions de l'utilisateur au sein de notre application Streamlit.
                        """)

with tab3 : 
    st.markdown("""
    La fonction `st.progress_bar` dans Streamlit est utilisée pour afficher une 
                barre de progression dans votre application web. Cette barre de progression est 
                utile lorsque vous avez une tâche longue ou une opération en cours, et vous souhaitez fournir 
                une indication visuelle de son avancement.

    **Utilité :**

    L'utilité principale de `st.progress_bar` est de rendre l'expérience utilisateur plus conviviale 
                en affichant visuellement l'état d'avancement d'une tâche en cours, comme le traitement 
                de données, le chargement d'informations, etc.

    

    Voici un exemple simple où nous utilisons `st.progress_bar` pour simuler une tâche en cours qui 
                progresse au fil du temps :""")
    with st.expander("Utilisation ", True):
        import time

        # Simuler une tâche en cours
        progress_bar = st.progress(0)

        for i in range(100):
            # Mise à jour de la barre de progression
            progress_bar.progress(i + 1)
            
            # Simuler une pause pour représenter une tâche en cours
            time.sleep(0.1)

        # Fin de la tâche
        st.success('Tâche terminée!')
    st.markdown("""
    ```python
    import streamlit as st
    import time

    # Simuler une tâche en cours
    progress_bar = st.progress(0)

    for i in range(100):
        # Mise à jour de la barre de progression
        progress_bar.progress(i + 1)
        
        # Simuler une pause pour représenter une tâche en cours
        time.sleep(0.1)

    # Fin de la tâche
    st.success('Tâche terminée!')
    ```

    Dans cet exemple :
    - Nous créons une barre de progression avec `st.progress(0)` et la 
                stockons dans la variable `progress_bar`.
    - Nous utilisons ensuite une boucle pour simuler une tâche en cours. À chaque itération, 
                nous mettons à jour la barre de progression avec `progress_bar.progress(i + 1)`.
    - Une pause est ajoutée (`time.sleep(0.1)`) pour simuler une opération en cours.
    - Après la fin de la boucle, nous affichons un message de succès avec `st.success` p
                our indiquer que la tâche est terminée.

    Ainsi, `st.progress_bar` est un outil utile pour améliorer l'expérience utilisateur en f
                ournissant une indication visuelle de l'état d'avancement d'une tâche longue dans votre application Streamlit.
                    """)
with tab4 : 
    st.markdown("""
    La fonction `st.spinner` de Streamlit est utilisée pour afficher un indicateur de chargement sous forme de spinner (icône de chargement tournante). Cela peut être utile lorsque vous effectuez une opération asynchrone ou une tâche qui prend du temps, afin d'informer les utilisateurs que quelque chose se passe en arrière-plan.

    **Utilité :**

    L'utilité principale de `st.spinner` est de fournir une indication visuelle que quelque chose est en cours de chargement ou de traitement, ce qui améliore l'expérience utilisateur en indiquant clairement que l'application est occupée à effectuer une tâche.

    **Exemple avec du code :**

    Voici un exemple simple où nous utilisons `st.spinner` pour indiquer le chargement d'une tâche asynchrone :""")
    with st.expander("Utilisation ", True):
        import time

        # Fonction simulant une tâche asynchrone
        def tache_asynchrone():
            with st.spinner('Chargement en cours...'):
                # Simuler une tâche asynchrone
                time.sleep(5)
            st.success('Tâche terminée!')

        # Bouton pour déclencher la tâche asynchrone
        if st.button('Démarrer la tâche'):
            tache_asynchrone()

    st.markdown("""
    ```python
    import streamlit as st
    import time

    # Fonction simulant une tâche asynchrone
    def tache_asynchrone():
        with st.spinner('Chargement en cours...'):
            # Simuler une tâche asynchrone
            time.sleep(5)
        st.success('Tâche terminée!')

    # Bouton pour déclencher la tâche asynchrone
    if st.button('Démarrer la tâche'):
        tache_asynchrone()
    ```

    Dans cet exemple :
    - La fonction `tache_asynchrone` contient le code qui simule une tâche asynchrone en utilisant `time.sleep(5)` pour représenter un délai de 5 secondes.
    - La barre de progression (`st.spinner`) est affichée avec le message "Chargement en cours..." pendant l'exécution de la tâche asynchrone.
    - Une fois la tâche terminée, un message de succès est affiché avec `st.success`.

    Cela montre comment `st.spinner` peut être utilisé pour indiquer de manière visuelle l'avancement ou le chargement d'une tâche asynchrone dans votre application Streamlit.
                """)

with tab5 : 
    st.markdown("""
    La fonction `st.set_page_config` de Streamlit est utilisée pour configurer 
    les paramètres de la page de votre application Streamlit. Vous pouvez utiliser 
    cette fonction pour personnaliser divers aspects de l'apparence et du comportement de la page.

    **Exemple avec du code :**

    Voici un exemple où nous utilisons `st.set_page_config` pour 
    personnaliser certains paramètres de la page :

    ```python
    import streamlit as st

    # Configuration de la page
    st.set_page_config(
        page_title="Mon Application Streamlit",
        page_icon=":rocket:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Contenu de l'application
    st.title("Bienvenue dans mon application Streamlit")
    st.write("C'est une démonstration de l'utilisation de st.set_page_config.")

    # ... Ajoutez le reste de votre application Streamlit ici ...
    ```

    Dans cet exemple :
    - `page_title` est utilisé pour définir le titre de la page.
    - `page_icon` permet de spécifier une icône qui sera affichée dans l'onglet du navigateur.
    - `layout` peut être réglé sur "wide" pour utiliser un layout plus large.
    - `initial_sidebar_state` peut être réglé sur "expanded" pour afficher la barre latérale initialement étendue.

    Vous pouvez personnaliser ces paramètres en fonction de vos besoins spécifiques. 
    L'utilisation de `st.set_page_config` vous permet de définir ces configurations 
    au début de votre script Streamlit pour influencer l'apparence globale de votre application.
                    """)

with tab6 : 
    st.markdown("""
    ## 🚀 Optimisation des Performances avec le Caching
    
    Streamlit propose deux fonctions principales de mise en cache pour optimiser les performances de vos applications :
    
    ### `st.cache_data` - Pour les données
    
    `st.cache_data` est utilisé pour mettre en cache les données (DataFrames, listes, dictionnaires, etc.). 
    Cette fonction est idéale pour :
    - Charger des données depuis un fichier ou une base de données
    - Effectuer des calculs coûteux sur des données
    - Appeler des API externes
    - Transformer des données
    
    **Exemple d'utilisation :**
    """)
    
    with st.expander("**Utilisation de st.cache_data**", True):
        st.code("""
import streamlit as st
import pandas as pd
import time

@st.cache_data
def charger_donnees(fichier):
    # Simulation d'un chargement de données lent
    time.sleep(2)
    df = pd.read_csv(fichier)
    return df

# Le premier appel prendra 2 secondes
# Les appels suivants seront instantanés
df = charger_donnees("mes_donnees.csv")
st.dataframe(df)
        """, language="python")
        
        st.info("""
        💡 **Conseil** : Utilisez `st.cache_data` pour toutes les fonctions qui retournent des données. 
        Le cache sera invalidé automatiquement si les paramètres d'entrée changent.
        """)
    
    st.markdown("""
    ### `st.cache_resource` - Pour les ressources
    
    `st.cache_resource` est utilisé pour mettre en cache des ressources globales (connexions de base de données, 
    modèles ML, etc.). Cette fonction est idéale pour :
    - Connexions à des bases de données
    - Modèles de machine learning
    - Clients d'API
    - Ressources qui ne doivent être créées qu'une seule fois
    
    **Exemple d'utilisation :**
    """)
    
    with st.expander("**Utilisation de st.cache_resource**", True):
        st.code("""
import streamlit as st
import pickle

@st.cache_resource
def charger_modele():
    # Chargement d'un modèle ML (une seule fois)
    with open('modele.pkl', 'rb') as f:
        modele = pickle.load(f)
    return modele

# Le modèle est chargé une seule fois et réutilisé
modele = charger_modele()
prediction = modele.predict(nouvelles_donnees)
        """, language="python")
        
        st.warning("""
        ⚠️ **Attention** : N'utilisez `st.cache_resource` que pour des objets qui peuvent être partagés 
        entre tous les utilisateurs de l'application.
        """)
    
    st.markdown("""
    ### Paramètres avancés du cache
    
    Les deux fonctions acceptent des paramètres optionnels :
    - **ttl** : Durée de vie du cache en secondes
    - **max_entries** : Nombre maximum d'entrées dans le cache
    - **show_spinner** : Afficher ou non un spinner pendant le chargement
    """)
    
    with st.expander("**Exemple avec paramètres**", True):
        st.code("""
# Cache expirant après 1 heure
@st.cache_data(ttl=3600)
def obtenir_donnees_api():
    return requests.get("https://api.exemple.com/data").json()

# Cache limité à 10 entrées
@st.cache_data(max_entries=10)
def calculer_statistiques(df):
    return df.describe()

# Sans spinner
@st.cache_data(show_spinner=False)
def chargement_rapide():
    return pd.read_csv("petit_fichier.csv")
        """, language="python")

with tab7 : 
    st.markdown("""
    ## 🌐 Déploiement de votre Application Streamlit
    
    Une fois votre application développée, vous pouvez la déployer pour la rendre accessible à tous. 
    Voici les principales options de déploiement.
    
    ### 1. Streamlit Community Cloud (Recommandé) ☁️
    
    **Streamlit Community Cloud** est la solution officielle gratuite pour déployer vos applications Streamlit.
    
    **Avantages :**
    - ✅ Gratuit pour les projets publics
    - ✅ Déploiement en quelques clics
    - ✅ Intégration directe avec GitHub
    - ✅ Mises à jour automatiques
    - ✅ Gestion des secrets sécurisée
    """)
    
    with st.expander("**📋 Étapes de déploiement sur Streamlit Cloud**", True):
        st.markdown("""
        1. **Préparez votre code** :
           - Créez un fichier `requirements.txt` avec toutes vos dépendances
           - Assurez-vous que votre code fonctionne localement
        
        2. **Poussez sur GitHub** :
           ```bash
           git init
           git add .
           git commit -m "Initial commit"
           git push origin main
           ```
        
        3. **Déployez sur Streamlit Cloud** :
           - Allez sur [share.streamlit.io](https://share.streamlit.io)
           - Connectez votre compte GitHub
           - Sélectionnez votre dépôt
           - Spécifiez le fichier principal (ex: `app.py`)
           - Cliquez sur "Deploy"
        
        4. **Gérez les secrets** (optionnel) :
           - Dans les paramètres de l'application
           - Ajoutez vos variables d'environnement et clés API
        """)
    
    st.markdown("""
    ### 2. Autres Options de Déploiement
    
    #### Heroku 🔴
    - Plateforme cloud populaire
    - Support de Docker
    - Niveau gratuit disponible (avec limitations)
    """)
    
    with st.expander("**Déploiement sur Heroku**", True):
        st.code("""
# Créez ces fichiers :

# requirements.txt
streamlit>=1.32.0
pandas>=2.0.0

# setup.sh
mkdir -p ~/.streamlit/
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml

# Procfile
web: sh setup.sh && streamlit run app.py
        """)
        
        st.markdown("""
        Puis déployez :
        ```bash
        heroku create
        git push heroku main
        heroku open
        ```
        """)
    
    st.markdown("""
    #### Docker 🐳
    - Conteneurisation pour un déploiement flexible
    - Portable sur n'importe quelle plateforme
    """)
    
    with st.expander("**Dockerfile exemple**", True):
        st.code("""
FROM python:3.9-slim

WORKDIR /app

# Copier les fichiers
COPY requirements.txt .
COPY app.py .

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port
EXPOSE 8501

# Commande de démarrage
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
        """, language="dockerfile")
        
        st.markdown("""
        Construire et exécuter :
        ```bash
        docker build -t mon-app-streamlit .
        docker run -p 8501:8501 mon-app-streamlit
        ```
        """)
    
    st.markdown("""
    ### 🔒 Bonnes Pratiques de Sécurité
    
    1. **Ne jamais committer de secrets** :
       - Utilisez `.gitignore` pour exclure les fichiers sensibles
       - Utilisez `st.secrets` pour gérer les clés API
    
    2. **Gérer les secrets avec Streamlit** :
    """)
    
    with st.expander("**Utilisation de st.secrets**", True):
        st.code("""
# .streamlit/secrets.toml (ne jamais committer !)
api_key = "votre_clé_secrète"
database_url = "postgresql://user:password@host:5432/db"

# Dans votre code Python
import streamlit as st

# Accéder aux secrets
api_key = st.secrets["api_key"]
db_url = st.secrets["database_url"]
        """, language="python")
    
    st.markdown("""
    ### 📊 Optimisation pour la Production
    
    Avant de déployer, assurez-vous de :
    
    - ✅ **Optimiser les performances** avec `@st.cache_data` et `@st.cache_resource`
    - ✅ **Gérer les erreurs** avec des try-except appropriés
    - ✅ **Tester** l'application avec différentes données
    - ✅ **Documenter** le code et créer un README clair
    - ✅ **Surveiller** les logs et les erreurs après le déploiement
    - ✅ **Limiter les ressources** (taille des uploads, requêtes API, etc.)
    
    ### 📚 Ressources Utiles
    
    - [Documentation Streamlit Cloud](https://docs.streamlit.io/streamlit-community-cloud)
    - [Guide de déploiement](https://docs.streamlit.io/streamlit-community-cloud/get-started)
    - [Exemples d'applications déployées](https://streamlit.io/gallery)
    """)

