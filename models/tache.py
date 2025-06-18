# -*- coding: utf-8 -*-

from odoo import models, fields

class Tache(models.Model):
    _name = 'gestion.tache'
    _description = 'Tâche à réaliser'

    name = fields.Char(
        string="Nom de la tâche", 
        required=True)
    
    description = fields.Text(string="Description")
    date_debut = fields.Date(string="Date de début")
    date_fin = fields.Date(string="Date de fin")
    
    stage_id = fields.Many2one(
        'gestion.stage', 
        string="Stagaire concerné", 
        ondelete='cascade')
    
    state = fields.Selection([
        ('non_demarre', 'Non démarrée'),
        ('en_cours', 'En cours'),
        ('terminee', 'Terminée'),
    ], string="Statut", default='non_demarre')
    
    # action du boutons save  
    def action_sauvegarder_stage(self):
        # Par défaut, on suppose que l'utilisateur a déjà cliqué "Créer"
        # On peut ici faire des vérifications supplémentaires
        if not self.name:
            raise UserError("Le nom du stage est obligatoire.")
        # Tu peux aussi lancer d'autres actions ici si nécessaire
        return True
