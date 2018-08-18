set1 = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six',7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten', 11:'ELeven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}

set2 = {20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety'}

set3 = {100:'One hundred', 200:'Two hundred', 300:'Three hundred', 400:'Four hundred', 500:'Five hundred', 600:'Six hundred', 700:'Seven hundred', 800:'Eight hundred', 900:'Nine hundred', 1000:'One Thousand'}

count = 0

def compute_two_digit(num):
    if (1 <= num <= 19):
        return set1[num]

    if 20<=num<=99:
        if num in set2:
            return set2[num]

        else:
            ones = num % 10
            tens_digit = num - ones
            return (set2[tens_digit] + set1[ones])

def naming (num):
    if num<=99:
        return compute_two_digit(num)

    else:
        if num in set3:
            return set3[num]

        else:
            tens = num % 100
            hundreds = num - tens
            return (set3[hundreds] + "and" + compute_two_digit(tens))

for x in range (1, 1001):
    count += len(naming(x))

print (count)

# print naming(210)
