def bmi_hesapla(kilo, boy):
 try:

    bmi = kilo / (boy ** 2)

    if bmi < 18.5:
        return f"BMI: {round(bmi, 2)} Zayıf"
    elif 18.5 <= bmi < 25:
        return f"BMI: {round(bmi, 2)} Normal"
    elif 25 <= bmi < 30:
        return f"BMI: {round(bmi, 2)} Fazla kilolu"
    else:
        return f"BMI: {round(bmi, 2)} Obez"
 except ZeroDivisionError:
        return "Hata: Boy değeri 0 olamaz."
 except Exception:
    return "Beklenmeyen bir hata oluştu."

# Kullanıcıdan bilgileri almak için
if __name__ == "__main__":
    try:

        kilo = float(input("Kilonuzu kilogram cinsinden giriniz: "))
        boy = float(input("Boyunuzu metre cinsinden giriniz: "))

        # BMI hesaplama ve sonucu almak için
        print(bmi_hesapla(kilo, boy))
    except ValueError:          
     print("Hata: Lütfen sayısal bir değer giriniz.")