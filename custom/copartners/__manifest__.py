{
    'name': "custom_copartners",
    'summary': "summary about corpartners"
    ,
    'description': """
    Description text
    """,
    'depends': ['base', 'crm'],
    # data files always loaded at installation
    'data': [
            'views/copartners_model_view.xml',
            'reports/report.xml',
            'reports/template.xml',
    ],

}
