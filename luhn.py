def checksum(card):
    digits = list(map(int, card))
    odd_sum = sum(digits[-1::-2])
    even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    return (odd_sum + even_sum) % 10

def verify(card):
    return (checksum(card) == 0)

# def generate(card):
#     csum = checksum(card + '0')
#     return (10 - csum) % 10

# def append(card):
#     return card + str(generate(card))


    