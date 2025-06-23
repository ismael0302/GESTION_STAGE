from odoo import http
from odoo.http import request

class StageDashboardController(http.Controller):

    @http.route('/gestion_stage/dashboard', type='http', auth='user', website=False)
    def stage_dashboard(self, **kw):
        Stage = request.env['gestion.stage'].sudo()
        total = Stage.search_count([])
        pending = Stage.search_count([('state', '=', 'pending')])
        accepted = Stage.search_count([('state', '=', 'accepted')])
        rejected = Stage.search_count([('state', '=', 'rejected')])

        stages_par_tutor = Stage.read_group(
            [('tutor_id', '!=', False)],
            ['tutor_id'],
            ['tutor_id']
        )

        all_stages = Stage.search([])

        return request.render('gestion_stage.template_stage_dashboard', {
            'total': total,
            'pending': pending,
            'accepted': accepted,
            'rejected': rejected,
            'stages_par_tutor': stages_par_tutor,
            'stages': all_stages,
        })
