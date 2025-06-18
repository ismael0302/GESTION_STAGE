# -*- coding: utf-8 -*-
from odoo import models, fields

class Planification(models.Model):
    _name = 'gestion.planification'
    _description = 'Planification du stage'

    stage_id = fields.Many2one(
        'gestion.stage', 
        string="Stagaire", 
        required=True, 
        ondelete='cascade')
    
    tutor = fields.Many2one(
        'hr.employee',
        string="Tuteur en entreprise",
        help="Employé de l'entreprise qui encadre le stagiaire")
    
    date_debut = fields.Date(string="Date de début")
    date_fin = fields.Date(string="Date de fin")
    taches = fields.Text(string="Tâches planifiées")
    
    # action du boutons save  
    def action_sauvegarder_stage(self):
        # Par défaut, on suppose que l'utilisateur a déjà cliqué "Créer"
        # On peut ici faire des vérifications supplémentaires
        if not self.name:
            raise UserError("Le nom du stage est obligatoire.")
        # Tu peux aussi lancer d'autres actions ici si nécessaire
        return True