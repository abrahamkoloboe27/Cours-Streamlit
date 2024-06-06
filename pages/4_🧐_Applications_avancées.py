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
tab1 , tab2 , tab3, tab4, tab5 = st.tabs(["Applications multi-pages", "Session state", 
                              "Barre de progression", "Spinner", "Configuration de pages"])


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
