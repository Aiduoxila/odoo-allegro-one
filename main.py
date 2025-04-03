from odoo import http

class AllegroIntegration(http.Controller):
    @http.route('/allegro/test_connection', auth='user')
    def test_connection(self):
        return "API Connection Successful!"
