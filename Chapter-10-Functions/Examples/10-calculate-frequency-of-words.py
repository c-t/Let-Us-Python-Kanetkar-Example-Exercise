def frequency(s):
    freq = {}
    for word in s.split():
        freq[word] = freq.get(word, 0) + 1
    return freq

sentence  = 'It is true for all that that that that that that that refers to is not the same that that that that refers to'
d = frequency(sentence)
words = sorted(d)

for w in words:
    print('%s:%d' % (w, d[w]))