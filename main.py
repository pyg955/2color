from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import  QIcon
import os
import sys
import random

class common:

    # 判断列表是否存在重复
    def repeat_list(self,lista):
        if len(lista) != len(set(lista)):
            return False
        else:
            return True

class LotterySimulation:

    # bonus_pool = 100000000
    # one_probability = 1/17721088
    # two_probability = 1/1181405
    # three_probability = 1/109389
    # four_probability = 1/2303
    # five_probability = 1/129
    # six_probability = 1/16

    # 初始化玩家选择的双色球数字,投注数量
    def __init__(self):
        self.red_ball = range(1, 34)
        self.blue_ball = range(1, 17)
        self.first_prize = 0
        self.second_prize = 0
        self.third_prize = 0
        self.fourth_prize = 0
        self.fifth_prize = 0
        self.sixth_prize = 0
        self.accumulated_bonus = 0


    # 玩家选号与投注
    def player(self, red_num, blue_num, pay_num):
        self.red_num = red_num
        self.blue_num = blue_num
        self.pay_num = pay_num
        self.ball_pool = [self.red_num, self.blue_num]
        print("玩家选择：" + str(self.ball_pool))
        return self.bonus_calculation()


    # 随机产生中奖号码
    def winning_number(self):
        self.winning_red_ball_pool = sorted(random.sample(self.red_ball, 6))
        self.winning_blue_ball_pool = sorted(random.sample(self.blue_ball, 1))

        # 测试
        # self.winning_red_ball_pool = [1, 2, 3, 4, 5, 6]
        # self.winning_blue_ball_pool = [16]

        self.winning_list = [self.winning_red_ball_pool, self.winning_blue_ball_pool]
        return self.winning_list

    # 中奖比对
    def compare_number(self):
        self.winning_list = self.winning_number()
        print("开奖号码："+str(self.winning_list))
        self.right_num = []
        self.wrong_num = []
        self.final_right_list = [] # 最终中奖数字清单
        self.final_wrong_list = [] # 最终未中奖数字清单
        for i_num in self.ball_pool[0]:
            if i_num in self.winning_list[0]:
                self.right_num.append(i_num)

            else:
                self.wrong_num.append(i_num)

        self.final_right_list.append(self.right_num)
        self.final_wrong_list.append(self.wrong_num)

        if self.ball_pool[1] == self.winning_list[1]:
            self.final_right_list.append(self.ball_pool[1])
            self.final_wrong_list.append([])
        else:
            self.final_right_list.append([])
            self.final_wrong_list.append(self.ball_pool[1])
        print("中奖号码：" + str(self.final_right_list) )
        # print("未中奖号码：" + str(self.final_wrong_list))
        return self.final_right_list, self.final_wrong_list

    # 中奖结果
    def result(self):
        self.final_right_list, self.final_wrong_list = self.compare_number()
        self.final_right_red_list = self.final_right_list[0]
        self.final_right_blue_list = self.final_right_list[1]
        self.red_count = len(self.final_right_red_list)  # 红球中奖数
        self.blue_count = len(self.final_right_blue_list) # 蓝球中奖数
        self.final_result = 0 # 中奖结果

        # 一等奖
        if self.red_count == 6 and self.blue_count == 1:
            self.final_result = 1
            self.first_prize += 1
            print("一等奖")
        elif self.red_count == 6 and self.blue_count == 0:
            self.final_result = 2
            self.second_prize += 1
            print("二等奖")
        elif self.red_count == 5 and self.blue_count == 1:
            self.final_result = 3
            self.third_prize += 1
            print("三等奖")
        elif self.red_count == 5 or (self.red_count == 4 and self.blue_count == 1):
            self.final_result = 4
            self.fourth_prize += 1
            print("四等奖")
        elif self.red_count == 4 or (self.red_count == 3 and self.blue_count == 1):
            self.final_result = 5
            self.fifth_prize += 1
            print("五等奖")
        elif self.red_count == 2 and self.blue_count == 1:
            self.final_result = 6
            self.sixth_prize += 1
            print("六等奖")
        elif self.red_count == 1 and self.blue_count == 1:
            self.final_result = 6
            self.sixth_prize += 1
            print("六等奖")
        elif self.blue_count == 1:
            self.final_result = 6
            self.sixth_prize += 1
            print("六等奖")
        else:
            print("本次未中奖")
        return self.final_result

    # 奖金计算
    def bonus_calculation(self):
        self.bonus = 0
        self.final_result = self.result()
        if self.final_result == 1:
            self.bonus += 5000000
        elif self.final_result == 2:
            self.bonus += 1250000
        elif self.final_result == 3:
            self.bonus += 3000
        elif self.final_result == 4:
            self.bonus += 200
        elif self.final_result == 5:
            self.bonus += 10
        elif self.final_result == 6:
            self.bonus += 5
        self.bonus *= self.pay_num
        self.accumulated_bonus += self.bonus
        print("本次奖金数为：" + str(self.bonus))
        return self.bonus

    # 获取中奖次数
    def get_winner_count(self):
        self.winner_count = {
            "一等奖：":self.first_prize,
            "二等奖：":self.second_prize,
            "三等奖：":self.third_prize,
            "四等奖：":self.fourth_prize,
            "五等奖：":self.fifth_prize,
            "六等奖：":self.sixth_prize
        }
        return self.winner_count

    # 获取累计奖金
    def get_accumulated_bonus(self):
        return self.accumulated_bonus

