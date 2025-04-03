from odoo import http
import json

class WebhookHandler(http.Controller):
    @http.route('/allegro/webhook', auth='public', methods=['POST'], csrf=False)
    def handle_webhook(self, **kwargs):
        event_data = json.loads(http.request.httprequest.data)
        event_type = event_data.get('event_type')

        if event_type == 'new_order':
            order_details = event_data.get('data')
            self.create_order(order_details)
        elif event_type == 'product_update':
            product_data = event_data.get('data')
            self.update_inventory(product_data)

        return "Webhook event processed successfully."

    def create_order(self, order_details):
        http.request.env['sale.order'].create({
            'partner_id': order_details['customer_id'],
            'order_line': [(0, 0, {
                'product_id': order_details['product_id'],
                'product_uom_qty': order_details['quantity']
            })]
        })

    def update_inventory(self, product_data):
        product = http.request.env['product.product'].search([('allegro_id', '=', product_data['id'])])
        if product:
            product.write({'qty_available': product_data['stock']})
