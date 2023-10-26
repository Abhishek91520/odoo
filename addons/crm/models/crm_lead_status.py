# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

AVAILABLE_PRIORITIES = [
    ('0', 'Negative Quality'),
    ('1', 'Active'),
    ('2', 'Working'),
    ('3', 'Lost'),
]


class LeadStatus(models.Model):
    """ Model for case stages. This models the main stages of a document
        management flow. Main CRM objects (leads, opportunities, project
        issues, ...) will now use only stages, instead of state and stages.
        Stages are for example used to display the kanban view of records.
    """
    _name = "crm.lead.status"
    _description = "CRM Lead Status"
    _rec_name = 'name'
    _order = "sequence, name, id"

    @api.model
    def default_get(self, fields):
        """ As we have lots of default_team_id in context used to filter out
        leads and opportunities, we pop this key from default of stage creation.
        Otherwise stage will be created for a given team only which is not the
        standard behavior of stages. """
        if 'default_team_id' in self.env.context:
            ctx = dict(self.env.context)
            ctx.pop('default_team_id')
            self = self.with_context(ctx)
        return super(LeadStatus, self).default_get(fields)

    name = fields.Char('Stage Name', required=True, translate=True)
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    is_default = fields.Boolean('Is Default?')




    def write(self,values):
        override_write = super(LeadStatus,self).write(values)
        if(  values['is_default']):
            self.env.cr.execute('''UPDATE crm_lead_status SET is_default=False''')
        return override_write
