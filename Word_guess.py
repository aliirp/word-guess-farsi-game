import time
import random


def file_maker():
    try:
        f = open('word.txt', 'r', encoding='utf-8')
        f.close()
    except FileNotFoundError:
        f = open('word.txt', 'w', encoding='utf-8')
        f.write(',salam,chetori,khobi,moshkel,kharid,bazar,dastor,ahval,berim,zanboor,danesh,film,ketab,namak,hava,azadi,mahsool,shirin,rahnama,aseman,azar,farda,shanbe,hafte,daftar,davat,tabriz,azad,bekhand,mahnaz,soal,ghaza,sib,sofre,boshke,ashk,bekhoon,shak,neveshtan,balal,parvaz,daneshgah,bime,bahar,akhar,koodak,film,name,nimazendegi,ghalb,barf,panir,kar,gharib,dar,baran,asr,meshki,sabz,rooz,roozaneh,dast,cheshm,behesht,darvaazeh,tavajo,rasool,sang,ebrahim,sara,aramesh,khosh,ghalat,farman,tanz,ahang,parvaz,safar,daricheh,parandeh,bad,angizeh,pasokh,jang,hame,damavand,ashena,goftegoo,ehsas,bazi,gol,parand,tavakkol,namayesh,atash,aziz,safhe,mohandess,')
        f.write(',shomal,sport,melal,tavallod,namakdan,tehran,panahgah,salon,safarnameh,tanaz,golestan,neshan,saghf,harf,karaj,goftegoo,bozorg,hotel,mahi,khodro,savad,raghs,eshgh,torki,haft,mehrdad,ahangari,parvaneh,sobhan,rozane,avar,gozargah,darya,cheshmdooz,penhan,zendan,aseman,modares,bozorgtar,koodaki,baran,tansiz,bahador,eshtebah,namakdan,shooleh,mehran,pardis,shokolat,baraye,karafs,navid,sedaghat,parvaz,saranjam,anjir,honar,tavab,ardebil,dasht,bazargani,khoshbakhti,gavazn,nama,salman,eshtebah,zangir,baran,shenavar,negarestan,tajrobeh,navazi,parandegan,khatereh,basirat,afrooz,gasht,melat,nazanin,saadi,eshteghal,shahrivar,bahar,zarand,mashhad,sazesh,nahang,tangeh,taraneh,parvandeh,bina,sargarmi,atashin,zahedan,shanbe,bisheh,aslan,')
        f.close


def chose_word():
    f = open('word.txt', 'r')
    a = f.read()
    list = a.split(',')
    word = random.choice(list)
    return word


def bazi():
    name = input('esmet chiye: ')
    file_maker()
    word = chose_word()
    print(f'salam {name} be bazi hads kalame khosh oomadi!')
    print('har zamani khasti baraye bazgasht be meno bejaye harf adad 0 vared kon')
    print(f'tedad hads:{len(word)*5}')
    print('amade bash!')
    time.sleep(1.5)
    print('3', end='')
    time.sleep(1.5)
    print(f'\r2', end='')
    time.sleep(1.5)
    print(f'\r1', end='')
    time.sleep(1.5)
    print(f'\rshoroo!')
    start_time = time.time()
    a = ('_')*len(word)
    shans = len(word)*5
    right_answer = []
    fals_answer = []
    while shans > 0:
        print(f'in kalame {len(word)} harfiye')
        print(a)
        hads = input('yek harf hads bezan: ')
        shans -= 1
        if hads == '0':
            main()
        if hads in word:
            list = []
            right_answer.append(hads)
            n = 0
            l = -1
            for j in word:
                l += 1
                if j == hads:
                    n += 1
                    list.append(n)
                    a = f'{a[:l]}{hads}{a[l+1:]}'

            print(f'afarin in kalame {n} bar vojod dard tedad hads:{shans}')

        else:
            fals_answer.append(hads)
            print(f'eshteba!!!tdad hads:{shans}')

        if '_'not in a:
            print('afarin kalame ra hads zadi')
            print(f'shoma {(len(word)*5)-shans} bar eshtebah vared kardid.')
            print(f'list kalamat dorost vared shode betartib: {right_answer}')
            print(f'list kalamat eshtebah vared shode betartib: {fals_answer}')
            natige = 'bord'
            end_time = time.time()
            zaman = end_time-start_time
            break
    else:
        print('natoonesti hads bezani!!')
        print(f'shoma {len(word)*5} bar eshtebah vared kardid.')
        print(f'list kalamat dorost vared shode betartib: {right_answer}')
        print(f'list kalamat eshtebah vared shode betartib: {fals_answer}')
        natige = 'bakht'
        end_time = time.time()
    zaman = end_time-start_time
    print(f'zaman bazi: {zaman} saniye')
    if len(word)-shans == 0:
        laghab = 'khoda'
    elif len(word)-shans < 5:
        laghab = 'ostoore'
    elif len(word)-shans < 10:
        laghab = 'mamooli'
    elif len(word)-shans < 20:
        laghab = 'gagool'
    zakhire_info(name, natige, right_answer, fals_answer, zaman, laghab)
    sabt_record(zaman, name)
    main()


def zakhire_info(name, natige, dorost, ghalat, zaman, laghab):
    f = open(f'{name}.txt', 'a', encoding='utf-8')
    f.write(f'palyer name:{name}\n')
    f.write(f'{name} dar bazi ghabl {natige}\n')
    f.write(f'kaamti ke dorst hads zade shodand: {dorost}\n')
    f.write(f'kalmati ke eshtebah hds zade shoaand: {ghalat}\n')
    f.write(f'zaman bazi kardan: {zaman} saniye \n')
    f.write(f'laghab player {laghab}')


def tarikhche_bazikon():
    name = input('nam bazikon ra vred konid: ')
    name = f'{name}.txt'
    try:
        f = open(name, 'r')
        print(f.read())
        f.close()
    except FileNotFoundError:
        print('bazikon ta be hal bazi nakarde ast!')
    main()


def ezafe_kalame():
    f = open('word.txt', 'a')
    a = input('kalamat mored nazar khod ra ba 1 space vard konid:')
    list = a.split()
    for i in list:
        f.write(f'{i},')
    print('sabt shod')
    main()


def sabt_record(time, name):
    try:
        with open('record.txt', 'r', encoding='utf-8') as file:
            current_record = file.read().split(',')
            current_record_time = float(current_record[0])
            current_record_name = current_record[1]
    except FileNotFoundError:
        current_record_time = float('inf')
        current_record_name = ''
    if time < current_record_time:
        with open('record.txt', 'w', encoding='utf-8') as file:
            file.write(f'{time},{name}')
        print(f'{name} tabrik rekord jadid zadi ba zaman {time}')
    else:
        print(f'zaman shoma {time} saniye ast ke behtar as rekord {
              current_record_time} tavasot {current_record_name} nist.')


def sazande():
    print('ali mirahmadi')
    main()


def main():
    print('meno')
    print('0-khorooj')
    print('1-bazi')
    print('2-tarikhche bazikon')
    print('3-sabt kalme jadidi')
    print('4-moshakhasat daneshjoo')
    num = input('adad mord nzar ra vared konid: ')
    if num == '0':
        exit()
    elif num == '1':
        bazi()
    elif num == '2':
        tarikhche_bazikon()
    elif num == '3':
        ezafe_kalame()
    elif num == '4':
        sazande()
    else:
        print('namotabar')
        main()


main()

