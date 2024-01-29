import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
st.set_page_config(
    page_title="📊 Traitement et Visualisation des données",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded",
)
with st.sidebar : 
    st.markdown("""
    ## Authors
    John R. AOGA
    * Email : <johnaoga@gmail.com>
    * WhatsApp : +229 97 99 92 77
    * Linkedin : [John AOGA](https://www.linkedin.com/in/john-aoga-2ba6a862/)
                
    Abraham KOLOBOE
    * Email : <abklb27@gmail.com>
    * WhatsApp : +229 91 83 84 21
    * Linkedin : [Abraham KOLOBOE](https://www.linkedin.com/in/abraham-koloboe-630683263)
                """)
st.title("📊 Traitement et Visualisation des données")
tab1,tab4, tab2, tab3 = st.tabs(["⏫Métriques", "📥Upload data","☁️Data Frame","〽️Charts"])

with tab1 : 
    st.markdown("""
    La fonction `st.metric` dans Streamlit est utilisée pour afficher une métrique (nombre ou mesure) dans votre application Streamlit. 
    C'est une manière visuellement attrayante de présenter des valeurs numériques importantes.
     """)
        
    with st.expander('**Utilisation :**', True):
        
        metric_value = st.number_input("Valeur", 27)
        st.metric(label="Ma Métrique", value=metric_value, delta=5.2)
        
    with st.expander("Code ", True):
        st.code(""" 
        import streamlit as st

        # Utilisation de st.metric pour afficher une métrique
        metric_value = st.number_input("Valeur", 27)
        st.metric(label="Ma Métrique", value=metric_value, delta=5.2, delta_color="inverse")
                    """)
    
    st.markdown("""
    Dans cet exemple, `label` représente l'étiquette de la métrique, `value` représente la valeur numérique principale à afficher, 
    `delta` est une valeur supplémentaire à afficher (par exemple, la différence par rapport à une valeur précédente), et `delta_color` 
    spécifie la couleur du delta.

    **Fonctionnalités clés :**
    - **Affichage attrayant :** `st.metric` est conçu pour présenter visuellement les métriques de manière attrayante.
    - **Compatibilité avec les valeurs delta :** Vous pouvez inclure une valeur delta pour montrer la différence par rapport 
    à une référence précédente.
    - **Personnalisation de la couleur :** Vous pouvez personnaliser la couleur du delta pour indiquer visuellement si 
    la métrique a augmenté ou diminué.

    C'est une fonction utile lorsque vous souhaitez mettre en avant des métriques importantes dans votre application 
    Streamlit de manière à la fois lisible et visuellement attrayante.
                    """)
with tab2 : 
    st.markdown("""
    La fonction `st.dataframe` dans Streamlit est utilisée pour afficher des DataFrames (tableaux de données) de manière interactive 
    dans votre application Streamlit.""")

    with st.expander('**Utilisation :**', True) :
        data = {'Nom': ['Alice', 'Bob', 'Charlie'],
                'Âge': [25, 30, 35],
                'Ville': ['Paris', 'New York', 'Londres']}
        df = pd.DataFrame(data)

        # Affichage du DataFrame avec st.dataframe
        st.dataframe(df)
    with st.expander("Code ", True):
        st.code(""" 
        import streamlit as st
        import pandas as pd

        # Création d'un DataFrame de démonstration
        data = {'Nom': ['Alice', 'Bob', 'Charlie'],
                'Âge': [25, 30, 35],
                'Ville': ['Paris', 'New York', 'Londres']}
        df = pd.DataFrame(data)
        # Affichage du DataFrame avec st.dataframe
        st.dataframe(df)
                """)
    st.markdown("""
    Dans cet exemple, `df` est un DataFrame Pandas, et `st.dataframe(df)` est utilisé pour afficher ce DataFrame dans l'application Streamlit.

    **Fonctionnalités clés :**
    - **Interactivité :** Le tableau de données est interactif, ce qui permet aux utilisateurs de trier les colonnes, de redimensionner les colonnes, etc.
    - **Affichage complet ou partiel :** Streamlit peut afficher automatiquement un DataFrame complet ou une partie de celui-ci, en fonction de la taille des données.
    - **Personnalisation :** Vous pouvez ajuster le comportement et l'apparence du tableau en fonction de vos besoins.

    `st.dataframe` est un moyen pratique d'afficher des données tabulaires dans votre application Streamlit, et il est souvent utilisé pour présenter des résultats d'analyse de données ou des jeux de données.
                """)
