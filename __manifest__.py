{
    'name': 'Odoo Allegro One',
    'version': '1.0',
    'summary': 'Integrates Allegro.CZ API with Odoo',
    'author': 'Your Name or Company',
    'category': 'Tools',
    'depends': ['base', 'product', 'sale'],
    'data': [
        'views/allegro_settings.xml',
        'views/allegro_sync.xml',
        'data/api_config.xml',
    ],
    'application': True,
}
