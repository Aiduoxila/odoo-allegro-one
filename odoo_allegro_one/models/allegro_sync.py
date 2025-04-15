from odoo import models, fields

class AllegroSyncTask(models.Model):
    _name = 'allegro.sync.task'
    _description = 'Allegro Synchronization Task'

    name = fields.Char(string='Task Name', required=True)
    last_run = fields.Datetime(string='Last Execution Time')
    status = fields.Selection([
        ('pending', 'Pending'),
        ('running', 'Running'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    ], string='Status', default='pending')