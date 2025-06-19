# -*- coding: utf-8 -*-

from odoo import models, fields

class JournalBord(models.Model):
    _name = 'gestion.journal'
    _description = "Journal de Bord / Rapport d’Activité"

    date = fields.Date(string="Date", default=fields.Date.today)
    activite = fields.Text(string="Activité réalisée")
    temps_passe = fields.Float(string="Temps passé (heures)", help="Durée approximative")
    lieu = fields.Char(string="Lieu")
    stage_id = fields.Many2one('gestion.stage', string="Stage concerné", ondelete="cascade")
