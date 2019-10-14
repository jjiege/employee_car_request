{
    'name': "Employee Car Request",

    'summary': """
        Resquest a car and get approval""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Terabithia Explorer",
    'website': "https://www.linkedin.com/in/tera4xp",
    'category': 'Human Resources',
    'version': '0.1',

    'depends': ['base', 'hr', 'fleet'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}