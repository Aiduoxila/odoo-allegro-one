# Odoo Allegro Integration Demo Guide

This guide will help you test the Odoo-Allegro integration using demo data.

## Demo Features

- Pre-configured Allegro API settings
- Sample products with Allegro mappings
- Demo orders for testing synchronization
- Test mode enabled for safe experimentation

## Quick Start

1. Install the module following instructions in README.md
2. The demo data will be automatically loaded
3. Navigate to Settings > Allegro Integration
   - You'll see a pre-configured "Demo Allegro Shop"
   - Test mode is enabled by default

## Sample Data

### Products
- Demo Laptop (DEMO-LAP-001)
  - Price: €999.99
  - Allegro ID: demo_allegro_123

- Demo Smartphone (DEMO-PHN-001)
  - Price: €499.99
  - Allegro ID: demo_allegro_456

### Orders
- Sample order DEMO-ORD-001
  - Customer: John Demo
  - Status: Confirmed

## Testing Synchronization

1. **Manual Sync Test**
   - Go to Allegro Integration > Dashboard
   - Click "Sync Now"
   - Check the sync status of demo products

2. **Periodic Sync Test**
   - Default interval: 60 minutes
   - You can modify this in settings

3. **Webhook Test**
   - Default URL: http://your-domain.com/allegro/webhook
   - Use this URL to simulate Allegro notifications

## Safety Notes

- All demo data is marked with "DEMO" prefix
- Test mode prevents actual API calls to Allegro
- Demo data can be safely removed through module uninstallation