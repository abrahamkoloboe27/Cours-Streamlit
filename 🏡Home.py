import streamlit as st
st.image(image="images/streamlit.png")
tab1,tab2,tab3, tab4 = st.tabs(["Description","Avantages","Plan du cours", "Quelques liens utiles" ])
with tab1 : 
    st.markdown("""
                Streamlit est un  framework open source en Python conçu pour simplifier le processus de **création d'applications web interactives** 
                destinées à **l'analyse et à la visualisation de données**. 
                
                Il offre une expérience de développement rapide en permettant aux utilisateurs de transformer leurs scripts 
                Python en applications web avec quelques lignes de code. 
                
                Streamlit se distingue par sa **simplicité d'utilisation** et son **orientation vers les développeurs 
                et les data scientists**, éliminant la complexité inhérente au développement web traditionnel. 
                
                Il prend en charge la __création de tableaux de bord interactifs__, la __visualisation__ de données, 
                l'intégration de widgets interactifs et offre une __expérience utilisateur fluide__. 
                
                Streamlit est devenu populaire dans le domaine de la science des données pour sa facilité d'apprentissage, 
                son efficacité et sa capacité à accélérer le déploiement d'applications web basées sur Python.
                """)

with tab2 : 
    st.markdown("""
    Streamlit présente plusieurs avantages qui ont contribué à sa popularité croissante, notamment dans le domaine de la 
    science des données et du développement d'applications web interactives. Voici quelques-uns des avantages clés de Streamlit :

    1. **Simplicité d'utilisation :** Streamlit est conçu pour être facile à apprendre et à utiliser. Les développeurs, 
    même ceux qui ne sont pas spécialisés dans le développement web, peuvent rapidement créer des applications interactives 
    avec quelques lignes de code.

    2. **Développement Rapide :** Le processus de développement est rapide, car les développeurs peuvent se concentrer 
    sur l'essentiel sans avoir besoin de gérer de nombreux détails liés au développement web traditionnel.

    3. **Intégration Transparente avec Python :** Étant une bibliothèque Python, Streamlit s'intègre naturellement avec 
    l'écosystème Python, en particulier avec des bibliothèques populaires telles que Pandas, Matplotlib et Plotly pour l'analyse 
    et la visualisation de données.

    4. **Widgets Intuitifs :** Streamlit offre une variété de widgets interactifs tels que des curseurs, des boutons et des 
    champs de texte, ce qui facilite l'ajout d'interactivité à vos applications.

    5. **Visualisation Instantanée :** Les DataFrames et les graphiques sont automatiquement rendus et actualisés, 
    permettant aux utilisateurs de voir instantanément les changements lors de la modification des paramètres.

    6. **Pas de Nécessité de Serveur Séparé :** Streamlit inclut un serveur web intégré, éliminant la nécessité de 
    déployer votre application sur un serveur distinct.

    7. **Personnalisation CSS Facile :** Bien que Streamlit soit axé sur la simplicité, il permet également une personnalisation 
    légère du style avec l'utilisation de code CSS.

    8. **Interactivité Déclarative :** L'interactivité est déclarative, ce qui signifie que les développeurs spécifient 
    simplement le comportement interactif souhaité, et Streamlit s'occupe du reste.

    9. **Documentation Complète et Communauté Active :** Streamlit dispose d'une documentation complète et d'une 
    communauté active qui facilite l'apprentissage et la résolution de problèmes.

    10. **Déploiement Facile :** Des options de déploiement simples et diverses sont disponibles, notamment Streamlit 
    Sharing, Heroku, Docker, etc.

    En combinant ces avantages, Streamlit offre une solution attrayante pour le développement rapide d'applications 
    interactives en Python, en particulier dans le domaine de l'analyse de données et de la création de tableaux de bord.
    """)
    
with tab3 : 
    st.markdown("""
    ### Introduction
    1. **Installation**
    - Installation de Streamlit.
    - Lancement d'une application streamlit.

    ### Les Fondamentaux de Streamlit
    2. **Première Application Streamlit**
    - Création d'une application simple "Hello World".
    - Structure de base d'une application Streamlit

    3. **Widgets et Interactivité**
    - Introduction aux widgets (boutons, sliders, etc.).
    - Utilisation des widgets pour interagir avec les visualisations.

    4. **Affichage de Données**
    - Intégration de DataFrames.
    - Personnalisation de l'affichage des données.

    ### Traitement de Données avec Streamlit
    5. **Chargement et Traitement de Données**
    - Importation de données .
    - Transformation de données avec Pandas.

    6. **Visualisations Interactives**
    - Création de graphiques interactifs avec Matplotlib, Plotly, etc.
    - Personnalisation des visualisations.

    ### Applications Avancées
    7. **Applications Multi-Pages**
    - Création d'applications avec plusieurs pages.
    - Utilisation de `st.session_state`.

    8. **Déploiement d'Applications**
        - Options de déploiement (Streamlit Sharing, Heroku, etc.).
        - Optimisation des performances.

    ### Projets Pratiques
    9. **Projet 1 : Dashboard de Données**
        - Création d'un dashboard interactif avec des widgets.

    10. **Projet 2 : Analyse de Données en Temps Réel**
        - Intégration de données en temps réel.
        - Utilisation des widgets pour les mises à jour.

    ### Conclusion
    

    """)

with tab4 : 
    st.markdown("""
                
                """)