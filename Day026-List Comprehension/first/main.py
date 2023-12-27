with open("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day026-List Comprehension\\first\\file1.txt") as file1:
    file1_list = [f1.strip() for f1 in file1.readlines()]
    print(file1_list)


with open("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day026-List Comprehension\\first\\file2.txt") as file2:
    file2_list = [f2.strip() for f2 in file2.readlines()]
    print(file2_list)   


compared_list = [int(num) for num in file1_list if num in file2_list]    

print(compared_list)

    