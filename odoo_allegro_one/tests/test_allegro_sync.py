from odoo.tests.common import TransactionCase

class TestAllegroSync(TransactionCase):
    def setUp(self):
        super(TestAllegroSync, self).setUp()
        self.sync_task = self.env['allegro.sync.task'].create({
            'name': 'Test Sync Task'
        })

    def test_sync_task_creation(self):
        """Test if sync task is created with correct default values"""
        self.assertEqual(self.sync_task.name, 'Test Sync Task')
        self.assertEqual(self.sync_task.status, 'pending')
        self.assertFalse(self.sync_task.last_run)

    def test_sync_task_status_transition(self):
        """Test sync task status transitions"""
        self.sync_task.write({'status': 'running'})
        self.assertEqual(self.sync_task.status, 'running')

        self.sync_task.write({'status': 'completed'})
        self.assertEqual(self.sync_task.status, 'completed')