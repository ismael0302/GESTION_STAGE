# -*- coding: utf-8 -*-
from odoo import models, fields

class SuiviStage(models.Model):
    _name = 'gestion.suivi'
    _description = 'Suivi du stage'

    date_suivi = fields.Date(
        string="Date", 
        default=fields.Date.today)
    
    commentaire = fields.Text(string="Commentaire / Observation")
    
    evaluation = fields.Selection([
        ('faible', 'Faible'),
        ('moyen', 'Moyen'),
        ('bon', 'Bon'),
        ('excellent', 'Excellent')
    ], string="Évaluation", default='moyen')
    
    stage_id = fields.Many2one(
        'gestion.stage', 
        string="Stage concerné", 
        ondelete='cascade')

