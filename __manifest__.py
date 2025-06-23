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
        'security/groups.xml',
        'security/ir_rule.xml',
        'security/ir.model.access.csv',
        'views/stage_view.xml',
        'views/menus_view.xml',
        'views/planification_view.xml',
        'views/tache_view.xml',
        'views/suivi_view.xml',
        'views/journal_view.xml',
        'views/evaluation_view.xml',
        'views/grille_view.xml',
        'views/attestation_template.xml',
        'report/reports.xml',
        'views/stage_dashboard_view.xml',
        'views/stage_dashboard_template.xml',
        'views/service_views.xml',
        'views/stage_graph_views.xml',
        
        
    ],
    'qweb': [
        'views/stage_dashboard_template.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'gestion_stage/static/src/js/stage_dashboard.js',
            'gestion_stage/static/src/xml/stage_dashboard_template.xml',
            ],
        },


    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}
