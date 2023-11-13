def solution(x):
    x = list(x)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    opposite = alphabet[::-1]
    cipher = {}
    for i in range(len(alphabet)):
        cipher[alphabet[i]] = opposite[i] 
    for j in range(len(x)):
        if x[j] in cipher.keys():
            x[j] = cipher[x[j]]
        
    print(''.join(x))
