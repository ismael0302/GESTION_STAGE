#-*-* coding: utf-8 -*-

from odoo import models, fields

class EvaluationFinale(models.Model):
    _name = 'gestion.evaluation'
    _description = "Évaluation Finale du Stage"

    date = fields.Date(string="Date d'évaluation", default=fields.Date.today)
    stage_id = fields.Many2one('gestion.stage', string="Stage concerné", required=True, ondelete="cascade")

    competences = fields.Selection([
        ('faible', 'Faible'),
        ('moyen', 'Moyen'),
        ('bon', 'Bon'),
        ('excellent', 'Excellent'),
    ], string="Compétences acquises")

    comportement = fields.Selection([
        ('insatisfaisant', 'Insatisfaisant'),
        ('satisfaisant', 'Satisfaisant'),
        ('très_satisfaisant', 'Très satisfaisant'),
    ], string="Comportement professionnel")

    performance = fields.Selection([
        ('faible', 'Faible'),
        ('moyenne', 'Moyenne'),
        ('élevée', 'Élevée'),
    ], string="Performance")

    note_finale = fields.Selection([
        ('non_evalue', 'Non évalué'),
        ('passable', 'Passable'),
        ('bien', 'Bien'),
        ('très_bien', 'Très bien'),
        ('excellent', 'Excellent'),
    ], string="Note finale", default='non_evalue')

    commentaire = fields.Text(string="Appréciation générale")
