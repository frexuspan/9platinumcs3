zlist = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]

birth = int(input("Enter your birth year: "))

base = 1900

basefinal = base + ((birth - base) // 12) * 12

diff = birth - basefinal

if birth < base:
    print("Invalid Year, it should not be earlier than 1900")
else:
    zodiac = zlist[diff]
    print(f"Your zodiac sign is: {zodiac}")