# -*- coding: utf-8 -*-
{
    'name': "recruit",

    'summary': """
        module de recruitement""",

    'description': """
        Ce module vous permet de gerer votre processus de recruitement
    """,

    'author': "GadioService",
    'website': "https://www.gadio.com",

    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'security/recruit_security.xml',
        'views/recruitment_views.xml',
        'views/recruiteur_view.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
