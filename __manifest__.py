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
    ],
    
    'installable': True,
    'application': True,
}
