from odoo.tests.common import TransactionCase

class TestAllegroSettings(TransactionCase):
    def setUp(self):
        super(TestAllegroSettings, self).setUp()
        self.settings = self.env['allegro.settings'].create({
            'sync_mode': 'manual',
            'sync_frequency': 30,
            'webhook_url': 'https://test.example.com/webhook'
        })

    def test_settings_creation(self):
        """Test if settings are created with correct values"""
        self.assertEqual(self.settings.sync_mode, 'manual')
        self.assertEqual(self.settings.sync_frequency, 30)
        self.assertEqual(self.settings.webhook_url, 'https://test.example.com/webhook')

    def test_sync_mode_validation(self):
        """Test sync mode selection values"""
        self.settings.write({'sync_mode': 'periodic'})
        self.assertEqual(self.settings.sync_mode, 'periodic')

        self.settings.write({'sync_mode': 'real_time'})
        self.assertEqual(self.settings.sync_mode, 'real_time')