
def picture(fail_try):
    filename = f'picture_{fail_try}.txt'
    try:
        with open(filename, 'r') as fh:
            for line in fh:
                print(line, end='')

    except OSError:
        print(f'Obrazek {filename} nelze precist.')
