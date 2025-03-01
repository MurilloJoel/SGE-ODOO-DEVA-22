from odoo import models, fields, api, exceptions

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
        string='Ingredients',
        required=True
    )
    image = fields.Image(
        string='Dish Image',
        max_width=1024,
        max_height=1024,
        help='Seleccionar Imagen'
    )
    active = fields.Boolean(string='Active', default=True)
    price = fields.Float(string='Price', digits='Product Price')
    calories = fields.Float(string='Calories')
    preparation_time = fields.Float(string='Preparation Time (mins)')

    _sql_constraints = [
        ('unique_dish_name', 'UNIQUE(name)', '¡El nombre del plato debe ser único!'),
        ('positive_price', 'CHECK(price >= 0)', '¡El precio debe ser ≥ 0!'),
        ('positive_calories', 'CHECK(calories >= 0)', '¡Calorías deben ser ≥ 0!'),
        ('positive_prep_time', 'CHECK(preparation_time > 0)', '¡Tiempo preparación > 0!')
    ]

    @api.constrains('ingredient_ids')
    def _check_ingredients(self):
        for record in self:
            if len(record.ingredient_ids) < 1:
                raise exceptions.ValidationError('¡Cada plato debe tener al menos 1 ingrediente!')