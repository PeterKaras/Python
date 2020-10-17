finding_city = [['01:14', 'Londyn', 'Pariz']]
task = [["potkan","Londyn","Pariz"]]
seperated_cities = ["Londyn","Pariz"]
result = 30
for i in range(len(task)):
    if seperated_cities.index(task[i][1]) <= seperated_cities.index(task[i][2]):
        result *= abs(seperated_cities.index(task[i][1]) - seperated_cities.index(task[i][2]))
    else:
        result *= seperated_cities.index(task[i][2])+1
    print(result)
    my_time = finding_city[0][0]
    print(my_time)
    print(int(my_time[0:2])*60)
    minutes = int(my_time[0:2])*60 + int(my_time[3:5]) + result
    print(minutes)
            
    result = 30
    print("{}:{}".format(*divmod(minutes, 60)))
