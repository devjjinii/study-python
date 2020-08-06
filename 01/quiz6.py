'''
남자 : 키 * 키 * 22
여자 : 키 * 키 * 21

조건 1: 표준 체중은 별도의 함수 내에서 계산
        함수명 : std_weight
        전달값 : 키(height), 성별(gender)
조건 2: 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
'''

def std_weight(height, gender): # 키 m단위
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # 키 cm 단위
gender = "남자"
weight = round(std_weight(height / 100 , gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
