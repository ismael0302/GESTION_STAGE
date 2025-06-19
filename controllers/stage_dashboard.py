from odoo import http
from odoo.http import request
from datetime import date

class StageDashboardController(http.Controller):

    @http.route('/gestion_stage/dashboard', type='http', auth='user', website=False)
    def stage_dashboard(self, **kw):
        Stage = request.env['gestion.stage']
        today = date.today()

        total = Stage.search_count([])
        en_attente = Stage.search_count([('statut', '=', 'en_attente')])
        accepte = Stage.search_count([('statut', '=', 'accepte')])
        rejete = Stage.search_count([('statut', '=', 'rejete')])
        
        # ➕ Nombre de stagiaires en cours
        en_cours = Stage.search_count([
            ('date_debut', '<=', today),
            ('date_fin', '>=', today)
        ])

        stages_par_tuteur = Stage.read_group(
            [('tuteur_id', '!=', False)],
            ['tuteur_id'],
            ['tuteur_id']
        )

        return request.render('gestion_stage.template_stage_dashboard', {
            'total': total,
            'en_attente': en_attente,
            'accepte': accepte,
            'rejete': rejete,
            'en_cours': en_cours,
            'stages_par_tuteur': stages_par_tuteur,
        })
        
        # Répartition par service
        repartition_service = Stage.read_group(
            [('service_id', '!=', False)],
            ['service_id'],
            ['service_id'])
