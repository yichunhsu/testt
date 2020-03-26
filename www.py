import vending_machine.vending_service as machine#模組名稱   將眾多function組成一個模組，模組在整合package

#建立物件導向 專案架構
flag=True#while需放判斷式 True執行程式
from vending_machine.data import Drink

balance=0
drinks=[
    Drink("可口可樂",35),
    Drink("無糖茶裏王",33),
    Drink("台鹽水",36),
    Drink("貝納頌",35),
    Drink("Dr. Milk",40),
]
def deposit():#function方法提出(將迴圈內部提出，inport進主程式
    global balance#代表外面的balance,需要宣告 否者內部無法與外面對應
    value = eval(input("要放多少金額:"))
    while value < 1:
        print("=====儲存金額需大於零=====")
        value = eval(input("要放多少金額"))
    balance += value#區域變數
    print(f"存完後餘額是{balance}元")  # f表示模組連結，非f表示字串顯示


def buy():#function
    """
    儲值功能
    解釋程式碼用意
    :return:
    """
    global balance,drinks
    print("請選擇商品")
    # for item in drinks:
    # print(f"{item["名稱"]},{item["價錢"]})
    for i in range(len(drinks)):  # 取list總長度清單,ex:0,1,2,3,4
        print(f'({i + 1})\t{drinks[i].name}  {drinks[i].price}元')  # 取索引值
    choose = eval(input("請選擇:"))  # 儲存變數
    while choose < 1 or choose > 5:  #
        print("=====請輸入1-5之間=====")
        choose = eval(input("請選擇:"))
    buy_drink = drinks[choose - 1]
    while balance<buy_drink.price:
        print("=====餘額不足，需要繼續存錢?=====")
        want_deposit=input("y/n?")
        if want_deposit =="y":
            deposit()#表示存錢函式
        elif want_deposit=="n":
            break#跳出迴圈
        else:
            print("=====請重新輸入=====")

    if balance >= buy_drink.price:#儲值後餘額大於商品方可購買
    #     print("=====餘額不足=====")
    # else:
        print(f'已購買{buy_drink.name}  {buy_drink.price}元')
        balance -= buy_drink.price
        print(f"購買後餘額是{balance}元")

while flag:
    print("\n==================================")
    select=eval(input("1.儲錢\n2.購買\n3.看餘額\n4.離開\n請選擇:"))
    if select==1:
        machine.deposit()
    elif select==2:
        machine.buy()
    elif select==3:
        print(f"目前餘額是{machine.balance}元")
    elif select==4:
        print("多謝惠顧")
        flag=False#停止程式
        break
    else:
        print("=====請輸入1-4之間=====")
        continue