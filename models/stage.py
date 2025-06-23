# -*- coding: utf-8 -*-
import random
import string
from datetime import datetime, date
from odoo import api, fields, models, exceptions
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from collections import defaultdict

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
    
    service_id = fields.Many2one('gestion.service', string="Service")
    
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
    # fonction des etapt du statu
    
    def action_accepter(self):
        for record in self:
            record.state = 'accepted'

    def action_rejeter(self):
        for record in self:
            record.state = 'rejected'

    def action_valider(self):
        for record in self:
            record.state = 'in_progress'

    def action_terminer(self):
        for record in self:
            record.state = 'completed'

    def action_annuler(self):
        for record in self:
            record.state = 'canceled'

    tutor = fields.Many2one(
        'hr.employee',
        string="Tuteur en entreprise",
        help="Employé de l'entreprise qui encadre le stagiaire")
    
    user_id = fields.Many2one('res.users', string="Utilisateur")

    tutor_id = fields.Many2one('res.partner', string="Tuteur")

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
    
    evaluation_ids = fields.One2many(
        'gestion.evaluation', 
        'stage_id', 
        string="Évaluations finales")
    
    grille_id = fields.One2many(
        'gestion.grille', 'stage_id', 
        string="Grille de notation")

    
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
    
    






# les fonction 
class GestionStage(models.Model):
    _inherit = 'gestion.stage'  # on étend le modèle existant

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        user = self.env.user
        if not user.has_group('base.group_system'):
            args = args + [('tutor_id', '=', user.id)]
        return super(GestionStage, self).search(args, offset=offset, limit=limit, order=order, count=count)


    def stagiaires_group_by_state(self):
            grouped = defaultdict(self.env['gestion.stage'].browse)

            # Récupère tous les stages
            stages = self.search([])

            # Regroupe les stages par état
            result = defaultdict(list)
            for stage in stages:
                result[stage.state].append(stage)

            # Convertir en dictionnaire de recordsets
            grouped = {state: self.browse([stage.id for stage in stages]) for state, stages in result.items()}
            return grouped
        
    @api.model
    def create(self, vals):
        # Si aucun service n'est fourni, affecter un service par défaut
        if not vals.get('service_id'):
            # Exemple : on affecte le service ayant un nom spécifique
            service = self.env['gestion.service'].search([('name', '=', 'Informatique')], limit=1)
            if service:
                vals['service_id'] = service.id

        return super(GestionStage, self).create(vals)

    #nombre de stagaire en cours 
    def count_stagiaires_en_cours(self):
        return self.search_count([('state', '=', 'en_cours')])
    
    # fonction imprime l'attestation uniquement pour les stage terminer
    def action_print_attestation(self):
        # Vérifie que tous les stages sélectionnés sont terminés
        if any(stage.state != 'completed' for stage in self):
            raise UserError("L'attestation ne peut être imprimée que pour les stages terminés.")

        # Lance le rapport QWeb (remplace 'module_name' par ton module)
        return self.env.ref('gestion.stage.action_report_attestation_stage').report_action(self)