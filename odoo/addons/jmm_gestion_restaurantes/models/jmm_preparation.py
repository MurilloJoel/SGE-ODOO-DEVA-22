from odoo import models, fields, api, exceptions

class Preparation(models.Model):
    _name = 'jmm_gestion_restaurantes.preparation'
    _description = 'Preparation Method'
    
    name = fields.Char(string='Method Name', required=True)
    description = fields.Text(string='Description')
    temperature = fields.Float(string='Required Temperature (°C)')
    time = fields.Float(string='Average Time (mins)')
    equipment = fields.Char(string='Required Equipment', required=True)
    dish_ids = fields.One2many(
        'jmm_gestion_restaurantes.dish', 
        'preparation_method_id', 
        string='Dishes'
    )

    _sql_constraints = [
        ('unique_method_name', 'UNIQUE(name)', '¡Nombre del método debe ser único!'),
        ('positive_temperature', 'CHECK(temperature >= 0)', '¡Temperatura ≥ 0!'),
        ('positive_time', 'CHECK(time > 0)', '¡Tiempo > 0!')
    ]

    @api.constrains('equipment')
    def _check_equipment(self):
        if not self.equipment.strip():
            raise exceptions.ValidationError('¡Debe especificar el equipo requerido!')