from odoo import models, fields
from odoo import api, exceptions, _

class CopartnersModel(models.Model):
    _name = "copartners.model"
    _rec_name = 'name'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    name = fields.Char(required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], tracking=True ,required=True )
    country= fields.Char(required=True, tracking=True )
    joining_date=fields.Date( required=True ,tracking=True )
    tag_ids = fields.Many2many('custom.model.tags', required=True ,tracking=True )
    customer_id = fields.Many2many('res.partner', required=True ,tracking=True )
    company_id = fields.Many2one('res.company', required=True ,tracking=True )
    notes=fields.Char( required=True ,tracking=True )
    comments=fields.Char( required=True ,tracking=True )


class CustomModelTags(models.Model):
    _name = 'custom.model.tags'
    _rec_name = 'tag_name'
    tag_name= fields.Char( required=True ,tracking=True )
    color = fields.Integer( required=True ,tracking=True )