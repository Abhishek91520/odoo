from odoo import api, fields, models


class IndustryType(models.Model):
    _name = "crm.industry.type"
    _description = "CRM Industry Type"
    _rec_name = 'industry_type'
    _order = "industry_type"

    industry_type = fields.Char('Industry Type', required=True, translate=True)
