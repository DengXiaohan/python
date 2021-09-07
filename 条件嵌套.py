print('请选择食品种类：1-盖浇钣  2-炒面  3-汤面')
zhonglei = input('请输入选号：')
if zhonglei == '1':
    print('1-红烧肉  2-土豆牛肉  3-宫爆鸡丁')
    xuanhao = input('请选择菜品号：')
    if xuanhao == '1':
        print('价格：18元')
    elif xuanhao == '2':
        print('价格：20元')
    elif xuanhao == '3':
        print('价格：16元')
    else:
        print('谢谢惠顾！')
elif zhonglei == '2':
    print('1-大份  2-小份')
    xuanhao = input('请选择份号：')
    if xuanhao == '1':
        print('价格：9元')
    elif xuanhao == '2':
        print('价格：7元')
    else:
        print('谢谢惠顾！')
elif zhonglei == '3':
    print('1-肉丝面  2-鸡蛋面')
    xuanhao = input('请选择种类：')
    if xuanhao == '1':
        print('价格：12元')
    elif xuanhao == '2':
        print('价格：8元')
    else:
        print('谢谢惠顾！')
else:
    print('谢谢惠顾！')
