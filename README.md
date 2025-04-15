# Odoo Allegro Integration

This module provides seamless integration between Odoo and Allegro.CZ marketplace, streamlining e-commerce operations through automated inventory management, order synchronization, and pricing updates.

## Features

- Real-time inventory synchronization
- Automated order processing
- Dynamic pricing management
- Webhook support for instant updates
- Configurable synchronization modes (Manual, Periodic, Real-time)
- Comprehensive API integration

## Requirements

- Odoo 16.0
- Python 3.8 or higher
- Valid Allegro.CZ API credentials

## Installation

1. Clone this repository to your Odoo addons directory:
   ```bash
   git clone https://github.com/your-repository/odoo-allegro-one.git
   ```

2. Update your Odoo addons list:
   - Navigate to Apps menu
   - Click on "Update Apps List"
   - Search for "Allegro Integration"
   - Click Install

## Configuration

1. Navigate to Settings > Allegro Integration
2. Configure your Allegro API credentials
3. Set up synchronization preferences:
   - Choose sync mode (Manual/Periodic/Real-time)
   - Configure sync frequency for periodic updates
   - Set up webhook URL for real-time updates

## Module Structure

```
odoo_allegro_one/
├── __init__.py               # Module initialization
├── __manifest__.py           # Module metadata
├── models/                   # Business logic
│   ├── __init__.py           # Models initialization
│   ├── allegro_api.py        # API integration logic
│   ├── allegro_settings.py   # Configuration models
│   └── allegro_sync.py       # Synchronization logic
├── controllers/              # Request handlers
│   ├── __init__.py           # Controllers initialization
│   └── main.py               # Webhook and routes
├── data/                     # Configuration data
│   └── api_config.xml        # Initial settings
├── views/                    # UI elements
│   ├── allegro_settings.xml  # Settings forms
│   └── allegro_sync.xml      # Sync task views
├── security/                 # Access control
│   └── ir.model.access.csv   # Access rights
└── tests/                    # Unit tests
    ├── __init__.py
    ├── test_allegro_settings.py
    └── test_allegro_sync.py
```

## Usage

1. **Manual Synchronization**
   - Navigate to Allegro Integration > Dashboard
   - Click "Sync Now" to manually trigger synchronization

2. **Periodic Synchronization**
   - Configure sync frequency in settings
   - System will automatically sync based on the set interval

3. **Real-time Updates**
   - Configure webhook URL in settings
   - Allegro will send instant notifications for any changes

## Support

For issues and feature requests, please use the GitHub issue tracker.

## License

This project is licensed under LGPL-3 - see the LICENSE file for details.

