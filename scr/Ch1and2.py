import random
import string
import re
import sys
import copy


# R-1.1
def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False


# R-1,2
def is_even(k):
    if k & 1 == 0:
        return True
    else:
        return False


# R-1.3
def maxmin(data):
    if data:
        m = n = data[0]
        for i in data:
            if i > m:
                m = i
            if i < n:
                n = i
        return (m, n)
    else:
        print("序列为空！")


# R-1.4
def square_sum(n):
    result = 0
    for i in range(n + 1):
        result += i ** 2
    return result


# R-1.5
def square_sum2(n):
    return sum([i ** 2 for i in range(n + 1)])


# R-1.6
def odd_square_sum(n):
    return sum([i ** 2 for i in range(n + 1) if i & 1 == 1])


# R-1.12
def my_choice(data):
    return data[random.randrange(len(data))]


# C-1.14
def funC14(data):
    for i in data:
        for j in data:
            if i != j and i * j % 2 != 0:
                return True
    return False


# C-1.15
def funC15(data):
    n = len(data)
    m = len(set(data))
    if n == m:
        return True
    else:
        return False


# C-1.20
def shuff1e1(data):
    result = []
    while data:
        p = random.randint(0, len(data) - 1)
        result.append(data[p])
        data.pop(p)
    return result


def shuffle2(data):
    for i in range(len(data) - 1, 0, -1):
        p = random.randint(0, i)
        data[i], data[p] = data[p], data[i]
    return data


def shuffle3(data):
    result = data[:]
    for i in range(1, len(data)):
        j = random.randint(0, i)
        result[i] = result[j]
        result[j] = data[i]
    return result


# C-1.22
def funC22(a, b):
    if len(a) != len(b):
        print("两个数组长度不相等！")
        return
    else:
        return [a[i] * b[i] for i in range(len(a))]


# C-1.27
def funC27(n):
    k = 1
    temp = []
    while k * k < n:
        if n % k == 0:
            yield k
            temp.append(n // k)
        k += 1
    if k * k == n:
        yield k
    for i in reversed(temp):
        yield i


# C-1.28
def norm(v, p):
    return sum([i ** p for i in v]) ** (1 / p)


# C-1.29
def Perm_k(arrs, k):
    # 若输入 [1,2,3]，则先取出1这个元素，将剩余的 [2,3]中取出另一个元素得到 [[1,2],[1,3]]
    # 同理，取出2或者3时，得到的分别是 [[2,1],[2,3]]和 [[3,1],[3,2]]
    if len(arrs) == 1:
        return [arrs]
    if k == 1:
        return list(map(lambda s: [s], arrs))  # 当 k 为 1 时，每(单)个元素都可以被选取
    result = []  # 最终的结果（即全排列的各种情况）
    for i in range(len(arrs)):
        rest_arrs = arrs[:i] + arrs[i + 1:]  # 取出arrs中的第 i个元素后剩余的元素
        rest_lists = Perm_k(rest_arrs, k - 1)  # 剩余的元素选取 k-1元素
        lists = []
        for term in rest_lists:
            lists.append(arrs[i:i + 1] + term)  # 将取出的第 i个元素加到剩余全排列的前面
        result += lists
    return result


# C-1.30
def funC30(n):
    if n <= 0:
        print("请输入一个正整数！")
        return
    i = 0
    while n >= 2:
        n = n // 2
        i += 1
    return i


# C-1.31
def funC31(price, pay):
    money = [100, 50, 20, 10, 5, 1, 0.5, 0.1]
    cash = {}
    # 由于python存在舍入误差（rounding errors），所以弄成整数以后再算
    temp = (pay - price) * 10
    if price < pay:
        for i in money:
            quotient = temp // (i * 10)
            remainder = round(temp % (i * 10))
            cash[i] = quotient
            if remainder == 0:
                break
            else:
                temp = remainder
        for key, value in cash.items():
            if value != 0:
                print("找零 {} 张 {} 元人民币".format(int(value), key))
    elif price == pay:
        print("刚好支付！")
    else:
        print("请支付足够金额！")


# P-1.35
def funP35(n):
    t = 0
    f = 0
    for p in range(100):
        birthdays = [random.choice([j for j in range(365)]) for i in range(n)]
        if len(birthdays) != len(set(birthdays)):
            t += 1
        else:
            f += 1
    print(t / 100)


# P-1.36
def funP36():
    words = "is a word like it is the the is word banana apple word is apple"
    count = {}
    words_list = words.split(" ")
    for word in words_list:
        count[word] = 1 + count.get(word, 0)
    print(count)


if __name__ == "__main__":
    a = [1, 2, 3, [2, 1, 1]]
    c = copy.deepcopy(a)
    b = list(a)
    b[3][0] = 0
    print(a)
    print(b)
    print(c)
