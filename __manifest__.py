# -*- coding: utf-8 -*-
{
    'name': "module-list-updater",

    'summary': """
          Module list updater intended to be used in Odoo CLI.
    """,

    'description': """
        It calls module list update function, so it can be used to update module list using Odoo command line interface.
    """,

    'author': "ygneo",
    'website': "http://www.coopdevs.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/update-module-list.xml',
    ],
}
