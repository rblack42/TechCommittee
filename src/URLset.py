URLset = {
    'courses':  {
        'server': 'http://www3.austincc.edu',
        'path': '/it/cms/www/catalog/coursedetails_fox.php',
        'query': 'year=%(year)s&deptcode=%(dept_code)s',
        'keys': [
            {
                'year': '2016',
                'dept_code': 'COSC',
            },
            {
                'year': '2016',
                'dept_code': 'COIS',
            }
        ]
    },
    'staff': {
        'server': 'http://www6.austincc.edu',
        'path': '/directory/search.php',
        'query': 'name=&campus=&dept=%(dept)s&position=&email=',
        'keys': [
            {
                'dept': 'COSC',
            },
            {
                'dept': 'COIS',
            }
        ]
    },
    'classes': {
        'server': 'http://www6.austincc.edu',
        'path': '/schedule/index.php',
        'query': 'op=browser&opclass=ViewSched&term=%(term)s&disciplineid=%(discipline_id)s&yr=%(year)s&ct=CC',
        'keys': [
            {
                'term': '216S000',
                'discipline_id': 'PCCOS',
                'year': '2016',
            },
            {
                'term': '216S000',
                'discipline_id': 'PCCIS',
                'year': '2016',
            }
        ]

    }
}

