import time
import random
from datetime import datetime
print("*"*55)
print(f"@aurthor :Ansh Srivastav\n@date :{datetime.now()}")
print("*"*55)




#---------------Code ----------------------------------

for i in range(1,90):
    print('')
space = " "
for i in range(1,10000):
    count = random.randint(1,100)
    while count > 0:
        space +=" "
        count-=1
    
    if count%10==0:
        print(space+"  🍁🍁    Wish You  Happy Holi    ✨ 🎊")
    
    if count%9 == 0:
        print(space+" 🎈                         🍁                   ✨")
    
    if count%5==0:
        print(space +"  🌟         🍂         ⭐         🌀         💞      💟")
    
    if count%3==0:
        print(space+" 🎆             🎊        🎀        🌂         🌈")
    
    else:
        print(space+" 💟              🎈        ✨       🔻           🔺")
    space= " "
    
    time.sleep(0.5)
