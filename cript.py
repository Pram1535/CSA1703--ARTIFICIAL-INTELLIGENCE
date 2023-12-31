from itertools import permutations
def solve_cryptarithmetic():
    letters = 'BASELGM'
    values = range(10)
    for perm in permutations(values, len(letters)):
        letter_to_value = {letters[i]: perm[i] for i in range(len(letters))}
        if 0 in [letter_to_value['S'], letter_to_value['M']]:
            continue
        send = letter_to_value['B'] * 1000 + letter_to_value['A'] * 100 + letter_to_value['S'] * 10 + letter_to_value['E']
        more = letter_to_value['B'] * 1000 + letter_to_value['A'] * 100 + letter_to_value['L'] * 10 + letter_to_value['L']
        money = letter_to_value['G'] * 10000 + letter_to_value['A'] * 1000 + letter_to_value['M'] * 100 + letter_to_value['E'] * 10 + letter_to_value['S']
        if send + more == money:
            return letter_to_value
    return None
solution = solve_cryptarithmetic()
if solution:
    for letter, value in solution.items():
        print(f'{letter}: {value}')
else:
    print('No solution found.')
