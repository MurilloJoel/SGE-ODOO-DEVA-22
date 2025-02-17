from odoo import models, fields

class Dish(models.Model):
    _name = 'JMM_kitchen.dish'
    _description = 'Dish'

    name = fields.Char(string='Dish Name', required=True)
    description = fields.Text(string='Description')
    category_id = fields.Many2one(
        'JMM_kitchen.category', 
        string='Category'
    )
    preparation_method_id = fields.Many2one(
        'JMM_kitchen.preparation', 
        string='Preparation Method'
    )
    ingredient_ids = fields.Many2many(
        'JMM_kitchen.ingredient',
        string='Ingredients'
    )
    image = fields.Binary(string='Dish Image')
    active = fields.Boolean(string='Active', default=True)
    price = fields.Float(string='Price')
    calories = fields.Float(string='Calories')
    preparation_time = fields.Float(string='Preparation Time (mins)')