import time
file = 'savol_4.txt'
new_file = 'savol_javob4.txt'

with open(f"{file}", "r") as f:   
    data = f.read()   
print(file, "nomli fayl oqilyapti..")
time.sleep(7)

with open(f"{new_file}", "w") as f:   
    f.write(data[::-1])
    print("aylantirilyapti..")
    time.sleep(3)
print("Prosses muafiqatli tugatildi!")    