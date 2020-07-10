#soru1
a = int(input("gün giriniz: "))
c = int(input("ay giriniz: "))
e = int(input("yıl giriniz: "))
l = {1:"ocak",2:"şubat",3:"mart",4:"nisan",5:"mayıs",6:"haziran",7:"temmuz",8:"agustos",9:"eylül",10:"ekim",11:"kasım",12:"aralık"}
y = (l[c])
print(a,"-",y,"-",e)

#soru3
list = []
a =[1,2,-1,2,5,2,-1,-2,2]
c = 0
e = 1
l = 2
döngü=0
name ="acelyabostancia"
dictionary={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14
            ,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,}
artan = 0
y = (dictionary[name[artan]])
print("Sonuçlar:")
for i in range(15):
    y = (dictionary[name[artan]])
    artan += 1
    list.append(y)
while (döngü < 5):
    döngü += 1
    sifre=(list[c]*a[0]+list[e]*a[1]+list[l]*a[2],list[c]*a[3]+list[e]*a[4]+list[l]*a[5],list[c]*a[6]+list[e]*a[7]+list[l]*a[8])
    c += 3
    e += 3
    l += 3
    print(sifre)

#soru4
list = []
a = 6
c = 2
for i in range(a):
    e = 0
    l = c
    y = 2
    if(c<a):
        c += 1
    for i in range(y, int(l)):
        if ((l) % i == 0):
            e = e + 1
    if (e == 0):
        print(l,"sayısı asal olduğu için listeye eklendi...")
        list.append(l)
    if (e == 1):
        print(l,"sayısı asal olmadığı için listeye eklenmedi...")
print(list)
