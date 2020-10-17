field = [['A', 'H', 'O', 'J'],
         ['B', 'U', 'M', 'O'],
         ['K', 'L', 'U', 'K']]
stance = [1,1]
down_merger,up_merger = "M"
print(down_merger,up_merger)

for i in range(len(field)):
    print(stance[0]-(i+1),stance[1]-(i+1))
    print(stance[0]+(i+1),stance[1]+(i+1))
    print(stance[1]-(i+1),stance[0]+(i+1))
    print(field[stance[0]-(i+1)][stance[1]-(i+1)])
    print(field[stance[0]+(i+1)][stance[1]+(i+1)])
    print(field[stance[0]-(i+1)][stance[1]+(i+1)])
    print(field[stance[0]+(i+1)][stance[1]-(i+1)])
    if stance[0]-(i+1) > 0 or stance[1]-(i+1) > 0:
        break
