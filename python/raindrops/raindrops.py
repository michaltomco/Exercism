def convert(number):
    drops = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    result = ''.join(sound for factor, sound in drops.items() if number % factor == 0)
    return result if result else str(number)
