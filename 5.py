def triangle(number):
    if type(number) != int:
        raise ValueError('Please input integer only!')
    else:
        for i in range(1, number+1):
            pict_triangle = print('{:>12}'.format(i * ' *', '\n'))
            
    return pict_triangle