import random
import string

def generate_random_id(length=10):
    """
    生成指定长度的随机字符串。字符将从数字、大写和小写字母中选择。
    """
    characters = string.ascii_letters + string.digits  # Combines lowercase, uppercase letters and digits
    return ''.join(random.choice(characters) for _ in range(length))


# 生成字符串样例 'JsPdGgFh6l'
random_id = generate_random_id()
print(random_id)


def generate_number(start_num=0):
    """
    生成器
    """
    num = start_num
    while True:
        yield num
        num += 1


number_generator = generate_number()


first_number = next(number_generator)
print(first_number)
first_number = next(number_generator)
print(first_number)
