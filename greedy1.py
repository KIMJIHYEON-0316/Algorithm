def min_coin_count(value, coin_list):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)

    for coin in coin_list:
        coin_num = value // coin
        total_coin_count += coin_num
        value -= coin_num * coin
        details.append([coin, coin_num])
    return total_coin_count, details


def min_coin_count2(value, coin_list):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)

# 안되는 이유: while 문을 돌면서 50원 단위일때 while문이 종료되어버림
    #while value >= coin_list[0]:
# 안되는 이유: while 문을 돌면서 10원 차례에서 나머지가 0이 되어서 마지막 반복문이 실행되지 않음
    #while value % coin_list[0] != 0:
# 계산식으로 처리하는게 아닌 리스트의 전체를 돌도록 반복문을 제어하면 정상적으로 됨 > for문으로 처리하는게 깔끔
    while coin_list:
        coin_num = value // coin_list[0]
        total_coin_count += coin_num
        value -= coin_num * coin_list[0]
        details.append([coin_list[0], coin_num])
        coin_list.pop(0)
    return total_coin_count, details


coin_list = [1, 100, 500, 50]

print(min_coin_count(4720,coin_list))
print(min_coin_count2(4720, coin_list))