from odoo import models, fields

class AllegroSettings(models.Model):
    _name = 'allegro.settings'
    _description = 'Allegro Integration Settings'

    sync_mode = fields.Selection([
        ('manual', 'Manual'),
        ('periodic', 'Periodic'),
        ('real_time', 'Real-time')
    ], string='Synchronization Mode', default='manual', required=True)
    
    sync_frequency = fields.Integer(
        string='Sync Frequency (minutes)',
        default=60,
        help='How often the synchronization should run'
    )
    
    webhook_url = fields.Char(
        string='Webhook URL',
        help='URL for receiving real-time updates from Allegro'
    )