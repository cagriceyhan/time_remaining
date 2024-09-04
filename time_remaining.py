import time

def remainingTimeFunc(seconds):
    while seconds>0:
        minutes, remainingSeconds = divmod(seconds,60) # divmod python'da built-in bir fonksiyondur.
        print(f"Süre: {minutes:02d}:{remainingSeconds:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
        


    print("Süreniz doldu")
    input("Çıkmak için bir tuşa basınız..")


while True:
    try:
        secondsInput = int(input("Lütfen kronometrenizin süresini saniye cinsinden giriniz: "))
        print("")
        if secondsInput < 0:
            print("Lütfen pozitif bir değer giriniz!\n")
        else:
            remainingTimeFunc(secondsInput)
            break
    except ValueError:
        print("\nLütfen saniye kısmına düzgün bir ifade giriniz!\n")


