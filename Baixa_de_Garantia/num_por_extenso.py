import sys

def number_to_portuguese_words(number):
    units = {
        0: 'zero',
        1: 'um',
        2: 'dois',
        3: 'tres',
        4: 'quatro',
        5: 'cinco',
        6: 'seis',
        7: 'sete',
        8: 'oito',
        9: 'nove'
    }

    teens = {
        10: 'dez',
        11: 'onze',
        12: 'doze',
        13: 'treze',
        14: 'quatorze',
        15: 'quinze',
        16: 'dezesseis',
        17: 'dezessete',
        18: 'dezoito',
        19: 'dezenove'
    }

    tens = {
        20: 'vinte',
        30: 'trinta',
        40: 'quarenta',
        50: 'cinquenta',
        60: 'sessenta',
        70: 'setenta',
        80: 'oitenta',
        90: 'noventa'
    }

    hundreds = {
        100: 'cem',
        200: 'duzentos',
        300: 'trezentos',
        400: 'quatrocentos',
        500: 'quinhentos',
        600: 'seiscentos',
        700: 'setecentos',
        800: 'oitocentos',
        900: 'novecentos'
    }

    def convert_hundreds(n):
        if n == 0:
            return ''
        elif n < 10:
            return units[n]
        elif n < 20:
            return teens[n]
        elif n < 100:
            tens_part = n // 10 * 10
            units_part = n % 10
            if units_part == 0:
                return tens[tens_part]
            else:
                return tens[tens_part] + ' e ' + units[units_part]
        else:
            if n == 100:
                return 'cem'
            else:
                hundreds_part = n // 100 * 100
                remainder = n % 100
                if remainder == 0:
                    return hundreds[hundreds_part]
                else:
                    if hundreds_part == 100:
                        hundreds_word = 'cento'
                    else:
                        hundreds_word = hundreds[hundreds_part]
                    return hundreds_word + ' e ' + convert_hundreds(remainder)

    def convert_number_to_words(n):
        if n == 0:
            return 'zero'
        elif n < 1000:
            return convert_hundreds(n)
        elif n < 1000000:
            thousands_part = n // 1000
            remainder = n % 1000
            if thousands_part == 1:
                thousands_word = 'mil'
            else:
                thousands_word = convert_hundreds(thousands_part) + ' mil'
            if remainder == 0:
                return thousands_word
            else:
                if remainder < 100:
                    conjunction = ' e '
                else:
                    conjunction = ' '
                return thousands_word + conjunction + convert_hundreds(remainder)
        else:
            return 'Número muito grande'

    # Split number into integer and fractional parts
    integer_part = int(number)
    fractional_part = round((number - integer_part) * 100)

    # Convert integer part
    if integer_part == 0:
        reais_part = ''
    else:
        reais_word = convert_number_to_words(integer_part)
        if integer_part == 1:
            reais_unit = 'real'
        else:
            reais_unit = 'reais'
        reais_part = reais_word + ' ' + reais_unit

    # Convert fractional part
    if fractional_part == 0:
        centavos_part = ''
    else:
        centavos_word = convert_number_to_words(fractional_part)
        if fractional_part == 1:
            centavos_unit = 'centavo'
        else:
            centavos_unit = 'centavos'
        centavos_part = centavos_word + ' ' + centavos_unit

    # Combine parts
    if reais_part and centavos_part:
        final_result = reais_part + ' e ' + centavos_part
    elif reais_part:
        final_result = reais_part
    elif centavos_part:
        final_result = centavos_part
    else:
        final_result = 'zero reais'

    # Convert to uppercase
    final_result = final_result.upper()

    return final_result

cod_titulo = sys.argv[1]
number_str = sys.argv[2]
number = float(number_str)
texto = number_to_portuguese_words(number)
print(texto)
file_name = cod_titulo + '_valor.txt'
with open(file_name, 'w') as file:
    file.write(texto)