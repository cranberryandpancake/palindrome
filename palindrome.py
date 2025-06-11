def reverse_number(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    return n == reverse_number(n)

def main():
    try:
        user_input = input("0 이상의 정수를 입력하세요.")
        number = int(user_input)
        
        if number < 0:
            print("음수는 입력할 수 없습니다. 0 이상의 정수를 입력해 주세요.")
            return
        
        reversed_num = reverse_number(number)
        print(f"뒤집은 숫자: {reversed_num}")
        
        if is_palindrome(number):
            print("이 숫자는 대칭입니다!")
        else:
            print("이 숫자는 대칭이 아닙니다.")
            
    except ValueError:
        print("정수만 입력해 주세요.")

if __name__ == "__main__":
    main()
