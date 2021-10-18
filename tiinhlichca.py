#@title Lich ca Ver-1.8
from datetime import datetime
from datetime import date
import datetime
 
#chuyen thoi gian ve mui gio ha noi
tz_hanoi = datetime.timezone(datetime.timedelta(hours=7))
dt = datetime.datetime.now(tz_hanoi)
dt3 = dt.strftime("Thoi gian---------: %H:%M:%S")
dt4= dt.strftime("%Y-%m-%d")
dt5= dt.strftime("Hom nay la ngay   : %d-%m-%Y")
#in ra thoi gian ngay thang hom nay
print(dt3)
print(dt5)
 
 
 
#Chon ca hom nay 
 
#3ca 5 kip
_3_Ca_5kip ='Ca_1'#@param ["Ca_1", "Ca_2", "Ca_3","Ca_4","Ca_5"]
Ca_hien_tai='ngay cuoi'#@param ["ngay dau", "ngay cuoi", "O sau ngay","chieu dau","chieu cuoi","O sau chieu","Khuya đau","khuya cuoi","O dau","O cuoi"]
 
#3 ca 4 kip
_3_Ca_4kip ='Ca_1'#@param ["Ca_1", "Ca_2", "Ca_3","Ca_4"]
Ca__hien__tai='chieu dau'#@param ["ngay dau", "ngay cuoi", "O sau ngay","chieu dau","chieu cuoi","O sau chieu","Khuya đau","khuya cuoi"]
#@title Date fields { run: "auto" }
ngay_can_tinh = "2022-02-01" #@param {type:"date"}
#tinh khoang thoi gian tu ngay can tinh den hom nay
str2=ngay_can_tinh
dt1 = datetime.datetime.strptime(dt4, "%Y-%m-%d")
dt2 = datetime.datetime.strptime(str2, "%Y-%m-%d")
m=dt2-dt1
n=m.days
print()
print()
print('Ngay can tinh     :',ngay_can_tinh)
print()
 
#3 Ca 5 Kip
print( _3_Ca_5kip,": 3ca5kip")
if Ca_hien_tai=="ngay dau":
    Cangaydau=["ngay dau", "ngay cuoi", "O sau ngay","chieu dau","chieu cuoi","O sau chieu","Khuya đau","khuya cuoi","O dau","O cuoi"]
    vitrica=n%10
    print(Cangaydau[vitrica])
elif Ca_hien_tai=="ngay cuoi":
    Cangaycuoi=["ngay cuoi", "O sau ngay","chieu dau","chieu cuoi","O sau chieu","Khuya đau","khuya cuoi","O dau","O cuoi","ngay dau"]
    vitrica=n%10
    print(Cangaycuoi[vitrica])
elif Ca_hien_tai=="O sau ngay":
    CaOsaungay=["O sau ngay","chieu dau","chieu cuoi","O sau chieu","Khuya đau","khuya cuoi","O dau","O cuoi","ngay dau","ngay cuoi"]
    vitrica=n%10
    print(CaOsaungay[vitrica])
elif Ca_hien_tai=="chieu dau":
    Cachieudau=["chieu dau","chieu cuoi","O sau chieu","Khuya đau","khuya cuoi","O dau","O cuoi","ngay dau","ngay cuoi","O sau ngay"]
    vitrica=n%10
    print(Cachieudau[vitrica])
elif Ca_hien_tai=="chieu cuoi":
    Cachieucuoi=["chieu cuoi","O sau chieu","Khuya đau","khuya cuoi","O dau","O cuoi","ngay dau","ngay cuoi","O sau ngay","chieu dau"]
    vitrica=n%10
    print(Cachieucuoi[vitrica])
elif Ca_hien_tai=="O sau chieu":
    CaOsauchieu=["O sau chieu","Khuya đau","khuya cuoi","O dau","O cuoi","ngay dau","ngay cuoi","O sau ngay","chieu dau","chieu cuoi"]
    vitrica=n%10
    print(CaOsauchieu[vitrica])
