# -*- coding: utf-8 -*-
import random
import string
from datetime import datetime, date
from odoo import api, fields, models, exceptions
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError


class Stage(models.Model):
    _name = 'gestion.stage'
    _description = 'Stage en entreprise'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string='Nom du stagiaire',
        required=True)
    
    contact = fields.Char(
        string="Contact du Stagiaire",
        help="Numéro de téléphone ou email du stagiaire")
    
    cv = fields.Binary(
        string="CV du Stagiaire",
        attachment=True,
        help="Curriculum Vitae du stagiaire") 
    
    cv_filename = fields.Char(
        string="Nom du fichier CV",
        invisible=True) # Rendu invisible 
    
    school = fields.Char(
        string="École / Université",
        help="Établissement scolaire d'origine du stagiaire")
    
    specialty = fields.Char(
        string="Spécialité / Formation",
        help="Domaine d'études ou spécialité du stagiaire")
    
    service_id = fields.Many2one('hr.department', string="Service")

    
    date_debut = fields.Date(string='Date de début')
    date_fin = fields.Date(string='Date de fin')

    state = fields.Selection([
            ('pending', 'En attente'),
            ('accepted', 'Accepté'),
            ('rejected', 'Rejeté'), # Statut rejeté 
            ('in_progress', 'En cours'),
            ('completed', 'Terminé'),
            ('canceled', 'Annulé'),
        ], string="Statut du Stage",
            default='pending',
            tracking=True, required=True,
            help="Statut actuel du processus de stage") 

    tutor = fields.Many2one(
        'hr.employee',
        string="Tuteur en entreprise",
        help="Employé de l'entreprise qui encadre le stagiaire")
    
    
    planification_ids = fields.One2many(
        'gestion.planification', 
        'stage_id', 
        string="Planifications")
    
    stage_id = fields.Many2one(
        'gestion.stage', 
        string="Stage")
    
    tache_ids = fields.One2many(
        'gestion.tache', 
        'stage_id', string="Tâches")
    
    suivi_ids = fields.One2many(
        'gestion.suivi', 'stage_id', 
        string="Suivis")
    
    journal_ids = fields.One2many(
        'gestion.journal', 'stage_id', 
        string="Journaux de bord")
    
    evaluation_ids = fields.One2many('gestion.evaluation', 'stage_id', string="Évaluations finales")
    grille_id = fields.One2many('gestion.grille', 'stage_id', string="Grille de notation")

    
    # action du boutons save  
    def action_sauvegarder_stage(self):
        # Par défaut, on suppose que l'utilisateur a déjà cliqué "Créer"
        # On peut ici faire des vérifications supplémentaires
        if not self.name:
            raise UserError("Le nom du stage est obligatoire.")
        # Tu peux aussi lancer d'autres actions ici si nécessaire
        return True
    
    # action genere l'attestaion de stage 
    def print_attestation_stage(self):
        if not self:
            raise UserError("Aucun stage sélectionné.")
        return self.env.ref('gestion_stage.action_attestation_stage_pdf').report_action(self)




