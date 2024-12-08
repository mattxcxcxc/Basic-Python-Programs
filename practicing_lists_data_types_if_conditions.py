# a='string'
# aa=sorted(a)
# print(aa)
# str2=''.join(aa)
# print(str2)
# item=input('Enter product name:')
# price=(input('Enter product price:'))
# total_len=len(item)+len(price)
# dots='.'*(25-total_len)
# print(item+dots+price)
# pass1=input('Enter a password:')
# pass2=input('Retype password to confirm:')
# if pass1==pass2:
#     print('Password Completed')
# while pass1 !=pass2:
#     print('Password not the same enter again:')
#     pass1=input('Enter a password:')
#     pass2=input('Retype password to confirm:')
# print('Password Completed')
# card_num=input('Enter card number:')
# last_digits=card_num[15::]
# four='*'*4+' '
# display=four*3+last_digits
# print('Display Card Num',display)
# emailid=input('Enter user ID:')
# atrate=emailid.find('@')
# print(atrate)
# print('user id:',emailid[:atrate])
# print('domain name:',emailid[atrate+1:])
# s1=input('Enter a string:')
# rev=s1[::-1]
# if s1==rev:
#     print('Palindrome')
# else:
#     print('Not a Palindrome')
# s1=input('Enter a string:')
# rev=s1[::-1]
# print(s1+rev)
# dd_mm_yy=input('Enter the day,month,year')
# l=dd_mm_yy.split('/')
# print('Day',l[0])
# print('Month',l[1])
# print('Year',l[2])
# s1=input('Enter a word: ')
# s2=input('Enter second word: ')
# if len(s1)==len(s2):
#     print('Both are anagrams')
# else:
#     print('Not anagrams')
# lower_s1,lower_s2=s1.lower(),s2.lower()
# s1_sorted,s2_sorted=sorted(lower_s1),sorted(lower_s2)
# if s1_sorted==s2_sorted:
#     print('Both are anagrams')
#     print(s1_sorted,s2_sorted)
# else:
#     print('Not anagrams.')
# s1=input('Enter a word: ')
# s2=input('Enter second word: ')
# if len(s1)!=len(s2):
#     print('Not Anagram')
# else:
#     for x in s1:
#         if x not in s2:
#             print('Not anagram')
#             break;
#     else:
#         print('Anagram')
# arrange_case=input('Enter some letters to be arranged: ')
# low=""
# up=""
# for x in arrange_case:
#     if x.islower():
#         low+=x
#     else:
#         up+=x
# combined_str=low+up
# print(combined_str)
# s1=input('Enter a string/email user id:')
# punctuations='''!()-[]{};:"\",<>./?@#$%^&*_~'''
# s2=""
# for x in s1:
#     if x not in punctuations:
#         s2+=x
# print(s2)
# wrk_hrs=[]
# hourly_wages=int(input('Enter hourly wage:'))
# while True:
#     hour=input("Enter your work hours (type 'done' to finish):")
#     if hour.lower()=='done':
#         break
#     wrk_hrs.append(int(hour))
# total_wrk_hours=sum(wrk_hrs)
# total_salary=total_wrk_hours*hourly_wages
# print(total_salary)
# nums_for_list=input('Enter numbers to put in a list use space in between: ')
# delete_duplicates=list(set(int(x)for x in nums_for_list.split()))
# print(delete_duplicates)
# l1=[3,5,7,9,3,6,5,2,3,7,10]
# l2=[]
# for x in l1:
#     if x not in l2:
#         l2.append(x)
# l2.sort()
# print(l2)
# l1=[3,5,10,7,12]
# l2=""
# for x in l1:
#     l2+=str(x)
# l2_int=int(l2)
# print(l2_int)
# l1=['pizza','nuggets','hotdog','noodles','pasta','burger']
# l2=['pizza','hotdog','noodles','pasta','nuggets','pizza']
# result=[]
# min_sum=float('inf')
# for x in l1:
#     if x in l2:
#         index_find1=l1.index(x)
#         index_find2=l2.index(x)
#         index_sum=index_find1+index_find2
#         if index_sum < min_sum:
#             min_sum=index_sum
#             result=x
#         elif index_sum == min_sum:
#             result.append(x)
# print(result)
# l1=[10,15,6,9,12,8,4]
# l2=[14,6,19,4,7,10,11]
# l3=[]
# for x in l1:
#     if x in l2:
#         l3.append(x)
# print(l3)
# l1=['A','B','C','D','E','A','B','E','B','D','B','E']
# result=[]
# for x in l1:
#     if x not in result:
#         count=l1.count(x)
#         result.append(x)
#         result.append(count)
# print(result)
# user_input_=input('Enter a word, program will display it in morse code: ')

# letters=['A','B','C','D','E','F','G','H','I','J','L','M',
# 'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# morse_code=['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
# '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
# '..-', '...-', '.--', '-..-', '-.--', '--..']

# user_input_=user_input_.upper()
# morse_code_result=""

# for x in user_input_:
#     if x in letters:
#         postion_letter=letters.index(x)
#         morse_code_result+=morse_code[postion_letter]
#         morse_code_result+=" "
# print(morse_code_result)
# m1=[[1,2,3],[4,5,6]]
# m2=[[7,8,9,],[10,11,12]]
# result=[]
# for x in range(len(m1)):
#     row_result=[]
#     for j in range(len(m1[x])):
#         total_sum=m1[x][j]+m2[x][j]
#         row_result.append(total_sum)
#     result.append(row_result)
# print(result)

# m1=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# l2=[]
# for x in range(4):
#     s=[]
#     for j in range(3):
#         s.append(m1[j][x])
#     l2.append(s)
# print(l2)
# letter=input('Enter a letter:')#if first letter matches in food list display that item in food list.
# food=['pizza','nuggets','hotdog','noodles','pasta','burger']
# for item in food:
#     if item[0]==letter:
#         print(item)
# list1=[None]*10
# print(len(list1))
# l =['python ', 'is', 'a', 'userfriendly', 'programming', 'language']
# value_=l[0:6:2]
# print(value_)