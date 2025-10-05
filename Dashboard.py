# dashboard_defense_usa_avance.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(
    page_title="Analyse Stratégique Avancée - États-Unis",
    page_icon="🇺🇸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé avancé
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        background: linear-gradient(45deg, #0033A0, #B22234, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .metric-card {
        background: linear-gradient(135deg, #0033A0, #B22234);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .section-header {
        color: #0033A0;
        border-bottom: 3px solid #B22234;
        padding-bottom: 0.8rem;
        margin-top: 2rem;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .navy-card {
        background: linear-gradient(135deg, #0033A0, #1E90FF);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    .airforce-card {
        background: linear-gradient(135deg, #1E90FF, #87CEEB);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .army-card {
        background: linear-gradient(135deg, #228B22, #32CD32);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .marines-card {
        background: linear-gradient(135deg, #8B0000, #FF0000);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .nato-card {
        background: linear-gradient(135deg, #0033A0, #00BFFF);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .alliance-card {
        background: linear-gradient(135deg, #4B0082, #8A2BE2);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

class DefenseUSADashboardAvance:
    def __init__(self):
        self.branches_options = self.define_branches_options()
        self.programmes_options = self.define_programmes_options()
        self.military_capabilities = self.define_military_capabilities()
        self.alliance_projects = self.define_alliance_projects()
        
    def define_branches_options(self):
        return [
            "États-Unis - Vue d'Ensemble", "US Army", "US Navy", 
            "US Air Force", "US Marine Corps", "US Space Force",
            "Alliances OTAN", "Coopérations Stratégiques"
        ]
    
    def define_programmes_options(self):
        return [
            "Modernisation Nucléaire", "Defense Missile Ballistique", 
            "Supériorité Aérienne", "Puissance Navale Globale",
            "Guerre Cyber Offensive", "Dominance Spatiale",
            "Commandement Cyber"
        ]
    
    def define_military_capabilities(self):
        return {
            "US Army": {
                "budget": 185.0,
                "personnel": 485,
                "divisions": 10,
                "equipements": "M1 Abrams, M2 Bradley, Apache",
                "technologies": "IA, Robots de combat, Drones"
            },
            "US Navy": {
                "budget": 244.0,
                "personnel": 347,
                "porte_avions": 11,
                "sous_marins": 68,
                "navires_combat": 290,
                "equipements": "Porte-avions, Destroyers, Sous-marins",
                "technologies": "Porte-avions nucléaires, F-35C, Armes laser"
            },
            "US Air Force": {
                "budget": 194.0,
                "personnel": 329,
                "avions_combat": 1300,
                "bombardiers": 141,
                "tankers": 500,
                "equipements": "F-35A, F-22, B-21, C-17",
                "technologies": "F-35A, B-21 Raider, F-22 Raptor"
            },
            "US Marine Corps": {
                "budget": 53.0,
                "personnel": 177,
                "expeditionary": "MEU, MEF",
                "aviation": "F-35B, V-22 Osprey",
                "equipements": "Véhicules amphibies, F-35B",
                "technologies": "Mobilité expéditionnaire avancée"
            },
            "US Space Force": {
                "budget": 26.0,
                "personnel": 8.4,
                "satellites": "GPS, Early Warning, Communications",
                "missions": "Surveillance spatiale, Guerre électronique",
                "equipements": "Satellites, Systèmes au sol",
                "technologies": "Satellites de nouvelle génération"
            }
        }
    
    def define_alliance_projects(self):
        return {
            "Commandement Cyber OTAN": {"pays": "OTAN", "type": "Cybersécurité", "statut": "Opérationnel", "localisation": "Belgique/États-Unis"},
            "Defense Missile Européenne": {"pays": "OTAN", "type": "Defense missile", "statut": "Déploiement", "objectif": "Couverture Europe"},
            "Exercice RIMPAC": {"pays": "Alliés Pacifique", "type": "Exercice naval", "statut": "Actif", "frequence": "Biannuel"},
            "Partenariat QUAD": {"pays": "USA/Japon/Inde/Australie", "type": "Coopération stratégique", "statut": "Renforcement", "domaines": "Indo-Pacifique"},
            "AUKUS": {"pays": "USA/UK/Australie", "type": "Partage technologique", "statut": "Actif", "technologies": "Sous-marins nucléaires"}
        }
    
    def generate_advanced_data(self, selection):
        """Génère des données avancées et détaillées pour les États-Unis"""
        annees = list(range(2000, 2028))
        
        config = self.get_advanced_config(selection)
        
        data = {
            'Annee': annees,
            'Budget_Defense_Mds': self.simulate_advanced_budget(annees, config),
            'Personnel_Milliers': self.simulate_advanced_personnel(annees, config),
            'PIB_Militaire_Pourcent': self.simulate_military_gdp_percentage(annees),
            'Exercices_Militaires': self.simulate_advanced_exercises(annees, config),
            'Readiness_Operative': self.simulate_advanced_readiness(annees),
            'Capacite_Dissuasion': self.simulate_advanced_deterrence(annees),
            'Temps_Mobilisation_Jours': self.simulate_advanced_mobilization(annees),
            'Exercices_Conjoints': self.simulate_joint_exercises(annees),
            'Developpement_Technologique': self.simulate_tech_development(annees),
            'Capacite_Navale': self.simulate_naval_capacity(annees),
            'Couverture_AD': self.simulate_air_defense_coverage(annees),
            'Cooperation_Alliances': self.simulate_alliance_cooperation(annees),
            'Cyber_Capabilities': self.simulate_cyber_capabilities(annees),
            'Production_Armements': self.simulate_weapon_production(annees)
        }
        
        # Données spécifiques aux programmes
        if 'nucleaire' in config.get('priorites', []):
            data.update({
                'Stock_Ogives_Nucleaires': self.simulate_nuclear_arsenal(annees),
                'Portee_Missiles_Km': self.simulate_missile_range(annees),
                'Triade_Nucleaire': self.simulate_nuclear_triad(annees)
            })
        
        if 'marine' in config.get('priorites', []):
            data.update({
                'Porte_Avions': self.simulate_aircraft_carriers(annees),
                'Sous_Marins': self.simulate_submarines(annees),
                'Projection_Maritime': self.simulate_maritime_projection(annees)
            })
        
        if 'innovation' in config.get('priorites', []):
            data.update({
                'Recherche_Defense': self.simulate_defense_research(annees),
                'Technologies_Emergentes': self.simulate_emerging_tech(annees),
                'Exportations_Armes': self.simulate_weapon_exports(annees)
            })
        
        if 'alliances' in config.get('priorites', []):
            data.update({
                'Exercices_OTAN': self.simulate_nato_exercises(annees),
                'Partenariats_Strategiques': self.simulate_strategic_partnerships(annees),
                'Bases_Etrangeres': self.simulate_foreign_bases(annees)
            })
        
        return pd.DataFrame(data), config
    
    def get_advanced_config(self, selection):
        """Configuration avancée avec plus de détails pour les États-Unis"""
        configs = {
            "États-Unis - Vue d'Ensemble": {
                "type": "superpuissance_globale",
                "budget_base": 850.0,
                "personnel_base": 1346,
                "exercices_base": 280,
                "priorites": ["nucleaire", "marine", "innovation", "cyber", "alliances", "spatial"],
                "doctrines": ["Supériorité globale", "Projection de puissance", "Dissuasion avancée"],
                "objectifs": "Maintien de l'hégémonie mondiale"
            },
            "US Navy": {
                "type": "marine_globale",
                "budget_base": 244.0,
                "personnel_base": 347,
                "priorites": ["porte_avions", "sous_marins", "projection", "cyber_maritime"],
                "capacites": ["11 porte-avions", "Forces expéditionnaires", "Sous-marins nucléaires"],
                "doctrine": "Sea Power 21"
            },
            "US Air Force": {
                "type": "suprematie_aerienne",
                "budget_base": 194.0,
                "personnel_base": 329,
                "priorites": ["avions_5e_gen", "bombardiers", "tankers", "espace"],
                "capacites": ["F-35, F-22, B-21", "Ravitaillement en vol", "Commandement spatial"],
                "doctrine": "Global Strike"
            },
            "Alliances OTAN": {
                "type": "leadership_alliances",
                "budget_base": 1200.0,
                "priorites": ["defense_collective", "interoperabilite", "exercices_conjoints"],
                "projets": ["Defense missile", "Commandement cyber", "Forces de réaction"],
                "objectifs": "Défense collective transatlantique"
            }
        }
        
        return configs.get(selection, {
            "type": "branche_militaire",
            "personnel_base": 200,
            "exercices_base": 40,
            "priorites": ["defense_generique"]
        })
    
    def simulate_advanced_budget(self, annees, config):
        """Simulation avancée du budget avec variations géopolitiques"""
        budget_base = config.get('budget_base', 850.0)
        budgets = []
        for annee in annees:
            base = budget_base * (1 + 0.045 * (annee - 2000))
            # Variations selon événements géopolitiques
            if 2001 <= annee <= 2003:  # Guerre contre le terrorisme
                base *= 1.25
            elif 2008 <= annee <= 2010:  # Crise financière
                base *= 0.95
            elif annee >= 2014:  # Pivot vers l'Asie
                base *= 1.08
            elif annee >= 2018:  # Compétition stratégique
                base *= 1.12
            elif annee >= 2022:  # Soutien Ukraine
                base *= 1.15
            budgets.append(base)
        return budgets
    
    def simulate_advanced_personnel(self, annees, config):
        """Simulation avancée des effectifs"""
        personnel_base = config.get('personnel_base', 1346)
        return [personnel_base * (1 + 0.003 * (annee - 2000)) for annee in annees]
    
    def simulate_military_gdp_percentage(self, annees):
        """Pourcentage du PIB consacré à la défense"""
        return [3.0 + 0.08 * (annee - 2000) for annee in annees]
    
    def simulate_advanced_exercises(self, annees, config):
        """Exercices militaires avec saisonnalité"""
        base = config.get('exercices_base', 280)
        return [base + 8 * (annee - 2000) + 12 * np.sin(2 * np.pi * (annee - 2000)/4) for annee in annees]
    
    def simulate_advanced_readiness(self, annees):
        """Préparation opérationnelle avancée"""
        readiness = []
        for annee in annees:
            base = 85  # Départ élevé
            if annee >= 2001:  # Post-9/11
                base += 5
            if annee >= 2014:  # Réorientation stratégique
                base += 3
            if annee >= 2020:  # Modernisation
                base += 2
            readiness.append(min(base, 95))
        return readiness
    
    def simulate_advanced_deterrence(self, annees):
        """Capacité de dissuasion avancée"""
        deterrence = []
        for annee in annees:
            base = 90  # Départ très élevé
            if annee >= 2001:
                base += 2  # Guerre contre le terrorisme
            if annee >= 2018:
                base += 3  # Compétition grandes puissances
            deterrence.append(min(base, 96))
        return deterrence
    
    def simulate_advanced_mobilization(self, annees):
        """Temps de mobilisation avancé"""
        return [max(30 - 1.0 * (annee - 2000), 7) for annee in annees]
    
    def simulate_joint_exercises(self, annees):
        """Exercices conjoints avec alliés"""
        exercises = []
        for annee in annees:
            if annee < 2001:
                exercises.append(50)
            elif annee < 2010:
                exercises.append(80 + (annee - 2001))
            else:
                exercises.append(100 + 3 * (annee - 2010))
        return exercises
    
    def simulate_tech_development(self, annees):
        """Développement technologique global"""
        return [min(80 + 1.5 * (annee - 2000), 95) for annee in annees]
    
    def simulate_naval_capacity(self, annees):
        """Capacité navale globale"""
        return [min(85 + 1.0 * (annee - 2000), 95) for annee in annees]
    
    def simulate_air_defense_coverage(self, annees):
        """Couverture de défense anti-aérienne"""
        return [min(80 + 1.2 * (annee - 2000), 94) for annee in annees]
    
    def simulate_alliance_cooperation(self, annees):
        """Coopération avec alliances"""
        return [min(75 + 1.0 * (annee - 2000), 92) for annee in annees]
    
    def simulate_cyber_capabilities(self, annees):
        """Capacités cybernétiques"""
        return [min(85 + 1.8 * (annee - 2000), 96) for annee in annees]
    
    def simulate_weapon_production(self, annees):
        """Production d'armements (indice)"""
        return [min(80 + 1.5 * (annee - 2000), 94) for annee in annees]
    
    def simulate_nato_exercises(self, annees):
        """Exercices OTAN"""
        return [min(40 + 2 * (annee - 2014), 80) for annee in annees if annee >= 2014] + [20] * (2014 - min(annees))
    
    def simulate_strategic_partnerships(self, annees):
        """Partenariats stratégiques"""
        return [min(60 + 1.5 * (annee - 2000), 88) for annee in annees]
    
    def simulate_foreign_bases(self, annees):
        """Bases militaires à l'étranger"""
        return [min(700 + 5 * (annee - 2000), 800) for annee in annees]
    
    def simulate_nuclear_arsenal(self, annees):
        """Arsenal nucléaire"""
        return [min(7000 - 50 * (annee - 2000), 5800) for annee in annees]
    
    def simulate_missile_range(self, annees):
        """Portée moyenne des missiles (km)"""
        return [min(12000 + 100 * (annee - 2000), 15000) for annee in annees]
    
    def simulate_nuclear_triad(self, annees):
        """Capacité de triade nucléaire"""
        return [min(95 + 0.2 * (annee - 2000), 98) for annee in annees]
    
    def simulate_aircraft_carriers(self, annees):
        """Porte-avions opérationnels"""
        return [min(11 + 0.1 * (annee - 2000), 12) for annee in annees]
    
    def simulate_submarines(self, annees):
        """Sous-marins stratégiques"""
        return [min(70 + 0.5 * (annee - 2000), 75) for annee in annees]
    
    def simulate_maritime_projection(self, annees):
        """Projection maritime"""
        return [min(90 + 0.5 * (annee - 2000), 96) for annee in annees]
    
    def simulate_defense_research(self, annees):
        """Recherche défense"""
        return [min(85 + 1.0 * (annee - 2000), 95) for annee in annees]
    
    def simulate_emerging_tech(self, annees):
        """Technologies émergentes"""
        return [min(80 + 1.8 * (annee - 2000), 94) for annee in annees]
    
    def simulate_weapon_exports(self, annees):
        """Exportations d'armes (milliards USD)"""
        return [min(15 + 0.8 * (annee - 2000), 35) for annee in annees]
    
    def display_advanced_header(self):
        """En-tête avancé avec plus d'informations"""
        st.markdown('<h1 class="main-header">🇺🇸 ANALYSE STRATÉGIQUE AVANCÉE - ÉTATS-UNIS</h1>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div style='text-align: center; background: linear-gradient(135deg, #0033A0, #B22234, #FFFFFF); 
            padding: 1rem; border-radius: 10px; color: white; margin: 1rem 0;'>
            <h3>🛡️ PUISSANCE MILITAIRE AMÉRICAINE - LEADERSHIP GLOBAL</h3>
            <p><strong>Analyse multidimensionnelle des capacités militaires et de la stratégie globale (2000-2027)</strong></p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_advanced_sidebar(self):
        """Sidebar avancé avec plus d'options"""
        st.sidebar.markdown("## 🎛️ PANEL DE CONTRÔLE AVANCÉ")
        
        # Sélection du type d'analyse
        type_analyse = st.sidebar.radio(
            "Mode d'analyse:",
            ["Vue d'Ensemble USA", "Analyse par Branche", "Alliances Stratégiques", "Scénarios Géopolitiques"]
        )
        
        if type_analyse == "Vue d'Ensemble USA":
            selection = st.sidebar.selectbox("Niveau d'analyse:", self.branches_options)
        elif type_analyse == "Analyse par Branche":
            selection = st.sidebar.selectbox("Branche militaire:", ["US Army", "US Navy", "US Air Force", "US Marine Corps", "US Space Force"])
        elif type_analyse == "Alliances Stratégiques":
            selection = st.sidebar.selectbox("Programme stratégique:", self.programmes_options)
        else:
            selection = "Scénarios Géopolitiques"
        
        # Options avancées
        st.sidebar.markdown("### 🔧 OPTIONS AVANCÉES")
        show_geopolitical = st.sidebar.checkbox("Contexte géopolitique", value=True)
        show_alliances = st.sidebar.checkbox("Analyse des alliances", value=True)
        show_technical = st.sidebar.checkbox("Détails techniques", value=True)
        threat_assessment = st.sidebar.checkbox("Évaluation des menaces", value=True)
        
        # Paramètres de simulation
        st.sidebar.markdown("### ⚙️ PARAMÈTRES DE SIMULATION")
        scenario = st.sidebar.selectbox("Scénario:", ["Leadership Global", "Compétition Grandes Puissances", "Guerre Limitée", "Défense Avancée"])
        
        return {
            'selection': selection,
            'type_analyse': type_analyse,
            'show_geopolitical': show_geopolitical,
            'show_alliances': show_alliances,
            'show_technical': show_technical,
            'threat_assessment': threat_assessment,
            'scenario': scenario
        }
    
    def display_strategic_metrics(self, df, config):
        """Métriques stratégiques avancées"""
        st.markdown('<h3 class="section-header">🎯 TABLEAU DE BORD STRATÉGIQUE ÉTATS-UNIS</h3>', 
                   unsafe_allow_html=True)
        
        derniere_annee = df['Annee'].max()
        data_actuelle = df[df['Annee'] == derniere_annee].iloc[0]
        data_2000 = df[df['Annee'] == 2000].iloc[0]
        
        # Première ligne de métriques
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <h4>💰 BUDGET DÉFENSE 2027</h4>
                <h2>{:.0f} Md$</h2>
                <p>📈 {:.1f}% du PIB américain</p>
            </div>
            """.format(data_actuelle['Budget_Defense_Mds'], data_actuelle['PIB_Militaire_Pourcent']), 
            unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card">
                <h4>👥 EFFECTIFS TOTAUX</h4>
                <h2>{:,.0f}K</h2>
                <p>⚔️ Professionnalisation avancée</p>
            </div>
            """.format(data_actuelle['Personnel_Milliers']), 
            unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="navy-card">
                <h4>☢️ TRIADE NUCLÉAIRE</h4>
                <h2>{:.0f}%</h2>
                <p>🚀 {} ogives stratégiques</p>
            </div>
            """.format(data_actuelle['Triade_Nucleaire'], 
                     int(data_actuelle.get('Stock_Ogives_Nucleaires', 0))), 
            unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="nato-card">
                <h4>🤝 LEADERSHIP ALLIANCES</h4>
                <h2>{:.0f}%</h2>
                <p>🌍 {} bases étrangères</p>
            </div>
            """.format(data_actuelle['Cooperation_Alliances'], 
                     int(data_actuelle.get('Bases_Etrangeres', 0))), 
            unsafe_allow_html=True)
        
        # Deuxième ligne de métriques
        col5, col6, col7, col8 = st.columns(4)
        
        with col5:
            reduction_temps = ((data_2000['Temps_Mobilisation_Jours'] - data_actuelle['Temps_Mobilisation_Jours']) / 
                             data_2000['Temps_Mobilisation_Jours']) * 100
            st.metric(
                "⏱️ Temps Mobilisation",
                f"{data_actuelle['Temps_Mobilisation_Jours']:.1f} jours",
                f"{reduction_temps:+.1f}%"
            )
        
        with col6:
            croissance_navale = ((data_actuelle['Capacite_Navale'] - data_2000['Capacite_Navale']) / 
                               data_2000['Capacite_Navale']) * 100
            st.metric(
                "🌊 Puissance Navale",
                f"{data_actuelle['Capacite_Navale']:.1f}%",
                f"{croissance_navale:+.1f}%"
            )
        
        with col7:
            if 'Portee_Missiles_Km' in df.columns:
                croissance_portee = ((data_actuelle['Portee_Missiles_Km'] - data_2000.get('Portee_Missiles_Km', 12000)) / 
                                   data_2000.get('Portee_Missiles_Km', 12000)) * 100
                st.metric(
                    "🎯 Portée Missiles Moyenne",
                    f"{data_actuelle['Portee_Missiles_Km']:,.0f} km",
                    f"{croissance_portee:+.1f}%"
                )
        
        with col8:
            st.metric(
                "📊 Préparation Opérationnelle",
                f"{data_actuelle['Readiness_Operative']:.1f}%",
                f"+{(data_actuelle['Readiness_Operative'] - data_2000['Readiness_Operative']):.1f}%"
            )
    
    def create_comprehensive_analysis(self, df, config):
        """Analyse complète multidimensionnelle"""
        st.markdown('<h3 class="section-header">📊 ANALYSE MULTIDIMENSIONNELLE ÉTATS-UNIS</h3>', 
                   unsafe_allow_html=True)
        
        # Graphiques principaux
        col1, col2 = st.columns(2)
        
        with col1:
            # Évolution des capacités principales
            fig = go.Figure()
            
            capacites = ['Readiness_Operative', 'Capacite_Dissuasion', 'Cyber_Capabilities', 'Cooperation_Alliances']
            noms = ['Préparation Opér.', 'Dissuasion Strat.', 'Capacités Cyber', 'Leadership Alliances']
            couleurs = ['#0033A0', '#B22234', '#4B0082', '#228B22']
            
            for i, (cap, nom, couleur) in enumerate(zip(capacites, noms, couleurs)):
                if cap in df.columns:
                    fig.add_trace(go.Scatter(
                        x=df['Annee'], y=df[cap],
                        mode='lines', name=nom,
                        line=dict(color=couleur, width=4),
                        hovertemplate=f"{nom}: %{{y:.1f}}%<extra></extra>"
                    ))
            
            fig.update_layout(
                title="📈 ÉVOLUTION DES CAPACITÉS STRATÉGIQUES USA (2000-2027)",
                xaxis_title="Année",
                yaxis_title="Niveau de Capacité (%)",
                height=500,
                template="plotly_white",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse des alliances stratégiques
            strategic_data = []
            strategic_names = []
            
            if 'Exercices_Conjoints' in df.columns:
                strategic_data.append(df['Exercices_Conjoints'])
                strategic_names.append('Exercices Conjoints')
            
            if 'Exercices_OTAN' in df.columns:
                strategic_data.append(df['Exercices_OTAN'])
                strategic_names.append('Exercices OTAN')
            
            if 'Partenariats_Strategiques' in df.columns:
                strategic_data.append(df['Partenariats_Strategiques'])
                strategic_names.append('Partenariats Strat.')
            
            if strategic_data:
                fig = make_subplots(specs=[[{"secondary_y": True}]])
                
                for i, (data, nom) in enumerate(zip(strategic_data, strategic_names)):
                    fig.add_trace(
                        go.Scatter(x=df['Annee'], y=data, name=nom,
                                 line=dict(width=4)),
                        secondary_y=(i > 0)
                    )
                
                fig.update_layout(
                    title="🤝 ALLIANCES STRATÉGIQUES - ÉVOLUTION COMPARÉE",
                    height=500,
                    template="plotly_white"
                )
                st.plotly_chart(fig, use_container_width=True)
    
    def create_geopolitical_analysis(self, df, config):
        """Analyse géopolitique avancée"""
        st.markdown('<h3 class="section-header">🌍 LEADERSHIP GLOBAL ÉTATS-UNIS</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Architecture géopolitique
            st.markdown("""
            <div class="navy-card">
                <h4>🏛️ ARCHITECTURE GÉOPOLITIQUE AMÉRICAINE</h4>
                <p><strong>OTAN:</strong> Leadership de l'alliance transatlantique</p>
                <p><strong>Pacifique:</strong> Réseau d'alliances (Japon, Corée du Sud, Australie)</p>
                <p><strong>Moyen-Orient:</strong> Partenariats stratégiques (Israël, Arabie Saoudite)</p>
                <p><strong>Amériques:</strong> Leadership continental via TIAR et OEA</p>
                <p><strong>Global:</strong> 750+ bases militaires dans 80+ pays</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Analyse des relations internationales
            st.markdown("""
            <div class="alliance-card">
                <h4>🌐 RELATIONS INTERNATIONALES</h4>
                <p><strong>Alliés:</strong> Réseau d'alliances le plus étendu au monde</p>
                <p><strong>Adversaires:</strong> Chine, Russie, Iran, Corée du Nord</p>
                <p><strong>Organisations:</strong> Leadership à l'ONU, FMI, Banque Mondiale</p>
                <p><strong>Économie:</strong> Dollar comme monnaie de réserve mondiale</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Projection de puissance globale
            projection_data = {
                'Région': ['Amérique du Nord', 'Europe', 'Asie-Pacifique', 
                          'Moyen-Orient', 'Amérique Latine', 'Afrique'],
                'Bases_Militaires': [120, 180, 220, 80, 50, 60],
                'Effectifs_Milliers': [450, 65, 85, 45, 15, 6],
                'Exercices_2023': [45, 38, 52, 25, 12, 8]
            }
            projection_df = pd.DataFrame(projection_data)
            
            fig = px.bar(projection_df, x='Région', y='Bases_Militaires',
                        title="🌍 PROJECTION DE PUISSANCE - BASES MILITAIRES PAR RÉGION",
                        color='Bases_Militaires',
                        color_continuous_scale='blues')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
            
            # Leadership technologique
            tech_data = {
                'Domaine': ['Aéronautique', 'Naval', 'Spatial', 'Cyber', 'Nucléaire', 'Renseignement'],
                'Avance_Technologique': [9, 9, 9, 9, 9, 9],  # sur 10
                'Depenses_RD_Mds': [45, 32, 28, 18, 25, 15]
            }
            tech_df = pd.DataFrame(tech_data)
            
            fig = px.scatter(tech_df, x='Depenses_RD_Mds', y='Avance_Technologique',
                           size='Depenses_RD_Mds', color='Domaine',
                           title="🚀 LEADERSHIP TECHNOLOGIQUE MILITAIRE",
                           size_max=30)
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
    
    def create_branch_analysis(self, df, config):
        """Analyse des capacités par branche"""
        st.markdown('<h3 class="section-header">⚔️ CAPACITÉS PAR BRANCHE MILITAIRE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Contributions des branches
            contributions_data = []
            for branche, data in self.military_capabilities.items():
                contributions_data.append({
                    'Branche': branche,
                    'Budget (Md$)': data['budget'],
                    'Personnel (K)': data['personnel'],
                    'Équipements Principaux': data.get('equipements', 'Non spécifié'),
                    'Technologies': data.get('technologies', 'Non spécifié')
                })
            
            contributions_df = pd.DataFrame(contributions_data)
            
            fig = px.bar(contributions_df, x='Branche', y='Budget (Md$)',
                        title="💰 RÉPARTITION BUDGÉTAIRE PAR BRANCHE",
                        color='Budget (Md$)',
                        color_continuous_scale='reds')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Spécialisations stratégiques
            st.markdown("""
            <div class="airforce-card">
                <h4>🎯 SPÉCIALISATIONS STRATÉGIQUES</h4>
                <p><strong>US Navy:</strong> Projection de puissance mondiale, contrôle des mers</p>
                <p><strong>US Air Force:</strong> Supériorité aérienne, frappe globale, espace</p>
                <p><strong>US Army:</strong> Puissance terrestre, occupation, stabilisation</p>
                <p><strong>US Marine Corps:</strong> Force expéditionnaire, intervention rapide</p>
                <p><strong>US Space Force:</strong> Domaine spatial, satellites, missile defense</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Avantages comparatifs
            advantages_data = {
                'Domaine': ['Puissance Navale', 'Supériorité Aérienne', 'Forces Terrestres', 
                           'Capacité Nucléaire', 'Cybersécurité', 'Renseignement', 'Espace'],
                'Score_USA': [10, 10, 9, 10, 10, 10, 10],
                'Score_Concurrents': [7, 8, 8, 9, 8, 8, 7]  # Meilleurs concurrents
            }
            advantages_df = pd.DataFrame(advantages_data)
            
            fig = go.Figure(data=[
                go.Bar(name='États-Unis', x=advantages_df['Domaine'], y=advantages_df['Score_USA']),
                go.Bar(name='Meilleurs Concurrents', x=advantages_df['Domaine'], y=advantages_df['Score_Concurrents'])
            ])
            fig.update_layout(title="📊 AVANTAGES COMPARATIFS STRATÉGIQUES (0-10)",
                             barmode='group', height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    def create_technical_analysis(self, df, config):
        """Analyse technique détaillée"""
        st.markdown('<h3 class="section-header">🔬 ANALYSE TECHNIQUE AVANCÉE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Analyse des systèmes d'armes avancés
            systems_data = {
                'Système': ['F-35 Lightning II', 'B-21 Raider', 'Gerald R. Ford', 
                           'Columbia Class', 'DDG(X)', 'Ground Based Strategic Deterrent',
                           'Hypersonic Strike', 'Space Fence'],
                'Portée/Puissance': [2200, 15000, 100000, 12000, 9000, 13000, 5000, 36000],
                'Branche': ['Air Force', 'Air Force', 'Navy', 'Navy', 'Navy', 'Air Force', 'Multi', 'Space Force'],
                'Statut': ['Opérationnel', 'Développement', 'Opérationnel', 'Développement', 'Développement', 'Développement', 'Test', 'Opérationnel']
            }
            systems_df = pd.DataFrame(systems_data)
            
            fig = px.scatter(systems_df, x='Portée/Puissance', y='Branche', 
                           size='Portée/Puissance', color='Branche',
                           hover_name='Système', log_x=True,
                           title="🚀 SYSTÈMES D'ARMES AVANCÉS DES ÉTATS-UNIS",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse de la supériorité technologique
            superiority_data = {
                'Domaine': ['Aviation 5e Génération', 'Porte-avions Nucléaires', 
                          'Sous-marins Furtifs', 'Missiles Hypersoniques',
                          'Guerre Cyber Offensive', 'Surveillance Spatiale'],
                'Avance_Annees': [15, 20, 10, 2, 5, 10],
                'Depenses_RD_Mds': [120, 45, 30, 8, 12, 15]
            }
            superior_df = pd.DataFrame(superiority_data)
            
            fig = go.Figure()
            fig.add_trace(go.Bar(name='Avance (années)', x=superior_df['Domaine'], 
                                y=superior_df['Avance_Annees'],
                                marker_color='#0033A0'))
            fig.add_trace(go.Scatter(name='Dépenses R&D (Md$)', x=superior_df['Domaine'], 
                                   y=superior_df['Depenses_RD_Mds'],
                                   yaxis='y2', mode='lines+markers',
                                   line=dict(color='#B22234', width=3)))
            
            fig.update_layout(title="📈 SUPÉRIORITÉ TECHNOLOGIQUE ET INVESTISSEMENTS",
                             yaxis2=dict(title='Dépenses R&D (Md$)', overlaying='y', side='right'),
                             height=500)
            st.plotly_chart(fig, use_container_width=True)
            
            # Innovations en cours
            st.markdown("""
            <div class="alliance-card">
                <h4>🚀 INNOVATIONS TECHNOLOGIQUES EN COURS</h4>
                <p><strong>IA Militaire:</strong> Maven Project, systèmes autonomes</p>
                <p><strong>Énergie Dirigée:</strong> Lasers tactiques, armes à micro-ondes</p>
                <p><strong>Guerre Cyber:</strong> USCYBERCOM, capacités offensives</p>
                <p><strong>Espace:</strong> USSF, systèmes anti-satellites</p>
                <p><strong>Biotechnologie:</strong> Améliorations cognitives, protection CBRN</p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_alliance_analysis(self, config):
        """Analyse des alliances stratégiques"""
        st.markdown('<h3 class="section-header">🤝 ANALYSE DES ALLIANCES STRATÉGIQUES</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Réseau d'alliances
            alliance_data = {
                'Alliance': ['OTAN', 'ANZUS', 'Traité de Sécurité Japon-USA', 
                            'Corée du Sud-USA', 'Israel-USA', 'Arabie Saoudite-USA',
                            'QUAD', 'AUKUS'],
                'Membres': [32, 3, 2, 2, 2, 2, 4, 3],
                'Année_Création': [1949, 1951, 1960, 1953, 1981, 1945, 2007, 2021],
                'Niveau_Coopération': [9, 8, 9, 9, 10, 8, 7, 8]  # sur 10
            }
            alliance_df = pd.DataFrame(alliance_data)
            
            fig = px.scatter(alliance_df, x='Année_Création', y='Niveau_Coopération',
                           size='Membres', color='Alliance',
                           title="🌐 RÉSEAU D'ALLIANCES STRATÉGIQUES",
                           size_max=30)
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Avantages des alliances
            st.markdown("""
            <div class="nato-card">
                <h4>🏆 AVANTAGES STRATÉGIQUES DES ALLIANCES</h4>
                <p><strong>Accès aux bases:</strong> 750+ bases à travers le monde</p>
                <p><strong>Interopérabilité:</strong> Standards communs avec 50+ pays</p>
                <p><strong>Partage du fardeau:</strong> 2% du PIB des alliés OTAN</p>
                <p><strong>Légitimité:</strong> Actions multilatérales approuvées</p>
                <p><strong>Renseignement:</strong> Partage avec Five Eyes et au-delà</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Domaines de coopération future
            future_coop_data = {
                'Domaine': ['Defense Missile Globale', 'Guerre Cyber Collective', 
                           'Espace Militaire', 'Guerre Électronique',
                           'Renseignement Artificiel', 'Exercices Conjoints Avancés'],
                'Potentiel': [9, 10, 8, 9, 10, 9]  # sur 10
            }
            future_coop_df = pd.DataFrame(future_coop_data)
            
            fig = px.bar(future_coop_df, x='Domaine', y='Potentiel',
                        title="🔮 POTENTIEL DE COOPÉRATION FUTURE",
                        color='Potentiel',
                        color_continuous_scale='reds')
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
    
    def create_threat_assessment(self, df, config):
        """Évaluation avancée des menaces"""
        st.markdown('<h3 class="section-header">⚠️ ÉVALUATION STRATÉGIQUE DES MENACES</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Matrice des menaces avancées
            threats_data = {
                'Type de Menace': ['Rivalité Chine', 'Confrontation Russie', 
                                 'Guerre Cyber Majeure', 'Prolifération Nucléaire',
                                 'Terrorisme Global', 'Instabilité Moyen-Orient',
                                 'Course Spatiale', 'Crise Taïwan'],
                'Probabilité': [0.9, 0.7, 0.8, 0.6, 0.5, 0.8, 0.7, 0.6],
                'Impact': [0.9, 0.8, 0.7, 0.8, 0.6, 0.7, 0.6, 0.9],
                'Niveau_Preparation': [0.8, 0.7, 0.9, 0.6, 0.9, 0.7, 0.8, 0.7]
            }
            threats_df = pd.DataFrame(threats_data)
            
            fig = px.scatter(threats_df, x='Probabilité', y='Impact', 
                           size='Niveau_Preparation', color='Type de Menace',
                           title="🎯 MATRICE RISQUES - PROBABILITÉ VS IMPACT",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Capacités de réponse par domaine
            response_data = {
                'Scénario': ['Conflit Hauturier Chine', 'Crise Ukraine/Russie', 
                           'Attaque Cyber Majeure', 'Crise Nucléaire Corée Nord',
                           'Crise Détroit Taïwan', 'Terrorisme Global'],
                'Puissance_Navale': [0.9, 0.7, 0.3, 0.6, 0.9, 0.4],
                'Supériorité_Aérienne': [0.8, 0.8, 0.2, 0.7, 0.9, 0.6],
                'Cybersécurité': [0.6, 0.5, 0.9, 0.4, 0.5, 0.7],
                'Alliances': [0.7, 0.9, 0.6, 0.5, 0.7, 0.8]
            }
            response_df = pd.DataFrame(response_data)
            
            fig = go.Figure(data=[
                go.Bar(name='Puissance Navale', x=response_df['Scénario'], y=response_df['Puissance_Navale']),
                go.Bar(name='Supériorité Aérienne', x=response_df['Scénario'], y=response_df['Supériorité_Aérienne']),
                go.Bar(name='Cybersécurité', x=response_df['Scénario'], y=response_df['Cybersécurité']),
                go.Bar(name='Alliances', x=response_df['Scénario'], y=response_df['Alliances'])
            ])
            fig.update_layout(title="🛡️ CAPACITÉS DE RÉPONSE PAR DOMAINE",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        # Recommandations stratégiques
        st.markdown("""
        <div class="alliance-card">
            <h4>🎯 RECOMMANDATIONS STRATÉGIQUES ÉTATS-UNIS</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div><strong>• Modernisation nucléaire:</strong> Triade nouvelle génération</div>
                <div><strong>• Innovation technologique:</strong> Maintien de l'avance qualitative</div>
                <div><strong>• Renforcement naval:</strong> 355+ navires pour contrer la Chine</div>
                <div><strong>• Cybersécurité offensive:</strong> Capacités de préemption</div>
                <div><strong>• Leadership spatial:</strong> US Space Force et domaines connexes</div>
                <div><strong>• Consolidation alliances:</strong> OTAN élargi, QUAD renforcé</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_alliance_database(self):
        """Base de données des alliances stratégiques"""
        st.markdown('<h3 class="section-header">🤝 BASE DE DONNÉES DES ALLIANCES STRATÉGIQUES</h3>', 
                   unsafe_allow_html=True)
        
        alliance_data = []
        for nom, specs in self.alliance_projects.items():
            alliance_data.append({
                'Projet': nom,
                'Pays Participants': specs['pays'],
                'Type': specs['type'],
                'Statut': specs['statut'],
                'Détails': specs.get('objectif', specs.get('localisation', specs.get('technologies', 'N/A')))
            })
        
        alliance_df = pd.DataFrame(alliance_data)
        
        # Affichage interactif
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig = px.treemap(alliance_df, path=['Type', 'Projet'],
                            title="🤝 CARTE DES ALLIANCES STRATÉGIQUES",
                            color='Type')
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class="nato-card">
                <h4>📋 PROJETS STRATÉGIQUES</h4>
            """, unsafe_allow_html=True)
            
            for projet in alliance_data:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.1); padding: 0.5rem; margin: 0.2rem 0; border-radius: 5px;">
                    <strong>{projet['Projet']}</strong><br>
                    🌍 {projet['Pays Participants']} • 🎯 {projet['Type']}<br>
                    📊 {projet['Statut']} • 📝 {projet['Détails']}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    def run_advanced_dashboard(self):
        """Exécute le dashboard avancé complet"""
        # Sidebar avancé
        controls = self.create_advanced_sidebar()
        
        # Header avancé
        self.display_advanced_header()
        
        # Génération des données avancées
        df, config = self.generate_advanced_data(controls['selection'])
        
        # Navigation par onglets avancés
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
            "📊 Tableau de Bord", 
            "🔬 Analyse Technique", 
            "🌍 Leadership Global", 
            "⚔️ Branches Militaires",
            "⚠️ Évaluation Menaces",
            "🤝 Alliances Stratégiques",
            "💎 Synthèse Stratégique"
        ])
        
        with tab1:
            self.display_strategic_metrics(df, config)
            self.create_comprehensive_analysis(df, config)
        
        with tab2:
            self.create_technical_analysis(df, config)
        
        with tab3:
            if controls['show_geopolitical']:
                self.create_geopolitical_analysis(df, config)
        
        with tab4:
            self.create_branch_analysis(df, config)
        
        with tab5:
            if controls['threat_assessment']:
                self.create_threat_assessment(df, config)
        
        with tab6:
            if controls['show_alliances']:
                self.create_alliance_database()
        
        with tab7:
            self.create_strategic_synthesis(df, config, controls)
    
    def create_strategic_synthesis(self, df, config, controls):
        """Synthèse stratégique finale"""
        st.markdown('<h3 class="section-header">💎 SYNTHÈSE STRATÉGIQUE - ÉTATS-UNIS</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="navy-card">
                <h4>🏆 AVANTAGES STRATÉGIQUES DÉCISIFS</h4>
                <div style="margin-top: 1rem;">
                    <div class="airforce-card" style="margin: 0.5rem 0;">
                        <strong>🌍 Projection de Puissance Globale</strong>
                        <p>11 porte-avions, 750+ bases étrangères, réseau d'alliances mondial</p>
                    </div>
                    <div class="army-card" style="margin: 0.5rem 0;">
                        <strong>🚀 Supériorité Technologique</strong>
                        <p>Leadership dans tous les domaines critiques (5e génération, cyber, espace)</p>
                    </div>
                    <div class="marines-card" style="margin: 0.5rem 0;">
                        <strong>💰 Capacité Budgétaire Inégalée</strong>
                        <p>Budget de défense supérieur aux 10 pays suivants combinés</p>
                    </div>
                    <div class="nato-card" style="margin: 0.5rem 0;">
                        <strong>🤝 Réseau d'Alliances</strong>
                        <p>Leadership de l'OTAN et partenariats stratégiques mondiaux</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="alliance-card">
                <h4>🎯 DÉFIS STRATÉGIQUES</h4>
                <div style="margin-top: 1rem;">
                    <div class="alliance-card" style="margin: 0.5rem 0;">
                        <strong>🇨🇳 Montée en Puissance Chinoise</strong>
                        <p>Compétition systémique dans tous les domaines</p>
                    </div>
                    <div class="alliance-card" style="margin: 0.5rem 0;">
                        <strong>🇷🇺 Revanchisme Russe</strong>
                        <p>Capacités nucléaires modernisées et guerre hybride</p>
                    </div>
                    <div class="alliance-card" style="margin: 0.5rem 0;">
                        <strong>💻 Vulnérabilités Cyber</strong>
                        <p>Dépendance croissante aux systèmes informatiques</p>
                    </div>
                    <div class="alliance-card" style="margin: 0.5rem 0;">
                        <strong>📉 Pressions Budgétaires</strong>
                        <p>Dette nationale et compétition pour les ressources</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Perspectives futures
        st.markdown("""
        <div class="metric-card">
            <h4>🔮 PERSPECTIVES STRATÉGIQUES 2027-2035</h4>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🔄 RÉORIENTATION STRATÉGIQUE</h5>
                    <p>• Pivot vers l'Indo-Pacifique<br>• Modernisation de la triade nucléaire<br>• Renforcement des capacités cyber<br>• Maintien de la supériorité technologique</p>
                </div>
                <div>
                    <h5>🤝 CONSOLIDATION ALLIANCES</h5>
                    <p>• OTAN élargi et renforcé<br>• Partenariats QUAD et AUKUS<br>• Nouveaux partenariats asiatiques<br>• Coopération spatiale élargie</p>
                </div>
                <div>
                    <h5>🚀 INNOVATION ACCÉLÉRÉE</h5>
                    <p>• Intelligence artificielle militaire<br>• Systèmes autonomes et robots<br>• Armes à énergie dirigée<br>• Supériorité dans les domaines émergents</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Recommandations finales
        st.markdown("""
        <div class="navy-card">
            <h4>🎖️ RECOMMANDATIONS STRATÉGIQUES FINALES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🛡️ MAINTIEN DE LA SUPÉRIORITÉ</h5>
                    <p>• Investissement continu dans la R&D de défense<br>
                    • Modernisation accélérée des capacités nucléaires<br>
                    • Expansion des forces navales à 355+ navires<br>
                    • Dominance dans les domaines cyber et spatial</p>
                </div>
                <div>
                    <h5>🌍 LEADERSHIP GLOBAL</h5>
                    <p>• Renforcement du réseau d'alliances<br>
                    • Coopération technologique avec les alliés<br>
                    • Promotion de l'ordre international libéral<br>
                    • Contrôle des biens communs globaux (mers, espace)</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Lancement du dashboard avancé
if __name__ == "__main__":
    dashboard = DefenseUSADashboardAvance()
    dashboard.run_advanced_dashboard()