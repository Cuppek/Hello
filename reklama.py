time = int(input('Wpisz długość filmu w minutach: '))
i = time
reklam = 0


while time > 40:
    reklam +=1
    time -= 40

print(f"Podczas filmu zostanie wyświetlone {reklam} reklam, łączny czas antenowy wynosi {i + reklam * 20} minut.")