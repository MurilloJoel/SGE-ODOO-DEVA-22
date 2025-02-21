from odoo import models, fields

class Dish(models.Model):
    _name = 'jmm_gestion_restaurantes.dish'
    _description = 'Dish'

    name = fields.Char(string='Dish Name', required=True)
    description = fields.Text(string='Description')
    category_id = fields.Many2one(
        'jmm_gestion_restaurantes.category', 
        string='Category'
    )
    preparation_method_id = fields.Many2one(
        'jmm_gestion_restaurantes.preparation', 
        string='Preparation Method'
    )
    ingredient_ids = fields.Many2many(
        'jmm_gestion_restaurantes.ingredient',
        relation="jmm_gestion_ingredient_dish",
        string='Ingredients'
    )
    image = fields.Binary(string='Dish Image')
    active = fields.Boolean(string='Active', default=True)
    price = fields.Float(string='Price')
    calories = fields.Float(string='Calories')
    preparation_time = fields.Float(string='Preparation Time (mins)')