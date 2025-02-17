from odoo import models, fields

class Preparation(models.Model):
    _name = 'JMM_kitchen.preparation'
    _description = 'Preparation Method'

    name = fields.Char(string='Method Name', required=True)
    description = fields.Text(string='Description')
    temperature = fields.Float(string='Required Temperature (°C)')
    time = fields.Float(string='Average Time (mins)')
    equipment = fields.Char(string='Required Equipment')
    dish_ids = fields.One2many(
        'JMM_kitchen.dish', 
        'preparation_method_id', 
        string='Dishes'
    )