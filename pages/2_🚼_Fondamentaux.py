import streamlit as st
import pandas as pd
from datetime import time, datetime, date
st.set_page_config(
    page_title="🚼 Fondamentaux",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("🚼 Fondamentaux")
tab1,tab2,tab3,tab4 = st.tabs(["👋🏾Hello World !","🔤Texte",
                               "🖇️Widget","🎞️Layouts" ])

with tab1 : 
    st.markdown("""
                Pour commencer, créons dans un dossier, un fichier **app.py**
                dans lequel nous allons écrire le code suivant :
                """)
    code_ = """
    import streamlit as st
    
    st.write("Hello World ! ")
    """
    st.code(code_, "python")
    st.markdown("""
                Puis dans l'invite de commande exécutons notre application en lancant  :
                """)
    st.code("streamlit run app.py", language="python")
    
with tab2 : 
    a,b,c,d = st.tabs(["Structures", "Markdown et HTML", "Write", "Messages de statut"])
    with a : 
       
        st.title("Tutoriel :red[Streamlit]")
        st.header(':blue[Introduction aux bases de données]')
        st.subheader("👨🏾‍💻 Applications web")
        st.text("Ma première application web avec Streamlit ! ")
        with st.expander("Code", True) : 
            code_ = """
            st.title("Tutoriel :red[Streamlit]")
            st.header(':blue[Introduction aux bases de données]')
            st.subheader("👨🏾‍💻 Applications web")
            st.text("Ma première application web avec Streamlit ! ")            
            """
            st.code(code_ , "python")
    with b : 
        st.header("Markdown")
        st.markdown("Pour écrire du code Markdown, il suffit d'utiliser la fonction :green[st.markdown()]")
        st.markdown("### Ceci est un texte ecrit en markdonw")
        st.markdown("### Ceci est un tableau réalisé en markdonw")
        st.markdown('''
                    | Data Science Tools     |
                    |------------------------|
                    | Jupyter Notebook       |
                    | RStudio                |
                    | VS Code with Python    |
                    ''')
        st.write("\n")
        with st.expander("Code", True) :
            st.code("""
                st.markdown("### Ceci est un texte ecrit en markdonw")
                st.markdown("### Ceci est un tableau réalisé en markdonw")
                st.markdown('''
                    | Data Science Tools     |
                    |------------------------|
                    | Jupyter Notebook       |
                    | RStudio                |
                    | VS Code with Python    |
                ''')
            """, language="python")
        st.header("**HTML**")
        st.markdown("""
                    Pour écrire du code HMTL, on utilise encore la fonction **:green[st.markdown()]** avec en argument 
                    du code HTML et cettre fois ci le paramètre **:red[unsafe_allow_html]=:blue[True]**.
                    
                    **Exemple**
                    """)
        # Utilisation de st.markdown pour afficher du code HTML
        st.markdown("<h1 style='text-align: center;'>Titre en HTML</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color: blue;'>Ceci est un paragraphe en HTML.</p>", unsafe_allow_html=True)

        # Vous pouvez également utiliser des balises HTML directement dans st.markdown
        st.markdown("<hr>", unsafe_allow_html=True)  # Ligne horizontale en HTML

        # Exemple avec une liste non ordonnée
        html_list = '''
        <ul>
            <li>Élément 1</li>
            <li>Élément 2</li>
            <li>Élément 3</li>
        </ul>
        '''
        st.markdown(html_list, unsafe_allow_html=True)
        
        with st.expander("Code", True) :
            st.code("""
                    # Utilisation de st.markdown pour afficher du code HTML
                    st.markdown("<h1 style='text-align: center;'>Titre en HTML</h1>", unsafe_allow_html=True)
                    st.markdown("<p style='color: blue;'>Ceci est un paragraphe en HTML.</p>", unsafe_allow_html=True)

                    # Vous pouvez également utiliser des balises HTML directement dans st.markdown
                    st.markdown("<hr>", unsafe_allow_html=True)  # Ligne horizontale en HTML

                    # Exemple avec une liste non ordonnée
                    html_list = '''
                    <ul>
                        <li>Élément 1</li>
                        <li>Élément 2</li>
                        <li>Élément 3</li>
                    </ul>
                    '''
                    st.markdown(html_list, unsafe_allow_html=True)   
                    """, language="python")
    with c : 
        st.markdown("""
                    ## La fonction :red[st.write()]
                    La fonction `st.write()` est une fonction polyvalente dans Streamlit qui permet d'afficher 
                    différents types de contenus, qu'il s'agisse de texte simple, de données structurées ou d'objets graphiques.
                    Elle offre une flexibilité significative pour communiquer des informations de manière concise 
                    et efficace dans une application Streamlit.
                    """)
        
        st.markdown("""**Utilisation de base :**""")
        # Affichage de texte
        st.write("Ceci est un texte simple.")

        # Affichage de données structurées (DataFrame, listes, dictionnaires, etc.)
        st.text("Voici une dataframe")
        data = pd.DataFrame({'Nom': ['Alice', 'Bob', 'Charlie'], 'Âge': [25, 30, 22]})
        st.write(data)

       

       
        with st.expander("Code", False) :
            st.code("""
                    import streamlit as st
                    import pandas as pd
                    # Affichage de texte
                    st.write("Ceci est un texte simple.")

                    # Affichage de données structurées (DataFrame, listes, dictionnaires, etc.)
                    data = pd.DataFrame{'Nom': ['Alice', 'Bob', 'Charlie'], 'Âge': [25, 30, 22]}
                    st.write(data)

                    """, language="python")
        st.markdown("""
                    **Caractéristiques clés :**
                    - **Polyvalence :** La fonction `st.write()` peut accepter une grande variété de types de 
                    , y compris du texte, des données structurées, des images, du code, etc.
                    - **Adaptabilité :** En fonction du type de contenu fourni en argument, Streamlit ajuste automatiquement 
                    la manière dont l'information est affichée.
                    - **Simplicité d'utilisation :** Il s'agit d'une méthode simple pour afficher des 
                    informations sans nécessiter de syntaxe complexe.

                    Que ce soit pour des démonstrations rapides, la visualisation de données, l'affichage de résultats 
                    de calculs ou la présentation de contenu divers, `st.write()` est un outil polyvalent et central dans 
                    le développement d'applications Streamlit.
                                        """)
    with d : 
        st.markdown("""
                    Streamlit offre différentes fonctions de messages de statut pour permettre aux développeurs de 
                    communiquer efficacement avec les utilisateurs de l'application. Ces fonctions facilitent la mise 
                    en évidence d'informations importantes, de mises en garde, d'erreurs ou de succès. Voici une description 
                    de certaines de ces fonctions :

                    1. **`st.warning(message)` :**
                    - Utilisé pour afficher un message d'avertissement.
                    - Le message est généralement mis en évidence avec une couleur jaune pour attirer l'attention de l'utilisateur.
                    - Exemple : """)
        
        st.warning("Cette opération peut entraîner la perte de données.")
        with st.expander("Code", True) :
            st.code("""st.warning("Cette opération peut entraîner la perte de données.")""", language="python")
        st.markdown("""
                    2. **`st.info(message)` :**
                    - Affiche un message informatif.
                    - Souvent utilisé pour fournir des détails supplémentaires ou des informations contextuelles.
                    - Exemple :""")
         
        st.info("Consultez la documentation pour plus d'informations.")
        with st.expander("Code", True) :
            st.code("""st.info("Consultez la documentation pour plus d'informations.")""", language="python")
        st.markdown("""3. **`st.success(message)` :**
                    - Utilisé pour indiquer que quelque chose s'est bien passé ou a réussi.
                    - Souvent utilisé après une opération réussie.
                    - Exemple :""")
        st.success("Les données ont été enregistrées avec succès.")
        with st.expander("Code", True) :
            st.code("""st.success("Les données ont été enregistrées avec succès.")""", language="python")
        st.markdown(""" 4. **`st.error(message)` :**
                    - Utilisé pour signaler une erreur ou un problème.
                    - La couleur rouge est généralement utilisée pour attirer l'attention sur l'importance de l'erreur.
                    - Exemple : """)
        st.error("Une erreur s'est produite lors du chargement des données.")
        with st.expander("Code", True) :
            st.code("""st.error("Une erreur s'est produite lors du chargement des données.")""", language="python")
        st.markdown("""
                    5. **`st.exception(exception)` :**
                    - Affiche une exception avec des détails.
                    - Utile pour afficher des messages d'erreur détaillés lorsqu'une exception se produit.
                    - Exemple :  """)
        st.exception(ValueError("Valeur non valide détectée."))
        with st.expander("Code", True) :
            st.code("""st.error("Une erreur s'est produite lors du chargement des données.")""", language="python")
        st.markdown("""Ces fonctions de messages de statut sont utiles pour améliorer l'expérience utilisateur en 
                    fournissant des informations claires et ciblées. Ils peuvent être utilisés dans divers scénarios, 
                    que ce soit pour avertir des 
                    actions potentiellement risquées, informer sur les succès, ou signaler des erreurs.
                    """)
with tab3 : 
    st.title(" Widgets")
    a,b,c,d,e,f,g,h,i = st.tabs(["Button","Checkbox","Radio Button", 
                    "Select Box","Multiselect","Slider", 
                    "Text/Number Input","Date input", "Formulaire"])
    with a : 
        st.markdown("""
        `st.button` est une fonction dans Streamlit qui permet de créer un 
        bouton interactif dans une application Streamlit. 
        Ce bouton peut être utilisé pour déclencher des actions ou des
        événements spécifiques lorsque l'utilisateur clique dessus. Il offre une 
        manière simple d'ajouter de l'interactivité à votre application en réagissant aux actions 
        de l'utilisateur.

       
        """)
        with st.expander('**Utilisation :**', True):
            if st.button("Cliquez-moi"):
                st.markdown("""### :blue[Vous venez de cliquer sur le boutton !]""")
            
        with st.expander("Code", True):
            st.code("""
         import streamlit as st
        # Création d'un bouton avec st.button
        if st.button("Cliquez-moi"):
            st.write("Vous venez de cliquer sur le boutton !")
        """)
        
        st.markdown("""
        Dans cet exemple, le bouton est créé avec l'étiquette "Cliquez-moi". 
        Lorsque l'utilisateur clique sur le bouton, le bloc de code à 
        l'intérieur du `if st.button(...)` est exécuté, et le message 
        "Le bouton a été cliqué !" est affiché.

        **Fonctionnalités clés :**
        - **Réactivité :** Le bloc de code associé au bouton est exécuté 
        lorsqu'il est activé par l'utilisateur.
        - **Personnalisation :** Vous pouvez personnaliser l'étiquette du bouton pour 
        qu'elle reflète l'action souhaitée.
        - **Intégration :** Les boutons peuvent être utilisés pour déclencher des mises à jour ou 
        des modifications dans l'interface utilisateur.

        En utilisant `st.button`, vous pouvez rendre votre application Streamlit 
        plus interactive et permettre aux utilisateurs d'initier des actions spécifiques 
        en un seul clic. Cela peut être utile pour implémenter des fonctionnalités telles que le 
        chargement de données, le calcul de résultats, ou tout autre comportement interactif que vous souhaitez 
        intégrer dans votre application.
        """)
    with b : 
        st.markdown("""
        `st.checkbox` est une fonction dans Streamlit qui permet de créer une case à cocher 
        (checkbox) dans une application Streamlit. Les cases à cocher 
        sont utiles pour permettre aux utilisateurs de sélectionner ou de 
        désélectionner des options et sont souvent utilisées pour activer 
        ou désactiver des fonctionnalités.
        
        **Utilisation :**
        """)
        with st.expander('**Utilisation :**', True):
            option_selected = st.checkbox("Activer une option")

            # Affichage en fonction de la sélection de la case à cocher
            if option_selected:
                st.write("L'option est **:blue[activée]** !")
            else:
                st.write("L'option est **:blue[désactivée]**.")
            
        
        with st.expander("Code", True):
            st.code("""
            import streamlit as st

            # Création d'une case à cocher avec st.checkbox
            option_selected = st.checkbox("Activer une option")

            # Affichage en fonction de la sélection de la case à cocher
            if option_selected:
                st.write("L'option est activée !")
            else:
                st.write("L'option est désactivée.")
        """)
        
        
        st.markdown("""
        Dans cet exemple, une case à cocher est créée avec l'étiquette "Activer une option". La valeur de la case à cocher 
        (True ou False) est stockée dans la variable `option_selected`. En fonction de la sélection de la case à cocher,
        différents messages sont affichés.

        **Fonctionnalités clés :**
        - **Réactivité :** La variable associée à `st.checkbox` est mise à jour en temps réel en fonction de l'état de la case à cocher.
        - **Personnalisation :** Vous pouvez personnaliser l'étiquette de la case à cocher pour refléter l'option
        que vous souhaitez activer ou désactiver.
        - **Utilisation conditionnelle :** Vous pouvez utiliser la valeur de la case à cocher pour prendre des 
        décisions conditionnelles dans votre application.

        En utilisant `st.checkbox`, vous pouvez ajouter des fonctionnalités 
        interactives à votre application Streamlit, permettant aux utilisateurs 
        de contrôler certains aspects de l'interface utilisateur en fonction de 
        leurs préférences. Cela peut être particulièrement utile pour activer ou 
        désactiver des visualisations, des filtres ou d'autres fonctionnalités de 
        manière flexible.
        """)
    with c :
        st.markdown("""
        `st.radio` est une fonction dans Streamlit qui permet de 
        créer un ensemble de boutons radio. Les boutons radio permettent 
        aux utilisateurs de choisir une seule option parmi plusieurs, 
        offrant une sélection mutuellement exclusive.""")
        
        with st.expander(" **Utilisation : Radio vertical**", True):
        # Création d'un ensemble de boutons radio avec st.radio
            selected_option = st.radio("Sélectionnez une option", 
            ["Option 1", "Option 2", "Option 3"], horizontal = True)

            # Affichage en fonction de l'option sélectionnée
            st.write(f"Vous avez sélectionné : **:blue[{selected_option}]**")
        with st.expander('**Utilisation : Radio horizontal**', True):
        # Création d'un ensemble de boutons radio avec st.radio
            selected_option = st.radio("Sélectionnez une option", 
                ["Option 1", "Option 2", "Option 3"])

            # Affichage en fonction de l'option sélectionnée
            st.write(f"Vous avez sélectionné : **:blue[{selected_option}]**")
        with st.expander("Code : Radio vertical", True):
            st.code("""
        import streamlit as st

        # Création d'un ensemble de boutons radio avec st.radio
        selected_option = st.radio("Sélectionnez une option", 
        ["Option 1", "Option 2", "Option 3"])

        # Affichage en fonction de l'option sélectionnée
        st.write(f"Vous avez sélectionné : {selected_option}") 
        """)
        with st.expander("Code : Radio horizontal", True):
            st.code("""
        import streamlit as st

        # Création d'un ensemble de boutons radio avec st.radio
        selected_option = st.radio("Sélectionnez une option", 
        ["Option 1", "Option 2", "Option 3"], horizontal = True)

        # Affichage en fonction de l'option sélectionnée
        st.write(f"Vous avez sélectionné : {selected_option}") 
        """)
        
        st.markdown("""
        Dans cet exemple, un ensemble de boutons radio est créé avec 
        l'étiquette "Sélectionnez une option" et les options "Option 1", 
        "Option 2" et "Option 3". La valeur sélectionnée est stockée dans 
        la variable `selected_option`, et un message est affiché en 
        fonction de l'option sélectionnée.

        **Fonctionnalités clés :**
        - **Sélection mutuellement exclusive :** Les boutons radio 
        permettent à l'utilisateur de choisir une seule option parmi 
        plusieurs.
        - **Personnalisation :** Vous pouvez personnaliser l'étiquette et l
        es options des boutons radio pour correspondre à votre application.
        - **Réactivité :** La variable associée à `st.radio` 
        est mise à jour en temps réel en fonction de l'option sélectionnée.

        `st.radio` est particulièrement utile lorsque vous avez une 
        liste d'options parmi lesquelles l'utilisateur doit faire un choix 
        exclusif. Cela peut être utilisé dans divers contextes, tels
        que la sélection de filtres, le choix de catégories, etc.
        """)
    with d : 
        st.markdown("""
            `st.selectbox` est une fonction de Streamlit qui permet de 
            créer une boîte de sélection déroulante (select box). Cette 
            boîte de sélection permet aux utilisateurs de choisir une 
            option parmi une liste déroulante d'options.""")
        with st.expander('**Utilisation :**', True):
            # Création d'une boîte de sélection avec st.selectbox
            selected_option = st.selectbox("Sélectionnez une option", 
                ["Option 1", "Option 2", "Option 3"])

            # Affichage en fonction de l'option sélectionnée
            st.write(f"Vous avez sélectionné : **:blue[{selected_option}]**")
        with st.expander("Code ", True):
            st.code("""
            import streamlit as st

            # Création d'une boîte de sélection avec st.selectbox
            selected_option = st.selectbox("Sélectionnez une option", 
                ["Option 1", "Option 2", "Option 3"])

            # Affichage en fonction de l'option sélectionnée
            st.write(f"Vous avez sélectionné : {selected_option}")""")
        
        st.markdown("""
            Dans cet exemple, une boîte de sélection déroulante est créée avec 
            l'étiquette "Sélectionnez une option" et les options "Option 1", 
            "Option 2" et "Option 3". La valeur sélectionnée est stockée dans la 
            variable `selected_option`, et un message est affiché en fonction de 
            l'option choisie.

            **Fonctionnalités clés :**
            - **Liste déroulante :** Les utilisateurs peuvent choisir une option dans 
            une liste déroulante.
            - **Personnalisation :** Vous pouvez personnaliser l'étiquette et les 
            options de la boîte de sélection pour répondre aux besoins de votre 
            application.
            - **Réactivité :** La variable associée à `st.selectbox` est mise à jour 
            en temps réel en fonction de l'option sélectionnée.

            `st.selectbox` est utile lorsque vous avez une liste d'options parmi 
            lesquelles l'utilisateur peut choisir, et vous souhaitez utiliser une 
            interface de sélection déroulante. Cela peut être appliqué dans divers 
            scénarios, 
            tels que la sélection de catégories, de filtres, ou d'autres options.
            """)
        with e : 
            st.markdown("""
            `st.multiselect` est une fonction dans Streamlit qui permet de 
            créer une boîte de sélection multiple. Cette boîte de sélection 
            permet aux utilisateurs de choisir plusieurs options parmi une 
            liste déroulante.
            """)
            with st.expander('**Utilisation : Sans valeur par défaut**', True):
                # Création d'une boîte de sélection multiple avec st.multiselect
                selected_options = st.multiselect("Sélectionnez plusieurs options", 
                        options = ["Option 1", "Option 2", "Option 3"])

                # Affichage en fonction des options sélectionnées
                st.write(f"Vous avez sélectionné : **:blue[{selected_options}]**")
            with st.expander('**Utilisation : Avec valeur par défaut**', True):
                # Création d'une boîte de sélection multiple avec st.multiselect
                selected_options = st.multiselect("Sélectionnez plusieurs options", 
                    options = ["Option 1", "Option 2", "Option 3"], 
                    default = ["Option 1"])

                # Affichage en fonction des options sélectionnées
                st.write(f"Vous avez sélectionné : **:blue[{selected_options}]**")
            
            with st.expander("Code: Sans valeur par défaut ", True):
                st.code("""
                import streamlit as st

                # Création d'une boîte de sélection multiple avec st.multiselect
                selected_options = st.multiselect("Sélectionnez plusieurs options", 
                ["Option 1", "Option 2", "Option 3"])

                # Affichage en fonction des options sélectionnées
                st.write(f"Vous avez sélectionné : {selected_options}")
                """)
            with st.expander("Code: Avec valeur par défaut ", True):
                st.code("""
                import streamlit as st

                # Création d'une boîte de sélection multiple avec st.multiselect
                selected_options = st.multiselect("Sélectionnez plusieurs options", 
                ["Option 1", "Option 2", "Option 3"], 
                default = ["Option 1"])

                # Affichage en fonction des options sélectionnées
                st.write(f"Vous avez sélectionné : {selected_options}")
                """)
            
            st.markdown("""
                Dans cet exemple, une boîte de sélection multiple est 
                créée avec l'étiquette "Sélectionnez plusieurs options" 
                et les options "Option 1", "Option 2" et "Option 3". Les 
                valeurs sélectionnées sont stockées dans la variable 
                `selected_options`, 
                et un message est affiché en fonction des options choisies.

                **Fonctionnalités clés :**
                - **Sélection multiple :** Les utilisateurs peuvent choisir 
                plusieurs options dans une liste déroulante.
                - **Personnalisation :** Vous pouvez personnaliser 
                l'étiquette et les options de la boîte de sélection 
                multiple.
                - **Réactivité :** La variable associée à `st.multiselect` 
                est mise à jour en temps réel en fonction des options 
                sélectionnées.

                `st.multiselect` est utile lorsque vous 
                avez une liste d'options parmi lesquelles les utilisateurs 
                peuvent choisir plusieurs éléments. Cela peut être appliqué 
                dans des cas tels que la sélection de filtres multiples, la 
                catégorisation, ou d'autres scénarios où une sélection 
                multiple est nécessaire.
                """)
    with f : 
        st.markdown("""
            `st.slider` est une fonction dans Streamlit qui 
            permet de créer un curseur (slider) interactif pour permettre 
            aux utilisateurs de choisir une valeur numérique dans une 
            plage définie.
            """)
        with st.expander('**Utilisation :**', True):
            #1
            # Création d'un curseur avec st.slider
            selected_value = st.slider("Sélectionnez une valeur", 
            min_value=0, max_value=100, value=50, step=1)

            # Affichage en fonction de la plage de valeurs sélectionnée
            st.write(f"Vous avez sélectionné : **:blue[{selected_value}]**")
            
            #2
            selected_value = st.slider("Sélectionnez une plage de valeurs", 
            min_value=0, max_value=100, value=(25,75), step=1)

            # Affichage en fonction de la plage de valeurs sélectionnée
            st.write(f"Vous avez sélectionné : **:blue[{selected_value}]**")
            
            #3
            selected_value = st.slider("Sélectionnez une plage de temps", 
            value=(time(6,0),time(18,30)))
            
            # Affichage en fonction de la plage de date sélectionnée
            st.write(f"""Vous avez sélectionné : **:blue[{selected_value[0]}]** - 
                    **:blue[{selected_value[1]}]**""")
            #4
            selected_value = st.slider("Sélectionnez une plage de date", 
            value= datetime(year=2024 , month=1 , day=29 , hour=8 , minute=45, second=25 ),
            format = "DD/MM/YYYY - hh:mm")

            # Affichage en fonction de la plage de date sélectionnée
            st.write(f"""Vous avez sélectionné : **:blue[{selected_value}]**""")
        with st.expander("Code ", True):
            
            st.code("""
            #1
            # Création d'un curseur avec st.slider
            selected_value = st.slider("Sélectionnez une valeur", 
            min_value=0, max_value=100, value=50, step=1)

            # Affichage en fonction de la plage de valeurs sélectionnée
            st.write(f"Vous avez sélectionné : **:blue[{selected_value}]**")
            
            #2
            selected_value = st.slider("Sélectionnez une plage de valeurs", 
            min_value=0, max_value=100, value=(25,75), step=1)

            # Affichage en fonction de la plage de valeurs sélectionnée
            st.write(f"Vous avez sélectionné : **:blue[{selected_value}]**")
            
            #3
            selected_value = st.slider("Sélectionnez une plage de temps", 
            value=(time(6,0),time(18,30)))
            
            # Affichage en fonction de la plage de date sélectionnée
            st.write(f'''Vous avez sélectionné : **:blue[{selected_value[0]}]** - 
                    **:blue[{selected_value[1]}]**''')
            #4
            selected_value = st.slider("Sélectionnez une plage de date", 
            value= datetime(year=2024 , month=1 , day=29 , hour=8 , minute=45, second=25 ),
            format = "DD/MM/YYYY - hh:mm")

            # Affichage en fonction de la plage de date sélectionnée
            st.write(f'''Vous avez sélectionné : **:blue[{selected_value}]**''')
            """)
        st.markdown("""
            Dans cet exemple, un curseur est créé avec l'étiquette 
            "Sélectionnez une valeur" et une plage allant de 0 à 100. 
            La valeur sélectionnée est stockée dans la variable 
            `selected_value`, et un message est affiché en fonction de la 
            valeur choisie.

            **Fonctionnalités clés :**
            - **Plage définie :** Vous pouvez spécifier la plage de valeurs 
            possibles avec les paramètres `min_value` et `max_value`.
            - **Valeur par défaut :** Vous pouvez définir une valeur par 
            défaut avec le paramètre `value`.
            - **Incrément :** Le paramètre `step` permet de définir 
            l'incrément du curseur.
            - **Réactivité :** La variable associée à `st.slider` est mise 
            à jour en temps réel en fonction du déplacement du curseur.

            `st.slider` est particulièrement utile lorsque 
            vous souhaitez permettre aux utilisateurs de choisir une valeur 
            numérique dans une plage continue. Cela peut être appliqué dans divers 
            contextes, tels que la sélection de plages de dates,
            de seuils, ou d'autres paramètres numériques.
            """)
        with g : 
            st.markdown("""
            `st.number_input` et `st.text_input` sont deux fonctions 
            dans Streamlit qui permettent respectivement de créer des 
            champs de saisie pour les valeurs numériques et les textes.
            
            ### `st.number_input` - Entrée Numérique :
            """)
            with st.expander('**Utilisation :**', True):
                numeric_value = st.number_input("Saisissez une valeur numérique", 
                min_value=0.0, max_value=100.0, value=50.0, step=1.0)

                # Affichage de la valeur saisie
                st.write(f"Vous avez saisi : **:blue[{numeric_value}]**")
            with st.expander("Code ", True):
                st.code("""
                import streamlit as st

                # Champ de saisie pour une valeur numérique avec st.number_input
                numeric_value = st.number_input("Saisissez une valeur numérique", 
                min_value=0.0, max_value=100.0, value=50.0, step=1.0)

                # Affichage de la valeur saisie
                st.write(f"Vous avez saisi : **:blue[{numeric_value}]**") """)
                    

        
            st.markdown("""
            **Fonctionnalités clés de `st.number_input` :**
            - **Plage définie :** Vous pouvez spécifier la plage de valeurs 
            possibles avec les paramètres `min_value` et `max_value`.
            - **Valeur par défaut :** Vous pouvez définir une valeur par 
            défaut avec le paramètre `value`.
            - **Incrément :** Le paramètre `step` permet de définir 
            l'incrément de saisie.
            - **Réactivité :** La variable associée à `st.number_input` 
            est mise à jour en temps réel en fonction de la saisie.

            ### `st.text_input` - Entrée Textuelle : """)
            with st.expander('**Utilisation :**', True):
                # Champ de saisie pour un texte avec st.text_input
                text_value = st.text_input("Saisissez un texte", 
                "Hello, Streamlit!")

                # Affichage du texte saisi
                st.write(f"Vous avez saisi : **:blue[{text_value}]**")
            with st.expander("Code ", True):
                st.code("""
                import streamlit as st

                # Champ de saisie pour un texte avec st.text_input
                text_value = st.text_input("Saisissez un texte", 
                "Hello, Streamlit!")

                # Affichage du texte saisi
                st.write(f"Vous avez saisi : **:blue[{text_value}]**")
                """)
            st.markdown("""
            **Fonctionnalités clés de `st.text_input` :**
            - **Texte par défaut :** Vous pouvez définir un texte par 
            défaut avec le deuxième argument (ici "Hello, Streamlit!").
            - **Réactivité :** La variable associée à `st.text_input` 
            est mise à jour en temps réel en fonction de la saisie.

            `st.number_input` et `st.text_input` sont utiles lorsque 
            vous souhaitez permettre aux utilisateurs de saisir des 
            valeurs numériques ou du texte, respectivement. Ces champs de 
            saisie sont adaptés pour collecter des 
            informations spécifiques dans le cadre d'une application 
            Streamlit.
            """)
        with h :
            st.markdown("""
            `st.date_input` est une fonction dans Streamlit qui permet de créer un sélecteur de date interactif. 
            Cette fonction est utile lorsque vous souhaitez permettre aux utilisateurs de sélectionner une date spécifique dans votre 
            application Streamlit.

            """)
            with st.expander('**Utilisation :**', True):
                # Sélecteur de date avec st.date_input
                selected_date = st.date_input("Sélectionnez une date", date.today())

                # Affichage de la date sélectionnée
                st.write(f"Vous avez sélectionné la date : **:blue[{selected_date}]**")
                
            with st.expander("Code ", True):
                st.code("""
                import streamlit as st
                from datetime import date

                # Sélecteur de date avec st.date_input
                selected_date = st.date_input("Sélectionnez une date", date.today())

                # Affichage de la date sélectionnée
                st.write(f"Vous avez sélectionné la date : **:blue[{selected_date}]**")
                """)
            st.markdown("""
            Dans cet exemple, un sélecteur de date est créé avec l'étiquette 
            "Sélectionnez une date" et la date par défaut est définie sur la date du 
            jour. La date sélectionnée est stockée dans la variable `selected_date`, 
            et un message est affiché en fonction de la date choisie.

            **Fonctionnalités clés :**
            - **Date par défaut :** Vous pouvez définir une date par défaut avec le 
            deuxième 
            argument (ici, `date.today()` est utilisé pour définir la date actuelle).
            - **Réactivité :** La variable associée à `st.date_input` est mise à jour 
            en temps réel en fonction de la date sélectionnée.

            `st.date_input` est particulièrement utile dans les applications où la 
            sélection de dates est cruciale, comme dans les applications de 
            planification, les outils de suivi du temps, 
            ou tout autre scénario où la gestion des dates est nécessaire.
                    """)
        with i :
            st.markdown("""
            `st.form` est une fonction dans Streamlit qui permet de créer 
            un formulaire interactif dans une application Streamlit. 
            Les formulaires sont utiles lorsque vous souhaitez collecter 
            plusieurs entrées de l'utilisateur et traiter ces entrées en 
            une seule fois.
            """)
            with st.expander('**Utilisation :**', True):
                # Création d'un formulaire avec st.form
                with st.form("Mon Formulaire"):
                    # Ajout de champs de saisie dans le formulaire
                    texte = st.text_input("Entrez du texte")
                    choix = st.selectbox("Choisissez un animal", ["Chien", "Chat", "Lion"])
                    nombre = st.number_input("Entrez un nombre", value = 27)
                    date = st.date_input("Sélectionnez une date",date.today())

                    # Ajout d'un bouton de soumission
                    soumettre = st.form_submit_button("Soumettre")

                    # Traitement des données après la soumission
                    if soumettre:
                        st.write(f'''Vous avez saisi : Texte - **:blue[{texte}]**, Animal - **:blue[{choix}]**, 
                                 Nombre - **:blue[{nombre}]**, Date - **:blue[{date}]**''')
                    
            with st.expander("Code ", True):
                st.code("""
                import streamlit as st

                # Création d'un formulaire avec st.form
                with st.form("Mon Formulaire"):
                    # Ajout de champs de saisie dans le formulaire
                    texte = st.text_input("Entrez du texte")
                    choix = st.selectbox("Choisissez un animal", ["Chien", "Chat", "Lion"])
                    nombre = st.number_input("Entrez un nombre", value = 27)
                    date = st.date_input("Sélectionnez une date",date.today())

                    # Ajout d'un bouton de soumission
                    soumettre = st.form_submit_button("Soumettre")

                # Traitement des données après la soumission
                if soumettre:
                    st.write(f'''Vous avez saisi : Texte - **:blue[{texte}]**, Animal - **:blue[{choix}]**,
                    Nombre - **:blue[{nombre}]**, Date - **:blue[{date}]**''') """)
                
        st.markdown("""
            Dans cet exemple, un formulaire est créé avec l'étiquette 
            "Mon Formulaire". À l'intérieur du formulaire, plusieurs champs de 
            saisie sont ajoutés pour collecter du texte, un nombre et une date. 
            Un bouton de soumission est également inclus. Une fois le formulaire 
            soumis, les données saisies sont affichées.

            **Fonctionnalités clés :**
            - **Encapsulation :** Les champs de saisie à l'intérieur du bloc `with st.form` font partie du formulaire.
            - **Bouton de soumission :** `st.form_submit_button` est utilisé pour ajouter un bouton de soumission au formulaire.
            - **Réactivité :** Les variables associées aux champs de saisie dans le formulaire sont mises à jour en temps réel.

            `st.form` est utile lorsque vous avez besoin de collecter plusieurs 
            entrées de l'utilisateur en une seule fois et de traiter ces entrées de 
            manière cohérente. 
            Cela simplifie la gestion des formulaires dans vos applications Streamlit.
                                """)

with tab4 : 
    
    a,b,c,d,e = st.tabs(["Sidebar", "Colonnes","Tabs(Onglets)", "Expander", "Code"])
    
    with a : 
        st.markdown(""" 
            `st.sidebar` est une fonction dans Streamlit qui permet de créer des éléments dans la barre latérale de l'interface 
            utilisateur. La barre latérale est souvent utilisée pour afficher des contrôles interactifs, des paramètres ou d'autres 
            éléments qui ne font pas partie du contenu principal de l'application, mais qui sont accessibles facilement.""")

        
        #   with st.expander('**Utilisation :**', True):
            #    # Utilisation de st.sidebar pour ajouter des éléments dans la barre latérale
            #    st.sidebar.header("Options")
            #    texte_sidebar = st.sidebar.text_input("Entrez du texte","Abraham")
            #    nombre_sidebar = st.sidebar.number_input("Entrez un nombre", min_value=0, max_value=100, value=27)

                # Affichage des valeurs saisies dans le contenu principal
            #    st.write(f"Vous avez saisi en barre latérale : Texte - **:blue[{texte_sidebar}]**, Nombre - **:blue[{nombre_sidebar}]**")
        
        with st.expander("Code ", True):
            st.code("""  
                    import streamlit as st

                    # Utilisation de st.sidebar pour ajouter des éléments dans la barre latérale
                    st.sidebar.header("Options")
                    texte_sidebar = st.sidebar.text_input("Entrez du texte","Abraham")
                    nombre_sidebar = st.sidebar.number_input("Entrez un nombre", min_value=0, max_value=100, value=27)

                    # Affichage des valeurs saisies dans le contenu principal
                    st.write(f"Vous avez saisi en barre latérale : Texte - **:blue[{texte_sidebar}]**, Nombre - **:blue[{nombre_sidebar}]**")
                    """)
            st.markdown(""" 
            Dans cet exemple, un champ de saisie de texte et un curseur numérique sont ajoutés à la barre latérale à l'aide de
            `st.sidebar`. Les valeurs saisies dans la barre latérale sont ensuite affichées dans le contenu principal de l'application.

            **Fonctionnalités clés :**
            - **Contrôles interactifs :** Vous pouvez utiliser `st.sidebar` pour ajouter divers contrôles interactifs tels que des champs de 
            saisie, des curseurs, des boutons, etc.
            - **Réactivité :** Les valeurs associées aux contrôles dans la barre latérale sont mises à jour en temps réel.
            - **Organisation :** La barre latérale est utile pour organiser les paramètres et contrôles de manière à ne pas encombrer le contenu 
            principal de l'application.

            L'utilisation de `st.sidebar` permet d'ajouter une dimension interactive et personnalisée à votre application Streamlit en plaçant 
            certains éléments dans une barre latérale distincte.
            """)
    with b : 
    
        st.markdown("""
        `st.columns` est une fonction dans Streamlit qui permet de créer des colonnes dans la mise en page de votre application. Cette 
        fonction est particulièrement utile lorsque vous souhaitez organiser le contenu de votre application en colonnes pour une présentation 
        plus structurée. """)

        with st.expander('**Utilisation :**', True):
            colonne1, colonne2 = st.columns(2)

            # Ajout de contenu dans chaque colonne
            with colonne1:
                st.header("Colonne 1")
                st.write("Contenu de la colonne ") 
                st.image("images/chien.png")

            with colonne2:
                st.header("Colonne 2")
                st.write("Contenu de la colonne 2") 
                st.image("images/minion.jpg")
        with st.expander("Code ", True):
            st.code("""  
            import streamlit as st

            # Création de deux colonnes avec st.columns
            colonne1, colonne2 = st.columns(2)

            # Ajout de contenu dans chaque colonne
            with colonne1:
                st.header("Colonne 1")
                st.write("Contenu de la colonne ") 
                st.image("images/chien.png")

            with colonne2:
                st.header("Colonne 2")
                st.write("Contenu de la colonne 2") 
                st.image("images/minion.jpg")
                """)
        st.markdown("""
        Dans cet exemple, deux colonnes sont créées à l'aide de `st.columns(2)`, ce qui divise l'espace horizontal 
        en deux parties égales. Ensuite, du contenu est ajouté à chaque colonne avec les blocs `with colonne1:` et `with colonne2:`.

        **Fonctionnalités clés :**
        - **Répartition de l'espace :** Vous pouvez spécifier le nombre de colonnes que vous souhaitez en passant un argument à `st.columns(n)`,
        où `n` est le nombre de colonnes.
        - **Contenu dans chaque colonne :** Vous pouvez ajouter du contenu, des widgets, des graphiques, etc., à chaque colonne en 
        utilisant les blocs `with colonneX:`.

        `st.columns` est utile pour créer une disposition de colonnes personnalisée dans votre application Streamlit, ce qui est particulièrement pratique lorsque 
        vous avez plusieurs éléments à afficher de manière côte à côte.
                                """)
    with c: 
        st.markdown(""""
                    
                        """)
    with d: 
        st.markdown("""
        `st.expander` est une fonction dans Streamlit qui permet de créer un panneau extensible (expander) dans lequel vous pouvez inclure du contenu. 
        Cela est utile lorsque vous avez du contenu supplémentaire que vous souhaitez rendre initialement caché et permettre à l'utilisateur de l'expander ou de le réduire 
        selon ses besoins.
        
        ### **Utilisation**
        """)


        with st.expander("Cliquez pour afficher le contenu",False):
            st.write("**:blue[Contenu caché que vous pouvez étendre ou réduire].**")
        with st.expander("Code ", True):
            st.code("""  
            # Utilisation de st.expander pour créer un panneau extensible
            with st.expander("Cliquez pour afficher le contenu",False):
                st.write("Contenu caché que vous pouvez étendre ou réduire.")
                    """)
            
        st.markdown("""
        Dans cet exemple, le texte "Cliquez pour afficher le contenu" est affiché en tant que titre du panneau extensible créé avec `st.expander`. 
        Lorsque l'utilisateur clique sur ce titre, le panneau s'étend pour révéler le contenu caché, et il peut être réduit à nouveau en cliquant sur le titre.

        **Fonctionnalités clés :**
        - **Contenu extensible :** Vous pouvez inclure n'importe quel widget ou contenu à l'intérieur du panneau extensible.
        - **Facilité d'utilisation :** L'utilisateur peut cliquer sur le titre pour étendre ou réduire le panneau, ce qui permet de conserver un espace propre dans votre 
        application.

        `st.expander` est particulièrement utile lorsque vous avez des informations complémentaires ou des détails que vous ne souhaitez pas afficher immédiatement, mais que 
        vous souhaitez rendre disponibles de manière optionnelle à l'utilisateur.
        """)
    with e: 
        st.markdown("""
        La fonction `st.code` dans Streamlit est utilisée pour afficher du code source dans votre application Streamlit. Elle prend en charge plusieurs langages de 
        programmation et fournit une mise en forme syntaxique pour rendre le code plus lisible.
        """)
        
        with st.expander('**Utilisation :**', True):
            # Utilisation de st.code pour afficher du code Python
            code_python = '''
            public class HelloWorld {
                public static void main(String[] args) {
                    System.out.println("Hello, World!");
                }
            }
            '''

            st.code(code_python, language='java')
        with st.expander("Code ", True):
            st.code(""" 
            import streamlit as st

            # Utilisation de st.code pour afficher du code Python
            code_python = '''
            public class HelloWorld {
                public static void main(String[] args) {
                    System.out.println("Hello, World!");
                }
            }
            '''

            st.code(code_python, language='java')
                    """)
        st.markdown("""
        Dans cet exemple, le code Python contenu dans la chaîne `code_python` est affiché à l'aide de `st.code`. L'argument `language` spécifie le langage du code pour une 
        mise en forme syntaxique appropriée.

        **Fonctionnalités clés :**
        - **Prise en charge de plusieurs langages :** Vous pouvez spécifier le langage du code source pour une mise en forme syntaxique correcte.
        - **Mise en forme syntaxique :** Le code est présenté de manière à ce que les éléments tels que les mots-clés, les chaînes de caractères, 
        les commentaires, etc., soient mis en surbrillance pour une meilleure lisibilité.
        - **Possibilité de plier/déplier le code :** Streamlit offre une fonctionnalité qui permet de plier et déplier le code pour économiser de l'espace.

        L'utilisation de `st.code` est particulièrement utile lorsque vous souhaitez partager des exemples de code, des extraits de code ou des démonstrations 
        dans votre application Streamlit.
                                """)