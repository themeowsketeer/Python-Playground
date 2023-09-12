import math

number = [float(x) for x in input("nhap cac so: ").split(" ")]
number.sort()

rangeArray = number[len(number)-1] - number[0]

Q1_pos = (len(number) + 1) / 4
Q1 = number[math.floor(Q1_pos)-1] + ( (number[math.floor(Q1_pos)] - number[math.floor(Q1_pos)-1]) * (Q1_pos - math.floor(Q1_pos)))

Q2_pos = (len(number) + 1) / 2
Q2 = number[math.floor(Q2_pos)-1] + ( (number[math.floor(Q2_pos)] - number[math.floor(Q2_pos)-1]) * (Q2_pos - math.floor(Q2_pos)))

Q3_pos = 3*(len(number) + 1) / 4
Q3 = number[math.floor(Q3_pos)-1] + ( (number[math.floor(Q3_pos)] - number[math.floor(Q3_pos)-1]) * (Q3_pos - math.floor(Q3_pos)))

Outlier = [x for x in number if x > (Q3 + (1.5 * (Q3 - Q1))) or x < (Q1 - (1.5 * (Q3 - Q1)))]
mean = 0.0
for x in number:
    mean += x
mean = mean / len(number)

sum_1 = 0.0
sum_2 = 0.0
for x in number:
    sum_1 += pow((x - (mean)),2)
sampleVariance = sum_1 / (len(number) - 1)
sampleDeviation = math.sqrt(sampleVariance)

for x in number:
    sum_2 += pow((x - (mean / len(number))),2)
populationVariance = sum_1 / (len(number))
populationDeviation = math.sqrt(populationVariance)

print(f'List Length: {len(number)} \nData Range: {rangeArray} \nMin value: {number[0]} \nLower Quartile: {math.ceil(Q1)} \nMedian: {math.ceil(Q2)} ' +
      f'\nUpper Quartile: {math.ceil(Q3)} \nMax Value: {number[len(number)-1]} \nOutlier List: {Outlier} \nSorted List: {number}' +
      f'\nMean: {mean} \nSample Variance: {round(sampleVariance, 4)} \nSample Deviation: {round(sampleDeviation, 4)}')