elif Ca_hien_tai=="Khuya đau":
    Cakhuyadau=["Khuya đau","khuya cuoi","O dau","O cuoi","ngay dau","ngay cuoi","O sau ngay","chieu dau","chieu cuoi","O sau chieu"]
    vitrica=n%10
    print(Cakhuyadau[vitrica])
elif Ca_hien_tai=="khuya cuoi":
    Cakhuyacuoi=["khuya cuoi","O dau","O cuoi","ngay dau","ngay cuoi","O sau ngay","chieu dau","chieu cuoi","O sau chieu","Khuya đau"]
    vitrica=n%10
    print(Cakhuyacuoi[vitrica])
elif Ca_hien_tai=="O dau":
    CaOdau=["O dau","O cuoi","ngay dau","ngay cuoi","O sau ngay","chieu dau","chieu cuoi","O sau chieu","Khuya đau","khuya cuoi"]
    vitrica=n%10
    print(CaOdau[vitrica])
elif Ca_hien_tai=="O cuoi":
    CaOcuoi=["O cuoi","ngay dau","ngay cuoi","O sau ngay","chieu dau","chieu cuoi","O sau chieu","Khuya đau","khuya cuoi","O dau"]
    vitrica=n%10
    print(CaOcuoi[vitrica])
print()
 
#3 ca 4 Kip
print( _3_Ca_4kip,": 3ca4kip")
if Ca__hien__tai=="ngay dau":
    Cangaydau=["ngay dau", "ngay cuoi", "O sau ngay","chieu dau","chieu cuoi","O sau chieu","Khuya đau","khuya cuoi"]
    vitrica=n%8
    print(Cangaydau[vitrica])
elif Ca__hien__tai=="ngay cuoi":
    Cangaycuoi=["ngay cuoi", "O sau ngay","chieu dau","chieu cuoi","O sau chieu","Khuya đau","khuya cuoi","ngay dau"]
    vitrica=n%8
    print(Cangaycuoi[vitrica])
elif Ca__hien__tai=="O sau ngay":
    CaOsaungay=["O sau ngay","chieu dau","chieu cuoi","O sau chieu","Khuya đau","khuya cuoi","ngay dau","ngay cuoi"]
    vitrica=n%8
    print(CaOsaungay[vitrica])
elif Ca__hien__tai=="chieu dau":
    Cachieudau=["chieu dau","chieu cuoi","O sau chieu","Khuya đau","khuya cuoi","ngay dau","ngay cuoi","O sau ngay"]
    vitrica=n%8
    print(Cachieudau[vitrica])
elif Ca__hien__tai=="chieu cuoi":
    Cachieucuoi=["chieu cuoi","O sau chieu","Khuya đau","khuya cuoi","ngay dau","ngay cuoi","O sau ngay","chieu dau"]
    vitrica=n%8
    print(Cachieucuoi[vitrica])
elif Ca__hien__tai=="O sau chieu":
    CaOsauchieu=["O sau chieu","Khuya đau","khuya cuoi","ngay dau","ngay cuoi","O sau ngay","chieu dau","chieu cuoi"]
    vitrica=n%8
    print(CaOsauchieu[vitrica])
elif Ca__hien__tai=="Khuya đau":
    Cakhuyadau=["Khuya đau","khuya cuoi","ngay dau","ngay cuoi","O sau ngay","chieu dau","chieu cuoi","O sau chieu"]
    vitrica=n%8
    print(Cakhuyadau[vitrica])
elif Ca__hien__tai=="khuya cuoi":
    Cakhuyacuoi=["khuya cuoi","ngay dau","ngay cuoi","O sau ngay","chieu dau","chieu cuoi","O sau chieu","Khuya đau"]
    vitrica=n%8
    print(Cakhuyacuoi[vitrica])
 

