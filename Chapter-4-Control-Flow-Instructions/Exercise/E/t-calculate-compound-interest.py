# calculate compound interest
# Formula
# amount = principal * ( 1 + rate/number of times compounded) ^ (years * compound_times)
def compoundInterest(principal, rate, years, compound_times):
    final_amount = principal * pow((1 + (rate / compound_times)), years * compound_times)
    return final_amount

for i in range(1,10):
    p, r, n, q = input('Enter principal, rate, years, compound_times: ').split()
    amount = compoundInterest(int(p), float(r), int (n), int(q))
    print('Final amount = ', amount)