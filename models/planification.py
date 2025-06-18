# -*- coding: utf-8 -*-
from odoo import models, fields

class Planification(models.Model):
    _name = 'gestion.planification'
    _description = 'Planification du stage'

    stage_id = fields.Many2one('gestion.stage', string="Stagaire", required=True, ondelete='cascade')
    tutor = fields.Many2one(
        'hr.employee',
        string="Tuteur en entreprise",
        help="Employé de l'entreprise qui encadre le stagiaire")
    date_debut = fields.Date(string="Date de début")
    date_fin = fields.Date(string="Date de fin")
    taches = fields.Text(string="Tâches planifiées")