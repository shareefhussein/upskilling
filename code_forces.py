# #  twins 

# def solve2(n, coins):

#     total = 0
#     for coin in coins:
#         total += int(coin)

#     coins.sort(reverse=True)

#     yourTotal = 0
#     yourCoinsCount = 0
#     halfTotal = total/2
#     for coin in coins:

#         if yourTotal > halfTotal:
#             break

#         yourTotal += int(coin)
#         yourCoinsCount += 1

#     return yourCoinsCount


# n = int(input())
# coins = map(int,input().split(" "))
# print(solve2(n, coins))


# n = int(input())
# count = 0
# for i in range(n):
# 	word = input().split(' ')
# 	c = list(map(int,word))
# 	if sum(c)>=2:
# 		count+=1
# print(count)	

# vowel = ['a','e','i','o','u']
# new_string = ''
# string = input()
# string= string.lower()
# for i in range(len(string)):
# 	if string[i] not in vowel:
# 		new_string+='.'
# 		new_string+=string[i]
# print(new_string)

n1 = 0
n2 = 1
count = 0
n = int(input('enter the nth term '))
for i in range(n):
    while count<n:
        print(n1,end=',')
        nth = n1+n2
        n1 = n2
        n2 = nth
        count+=1