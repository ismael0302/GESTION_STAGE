from odoo import http
from odoo.http import request

class StageDashboardController(http.Controller):

    @http.route('/gestion_stage/dashboard', type='http', auth='user', website=False)
    def stage_dashboard(self, **kw):
        Stage = request.env['gestion.stage']
        total = Stage.search_count([])
        en_attente = Stage.search_count([('state', '=', 'en_attente')])
        accepte = Stage.search_count([('state', '=', 'accepte')])
        rejete = Stage.search_count([('state', '=', 'rejete')])

        stages_par_tuteur = request.env['gestion.stage'].read_group(
            [('tutor', '!=', False)],
            ['tutor'],
            ['tutor']
        )

        return request.render('gestion_stage.template_stage_dashboard', {
            'total': total,
            'en_attente': en_attente,
            'accepte': accepte,
            'rejete': rejete,
            'stages_par_tuteur': stages_par_tuteur
        })
        
        