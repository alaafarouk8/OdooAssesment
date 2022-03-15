from odoo import fields, models, api
from odoo.exceptions import ValidationError, UserError


class CrmInherit(models.Model):
    _inherit = "res.company"

    copartners_id = fields.One2many('copartners.model', 'company_id')
