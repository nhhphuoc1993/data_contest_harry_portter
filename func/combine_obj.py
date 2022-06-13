import copy

def combine_2_series(serie_1, serie_2):
    output = copy.deepcopy(serie_1)
    for index, value in output.items():
        output[index] = '{}({})'.format(value.strip(), serie_2[index])
    return output