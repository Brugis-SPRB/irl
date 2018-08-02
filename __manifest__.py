# -*- coding: utf-8 -*-
{
    'name': "irl",

    'summary': """
        irl""",

    'description': """
        irl
    """,

    'author': "Geode SPRL",
    'website': "http://www.opengeode.be",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'SPRB',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
        'geode_geoengine'
    ],

    'application': True,
    # always loaded
    'data': [
        'security/data.xml',
        'security/ir.model.access.csv',
        'views/view.xml',
        'views/menu.xml',
        'views/web.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