class my:

    def __init__(self):
        self.money = 100

    def save_money(self, num):
        self.money += num

    def get_money(self, num):
        if self.money >= num:
            self.money -= num



class lotteryStore:

    def __init__(self):
        self.my_person = my()
        self.my_lottery = LotterySimulation()
        self.winner_count = 0
        self.accumulated_pay = 0
        self.total_buy = 0
        self.winner_count_dir = {
            "一等奖：": 0,
            "二等奖：": 0,
            "三等奖：": 0,
            "四等奖：": 0,
            "五等奖：": 0,
            "六等奖：": 0
        }

    # 判断余额是否足够
    def jugde_balance(self, pay_num):
        self.pay_money = 2 * pay_num
        if self.pay_money > self.my_person.money:
            return 0
        else:
            print('本次花费：' + str(self.pay_money))
            self.my_person.get_money(self.pay_money)
            self.accumulated_pay += self.pay_money
            return 1

    # 购买彩票
    def buy_lottery(self, red_num, blue_num, pay_num):
        self.this_result = self.my_lottery.player(red_num, blue_num, pay_num)
        if self.this_result > 0:
            self.my_person.save_money(self.this_result)
            self.winner_count += 1
        self.winner_count_dir = self.my_lottery.get_winner_count()
        print('目前银行账号余额：' + str(self.my_person.money))

    # 多次购买单式彩票循环
    def normal_multiple_purchases(self, red_num, blue_num, pay_num, buy_count):
        for i_buy in range(1, buy_count+1):
            self.total_buy += 1
            if self.jugde_balance(pay_num) == 1:
                self.buy_lottery(red_num, blue_num, pay_num)
                print(' '*11 + "*" * 25 + "这是第" + str(i_buy) + "次购买彩票,目前中奖：" + str(self.get_winner_count()) + "次" + "*" * 25)
            else:
                print('余额不足，银行余额剩余：' + str(self.my_person.money))
                break

    # 机选号码循环
    def machine_multiple_purchases(self, pay_num, buy_count):
        for i_buy in range(1, buy_count+1):
            self.total_buy += 1
            if self.jugde_balance(pay_num) == 1:
                self.msn_red_ball_pool = sorted(random.sample(range(1, 34), 6))
                self.msn_blue_ball_pool = sorted(random.sample(range(1, 17), 1))
                self.buy_lottery(self.msn_red_ball_pool, self.msn_blue_ball_pool, pay_num)
                print(' '*11 + "*" * 25 + "这是第" + str(i_buy) + "次购买彩票,目前中奖：" + str(self.get_winner_count()) + "次" + "*" * 25)
            else:
                print('破产!!!银行余额剩余：' + str(self.my_person.money))
                break

    def print_winner_info(self):
        self.text = "中奖详情"
        self.text1 = str(self.winner_count_dir)  # 累计中奖情况
        self.text2 = "累计中奖金额：" + str(self.my_lottery.get_accumulated_bonus())  # 累计中奖金额
        self.text3 = "银行账号当前余额：" + str(self.my_person.money)  # 目前银行账号余额
        self.text4 = "累计花费金额："  + str(self.accumulated_pay)  # 累计花费金额

        self.screen_width = 100
        self.txt_width = len(self.text1) +20
        self.left_margin = (self.screen_width - self.txt_width) // 2  # 框左边的空格数
        self.box_width = self.screen_width // 4 + self.left_margin + 5  # 居中

        print(' ' * self.left_margin + '+' + '-' * (self.txt_width) + '+')
        print(' ' * self.left_margin + ' ' * (self.box_width + 4) + self.text)
        print(' ' * self.left_margin  + ' ' * (self.txt_width) )
        print(' ' * self.left_margin  + ' ' * 3 + self.text1 )
        print(' ' * self.left_margin  + ' ' * (self.box_width) + self.text2)
        print(' ' * self.left_margin  + ' ' * (self.box_width) + self.text3)
        print(' ' * self.left_margin + ' ' * (self.box_width) + self.text4)
        print(' ' * self.left_margin  + ' ' * (self.txt_width) )
        print(' ' * self.left_margin + '+' + '-' * (self.txt_width) + '+')



    def get_winner_count(self):
        return self.winner_count

    def get_total_buy(self):
        return self.total_buy



