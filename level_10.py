# LEVEL 10
# http://www.pythonchallenge.com/pc/return/bull.html
# a = [1, 11, 21, 1211, 111221,
# len(a[30]) = ?

prev = '1'


# a = [1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211,
def next_term(prev_term):
    pos = 0
    prev_dig = None
    digit_seq_l = 0
    result = ''
    while pos < len(prev_term):
        digit = prev_term[pos]
        if digit == prev_dig:
            digit_seq_l += 1
        else:
            if prev_dig is not None:
                result += str(digit_seq_l) + prev_dig
            digit_seq_l = 1
        prev_dig = digit
        pos += 1
    result += str(digit_seq_l) + digit
    return result


test_data = [1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, 31131211131221, 13211311123113112211,
             11131221133112132113212221, 3113112221232112111312211312113211,
             1321132132111213122112311311222113111221131221,
             11131221131211131231121113112221121321132132211331222113112211,
             311311222113111231131112132112311321322112111312211312111322212311322113212221]

term = next_term('1')
for i in range(1, len(test_data)):
    if term != str(test_data[i]):
        print("error: {} != {}".format(term, test_data[i]))
    term = next_term(term)
print('ok')

term = '1'
for i in range(31):
    print(i, len(term))
    term = next_term(term)
