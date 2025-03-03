from odoo import models, fields

class Preparation(models.Model):
    _name = 'jmm_gestion_restaurantes.preparation'
    _description = 'Preparation Method'

    name = fields.Char(string='Method Name', required=True)
    description = fields.Text(string='Description')
    temperature = fields.Float(string='Required Temperature (°C)')
    time = fields.Float(string='Average Time (mins)')
    equipment = fields.Char(string='Required Equipment')
    # Relacion para ver que platos se realizan con ese metodo de preparacion
    dish_ids = fields.One2many(
        'jmm_gestion_restaurantes.dish', 
        'preparation_method_id', 
        string='Dishes'
    )