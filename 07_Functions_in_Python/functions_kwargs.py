
def player_info(**kwargs):
    print('-------------------')
    for key in kwargs.keys():
        print(f"{key} : {kwargs[key]}")


player_info(name='Sachin', runs=12000)
player_info(name='Virat', runs=11000, avg=58.02)