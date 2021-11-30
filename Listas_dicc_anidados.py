def run():
    my_list = [1,"Hello", True, 4.5]
    my_dict = {"firstname":"Facundo", "lastname":"Perez"}

    super_list = [
        
        {"firstname": "Andres", "lastname":"Jimenez"},
        {"firstname": "Anderson", "lastname":"Pabon"},
        {"firstname": "Arley", "lastname":"Jilgar"},
        {"firstname": "Jeisson", "lastname":"Casas"}

    ]

    super_dict = {

        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[2.3,3.5,3.5]   }


    for key, value in super_dict.items():
        print(key,"-",value)

    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')

if __name__ == '__main__':
    run()