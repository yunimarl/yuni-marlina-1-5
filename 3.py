def sequence(number):
    seq_num = []
    if (number < 0) | (type(number) != int):
        raise ValueError('Parameter harus bilangan bulat positif!')
        
    seq_num.append(number)
    
    if number % 2 == 0:
        n = number/2
        seq_num.append(int(n))
        
        if (n % 2 == 0) & (n != 1):
            while n > 1:
                if n % 2 == 0:
                    n = n/2
                    seq_num.append(int(n))
                elif n != 1:
                    n = (3 * n) + 1
                    seq_num.append(int(n))

    elif number != 1:
        n = (3 * number) + 1
        seq_num.append(int(n))
        if (n % 2 == 0) & (n != 1):
            while n > 1:
                if n % 2 == 0:
                    n = n/2
                    seq_num.append(int(n))
                elif n != 1:
                    n = (3 * n) + 1
                    seq_num.append(int(n))
          
    return print(seq_num, '\n', 'count: ', len(seq_num))