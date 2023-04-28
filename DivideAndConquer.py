def coinExchange(amount, coinList):
    ans = [0, 0, 0, 0]
    all = coinList[0] + coinList[1] + coinList[2] + coinList[3]
    check = coinList[0]*10 + coinList[1]*5 + coinList[2]*2 + coinList[3]*1
    while amount > 0:
        if check < amount:
            print("Coins are not enough")
            print(check)
            break
        else:
            if amount-10 >= 0 and coinList[0] > 0:
                ans[0] += 1
                coinList[0] -= 1
                amount -= 10
                #print("10")
            elif amount-5 >= 0 and coinList[1] > 0:
                ans[1] += 1
                coinList[1] -= 1
                amount -= 5
                #print("5")
            elif amount-2 >= 0 and coinList[2] > 0:
                ans[2] += 1
                coinList[2] -= 1
                amount -= 2
                #print("2")
            elif amount-1 >= 0 and coinList[3] > 0:
                ans[3] += 1
                coinList[3] -= 1
                amount -= 1
                #print("1")
    #print(coinList[0])
    num = ans[0] + ans[1] + ans[2] + ans[3]
    print(ans)
    print("number of coins :", num)

coinList = [10, 10, 10, 10]
coinExchange(127, coinList)
