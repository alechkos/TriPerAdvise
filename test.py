import firebase as fb

data_cities = {'Cities': ['Jeruslem', 'Haifa', 'Ashdod', 'Tel_aviv']}

fb.db.push(data_cities)