{
    'name': 'Allegro Integration',
    'version': '16.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': 'Integration with Allegro.CZ marketplace',
    'description': """
        This module provides integration with Allegro.CZ marketplace:
        * Inventory Management
        * Order Synchronization
        * Pricing Updates
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'sale_management', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/allegro_settings.xml',
        'views/allegro_sync.xml',
        'data/api_config.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
