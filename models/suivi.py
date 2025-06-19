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
    
    # Évaluation intermédiaire par le tuteur
    ponctualite = fields.Selection([
        ('mauvais', 'Mauvais'), 
        ('moyen', 'Moyen'),
        ('bon', 'Bon'), 
        ('excellent', 'Excellent')], string="Ponctualité")

    consignes = fields.Selection([
        ('mauvais', 'Mauvais'), 
        ('moyen', 'Moyen'), 
        ('bon', 'Bon'), 
        ('excellent', 'Excellent')], string="Respect des consignes")

    qualite_travail = fields.Selection([
        ('mauvais', 'Mauvais'), 
        ('moyen', 'Moyen'), 
        ('bon', 'Bon'), 
        ('excellent', 'Excellent')], string="Qualité du travail")

    autonomie = fields.Selection([
        ('mauvais', 'Mauvais'), 
        ('moyen', 'Moyen'), 
        ('bon', 'Bon'), 
        ('excellent', 'Excellent')], string="Autonomie")

    communication = fields.Selection([
        ('mauvais', 'Mauvais'), 
        ('moyen', 'Moyen'),
        ('bon', 'Bon'), 
        ('excellent', 'Excellent')], string="Communication")

    note_globale = fields.Selection([
        ('non_evalue', 'Non évalué'), 
        ('passable', 'Passable'), 
        ('bien', 'Bien'), 
        ('tres_bien', 'Très bien'), 
        ('excellent', 'Excellent')], string="Note globale", default='non_evalue')
