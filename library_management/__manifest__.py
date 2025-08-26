{
    'name': 'Library Management',
    'author': 'Ahmed Rasmy',
    'category': 'Uncategorized',
    'depends': ['base','mail'],
    'version': '0.1',
    'data':[
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/library_book_view.xml',
        'views/library_author_view.xml',
        'views/library_rental_view.xml',
    ],
    'application': True,
    'license' : 'LGPL-3',

}