time = int(input('Wpisz długość filmu w minutach: '))
i = time
reklam = -1

if time > 40:
    while time >= 40:
        reklam +=1
        time -= 40
else:
    reklam = 0


print(f"Podczas filmu zostanie wyświetlone {reklam} reklam, łączny czas antenowy wynosi {i + reklam * 20} minut.")