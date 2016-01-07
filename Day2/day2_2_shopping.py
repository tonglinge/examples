# -*- coding:utf-8 -*-
"""
__auther:super
"""

import re

# 保存用户金额变量
USER_ACCOUNT = 0
# 保存用户购物车商品
USER_SHOPPING_CART = []


# 欢迎信息
def print_welcome_menu():
    menu_list = "=====================================================\n" \
                "=                                                   =\n" \
                "=              WELCOME TO SHOPPING MARKET           =\n" \
                "=                                                   =\n" \
                "=====================================================\n"
    return menu_list


def print_choose_menu():
    choose_menu = "1. 进入购物商城\n" \
                  "2. 查看账户余额\n" \
                  "3. 查看购物车\n" \
                  "4. 给账户充值\n" \
                  "5. 退出系统"
    return choose_menu


# 商品信息
def goods_list():
    goodslist = (
        {'no': '001', 'name': '联想笔记本电脑', 'price': 5000},
        {'no': '002', 'name': '手机Iphone 6S', 'price': 3000},
        {'no': '003', 'name': '耐克篮球鞋', 'price': 700},
        {'no': '004', 'name': 'Python源码分析', 'price': 80},
        {'no': '005', 'name': '三星固态硬盘', 'price': 1000},
    )
    return goodslist


# 获取汉字个数
def get_chinese_num(uchar):
    i = 0
    for utext in uchar:
        if u'\u4e00' <= utext <= u'\u9fa5':
            i += 1
    return i


# 打印商品信息
def print_goods_list(lists):
    _goodlist = lists
    # print('|  %5s   |    %-15s   |   %6s   |' % ('商品编号', '商品名称', '商品价格(RMB)'))
    print('|' + '商品编号'.center(16) + '|' + '商品名称'.center(23) + '|' + '商品价格(RMB)'.center(22) + '|')
    print('%s' % '-' * 53)
    for goods in _goodlist:
        chinese_num = get_chinese_num(goods['name'].decode('utf-8'))
        len_name = len(goods['name'].decode('utf-8'))
        space_str = (19 - len_name - chinese_num) * " "
        print('|%-12s|%s|%18s|' % (goods['no'], goods['name'] + space_str, str(goods['price'])))


# 检测输入商品编号是否存在
def check_goods_id_exist(gid):
    is_exist_flag = False
    for goods in goods_list():
        if goods['no'] == gid:
            is_exist_flag = True
    return is_exist_flag


# 通过商品编号获取商品,返回商品字典
def get_goods_by_gid(gid):
    _good_list = goods_list()
    for goods in _good_list:
        if goods['no'] == gid:
            return goods


if __name__ == "__main__":
    exit_sys_flag = True
    print(print_welcome_menu())

    while exit_sys_flag:
        print(print_choose_menu())
        choose = raw_input('请选择功能编号[1-5]:')
        # 退出循环,退出系统
        if choose == "5":
            exit_sys_flag = False
            continue

        # 不在选择的菜单中，重新选择
        if choose not in ('1', '2', '3', '4'):
            print('\n您选择的功能编号不存在,请重新选择！\n')
            continue

        # 选择购物菜单
        if choose == "1":
            choose_loop_flag = True
            while choose_loop_flag:
                # 打印商品菜单
                print_goods_list(goods_list())
                goods_no = raw_input('请选择要购买的商品编号(quit 返回主菜单): ').strip()
                if goods_no == "quit":
                    choose_loop_flag = False
                    continue

                # 如果输入的商品编号不存在
                if not check_goods_id_exist(goods_no):
                    print('\n\033[1;31m您输入的商品编号不存在,请重新选择\033[0m\n')
                    continue
                else:
                    choose_goods = get_goods_by_gid(goods_no)
                    # 检查余额是否可以购买商品
                    if USER_ACCOUNT >= choose_goods['price']:
                        # 保存到购物车
                        USER_SHOPPING_CART.append(choose_goods)
                        # 扣款
                        USER_ACCOUNT -= choose_goods['price']
                        # 打印购物车信息
                        print_goods_list(USER_SHOPPING_CART)
                        goon_shop_flag = raw_input('\n已加入购物车,是否继续购买[y/n]:').strip().lower()
                        if goon_shop_flag == 'n':
                            choose_loop_flag = False
                        continue
                    # 余额不足啊
                    else:
                        print('\n\033[1;31m当前账户余额为 %d,无法购买此商品,请先充值!\033[0m\n' % USER_ACCOUNT)
                        continue

        # 选择查看账户余额
        if choose == "2":
            print('\n\033[1;32m您当前的账户余额为 %d 元.\033[0m\n' % USER_ACCOUNT)
            continue

        # 查看购物车
        if choose == "3":
            if len(USER_SHOPPING_CART) > 0:
                print_goods_list(USER_SHOPPING_CART)
            else:
                print('\n您当前的购物车无任何商品信息！\n')
            continue

        # 账户充值
        if choose == "4":
            add_money = raw_input('请输入您要充值的金额:').strip()
            # 输入必须为数字，检查是否合法
            while len(re.findall('[^0-9]', add_money)) > 0:
                print('\n\033[1;31m输入的金额不合法,必须为数字,请重新输入\033[0m\n')
                add_money = raw_input('请输入您要充值的金额:').strip()
            USER_ACCOUNT += int(add_money)
            print('\n\033[1;32m充值成功! 您当前的账户余额为: %d 元 \033[0m\n' % USER_ACCOUNT)
            continue
