from datetime import datetime, timedelta
from odoo import api, fields, models, _

class CRMLead(models.Model):
    _inherit = 'crm.lead'

    def check_lost_leads(self):
        # Get the 'Lost in days' value from configuration
        lost_in_days = self.env['ir.config_parameter'].sudo().get_param('crm.lost_in_days')

        # Calculate the date threshold
        today = fields.Datetime.now()
        date_threshold = today - timedelta(days=int(float(lost_in_days)))
        # Find the 'Lost' stage

        str_query = '''UPDATE crm_lead SET active=False where date_last_stage_update <='{}' '''
        self.env.cr.execute(str_query.format(date_threshold))


        # Move the leads to the 'Lost' stage and set the lost reason

class CRMConfiguration(models.TransientModel):
    _inherit = 'res.config.settings'

    lost_in_days = fields.Float(
        string='Lost in days',
        config_parameter='crm.lost_in_days'
    )
