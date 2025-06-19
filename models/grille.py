from odoo import models, fields, api

class GrilleNotation(models.Model):
    _name = 'gestion.grille'
    _description = 'Grille de notation du stage'

    stage_id = fields.Many2one('gestion.stage', string="Stage concerné", required=True, ondelete="cascade")

    ponctualite = fields.Integer(string="Ponctualité (/10)")
    autonomie = fields.Integer(string="Autonomie (/10)")
    communication = fields.Integer(string="Communication (/10)")
    initiative = fields.Integer(string="Esprit d’initiative (/10)")
    qualite_travail = fields.Integer(string="Qualité du travail (/10)")

    note_totale = fields.Float(string="Note totale", compute="_compute_note_totale", store=True)
    commentaire = fields.Text(string="Commentaire global")

    @api.depends('ponctualite', 'autonomie', 'communication', 'initiative', 'qualite_travail')
    def _compute_note_totale(self):
        for record in self:
            notes = [
                record.ponctualite or 0,
                record.autonomie or 0,
                record.communication or 0,
                record.initiative or 0,
                record.qualite_travail or 0
            ]
            record.note_totale = sum(notes) / 5 if any(notes) else 0
