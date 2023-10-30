def solution(x):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    switch = str.maketrans(alphabet, alphabet[::-1])
    return x.translate(switch)
