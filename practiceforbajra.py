
# # #--------Q.N.1-----------------
# # # string1 = "Sauravi Rajbhandari"

# # # string1 = string1.replace(" ","").lower()

# # # string= [a for a in string1]
# # # print(string)
# # # repeated =[]
# # # for i in range(0,len(string)):
# # #     if string[i] in repeated:
# # #         continue
# # #     count = 0

# # #     for j in range(0,len(string)):
# # #         if string[i]==string[j]:
# # #            repeated.append(string[i]) 
# # #            count+=1

# # #     print(f"{string[i]} is repeated {count} times")       

# # #----------------Q.N.2-------------------------------
# # a = "*"
# # for i in range(5):
# #     ok=""
# #     for j in range(0,i):
# #         ok+=" "
# #         # ok+=a
# #     for j in range(i,5):
# #         # ok+=" "
# #         ok+=a 
# #         ok+=" " 
# #     # for j in range(i,5):
# #     #     ok+=" "      
# #     print(ok)
# #     print("\n")    

# enter = input().lower()

# entered_list = [e  for e in enter]
# palindromes = []
# while len(entered_list) > 0:
    
#     for i in range(len(entered_list)):
#         straigt = []
#         remain_strait = []
#         straigt_str = ""
#         reverse_str = ""
#         reverse=[]
#         for j in range(0,i+1):
#             straigt.append(entered_list[j])
        
#         if len(straigt) == 1:
#             continue
#         remain_strait= straigt
#         for a in remain_strait:
#             straigt_str+=a
#         straigt.reverse()
#         reverse= straigt
#         # print("Rever",reverse)
        
#         for b in reverse:
#             reverse_str+=b    
#         # print("rrr",reverse_str)
#         # print("okok",straigt_str)


#         if straigt_str == reverse_str:
#             # print("yes")
#             palindromes.append(straigt_str)

#     entered_list.pop(0)

# print("palindromes" ,palindromes)

# dic = {}
# indexes_list = []

# if len(palindromes)>0:
#     for m in palindromes:
#         dic[len(m)] = m
#         indexes_list.append(len(m))

#     indexes_list.sort(reverse=True)

#     print(dic[indexes_list[0]])
# else:
#     print("NO SUCH PALINDROME EXISTS")


# a=[1,1,2,3,3,3,3,4,4,785]
# already = []
# largest = 0
# for i in a:
    
#     for j in range(len(a)):

#         if i < a[j]:
#             largest = a[j]


# largest = [i for i in a if i>[l for l in range(len(a))]]            
# print(largest)            



