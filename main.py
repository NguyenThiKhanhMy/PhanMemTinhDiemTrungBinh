math_score = literature_score = english_score = average_score = 0

# Nhập điểm của học sinh
student_name = input("Nhập vào Họ và tên: ")
math_score = float(input("Nhập vào điểm môn Toán: "))
literature_score = float(input("Nhập vào điểm môn Văn: "))
english_score = float(input("Nhập vào điểm môn Anh: "))

# Tính điểm trung bình của học sinh
average_score = (math_score + literature_score + english_score) / 3

# In ra màn hình điểm trung bình của học sinh
print("Điểm trung bình của học sinh",student_name,"là:",average_score)
