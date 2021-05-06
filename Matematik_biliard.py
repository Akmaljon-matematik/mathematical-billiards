#BRR
#ikki idishdan foydalanid, berilgan litrda suv olish
b = int(input("Birinchi idish necha litr bo'lsin?-->", ))#birinchi idish hajmi so'raladi
i = int(input("Ikkinchi idish necha litr bo'lsin?-->", ))#ikkinchi idish hajmi so'raladi
zm = int(input("Necha litr olasiz?-->", ))#kerakli miqdor so'raladi
bih1 = max(b,i)#berilgan sonlarning kattasi aniqlanadi
iih1 = min(b,i)#berilgan sonlarning kichigi aniqlanadi
s=0#Shu yerda boshlab berilgan sonlarning o'zaro tub yoki yo'qligi aniqlanadi
while s==0:
	if bih1%iih1==0:
		programma_ishlasin=0#berilgan sonlar o'zaro tub emas

		s+=1
	else:
		b2= bih1 % iih1
		a2=iih1

		if b2==1:
			programma_ishlasin=1 #berilgan sonlar o'zaro tub

			s+=1
		else:
			iih1=b2
			bih1=a2
#berilgan sonlar o'zaro tub yoki yo'qligi aniqlandi
#bundan buyog'ida berilgan sonlardan iborat idishlardan foydalanib matematik billiard usuli yordamida kerakli hajmni aniqlash programmasi tuziladi
if programma_ishlasin ==1:#berilgan sonlar o'zaro tub bo'lsa programma ishlaydi
    Okboev=0
    bih = max(b,i)
    iih = min(b,i)
    while Okboev<=1:
        l=1
        bism=0#birinchi idishdagi suv miqdori
        iism=0#ikkinchi idishdagi suv miqdori
        akmal=0
        iibj=iih #ikkinchi idishdagi bo'sh joy
        while akmal==0:
            if bism==zm:
        		    print(l - 1, "-qadamda", zm, "litr suv olindi")
        		    akmal+=1
            elif iism == zm:
        		    print(l - 1, "-qadamda", zm, "litr suv olindi")
        		    akmal+=1
            elif iibj==0:
        	    iism=0
        	    iibj = iih - iism
        	    print(l, "-qadam:", "birinchi idish=", bism, "ikkinchi idish=", iism)
            elif bism==0:
                bism+=bih
                iibj = iih - iism
                #ikkinchi_idishdagi_suv_miqdori= Ikkinchi_idish_hajmi - ikkinchi_idishdagi_bush_joy
                print(l, "-qadam:", "birinchi idish=", bism, "ikkinchi idish=", iism)
            elif bism>iibj:
        	    bism= bism - iibj
        	    iism= iism + iibj
        	    iibj = iih - iism
        	    print(l, "-qadam:", "birinchi idish=", bism, "ikkinchi idish=", iism)
            elif bism!=0 and bism<=iibj:
        	    iism+=bism
        	    bism=0
        	    iibj = iih - iism
        	    print(l, "-qadam:", "birinchi idish=", bism, "ikkinchi idish=", iism)

            l+=1


        print(Okboev +1, "usulda", l-2, "qadamda chiqdi")
        bih = min(b,i)
        iih = max(b,i)
        m = l-2

        Okboev+=1
        print("eng qisqa yo'l ", min(m,l-2), "qadamda olinar ekan!")
elif programma_ishlasin ==0:
	print("""Bu sonlar o'zaro tub emas!
	Bunday sonlarda masala yechimga ega emas!""")

        #ALRA
