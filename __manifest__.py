# -*- coding: utf-8 -*-

{
    'name': 'Gestion des Stages',
    'version': '1.0',
    'summary': "Module pour gérer les stages en entreprise, de la candidature à l'évaluation finale",
    
    'description': """Ce module permet la gestion complète des stages :
        - Candidatures avec informations stagiaire
        - Planification avec tuteur et période
        - Suivi du stage (journal, évaluations intermédiaires)
        - Évaluation finale avec grille de notation
        - Attestation PDF automatique
        - Tableau de bord avec statistiques des stages""",
        
    'category': 'Human Resources',
    'author': 'ISMAEL_TASSU',
    'depends': ['base','hr','mail'],
    
    'data': [
        'security/ir.model.access.csv',
        'views/stage_view.xml',
        'views/menus_view.xml',
        'views/planification_view.xml',
        'views/tache_view.xml',
        'views/suivi_view.xml',
        'views/journal_view.xml',
        'views/evaluation_view.xml',
        'views/grille_view.xml',
        'report/attestation_template.xml',
        'report/report.xml',
        #'views/stage_dashboard_view.xml',
    ],
    
    'qweb': [
        #'views/stage_dashboard_template.xml',
    ],


    'installable': True,
    'application': True,
}
