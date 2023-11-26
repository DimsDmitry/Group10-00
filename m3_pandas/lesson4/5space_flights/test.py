time = 'Fri Aug 07, 2020 05:12 UTC'


def set_datum(datum):
    try:
        datum = datum.split()[4].split(':')[0]
        morning = '04 05 06 07 08 09 10 11 12 13'.split()
        if datum in morning:
            return 0
        return 1
    except:
        return 0


print(set_datum(time))
