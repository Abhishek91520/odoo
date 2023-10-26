# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models



class BusinessType(models.Model):
    """ Model for case stages. This models the main stages of a document
        management flow. Main CRM objects (leads, opportunities, project
        issues, ...) will now use only stages, instead of state and stages.
        Stages are for example used to display the kanban view of records.
    """
    _name = "crm.business.type"
    _description = "CRM Business Type"
    _rec_name = 'business_type'
    _order = "business_type"


    business_type = fields.Char('Business', required=True, translate=True)