# UI界面
class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load("UI.ui")
        self.my_program = lotteryStore()
        self.my_common = common()
        self.ui.lineEdit.setText(str(self.get_money()))

        self.ui.pushButton_4.clicked.connect(self.button_reflash)  # 刷新按钮
        self.ui.pushButton_3.clicked.connect(self.button_save)  # 存钱按钮
        self.ui.pushButton.clicked.connect(self.nmp)  # 单式投注
        self.ui.pushButton_2.clicked.connect(self.mmp)  # 机器投注

    # 结果展示
    def result_show(self):
        self.bet_multiple = self.get_bet_multiple()
        self.buy_count = self.get_buy_count()
    #   if self.get_money() - 2*self.bet_multiple*self.buy_count > 0:
        if self.get_money() - 2*self.bet_multiple > 0:
            self.ui.textEdit.setText("累计购买：" + str(self.my_program.get_total_buy()) + "期\n" +
                                     "一等奖：" + str(self.my_program.winner_count_dir["一等奖："]) + "次\n" +
                                     "二等奖：" + str(self.my_program.winner_count_dir["二等奖："]) + "次\n" +
                                     "三等奖：" + str(self.my_program.winner_count_dir["三等奖："]) + "次\n" +
                                     "四等奖：" + str(self.my_program.winner_count_dir["四等奖："]) + "次\n" +
                                     "五等奖：" + str(self.my_program.winner_count_dir["五等奖："]) + "次\n" +
                                     "六等奖：" + str(self.my_program.winner_count_dir["六等奖："]) + "次\n" +
                                     "累计中奖次数：" + str(self.my_program.get_winner_count()) + "\n" +
                                     "累计中奖金额：" + str(self.my_program.my_lottery.get_accumulated_bonus()) + "\n" +
                                     "累计花费金额：" + str(self.my_program.accumulated_pay)
                                     )
        else:
            print(self.get_money())
            self.ui.textEdit.setText("余额不足！无法继续购买，请充值！" + "\n" +
                                     "累计购买：" + str(self.my_program.get_total_buy()) + "期\n" +
                                     "一等奖：" + str(self.my_program.winner_count_dir["一等奖："]) + "次\n" +
                                     "二等奖：" + str(self.my_program.winner_count_dir["二等奖："]) + "次\n" +
                                     "三等奖：" + str(self.my_program.winner_count_dir["三等奖："]) + "次\n" +
                                     "四等奖：" + str(self.my_program.winner_count_dir["四等奖："]) + "次\n" +
                                     "五等奖：" + str(self.my_program.winner_count_dir["五等奖："]) + "次\n" +
                                     "六等奖：" + str(self.my_program.winner_count_dir["六等奖："]) + "次\n" +
                                     "累计中奖次数：" + str(self.my_program.get_winner_count()) + "\n" +
                                     "累计中奖金额：" + str(self.my_program.my_lottery.get_accumulated_bonus()) + "\n" +
                                     "累计花费金额：" + str(self.my_program.accumulated_pay)
                                     )
            QMessageBox.warning(
                self.ui,
                '破产警告！',
                '余额不足，你已破产')

    # 机投
    def mmp(self):
        self.bet_multiple = self.get_bet_multiple()
        self.buy_count = self.get_buy_count()
        self.my_program.machine_multiple_purchases(self.bet_multiple, self.buy_count)
        self.ui.lineEdit.setText(str(self.get_money()))
        self.result_show()


    # 单式投注
    def nmp(self):
        self.red_list, self.blue_list = self.get_ball_num()
        # 判断是否有重复数字
        if self.my_common.repeat_list(self.red_list)  == True:
            self.bet_multiple = self.get_bet_multiple()
            self.buy_count = self.get_buy_count()
            self.my_program.normal_multiple_purchases(self.red_list, self.blue_list, self.bet_multiple, self.buy_count)  # 调用单式投注方法
            self.ui.lineEdit.setText(str(self.get_money()))
            self.result_show()
        else:
            QMessageBox.critical(
                self.ui,
                '错误',
                '红球存在重复号码')


    # 获取购买期数
    def get_buy_count(self):
        try:
            self.buy_count = int(self.ui.lineEdit_4.text())
            return self.buy_count
        except:
            QMessageBox.critical(
                self.ui,
                '错误',
                '请输入正确整数期数')

    # 获取单注倍数
    def get_bet_multiple(self):
        try:
            self.bet_multiple = int(self.ui.lineEdit_3.text())
            return self.bet_multiple
        except:
            QMessageBox.critical(
                self.ui,
                '错误',
                '请输入正确整数倍数')

    # 获取玩家红球、蓝球数字
    def get_ball_num(self):
        self.red_list = []
        self.blue_list = []
        self.red_list.append(self.ui.spinBox.value())  # 红球 1-6
        self.red_list.append(self.ui.spinBox_2.value())
        self.red_list.append(self.ui.spinBox_3.value())
        self.red_list.append(self.ui.spinBox_4.value())
        self.red_list.append(self.ui.spinBox_5.value())
        self.red_list.append(self.ui.spinBox_6.value())
        self.blue_list.append(self.ui.spinBox_8.value())  # 蓝球
        return self.red_list, self.blue_list


    # 存钱按钮
    def button_save(self):
        try:
            self.lineEdit_2_text = int(self.ui.lineEdit_2.text())
            print(type(self.lineEdit_2_text))
            self.my_program.my_person.save_money(self.lineEdit_2_text)
            self.ui.lineEdit.setText(str(self.get_money()))
        except:
            QMessageBox.critical(
                self.ui,
                '错误',
                '请输入正确整数金额')


    # 重置按钮
    def button_reflash(self):
        # 重置程序
        self.my_program = lotteryStore()
        self.my_common = common()
        self.ui.lineEdit.setText(str(self.get_money()))
        self.ui.textEdit.clear()


    # 取金额
    def get_money(self):
        return self.my_program.my_person.money

if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon("loge.jpg"))
    stats = Stats()
    stats.ui.show()
    app.exec_()