def data_processing(data: str) -> [int, str]:
    if data.isnumeric():
        return int(data)
    else:
        return data


def get_data(line: str) -> tuple:
    operand_1, operation, operand_2 = map(data_processing, line.split())
    return operand_1, operation, operand_2


def calc(operands: tuple) -> [int, float, bool]:
    if operands[1] == '+':
        result = operands[0] + operands[2]
    elif operands[1] == '//':
        result = operands[0] // operands[2]
    elif operands[1] == '/':
        result = operands[0] / operands[2]
    elif operands[1] == '%':
        result = operands[0] % operands[2]
    elif operands[1] == '-':
        result = operands[0] - operands[2]
    elif operands[1] == '*':
        result = operands[0] * operands[2]
    elif operands[1] == '**':
        result = operands[0] ** operands[2]
    else:
        result = False
    return result


if __name__ == '__main__':
    errors = {}
    with open('calc.txt', 'r', encoding='utf-8') as f:
        for ind,line in enumerate(f):
            try:
                calc(get_data(line))
            except ValueError as exc:
                errors[ind+1] = (exc,exc.args)
    for key, val in errors.items():
        got_args = val[1][0].split()[8].split(')')[0]
        print(f'Строка {key}: недостаточно аргументов для вычислений. Ожидается {3}, передано {got_args}')
    print(f'Всего ошибок: {len(errors)}')
