y = 'y'
while y == 'y':
    input_data = input("Enter list of numbers, using comma: ")
    splited_input_data = input_data.split(',')
    int_input_data = map(int, splited_input_data)
    list_data = list(int_input_data)
    tuple_data = tuple(list_data)
    print('List: ', list_data)
    print('Tuple: ', tuple_data)
    print(f'First: {list_data[0]}; last: {list_data[-1]}')
    y = input('restart?(y/n): ')
