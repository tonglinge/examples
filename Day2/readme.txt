本目录下的为第二天的作业,包括如下两个程序
所有程序运行在python 2.x版本下

1: day2_1_calc.py

计算器程序:
主要功能：为将一个复杂的表达式包括 + - * / （）计算出结果
设计思路：包括两个主要的函数
      (1)  get_simple_express(string, source)：
       功能：去括号,获取括号中的单一表达式
       实现：
            将传入的字符串去括号,通过循环每次找到最小单位的括号()中的表达式,将括号中的单一表达式 交给另一
      个函数 calc_string(string) 去处理，返回计算的结果。
          将原表达式中的括号中的内容替换为计算的结果值，再将新的字符串通过递归再次执行，一直这样下去直到去掉
      所有的括号，并最终的到结果值


      (2) calc_string(string)
      功能： 计算表达式的结果，包括 + - * /
      实现：
            按照 * / + - 的顺序来拆表达式
            通过截取字符串的方式获取对应的数字，并计算出结果
            将表达式替换为结果值，并一直循环直到算出结果
运用到的主要知识点：
       1、数据的转换及运算符操作
       2、涉及到字符串的处理，包括字符串的切片、组合
       3、if...else...条件判断, while循环等表达式的应用

       (3) format_str(string)
       功能：将字符串中的符号进行格式化



2：day2_2_shopping.py

模拟简单购物程序：
主要功能：
       (1) 打印商品列表，通过选择商品编号选择商品
       (2) 选择商品进行购物、扣款等模拟购物功能
       (3) 查看购物车
       (4) 账户充值
设计思路：
       首先定义2个全局的变量，分别保存用户的账户金额、购物车列表
       用户选择商品的编号，如果编号存在就将商品加入到购物车的变量中，并扣款
       扣款时先判断选择商品的价格是否小于用户的账户金额
运用到的主要知识点：
        1、列表、字典的操作
        2、打印时用到字符的center函数
