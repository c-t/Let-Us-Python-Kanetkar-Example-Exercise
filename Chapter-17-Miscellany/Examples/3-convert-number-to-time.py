tm = 26031
hr = tm >> 11
min = (tm & 0b11111100000) >> 5
sec = (tm & 0b11111) * 2
print(str(hr) + ':' + str(min) + ':' + str(sec))
