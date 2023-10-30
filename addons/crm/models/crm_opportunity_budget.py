from odoo import models, fields


class CrmOppBudget(models.Model):
    _inherit = 'crm.lead'
    budget_amt = fields.Float('Budget')
    budget_confirmed = fields.Boolean('Budget Confirmed')
    roi_known = fields.Float('ROI Known')
    roi_analysis = fields.Boolean('ROI Analysis Completed')
    amortization = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24')],
        string='Amortization with in Month'
    )
    budget_level = fields.Text('Budget level & Source')
    initial_meeting = fields.Boolean('Initial Meeting')
    initial_meeting_date = fields.Date(string='Initial Meeting Date')
    quote_received = fields.Boolean('Quote Received')
    technical_evaluation = fields.Text('Technical Evaluation Completed')
    offer_discussed = fields.Boolean('Offer Discussed in Details')
    next_step = fields.Boolean('Next Step')
    demo_done = fields.Boolean('Demo Done')

class CrmPolitics(models.Model):
    _inherit = 'crm.lead'
    contact_selection = fields.Selection([
        ('contact1', 'Contact 1'),
        ('contact2', 'Contact 2'),
        ('contact3', 'Contact 3')],
    )
    decision_criteria = fields.Text('Decision Criteria')
    research_completed = fields.Boolean('Research Completed')
    competition = fields.Selection([
        ('competition1', 'Competition 1'),
        ('competition2', 'Competition 2'),
        ('competition3', 'Competition 3')],
        string='Competition',
        widget="many2many_tags"
    )


    int_ext_comp = fields.Text('Internal & External Competition')

    int_support = fields.Text('Internal Support')
    decision_process = fields.Text('Decision Process')
    quotation_received = fields.Boolean('Quotation Received')
    tech_discussion = fields.Text('Technical Discussion Evaluator')
    offer_discount = fields.Boolean('Offer Discount in Detail')


class DemoDetails(models.Model):
    _inherit = 'crm.lead'
    sequence = fields.Integer("Sequence")
    customer = fields.Char("Customer")
    material = fields.Text("Material")
    hsncode = fields.Char("HSN Code")
    media_used = fields.Char("Media Used")
    nda = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')],
        string="NDA")
    demo = fields.Char("Demo")
    description = fields.Text("Description")
    decision_criteria = fields.Text("Decision Criteria")
    pic = fields.Image("Pictures")
    notes = fields.Text("Notes")
    part_img_before = fields.Image("Part Image Before Process")
    part_img_after = fields.Image("Part Image After Process")
    total_hours = fields.Integer("Total Hours Required")
    machine_use = fields.Char("Machine Use")

    



