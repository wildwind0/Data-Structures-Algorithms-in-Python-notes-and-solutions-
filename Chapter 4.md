# 递归

## 例题 

> 递归是一种技术，这种技术通过一个函数在执行过程中一次或者多次调用其本身，或者通过一种数据结构在其表示中依赖于相同类型的结构更小的实例

注：函数调用时局部变量和执行位置信息压栈，调用结束后恢复。



例1：阶乘函数的递归实现

~~~python
def factoria(n):
    if n==0:
        return 1
   	else:
        return n * factoria(n-1)
~~~

例2：英式标尺 （二路递归）

~~~python
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
    for i in range(1, num_inches+1):
        draw_interval(major_length - 1)
        draw_line(major_length, str(i))

if __name__ == "__main__":
    draw_ruler(1,5)
~~~

例3：二分查找（尾递归）

~~~python
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
~~~

例4：磁盘使用情况 （多重递归）

~~~python
def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    print('{0:<7}'.format(total), path)
~~~

例5：斐波拉契数列的递归实现

~~~python
def good_fibonacci(n):
    if n <= 1:
        print(0)
        return (0, n)
    else:
        (a, b) = good_fibonacci(n - 1)
        print(b)
        return (b, a+b)
~~~

例6：递归求幂

~~~python
def power(x, n):0
    if n == 0:
        return 1
    else:
        partial = power(x, n//2)
        total = partial * partial
        if n % 2 == 1:
            total *= x
        return total
~~~



> 修改递归深度的方法：
>
> ~~~python
> import sys
> old = sys.getrecursionlimit()
> sys.setrecursionlimit(100000)
> ~~~

## 递归算法的形式

- *对于基本情况的测试* 。首先测试一组基本情况（至少应该有一个）。每个可能的递归调用链最终都会达到一种基本情况，即终止条件，并且每个基本情况的处理都不应该使用递归。
- *递归*。 如果不是一种基本情况，则执行一个或者多个递归调用。这个递归步骤可能包括一个测试，该测试决定执行哪几种可能的递归调用。这些递归调用会向一种基本情况靠近。

## 递归问题时间、空间复杂度估算

- 时间复杂度

  Master公式：

  这个方法针对形如：T(n) = aT(n/b) + f(n^d^)的递归方程。这种递归方程是分治法的时间复杂性所满足的递归关系，即一个规模为n的问题被分成规模。<u>**均为**</u>n/b的a个子问题，递归地求解这a个子问题，然后通过对这a个子问题的解的综合，得到原问题的解。这种方法是对于分治问题最好的解法，我们先给出如下的公式：

  ①当d<logb a时，时间复杂度为O(n^(logb a))
  ②当d=logb a时，时间复杂度为O((n^d)*logn)
  ③当d>logb a时，时间复杂度为O(n^d)

  公式记忆：我们实际上是比较n^logb a和f(n)的阶，如果他们不等，那么T(n)取他们中的较大者，如果他们的阶相等，那么我们就将他们的任意一个乘以logn就可以了。

  空间复杂度

- 空间复杂度：**不是计算实际占用的空间，而是计算整个算法的辅助空间单元的个数，与问题的规模没有关系**(简单理解就是算法执行时创建的变量（包括临时变量）个数)

  ①忽略常数，用O(1)表示 
  ②递归算法的空间复杂度=递归深度N*每次递归所要的辅助空间 
  ③对于单线程来说，递归有运行时堆栈，求的是递归最深的那一次压栈所耗费的空间的个数，因为递归最深的那一次所耗费的空间足以容纳它所有递归过程。递归是要返回上一层的，所以它所需要的空间不是一直累加起来的 

  [参考][https://blog.csdn.net/w_y_x_y/article/details/78733667]

## 习题

**R-4.1** 对于一个含有n个元素的序列S， 描述一个递归算法查找其最大值。所给算法的时间复杂度和空间复杂度各是多少？

~~~python
def find_max(data):
    if len(data) == 1: 
        return data[0]
    elif len(data) == 2:
        return data[0] if data[0] > data[1] else data[1]
    else:
        mid = len(data) // 2
        max_left = find_max(data[:mid])
        max_right = find_max(data[mid:])
        return max_left if max_left > max_right else max_right
~~~

根据master公式，该算法的时间复杂度为 O(n)

**R-4.6** 递归求第n个调和数 $H_{n}=\sum_{i=1}^{n}1/i​$

~~~python
def harmonic(n):
    if n == 1:
        return 1
    else:
        return 1/n + harmonic(n-1)
~~~

**R-4.7** 使用递归的方法，将一串数字转换成对应的整数。

~~~python
def string_to_integer(string):
    if len(string) == 1:
        return int(string[0])
    else:
        return int(string[0]) * 10 ** (len(string) - 1) + string_to_integer(string[1:])
    
if __name__ == "__main__":
    string = ['1', '3', '4', '3']
    print(string_to_integer(string))
~~~

**R-4.8** 

此方法将规模为n的计算，均分为 规模为2的子问题，一共n/2个，根据master公式，时间复杂度为O(n)



**C-4.9** 递归的方法查找一个序列中的最大值和最小值

~~~python
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
~~~

**C-4.10** 在只使用加法和整除的情况下，使用递归计算以2为底的n的对数的整数部分。

~~~python
def funR10(n, i=0):
    if 2**i >= n:
        return i
    else:
        return funR10(n, i+1)
~~~

**C-4.11** 使用递归函数求解元素的唯一性，在不使用排序的最坏的情况下运行时间最多是O(n^2^)

~~~python
def funC11(data):
    if len(data) == 1:
        return True
    else:
        for j in data[1:]:
            if data[0] == j:
                return False
        return funC11(data[1:])
~~~

**C-4.12** 在只使用加减法的情况下，递归求两个正整数m和n的乘积。

~~~python
def funC12(m, n):
    if m == 1:
        return n
    else:
        return n + funC12(m - 1, n)
~~~

**C-4.14** 汉罗塔问题

~~~python
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
        
if __name__ == "__main__":
    hanoi_tower(4, 'a', 'b', 'c')
~~~

![图1](.\fig\C-4.14_2.png)

![图2](.\fig\C-4.14_1.gif)

**C-4.15** 递归实现，输出一个含有n个元素的集合的所有子集（没有任何重复的子集）

~~~python
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
if __name__ == "__main__":
    data = [1,2,3,4]
    result = []
    for k in range(1, len(data)+1):
        lists = subset(data, k)
        result += lists
    print(result)
~~~

**C-4.16** 递归实现，逆置字符串。

~~~python
def reverse_string(string, start, stop):
    if start > stop:
        return
    else:
        string[start], string[stop] = string[stop], string[start]
        reverse_string(string, start+1, stop-1)
    return string

if __name__ == "__main__":
    string = list('snap&stop')
    print(''.join(reverse_string(string, 0 , len(string)-1)))
~~~

**C-4.17** 递归实现，确定一个字符串s是否是它的一个回文字符串。

~~~python
def is_huiwen(string, start, stop):
    if string[start] != string[stop]:
        return False
    elif start == stop or start == stop -1:
        return True
    else:
        return is_huiwen(string, start+1, stop-1)
if __name__ == "__main__":
    string = list('abccba')
    print(is_huiwen(string,0,len(string)-1))
~~~

**C-4.18** 递归实现，确定字符串s中是否元音字母比辅音字母多。

~~~python
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


if __name__ == "__main__":
    letters = {chr(i) for i in range(65, 91)} | {chr(i) for i in range(97, 123)}
    vowels = {'a', 'e', 'i', 'o', 'u'} | {'A', 'E', 'I', 'O', 'U'}
    consonants = letters - vowels
    s = list('FAIOJIOWAHFOgioqoinnaoanfoe&87*12JEIQEOQNFN')
    result = C17(s, 0, len(s))
    if  result > 0:
        print("元音字母多")
    elif result == 0:
        print("一样多")
    else:
        print("辅音字母多")
~~~

**C-4.19** 递归实现，重新排列一个整数值序列，使得所有欧数值出现在所有奇数值前面。

~~~python
def separate_odd_even(data):
    if len(data) == 1:
        return [data[0]]

    for i in range(len(data)):
        if data[i] % 2 == 0:
            return [data[i]] + separate_odd_even(data[i+1:])
        else:
            return separate_odd_even(data[i+1:]) + [data[i]]

if __name__ == "__main__":
    data =  [1,2,3,10,4,3,4,5,6,7]
    print(separate_odd_even(data))
~~~

**C-4.20** 递归实现，对于未排序的整数序列S和整数k，使得所有小于等于k的元素在所有大于k的元素之前。并求时间复杂度。

~~~python
def funC20(data, k):
    if len(data) == 1:
        return [data[0]]

    for i in range(len(data)):
        if data[i] <= k:
            return [data[i]] + funC20(data[i+1:], k)
        else:
            return funC20(data[i+1:], k) + [data[i]]
if __name__ == "__main__":
    data =  [1,2,3,10,4,3,4,5,6,7,-4,-1,-3]
    print(funC20(data, 3))
~~~

时间复杂度 O(n^2^)

**C-4.21** 给出一个含有n各元素的序列S，其中元素升序排列，递归找到S中总和为k得两个整数（假设一对整数存在）。算法复杂度是多少？

~~~python
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
~~~

时间复杂度 O(nlogn)