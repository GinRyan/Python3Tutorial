file_path=r'D:\Tutorial4MachineLearning\i_digits.txt'
import os

absfilePath = os.path.abspath(file_path)
print(absfilePath)

with open(file_path) as file_object2:
    for line in file_object2:
        print(line)

