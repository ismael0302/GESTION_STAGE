from odoo import models, fields

class GestionService(models.Model):
    _name = 'gestion.service'
    _description = 'Service dans l\'entreprise'

    name = fields.Char(string="Nom du service", required=True)
    responsable = fields.Char(string="Responsable")