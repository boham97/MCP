def read_file(file_name, offset, size):
    content = ""
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            content = ''.join(lines[offset:offset + size])
    except FileNotFoundError:
        print("파일이 존재하지 않습니다.")

    except OSError as e:
        print(f"파일 입출력 오류: {e}")

    except Exception as e:
        print(f"예기치 않은 오류 발생: {e}")

    return content

if __name__ == "__main__":
    res = read_file('fibonacci.rb', 0, 10)
    print(res)