import os
import random
# eg.1


def factoria(n):
    if n == 0:
        return 1
    else:
        return n * factoria(n - 1)


# eg.2
def draw_line(tick_length, tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)


def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')
    for i in range(1, num_inches + 1):
        draw_interval(major_length - 1)
        draw_line(major_length, str(i))

# eg.3


def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)

# eg.4


def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    print('{0:<7}'.format(total), path)

# eg.5


def good_fibonacci(n):
    if n <= 1:
        print(0)
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n - 1)
        print(a)
        return (a + b, a)
# eg.6


def power(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        total = partial * partial
        if n % 2 == 1:
            total *= x
        return total

# R-4.1


def find_max(data):
    if len(data) == 1:  # 只有一个元素
        return data[0]
    elif len(data) == 2:
        return data[0] if data[0] > data[1] else data[1]
    else:
        mid = len(data) // 2
        max_left = find_max(data[:mid])
        max_right = find_max(data[mid:])
        return max_left if max_left > max_right else max_right
# R-4.6


def harmonic(n):
    if n == 1:
        return 1
    else:
        return 1 / n + harmonic(n - 1)

# R-4.7


def string_to_integer(string):
    if len(string) == 1:
        return int(string[0])
    else:
        return int(string[0]) * 10 ** (len(string) - 1) + \
            string_to_integer(string[1:])

# C4.9
def find_min_and_max(data):
    if len(data) == 1:  # 只有一个元素
        return (data[0], data[0])
    elif len(data) == 2:
        max_num = data[0] if data[0] > data[1] else data[1]
        min_num = data[0] if data[0] < data[1] else data[1]
        return (max_num, min_num)
    else:
        mid = len(data) // 2
        max_num_left, min_num_left = find_min_and_max(data[:mid])
        max_num_right, min_num_right = find_min_and_max(data[mid:])
        max_ = max_num_left if max_num_left > max_num_right else max_num_right
        min_ = min_num_left if min_num_left < min_num_right else min_num_right
        return (max_, min_)

# C-4.10
def funC10(n, i=0):
    if 2**i >= n:
        return i
    else:
        return funC10(n, i+1)
# C-4.11
def funC11(data):
    if len(data) == 1:
        return True
    else:
        for j in data[1:]:
            if data[0] == j:
                return False
        return funC11(data[1:])

# C-4.12
def funC12(m, n):
    if m == 1:
        return n
    else:
        return n + funC12(m - 1, n)

# C-4.14
def hanoi_tower(n, a, b, c):
    """
    :param n: 碟子数
    :param a:  碟子摞
    :param b:  辅助摞
    :param c:  目标摞
    """
    def move(a, x, c):
        print("{}>>>_{}_>>>{}".format(a, x, c))
    if n == 1:
        move(a, n,c)
    else:
        hanoi_tower(n-1, a, c, b)
        move(a, n, c)
        hanoi_tower(n -1, b, a, c)
# C-4.15
def subset(data, k):
    if len(data) == 1:
        return [data]
    if k == 1:
        return [[i] for i in data]
    result = []
    for j in range(len(data)):
        if len(data[j+1:]) >= k-1:
            rest_data = subset(data[j+1:], k-1)
            lists = []
            for r in rest_data:
                lists.append(data[j:j+1] + r)
            result += lists
    return result
# C-4.16
def reverse_string(string, start, stop):
    if start > stop:
        return
    else:
        string[start], string[stop] = string[stop], string[start]
        reverse_string(string, start+1, stop-1)
    return string
# C-4.17
def is_huiwen(string, start, stop):
    if string[start] != string[stop]:
        return False
    elif start == stop or start == stop -1:
        return True
    else:
        return is_huiwen(string, start+1, stop-1)

# C-4.18
def C18(s, start, stop):
    if start == stop - 1:
        if s[start] in vowels:
            return 1
        elif s[start] in consonants:
            return -1
        else:
            return 0
    else:
        mid = (start + stop) // 2
        return C18(s, start, mid) + C18(s, mid, stop)

# C-4.19
def separate_odd_even(data):
    if len(data) == 1:
        return [data[0]]

    for i in range(len(data)):
        if data[i] % 2 == 0:
            return [data[i]] + separate_odd_even(data[i+1:])
        else:
            return separate_odd_even(data[i+1:]) + [data[i]]

# C-4.20
def funC20(data, k):
    if len(data) == 1:
        return [data[0]]

    for i in range(len(data)):
        if data[i] <= k:
            return [data[i]] + funC20(data[i+1:], k)
        else:
            return funC20(data[i+1:], k) + [data[i]]

# C-4.21
def funC21(data, k):
    def binary_search(data, target, start, end):
        if start > end:
            return False
        mid = (start + end) // 2
        if data[mid] == target:
            return data[mid]
        elif data[mid] > target:
            return binary_search(data, target, start, mid - 1)
        else:
            return binary_search(data, target, mid + 1, end)
    for j in range(len(data)-1):
        target = k - data[j]
        temp = binary_search(data[j+1:], target, 0, len(data[j+1:]))
        if temp:
            print('{}+{}={}'.format(data[j], temp, k))


if __name__ == "__main__":
    data =  [1,2,3,4,5,6,10,11]
    funC21(data, 11)
