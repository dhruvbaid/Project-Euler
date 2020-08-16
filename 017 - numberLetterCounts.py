"""
Number Letter Counts - If all the numbers from 1 to 1000 (one thousand)
inclusive were written out in words, how many letters would be used?
"""
import math

def numCounts():
        ones = ['','one', 'two','three', 'four', 'five', 'six', 'seven', 'eight',
                'nine']
        tens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                'sixteen', 'seventeen', 'eighteen', 'nineteen']
        rest = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
                'eighty', 'ninety']
        count = 0;
        count0 = 0;
        for i in range(1, 100):
                if(i < 10):
                        count0 += len(ones[i])
                elif(10 <= i < 20):
                        count0 += len(tens[i - 10]);
                else:
                        count0 += len(rest[math.floor(i/10) - 2] + ones[i%10])
        count += count0;
        for j in range(1, 10):
                count += len(ones[j] + 'hundred')
                count += 99 * len(ones[j] + 'hundredand');
                count += count0;
        count += len('onethousand')
        return count;
