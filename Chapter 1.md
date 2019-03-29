- **R-1.1** 实现函数 is_multiple(n, m), n和m为整数，如果n是m的倍数则返回True，否则返回False.

  ~~~python
  def is_multiple(n, m):
          if n % m == 0:
              return True
          else:
              return  False
  ~~~

- **R-1.2** 实现函数 is_even(k), 判断整数k是否为偶数，不能使用乘法，除法或者取余数操作.

  思路：使用位运算

  ~~~python
  def is_even(k):
      if k & 1 == 0:
          return True
      else:
          return False  
  ~~~

- **R-1.3** 实现函数 minmax(data), 找出序列data中的最大数和最小数，并以长度为2的元组返回。不能使用内置函数max和min。

  ```python
  def maxmin(data):
      if data:
          m = n = data[0]
          for i in data:
              if i > m:
                  m = i
              if i < n:
                  n = i
          return (m,n)
      else:
          print("序列为空！")
  ```

- **R-1.4** 编写函数，用来接受正整数n，返回1~n的平方和.

  ~~~python
  def square_sum(n):
      result = 0
      for i in range(n+1):
          result += i**2
      return result
  ~~~

- **R-1.5**  使用解析语法和sum函数实现R-1.4

  ~~~python
  def square_sum2(n):
  	return sum([i**2 for i in range(n+1)])
  ~~~

- **R-1.6** 编写函数，实现接受正整数n，返回1~n中所有奇数平方和.

  ~~~python
  def odd_square_sum(n):
      return sum([i**2 for i in range(n+1) if i&1==1])
  ~~~

- **R-1.7** 同上

- **R-1.8** 长度为n的字符串s， 当索引值为 -n &le; k &le; 0 时，所指元素为s[k]，那么求一个正整数索引值 j&geqslant; 0, 使得s[j]指向的也是相同的元素、

  j = n-k

- **R-1.9** 生成50,60,70,80的排列。

  ~~~python
  a = list(range(50,90,10))
  ~~~

- **R-1.10** 生成8,6,4,2,0,-2,-4,-6,-8的排列。

  ~~~python
  a = list(range(8,-10,-2))
  ~~~

- **R-1.11** 使用列表解析生成列表[1,2,4,8,16,32,64,128,256].

  ~~~python
  a = [2**i for i in range(10)]
  ~~~

- **R-1.12** 使用randrange函数，实现自己的choice函数.

  ~~~python
  def my_choice(data):
      return data[random.randrange(len(data))]
  ~~~

- **C-1.13** 逆置n个整数的列表

  ~~~python
  a = [1,12,31,4,13,4]
      b=[]
      for i in range(len(a)-1,-1,-1):
          print(i)
          b.append(a[i])
      a.reverse()
      print(b)
      print(a)
  ~~~

- **C-1.14** 编写函数，判断一个整数序列中是否存在一对乘积是奇数的互不相同的数。

  ~~~python
  def fun14(data):
      for i in data:
          for j in data:
              if i != j and i*j % 2 != 0:
                  return True
      return False
  ~~~

- **C-1.15** 编写函数，判断一个数字序列是否所有数字都互不相同。

  ~~~python
  def fun15(data):
      n = len(data)
      m = len(set(data))
      if n==m:
          return True
      else:
          return False
  ~~~