with tab3 : 
    a,b,c,d,e = st.tabs(["📉Line Charts", "📊Bar Charts", "📌Map","🧮Matplotlib Charts","🔍Plotly Charts"])
    with a : 
        st.markdown("""
        La fonction `st.line_chart` dans Streamlit est utilisée pour afficher un graphique en ligne (line chart) interactif 
        dans votre application Streamlit. Cette fonction prend en charge les graphiques basés sur les lignes, tels que les séries 
        chronologiques.""")

        with st.expander('**Utilisation :**', True) :            
            df = pd.DataFrame(np.random.randn(20,3), columns = ["A","B","C"])
            st.line_chart(df)
        with st.expander("Code ", True):
            st.code(""" 
            import streamlit as st
            import pandas as pd
            import numpy as np

            # Création d'un DataFrame de démonstration avec des données temporelles
             df = pd.DataFrame(np.random.randn(20,3), columns = ["A","B","C"])

            # Affichage du graphique en ligne avec st.line_chart
            st.line_chart(df)
                    """)
        st.markdown("""

        Dans cet exemple, `df` est un DataFrame Pandas contenant des données temporelles, et `st.line_chart(df.set_index('Date'))` 
        est utilisé pour afficher un graphique en ligne basé sur ces données temporelles.

        **Fonctionnalités clés :**
        - **Interactivité :** Le graphique en ligne est interactif, ce qui permet aux utilisateurs de zoomer, déplacer, et explorer les 
        données.
        - **Personnalisation :** Vous pouvez personnaliser le graphique en ligne en ajustant les options telles que les étiquettes d'axe, 
        les couleurs, etc.
        - **Compatibilité avec les données Pandas :** `st.line_chart` fonctionne bien avec les objets DataFrame de Pandas.

        `st.line_chart` est couramment utilisé pour visualiser des séries temporelles, mais il peut également être utilisé pour 
        d'autres types de données où une représentation graphique en ligne est pertinente.
        """)
    with b  : 
        st.markdown("""
        La fonction `st.bar_chart` dans Streamlit est utilisée pour afficher un graphique à barres (bar chart) 
        interactif dans votre application Streamlit.
                            """)
        with st.expander('**Utilisation :**', True) :            
            df = pd.DataFrame(np.random.rand(20,3), columns = ["A","B","C"])
            st.bar_chart(df)
        with st.expander("Code ", True):
            st.code(""" 
            # Création d'un DataFrame de démonstration
            df = pd.DataFrame(np.random.rand(20,3), columns = ["A","B","C"])
            
            # Affichage du graphique à barres avec st.bar_chart
            st.bar_chart(df)
                    """)
        st.markdown("""
        Dans cet exemple, `df` est un DataFrame Pandas contenant des données de catégorie et de valeur, et 
        `st.bar_chart(df.set_index('Catégorie'))` est utilisé pour afficher un graphique à barres basé sur ces données.

        **Fonctionnalités clés :**
        - **Interactivité :** Le graphique à barres est interactif, ce qui permet aux utilisateurs de 
        zoomer, déplacer, et explorer les données.
        - **Personnalisation :** Vous pouvez personnaliser le graphique à barres en ajustant les options telles que les couleurs, 
        les étiquettes d'axe, etc.
        - **Compatibilité avec les données Pandas :** `st.bar_chart` fonctionne bien avec les objets DataFrame de Pandas.

        Cette fonction est couramment utilisée pour représenter graphiquement des catégories et leurs valeurs associées sous 
        forme de barres, ce qui est utile pour visualiser des comparaisons entre différentes catégories.
                    """)  
    with c : 
        st.markdown("""
        La fonction `st.map` dans Streamlit est utilisée pour afficher une carte interactive dans votre application Streamlit. 
        Elle prend en charge la visualisation de données géographiques, telles que des points sur une carte.
        """)
        
        with st.expander('**Utilisation :**', True) : 
            
            df = pd.DataFrame( np.random.randn(100,2) /[100,100] + [6.36 ,2.43],
                columns = ['lat', 'lon']                
                )
            st.map(df)
        with st.expander("Code ", True):
            st.code(""" 
            import streamlit as st
            import pandas as pd

            # Création d'un DataFrame de démonstration avec des coordonnées géographiques
            df = pd.DataFrame( np.random.randn(100,2) /[50,50] + [37.76 ,-122.4],
                columns = ['lat', 'lon']                
                )

            # Affichage de la carte avec st.map
            st.map(df)
                    """)
        st.markdown("""
        Dans cet exemple, `df` est un DataFrame Pandas contenant des coordonnées géographiques (latitude et longitude) ainsi que des informations sur les villes. `st.map(df)` est utilisé pour afficher ces points sur une carte interactive.

        **Fonctionnalités clés :**
        - **Points interactifs :** Les points sur la carte sont interactifs, et les utilisateurs peuvent zoomer et déplacer la carte.
        - **Personnalisation :** Vous pouvez personnaliser la carte en ajustant des options telles que le niveau de zoom initial, les marqueurs de couleur, etc.
        - **Compatibilité avec les données géographiques :** `st.map` fonctionne bien avec les données qui incluent des coordonnées géographiques.

        Cette fonction est particulièrement utile lorsque vous souhaitez représenter visuellement des données spatiales, comme des emplacements géographiques spécifiques.
                            """)
    with d :
        st.markdown("""
        La fonction `st.pyplot` dans Streamlit est utilisée pour afficher des graphiques générés avec Matplotlib dans votre application 
        Streamlit. Elle offre une intégration simple et efficace avec Matplotlib pour visualiser des données dans vos applications.

       """)
        with st.expander('**Utilisation :**', True) : 
            x = np.linspace(- 2 * np.pi, 2 * np.pi, 100)
            y = np.sin(x)
            # Affichage du graphique avec st.pyplot
            fig, ax = plt.subplots()
            ax.plot(x, y)
            st.pyplot(fig)
        with st.expander("Code ", True):
            st.code(""" 
            import streamlit as st
            import matplotlib.pyplot as plt
            import numpy as np

            # Création d'un graphique avec Matplotlib
            x = np.linspace(- 2 * np.pi, 2 * np.pi, 100)
            y = np.sin(x)

            # Affichage du graphique avec st.pyplot
            fig, ax = plt.subplots()
            ax.plot(x, y)
            st.pyplot(fig)
                    """)
        st.markdown("""
        Dans cet exemple, un graphique sinusoidal simple est créé avec Matplotlib, puis affiché dans l'application Streamlit à l'aide de `st.pyplot`.

        **Fonctionnalités clés :**
        - **Intégration avec Matplotlib :** Vous pouvez utiliser `st.pyplot` pour afficher des graphiques générés avec la bibliothèque Matplotlib.
        - **Interactivité :** Les graphiques affichés avec `st.pyplot` sont interactifs, ce qui signifie que les utilisateurs peuvent zoomer, déplacer, et explorer les données.
        - **Compatibilité avec les autres éléments Streamlit :** Les graphiques Matplotlib peuvent être intégrés de manière transparente avec d'autres éléments Streamlit dans votre application.

        L'utilisation de `st.pyplot` est courante lorsque vous avez besoin d'afficher des graphiques générés avec Matplotlib dans vos applications Streamlit. Cela peut être utile pour la visualisation de données et l'analyse exploratoire.
                            """)
    with e :
        st.markdown("""
        La fonction `st.plotly_chart` dans Streamlit est utilisée pour afficher des graphiques générés avec Plotly dans votre application 
        Streamlit. Plotly est une bibliothèque de visualisation qui offre une grande flexibilité et des fonctionnalités interactives.
        """)
        
        with st.expander('**Utilisation :**', True) : 
            df = pd.DataFrame(np.random.rand(20,3), columns = ["A","B","C"])
            # Création d'un graphique à barres avec Plotly Express
            fig = px.bar(df, title='Graphique à Barres avec Plotly Express')
            # Affichage du graphique avec st.plotly_chart
            st.plotly_chart(fig)
        with st.expander("Code ", True):
            st.code(""" 
            import streamlit as st
            import plotly.express as px
            import pandas as pd
            import numpy as np

            # Création d'un DataFrame de démonstration
            df = pd.DataFrame(np.random.rand(20,3), columns = ["A","B","C"])

            # Création d'un graphique à barres avec Plotly Express
            fig = px.bar(df, title='Graphique à Barres avec Plotly Express')

            # Affichage du graphique avec st.plotly_chart
            st.plotly_chart(fig)
                    """)
        st.markdown("""
        Dans cet exemple, Plotly Express est utilisé pour créer un graphique à barres à partir d'un DataFrame Pandas, 
        puis le graphique est affiché dans une application Streamlit à l'aide de `st.plotly_chart`.

        **Fonctionnalités clés :**
        - **Intégration avec Plotly :** Vous pouvez utiliser `st.plotly_chart` pour afficher des graphiques générés avec 
        la bibliothèque Plotly.
        - **Interactivité :** Les graphiques affichés avec `st.plotly_chart` sont interactifs, ce qui signifie que les 
        utilisateurs peuvent zoomer, déplacer, et explorer les données.
        - **Compatibilité avec les autres éléments Streamlit :** Les graphiques Plotly peuvent être intégrés de manière 
        transparente avec d'autres éléments Streamlit dans votre application.

        L'utilisation de `st.plotly_chart` est courante lorsque vous avez besoin de créer des visualisations interactives et 
        personnalisables dans vos applications Streamlit. Cela peut être particulièrement utile pour les applications nécessitant 
        des fonctionnalités avancées de visualisation des données.
                            """)