- **C-1.16** 如下scale函数，循环体内执行命令data[j] *= factor。我们已经说过这个数字类型是不可变的，操作符 *= 在这种背景下使用时创建了一个新实例（而不是现有实例的变化）。那么scale函数是如何改变调用者发送的实际参数呢？

  ~~~python
      def scale(data, factor):
          for j in range(len(data)):
              data[j] *= factor
      grade = [1,2,3]
      scale(grade, 2)
      print(grade)
      
      OUT：[2,4,6]
  ~~~

  [参考:python中list作函数形参，如何防止被实参修改](https://blog.csdn.net/qq_17753903/article/details/82886625)

  在python中数据有两种类型，mutable（可变） 和 immutable （不可变）st ,dict是mutable的；int , string , float ,tuple是inmutable 的。在函数参数的传递过程中：对于inmutable object ，函数参数传递是值对于mutable object，函数参数传递是指针。因此当我们把grade传入scale函数时，实际上把它的指针传给了data变量，所以grade的值会随着data的值变化。**如果传递给函数的是可变序列，并且在函数内部使用下标或可变序列自身的方法增加、删除元素或修改元素时，修改后的结果是可以反映到函数之外的，实参也得到相应的修改。**但如果，scale函数内写成data = data * factor， 这时grade并不会被改变。

- **C-1.17** 

  如果上题中的scale函数如下，能正常工作吗？

  ~~~python
      def scale(data, factor):
          for val in data:
              val *= factor
  ~~~

  不能。理由见上题。

- **C-1.18** 使用列表解析产生[0,2,6,12,20,30,42,56,72,90]

  ~~~python
  [i*(i-1) for i in range(1,11)]
  ~~~

- **C-1.19** 在不输入26个英文字母的情况下产生列表['a','b',...,'z']

  ~~~python
  [i*(i-1) for i in range(97,123)]
  ~~~

- **C-1-20** 只使用randint()函数实现shuffle()函数。

  解法1：Fisher-Yates Shuffle: 从原始数据中随机抽取一个新的数字到新的数组中。O(n^2^)

  ~~~python
  def shuffe1(data):
      result = []
      while data:
          p = random.randint(0,len(data)-1)
          result.append(data[p])
          data.pop(p)
      return result
  ~~~

  解法2：Knuth-Durstenfeld Shuffle：原地打乱顺序算法，每次从未处理的数字中取一个放到尾部。 O(n)

  ```python
  def shuffle2(data):
      for i in range(len(data)-1,0,-1):
          p = random.randint(0,i)
          data[i], data[p] = data[p], data[i]
      return data
  ```

  解法3：Inside-Out：解法2改变了原始数据，这种方法不会改变原始数据。

  ~~~python
  def shuffle3(data):
      result = data[:]
      for i in range(1,len(data)):
          j = random.randint(0,i)
          result[i] = result[j]
          result[j] = data[i]
      return result
  ~~~

- **C-1.21** 反复从标准输入读取一行直到抛出EOFerror异常，然后以相反的顺序输出这些行。

  ~~~python
      input_line = []
      while True:
          try:
              input_line.append(input())
          except EOFError:
              input_line.reverse()
              print(input_line)
              break  
  ~~~

  注意：windows下输入ctrl+z触发EOFerror异常

- **C-1.22** 求长度都为n的两个数组的点积

  ~~~python
  def dot(a, b):
      if len(a)!=len(b):
          print("两个数组长度不相等！")
          return
      else:
          return [a[i]*b[i] for i in range(len(a))]
  ~~~

- **C-1.23** 列表索引越界异常捕捉。

  ~~~python
  a = [1,2,3]
      for i in range(len(a)+1):
          try:
              print(a[i])
          except IndexError:
              print("Don't try buffer overflow attacks in Python")
  ~~~

- **C-1.24** 编写函数，求所给字符串中元音字母的个数。

  ~~~python
  vowel = ['a', 'e', 'i', 'o', 'u']
      line = "haiafjaneawdiuhawoehoiasjdoihbjkfanowij"
      num = 0
      for i in line:
          if i in vowel:
             num += 1
      print(num)
  ~~~

- **C-1.25** 删除句中标点。

  参考：[Python文本处理——中文标点符号处理](https://www.cnblogs.com/arkenstone/p/6092255.html)

  ~~~python
  punctuation = string.punctuation
  sentence = "how are you? ,. I'm fine!"
  result = re.sub("[%s]+" % punctuation, "", sentence)
  print(result)
  ~~~

- **C-1.26** 在控制台输入3个整数，并确定他们是否可以在一个正确的算法公式（给定顺序）下成立。

  ~~~python
  	a,b,c = input("请输入三个整数：")
      a,b,c = int(a), int(b), int(c)
      if a + b == c:
          print("{}+{}={}".format(a,b,c))
      if a - b == c:
          print("{}-{}={}".format(a,b,c))
      if a / b == c:
          print("{}/{}={}".format(a,b,c))
      if a * b == c:
          print("{}*{}={}".format(a,b,c))
  ~~~

- **C-1.27** 使用生成器求整数因子。

  ~~~python
  def funC27(n):
      k = 1
      temp = []
      while k * k < n:
          if n % k == 0:
              yield k
              temp.append(n//k)
          k += 1
      if k * k == n:
          yield k
      for i in reversed(temp):
          yield i
  ~~~

- **C-1.28** 编写函数，求向量的p范数

  ~~~python
  def norm(v ,p):
      return sum([i**p for i in v])**(1/p)
  ~~~

- **P-1.29** 排列问题

  [参考](https://blog.csdn.net/Deeven123/article/details/82970560)

  ~~~python
  def Perm_k(arrs, k):
      # 若输入 [1,2,3]，则先取出1这个元素，将剩余的 [2,3]中取出另一个元素得到 [[1,2],[1,3]]
      # 同理，取出2或者3时，得到的分别是 [[2,1],[2,3]]和 [[3,1],[3,2]]
      if len(arrs)==1:
          return [arrs]
      if k==1:
          return list(map(lambda s:[s], arrs))  #  当 k 为 1 时，每(单)个元素都可以被选取
      result = []  # 最终的结果（即全排列的各种情况）
      for i in range(len(arrs)):
          rest_arrs = arrs[:i]+arrs[i+1:]  # 取出arrs中的第 i个元素后剩余的元素
          rest_lists = Perm_k(rest_arrs, k-1)     # 剩余的元素选取 k-1元素
          lists = []
          for term in rest_lists:
              lists.append(arrs[i:i+1]+term)  # 将取出的第 i个元素加到剩余全排列的前面
          result += lists
      return result
  
  result = []
      data = ['c', 'a', 't', 'd', 'o', 'g']
      for i in range(1, len(data)+1):
          temp = Perm_k(data, i)
          result.append([''.join(item) for item in temp])
      print([j for i in result for j in i])
  ~~~

  

- **P-1.30** 编写程序，输入一个大于2的正整数，求将该数反复被2整除直到商小于2为止的次数。

  ```python
  def funC30(n):
      if n <= 0:
          print("请输入一个正整数！")
          return
      i = 0
      while n >= 2:
          n = n // 2
          i += 1
      return i
  ```

- **P-1.31** 编写找零钱的程序。

  [舍入误差](https://stackoverflow.com/questions/14763722/python-modulo-on-floats)

  ~~~python
  def funC31(price, pay):
      money = [100, 50, 20, 10, 5, 1, 0.5, 0.1]
      cash = {}
      # 由于python存在舍入误差（rounding errors），所以弄成整数以后再算
      temp = (pay - price) * 10
      if price < pay:
          for i in money:
              quotient = temp // (i*10)
              remainder = round(temp % (i*10))
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
  ~~~

- ***P-1.32** 计算器

  ~~~python
  while True:
      a = int(input())
      symbol = input()
      b = int(input())
      if symbol=="+":
          c = a + b
      if symbol=="-":
          c = a - b
      if symbol=="*":
          c = a * b
      if symbol=="÷":
          c = a / b
      equal = input()
      if equal=="=":
          print(c)
          continue
  ~~~

- **P1-1.35** 生日悖论

  ~~~python
  def funP35(n):
      t = 0
      f = 0
      for p in range(100):
          birthdays = [random.choice([j for j in range(365)]) for i in range(n)]
          if len(birthdays) != len(set(birthdays)):
              t += 1
          else:
              f += 1
      print(t/100)
  ~~~

- **P-1.36** 词频统计

  ~~~python
  def funP36():
      words = "is a word like it is the the is word banana apple word is apple"
      count = {}
      words_list = words.split(" ")
      for word in words_list:
          count[word] = 1 + count.get(word, 0)
      print(count)
  ~~~

  