with tab4 :
    st.markdown("""
    La fonction `st.uploader` dans Streamlit est utilisée pour permettre aux utilisateurs de télécharger 
    des fichiers dans votre application Streamlit. Elle fournit une interface conviviale pour que les utilisateurs 
    puissent sélectionner et télécharger des fichiers depuis leur propre machine.""")

    
    with st.expander('**Utilisation :**', True) : 
        file = st.file_uploader("Importer vos données ici", type="csv")

        # Vérification si un fichier a été téléchargé
        if file is not None:
            # Traitement du fichier téléchargé (par exemple, afficher les 5 premières lignes d'un DataFrame Pandas)
            df = pd.read_csv(file)
            st.dataframe(df.head())
    with st.expander("Code ", True):
        st.code("""
        import streamlit as st

        # Affichage de l'uploader dans l'application Streamlit
        file = st.file_uploader("Importer vos données ici", type=["csv"])

        # Vérification si un fichier a été téléchargé
        if file is not None:
            # Traitement du fichier téléchargé (par exemple, afficher les 5 premières lignes d'un DataFrame Pandas)
            df = pd.read_csv(file)
            st.dataframe(df.head())
                    """)
            
    st.markdown("""
    Dans cet exemple, `st.uploader` affiche un bouton permettant aux utilisateurs de sélectionner un 
    fichier CSV à télécharger. Le paramètre `type` est utilisé pour spécifier le type de fichier autorisé (dans cet exemple, 
    uniquement les fichiers CSV).

    **Fonctionnalités clés :**
    - **Interface conviviale :** Les utilisateurs peuvent cliquer 
    sur un bouton pour sélectionner des fichiers à télécharger.
    - **Spécification du type de fichier :** Vous pouvez limiter 
    les types de fichiers autorisés en utilisant le paramètre `type`.
    - **Manipulation du fichier téléchargé :** Une fois un fichier téléchargé, 
    vous pouvez effectuer des opérations de traitement sur le fichier, par exemple en le chargeant dans un DataFrame Pandas.

    L'utilisation de `st.uploader` est courante lorsque vous souhaitez permettre aux utilisateurs de 
    télécharger des fichiers dans votre application Streamlit, ce qui est utile dans de nombreuses situations, 
    notamment pour l'analyse de données et le traitement de fichiers.
                """)