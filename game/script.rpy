# Вы можете расположить сценарий своей игры в этом файле.

# Определение переменных
default health = 24
default gold = 20
default mastery = 12
default luck = 12
default bribeGuard = 0
default meal = 2
default factOfEatingInPrison = 0
default sword = 1
default twoHandedSword = 0 # двуручный меч
default axe = 1 #Топор
default bowAndArrows = 0 #Лук и стрелы с серебрянными наконечниками
default dice = 1
default twodice = 2
default festival = 0
default blackmask = 1 # Черная маска
default healingPotion = 1 # Зелье здоровья
default bagWithThreeStones = 1 # Мешочек с камнями
default servingOfSeaSand = 1 # порция Морского Песка
default chainPrice = 0
default perch = 0
default magicalSelfLockingChain = 0
default summ = 0
default loop = 0
default bidAmount = 0
default targAmount = 0
default winner = 0
default winsum = 0
default braceletBones = 1 # Косятной браслет
default streetfighter = 0
default dimChain = 0 # Тусклая цепь
default goldFramedMirror = 0 # Заркало в золотой рамке
default scrollParchment = 0 # Свиток пергамента
default chainmailGloves = 0
default leatherGloves = 0
default bottleWithTheInscription = 0 #Бутылка с надписью: «Таинственное зелье»
default honeycombWithBeeswax = 0 #Соты с пчелиным воском / пчелиный воск
default bottleDust = 1 #Маленький флакон с пылью
default kharLibra = 0
default backlandLibra = 0
default goatCheese = 0 #Козий сыр
default emptyWallet = 0 #Пустой кошелек
default goodLuckCharm = 0 #Талисман удачи
default cuffWithDarts = 0 #Манжета с дротиками
default poison = 0 #Яд
default spirits = 0 #Духи
default block61and140 = 0 #Блокировка переходов на 61 и 140
default ans = 0 #Ответ на вопрос Жреца
default wig = 0 #Парик
default copperKey = 0 # Медный ключ. Когда узнаешь, что за число на нем выгровированно, ПОПРАВЬ 143
default axeselect = 0
default hGhost = 8
default bambooFlute = 0 # Бамбуковая флейта
default goblinTeethBag = 0 # сумка с зубами гоблинов
default largeBackpack = 0 # большой рюкзак
default countBarter = 0
default goblinsTooth = 0 # Зубы гоблинов
default giantsTooth = 0 # Зубы великанов
default snakeShapedRing = 0 # Серебряное кольцо в форме змеи, обвивающейся вокруг пальца владельца. Параграф 130
default flint = 0 # огниво
default antidoteSnakeVenom = 0 #Антидот от змеиного яда
default label_counter = 0

# label choice_17  label choice_149

# Определение персонажей игры.
define e = Character(color="#c8ffc8")
define g = Character(_("Страж городских ворот"), color="#FA8072")
define i = Character(_("Игрок"), color="#9ACD32")
define s = Character(_("Система"), color="#7B68EE")
define o = Character(_("Старец"), color="#0000FF")
define be = Character(_("Черный эльф"), color="#F4A460")
define f = Character(_("Ход боя"), color="#483D8B")
define p = Character(_("Свинн-мастер"), color="#9ACD32")
define h = Character(_("Обитатель дома"), color="#FF6347")
define ork = Character(_("Орклинги"), color="#5F9EA0")
define bm = Character(_("Заросший щетиной мужчина"), color="#008080")
define rm = Character(_("Кто-то из тольпы"), color="#20B2AA")
define pr = Character(_("Зазывала при ринге"), color="#FFFFE0")
define ym = Character(_("Юноша-странник"), color="#1E90FF")
define bem = Character(_("Неопрятный бородач"), color="#FF00FF")
define bck = Character(_("Букмекер"), color="#FF00FF")
define lo = Character(_("Один из малышей орклингов"), color="#7B68EE")
define tw = Character(_("Горожанка"), color="#FF00FF")
define se = Character(_("Торговец"), color="#191970")
define sp = Character(_("Спрайт"), color="#CD853F")
define pi = Character(_("Пикси"), color="#BC8F8F")
define m = Character(_("Ученый и исследователь"), color="#A52A2A")
define inn = Character(_("Трактирщик"), color="#FF00FF")
define wwc = Character(_("Прихожанка"), color="#808000")
define bs = Character(_("Жрец"), color="#00FFFF")
define sa = Character(_("Матрос"), color="#008080")
define pa = Character(_("Художник"), color="#778899")
define fc = Character(_("Заклинатель огня"), color="#4169E1")
define el = Character(_("Эльвин"), color="#2F4F4F")
define cy = Character(_("Странное существо с закрытыми глазами"), color="#FAEBD7")
define osk = Character(_("Старик из гроба"), color="#BC8F8F")
define lbg = Character(_("Маленький бородатый гном"), color="#8A2BE2")
define pm = Character(_("Нищий"), color="#DA70D6")
define ta = Character(_("Надпись на табличке"), color="#BA55D3")
define sg = Character(_("Городской стражник"), color="#0000FF")
define idd = Character(_("Идол"), color="#A0522D")
define ga = Character(_("Ворота"), color="#808080")
define spoot = Character(_("Старший Дозорный в Форпостном Городке"), color="#FFA07A")
define ww = Character(_("Женский голос из колодца"), color="#FA8072")
define iw = Character(_("Незнакомец за спиной"), color="#00FF7F")
define sggh = Character(_("Охранник игорных залов"), color="#20B2AA")


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.


image Guard = "g.png"
image GuardHoldsHand = "ghh.png"
image Guard2 = "g2.png"
image Guard3 = "g33.png"
image OldMan = "o.png"
image OldManSleep = "os.png"
image Pork = "p.png"
image PorkDead = "pd.png"
image Bubble = "b.png"
image BlackMan = "bm.png"
image BlackManDead = "bmd.png"
image BlackManBow = "bmb.png"
image YoungMan = "ym.png"
image BeardedMan = "bem.png"
image Bookmaker = "bck.png"
image Townswoman = "tw.png"
image Magician = "m.png"
image MagicianNoLizard = "mnl.png"
image Innkeeper = "in.png"
image EvilInnkeeper = "ein.png"
image WomanWithChild = "wwc.png"
image Lizard = "ya.png"
image Sailor = "s.png"
image Caster = "c.png"
image Drunkard = "d.png"
image Elvin = "el.png"
image SlimeEater = "se.png"
image BambooFlute = "bf.png"
image GoblinTeethBag = "gtb.png"
image GoodLuckCharm = "glc.png"
image EnchantedCompass = "ec.png"
image LargeBackpack = "l.png"
image HoneycombWithBeeswax = "h.png"
image SnakeShapedRing = "ssr.png"
image SeniorPatrolOfficerOutpostTown = "spoot.png"
image SecurityGuardOfGamblingHalls = "sggh.png"


# данный код можно прописать в любом файле вашего проекта(например, в script.rpy)





python early:
    # Функция для показа полноэкранной рекламы
    def show_fullscreen_ad():
        renpy.emscripten.run_script("showFullscreenAd();")

    # Функция для показа видео с наградой (оставим ее)
    def show_rewarded_video():
        renpy.emscripten.run_script("showRewardedAd('reward_received');")

init python:
    if renpy.android:
        try:
            from jnius import autoclass, cast

            try:
                _activity = autoclass('org.renpy.android.PythonSDLActivity').mActivity
            except Exception:
                _activity = autoclass('org.kivy.android.PythonActivity').mActivity

            _Settings = autoclass('android.provider.Settings$Secure')
            _client_id = _Settings.getString(
                _activity.getContentResolver(), _Settings.ANDROID_ID
            )

            URL = autoclass('java.net.URL')
            String = autoclass('java.lang.String')

            _post_data = "clientId=" + str(_client_id) + "&group=khar"
            _post_bytes = String(_post_data).getBytes("UTF-8")

            _url = URL("https://khar.ttp3d.cn/counter.php")
            _conn = cast('java.net.HttpURLConnection', _url.openConnection())
            _conn.setRequestMethod("POST")
            _conn.setDoOutput(True)
            _conn.setConnectTimeout(15000)
            _conn.setReadTimeout(15000)
            _conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded")

            _os = _conn.getOutputStream()
            _os.write(_post_bytes)
            _os.flush()
            _os.close()

            _conn.getResponseCode()
            _conn.disconnect()
        except Exception:
            pass

# Игра начинается здесь:

screen game_over():
    modal True
    frame:
        xalign 0.5 yalign 0.5
        padding (20, 20)
        vbox:
            text "游戏结束" size 40 color "#ff0000" xalign 0.5
            text "您的健康已耗尽！" size 24 xalign 0.5
            textbutton "退出" xalign 0.5 action Quit(confirm=False)
            textbutton "重新开始" xalign 0.5 action Start()

screen victory():
    modal True
    frame:
        xalign 0.5 yalign 0.5
        padding (20, 20)
        vbox:
            text "胜利！" size 40 color "#00ff00" xalign 0.5
            text "您已经克服了Khar并进入了Bakland！" size 24 xalign 0.5
            text "我们的故事到此结束。" size 20 xalign 0.5
            text "感谢您的游玩！" size 20 xalign 0.5
            textbutton "再玩一次" xalign 0.5 action Start()

screen rune_choice():
    modal True  # Блокирует взаимодействие с фоном
    frame:
        xalign 0.5 yalign 0.5
        padding (20, 20)
        hbox:
            spacing 20
            imagebutton:
                idle "r1.png"
                action Jump("choice_115")
            imagebutton:
                idle "r2.png"
                action Jump("choice_255")
            imagebutton:
                idle "r3.png"
                action Jump("choice_274")
            imagebutton:
                idle "r4.png"
                action Jump("choice_72")

style small_say_window:
    is say_window  # Наследуем базовый стиль диалогового окна
    xsize 800      # Ширина окна (меньше стандартного, например, 1280)
    ysize 200      # Высота окна
    padding (20, 20)  # Уменьшенные отступы внутри окна


label start:

    play music "audio/main_theme.mp3" loop
    scene 1-1

    narrator "Кхар – место, где правит хаос. Этот город - ворота в Бакланд."

    #e "Вы смотрите вниз"

    narrator "Кхар расположен у подножия Холмов Шамутанти, на берегу стремительно текущей великой реки Джабаджи"

    e "Вы останавливаетесь на середине спуска, чтобы осмотреться"

    scene 1-11 with dissolve
    pause 1

    e "Легенда гласит, что Кхар возник много лет назад, как приют пилигримов рядом с единственной удобной переправой на реке. Но это не слишком правдоподобная история."

    scene 1-2 with dissolve
    pause 0.5

    e "Вы больше верите в то, что на этом месте изначально было логово речных пиратов, всевозможных злодеев и головорезов"

    scene 1-12 with dissolve
    pause 0.5

    e "Ходят слухи, что этот сброд не брезговал помощью всякой нечести"

    #e "Которые устраивали засады на небольшие парусные суда"

    #e "перевозившие грузы между озером Лумле и Кахабадским морем"

    scene 1-11 with dissolve
    pause 0.5

    e "Вы верите в эту легенду потому, что с виду мирный город наполнен ловушками для противостояния злым существам"

    #e "Город стал, как магнитом, притягивать к себе все отребье из Бакланда и Шамутанти."

    #e "Множество злых существ, готовых убить родного брата за шнурки от ботинок, заполонили город."

    #e "Их беззаконное поведение породило сложную систему ловушек, разработанную жителями города для защиты от бродящих по улицам преступников."

    #scene 1-3 with dissolve
    #pause 0.5

    e "Именно поэтому Кхар получил прозвище Город Ловушек"

    e "Цель вашей миссии лежит далеко за пределами Кхара, и, зная его репутацию, вы бы предпочли не проходить через это место. Но иного пути нет!"

    #e "Но пройти надо, ибо иного пути нет"

    #e "С вашего наблюдательного пункта вы можете окинуть взглядом крепостную стену, окружающую город."

    e "Только двое ворот соединяют Кхар с остальным миром. Перед вами Южные Врата - единственный вход со стороны реки. На противоположной стороне города находятся Северные Врата – путь в Бакланд."

    scene 1-4 with dissolve
    pause 0.5

    e "Вы громко стучите, чтобы привлечь внимание стражи"

    play sound "audio/1-1.mp3"

    scene 1-5 with dissolve
    pause 0.5

    show Guard at Position(xalign=0.2)

    g "Кто идёт?"

    i "Я Бондис из Дампуса. Иду навестить отца."

    g "Подожди здесь, Бондис из Дампуса. Я доложу офицеру."

    menu:
        "Подождать":
            jump choice_225
        "Быстро предложить ему взятку в две золотых. {color=#FF00FF}Количество денег у вас: [gold]{/color}":
            if gold >= 2:
                jump choice_59
            else:
                i "У вас недостаточно золота, чтобы дать взятку"
                jump choice_225

label choice_225:

        scene 1-5

        show Guard at Position(xalign=0.2)

        hide Guard with moveoutright

        show Guard at Position(xalign=0.8)

        g "Эй, ты - из Дампуса, входи!"

        scene 225-11 with dissolve
        pause 2

        show Guard at Position(xalign=0.8)

        show Guard2 at Position(xalign=0.5)

        show Guard3 at Position(xalign=0.2)

        g "Ты арестован!"

        scene 225-1 with dissolve
        pause 0.1

        e "Сделав несколько шагов, вы чувствуете, как вам накидывают на голову мешок, после чего хватают за руки и плечи"

        e "Вы боретесь, но стражники крепко держат вас и куда-то тащат"

        if bribeGuard == 0:
            jump choice_291
        if bribeGuard == 1:
            jump choice_36

label choice_59:
        scene 1-5

        show GuardHoldsHand at Position(xalign=0.2)

        $ gold -= 2

        $ bribeGuard = 1

        s "Количество ваших золотых монет уменьшилось на два и теперь равно {color=#FF00FF}[gold]{/color}"

        g "Пожалуйста, немножко подожди."

        #s "Перед началом следующей главы будет короткая рекламная пауза."
        #$ renpy.pause(2.0) # Даем игроку время прочитать сообщение
        #$ show_fullscreen_ad()
        # Вызываем нашу специальную метку для показа рекламы
        #call show_interstitial_ad

        #s "Спасибо за терпение! Начинаем вторую главу."

        jump choice_225

label choice_36:
    scene 225-1

    menu:
        "Попытаться доставить неприятности стражнику, объявив о его взяточничестве":
            jump choice_126
        "Промолчать":
            jump choice_291

label choice_291:
    scene 291-1 with dissolve
    pause 0.5

    e "Стражники подтаскивают вас к сторожке и заталкивают внутрь"

    scene 291-2 with dissolve
    pause 0.5

    e "А потом запирают за вами дверь"

    jump choice_254

label choice_254:
    scene 254-1 with dissolve
    pause 0.5

    show OldMan

    o "Что привело вас в это злосчастное место?"
    i "Я просто хотел пройти сквозь город"
    o "Тогда я понимаю, незнакомец, что вы колдун. Раньше это тоже было и моей профессией, пока судьба - с небольшой помощью огра из шахты Шанкера - не положила конец моим амбициям и моей карьере. Только чародей может знать заклинание, открывающее Северные Врата."
    i "Так вы знаете заклинание или нет?"
    o "Только Первый Архонт города знает его целиком. Есть еще четыре знатных горожанина, которые знают по одной строке."
    i "Кто эти знатные горожане?"
    o "Один какой-то ученый, остальных я вообще не знаю."
    i "А где мы находимся?"
    o "Это здание городской тюрьмы. Как только офицеры охраны убедятся, что вы не опасны вас освободят."
    i "Как долго ждать?"
    o "День или два."

    jump choice_260

label choice_126:
    scene 225-1
    e "Вы поспешно рассказываете другим стражникам о 2 золотых, которые их товарищ забрал у вас. Они с подозрением смотрят на часового у ворот, но он сердито отрицает ваши обвинения и бьет вас в живот."
    $ health -= 2
    s "Количество вашего здоровья уменьшилось на два и теперь равно {color=#FF00FF}[health]{/color}"
    if health > 0:
        jump choice_291
    else:
        jump game_over

label choice_260:
    scene 254-1
    show OldMan
    e "День проходит, но стражников все нет."

    if meal > 0:
        menu:
            "Перекусить. Количество еды у вас на {color=#FF00FF}[meal]{/color} приемов пищи.":
                jump choice_308
            "Не перекусывать":
                jump choice_333
    else:
        jump choice_333

label choice_308:
    scene 254-1
    show OldMan
    $ meal -= 1
    s "Количество вашей еды теперь равно {color=#FF00FF}[meal]{/color}"
    e "Еда восстанавливает вам 2 очка Выносливости"
    $ health += 2
    s "Количество вашего здоровья теперь равно {color=#FF00FF}[health]{/color}"
    e "Однако вы не смогли не поделиться едой со старцем"
    $ meal -= 1
    s "Количество вашей еды теперь равно {color=#FF00FF}[meal]{/color}"
    $ factOfEatingInPrison = 1
    jump choice_333

label choice_333:
    scene 254-1
    show OldMan
    e "Вас клонит в сон. Но можете ли вы доверять старику?"
    menu:
        "Свернуться калачиков на полу и заснуть":
            jump choice_21
        "Бодрствовать, не спуская глаз со своего рюкзака, в ожидании возвращения стражи":
            jump choice_102

label choice_21:
    scene 254-1
    show OldMan
    e "Сон восстанавливает вам 2 очка Выносливости, на рассвете вы просыпаетесь."
    $ health += 2
    s "Количество вашего здоровья теперь равно {color=#FF00FF}[health]{/color}"
    if factOfEatingInPrison == 0:
        e "Вы ничего не ели вчера, от голода теряете 3 очка Выносливости."
        $ health -= 3
        s "Количество вашего здоровья теперь равно {color=#FF00FF}[health]{/color}"
        if health <= 0:
            jump game_over
    hide OldMan with moveoutright

    show Guard

    g "Вы со стариком угрозы для города не представляете. Можете валить из темницы."

    scene 21-1 with dissolve
    pause 0.5
    e "Вы оба направляетесь в город, но ваш попутчик двигается на удивление шустро и вскоре оставляет вас позади."
    e "Вы видите, как он поворачивает направо на ближайшем перекрестке."
    e "Такая прыть кажется вам подозрительной, вы останавливаетесь и открываете рюкзак."
    scene 21-2 with dissolve
    pause 0.5
    e "Так и есть, вы не должны были доверять этому проходимцу, он 10 золотых монет."
    $ gold -= 10
    s "Количество вашего золота теперь равно {color=#FF00FF}[gold]{/color}"
    jump choice_81

label choice_102:
    scene 254-1
    show OldManSleep
    e "Вы ждете всю ночь, но стража не появляется, а старик мирно спит на скамье."
    e "Из-за бессонной ночи теряете 2 очка здоровья"
    $ health -= 2
    s "Количество вашего здоровья теперь равно {color=#FF00FF}[health]{/color}"
    if factOfEatingInPrison == 0:
        e "Вы ничего не ели вчера, от голода теряете 3 очка Выносливости."
        $ health -= 3
        s "Количество вашего здоровья теперь равно {color=#FF00FF}[health]{/color}"
        if health <= 0:
            jump game_over
    hide OldManSleep
    show Guard

    g "Вы со стариком угрозы для города не представляете. Можете валить из темницы."
    scene 21-1 with dissolve
    pause 0.5
    e "Вы оба направляетесь в город, но ваш попутчик двигается на удивление шустро и вскоре оставляет вас позади."
    e "Вы видите, как он поворачивает направо на ближайшем перекрестке"
    jump choice_81

label choice_81:
    scene 81-1 with dissolve
    pause 0.5
    e "Вы выходите на перекресток"
    e "Вы видите, как Старик забегает в одну из хижин справа"
    e "Осмотритесь, чтобы принять решение куда двигаться дальше"
    menu:
        "Пойти налево":
            jump choice_23
        "Продолжить идти прямо":
            jump choice_138
        "Пойти направо":
            jump choice_292

label choice_23:
    scene 23-1 with dissolve
    pause 0.5
    e "Странные лица выглядывают из окон, наблюдая за вами"
    show Guard at Position(xalign=0.8)
    show Guard2 at Position(xalign=0.5)
    show Guard3 at Position(xalign=0.2)
    e "Мгновенно среагировав на появление стражи, вы ныряете в темную хижину поблизости и прикрываете за собой дверь."
    scene 23-2 with dissolve
    pause 0.5
    e "В воздухе мрачной хижины пахнет друман-травой"
    be "Пыхнешь с нами?"
    menu:
        "Присесть и сделать пару затяжек":
            jump choice_150
        "Извиниться за беспокойство и выйти":
            jump choice_213
        "Попробовать выжать из них какую-либо информацию":
            jump choice_242
        "Взяться за оружие и атаковать их":
            jump choice_58

label choice_138:
    scene 138-1 with dissolve
    pause 0.5
    e "Вы продолжаете путь по дороге в сторону скопления небольших хижин."
    e "Пока вы проходите мимо этих домов, обитающие в них уродливые существа занимаются своими повседневными делами и наблюдают за вами."
    e "Немного дальше по пути вам попадется лежащее в сточной канаве лицом вниз тело."
    e "На первый взгляд это спящий нищий или пьяница."
    menu:
        "Остановиться и посмотреть, не нужна ли бедолаге ваша помощь":
            jump choice_256
        "Пройти мимо":
            jump choice_239

label choice_292:
    scene 292-1 with dissolve
    pause 0.5
    e "Старик скрылся в большой хижине с грязными стенами слева от дороги."
    menu:
        "Проследовать за ним":
            jump choice_66
        "Пересечь дорогу и войти в хижину напротив, из которой доносится аппетитный запах":
            jump choice_171
        "Миновать хижины":
            jump choice_294

label choice_150:
scene 23-2
e "Вы садитесь рядом с ними на край матраса."
e "Они скалятся вам, демонстрируя грязные зубы, и передают трубку."
e "Вы делаете несколько затяжек и откидываетесь на спину."
e "Трубка обходит всех по кругу, и вскоре вы вчетвером безучастно смотрите в потолок."
e "Вы начинаете чувствовать головокружение. Курение травки дает непредсказуемый эффект."
$ dice = renpy.random.randint(1, 6)
s "Вам достался случайный эффект от дурмант травы под номером {color=#FF00FF}[dice]{/color}"
if dice == 1:
    e "Эффект приятный и расслабляющий"
    e "У вас восстановилось 2 очка здоровья."
    $ health += 2
    s "Количество вашего здоровья теперь равно {color=#FF00FF}[health]{/color}"
    jump choice_242
if dice == 2:
    e "Вас охватывает огромное чувство уверенности"
    e "Ваше мастерство увеличивается на 1 пункт!"
    $ mastery += 1
    s "Уровень вашего мастерства теперь равен {color=#FF00FF}[mastery]{/color}"
    jump choice_242
if dice == 3:
    e "Вы чувствуете сонливость и спите в течение следующих двадцати минут."
    jump choice_242
if dice == 4:
    e "Вы не можете устоять перед желанием сделать что-нибудь иррациональное и даете 1 золотую монету каждому из эльфов."
    $ gold -= 3
    s "Количество вашего золота теперь равно {color=#FF00FF}[gold]{/color}"
    jump choice_242
if dice == 5:
    e "Вы ощущаете сильную паранойю"
    e "Вы теряете по одной единице здоровья и мастерства"
    $ health -= 1
    $ mastery -= 1
    s "Количество вашего здоровья теперь равно {color=#FF00FF}[health]{/color}"
    if health <= 0:
        jump game_over
    s "Уровень вашего мастерства теперь равен {color=#FF00FF}[mastery]{/color}"
    jump choice_242
if dice == 6:
    e "Вы становитесь жестоким и тянетесь к своему оружию"
    jump choice_58

label choice_213:
    scene 213-1 with dissolve
    pause 0.5
    e "Стражников уже не видно, и можно спокойно продолжить путь."
    scene 213-2 with dissolve
    pause 0.5
    e "Маленькая серебристая рыбка в пруду выныривает из-за камня и смотрит прямо на вас."
    e "Пузыри выходят у нее изо рта, это выглядит так, как будто она хочет вам что-то сказать!"
    e "Еще вы замечаете на дне пруда золотую монету"
    menu:
        "Нагнуться ближе к рыбке, чтобы узнать, что она говорит":
            jump choice_320
        "Вытащить из воды монету":
            jump choice_85
        "Продолжить свой путь":
            jump choice_28

label choice_242:
    scene 23-2

    e "Вы отчаянно пытаетесь завязать разговор, но курильщики очень рассеяны и ничего толком не говорят."
    e "Вы спрашиваете, не живет ли поблизости какой-нибудь ученый."
    e "Они тупо смотрят друг на друга, а потом один из них кивает и показывает рукой дальше по дороге, по которой вы шли. На этом вы заканчиваете беседу и уходите."
    jump choice_213

label choice_58:
    scene 58-1 with dissolve
    pause 0.5
    e "Эльфы с трудом встают на ноги и неуклюже нащупывают свое оружие. Сражайтесь с ними по одному."
    $ enemies = [
        {"name": "第一黑暗精灵", "mastery": 6, "health": 5}, # Первый Черный Эльф
        {"name": "第二黑暗精灵", "mastery": 7, "health": 4}, # Второй Черный Эльф
        {"name": "第三黑暗精灵", "mastery": 5, "health": 5}, # Третий Черный Эльф
    ]
    jump choice_58_loop

label choice_58_loop:
    if health <= 0:
        f "Твои силы иссякли в бою с [current_enemy['name']]! Ты падаешь без сознания."
        jump game_over

    $ living_elves = [e for e in enemies if e["health"] > 0]
    if not living_elves:
        f "Все эльфы повержены! Ты стоишь над их телами, тяжело дыша. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
        jump choice_251

    $ current_enemy = renpy.random.choice(living_elves)

    $ enemy_attack = renpy.random.randint(1, 12) + current_enemy["mastery"]
    $ player_attack = renpy.random.randint(1, 12) + mastery

    if enemy_attack == player_attack:
        f "Ты ([player_attack]) и [current_enemy['name']] ([enemy_attack]) наносите удары одновременно, но оба уклоняетесь! Никто не ранен. Твое здоровье: {color=#FF00FF}[health]{/color}, здоровье врага: {color=#FF00FF}[current_enemy['health']]{/color}."
        jump choice_58_loop

    elif enemy_attack < player_attack:
        $ current_enemy["health"] -= 2
        if current_enemy["health"] > 0:
            f "Твой удар ([player_attack]) превосходит защиту [current_enemy['name']] ([enemy_attack])! Ты наносишь 2 урона. У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твое здоровье: {color=#FF00FF}[health]{/color}."
        else:
            f "Твой мощный удар ([player_attack]) сокрушает [current_enemy['name']] ([enemy_attack])! Враг повержен! Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}."

        menu:
            "Использовать удачу, чтобы нанести дополнительный урон":
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ current_enemy["health"] -= 2
                    $ luck -= 1
                    if current_enemy["health"] > 0:
                        f "Удача на твоей стороне! Ты наносишь [current_enemy['name']] дополнительный урон (2). У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                    else:
                        f "Удача помогает тебе! Мощный дополнительный удар (2 урона) добивает [current_enemy['name']]! Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ current_enemy["health"] += 1
                    $ luck -= 1
                    f "Удача отвернулась! [current_enemy['name']] восстанавливает 1 здоровье (теперь {color=#FF00FF}[current_enemy['health']]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
            "Не использовать удачу, чтобы нанести дополнительный урон":
                pass
        jump choice_58_loop

    else:
        $ health -= 2
        if health > 0:
            f "[current_enemy['name']] наносит тебе удар ([enemy_attack])! Твоя защита ([player_attack]) не справляется. Ты теряешь 2 здоровья, осталось {color=#FF00FF}[health]{/color}."
        else:
            f "[current_enemy['name']] наносит сокрушительный удар ([enemy_attack]) против твоей защиты ([player_attack])! Ты теряешь последние силы и падаешь."
            jump game_over

        menu:
            "Использовать удачу, чтобы смягчить урон":
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ health += 1
                    $ luck -= 1
                    f "Удача спасает тебя! Ты восстанавливаешь 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ health -= 1
                    $ luck -= 1
                    if health > 0:
                        f "Удача подвела! Ты теряешь дополнительное 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                    else:
                        f "Удача подвела, и ты теряешь последнее здоровье! [current_enemy['name']] добивает тебя."
                        jump game_over
            "Не использовать удачу, чтобы смягчить урон":
                pass
        jump choice_58_loop

label choice_256:
    scene 138-1
    e "Вы останавливаетесь над телом в канаве."
    e "Никто на улице, кажется, не обращает на вас внимания, и вы наклоняетесь ближе."
    e "Вы берете его за плечо и трясете. Нет реакции."
    e "Хватаете за руку и переворачиваете лицом вверх, а затем в испуге отпрыгиваете назад."
    scene 256-2 with dissolve
    pause 0.5
    e "Пред вами лежит полуразложившийся труп! Его гниющая голова наполовину череп наполовину гниющая плоть, и вы с трудом подавляете крик отвращения и ужаса."
    e "Но когда вы отворачиваетесь от него, злобная улыбка искажает оставшуюся часть губ трупа, и он вскакивает на ноги. Тварь прыгает на вас, и вы едва успеваете выхватить оружие."
    $ current_enemy = {"name": "复活的尸体", "mastery": 6, "health": 6} # Оживший Труп
    jump choice_256_fight

label choice_256_fight:
    if health <= 0:
        f "Твои силы иссякли в бою с [current_enemy['name']]! Ты падаешь, побежденный его мертвой хваткой."
        jump game_over

    if current_enemy["health"] <= 0:
        f "Оживший Труп повержен! Ты стоишь над его неподвижным телом, тяжело дыша. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
        jump choice_11

    $ enemy_attack = renpy.random.randint(1, 12) + current_enemy["mastery"]
    $ player_attack = renpy.random.randint(1, 12) + mastery

    if enemy_attack == player_attack:
        f "Ты ([player_attack]) и [current_enemy['name']] ([enemy_attack]) атакуете одновременно, но оба уклоняетесь! Никто не ранен. Твое здоровье: {color=#FF00FF}[health]{/color}, здоровье врага: {color=#FF00FF}[current_enemy['health']]{/color}."
        jump choice_256_fight

    elif enemy_attack < player_attack:
        $ current_enemy["health"] -= 2
        if current_enemy["health"] > 0:
            f "Твой удар ([player_attack]) пробивает защиту [current_enemy['name']] ([enemy_attack])! Ты наносишь 2 урона. У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твое здоровье: {color=#FF00FF}[health]{/color}."
        else:
            f "Твой мощный удар ([player_attack]) разрывает [current_enemy['name']] ([enemy_attack]) на части! Враг повержен! Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}."

        menu:
            "Использовать удачу, чтобы нанести дополнительный урон":
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ current_enemy["health"] -= 2
                    $ luck -= 1
                    if current_enemy["health"] > 0:
                        f "Удача на твоей стороне! Ты наносишь [current_enemy['name']] дополнительный урон (2). У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                    else:
                        f "Удача помогает тебе! Мощный дополнительный удар (2 урона) окончательно уничтожает [current_enemy['name']]! Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ current_enemy["health"] += 1
                    $ luck -= 1
                    f "Удача отвернулась! [current_enemy['name']] восстанавливает 1 здоровье (теперь {color=#FF00FF}[current_enemy['health']]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
            "Не использовать удачу, чтобы нанести дополнительный урон":
                pass
        jump choice_256_fight

    else:
        $ health -= 2
        if health > 0:
            f "[current_enemy['name']] наносит тебе удар ([enemy_attack])! Твоя защита ([player_attack]) не справляется. Ты теряешь 2 здоровья, осталось {color=#FF00FF}[health]{/color}."
        else:
            f "[current_enemy['name']] наносит сокрушительный удар ([enemy_attack]) против твоей защиты ([player_attack])! Ты теряешь последние силы и падаешь."
            jump game_over

        menu:
            "Использовать удачу, чтобы смягчить урон":
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ health += 1
                    $ luck -= 1
                    f "Удача спасает тебя! Ты восстанавливаешь 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ health -= 1
                    $ luck -= 1
                    if health > 0:
                        f "Удача подвела! Ты теряешь дополнительное 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                    else:
                        f "Удача подвела, и ты теряешь последнее здоровье! [current_enemy['name']] добивает тебя."
                        jump game_over
            "Не использовать удачу, чтобы смягчить урон":
                pass
        jump choice_256_fight

label choice_239:
    scene 239-1 with dissolve
    pause 0.5
    e "Миновав этот небольшой район, вы подходите к маленькому полю, обнесенному грубым деревянным забором."
    e "Полдюжины свиней роются в грязи в стороне от группы существ, сгрудившихся вокруг костра."
    menu:
        "Перелезть через ограду и посмотрите, что здесь происходит":
            jump choice_307
        "Пойти дальше":
            jump choice_62

label choice_66:
    scene 66-1 with dissolve
    pause 0.5
    e "Здесь никого, но есть дверь, ведущая в задние помещения."
    menu:
        "Позвать мастера":
            jump choice_280
        "Быстренько пошарить по комнате пока никого нет":
            jump choice_215

label choice_171:
    scene 171-1 with dissolve
    pause 0.5
    e "Вы толкаете дверь, она не заперта."
    menu:
        "Постучать и попросить разрешения войти":
            jump choice_90
        "Распахнуть дверь и ворваться внутрь, чтобы застать врасплох тех, кто находится внутри":
            jump choice_75

label choice_294:
    scene 294-1 with dissolve
    pause 0.5
    play sound "audio/294-1.mp3"
    e "Вы идете дальше по дороге и слышите впереди многоголосый шум, как от большой толпы."
    e "Возможно, вы идёте к рынку или какой-то ярмарке."
    menu:
        "Продолжить путь прямо":
            jump choice_244
        "Повернуть налево":
            jump choice_328

label choice_320:
    scene 213-2
    e "Вы наклоняетесь ближе к пруду и прикладываете ухо к поверхности воды."
    e "Рыбка вертится рядом с вами, плеща водой на вашу щеку."
    e "Если бы рыбы могли смеяться, вы бы могли поклясться, что она хихикает!"
    e "Еще одна струйка пузырьков вырывается у нее изо рта, но вы слышите только бульканье."
    e "Вам удалось разобрать только что-то похожее на «Бурерркы». Но что это может значить? Рыбка снова прячется за камень."
    menu:
        "Продолжить свой путь":
            jump choice_28
        "Попытаться достать монету из пруда":
            jump choice_85

label choice_85:
    scene 213-2
    $ twodice = renpy.random.randint(1, 12)
    e "Вам пришлось испытать удачу, чтобы попытаться вытащить монетку из пруда"
    s "Уровень вашей удачи - {color=#FF00FF}[luck]{/color}, требуемый уровень удачи - {color=#FF00FF}[twodice]{/color}"
    if twodice <= luck:
        e "Когда вы суете руку в воду за монетой, возмущенная вашим поступком серебристая рыбка больно кусает вас, теряете 1 очко Здоровья."
        e "Вам повезло и удалось поймать монетку!"
        $ health -= 1
        $ gold += 1
        s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
        if health <= 0:
            jump game_over
        s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
        $ luck -= 1
    else:
        e "Когда вы суете руку в воду за монетой, возмущенная вашим поступком серебристая рыбка больно кусает вас, теряете 1 очко Здоровья."
        e "Вам НЕ повезло и удалось поймать монетку!"
        $ health -= 1
        s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
        if health <= 0:
            jump game_over
        $ luck -= 1
    s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
    jump choice_28

label choice_28:
    scene 28-1 with dissolve
    pause 0.5
    e "Вы подходите к развилке, откуда можно идти прямо или повернуть налево. Рядом с развилкой стоит хижина, а около хижины привязан жеребец."
    menu:
        "Пойти прямо":
            jump choice_233
        "Повернуть налево":
            jump choice_300
        "Подойти к лошади":
            jump choice_183

label choice_251:
    scene 251-1 with dissolve
    pause 0.5
    e "В карманах убитых вы находите 5 золотых."
    $ gold += 5
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    play sound "audio/294-1.mp3"
    e "Шум снаружи пугает вас, и вы поворачиваетесь к двери."
    menu:
        "Выйти наружу":
            jump choice_213
        "Продолжить обыск комнаты":
            jump choice_305

label choice_11:
    scene 11-1 with dissolve
    pause 0.5

    e "После того как живой труп упал поверженный, части его тела разлетелись в разные стороны и пытаются на вас напасть!"
    e "Вам ничего не остается, кроме как продолжить битву с шестью противниками разом: головой, туловищем двумя ногами и двумя руками."
    $ enemies = [
        {"name": "头部", "mastery": 3, "health": 1}, # Голова
        {"name": "躯干", "mastery": 2, "health": 1}, # Туловище
        {"name": "左手", "mastery": 3, "health": 1}, # Левая Рука
        {"name": "右手", "mastery": 3, "health": 1}, # Правая Рука
        {"name": "左腿", "mastery": 3, "health": 1}, # Левая Нога
        {"name": "右腿", "mastery": 3, "health": 1}, # Правая Нога
    ]
    jump choice_11_fight

label choice_11_fight:
    if health <= 0:
        f "Твои силы иссякли в бою с [current_enemy['name']]! Ты падаешь, побежденный их неестественной живучестью."
        jump game_over

    $ living_enemies = [e for e in enemies if e["health"] > 0]
    if not living_enemies:
        f "Все части тела повержены! Ты стоишь над их неподвижными останками, тяжело дыша. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
        jump choice_276

    $ current_enemy = renpy.random.choice(living_enemies)

    $ enemy_attack = renpy.random.randint(1, 12) + current_enemy["mastery"]
    $ player_attack = renpy.random.randint(1, 12) + mastery

    if enemy_attack == player_attack:
        f "Ты ([player_attack]) и [current_enemy['name']] ([enemy_attack]) атакуете одновременно, но оба уклоняетесь! Никто не ранен. Твое здоровье: {color=#FF00FF}[health]{/color}, здоровье врага: {color=#FF00FF}[current_enemy['health']]{/color}."
        jump choice_11_fight

    elif enemy_attack < player_attack:
        $ current_enemy["health"] -= 2
        if current_enemy["health"] > 0:
            f "Твой удар ([player_attack]) пробивает защиту [current_enemy['name']] ([enemy_attack])! Ты наносишь 2 урона. У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твое здоровье: {color=#FF00FF}[health]{/color}."
        else:
            f "Твой мощный удар ([player_attack]) разрушает [current_enemy['name']] ([enemy_attack])! Эта часть тела повержена! Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}."

        menu:
            "Использовать удачу, чтобы нанести дополнительный урон":
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ current_enemy["health"] -= 2
                    $ luck -= 1
                    if current_enemy["health"] > 0:
                        f "Удача на твоей стороне! Ты наносишь [current_enemy['name']] дополнительный урон (2). У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                    else:
                        f "Удача помогает тебе! Мощный дополнительный удар (2 урона) окончательно уничтожает [current_enemy['name']]! Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ current_enemy["health"] += 1
                    $ luck -= 1
                    f "Удача отвернулась! [current_enemy['name']] восстанавливает 1 здоровье (теперь {color=#FF00FF}[current_enemy['health']]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
            "Не использовать удачу, чтобы нанести дополнительный урон":
                pass
        jump choice_11_fight

    else:
        $ health -= 2
        if health > 0:
            f "[current_enemy['name']] наносит тебе удар ([enemy_attack])! Твоя защита ([player_attack]) не справляется. Ты теряешь 2 здоровья, осталось {color=#FF00FF}[health]{/color}."
        else:
            f "[current_enemy['name']] наносит сокрушительный удар ([enemy_attack]) против твоей защиты ([player_attack])! Ты теряешь последние силы и падаешь."
            jump game_over

        menu:
            "Использовать удачу, чтобы смягчить урон":
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ health += 1
                    $ luck -= 1
                    f "Удача спасает тебя! Ты восстанавливаешь 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ health -= 1
                    $ luck -= 1
                    if health > 0:
                        f "Удача подвела! Ты теряешь дополнительное 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                    else:
                        f "Удача подвела, и ты теряешь последнее здоровье! [current_enemy['name']] добивает тебя."
                        jump game_over
            "Не использовать удачу, чтобы смягчить урон":
                pass
        jump choice_11_fight

label choice_307:
    scene 307-1 with dissolve
    pause 0.5
    e "Осмотритесь и примите решение что делать длаьше"
    menu:
        "Подружиться с этими бродягами и, когда свинья будет готова, присоединиться к их трапезе":
            jump choice_245
        "Уходить":
            jump choice_62

label choice_62:
    scene 62-1 with dissolve
    pause 0.5
    play sound "audio/294-1.mp3"
    e "Со стороны ярмарки слышится шум"
    menu:
        "Пойти налево":
            jump choice_32
        "Пойти направо":
            jump choice_322
        "Пойти прямо":
            jump choice_57

label choice_280:
    scene 66-1
    e "Вы ждете и, наконец, слышите шарканье за дальней дверью."
    play sound "audio/280-1.mp3"
    pause 4
    show Pork
    pause 0.5
    p "Цепь брать будешь?"
    menu:
        "Выбрать несколько приглянувшихся вам цепей и спросить, сколько он хочет за одну из них.":
            jump choice_332
        "Спросить, может ли он помочь вам в поисках строк заклинания, открывающего Северные Врата.":
            jump choice_161

label choice_215:
    scene 66-1
    e "Для того, чтобы осмотреть комнату и не задеть гремящие цепи потребуется удача!"
    $ twodice = renpy.random.randint(1, 12)
    s "Уровень вашей удачи - {color=#FF00FF}[luck]{/color}, требуемый уровень удачи - {color=#FF00FF}[twodice]{/color}"
    if twodice <= luck:
        $ luck -= 1
        s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
        jump choice_181
    else:
        $ luck -= 1
        s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
        jump choice_19

label choice_90:
    scene 171-1
    play sound "audio/1-1.mp3"
    pause 1
    i "Можно войти?"
    h "Входите, мой друг, но осторожней открывайте дверь"
    scene 90-1 with dissolve
    play sound "audio/90-1.mp3"
    pause 2
    e "Вы открываете дверь и быстро делаете шаг назад"
    e "Когда на пол с притолоки падает пузырек с какой-то жидкостью"
    e "Перешагнув через него, вы входите в хижину"
    jump choice_43

label choice_75:
    scene 90-1
    show Bubble
    play sound "audio/90-1.mp3"
    pause 2
    e "Вы распахиваете дверь и врываетесь внутрь, держа оружие наготове."
    e "Но внезапно маленький пузырек с жидкостью, стоявший на верхушке двери"
    e "Опрокидывается вам на голову, расплескивая свое содержимое."
    e "Вы протираете голову, но маслянистая жидкость уже пропитала ваши волосы."
    e "Когда вы смотрите на свою руку, то видите, что она вся покрыта волосами."
    e "Вы проводите еще раз, и большой пучок волос падает на пол."
    h "Стучаться надо, нарушитель!"
    h "Возможно, облысение научит тебя хорошим манерам!"
    e "Действительно через несколько секунд ваша голова уже гладкая как бильярдный шар!"
    e "Вам остается только утешать себя тем, что эффект от зелья облысения временный."
    e "После того как вы вымоете голову, волосы вырастут снова – но на это уйдет еще какое-то время"
    jump choice_43

label choice_244:
    if festival == 1:
        jump choice_263
    else:
        $ festival = 1
    scene 244-1 with dissolve
    pause 0.5
    e "Вы решаете задержаться здесь и осмотреться."
    e "Вы смешиваетесь с толпой и проходите мимо, разглядывая местные аттракционы."
    e "В одном месте группа музыкантов играет веселую джигу для труппы танцоров."
    e "В другом гном держит на поводке дрессированного танцующего медведя."
    e "Рядом установлен ринг, на котором стоит какой-то тип и зазывает претендентов для схватки с местным чемпионом."
    menu:
        "Понаблюдать за танцорами":
            jump choice_261
        "Взглянуть на танцующего медведя":
            jump choice_269
        "Посмотреть на схватку с участием местного чемпиона":
            jump choice_33
        "Покинуть фестиваль":
            jump choice_263

label choice_328:
    scene 328-1 with dissolve
    pause 0.5
    e "Осмотритесь и решите куда идти дальше"
    menu:
        "Пойти прямо к небольшой группе домов":
            jump choice_32
        "Повернуть направо":
            jump choice_57

label choice_233:
    scene 233-1 with dissolve
    pause 0.5
    e "Дорога просто кишит гномами и другими маленькими созданиями."
    e "По их презрительным взглядам, которыми они награждают вас, проходя мимо, вы делаете вывод, что они не жалуют здесь посторонних, особенно людей."
    e "Чуть дальше по улице вы замечаете небольшую толпу, собравшуюся вокруг драки между двумя существами."
    menu:
        "Зайти в небольшой магазин в центре этого района":
            jump choice_149
        "Продолжить путь":
            jump choice_153
        "Подойти ближе к драке":
            jump choice_98

label choice_300:
    scene 300-1 with dissolve
    pause 0.5
    e "Вы идете по постепенно сужающейся дороге."
    e "Группа юных орклингов несутся к вам навстречу, толкая и пихая друг друга."
    e "Увидев вас, они прибавляют ходу и окружают вас, а затем десяток тоненьких голосов начинают канючить:"
    ork "Эй! Один золотой, всего один золотой!"
    ork "Неужели жалко всего один золотой?"
    e "Их руки тянутся к вашим карманам, и они не прекращают вымаливать подачку."
    menu:
        "Бросить им золотой":
            jump choice_91
        "Пройти мимо":
            jump choice_329

label choice_183:
    scene 183-1 with dissolve
    play sound "audio/183-1.mp3"
    pause 1.5
    e "Лошадь нервно фыркает, когда вы подходите к ней, и неловко переступает ногами."
    menu:
        "Попытаться поговорить с лошадью":
            jump choice_128
        "Залезть на спину лошади":
            jump choice_49
        "Уйти и продолжить свой путь":
            jump choice_237

label choice_305:
    scene 251-1
    e "Под матрасом в углу комнаты вы находите маску из черного дерева, вырезанную наподобие лика одного из богов черных эльфов."
    e "Вы берете ее с собой"
    e "Больше ничего интересного в комнате нет, и вы покидаете хижину"
    $ blackmask = 1
    jump choice_213

label choice_276:
    scene 138-1 with dissolve
    pause 0.5
    e "Вы отступаете назад, а изрубленные фрагменты мертвого тела бесцельно ползают вокруг вас."
    e "Наконец они снова соединяются в одно целое, и на земле остается лежать труп"
    e "Который выглядит так, как будто по нему на колесницах ездили."
    e "Из ближайшей хижины появляется голова ее обитателя и вам жестом предлагают зайти."
    e "Несколько гномов наблюдали за вашей битвой с нежитью"
    e "И они благодарят вас за то, что вы избавили их самих и их соседей от ужасного существа."
    e "Теперь дети в этом районе смогут снова в безопасности играть на улице."
    e "Они дарят вам 5 золотых и спрашивают, чем еще могут помочь."
    $ gold += 5
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    e "Вы вкратце объясняете суть вашей миссии."
    e "Они согласны с тем, что вам надо найти четыре строки заклинания открывающего ворота на северной стороне города"
    e "И предлагают вам обратиться за помощью к жрецу, живущему здесь неподалеку, если идти прямо к центру города."
    e "Они также предлагают вам одну из некоторых вещей, которые можно использовать для накладывания заклинаний."
    e "Какую вы выберете?"
    menu:
        "Взять у них лечебное зелье":
            $ healingPotion += 1
        "Взять у них мешочек с тремя камнями голышами":
            $ bagWithThreeStones += 1
        "Взять у них пузырек с 1 порцией морского песка (редкий товар так далеко от моря)":
            $ servingOfSeaSand +=1
    e "Вы берете выбранный вами предмет и уходите"
    jump choice_239

label choice_245:
    scene 307-1
    e "Эти бродяги представляют собой сборную солянку из разных существ и им все равно, кто вы."
    e "Вы рассказываете им несколько историй и шуток, и они охотно делятся с вами своей добычей."
    e "Вам дают большой жирный кусок свиной ноги, но вы слишком поспешно проглотили первый кусок"
    e "И слишком поздно поняли, что он еще не остыл."
    e "Вы сгибаетесь пополам, чувствуя сильное жжение в желудке, теряете 1 очко Здоровья."
    $ health -= 1
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    if health <= 0:
        jump game_over
    e "Вы больше не сможете есть сегодня до конца дня."
    e "Вы прощаетесь с бродягами и уходите/"
    jump choice_62

label choice_32:
    scene 328-1
    e "Вы идете по дороге мимо хижин до новой развилки, где поворачиваете направо"
    jump choice_297

label choice_322:
    scene 239-1
    e "Вы следуете по дороге до очередной развилки. Слева вы слышите шум толпы и поворачиваете в эту сторону"
    play sound "audio/294-1.mp3"
    pause 4
    jump choice_244

label choice_57:
    scene 57-1 with dissolve
    pause 0.5
    e "Вы приближаетесь к центру города, застройка здесь более плотная."
    e "Пока вы, идя по одной стороне дороги, наблюдали за другой"
    e "Вас хватают сзади и затаскивают в дом."
    scene 57-2 with dissolve
    pause 0.5
    show BlackMan
    e "Вы поворачиваетесь лицом к атакующему, это заросший щетиной темнокожий мужчина."
    e "Он, очевидно, удивлен вашей силой и отпускает вас, подняв руки, чтобы показать, что он не собирается причинять вам никакого вреда."
    bm "Мой друг, я весьма сожалею, что испугал вас"
    bm "Но я одинокий человек, вынужденный обитать в этом злом городе."
    bm "Вы такой же человек, как я, и я не видел вас в этих местах раньше."
    bm "Молю, присядьте и поговорите со мной некоторое время."
    bm "Я не причиню вам вреда"
    e "Кажется, он достаточно дружелюбен, но вам не нравится зловещий блеск его глаз."
    e "Вы оглядываете его дом"
    hide BlackMan
    pause 2
    show BlackMan
    menu:
        "Остаться и поговорите с ним":
            jump choice_186
        "Покинуть дом":
            jump choice_173

label choice_332:
    scene 66-1
    show Pork
    e "Он оценивающе смотрит на вас, пытаясь решить, сколько с вас можно содрать денег."
    if mastery >= 8:
        e "Вы выглядите как довольно могучий и, следовательно, богатый путешественник"
        p "Я хочу за цепь 5 золотых!"
        $ chainPrice = 5
    else:
        e "Он видит в вас обычного посетителя"
        p "Я хочу за цепь 2 золотых!"
        $ chainPrice = 2
    menu:
        "Купить цепь и заплатить ему":
            $ gold = gold - chainPrice
            s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
            jump choice_203
        "Уйти":
            jump choice_9
        "Атаковать его, чтобы проучить этого жлоба, а заодно уж и обворовать его":
            jump choice_119

label choice_161:
    scene 66-1
    show Pork
    p "Я ничего не знаю о заклинании! Ты мешаешь мне работать!"
    menu:
        "Покинуть мастерскую":
            jump choice_9
        "Напасть на этого невежу":
            jump choice_119

label choice_181:
    scene 181-1 with dissolve
    pause 0.5
    e "В маленькой шкатулке на столе у одной из стен вы находите 3 золотых."
    $ gold += 3
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    menu:
        "Покинуть комнату":
            jump choice_9
        "Продолжить обыск":
            e "Вам придется испытать удачу"
            $ twodice = renpy.random.randint(1, 12)
            s "Уровень вашей удачи - {color=#FF00FF}[luck]{/color}, требуемый уровень удачи - {color=#FF00FF}[twodice]{/color}"
            if twodice <= luck:
                s "Вам повезло!"
                $ luck -= 1
                s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
                jump choice_134
            else:
                s "Вам не повезло!"
                $ luck -= 1
                s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
                jump choice_19

label choice_19:
    scene 66-1
    e "Коснувшись цепи, вы устроили настоящий грохот, и хозяин мастерской выбегает на шум из задней комнаты."
    play sound "audio/19-1.mp3"
    pause 4
    show Pork
    e "Он страшно возмущен вашим вторжением"
    jump choice_119

label choice_43:
    scene 43-1 with dissolve
    pause 0.5
    e "Да ведь это же Пожиратель - разумный паразит, который пожирает мозг своего носителя"
    e "чтобы потом управлять его телом!"
    e "Кроме этого, странного существа ваше внимание привлекает коробка под одним из столов"
    e "Из которой торчат свиток и блестящее зеркало."
    e "Хозяин дома ждет вашей реакции."
    menu:
        "Попробовать поговорить с ним":
            jump choice_145
        "Обнажить оружие и атаковать его":
            jump choice_243
        "Уйти и продолжить свой путь":
            jump choice_294

label choice_263:
    scene 263-1 with dissolve
    pause 0.5
    e "Вы покидаете фестиваль, но, когда проходите мимо последней палатки"
    e "Замечаете любопытную вывеску: «ШКАФ ФОРТУНЫ – ИСПЫТАЙ УДАЧУ – ПРИЗЫ ДЛЯ ВСЕХ – ТОЛЬКО 2 ЗОЛОТЫХ»"
    menu:
        "Зайти и взглянуть, что это такое":
            jump choice_240
        "Продолжить путь":
            jump choice_160

label choice_261:
    scene 261-1 with dissolve
    pause 0.5
    play sound "audio/261-1.mp3"
    pause 3
    e "Вы присоединяетесь к толпе и наблюдаете, как танцоры отплясывают и крутятся под мелодию музыкантов."
    e "Они наращивают темп, и толпа присоединяется к танцу."
    e "Восхищенный мастерством танцоров вы тоже увлекаетесь и начинаете приплясывать и топать ногами."
    e "Восстановите 1 очко Здоровья благодаря полученному удовольствию."
    $ health += 1
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    e "Танцоры кружат вдоль зрителей и хватают то одного, а то и двух из них"
    e "Втягивая их в танец, к большему веселью толпы"
    e "Один из танцоров хватает вас и втягивает вас в круг."
    menu:
        "Присоединиться танцу":
            jump choice_17
        "Оторваться от партнера, не желая выставлять себя на посмешище":
            jump choice_40

label choice_269:
    scene 269-1 with dissolve
    pause 0.5
    e "Вокруг гнома и его медведя собралась толпа."
    e "В одной руке он держит поводок, прикрепленный к кольцу в носу у медведя."
    e "Дергая за него, он заставляет медведя спотыкаться в каком-то подобии танца."
    e "В другой руке он держит у рта маленькую дудочку и играет на ней живую мелодию."
    e "Медведь отнюдь не грациозный танцор, и толпа громко смеется над его неуклюжими действиями."
    e "Вы смотрите на это в течение нескольких минут."
    e "Внезапно раздается крик."
    rm "Мое золото пропало!"
    rm "Карманник!"
    rm "Осторожно, карманник!"
    rm "Держи вора!"
    e "Вы и остальная часть толпы поворачиваетесь на голос."
    e "Вы видите, как маленькое существо вылетает из толпы и бежит вниз по дороге в одну из палаток."
    e "Есть небольшая надежда на то, что его поймают."
    e "Вы вовремя оборачиваетесь к гному и его медведю, чтобы увидеть, как они исчезают в воздухе!"
    e "Это шоу было не чем иным, как иллюзией, созданной, чтобы отвлечь аудиторию, пока карманник крадет золото."
    e "Другие существа в толпе проверяют свое золото, некоторые из них тоже стали жертвами карманника."
    e "Настало время испытать вышу удачу!"
    $ twodice = renpy.random.randint(1, 12)
    s "Уровень вашей удачи - {color=#FF00FF}[luck]{/color}, требуемый уровень удачи - {color=#FF00FF}[twodice]{/color}"
    if twodice <= luck:
        s "Вам повезло!"
        $ luck -= 1
        s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
        jump choice_63
    else:
        s "Вам не повезло!"
        $ luck -= 1
        s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
        jump choice_177

label choice_33:
    scene 33-1 with dissolve
    pause 0.5
    pr "Очень хорошо, народ, у нас есть новый соискатель."
    pr "В белом углу ринга, давайте поприветствуем его, Анвар Варвар!"
    play sound "audio/33-1.mp3"
    pause 3
    e "Зрители аплодируют."
    pr "И в черном углу ринга чемпион Кхара по мордобою"
    pr "Могучий огр, так же известный как Череподробитель, Кагу из Дадду-Лей!"
    play sound "audio/33-1.mp3"
    pause 3
    e "Зрители опять же аплодируют"
    e "Похоже, предстоит серьезная драка."
    menu:
        "Поставить на результат боя" if gold > 0:
            jump choice_190
        "Просто понаблюдать":
            jump choice_234

label choice_149:
    scene 149-1 with dissolve
    pause 0.5
    s "Количество вашего золота - {color=#FF00FF}[gold]{/color}"
    if gold >= 2:
        e "Вы можете себе позволить купить некоторые вещи"
        menu:
            "Бутылка с надписью: «Таинственное зелье» (2 золотых)" if gold >= 2:
                $ gold -= 2
                $ bottleWithTheInscription += 1
                s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
                jump choice_199
            "Соты с пчелиным воском (2 золотых)" if gold >= 2:
                $ gold -= 2
                $ honeycombWithBeeswax += 1
                s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
                jump choice_199
            "Еда - одна порция (3 золотых)" if gold >= 3:
                $ gold -= 3
                $ meal += 1
                s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
                s "Теперь количество вашей еды - {color=#FF00FF}[meal]{/color}"
                jump choice_199
            "Маленький флакон с пылью (3 золотых)" if gold >= 3:
                $ gold -= 3
                $ bottleDust += 1
                s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
                jump choice_199
            "Набор перчаток (5 золотых)" if gold >= 5 and perch == 0:
                $ gold -= 5
                $ perch = 1
                s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
                jump choice_199
            "Ничего не покупать":
                jump choice_170
    else:
        e "Вы не можете себе ничего купить"
        jump choice_170

label choice_153:
    scene 153-1 with dissolve
    pause 0.5
    e "Вы покидаете поселение гномов и продолжаете идти вперед."
    e "Медальон на шее у статуи выглядит слишком ценным артефактом, чтобы его можно было повесить на простую статую и оставить без присмотра"
    e "Возможно, он очень ценный, возможно, даже волшебный"
    menu:
        "Присмотреться к статуе":
            jump choice_8
        "Войти в хижину за ее спиной":
            jump choice_27
        "Проигнорировать это искушение и продолжите путь":
            jump choice_137

label choice_98:
    scene 98-1 with dissolve
    pause 0.5
    e "Сквозь небольшую толпу вы можете увидеть двух крошечных существ, сражающихся друг с другом на земле."
    play sound "audio/33-1.mp3"
    pause 3
    e "Борьба идет между спрайтом и пикси."
    e "Половина зрителей подбадривают пикси, а остальные встали на сторону спрайта."
    e "Никто не пытается прекратить эту драку."
    menu:
        "Попытаться разнять дерущихся":
            jump choice_302
        "Помочь одному из двух существ":
            jump choice_321
        "Проигнорировать все это и продолжить свой путь":
            jump choice_153

label choice_91:
    scene 300-1
    e "Бросаете им монету, и они начинают ссориться из-за нее."
    $ gold -= 1
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    e "Пока суть, да дело, вы можете задать им вопрос"
    menu:
        "Откуда они пришли?":
            jump choice_180
        "Как добраться до центра города?":
            jump choice_289
        "Слышали ли они о ком-то по имени Вик?":
            jump choice_246

label choice_329:
    scene 329-1 with dissolve
    pause 0.5
    e "Когда эти юные бандиты приближаются к вам, вы чувствуете, как их маленькие руки рвут ваш рюкзак."
    e "Они пытаются проникнуть внутрь, чтобы спереть что-нибудь!"
    e "Настало время испытать вышу удачу!"
    $ twodice = renpy.random.randint(1, 12)
    s "Уровень вашей удачи - {color=#FF00FF}[luck]{/color}, требуемый уровень удачи - {color=#FF00FF}[twodice]{/color}"
    if twodice <= luck:
        s "Вам повезло!"
        $ luck -= 1
        s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
        jump choice_316
    else:
        s "Вам не повезло!"
        $ luck -= 1
        s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
        jump choice_262

label choice_128:
    scene 183-1
    e "Животное странно смотрит на вас."
    e "Вы произносите несколько ласковых слов, и лошадь немного успокаивается, но не дает никаких признаков ответа."
    e "В конце концов, вы прекращаете это одностороннее общение."
    e "Лошадь успокоилась"
    menu:
        "Запрыгнуть жеребцу на спину":
            jump choice_49
        "Пойти своим путем":
            jump choice_237

label choice_49:
    scene 49-1 with dissolve
    pause 0.5
    e "Вы отвязываете поводья и запрыгиваете на спину коню. Он громко ржет и поднимается на дыбы."
    play sound "audio/49-1.mp3"
    pause 4
    e "Прежде чем успеваете среагировать, он молнией скачет по дороге в ту сторону откуда вы пришли."
    menu:
        "Крепко держаться в седле и смотреть, куда он вас привезет":
            jump choice_268
        "Проверить Удачу в попытке остановить его и сойти":
            jump choice_220

label choice_237:
    scene 237-1 with dissolve
    pause 0.5
    e "Примите решение куда пойдете дальше"
    menu:
        "Повернуть налево":
            jump choice_300
        "Продолжить идти прямо":
            jump choice_233

label choice_297:
    scene 297-1 with dissolve
    pause 0.5
    e "Вы входите в центр города, дома и строения здесь заметно плотнее, народу на улицах тоже больше."
    e "День подходит к концу, и вы начинаете присматривать себе место для ночлега."
    show YoungMan
    e "Некоторое время вы идете рядом с каким-то юношей и затем завязываете с ним беседу."
    ym "Меня зовут Слангг"
    ym "Я живу за Северными Вратами Кхара"
    ym "Моя мать - скунсомедведица"
    ym "Я сам ничего не ем, кроме крысиных мозгов"
    ym "Я - личный слуга Первого Архонта Кхара"
    e "Вы скоро понимаете, что он записной враль, и все, что он говорит, брехня."
    scene 297-2 with dissolve
    pause 0.5
    show YoungMan
    e "Вы подходите к развилке, где вам надо расстаться."
    e "Напоследок, вы можете попросить у него совета."
    menu:
        "Спросить, как быстрее добраться до ближайшей гостиницы":
            jump choice_216
        "Спросить не знает ли он что-нибудь о хранителях заклинания, открывающего Северные Врата":
            jump choice_51

label choice_186:
    scene 57-2
    show BlackMan
    bm "Каков мир за пределами Кхара?"
    i "Он огромен и разнообразен"
    bm "Огромен... Разнообразен..."
    i "А как вам нравится город Кхар?"
    bm "Ах, это коварное место"
    bm "Я могу рассказать вам много об опасностях этого города – но сначала давайте выпьем эля а?"
    menu:
        "Выпить с ним":
            jump choice_34
        "Покинуть его дом":
            jump choice_173

label choice_173:
    scene 57-2
    show BlackMan
    e "Человек внезапно становиться агрессивным."
    bm "Неблагодарный путешественник!"
    bm "Ты не можешь отказаться от моего гостеприимства."
    bm "Присоединяйся ко мне, и выпьем по кружке эля."
    bm "Пока не сделаешь этого, ты не уйдешь из моего дома!"
    menu:
        "Выпить с ним":
            jump choice_34
        "Уйти отсюда во что бы то ни стало":
            jump choice_223

label choice_203:
    scene 203-1 with dissolve
    pause 0.5
    $ magicalSelfLockingChain += 1
    e "Это настоящая находка – волшебная самозамыкающаяся цепь, которую можно использовать в бою."
    e "Всякий раз, когда вы уменьшаете Выносливость противника до 3 очков или менее, можете метнуть эту цепь во врага, и она обовьется вокруг ослабленной жертвы и замкнется, обездвижив его, что позволит вам подойти к нему и прикончить, не опасаясь ответного удара."
    e "К несчастью, вы не знаете, как разомкнуть цепь, так что сможете использовать ее только один раз."
    jump choice_9

label choice_9:
    scene 292-1 with dissolve
    pause 0.5
    e "Напротив мастерской по изготовлению цепей находится другая хижина, и из нее доносится аппетитный запах."
    menu:
        "Подойти к ней и заглянуть внутрь":
            jump choice_171
        "Продолжить путь по дороге":
            jump choice_294

label choice_119:
    scene 66-1
    show Pork
    e "Свинн срывает длинную цепь со стены и раскручивает ее над головой, чтобы наносить вам удары."
    $ current_enemy = {"name": "斯温", "mastery": 8, "health": 7} # Свинн
    jump choice_119_fight

label choice_119_fight:
    if health <= 0:
        f "Твои силы иссякли в бою с [current_enemy['name']]! Ты падаешь, побежденный его яростными ударами цепью."
        jump game_over

    if current_enemy["health"] <= 0:
        f "Свинн повержен! Ты стоишь над его телом, тяжело дыша. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
        jump choice_195

    $ enemy_attack = renpy.random.randint(1, 12) + current_enemy["mastery"]
    $ player_attack = renpy.random.randint(1, 12) + mastery

    if enemy_attack == player_attack:
        f "Ты ([player_attack]) и [current_enemy['name']] ([enemy_attack]) атакуете одновременно, но оба уклоняетесь! Никто не ранен. Твое здоровье: {color=#FF00FF}[health]{/color}, здоровье врага: {color=#FF00FF}[current_enemy['health']]{/color}."
        jump choice_119_fight

    elif enemy_attack < player_attack:
        $ current_enemy["health"] -= 2
        if current_enemy["health"] > 0:
            f "Твой удар ([player_attack]) пробивает защиту [current_enemy['name']] ([enemy_attack])! Ты наносишь 2 урона. У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твое здоровье: {color=#FF00FF}[health]{/color}."
            if current_enemy["health"] == 3 and magicalSelfLockingChain == 1:
                menu:
                    "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить и добить Свинна":
                        $ current_enemy["health"] = 0
                        $ magicalSelfLockingChain = 0
                        f "Ты метаешь волшебную цепь! Она обвивается вокруг ослабленного Свинна, обездвиживая его. Ты наносишь решающий удар, и Свинн повержен! Цепь использована, и ты не можешь её снять. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
                        jump choice_195
                    "Не использовать цепь":
                        pass
        else:
            f "Твой мощный удар ([player_attack]) сокрушает [current_enemy['name']] ([enemy_attack])! Враг повержен! Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}."

        menu:
            "Использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ current_enemy["health"] -= 2
                    $ luck -= 1
                    if current_enemy["health"] > 0:
                        f "Удача на твоей стороне! Ты наносишь [current_enemy['name']] дополнительный урон (2). У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                        if current_enemy["health"] == 3 and magicalSelfLockingChain == 1:
                            menu:
                                "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить и добить Свинна":
                                    $ current_enemy["health"] = 0
                                    $ magicalSelfLockingChain = 0
                                    f "Ты метаешь волшебную цепь! Она обвивается вокруг ослабленного Свинна, обездвиживая его. Ты наносишь решающий удар, и Свинн повержен! Цепь использована, и ты не можешь её снять. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
                                    jump choice_195
                                "Не использовать цепь":
                                    pass
                    else:
                        f "Удача помогает тебе! Мощный дополнительный удар (2 урона) добивает [current_enemy['name']]! Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                        jump choice_195
                else:
                    $ current_enemy["health"] += 1
                    $ luck -= 1
                    f "Удача отвернулась! [current_enemy['name']] восстанавливает 1 здоровье (теперь {color=#FF00FF}[current_enemy['health']]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
            "Не использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                pass
        jump choice_119_fight

    else:
        $ health -= 2
        if health > 0:
            f "[current_enemy['name']] наносит тебе удар ([enemy_attack])! Твоя защита ([player_attack]) не справляется. Ты теряешь 2 здоровья, осталось {color=#FF00FF}[health]{/color}."
        else:
            f "[current_enemy['name']] наносит сокрушительный удар ([enemy_attack]) против твоей защиты ([player_attack])! Ты теряешь последние силы и падаешь."
            jump game_over

        menu:
            "Использовать удачу, чтобы смягчить урон":
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ health += 1
                    $ luck -= 1
                    f "Удача спасает тебя! Ты восстанавливаешь 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ health -= 1
                    $ luck -= 1
                    if health > 0:
                        f "Удача подвела! Ты теряешь дополнительное 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                    else:
                        f "Удача подвела, и ты теряешь последнее здоровье! [current_enemy['name']] добивает тебя."
                        jump game_over
            "Не использовать удачу, чтобы смягчить урон":
                pass
        jump choice_119_fight

label choice_134:
    scene 134-1 with dissolve
    pause 0.5
    e "В шкафу в углу комнаты вы находите два стеклянных сосуда."
    e "Первый подписан, как «Сок Блимберри», это лекарственное зелье, которое используется в народной медицине."
    e "Во втором пузырьке клей, видимо, он нужен мастеру для работы с тонкими деталями."
    menu:
        "Уйти":
            jump choice_9
        "Продолжить грабеж":
            jump choice_134_1

label choice_134_1:
    scene 134-1
    e "Настало время испытать вышу удачу!"
    $ twodice = renpy.random.randint(1, 12)
    s "Уровень вашей удачи - {color=#FF00FF}[luck]{/color}, требуемый уровень удачи - {color=#FF00FF}[twodice]{/color}"
    if twodice <= luck:
        s "Вам повезло!"
        $ luck -= 1
        s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
        jump choice_235
    else:
        s "Вам не повезло!"
        $ luck -= 1
        s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
        jump choice_19

label choice_145:
    scene 145-1 with dissolve
    pause 0.5
    e "Существо наклоняется над столом и бросает ложку и поварешку."
    menu:
        "Показать ему свое оружие и потребовать, чтобы оно отдало вам коробку со свитком и зеркалом":
            jump choice_273
        "Попытаться обмануть его и спросить, не можете ли вы купить у него еды":
            jump choice_283

label choice_243:
    scene 145-1 with dissolve
    pause 0.5
    e "Когда вы достаете оружие, существо громко ревет и бросается на вас."
    e "Вы должны сражаться с Пожирателем, который атакует, сильно раскачивая своей головой из стороны в сторону."
    e "При этом его длинные щупальца стараются схватить вас."
    $ current_enemy = {"name": "吞噬者", "mastery": 8, "health": 7} # Пожиратель
    jump choice_243_fight

label choice_243_fight:
    if health <= 0:
        f "Твои силы иссякли в бою с [current_enemy['name']]! Ты падаешь, побежденный его яростными щупальцами."
        jump game_over

    if current_enemy["health"] <= 0:
        f "Пожиратель повержен! Ты стоишь над его телом, тяжело дыша. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
        jump choice_29

    $ enemy_attack = renpy.random.randint(1, 12) + current_enemy["mastery"]
    $ player_attack = renpy.random.randint(1, 12) + mastery

    if enemy_attack == player_attack:
        f "Ты ([player_attack]) и [current_enemy['name']] ([enemy_attack]) атакуете одновременно, но оба уклоняетесь! Никто не ранен. Твое здоровье: {color=#FF00FF}[health]{/color}, здоровье врага: {color=#FF00FF}[current_enemy['health']]{/color}."
        jump choice_243_fight

    elif enemy_attack < player_attack:
        $ current_enemy["health"] -= 2
        if current_enemy["health"] > 0:
            f "Твой удар ([player_attack]) пробивает защиту [current_enemy['name']] ([enemy_attack])! Ты наносишь 2 урона. У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твое здоровье: {color=#FF00FF}[health]{/color}."
            if current_enemy["health"] == 3 and magicalSelfLockingChain == 1:
                menu:
                    "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить и добить Пожирателя":
                        $ current_enemy["health"] = 0
                        $ magicalSelfLockingChain = 0
                        f "Ты метаешь волшебную цепь! Она обвивается вокруг ослабленного Пожирателя, обездвиживая его. Ты наносишь решающий удар, и Пожиратель повержен! Цепь использована, и ты не можешь её снять. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
                        jump choice_29
                    "Не использовать цепь":
                        pass
        else:
            f "Твой мощный удар ([player_attack]) сокрушает [current_enemy['name']] ([enemy_attack])! Враг повержен! Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}."

        menu:
            "Использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ current_enemy["health"] -= 2
                    $ luck -= 1
                    if current_enemy["health"] > 0:
                        f "Удача на твоей стороне! Ты наносишь [current_enemy['name']] дополнительный урон (2). У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                        if current_enemy["health"] == 3 and magicalSelfLockingChain == 1:
                            menu:
                                "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить и добить Пожирателя":
                                    $ current_enemy["health"] = 0
                                    $ magicalSelfLockingChain = 0
                                    f "Ты метаешь волшебную цепь! Она обвивается вокруг ослабленного Пожирателя, обездвиживая его. Ты наносишь решающий удар, и Пожиратель повержен! Цепь использована, и ты не можешь её снять. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
                                    jump choice_29
                                "Не использовать цепь":
                                    pass
                    else:
                        f "Удача помогает тебе! Мощный дополнительный удар (2 урона) добивает [current_enemy['name']]! Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                        jump choice_29
                else:
                    $ current_enemy["health"] += 1
                    $ luck -= 1
                    f "Удача отвернулась! [current_enemy['name']] восстанавливает 1 здоровье (теперь {color=#FF00FF}[current_enemy['health']]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
            "Не использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                pass
        jump choice_243_fight

    else:
        $ health -= 2
        if health > 0:
            f "[current_enemy['name']] наносит тебе удар ([enemy_attack])! Твоя защита ([player_attack]) не справляется. Ты теряешь 2 здоровья, осталось {color=#FF00FF}[health]{/color}."
        else:
            f "[current_enemy['name']] наносит сокрушительный удар ([enemy_attack]) против твоей защиты ([player_attack])! Ты теряешь последние силы и падаешь."
            jump game_over

        menu:
            "Использовать удачу, чтобы смягчить урон":
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ health += 1
                    $ luck -= 1
                    f "Удача спасает тебя! Ты восстанавливаешь 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ health -= 1
                    $ luck -= 1
                    if health > 0:
                        f "Удача подвела! Ты теряешь дополнительное 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                    else:
                        f "Удача подвела, и ты теряешь последнее здоровье! [current_enemy['name']] добивает тебя."
                        jump game_over
            "Не использовать удачу, чтобы смягчить урон":
                pass
        jump choice_243_fight

label choice_257:
    jump choice_243

label choice_240:
    scene 240-1 with dissolve
    pause 0.5
    e "Вы входите в палатку, и неопрятный бородач приветствует вас."
    show BeardedMan
    bem "Добро пожаловать, добро пожаловать, мой друг!"
    bem "И давайте посмотрим, какой приз вы сможете выиграть сегодня."
    bem "У Честного Ганна и его Шкафа Фортуны не бывает проигравших!"
    e "Он подводит вас к большому застекленному шкафу."
    e "Внутри лежат разные предметы: украшения, книги, золото, сумки и еда."
    e "Вместе с ними в шкафу заперто маленькое крылатое гуманоидное существо - Мит."
    bem "Всего 2 золотых, мой друг, и мы увидим, что мой маленький питомец добудет для вас!"
    menu:
        "Заплатить" if gold >= 2:
            jump choice_318
        "Покинуть палатку и фестиваль":
            jump choice_160

label choice_160:
    scene 297-2 with dissolve
    pause 0.5
    e "Вы приближаетесь к центру Кхара. Застройка становится плотней, а дороги грязнее."
    e "Народ толпится на улицах и пялится на вас, пока вы проходите мимо."
    e "Вы подходите к развилке."
    menu:
        "Повернуть налево":
            jump choice_202
        "Продолжить путь в портовый район":
            jump choice_165

label choice_17:
    scene 261-1
    e "Вы стараетесь изо всех сил следовать за коленцами танцоров, но без особого успеха."
    e "Тем не менее, вы наслаждаетесь пляской и можете восстановить еще 1 очко Здоровья."
    $ health += 1
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    e "Но танец начинает утомлять вас, особенно учитывая вес вашего рюкзака и оружия."
    e "Кажется, мелодия и не собирается заканчиваться."
    e "Удастся ли продержаться до конца танца?"
    $ loop = 0
    jump choice_17_loop

label choice_17_loop:
    if health <= 0:
        jump game_over
    if loop >= 5:
        jump choice_201
    $ loop += 1
    if gold > 0:
        $ summ = meal + sword + blackmask + healingPotion + bagWithThreeStones + servingOfSeaSand + perch + magicalSelfLockingChain + braceletBones + dimChain + goldFramedMirror + scrollParchment + bottleWithTheInscription + honeycombWithBeeswax + bottleDust + goatCheese + emptyWallet + goodLuckCharm + cuffWithDarts + poison + spirits + wig + 3
    else:
        $ summ = meal + sword + blackmask + healingPotion + bagWithThreeStones + servingOfSeaSand + perch + magicalSelfLockingChain + braceletBones + dimChain + goldFramedMirror + scrollParchment + bottleWithTheInscription + honeycombWithBeeswax + bottleDust + goatCheese + emptyWallet + goodLuckCharm + cuffWithDarts + poison + spirits + wig
    $ twodice = renpy.random.randint(1, 12)
    s "Вес носимых вами артефактов - {color=#FF00FF}[summ]{/color}. Ваше выносливость в танце - {color=#FF00FF}[twodice]{/color}"
    if summ < twodice:
        e "Вы продержались не переутомившись до конца танца"
        jump choice_201
    else:
        e "Вы не смогли продержаться до конца танца"
        e "Вы теряете одну единицу Здровья"
        $ health -= 1
        s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
        if health <=0:
            jump game_over
        e "Но танец продолжается!"
        s "Танец уже продолжается {color=#FF00FF}[loop]{/color} минут из 5-и"
        jump choice_17_loop

label choice_40:
    scene 261-1
    e "Зрители в толпе вокруг вас злятся на ваш отказ присоединиться к танцу."
    e "Они толкают вас вперед, а вы пытаетесь сдержать закипающую в вас злобу."
    rm "Где же твой дух?"
    rm "Засранец. Это всего лишь немного веселья"
    menu:
        "Настаивать на том, чтобы отклонить приглашение на танец":
            jump choice_230
        "Не рисковать и не сердить толпу":
            jump choice_17

label choice_63:
    scene 269-1
    e "С радостью и облегчением вы обнаруживаете, что ваше собственное золото все еще при вас."
    e "В толпе вспыхивают драки и ссоры – жертвы карманника обвиняют в краже своих соседей."
    e "Вы решаете уйти."
    menu:
        "Посмотреть на танцы":
            jump choice_261
        "Отправиться к рингу, чтобы узнать, появился ли у чемпиона претендент":
            jump choice_33
        "Уйти с фестиваля":
            jump choice_263

label choice_177:
    scene 269-1
    e "Ваше сердце замирает, когда вы ощупываете свой кошелек."
    e "Карманник украл все ваши деньги - вы теперь без гроша!"
    $ gold = 0
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    e "В толпе вспыхивают драки и ссоры – жертвы карманника обвиняют в краже своих соседей."
    e "Вы решаете уйти."
    menu:
        "Посмотреть на танцы":
            jump choice_261
        "Отправиться к рингу, чтобы узнать, появился ли у чемпиона претендент":
            jump choice_33
        "Уйти с фестиваля":
            jump choice_263

label choice_190:
    scene 33-1
    show Bookmaker
    i "Какие ставки ты принимаешь?"
    bck "Чувствуешь, что сегодня тебе повезет?"
    bck "Ставки на чемпиона 3 к 1. Устраивает?"
    e "Каждая монета, которую вы поставите на варвара, принесет вам выигрыш в 3 золотых, а если поставите на огра, то каждые 3 монеты дадут выигрыш в 1 золотой."
    e "Это если вы угадаете победителя, если не угадаете, то теряете свою ставку."
    s "Количество вашего золота - {color=#FF00FF}[gold]{/color}"
    $ user_input = renpy.input("输入下注金额：")
    $ user_input = user_input.strip()  # Удаляем пробелы
    if user_input.isdigit() or (user_input.startswith("-") and user_input[1:].isdigit()):
        $ bidAmount = int(user_input)
        if bidAmount > gold:
            $ bidAmount = gold
            s "Вша ставка: [bidAmount]."
        else:
            s "Вша ставка: [bidAmount]."
    else:
        "Ошибка: введите корректное целое число!"
    menu:
        "Ставка на Варвара":
            $ targAmount = 1
        "Ставка на Огра":
            $ targAmount = 2
    $ gold = gold - bidAmount
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    jump choice_234

label choice_234:
    scene 33-1
    play sound "audio/33-1.mp3"
    pause 3
    e "Бой начинается! Варвар и Огр сходятся на ринге, толпа ревет от восторга."
    $ barbarian = {"name": "野蛮人", "mastery": 8, "health": 8} # Варвар
    $ ogre = {"name": "食人魔", "mastery": 9, "health": 12} # Огр
    $ winner = 0
    jump choice_234_fight

label choice_234_fight:
    if barbarian["health"] <= 0:
        f "Огр наносит сокрушительный удар! Варвар падает, побежденный."
        $ winner = 2
        jump choice_234_result

    if ogre["health"] <= 0:
        f "Варвар с ревом наносит последний удар! Огр рухнул на ринг!"
        $ winner = 1
        jump choice_234_result

    $ barb_attack = renpy.random.randint(1, 12) + barbarian["mastery"]
    $ ogre_attack = renpy.random.randint(1, 12) + ogre["mastery"]

    if barb_attack == ogre_attack:
        f "Варвар ([barb_attack]) и Огр ([ogre_attack]) атакуют одновременно, но оба уклоняются! Никто не ранен."
        jump choice_234_fight

    elif barb_attack > ogre_attack:
        $ ogre["health"] -= 2
        f "Варвар ([barb_attack]) пробивает защиту Огр ([ogre_attack])! Огр теряет 2 здоровья, осталось {color=#FF00FF}[ogre['health']]{/color}."
        jump choice_234_fight

    else:
        $ barbarian["health"] -= 2
        f "Огр ([ogre_attack]) наносит мощный удар Варвару ([barb_attack])! Варвар теряет 2 здоровья, осталось {color=#FF00FF}[barbarian['health']]{/color}."
        jump choice_234_fight

label choice_234_result:
    scene 33-1
    if targAmount == 1 and winner == 1:
        e "Вы поставили на Варвара и он победил!"
        $ winsum = bidAmount + bidAmount * 3
        s "Сумма вашего выигрыша составила - {color=#FF00FF}[winsum]{/color}"
        $ gold = gold + winsum
        s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    if targAmount == 2 and winner == 2:
        e "Вы поставили на Огра и он победил!"
        $ winsum = bidAmount + bidAmount
        s "Сумма вашего выигрыша составила - {color=#FF00FF}[winsum]{/color}"
        $ gold = gold + winsum
        s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    else:
        e "Ваша ставка не сыграла"
        s "Количество вашего золота по прежнему - {color=#FF00FF}[gold]{/color}"
    jump choice_136

label choice_199:
#Предложи вернуться в магазин на 149
    scene 149-1
    menu:
        "Купить еще что-нибудь" if gold >= 2:
            jump choice_149
        "Двигаться дальше":
            jump choice_199_a

label choice_199_a:
    scene 149-1
    if perch == 1:
        jump choice_210
    else:
        jump choice_272

label choice_170:
    scene 233-1 with dissolve
    pause 0.5
    e "Примите решение куда двигаться дальше"
    menu:
        "Покинуть этот район":
            jump choice_153
        "Присоединиться к толпе, наблюдающей за уличной дракой":
            jump choice_185

label choice_8:
    scene 153-1
    e "Вы подходите к статуе, думая, что это, должно быть, работа очень талантливого художника, ведь она выглядит очень реалистично."
    e "Но затем «статуя» мигает, ломая свою игру, впрочем, ваша реакция уже все равно запоздала."
    scene 8-1 with dissolve
    pause 0.5
    e "В одно мгновение длинные руки существа вытягиваются к вам, хватают вас за плечи, поднимают в воздух и подносят к его лицу."
    e "Оно открывает пасть и вонзает острые зубы вам в шею. Вы умираете, прежде чем осознаете, что произошло!"
    e "Вы повстречались с одним из самых смертоносных обитателей Кхара – Человеком-Богомолом."
    jump game_over

label choice_27:
    scene 27-1 with dissolve
    pause 0.5
    e "Внутри хижины на полу валяются кости. Тот, кто живет здесь, явно плотоядный."
    e "Судя по размеру некоторых костей, это существо, похоже, весьма неравнодушно к людям."
    e "Поскольку хижина в данный момент пуста, вы шарите среди останков."
    e "Повсюду разбросана одежда несчастных жертв, а в их карманах вы находите 15 золотых, а также несколько мелких костей, скрученных в браслет."
    e "Вы берете находки с собой"
    $ gold += 15
    $ braceletBones = 1
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    e "Вы осторожно вы выходите из хижины, предварительно убедившись, что никого нет рядом"
    jump choice_37

label choice_137:
    scene 137-1 with dissolve
    pause 0.5
    e "Вы продолжаете путь по дороге, пока не подходите к Y-образной развилке, и продолжаете путь на север."
    jump choice_191

label choice_302:
    scene 98-1
    jump choice_311

label choice_321:
    scene 98-1
    e "Толпа недовольна вашим вмешательством. Вы должны выбрать против кого будете драться"
    menu:
        "Против Спрайта":
            $ streetfighter = 1
        "Против Пикси":
            $ streetfighter = 2
    e "Для того, чтобы помочь вашему противнику в бой неожидано влезает гном"
    scene 321-1 with dissolve
    pause 0.5
    if streetfighter == 1:
        $ enemies = [
            {"name": "精灵", "mastery": 5, "health": 6}, # Спрайт
            {"name": "侏儒", "mastery": 6, "health": 6} # Гном
        ]
    else:
        $ enemies = [
            {"name": "皮克西", "mastery": 5, "health": 5}, # Пикси
            {"name": "侏儒", "mastery": 6, "health": 6} # Гном
        ]
    jump choice_321_fight

label choice_321_fight:
    if health <= 0:
        f "Твои силы иссякли в бою с [current_enemy['name']]! Ты падаешь, побежденный их слаженной атакой."
        jump game_over

    $ living_enemies = [e for e in enemies if e["health"] > 0]
    if not living_enemies and streetfighter == 1:
        f "Спрайт и гном побеждены! Ты стоишь над их телами, тяжело дыша. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
        jump choice_335
    if not living_enemies and streetfighter == 2:
        f "Пикси и гном побеждены! Ты стоишь над их телами, тяжело дыша. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
        jump choice_293

    $ current_enemy = renpy.random.choice(living_enemies)

    $ enemy_attack = renpy.random.randint(1, 12) + current_enemy["mastery"]
    $ player_attack = renpy.random.randint(1, 12) + mastery

    if enemy_attack == player_attack:
        f "Ты ([player_attack]) и [current_enemy['name']] ([enemy_attack]) атакуете одновременно, но оба уклоняетесь! Никто не ранен. Твое здоровье: {color=#FF00FF}[health]{/color}, здоровье врага: {color=#FF00FF}[current_enemy['health']]{/color}."
        jump choice_321_fight

    elif enemy_attack < player_attack:
        $ current_enemy["health"] -= 2
        if current_enemy["health"] > 0:
            f "Твой удар ([player_attack]) пробивает защиту [current_enemy['name']] ([enemy_attack])! Ты наносишь 2 урона. У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твое здоровье: {color=#FF00FF}[health]{/color}."
            if current_enemy["health"] <= 3 and magicalSelfLockingChain == 1:
                menu:
                    "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить и добить [current_enemy['name']]":
                        $ current_enemy["health"] = 0
                        $ magicalSelfLockingChain = 0
                        f "Ты метаешь волшебную цепь! Она обвивается вокруг ослабленного [current_enemy['name']], обездвиживая его. Ты наносишь решающий удар, и [current_enemy['name']] повержен! Цепь использована, и ты не можешь её снять. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
                        jump choice_321_fight
                    "Не использовать цепь":
                        pass
        else:
            f "Твой мощный удар ([player_attack]) сокрушает [current_enemy['name']] ([enemy_attack])! Враг повержен! Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}."

        menu:
            "Использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ current_enemy["health"] -= 2
                    $ luck -= 1
                    if current_enemy["health"] > 0:
                        f "Удача на твоей стороне! Ты наносишь [current_enemy['name']] дополнительный урон (2). У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                        if current_enemy["health"] <= 3 and magicalSelfLockingChain == 1:
                            menu:
                                "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить и добить [current_enemy['name']]":
                                    $ current_enemy["health"] = 0
                                    $ magicalSelfLockingChain = 0
                                    f "Ты метаешь волшебную цепь! Она обвивается вокруг ослабленного [current_enemy['name']], обездвиживая его. Ты наносишь решающий удар, и [current_enemy['name']] повержен! Цепь использована, и ты не можешь её снять. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
                                    jump choice_321_fight
                                "Не использовать цепь":
                                    pass
                    else:
                        f "Удача помогает тебе! Мощный дополнительный удар (2 урона) добивает [current_enemy['name']]! Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ current_enemy["health"] += 1
                    $ luck -= 1
                    f "Удача отвернулась! [current_enemy['name']] восстанавливает 1 здоровье (теперь {color=#FF00FF}[current_enemy['health']]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
            "Не использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                pass
        jump choice_321_fight

    else:
        $ health -= 2
        if health > 0:
            f "[current_enemy['name']] наносит тебе удар ([enemy_attack])! Твоя защита ([player_attack]) не справляется. Ты теряешь 2 здоровья, осталось {color=#FF00FF}[health]{/color}."
        else:
            f "[current_enemy['name']] наносит сокрушительный удар ([enemy_attack]) против твоей защиты ([player_attack])! Ты теряешь последние силы и падаешь."
            jump game_over

        menu:
            "Использовать удачу, чтобы смягчить урон":
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ health += 1
                    $ luck -= 1
                    f "Удача спасает тебя! Ты восстанавливаешь 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ health -= 1
                    $ luck -= 1
                    if health > 0:
                        f "Удача подвела! Ты теряешь дополнительное 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                    else:
                        f "Удача подвела, и ты теряешь последнее здоровье! [current_enemy['name']] добивает тебя."
                        jump game_over
        jump choice_321_fight

label choice_180:
    scene 300-1
    i "Откуда вы Идете?"
    lo "Мы идем с уроков, которые дает нам один ученый, его дом чуть дальше по дороге."
    jump choice_329

label choice_289:
    scene 300-1
    i "Как добраться до центра города?"
    lo "Вы идете не в ту сторону. Вы должны повернуть назад и на развилке свернуть на другую дорогу."
    menu:
        "Послушать орклингов":
            jump choice_233
        "Продолжить путь в прежнем направлении":
            jump choice_329

label choice_246:
    scene 300-1
    i "Вы слышали о ком-то по имени Вик?"
    e "Они смотрят друг на друга и качают головами."
    e "Они никогда не слышали ни о ком по имени Вик."
    lo "Дай еще золотой!"
    e "Все остальные присоединяются к его крику, протягивая руки и требуя больше денег"
    jump choice_329

label choice_316:
    scene 300-1
    e "Вы прогоняете пострелят и продолжаете свой путь."
    scene 316-1 with dissolve
    pause 0.5
    e "Вскоре вы подходите к большому дому, сложенному из камней, скрепленных раствором."
    e "Он выглядит довольно внушительно."
    menu:
        "Подняться к входной двери" if block61and140 == 0:
            jump choice_140
        "Пробраться к задней части дома" if block61and140 == 0:
            jump choice_208
        "Пройти мимо дома дальше по дороге":
            jump choice_133

label choice_262:
    scene 329-1
    $ dice = renpy.random.randint(1, 6)
    if dice <= 3:
        e "Маленькие бандиты украли у вас 3 монеты!"
        $ gold -= 3
        if gold > 0:
            s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
        else:
            $ gold = 0
            s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    else:
        e "Маленькие бандиты украли у вас всю еду!"
        $ meal = 0
        s "Теперь количество вашей еды - {color=#FF00FF}[meal]{/color}"
    jump choice_61

label choice_268:
    scene 49-1
    e "Лошадь галопом мчится по дороге, а вы отчаянно стараетесь удержаться на ней."
    scene 268-1 with dissolve
    pause 0.5
    e "Когда она приближается к группе хижин, маленькое чешуйчатое существо перебегает дорогу перед ней и пугает ее."
    e "Конь встает на дыбы, вы теряете стремена и соскальзываете у него со спины, падая на землю."
    e "К счастью, вы остались невредимы."
    e "Конь ржет и мчится дальше, оставляя вас сидеть посреди дороги."
    e "Вы встаете и осматриваетесь."
    menu:
        "Подойти к хижине слева от дороги":
            jump choice_66
        "Подойти к хижине справа от дороги":
            jump choice_171
        "Пойти прямо":
            jump choice_294

label choice_220:
    scene 49-1
    e "Настало время испытать вышу удачу!"
    $ twodice = renpy.random.randint(1, 12)
    s "Уровень вашей удачи - {color=#FF00FF}[luck]{/color}, требуемый уровень удачи - {color=#FF00FF}[twodice]{/color}"
    if twodice <= luck:
        s "Вам повезло!"
        $ luck -= 1
        s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
        jump choice_106
    else:
        s "Вам не повезло!"
        $ luck -= 1
        s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
        jump choice_6

label choice_216:
    scene 297-2
    show YoungMan
    ym "Если хотите найти комнату на ночь"
    ym "То на вашем месте я бы не ходил направо на развилке впереди"
    e "Вы благодарите его за совет и ломаете голову над его ответом, когда подходите к развилке."
    e "Помните, что он отъявленный лжец."
    jump choice_144

label choice_51:
    scene 297-2
    show YoungMan
    ym "Давайте посмотрим"
    ym "Кто может знать строку из заклинания."
    ym "Ах, да. На развилке впереди не идите прямо, а в конце не поворачивайте налево."
    ym "Да .. Я думаю, что это все. Удачи"
    e "Вы не совсем уверены в том, что поняли его совет и, что вам делать, но идете к указанному перекрестку."
    e "Помните, что он отъявленный лжец."
    jump choice_144

label choice_34:
    scene 57-2
    show BlackMan
    e "Он возвращается с двумя кружками эля и ставит одну перед вами."
    bm "Центр Кхара находится вокруг порта"
    bm "И это опасное место для ночлега."
    bm "Многие из тех, кто бродят там ночью, попадают в плен к командам кораблей работорговцев"
    bm "Поэтому перед заходом солнца найди себе ночлег в какой-нибудь таверне."
    bm "И еще одна вещь... но давай, выпей свой эль"
    e "Вы отпиваете из кружки"
    jump choice_236

label choice_223:
    scene 57-2
    show BlackMan
    e "Вы делаете шаг к выходу."
    hide BlackMan
    show BlackManBow
    bm "Никто не сбежит от Вангорна Убийцы!"
    jump choice_13

label choice_195:
    scene 66-1
    show PorkDead
    e "Обшарив карманы свинна, вы находите 10 золотых – видимо, изготовление цепей выгодное занятие в Кхаре."
    $ gold += 10
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    e "Еще в кармане у него лежит аккуратно сложенная шапочка из ткани, она может пригодиться вам при накладывании заклинаний."
    e "Выходя из мастерской, вы цепляетесь за тусклую цепь, которая привлекает ваше внимание, и решаете взять ее с собой."
    e "Это оказался талисман, прибавляющий 1 очко удачи!"
    $ dimChain = 1
    $ luck += 1
    s "Теперь уровень вашей удачи - {color=#FF00FF}[luck]{/color}"
    jump choice_203

label choice_235:
    scene 66-1
    e "Вам невероятно везет, хозяин мастерской до сих пор не услышал, как вы шарите по его дому."
    e "Но он не оставил свою мастерскую без защиты."
    e "Когда вы пересекаете комнату, с потолка падает сеть из цепей и опутывает вас."
    e "Вы пытаетесь вырваться из нее, но лишь сильнее запутываетесь."
    jump choice_154

label choice_273:
    scene 145-1
    e "Проверьте уровень своего мастерства!"
    $ twodice = renpy.random.randint(1, 20)
    s "Уровень вашего мастерства - {color=#FF00FF}[mastery]{/color}, требуемый уровень мастерства - {color=#FF00FF}[twodice]{/color}"
    if twodice <= mastery:
        s "Ваше мастерство позволило сделать задуманное!"
        jump choice_313
    else:
        s "Ваше мастерство не позволило сделать задуманное!"
        jump choice_203

label choice_283:
    scene 43-1 with dissolve
    pause 0.5
    h "Трапеза обойдется тебе в 5 золотых"
    menu:
        "Продолжить ваш обман, заплатить и поесть" if gold >= 5:
            jump choice_100
        "Уйти":
            jump choice_294
        "Напасть на него":
            jump choice_243

label choice_29:
    scene 29-1 with dissolve
    pause 0.5
    e "Вы хватаете ящик и выбегаете из дома."
    e "Кажется, странное существо хранило в нем все свое самое ценное имущество, впрочем, немногочисленное."
    e "Внутри лежит изысканное зеркало в золотой оправе – самый впечатляющий предмет, свиток пергамента, весь покрытый письменами на языке, который вы не понимаете и 2 золотых."
    $ goldFramedMirror = 1
    $ scrollParchment = 1
    $ gold += 2
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    jump choice_294

label choice_318:
    scene 240-1
    show BeardedMan
    e "Бородач берет ваши деньги и нажимает маленькую кнопку на стене шкафа."
    $ gold -= 2
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    e "Маленькое существо начинает с визгом метаться внутри, хватает один из призов и через маленькое отверстие в передней стенке выбрасывает его вам под ноги."
    $ dice = renpy.random.randint(1, 6)
    if dice == 1:
        jump choice_279
    if dice == 2:
        jump choice_5
    if dice == 3:
        jump choice_167
    if dice == 4:
        jump choice_92
    if dice == 5:
        jump choice_71
    if dice == 6:
        jump choice_219

label choice_202:
    scene 137-1 with dissolve
    pause 0.5
    e "Следуя по этой улице, вы выходите на развилку."
    menu:
        "Продолжить путь прямо":
            jump choice_131
        "Свернуть направо на другую улицу":
            jump choice_139

label choice_165:
    scene 297-2
    e "Ночь приближается, и вас нет никакого желания провести ее на улицах Кхара."
    show Townswoman
    e "Вы останавливаете проходящую мимо женщину и спрашиваете у нее, где здесь ближайшая гостиница."
    tw "Иди прямо к порту"
    tw "Там по пути есть таверна."
    tw "Но поспеши, незнакомец, ночь наступает"
    i "Благодарю вас!"
    scene 165-1 with dissolve
    pause 0.5
    e "Вы благодарите ее и продолжаете путь. В конце концов, вы добираетесь до заведения под названием «Отдых путника» и заходите внутрь"
    jump choice_110

label choice_201:
    scene 244-1 with dissolve
    pause 0.5
    e "Вы покидаете танцующих"
    menu:
        "Посмотреть состязание с участием местного чемпиона":
            jump choice_33
        "Покинуть фестиваль":
            jump choice_263

label choice_230:
    scene 261-1
    e "Вы пробираетесь через толпу подальше от танца, а зрители улюлюкают и издеваются над вами."
    e "Кто-то отвешивает вам сильного пинка, заставляя вздрогнуть и ускориться, теряете 2 очка Здоровья."
    $ health -= 2
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    if health <=0:
        jump game_over
    e "В конце концов, вы пробиваетесь сквозь толпу"
    jump choice_201

label choice_136:
    scene 136-1 with dissolve
    pause 0.5
    e "Теперь вы видели, как проходят здесь чемпионские бои."
    e "Вы тоже можете бросить вызов чемпиону, приз победителю 15 золотых"
    menu:
        "Бросить вызов чемпиону":
            jump choice_82
        "Покинуть фестиваль":
            jump choice_263

label choice_210:
    scene 149-1
    se "Какие именно перчатки вы хотите? Кольчужные или кожаные?"
    menu:
        "Кольчужные":
            $ chainmailGloves = 1
            jump choice_228
        "Кожаные":
            $ leatherGloves = 1
            jump choice_238

label choice_272:
    scene 149-1
    if bottleDust >= 1:
        jump choice_247
    else:
        jump choice_259

label choice_185:
    scene 233-1 with dissolve
    pause 0.5
    e "Бой в далеке уже начал утихать"
    $ dice = renpy.random.randint(1, 6)
    if dice % 2 == 0:
        jump choice_153
    else:
        jump choice_98

label choice_37:
    scene 37-1 with dissolve
    pause 0.5
    e "Выйдя из хижины, вы снова смотрите на статую. Хотя вы не уверены, но вам кажется, что что-то изменилось."
    e "А потом до вас доходит, ее голова повернулась и теперь смотрит прямо на вас!"
    menu:
        "Попытаться быстро убежать":
            jump choice_55
        "Взяться за оружие":
            jump choice_76

label choice_191:
    scene 191-1 with dissolve
    pause 0.5
    e "Вы достигаете развилки, где сходятся несколько дорог."
    menu:
        "Продолжить путь прямо":
            jump choice_297
        "Повернуть направо":
            jump choice_84

label choice_311:
    scene 311-1 with dissolve
    pause 0.5
    e "Толпа освистывает вас, когда вы шагаете вперед."
    e "Вы хватаете дерущихся малышей и растаскиваете их."
    e "Однако мелкие засранцы вам вовсе не благодарны, и теперь они оба поворачиваются, чтобы напасть на вас!"
    $ enemies = [
        {"name": "精灵", "mastery": 5, "health": 6}, # Спрайт
        {"name": "皮克西", "mastery": 5, "health": 5} # Пикси
    ]
    jump choice_311_fight

label choice_311_fight:
    if health <= 0:
        f "Твои силы иссякли в бою с [current_enemy['name']]! Ты падаешь, побежденный их слаженной атакой."
        jump game_over

    $ living_enemies = [e for e in enemies if e["health"] > 2]
    if not living_enemies:
        f "Спрайт и Пикси отступают, тяжело дыша! Ты заставил их прекратить драку. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
        jump choice_153

    $ current_enemy = renpy.random.choice(living_enemies)

    $ enemy_attack = renpy.random.randint(1, 12) + current_enemy["mastery"]
    $ player_attack = renpy.random.randint(1, 12) + mastery

    if enemy_attack == player_attack:
        f "Ты ([player_attack]) и [current_enemy['name']] ([enemy_attack]) атакуете одновременно, но оба уворачиваетесь! Никто не ранен. Твое здоровье: {color=#FF00FF}[health]{/color}, здоровье врага: {color=#FF00FF}[current_enemy['health']]{/color}."
        jump choice_311_fight

    elif enemy_attack < player_attack:
        $ current_enemy["health"] -= 2
        if current_enemy["health"] > 2:
            f "Твой удар ([player_attack]) пробивает защиту [current_enemy['name']] ([enemy_attack])! Ты наносишь 2 урона. У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твое здоровье: {color=#FF00FF}[health]{/color}."
            if current_enemy["health"] <= 3 and magicalSelfLockingChain == 1:
                menu:
                    "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить [current_enemy['name']]":
                        $ current_enemy["health"] = 2
                        $ magicalSelfLockingChain = 0
                        f "Ты метаешь волшебную цепь! Она обвивается вокруг [current_enemy['name']], обездвиживая его. Он теряет силы, осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Цепь использована, и ты не можешь её снять."
                        jump choice_311_fight
                    "Не использовать цепь":
                        pass
        else:
            f "Твой удар ([player_attack]) заставляет [current_enemy['name']] ([enemy_attack]) отступить! Он ослаб, осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твое здоровье: {color=#FF00FF}[health]{/color}."

        menu:
            "Использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 2:
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ current_enemy["health"] -= 2
                    $ luck -= 1
                    if current_enemy["health"] > 2:
                        f "Удача на твоей стороне! Ты наносишь [current_enemy['name']] дополнительный урон (2). У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                        if current_enemy["health"] <= 3 and magicalSelfLockingChain == 1:
                            menu:
                                "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить [current_enemy['name']]":
                                    $ current_enemy["health"] = 2
                                    $ magicalSelfLockingChain = 0
                                    f "Ты метаешь волшебную цепь! Она обвивается вокруг [current_enemy['name']], обездвиживая его. Он теряет силы, осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Цепь использована, и ты не можешь её снять."
                                    jump choice_311_fight
                                "Не использовать цепь":
                                    pass
                    else:
                        f "Удача помогает тебе! Дополнительный удар (2 урона) заставляет [current_enemy['name']] отступить! Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ current_enemy["health"] += 1
                    $ luck -= 1
                    f "Удача отвернулась! [current_enemy['name']] восстанавливает 1 здоровье (теперь {color=#FF00FF}[current_enemy['health']]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
            "Не использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 2:
                pass
        jump choice_311_fight

    else:
        $ health -= 2
        if health > 0:
            f "[current_enemy['name']] наносит тебе удар ([enemy_attack])! Твоя защита ([player_attack]) не справляется. Ты теряешь 2 здоровья, осталось {color=#FF00FF}[health]{/color}."
        else:
            f "[current_enemy['name']] наносит сокрушительный удар ([enemy_attack]) против твоей защиты ([player_attack])! Ты теряешь последние силы и падаешь."
            jump game_over

        menu:
            "Использовать удачу, чтобы смягчить урон":
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ health += 1
                    $ luck -= 1
                    f "Удача спасает тебя! Ты восстанавливаешь 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ health -= 1
                    $ luck -= 1
                    if health > 0:
                        f "Удача подвела! Ты теряешь дополнительное 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                    else:
                        f "Удача подвела, и ты теряешь последнее здоровье! [current_enemy['name']] добивает тебя."
                        jump game_over
        jump choice_311_fight

label choice_293:
    scene 293-1 with dissolve
    pause 0.5
    sp "Я очень благодарен вам! Как я могу вас отблагодарить"
    i "Мне нужно узнать заклинание, открывающее Северные Врата."
    sp "Я ничего не знаю о заклинании, но знаю того, кто может помочь!"
    scene 293-2 with dissolve
    pause 0.5
    sp "Следуй за мной!"
    scene 316-1 with dissolve
    pause 0.5
    e "В конце концов, вы подходите к большому дому, сложенному из камней, скрепленных раствором, и спрайт покидает вас, указав на него."
    e "Строение выглядит довольно внушительно."
    menu:
        "Подняться к входной двери" if block61and140 == 0:
            jump choice_140
        "Пробраться к задней части дома" if block61and140 == 0:
            jump choice_208
        "Пройти мимо дома дальше по дороге":
            jump choice_133

label choice_335:
    scene 335-1 with dissolve
    pause 0.5
    pi "Благодарю вас за помощь!"
    pi "Могу ли я что-нибудь сделать для вас взамен?"
    i "Мне нужно узнать заклинание, открывающее Северные Врата."
    pi "Заклинания я не знаю, но у меня есть другая информация, которая может быть вам интересна"
    pi "Вы можете узнать о заклинании у жреца, который очень хорошо осведомлен о всех делах и событиях в Кхаре."
    pi "Вы встретите его, по дороге дальше, сегодня он будет пытаться привлечь новообращенных к своей вере в своей часовне."
    pi "И еще... будте осторожным в центре города, потому что портовый район – любимое место охоты работорговцев."
    pi "Они подкарауливают неосторожных и затаскивают на свои корабли."
    pi "Их любимая уловка – подпоить жертву, а затем похитить."
    e "Получив ценную информацию вы восстанавливаете 1 очко удачи"
    $ luck += 1
    s "Теперь уровень вашей удачи - {color=#FF00FF}[luck]{/color}"
    jump choice_153

label choice_140:
    scene 140-1 with dissolve
    pause 0.5
    e "Вы стоите перед солидной дубовой дверью, украшенной затейливой резьбой."
    e "В центре укреплен латунный молоток, и вы трижды стучите им в дверь."
    play sound "audio/1-1.mp3"
    pause 2
    scene 140-2 with dissolve
    pause 0.5
    show Magician
    pause 2
    i "Здравствуйте! Не будете ли вы так любезны пустить меня в ваш дом?"
    m "Здравствуйте! Отдай мне всё свое оружие, тогда пущу"
    menu:
        "Согласиться на его требование":
            jump choice_229
        "Силой вломиться в дом":
            jump choice_95

label choice_208:
    scene 208-1 with dissolve
    pause 0.5
    e "Вы крадётесь вокруг дома и проверяете окна."
    e "За одним из них вы видите просторный кабинет, вдоль стен которого стоят сплошь полки с книгами."
    e "Очевидно, владелец дома – это мудрец, ученый или волшебник."
    menu:
        "Вернуться к входной двери":
            jump choice_140
        "Попытаться проникнуть внутрь через заднюю дверь":
            jump choice_172

label choice_133:
    scene 133-1 with dissolve
    pause 0.5
    e "Чуть дальше по дороге вы попадаете в район, где гончары, ткачи и художники демонстрируют и продают свои товары прямо на пороге своих хижин."
    menu:
        "Остановиться и осмотреться":
            jump choice_3
        "Продожить путь":
            jump choice_173

label choice_61:
    scene 316-1 with dissolve
    pause 0.5
    e "Вскоре вы подходите к большому дому, сложенному из камней, скрепленных раствором."
    e "Он выглядит довольно внушительно."
    menu:
        "Подняться к входной двери" if block61and140 == 0:
            jump choice_140
        "Пробраться к задней части дома" if block61and140 == 0:
            jump choice_208
        "Пройти мимо дома дальше по дороге":
            jump choice_133

label choice_106:
    scene 49-1
    e "Лошадь встает на дыбы, когда вы тянете за поводья."
    e "Вам не удается остановить ее, она продолжает мчаться по дороге, а вы можете лишь изо всех сил стараться удержаться в седле"
    jump choice_268

label choice_6:
    scene 49-1
    e "Жеребец встает на дыбы, когда вы натягиваете поводья в попытке его остановить."
    e "Вы отчаянно пытаетесь удержаться в седле, но безуспешно: он сбрасывает вас на землю, теряете 2 очка Здоровья."
    $ health -= 2
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    if health <=0:
        jump game_over
    e "Вы поднимаетесь на ноги и отряхиваетесь. Лошадь тем временем исчезает за поворотом впереди, и вы можете вернуться к развилке"
    jump choice_237

label choice_144:
    scene 237-1 with dissolve
    pause 0.5
    e "Вы вышли на развилку"
    menu:
        "Пойти прямо":
            jump choice_165
        "Повернуть направо":
            jump choice_120

label choice_236:
    scene 57-2
    show BlackMan
    e "Вы отхлебываете из кружки и слизываете пену с губ."
    bm "Как я уже говорил"
    bm "Еще одна вещь, на которую нужно обратить внимание — это ловушки-порталы на дальней стороне Джабаджи."
    bm "Архонты живут на северной стороне и защищают себя магическими порталами."
    bm "Если вы попадете в один из них, кто знает, где вы окажетесь!"
    e "Тон его голоса меняется, а глаза сужаются"
    bm "Но вы, мой друг, никогда не достигнете северной стороны, Вангорн Убийца заполучил еще одну жертву!"
    e "Он громко смеется, и вы чувствуете острую боль в животе. Вас отравили!"
    if kharLibra == 0:
        e "Вы призываете Либру"
        jump choice_129
    else:
        jump game_over

label choice_13:
    scene 57-2
    show BlackManBow
    e "Прежде чем вы успеваете добраться до него, он спускает тетиву."
    e "Куда попала стрела определит случай"
    $ dice = renpy.random.randint(1, 6)
    if dice == 1:
        e "Стрела попала вам в глаз, вы убиты."
        jump game_over
    if dice == 2:
        e "Стрела попала вам в грудь, теряете 5 очков Здоровья"
        $ health -= 5
        s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
        if health <=0:
            jump game_over
    if dice == 3:
        e "Стрела попала вам в ногу, теряете 3 очка Здоровья."
        $ health -= 3
        s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
        if health <=0:
            jump game_over
    if dice == 4:
        e "Стрела попала вам в плечо, теряете 2 очка Здоровья."
        $ health -= 2
        s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
        if health <=0:
            jump game_over
    if dice == 5:
        e "Стрела попала вам в правую руку, теряете 1 очко Здоровья и 2 очка Мастерства."
        $ health -= 1
        s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
        if health <=0:
            jump game_over
        $ mastery -= 2
        s "Теперь ваш уровень мастерства - {color=#FF00FF}[mastery]{/color}"
    if dice == 6:
        e "Стрела пролетела мимо"
    e "Вы вступаете в бой с Вангорном"
    $ current_enemy = {"name": "凡戈恩", "mastery": 7, "health": 8} # Вангорн
    jump choice_13_fight

label choice_13_fight:
    if health <= 0:
        f "Твои силы иссякли в бою с [current_enemy['name']]! Ты падаешь, побежденный его метким выстрелом."
        jump game_over

    if current_enemy["health"] <= 0:
        f "Вангорн отступает, тяжело дыша! Он мертв. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
        jump choice_105

    $ enemy_attack = renpy.random.randint(1, 12) + current_enemy["mastery"]
    $ player_attack = renpy.random.randint(1, 12) + mastery

    if enemy_attack == player_attack:
        f "Ты ([player_attack]) и [current_enemy['name']] ([enemy_attack]) атакуете одновременно, но оба уворачиваетесь! Никто не ранен. Твое здоровье: {color=#FF00FF}[health]{/color}, здоровье врага: {color=#FF00FF}[current_enemy['health']]{/color}."
        jump choice_13_fight

    elif enemy_attack < player_attack:
        $ current_enemy["health"] -= 2
        if current_enemy["health"] > 2:
            f "Твой удар ([player_attack]) пробивает защиту [current_enemy['name']] ([enemy_attack])! Ты наносишь 2 урона. У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твое здоровье: {color=#FF00FF}[health]{/color}."
            if current_enemy["health"] <= 3 and magicalSelfLockingChain == 1:
                menu:
                    "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить [current_enemy['name']]":
                        $ current_enemy["health"] = 2
                        $ magicalSelfLockingChain = 0
                        f "Ты метаешь волшебную цепь! Она обвивается вокруг [current_enemy['name']], обездвиживая его. Он теряет силы, осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Цепь использована, и ты не можешь её снять."
                        jump choice_13_fight
                    "Не использовать цепь":
                        pass
        else:
            f "Твой удар ([player_attack]) заставляет [current_enemy['name']] ([enemy_attack]) отступить! Он ослаб, осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твое здоровье: {color=#FF00FF}[health]{/color}."

        menu:
            "Использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 2:
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ current_enemy["health"] -= 2
                    $ luck -= 1
                    if current_enemy["health"] > 2:
                        f "Удача на твоей стороне! Ты наносишь [current_enemy['name']] дополнительный урон (2). У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                        if current_enemy["health"] <= 3 and magicalSelfLockingChain == 1:
                            menu:
                                "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить [current_enemy['name']]":
                                    $ current_enemy["health"] = 2
                                    $ magicalSelfLockingChain = 0
                                    f "Ты метаешь волшебную цепь! Она обвивается вокруг [current_enemy['name']], обездвиживая его. Он теряет силы, осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Цепь использована, и ты не можешь её снять."
                                    jump choice_13_fight
                                "Не использовать цепь":
                                    pass
                    else:
                        f "Удача помогает тебе! Дополнительный удар (2 урона) заставляет [current_enemy['name']] отступить! Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ current_enemy["health"] += 1
                    $ luck -= 1
                    f "Удача отвернулась! [current_enemy['name']] восстанавливает 1 здоровье (теперь {color=#FF00FF}[current_enemy['health']]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
            "Не использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 2:
                pass
        jump choice_13_fight

    else:
        $ health -= 2
        if health > 0:
            f "[current_enemy['name']] наносит тебе удар ([enemy_attack])! Твоя защита ([player_attack]) не справляется. Ты теряешь 2 здоровья, осталось {color=#FF00FF}[health]{/color}."
        else:
            f "[current_enemy['name']] наносит сокрушительный удар ([enemy_attack]) против твоей защиты ([player_attack])! Ты теряешь последние силы и падаешь."
            jump game_over

        menu:
            "Использовать удачу, чтобы смягчить урон":
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ health += 1
                    $ luck -= 1
                    f "Удача спасает тебя! Ты восстанавливаешь 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ health -= 1
                    $ luck -= 1
                    if health > 0:
                        f "Удача подвела! Ты теряешь дополнительное 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                    else:
                        f "Удача подвела, и ты теряешь последнее здоровье! [current_enemy['name']] добивает тебя."
                        jump game_over
        jump choice_13_fight

label choice_154:
    scene 66-1
    e "В конце концов, из задней комнаты выходит старик, с которым вы провели ночь в сторожке у ворот, и вглядывается в ваше лицо."
    show OldMan
    o "Ага, мой друг"
    o "Я вижу, вы попали в ловушку хозяина мастерской."
    o "Вам действительно повезло, что вас нашел я, а не он"
    e "Старик согласен вас освободить, но вы должны вернуть все украденное."
    e "Вы отдаете ему свою добычу, а он выпутывает вас из цепей."
    $ gold -= 10
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    $ magicalSelfLockingChain = 0
    s "Волшебной цепи у вас теперь нет."
    o "Вам лучше уйти"
    o "Пока хозяин не вернулся"
    i "Благодарю! Досвидания!"
    jump choice_9

label choice_313:
    scene 313-1 with dissolve
    pause 0.5
    e "Ваш тон пугает существо, оно отступает в угол, позволяя вам, взять коробку"
    jump choice_29

label choice_100:
    scene 43-1 with dissolve
    pause 0.5
    e "Пища – какое-то подозрительное мясо с гарниром из овощей - не слишком хороша на вкус, но питательна."
    e "Gища восстановит вам 2 очка Здоровья"
    $ health += 2
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    e "Существо кивает и предлагает вам кружку мутной жидкости, запить еду."
    e "Вы намеренно проливаете напиток, и ваш хозяин суетится, доставая тряпку, чтобы вытереть лужу."
    e "Это ваш шанс украсть ящик"
    jump choice_29

label choice_279:
    scene 279-1 with dissolve
    pause 0.5
    e "Кусочек заплесневелого козьего сыра падает вам под ноги."
    e "Запах ужасный."
    e "Вы можете выбросить его или взять с собой. Если вы хотите сохранить его, то должны потерять 1 очко Здоровья, пока он находится у вас."
    menu:
        "Взять":
            $ goatCheese += 1
            $ health -= 1
            s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
            if health <=0:
                jump game_over
            scene 240-1
            show BeardedMan
            e "Вы сердито поворачиваетесь к человеку"
            bem "Вам просто не повезло"
            e "Вы покидаете палатку и продолжаете свое путешествие"
            jump choice_160
        "Выбросить":
            scene 240-1
            show BeardedMan
            e "Вы сердито поворачиваетесь к человеку"
            bem "Вам просто не повезло"
            e "Вы покидаете палатку и продолжаете свое путешествие"
            jump choice_160

label choice_5:
    scene 5-1 with dissolve
    pause 0.5
    e "Из шкафа на землю у ваших ног выпадает кошелек."
    e "Вы открываете его и заглядываете внутрь, но там ничего нет."
    e "Вы берете его с собой"
    $ emptyWallet += 1
    e "Вскоре вы обнаружите, что он был не совсем пустым."
    e "Когда вы открыли его, семья блох переселилась вам в рукава и теперь обитает на вашем теле."
    e "Но вы не заметите этого, пока их укусы не начнут зудеть через некоторое время."
    e "Однако, это мелкое неудобство не составит для вас большой проблемы, вы покидаете палатку и продолжаете свой путь"
    jump choice_160

label choice_167:
    scene 167-1 with dissolve
    pause 0.5
    e "Вы получили талисман удачи. Он прибавляет 5 очков к уровню соответствующего показателя"
    $ luck += 5
    $ goodLuckCharm = 1
    s "Теперь уровень вашей удачи - {color=#FF00FF}[luck]{/color}"
    e "Теперь вы можете покинуть палатку"
    jump choice_160

label choice_92:
    scene 92-1 with dissolve
    pause 0.5
    e "К вашим ногам падает маленькая сумка, внутри вы находите манжету, к которой прикреплены два маленьких метательных дротика."
    $ cuffWithDarts += 2
    e "Данное оружие прибавляет 3 очка к вашему мастерству"
    $ mastery += 3
    s "Теперь ваш уровень мастерства - {color=#FF00FF}[mastery]{/color}"
    e "Вы покидаете палатку"
    jump choice_160

label choice_71:
    scene 71-1 with dissolve
    pause 0.5
    $ braceletBones += 1
    e "Из шкафа выпадает маленький браслет. Вы берете его и крутите в руках."
    e "Он сделан из костяшек пальцев гнома и может быть полезен при наложении заклинаний."
    e "Вы кладете его в рюкзак и покидаете палатку"
    jump choice_160

label choice_219:
    scene 219-1 with dissolve
    pause 0.5
    e "Красное яблоко падает из шкафа вам под ноги."
    e "Оно очень красивое и спелое, вы кладете его в рюкзак вместе с другой едой."
    e "Тем не менее, внутри яблоко гнилое. В следующий раз, когда вы откроете свой рюкзак, чтобы поесть, вы обнаружите, что оно не только сгнило само, но и испортило одну порцию пищи"
    if meal > 0:
        $ meal -= 1
        s "Теперь количество вашей еды - {color=#FF00FF}[meal]{/color}"
    e "Вы покидаете палатку и продолжаете свое путешествие"
    jump choice_160

label choice_131:
    scene 131-1 with dissolve
    pause 0.5
    e "Улица заканчивается на пересечении с другой. Повернув направо, вы направляетесь к центру Кхара"
    jump choice_165

label choice_139:
    scene 139-1 with dissolve
    pause 0.5
    e "Следуя по этой улице, вы подходите к небольшой часовне. По шуму, доносящемуся изнутри, вы можете догадаться, что там происходит какая-то встреча."
    menu:
        "Заглянуть внутрь":
            jump choice_187
        "Пройти мимо":
            jump choice_165

label choice_110:
    scene 110-1 with dissolve
    pause 0.5
    e "Таверна «Отдых путника» — это шумное людное место, и никто не обращает на вас особого внимания."
    e "Трактирщик стоит за стойкой и пытается вовремя обслужить множество клиентов, постоянно требующих своего эля."
    e "Таверна, очевидно, служит местом встречи для моряков из порта и девушек с пониженной социальной ответственностью"
    e "Повсюду за столами хохочут и горланят песни просоленные волнами типы и пышные девки"
    e "Вам удается привлечь внимание трактирщика."
    show Innkeeper
    e "Это угрюмый лысый тип, привыкший иметь дело с отбросами из доков, его удивляет ваша одежда и вежливые манеры."
    inn "И какое же дело привело вас в эти места?"
    i "Ищу место для ночлега, а возможно и ужин. Какова цена?"
    inn "Комната наверху обойдется в 4 золотых"
    inn "И хорошая кормежка еще в 4"
    menu:
        "Поужинать здесь и переночевать" if gold >= 8:
            jump choice_331
        "Просто лечь спать" if gold >= 4:
            jump choice_282
        "Ни спать и ни есть":
            jump choice_68

label choice_187:
    scene 139-1
    e "У входа в часовню вы сталкиваетесь с женщиной и ребенком, выходящими наружу."
    show WomanWithChild
    wwc "Он действительно святой"
    wwc "Брат Салена – тот, что хромой - ответил на его вопрос вчера, и его нога исцелилась!"
    wwc "Он побежал впервые за всю свою жизнь!"
    e "Заинтригованный вы входите в зал собраний."
    e "Взрослые и дети сидят здесь на полу, в конце зала на возвышении стоит и проповедует перед толпой седой человек в белом балахоне."
    bs "Кто-нибудь еще желает пройти испытание Слангга?"
    bs "Если вы сможете ответить на вопрос, он исполнит любое ваше желание."
    bs "Если не сможете, вы должны отречься от своих богов и поклоняться только ему – Сланггу, Богу Злобы"
    menu:
        "Принять вызов":
            jump choice_156
        "Уйти":
            jump choice_165

label choice_228:
    scene 149-1
    e "В кольчужных перчатках вы чувствуете странную уверенность в своих силах, а ваше оружие кажется вам легче в руке."
    e "Вы уверены, что ваши навыки боя улучшатся с этими перчатками, но это только магическая иллюзия, на самом деле ваш боевой навык уменьшится."
    e "Вы поняли, что перчатки прокляты и выбросили их."
    $ chainmailGloves = 0
    if bottleDust >= 1:
        jump choice_247
    else:
        jump choice_259

label choice_238:
    scene 149-1
    e "Вы купили оружейные перчатки, которые наделены магической силой и помогают своему владельцу в трудные времена."
    e "Ваше здоровье увеличивается на 5 единиц"
    $ health += 5
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    if bottleDust >= 1:
        jump choice_247
    else:
        jump choice_259

label choice_247:
    scene 149-1
    e "Пыль внутри купленного вами флакона — это не пыль, а песчинки."
    jump choice_259

label choice_259:
    scene 149-1
    if bottleWithTheInscription >= 1:
        jump choice_281
    else:
        jump choice_170

label choice_55:
    scene 37-1
    e "Вы делаете шаг назад, и статуя оживает!"
    e "Длинные руки стремительно выбрасываются в вашу сторону и пытаются схватить вас."
    e "Это смертельно опасный Человек-Богомол."
    e "Если он схватит вас, то вырваться из его шипастых ладоней будет невозможно, он подтянет вас к себе, и его острые зубы убьют вас за секунду."
    e "Тем не менее, вы можете атаковать его руки, и если перерубите их, он станет беспомощен."
    $ current_enemy = {"name": "螳螂人", "mastery": 6, "health": 5} # Человек-Богомол
    jump choice_55_fight

label choice_55_fight:
    if health <= 0:
        f "Твои силы иссякли в бою с [current_enemy['name']]! Его шипастые лапы сжимают тебя, и ты падаешь."
        jump game_over

    if current_enemy["health"] <= 0:
        f "Человек-Богомол повержен! Ты стоишь над его неподвижным телом, тяжело дыша. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
        jump choice_117

    $ enemy_attack = renpy.random.randint(1, 12) + current_enemy["mastery"]
    $ player_attack = renpy.random.randint(1, 12) + mastery

    if enemy_attack == player_attack:
        f "Ты ([player_attack]) и [current_enemy['name']] ([enemy_attack]) атакуете одновременно, но оба уворачиваетесь! Никто не ранен. Твое здоровье: {color=#FF00FF}[health]{/color}, здоровье врага: {color=#FF00FF}[current_enemy['health']]{/color}."
        jump choice_55_fight

    elif enemy_attack < player_attack:
        $ current_enemy["health"] -= 2
        if current_enemy["health"] > 0:
            f "Твой удар ([player_attack]) пробивает защиту [current_enemy['name']] ([enemy_attack])! Ты наносишь 2 урона. У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твое здоровье: {color=#FF00FF}[health]{/color}."
            if current_enemy["health"] <= 3 and magicalSelfLockingChain == 1:
                menu:
                    "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить [current_enemy['name']]":
                        $ current_enemy["health"] = 0
                        $ magicalSelfLockingChain = 0
                        f "Ты метаешь волшебную цепь! Она обвивается вокруг [current_enemy['name']], обездвиживая его. Ты наносишь решающий удар, и [current_enemy['name']] повержен! Цепь использована, и ты не можешь её снять."
                        jump choice_117
                    "Не использовать цепь":
                        pass
        else:
            f "Твой мощный удар ([player_attack]) сокрушает [current_enemy['name']] ([enemy_attack])! Враг повержен! Твое здоровье: {color=#FF00FF}[health]{/color}."

        menu:
            "Использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ current_enemy["health"] -= 2
                    $ luck -= 1
                    if current_enemy["health"] > 0:
                        f "Удача на твоей стороне! Ты наносишь [current_enemy['name']] дополнительный урон (2). У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                        if current_enemy["health"] <= 3 and magicalSelfLockingChain == 1:
                            menu:
                                "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить [current_enemy['name']]":
                                    $ current_enemy["health"] = 0
                                    $ magicalSelfLockingChain = 0
                                    f "Ты метаешь волшебную цепь! Она обвивается вокруг [current_enemy['name']], обездвиживая его. Ты наносишь решающий удар, и [current_enemy['name']] повержен! Цепь использована, и ты не можешь её снять."
                                    jump choice_117
                                "Не использовать цепь":
                                    pass
                    else:
                        f "Удача помогает тебе! Мощный дополнительный удар (2 урона) добивает [current_enemy['name']]! Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                        jump choice_117
                else:
                    $ current_enemy["health"] += 1
                    $ luck -= 1
                    f "Удача отвернулась! [current_enemy['name']] восстанавливает 1 здоровье (теперь {color=#FF00FF}[current_enemy['health']]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
            "Не использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                pass
        jump choice_55_fight

    else:
        $ health -= 2
        if health > 0:
            f "[current_enemy['name']] наносит тебе удар ([enemy_attack])! Твоя защита ([player_attack]) не справляется. Ты теряешь 2 здоровья, осталось {color=#FF00FF}[health]{/color}."
        else:
            f "[current_enemy['name']] наносит сокрушительный удар ([enemy_attack]) против твоей защиты ([player_attack])! Ты теряешь последние силы и падаешь."
            jump game_over

        menu:
            "Использовать удачу, чтобы смягчить урон":
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ health += 1
                    $ luck -= 1
                    f "Удача спасает тебя! Ты восстанавливаешь 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ health -= 1
                    $ luck -= 1
                    if health > 0:
                        f "Удача подвела! Ты теряешь дополнительное 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                    else:
                        f "Удача подвела, и ты теряешь последнее здоровье! [current_enemy['name']] добивает тебя."
                        jump game_over
        jump choice_55_fight

label choice_76:
    jump choice_55

label choice_84:
    scene 292-1 with dissolve
    pause 0.5
    e "Скоро вы выходите на очередную развилку."
    menu:
        "Повернуть налево":
            jump choice_57
        "Пойти прямо":
            jump choice_322

label choice_229:
    scene 140-2
    show Magician
    e "Вы отдаете ему оружие и, похоже, этот поступок искренне располагает его к вам."
    m "Я - Лортаг Старший, ученый и исследователь, и приглашаю вас в мой кабинет"
    jump choice_336

label choice_95:
    scene 140-2
    show Magician
    e "Мужчина отступает назад и дает команду своему домашнему питомцу."
    hide Magician
    pause 1
    show Lizard
    e "Шипастый зверь обнажает острые зубы и прыгает на вас."
    $ current_enemy = {"name": "多刺怪兽", "mastery": 5, "health": 7} # Шипастый Зверь
    jump choice_95_fight

label choice_95_fight:
    if health <= 0:
        f "Твои силы иссякли в бою с [current_enemy['name']]! Его острые зубы и шипы одолевают тебя, и ты падаешь."
        jump game_over

    if current_enemy["health"] <= 0:
        f "Шипастый Зверь повержен! Ты стоишь над его неподвижным телом, тяжело дыша. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
        jump choice_14

    $ enemy_attack = renpy.random.randint(1, 12) + current_enemy["mastery"]
    $ player_attack = renpy.random.randint(1, 12) + mastery

    if enemy_attack == player_attack:
        f "Ты ([player_attack]) и [current_enemy['name']] ([enemy_attack]) атакуете одновременно, но оба уворачиваетесь! Никто не ранен. Твое здоровье: {color=#FF00FF}[health]{/color}, здоровье врага: {color=#FF00FF}[current_enemy['health']]{/color}."
        jump choice_95_fight

    elif enemy_attack < player_attack:
        $ current_enemy["health"] -= 2
        if current_enemy["health"] > 0:
            f "Твой удар ([player_attack]) пробивает защиту [current_enemy['name']] ([enemy_attack])! Ты наносишь 2 урона. У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твое здоровье: {color=#FF00FF}[health]{/color}."
            if current_enemy["health"] <= 3 and magicalSelfLockingChain == 1:
                menu:
                    "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить [current_enemy['name']]":
                        $ current_enemy["health"] = 0
                        $ magicalSelfLockingChain = 0
                        f "Ты метаешь волшебную цепь! Она обвивается вокруг [current_enemy['name']], обездвиживая его. Ты наносишь решающий удар, и [current_enemy['name']] повержен! Цепь использована, и ты не можешь её снять."
                        jump choice_14
                    "Не использовать цепь":
                        pass
        else:
            f "Твой мощный удар ([player_attack]) сокрушает [current_enemy['name']] ([enemy_attack])! Враг повержен! Твое здоровье: {color=#FF00FF}[health]{/color}."

        menu:
            "Использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ current_enemy["health"] -= 2
                    $ luck -= 1
                    if current_enemy["health"] > 0:
                        f "Удача на твоей стороне! Ты наносишь [current_enemy['name']] дополнительный урон (2). У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                        if current_enemy["health"] <= 3 and magicalSelfLockingChain == 1:
                            menu:
                                "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить [current_enemy['name']]":
                                    $ current_enemy["health"] = 0
                                    $ magicalSelfLockingChain = 0
                                    f "Ты метаешь волшебную цепь! Она обвивается вокруг [current_enemy['name']], обездвиживая его. Ты наносишь решающий удар, и [current_enemy['name']] повержен! Цепь использована, и ты не можешь её снять."
                                    jump choice_14
                                "Не использовать цепь":
                                    pass
                    else:
                        f "Удача помогает тебе! Мощный дополнительный удар (2 урона) добивает [current_enemy['name']]! Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                        jump choice_14
                else:
                    $ current_enemy["health"] += 1
                    $ luck -= 1
                    f "Удача отвернулась! [current_enemy['name']] восстанавливает 1 здоровье (теперь {color=#FF00FF}[current_enemy['health']]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
            "Не использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                pass
        jump choice_95_fight

    else:
        $ health -= 2
        if health > 0:
            f "[current_enemy['name']] наносит тебе удар ([enemy_attack])! Твоя защита ([player_attack]) не справляется. Ты теряешь 2 здоровья, осталось {color=#FF00FF}[health]{/color}."
        else:
            f "[current_enemy['name']] наносит сокрушительный удар ([enemy_attack]) против твоей защиты ([player_attack])! Ты теряешь последние силы и падаешь."
            jump game_over

        menu:
            "Использовать удачу, чтобы смягчить урон":
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ health += 1
                    $ luck -= 1
                    f "Удача спасает тебя! Ты восстанавливаешь 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ health -= 1
                    $ luck -= 1
                    if health > 0:
                        f "Удача подвела! Ты теряешь дополнительное 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                    else:
                        f "Удача подвела, и ты теряешь последнее здоровье! [current_enemy['name']] добивает тебя."
                        jump game_over
        jump choice_95_fight

label choice_172:
    scene 208-1
    e "Вы подкрадываетесь к задней части дома."
    e "Когда вы подходите к двери, она внезапно открывается, и перед вами появляется пожилой мужчина в темном платье."
    show Magician
    e "Его домашнее животное, похожее на покрытую шипами ящерицу стоит у его ног."
    m "Почему вы нарушили границы моего сада?!"
    i "Я уже стучался во входную дверь и думал, что дома никого нет."
    e "Убедительность вашей лжи зависит от вашего мастерства"
    $ twodice = renpy.random.randint(1, 20)
    s "Уровень вашего мастерства - {color=#FF00FF}[mastery]{/color}, требуемый уровень мастерства - {color=#FF00FF}[twodice]{/color}"
    if twodice <= mastery:
        s "Ваше мастерство позволило сделать задуманное!"
        jump choice_53
    else:
        s "Ваше мастерство не позволило сделать задуманное!"
        jump choice_194

label choice_3:
    scene 133-1
    e "Работы двух ремесленников вас особенно заинтересовали"
    e "Первый – художник без рук, который выставил на продажу серию портретов"
    e "Второй – заклинатель огня, показывающий огненные узоры всех цветов и оттенков."
    menu:
        "Посмотреть работы художника":
            jump choice_18
        "Посмотреть на огненное представление":
            jump choice_96

label choice_120:
    scene 62-1 with dissolve
    pause 0.5
    e "Пройдя до конца улицы, вы попадаете на развилку."
    menu:
        "Продолжить путь прямо":
            jump choice_60
        "Повернуть налево":
            jump choice_139

label choice_129:
    scene 57-2
    show BlackManDead
    e "Вы падаете на пол и теряете сознание, из последних сил произнося слова своей молитвы."
    e "Через некоторое время вы открываете глаза."
    e "Убийца лежит на земле мертвым."
    e "Вы не представляете, что произошло, но уверены в одном; это дело рук вашей доброй богини."
    e "Но теперь вы не можете воззвать к ней снова, пока не покинете этот город"
    jump choice_105

label choice_105:
    scene 57-2
    show BlackManDead
    e "Вы обшариваете карманы убитого и находите 8 золотых."
    $ gold += 8
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    e "В комнате мало ценного, но вы находите две стеклянные банки, одна помечена как «Яд», вторая как «Духи Эссенция Коры»."
    e "Вы берете их с собой"
    $ spirits += 1
    $ poison += 1
    e "Затем вы покидаете дом"
    jump choice_46

label choice_82:
    scene 82-1 with dissolve
    pause 0.5
    e "Ваш вызов принят."
    e "Толпа рукоплещет вам, когда вы занимаете место в белом углу."
    play sound "audio/33-1.mp3"
    pause 2
    e "Вы уверены, что сможете победить чемпиона, предыдущий поединок должен был сильно ослабить его."
    e "Но когда вы смотрите в черный угол, ваше сердце на мгновение замирает."
    e "Пройдоха зазывала успел тайком наложить на вашего противника исцеляющее заклинание, его силы полностью восстановлены."
    menu:
        "Воззвать к Либре" if kharLibra == 0:
            jump choice_70
        "Начать бой своими силами":
            jump choice_323

label choice_331:
    scene 110-1
    hide Innkeeper
    $ gold -= 8
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    e "Вы платите трактирщику за ужин, и он исчезает в задней комнате, чтобы вернуться с большой тарелкой дымящейся пищи."
    show Innkeeper
    inn "Вот, пожалуйста"
    inn "и есть еще, если вам понадобится добавка"
    e "Вы берете тарелку, садитесь за стол и начинаете есть."
    $ health += 2
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    hide Innkeeper
    show Sailor
    e "К вам подходит разбойничьего вида матрос и садится напротив вас."
    e "Он пытается завести разговор, но вы уделяете все внимание еде."
    sa "Может быть кружку эля?"
    i "Давай!"
    e "Вы заканчиваете есть и приступаете к элю, восстановите еще 1 очко Здоровья."
    $ health += 1
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    sa "Что ты забыл в этой дыре?"
    i "Я ищу заклинание отворяющие ворота на север."
    sa "Ну ладно, как хочешь"
    sa "Но все-таки, если не умеешь убивать нежить, то это безнадежное дело. Как ещё насчет эля?"
    menu:
        "Принять предложение и продолжить беседу":
            jump choice_253
        "Отправиться спать":
            jump choice_86

label choice_282:
    scene 282-1 with dissolve
    pause 0.5
    e "Заплатив, вы поднимаетесь по лестнице в отведенную вам комнату."
    e "Она темная и вам не дали свечи, поэтому приходится искать кровать на ощупь, прежде чем сесть на нее."
    menu:
        "Принять пищу и лечь спать" if meal >= 1:
            $ meal -= 1
            s "Теперь количество вашей еды - {color=#FF00FF}[meal]{/color}"
            e "Уровень вашего здоровья увеличивется на 2 единицы"
            $ health += 2
            s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
            jump choice_227
        "Просто лечь спать":
            jump choice_227

label choice_68:
    scene 68-1 with dissolve
    pause 0.5
    e "Вы выходите из таверны и бродите вокруг по улице, присматривая себе место для ночлега."
    menu:
        "Устроиться в темном переулке позади таверны":
            jump choice_94
        "Бодрствовать всю ночь":
            jump choice_159

label choice_156:
    scene 187-1
    e "Вы вскидываете руку в знак того, что принимаете вызов."
    bs "И кто твой бог, незнакомец?"
    i "Либра, Богиня Правосудия"
    bs "Я ничего не знаю о ней"
    bs "Но вы найдете Слангга гораздо более могущественным божеством."
    bs "Давайте посмотрим, сможет ли Либра помочь вам с испытанием Слангга."
    bs "Если вы правильно ответите на мой вопрос, то сможете спросить у меня что угодно."
    bs "Но если не сможете, вам придется отказаться от поклонения Либре и стать последователем Слангга."
    bs "Вы согласны?"
    e "Вы киваете"
    bs "Старейшина Большеног прошел на юг три четверти мили, чтобы посеять овес, затем на восток еще полмили, чтобы посеять кукурузу"
    bs "а затем на север милю с четвертью, чтобы посеять пшеницу, и, наконец, милю на юго-запад, чтобы скосить сена. Вы поняли это?"
    bs "А теперь вопрос"
    jump choice_301

label choice_281:
    scene 149-1
    e "Вы глотаете зелье и ждете, что случится. У вас кружится голова, и вы падаете в обморок."
    scene 281-1 with dissolve
    pause 0.5
    e "Когда вы просыпаетесь и осматриваетесь по сторонам, то понимаете, что лежите на улице совсем в другом районе"
    e "Прохожие смотрят на вас с удивлением"
    jump choice_294

label choice_117:
    scene 117-1 with dissolve
    pause 0.5
    e "Вы срываете с шеи существа золотой медальон. Он стоит 8 золотых монет."
    $ gold += 8
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    e "Внутри медальона находится маленькая солнечная жемчужина, желтый камень, который ярко светится своим собственным светом."
    e "Восстановите 1 очко Удачи за то, что уцелели в этой битве, и продолжите свое путешествие"
    $ luck += 1
    s "Теперь уровень вашей удачи - {color=#FF00FF}[luck]{/color}"
    jump choice_137

label choice_336:
    scene 336-1 with dissolve
    pause 0.5
    e "Вы следуете за ним в кабинет, элегантную комнату, в которой все место вдоль стен от пола до полка занимают книжные полки."
    show MagicianNoLizard
    m "Я ученый. В данный момент я увлечен педагогикой"
    m "Я прожил славную жизнь, и он хочет потратить оставшиеся ему годы на то, чтобы помочь понемногу цивилизовать этот город."
    e "Похоже, что он может помочь вам в ваших поисках"
    i "Знаете ли вы что-нибудь о заклинании, открывающем северные ворота?"
    m "Действительно, я знаю одну из строк этого заклинания"
    m "И я с радостью скажу ее вам, если вы сможете помочь мне с одной проблемой"
    i "Я сделаю всё, что в моих силах!"
    m "Недавно я пытался расшифровать некоторые руны."
    m "Я работаю над этой проблемой, но теперь я застрял, потому что я не знаю, точную последовательность рун."
    m "Какая из них, по вашему мнению, должна быть следующей?"
    e "Вы немного разбираетесь в рунах и внимательно изучаете эту проблему."
    scene 336-2 with dissolve
    pause 0.5
    e "Посмотрите на изображенную последовательность на иллюстрации и выберите руну, которая, по вашему мнению, должна быть следующей."
    e "..."
    menu:
        "Руна 1":
            jump choice_115
        "Руна 2":
            jump choice_255
        "Руна 3":
            jump choice_274
        "Руна 4":
            jump choice_72

label choice_14:
    scene 140-1 with dissolve
    pause 0.5
    play sound "audio/14-1.mp3"
    pause 1
    e "Когда вы побеждаете зверя, его хозяин захлопывает дверь. Пытаетесь открыть ее, но она крепко заперта."
    e "Вы не можете войти и потому уходите"
    $ block61and140 = 1
    jump choice_133

label choice_53:
    scene 208-1
    show Magician
    m "Мой слух с возрастом стал хуже."
    m "Вы должны меня извинить, вполне естественно с подозрением относится к незнакомцам в таком месте, как Кхар."
    m "Если вы отдадите свое оружие, я буду рад видеть вас в своем доме"
    s "Повторно оказаться на данной локации будет невозможно"
    $ block61and140 = 1
    menu:
        "Передать свое оружие ему и войти":
            jump choice_229
        "Уйти":
            jump choice_133

label choice_194:
    scene 208-1
    show Magician
    m "Я вам не верю!"
    i "Пустите меня! Я готов отдать вам свое оружие!"
    m "Я не хочу вас видеть!"
    $ block61and140 = 1
    jump choice_95

label choice_18:
    scene 18-1 with dissolve
    pause 0.5
    e "На портретах художника изображены различные аристократы и знатные жители Кхара."
    i "Как можно рисовать без рук?"
    pa "Я делаю это с помощью волшебной кисти"
    pa "Даже сейчас я использую кисть внутри своей хижины"
    menu:
        "Зайти в дом художника, чтобы увидеть его нынешнее творение":
            jump choice_176
        "Посмотреть выступление заклинателя огня":
            jump choice_96

label choice_96:
    scene 96-1 with dissolve
    pause 0.5
    i "Приветствую тебя, заклинатель огня!"
    fc "Надеюсь, что вам понравятся мои огни!"
    e "Он показывает вам прекрасное белое, зеленое, синее и черное пламя."
    e "Он способен создавать маленькие огни всех этих цветов, помещая особые камни соответствующего цвета в пламя."
    e "Вы впечатлены, его творения, безусловно, прекрасны, но они малополезны для вас."
    fc "Возможно, вас заинтересует один из моих особых огней"
    fc "Загляните внутрь"
    menu:
        "Зайти в его хижину":
            jump choice_108
        "Пойти посмотреть на картины художника":
            jump choice_18

label choice_60:
    jump choice_165

label choice_46:
    scene 46-1 with dissolve
    pause 0.5
    e "Продолжая идти по улице, вы выходите на очередную развилку."
    menu:
        "Повернуть налево":
            jump choice_131
        "Повернуть направо":
            jump choice_60
        "Продолжить путь прямо":
            jump choice_139

label choice_70:
    scene 82-1
    $ kharLibra = 1
    e "Вы безмолвно молите Либру о помощи."
    e "Вы не ощущаете ее присутствие, но она будет рядом с вами в этой битве."
    e "Ваша первая успешная атака в том бою мгновенно убила чемпиона"
    e "Но помните, что теперь вы не сможете воззвать к Либре, пока не покинете Кхар."
    e "За победу вы получаете 15 золотых"
    $ gold += 15
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    jump choice_263

label choice_323:
    scene 82-1
    e "Бой начался! Огромный огр, местный чемпион, выходит на ринг, сжимая массивную дубину. Его глаза горят яростью, и толпа ревет от восторга."
    play sound "audio/33-1.mp3"
    pause 2
    $ current_enemy = {"name": "食人魔", "mastery": 9, "health": 12} # Огр
    jump choice_323_fight

label choice_323_fight:
    if health <= 0:
        f "Твои силы иссякли в бою с [current_enemy['name']]! Его сокрушительная дубина повергает тебя на землю."
        jump game_over

    if current_enemy["health"] <= 0:
        f "Огр повержен! Ты стоишь над его массивным телом, тяжело дыша. Толпа замолкает, поражённая твоей победой. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
        e "За победу ты получаешь 15 золотых"
        $ gold += 15
        s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
        jump choice_263

    $ enemy_attack = renpy.random.randint(1, 12) + current_enemy["mastery"]
    $ player_attack = renpy.random.randint(1, 12) + mastery

    if enemy_attack == player_attack:
        f "Ты ([player_attack]) и [current_enemy['name']] ([enemy_attack]) атакуете одновременно, но оба уворачиваетесь! Никто не ранен. Твое здоровье: {color=#FF00FF}[health]{/color}, здоровье врага: {color=#FF00FF}[current_enemy['health']]{/color}."
        jump choice_323_fight

    elif enemy_attack < player_attack:
        $ current_enemy["health"] -= 2
        if current_enemy["health"] > 0:
            f "Твой удар ([player_attack]) пробивает защиту [current_enemy['name']] ([enemy_attack])! Ты наносишь 2 урона. У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твое здоровье: {color=#FF00FF}[health]{/color}."
            if current_enemy["health"] <= 3 and magicalSelfLockingChain == 1:
                menu:
                    "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить [current_enemy['name']]":
                        $ current_enemy["health"] = 0
                        $ magicalSelfLockingChain = 0
                        f "Ты метаешь волшебную цепь! Она обвивается вокруг [current_enemy['name']], обездвиживая его. Ты наносишь решающий удар, и [current_enemy['name']] повержен! Цепь использована, и ты не можешь её снять."
                        jump choice_263
                    "Не использовать цепь":
                        pass
        else:
            f "Твой мощный удар ([player_attack]) сокрушает [current_enemy['name']] ([enemy_attack])! Враг повержен! Твое здоровье: {color=#FF00FF}[health]{/color}."

        menu:
            "Использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ current_enemy["health"] -= 2
                    $ luck -= 1
                    if current_enemy["health"] > 0:
                        f "Удача на твоей стороне! Ты наносишь [current_enemy['name']] дополнительный урон (2). У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                        if current_enemy["health"] <= 3 and magicalSelfLockingChain == 1:
                            menu:
                                "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить [current_enemy['name']]":
                                    $ current_enemy["health"] = 0
                                    $ magicalSelfLockingChain = 0
                                    f "Ты метаешь волшебную цепь! Она обвивается вокруг [current_enemy['name']], обездвиживая его. Ты наносишь решающий удар, и [current_enemy['name']] повержен! Цепь использована, и ты не можешь её снять."
                                    jump choice_263
                                "Не использовать цепь":
                                    pass
                    else:
                        f "Удача помогает тебе! Мощный дополнительный удар (2 урона) добивает [current_enemy['name']]! Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                        jump choice_263
                else:
                    $ current_enemy["health"] += 1
                    $ luck -= 1
                    f "Удача отвернулась! [current_enemy['name']] восстанавливает 1 здоровье (теперь {color=#FF00FF}[current_enemy['health']]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
            "Не использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                pass
        jump choice_323_fight

    else:
        $ health -= 2
        if health > 0:
            f "[current_enemy['name']] наносит тебе удар ([enemy_attack])! Твоя защита ([player_attack]) не справляется. Ты теряешь 2 здоровья, осталось {color=#FF00FF}[health]{/color}."
        else:
            f "[current_enemy['name']] наносит сокрушительный удар ([enemy_attack]) против твоей защиты ([player_attack])! Ты теряешь последние силы и падаешь."
            jump game_over

        menu:
            "Использовать удачу, чтобы смягчить урон":
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ health += 1
                    $ luck -= 1
                    f "Удача спасает тебя! Ты восстанавливаешь 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ health -= 1
                    $ luck -= 1
                    if health > 0:
                        f "Удача подвела! Ты теряешь дополнительное 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                    else:
                        f "Удача подвела, и ты теряешь последнее здоровье! [current_enemy['name']] добивает тебя."
                        jump game_over
        jump choice_323_fight

label choice_253:
    scene 110-1
    show Sailor
    e "Он покупает вам еще по кружке эля, и вы распиваете их."
    e "Восстановите еще 2 очка Здоровья."
    $ health += 2
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    e "Сейчас вы в довольно приподнятом настроении и оба хохочете во все горло."
    e "Ваш собеседник хорошо знает город, и вы стараетесь выжать из него побольше дополнительной информации"
    i "Что ты знаешь о хранителях строк заклинания?"
    sa "Я мало про них знаю, но есть слух, что один из хранителей, недавно потерял благосклонность Третьего Архонта Кхара и теперь проклят живой смертью"
    sa "Говорят, что Третий Архонт Кхара - вампир"
    sa "Один мой друг пытался поговорить с богом Кургой и был убит в его храме за то, что осмелился поцеловать в щеку статую божества."
    sa "Выпьем еще?"
    menu:
        "Согласитесь на его предложение и купите еще по кружке":
            jump choice_306
        "Отправитесь спать":
            jump choice_86

label choice_86:
    scene 110-1
    show Innkeeper
    menu:
        "Заплатить трактирщику 4 золотых, вы отправляетесь в свою комнату" if gold >= 4:
            $ gold -= 4
            s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
            jump choice_282
        "Переночевать на улице":
            jump choice_68

label choice_227:
    scene 227-1 with dissolve
    pause 0.5
    e "Вам снится странный сон, как будто вас схватил палач с садистским воображением"
    e "Который замышляет для вас всевозможные ужасные пытки и казни."
    scene 227-2 with dissolve
    pause 0.5
    e "Вы с криком просыпаетесь весь в холодном поту."
    e "Над вашей головой вы видите то, что заставляет вашу кровь застыть в жилах."
    e "Вы привязаны к кровати кожаными шнурками, а над шеей у вас висит острое и тяжелое лезвие для гильотины!"
    play sound "audio/227-1.mp3"
    pause 3
    e "Смех у кровати привлекает ваше внимание, и, повернув голову, вы смотрите прямо в прищуренные глаза трактирщика."
    show EvilInnkeeper
    pause 3
    hide EvilInnkeeper
    e "Похоже, он охотится за мясом для сегодняшнего рагу, и вы попали в меню."
    e "Возможно, он не любит убивать самостоятельно или просто наслаждается длительными страданиями"
    e "По какой-то причине он дает вам шанс на спасение, указывая на шнур, закрепленный на вашем левом запястье."
    e "Он развязывает шнур, вкладывает свободный конец вам в ладонь, и вы чувствуете тяжесть в руке."
    e "Можете потянуть за него или отпустить."
    e "Один выбор означает вашу смерть, другое решение поднимет лезвие и позволит вам сесть и освободиться."
    e "Очевидно, что трактирщик совершенно безумен, и никакой помощи от него не дождешься."
    menu:
        "Потянуть шнур":
            jump choice_211
        "Отпустить шнур":
            jump choice_15

label choice_94:
    scene 68-1
    e "Вы сворачиваетесь калачиком в углу и собираетесь заснуть."
    menu:
        "Перекусть на ночь" if meal >= 1:
            $ meal -= 1
            $ health += 2
            s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
            e "Посреди ночи вас будит звук шагов поблизости."
            e "Прежде чем успеваете понять, что происходит, вы получаете удар по голове и теряете сознание"
            jump choice_312
        "Лечь спать не перекусывая.":
            e "Посреди ночи вас будит звук шагов поблизости."
            e "Прежде чем успеваете понять, что происходит, вы получаете удар по голове и теряете сознание"
            jump choice_312

label choice_159:
    scene 68-1
    e "Вы должны потерять 2 очка Выносливости из-за того, что не спали всю ночь."
    $ health -= 2
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    if health <=0:
        jump game_over
    e "На рассвете вы продолжаете свое путешествие"
    jump choice_267

label choice_301:
    scene 187-1
    bs "А вопрос…"
    e "Жрец берет эффектную паузу. Напряжение растет, все зрители затаили дыхание."
    bs "А вопрос… Какой у него любимый цвет?"
    i "Я возмущен таким дурацким вопросом"
    i "Это не справедливо!"
    play sound "audio/301-1.mp3"
    pause 3
    e "Растерянно улыбаясь, вы понимаете, что попались на его шуточку, видимо, это его стандартный трюк."
    e "Он, безусловно, настоящий шоумен этот жрец."
    bs "Хорошо, аналэндец"
    e "Вы поражены. Как он узнал, что вы из Аналэнда?"
    bs "В семье Большенога шесть сыновей."
    bs "Старик чувствует приближение смерти и решает разделить свое богатство между сыновьями."
    bs "Он дает 5 золотых своему второму из самых младших сыновей, 13 своему старшему и 9 четвертому из самых младших."
    bs "Сколько всего у него было золотых монет?"
    $ ans = renpy.input("请输入正确答案！")
    $ ans = ans.strip()
    if (ans.isdigit() or (ans.startswith("-") and ans[1:].isdigit())) and ans == "48":
        e "Ответ верный!"
        jump choice_48
    if (ans.isdigit() or (ans.startswith("-") and ans[1:].isdigit())) and ans != "48":
        e "Ответ не верный!"
        jump choice_248
    else:
        s "Ошибка: введите корректное целое число!"
        jump choice_301

label choice_115:
    scene 336-1
    show MagicianNoLizard
    m "Хмм, дайте мне посмотреть"
    m "Нет, я не думаю, что это правильно."
    m "Я уже пробовал эту руну, и она не имеет смысла."
    m "Не берите в голову."
    m "В любом случае, спасибо за попытку."
    m "Вам уже пора идти."
    m "Я получил удовольствие от нашей беседы и желаю вам удачи в вашем путешествии."
    m "Возможно, это поможет вам, в этом городе нелюди часто знают больше, чем люди, поэтому этот подарок может быть вам полезен"
    e "Он протягивает вам маленькую сумочку с чем-то зеленым внутри."
    e "Вы вытаскиваете это и обнаруживаете, что это парик, который может быть полезен при наложении заклинаний."
    $ wig += 1
    e "Поблагодарив его, вы решаете поспешить и уходите, не забыв забрать оружие на выходе."
    e "Ваша удача восстанавливается до исходного уровня"
    $ luck = 12
    s "Теперь уровень вашей удачи - {color=#FF00FF}[luck]{/color}"
    $ block61and140 = 1
    jump choice_133

label choice_255:
    scene 336-1
    show MagicianNoLizard
    m "Эта?"
    m "Да ведь даже мои ученики могут увидеть, что это не та руна!"
    m "О боги, я не сомневаюсь, что вам придется слишком часто полагаться на свою удачу, чтобы закончить ваше путешествие!"
    play sound "audio/227-1.mp3"
    pause 3
    m "Прежде чем вы уйдете, мой друг, я дам вам кое-что, чтобы усилить ваше везение"
    m "А оно вам понадобится, если не откажетесь от своей миссии, хотя я искренне советую именно это и сделать."
    m "Вот, возьмите это"
    e "Он вручает вам маленькую овсяную лепешку"
    m "Лепешка даст вам невиданный уровень удачи"
    $ luck += 4
    s "Теперь уровень вашей удачи - {color=#FF00FF}[luck]{/color}"
    i "Благодарю вас! Прощайте!"
    $ block61and140 = 1
    jump choice_133

label choice_274:
    scene 336-1
    show MagicianNoLizard
    m "Дайте мне посмотреть"
    m "Почему вы думаете, что эта правильная руна?"
    i "На остальных клочках пергамента изображены грани игрального кубика, и только на этом изображена руна."
    m "Конечно!"
    e "Он очень взволнован тем, что вы решили его проблему, и с энтузиазмом соглашается помочь вам в ваших поисках."
    m "Я знаю только одну строчку в заклинании, которое вам требуется"
    m "И она гласит"
    m "{color=#808000}Четыре замка внутри каменных плит{/color}"
    m "Я не знаю, кто хранит другие три строки, но все они являются влиятельными гражданами."
    m "В этом городе нелюди часто знают больше, чем люди, поэтому этот подарок может быть вам полезен"
    e "Он протягивает вам маленькую сумочку с чем-то зеленым внутри."
    e "Вы вытаскиваете это и обнаруживаете, что это парик, который может быть полезен при наложении заклинаний."
    $ wig += 1
    e "Поблагодарив его, вы решаете поспешить и уходите, не забыв забрать оружие на выходе."
    e "Ваша удача восстанавливается до исходного уровня"
    $ luck = 12
    s "Теперь уровень вашей удачи - {color=#FF00FF}[luck]{/color}"
    jump choice_133


label choice_72:
    scene 336-1
    show MagicianNoLizard
    m "Вы шутите!"
    m "Это, безусловно, не та руна."
    m "Незнакомец, если такова ваша мудрость, вам понадобится больше, чем просто помощь вашей богини в этом путешествии"
    m "Я хочу продолжить свою работу, а значит, вы должны покинуть мой дом."
    e "Вы забираете свое оружие и уходите"
    $ block61and140 = 1
    jump choice_133

label choice_176:
    scene 176-1 with dissolve
    pause 0.5
    e "Вы входите в хижину художника"
    e "Вы пересекаете комнату и смотрите на холст."
    e "Незаконченный рисунок изображает вас!"
    menu:
        "Вы позволите кисти закончить ваш портрет и возможно даже купите его":
            jump choice_67
        "Помешаете кисти, закончить рисунок":
            jump choice_44
        "Покинете комнату":
            jump choice_137

label choice_67:
    scene 67-1 with dissolve
    pause 0.5
    e "Когда картина завершена, то к вашему удивлению изображение на холсте начинает двигаться."
    e "Глядя прямо на вас, портрет руками хватается за края холста, вылезает из картины и спускается на землю."
    e "Перед вами стоит ваша точная копия!"
    e "Вы мгновение смотрите друг на друга."
    e "Снаружи доносится голос художника"
    pa "Напади на него! И отбери все деньги!"
    $ current_enemy = {"name": "你的分身", "mastery": mastery, "health": health} # Ваш Двойник
    jump choice_67_fight

label choice_67_fight:
    if health <= 0:
        f "Твои силы иссякли в бою с [current_enemy['name']]! Его точный удар повергает тебя, и ты падаешь, побежденный собственной тенью."
        jump game_over

    if current_enemy["health"] <= 0:
        f "Ваш Двойник повержен! Его тело растворяется в воздухе, оставляя лишь пустой холст. Ты тяжело дышишь, но чувствуешь облегчение. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
        jump choice_137

    $ enemy_attack = renpy.random.randint(1, 12) + current_enemy["mastery"]
    $ player_attack = renpy.random.randint(1, 12) + mastery

    if enemy_attack == player_attack:
        f "Ты ([player_attack]) и [current_enemy['name']] ([enemy_attack]) атакуете одновременно, но оба уворачиваетесь! Никто не ранен. Твое здоровье: {color=#FF00FF}[health]{/color}, здоровье врага: {color=#FF00FF}[current_enemy['health']]{/color}."
        jump choice_67_fight

    elif enemy_attack < player_attack:
        $ current_enemy["health"] -= 2
        if current_enemy["health"] > 0:
            f "Твой удар ([player_attack]) пробивает защиту [current_enemy['name']] ([enemy_attack])! Ты наносишь 2 урона. У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твое здоровье: {color=#FF00FF}[health]{/color}."
            if current_enemy["health"] <= 3 and magicalSelfLockingChain == 1:
                menu:
                    "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить [current_enemy['name']]":
                        $ current_enemy["health"] = 0
                        $ magicalSelfLockingChain = 0
                        f "Ты метаешь волшебную цепь! Она обвивается вокруг [current_enemy['name']], обездвиживая его. Ты наносишь решающий удар, и [current_enemy['name']] повержен! Цепь использована, и ты не можешь её снять."
                        jump choice_137
                    "Не использовать цепь":
                        pass
        else:
            f "Твой мощный удар ([player_attack]) сокрушает [current_enemy['name']] ([enemy_attack])! Враг повержен! Твое здоровье: {color=#FF00FF}[health]{/color}."

        menu:
            "Использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ current_enemy["health"] -= 2
                    $ luck -= 1
                    if current_enemy["health"] > 0:
                        f "Удача на твоей стороне! Ты наносишь [current_enemy['name']] дополнительный урон (2). У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                        if current_enemy["health"] <= 3 and magicalSelfLockingChain == 1:
                            menu:
                                "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить [current_enemy['name']]":
                                    $ current_enemy["health"] = 0
                                    $ magicalSelfLockingChain = 0
                                    f "Ты метаешь волшебную цепь! Она обвивается вокруг [current_enemy['name']], обездвиживая его. Ты наносишь решающий удар, и [current_enemy['name']] повержен! Цепь использована, и ты не можешь её снять."
                                    jump choice_137
                                "Не использовать цепь":
                                    pass
                    else:
                        f "Удача помогает тебе! Мощный дополнительный удар (2 урона) добивает [current_enemy['name']]! Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                        jump choice_137
                else:
                    $ current_enemy["health"] += 1
                    $ luck -= 1
                    f "Удача отвернулась! [current_enemy['name']] восстанавливает 1 здоровье (теперь {color=#FF00FF}[current_enemy['health']]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
            "Не использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                pass
        jump choice_67_fight

    else:
        $ health -= 2
        if health > 0:
            f "[current_enemy['name']] наносит тебе удар ([enemy_attack])! Твоя защита ([player_attack]) не справляется. Ты теряешь 2 здоровья, осталось {color=#FF00FF}[health]{/color}."
        else:
            f "[current_enemy['name']] наносит сокрушительный удар ([enemy_attack]) против твоей защиты ([player_attack])! Ты теряешь последние силы и падаешь."
            jump game_over

        menu:
            "Использовать удачу, чтобы смягчить урон":
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ health += 1
                    $ luck -= 1
                    f "Удача спасает тебя! Ты восстанавливаешь 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ health -= 1
                    $ luck -= 1
                    if health > 0:
                        f "Удача подвела! Ты теряешь дополнительное 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                    else:
                        f "Удача подвела, и ты теряешь последнее здоровье! [current_enemy['name']] добивает тебя."
                        jump game_over
        jump choice_67_fight

label choice_44:
    scene 176-1 with dissolve
    pause 0.5
    e "Вы пытаетесь схватить волшебную кисть, но она ловко уклоняется от ваших рук и продолжает рисовать ваш портрет."
    e "Потеряв терпение, вы беретесь за оружие и пытаетесь сломать ее."
    $ current_enemy = {"name": "飞行画笔", "mastery": 8, "health": 5} # Летающая Кисть
    $ fight_round = 0
    jump choice_44_fight

label choice_44_fight:
    if fight_round >= 5:
        f "Летающая Кисть ускользает от твоих ударов и завершает портрет! Ты не успел ее уничтожить за пять раундов."
        jump choice_67

    if current_enemy["health"] <= 0:
        f "Летающая Кисть повержена! Она падает на пол, сломавшись, и портрет остается незавершенным. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
        jump choice_137

    $ fight_round += 1
    $ enemy_attack = renpy.random.randint(1, 12) + current_enemy["mastery"]
    $ player_attack = renpy.random.randint(1, 12) + mastery

    if enemy_attack >= player_attack:
        f "Ты ([player_attack]) пытаешься ударить [current_enemy['name']] ([enemy_attack]), но она ловко уклоняется! Никто не ранен. Твое здоровье: {color=#FF00FF}[health]{/color}, здоровье кисти: {color=#FF00FF}[current_enemy['health']]{/color}. Раунд: {color=#FF00FF}[fight_round]{/color}/5."
        jump choice_44_fight

    else:
        $ current_enemy["health"] -= 2
        if current_enemy["health"] > 0:
            f "Твой удар ([player_attack]) задевает [current_enemy['name']] ([enemy_attack])! Ты наносишь 2 урона. У кисти осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твое здоровье: {color=#FF00FF}[health]{/color}. Раунд: {color=#FF00FF}[fight_round]{/color}/5."
            if current_enemy["health"] <= 3 and magicalSelfLockingChain == 1:
                menu:
                    "Использовать волшебную самозамыкающуюся цепь, чтобы поймать [current_enemy['name']]":
                        $ current_enemy["health"] = 0
                        $ magicalSelfLockingChain = 0
                        f "Ты метаешь волшебную цепь! Она обвивается вокруг [current_enemy['name']], и кисть падает, сломавшись. Портрет остается незавершенным! Цепь использована, и ты не можешь её снять."
                        jump choice_137
                    "Не использовать цепь":
                        pass
        else:
            f "Твой мощный удар ([player_attack]) разрушает [current_enemy['name']] ([enemy_attack])! Кисть падает, сломавшись. Твое здоровье: {color=#FF00FF}[health]{/color}. Раунд: {color=#FF00FF}[fight_round]{/color}/5."

        menu:
            "Использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ current_enemy["health"] -= 2
                    $ luck -= 1
                    if current_enemy["health"] > 0:
                        f "Удача на твоей стороне! Ты наносишь [current_enemy['name']] дополнительный урон (2). У кисти осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твоя удача снизилась до {color=#FF00FF}[luck]{/color}. Раунд: {color=#FF00FF}[fight_round]{/color}/5."
                        if current_enemy["health"] <= 3 and magicalSelfLockingChain == 1:
                            menu:
                                "Использовать волшебную самозамыкающуюся цепь, чтобы поймать [current_enemy['name']]":
                                    $ current_enemy["health"] = 0
                                    $ magicalSelfLockingChain = 0
                                    f "Ты метаешь волшебную цепь! Она обвивается вокруг [current_enemy['name']], и кисть падает, сломавшись. Портрет остается незавершенным! Цепь использована, и ты не можешь её снять."
                                    jump choice_137
                                "Не использовать цепь":
                                    pass
                    else:
                        f "Удача помогает тебе! Мощный дополнительный удар (2 урона) разрушает [current_enemy['name']]! Твоя удача снизилась до {color=#FF00FF}[luck]{/color}. Раунд: {color=#FF00FF}[fight_round]{/color}/5."
                        jump choice_137
                else:
                    $ current_enemy["health"] += 1
                    $ luck -= 1
                    f "Удача отвернулась! [current_enemy['name']] восстанавливает 1 здоровье (теперь {color=#FF00FF}[current_enemy['health']]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}. Раунд: {color=#FF00FF}[fight_round]{/color}/5."
            "Не использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                pass
        jump choice_44_fight

label choice_108:
    scene 108-1 with dissolve
    pause 0.5
    e "Вы входите в хижину."
    e "В центре комнаты под открытым дымоходом горит большой костер."
    e "Хотя пламя сильное, но от него исходит очень мало тепла, и, глядя в него, вы видите деревянный сундук, покоящийся на углях в центре костра - и он не горит!"
    e "Вы опасаетесь ловушки"
    menu:
        "Покинуть хижину и продолжить свой путь":
            jump choice_137
        "Можете попробовать войти в пламя, так как оно не обжигает (попробовать найти способ увидеть, какие сокровища могут лежать в этом сундуке)":
            jump choice_130

label choice_130:
    scene 108-1
    e "Вы осторожно шагаете в огонь. Хотя пламя не обжигает вас, огонь начинает шипеть и плеваться, когда вы ступаете в него."
    e "Похоже, этот шум был сигналом тревоги, и в дверях появляется заклинатель огня."
    show Caster
    fc "Вы пытаетесь украсть мой сундук!"
    e "Он очень зол и кричит. А затем бросает в огонь красный порошок."
    hide Caster
    e "Вы громко вопите, огонь начинает жечь вас!"
    e "Вы выпрыгиваете из пламени в горящей одежде."
    e "Потеряйте 5 очков Здоровья из-за ожогов."
    $ health -= 5
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    if health <=0:
        jump game_over
    e "Вы гасите одежду"
    show Caster
    fc "Убирайтесь прочь!"
    jump choice_137

label choice_306:
    scene 110-1
    show Sailor
    if gold < 2:
        e "У вас недостаточно денег, чтобы продожать пьянку"
        jump choice_86
    else:
        sa "Согласен! Давай пить еще!"
        e "Вы возвращаетесь за стол и вскоре вы оба сильно пьяны."
        e "Ваш собутыльник видит друга за вашей спиной и машет ему рукой."
        hide Sailor
        show Drunkard
        e "Но тот вместо того, чтобы приветствовать приятеля, вытаскивает из-за пояса дубинку и бьет вас по затылку."
        e "Без сознания вы падаете лицом вниз на стол"
        jump choice_312

label choice_211:
    scene 227-2
    e "Лезвие падает и отсекает вам голову."
    e "Ваше приключение заканчивается здесь."
    jump game_over

label choice_15:
    scene 227-2
    show EvilInnkeeper
    e "Лезвие гильотины поднимается, и вы с облегчением вздыхаете."
    e "Трактирщик проклинает все на свете и исчезает внизу, позволяя вам освободиться от пут."
    hide EvilInnkeeper
    e "Вы стремительно покидаете таверну"
    e "Восстановите 1 очко Удачи за это чудесное спасение, вы даже смогли неплохо отдохнуть за ночь, восстановите 2 очка Здоровья"
    $ luck += 1
    s "Теперь уровень вашей удачи - {color=#FF00FF}[luck]{/color}"
    $ health += 2
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    jump choice_267

label choice_312:
    scene 312-1 with dissolve
    pause 0.5
    e "Вы открываете глаза и чувствуете, как ваша голова раскалывается от боли."
    e "Теряете 2 очка Здоровья."
    $ health -= 2
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    if health <=0:
        jump game_over
    e "Вы поднимаете руку и растираете себе шею и затылок, прежде чем начнете осматриваться по сторонам."
    e "Земля под вами мягко покачивается, сначала вы списываете это на последствие удара, но потом понимаете, что находитесь в корабельном трюме."
    e "Лучи света, проникающие сквозь зарешеченный люк в потолке, освещают другие бессознательные тела, лежащие рядом."
    e "Вы тормошите ближайшего товарища по несчастью."
    e "Он в том же состоянии, что и вы."
    e "Когда он приходит в себя, вы начинаете вдвоем размышлять, где находитесь, и приходите к выводу, что вас похитила команда корабля работорговцев."
    e "Единственный выход высоко в потолке."
    jump choice_179

label choice_179:
    scene 312-1
    e "Люк наверху открывается, и еще несколько бесчувственных тел сбрасывают вниз, но никто из членов экипажа так и не появляется."
    e "Проходит несколько часов, шум наверху указывает, что корабль вот-вот отчалит, а у вас все еще нет ни малейшей возможности для побега!"
    e "Корабль отплывает, и вы вместе с ним покидаете Кхар, но в совсем не том направлении, которое вам нужно."
    e "Вам суждено стать рабом, а ваша миссия потерпела крах."
    jump game_over

label choice_267:
    jump choice_325

label choice_325:
    scene 325-1 with dissolve
    pause 0.5
    e "Вы оставляете таверну позади."
    e "В утреннем свете видно, что она находится почти на берегу реки недалеко от Портового моста, единственной переправы через Джабаджи."
    e "Вы пересекаете великую реку."
    e "Дорога на другом берегу приводит к развилке."
    menu:
        "Повернете налево":
            jump choice_132
        "Повернете направо":
            jump choice_198

label choice_48:
    scene 187-1
    e "Жрец не может скрыть своего разочарования."
    e "Видимо народ Кхара не слишком обучен математике, в отличии от жителей Аналэнда."
    e "Как и говорил, он готов исполнить одно ваше желание."
    i "Знаете ли вы заклинание, открывающее ворота на севере Кхара?"
    bs "Я не могу сказать вам это заклинание полностью"
    bs "Все четыре строки знает только Первый Архонт."
    bs "Но я скажу вам одну из строк."
    bs "Вот она"
    bs "{color=#191970}Выход из города будет открыт{/color}"
    e "Его аудитория поражена вашей мудростью, они выкрикивают вам пожелания удачи, когда вы выходите из часовни."
    e "Восстановите свою Удачу до начального уровня"
    $ luck = 12
    s "Теперь уровень вашей удачи - {color=#FF00FF}[luck]{/color}"
    jump choice_165

label choice_248:
    scene 187-1
    bs "Братья и сестры!"
    bs "У нас новый новообращенный к Богу Злобы!"
    e "Вы дали согласие заранее, поэтому должны отказаться от своей веры в Либру и отныне поклоняться Сланггу."
    e "Это означает, что вы никогда больше не сможете обратиться за помощью к доброй богине."
    $ kharLibra = 1
    $ backlandLibra = 1
    e "Вы в одиночестве в Кахабаде до конца своего приключения."
    e "После принятия обетов вы покидаете часовню."
    e "Потеряйте 2 очка Удачи"
    $ luck -= 2
    s "Теперь уровень вашей удачи - {color=#FF00FF}[luck]{/color}"
    jump choice_165

label choice_132:
    scene 132-1 with dissolve
    pause 0.5
    e "Вы идете по узкой извилистой улице мимо магазинов и киосков."
    e "Пока еще рано, и они откроются через час или два, но в домах уже начинается утренняя суматоха."
    e "В одном из окон появляется лицо и, кажется, наблюдает за вами, хотя его глаза закрыты, и вы не уверены, что он вас действительно может увидеть."
    e "Еще одно подобное существо стоит у дверного проема и умывается на улице."
    e "Оно худое и тощее, с длинным лицом - и как у первого его глаза закрыты."
    e "Множество подобных существ – все молодые мужчины – толпятся вместе чуть дальше."
    e "Они беседуют и пинают камни в сточную канаву."
    e "Один из них «видит» вас и говорит это другим."
    e "Это может быть проблемой."
    menu:
        "Вы хотите продолжить путь и, проходя мимо, пожелать им приятного дня":
            jump choice_286
        "Продолжить путь, но приготовитесь защищаться на случай их нападения":
            jump choice_121
        "Повернете на боковую улицу, чтобы избежать встречи с ними":
            jump choice_24

label choice_286:
    scene 132-1
    e "Они смеются в ответ на вашу любезность. Один из них ставит вам подножку, и вы падаете на мостовую."
    if gold <= 0:
        e "Вы теряете 2 очка Здоровья из-за ушибленного колена"
        $ health -= 2
        s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
        if health <=0:
            jump game_over
        jump choice_89
    else:
        e "Когда вы падаете, ваша сумка с золотом открывается, и монеты высыпаются"
        e "Существа прыгают вокруг вас, утверждая, что помогут вам собрать ваше золото, но на самом деле кладут его себе в карманы."
        $ tgold = gold
        if gold >= 6:
            $ dice = renpy.random.randint(1, 6)
        else:
            $ dice = renpy.random.randint(1, gold)
        e "Вам удалось схватить {color=#FF00FF}[dice]{/color} золотых"
        $ gold = dice
        s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
        e "Прежде чем они украдут остальное, и это все, что осталось от вашего золота."
        menu:
            "Испытать удачу, чтобы попробовать собрать еще монет?" if tgold >= 7:
                e "Настало время испытать вышу удачу!"
                $ twodice = renpy.random.randint(1, 12)
                s "Уровень вашей удачи - {color=#FF00FF}[luck]{/color}, требуемый уровень удачи - {color=#FF00FF}[twodice]{/color}"
                if twodice <= luck:
                    s "Вам повезло!"
                    $ luck -= 1
                    s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
                    if tgold >= 12:
                        $ dice = renpy.random.randint(1, 6)
                    else:
                        $ dice = renpy.random.randint(1, tgold - 6)
                    e "Вам удалось схватить {color=#FF00FF}[dice]{/color} золотых"
                    $ gold += dice
                    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
                    jump choice_286_a
                else:
                    s "Вам не повезло!"
                    $ luck -= 1
                    s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
                    jump choice_286_a
            "Не испытывать удачу":
                jump choice_286_a

label choice_286_a:
    scene 132-1
    menu:
        "Бросите им вызов, чтобы вернуть украденное золото":
            jump choice_277
        "Не станете связываться и продолжите путь":
            jump choice_89

label choice_277:
    scene 132-1
    e "Они насмехаются над вами и совсем вас не бояться."
    e "Вы должны принудить их вернуть вам золото."
    scene 277-1 with dissolve
    pause 0.5
    e "Один из них случайно моргает, смотря на землю, и, когда его веки размыкаются, вы видите, что его глаза — это два горящих красных шара пламени!"
    menu:
        "Приготовитесь атаковать их":
            jump choice_103
        "Уйдете":
            jump choice_89

label choice_103:
    jump choice_192

label choice_192:
    scene 132-1 with dissolve
    pause 0.5
    e "Они смеются, когда вы выхватываете оружие."
    scene 277-1 with dissolve
    pause 0.5
    e "Один из них приподнимает веки, и красный луч вылетает из его глаз, обжигая ваше запястье, вы роняете оружия и теряете 2 очка Здоровья."
    $ health -= 2
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    if health <=0:
        jump game_over
    e "Они надвигаются на вас и окружают, у вас нет другого выбора, кроме как сдаться."
    scene 192-1 with dissolve
    pause 0.5
    e "Они ведут вас к квадратному зданию и заводят внутрь."
    e "Там они о чем-то беседуют еще с одним похожим на них существом, но немного более старым."
    scene 192-2 with dissolve
    pause 0.5
    e "Кажется, что это их личная тюрьма, во всяком случае, вас запирают в камере"
    jump choice_143

label choice_143:
    scene 192-2
    e "У вас отбирают рюкзак и оружие и запирают, под наблюдением стража."
    e "Однако у вас есть сокамерник, маленький неунывающий эльвин."
    show Elvin
    el "Приветствую тебя в твоем новом доме!"
    el "Вы попали в плен к Красным Глазам."
    el "Представители этой странной и загадочной расы из-за их высокомерного и гнусного характера давно изгнаны из всех цивилизованных мест"
    el "Они вынуждены вести кочевой образ жизни, и лишь здесь в Кхареу них есть постоянная колония"
    el "Наделенная особыми правами и привилегиями, в том числе на свою частную тюрьму, так что вы здесь надолго."
    el "Сам я родом из Долины Эльвинов, что в Холмах Шамутанти"
    el "Но я заперт здесь уже несколько месяцев, поэтому рад любой компании."
    i "Почему ты до сих пор не сбежал, ведь эльвины волшебные существа?"
    el "В стенах этой тюрьмы не действуют никакие заклинания, я подозреваю наличие мощной антимагической защиты."
    if copperKey > 0:
        e "Ваш медный ключ пригодился вам!"
        #jump choice_
    if kharLibra == 0:
        e "Вы решили воззвать к Либре"
        hide Elvin
        jump choice_30
    e "Вам придется сидеть здесь до конца вашей жизни..."
    jump game_over

label choice_30:
    scene 192-2
    e "Вы молитесь своей богине-покровительнице."
    e "Вы слышите тихий щелчок от двери"
    play sound "audio/30-1.mp3"
    pause 1
    show Elvin
    el "Тссс! Это сработало! Дверь открыта!"
    e "Теперь вы можете уйти, когда захотите, но решаете подождать, пока охранник уснет."
    e "Вы беззвучно произносите благодарственную молитву Либре, но помните, что больше не сможете призвать ее на помощь в этой части приключения"
    jump choice_206

label choice_121:
    scene 132-1
    e "Они внимательно следят за вами, когда вы проходите мимо."
    e "Они знают, что вы готовы к бою, но совсем вас не опасаются."
    e "Внезапно один из них подает знак другим, и они все атакуют вас."
    e "Вам придется сражаться с ними"
    jump choice_103

label choice_198:
    scene 198-1 with dissolve
    pause 0.5
    e "Утреннее солнце освещает пробуждающиеся улицы Кхара."
    e "Вы следуете по дороге, пока не выходите на площадь, в центре которой странные существа собираются вокруг какого-то, то ли памятника, то ли монумента."
    e "Вы подходите поближе."
    e "У монумента впереди есть большая арка, за которой, видимо, находится нечто очень важное, судя по тому, как в нее вглядываются зрители."
    e "Сами зрители довольно странные личности."
    e "Они худые и тощие, с вытянутыми лицами."
    e "И их глаза, кажется, постоянно закрыты!"
    menu:
        "Подойдете ближе к сооружению":
            jump choice_204
        "Обогнете его и пересечете площадь":
            jump choice_50

label choice_204:
    scene 198-1
    e "Вы поднимаетесь по ступенькам, окружающим монумент и пытаетесь заглянуть внутрь, чтобы понять, что там находится."
    cy "Эй, не толкайся! Осторожней!"
    e "Вы извиняетесь и всматриваетесь дальше."
    scene 204-1 with dissolve
    pause 0.5
    e "Внутри вы видите что-то похожее на бассейн с мерцающей водой, хотя не совсем уверены, что это именно вода."
    menu:
        "Вы наклонитесь ближе":
            jump choice_123
        "Спросите у окружающих, что это":
            jump choice_116
        "Отступите назад и покинете площадь":
            jump choice_275

label choice_123:
    scene 204-1
    e "Вы опускаетесь на колени и слышите хихиканье позади себя, а затем ботинок врезается вам в зад и посылает вас прямиком в бассейн!"
    e "Всплеска воды, которого вы ожидаете, не происходит"
    jump choice_270

label choice_270:
    scene 270-1 with dissolve
    pause 0.5
    e "Вы медленно плывете по воздуху, переворачиваясь снова и снова ..."
    e "В кромешной тьме вы ничего не видите."
    scene 270-2 with dissolve
    pause 0.5
    e "Затем, как будто попадаете в туннель, вдалеке вы видите пятно света, которое становится больше, когда падаете к нему навстречу."
    e "В конце концов, вы выходите из туннеля…."
    e "И понимаете, что ваша судьба лишь немногим лучше смерти!"
    scene 270-3 with dissolve
    pause 0.5
    e "Вы находитесь в канализации глубоко под Кхаром."
    e "Туннели тянутся и исчезают вдали во всех направлениях, а зловоние здесь невыносимое."
    e "Вы упали в отвратительную груду невероятной грязи: слизь, экскременты, шлак, навоза и мусор - и вы в ней по горло!"
    e "Еще до того, как вы попытаетесь выползти из этой трясины, брызги слева от вас обращают ваше внимание на небольшое отверстие в стене рядом с вашим ухом."
    e "Из этой трубы вытекает поток жидких сточных вод и помоев."
    e "Через несколько мгновений он вырвется из трубы прямо вам в лицо!"
    e "Вы должны принять решение быстро"
    menu:
        "Пригнуться и нырнуть":
            jump choice_250
        "Стоять как стоял":
            jump choice_327

label choice_250:
    scene 270-3
    e "Вы делаете глубокий вдох и погружаетесь в отвратительную грязь."
    e "Когда выныриваете обратно, поток уже пронесся дальше, и вы можете выбраться из груды отбросов."
    e "Чувствуете себя отвратительно, теряете 3 очка Здоровья."
    $ health -= 3
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    if health <=0:
        jump game_over
    e "Вы как можно лучше очищаете себя от грязи, и теперь должны попытаться найти выход."
    menu:
        "Пойдете прямо, повернете направо, потом снова направо":
            jump choice_298
        "Пойдете прямо, повернете налево, затем снова налево":
            jump choice_42
        "Пойдете прямо, повернете налево, а затем на развилке снова прямо":
            jump choice_174

label choice_327:
    scene 270-3
    e "Вы задерживаете дыхание, когда струя грязной жидкости вылетает из трубы прямо вам в лицо."
    e "Вас как будто ведром с помоями ударили, теряете 3 очка Здоровья."
    $ health -= 3
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    if health <=0:
        jump game_over
    e "Вы вылезаете из груды мерзкого мусора и пытаетесь как можно лучше очистить себя."
    e "Теперь вы должны попытаться найти выход."
    menu:
        "Пройдете вперед, затем первый поворот налево, затем первый направо, потом снова первый направо и наконец первый налево":
            jump choice_10
        "Пройдете вперед, затем второй поворот направо, потом первый на право и дальше вперед":
            jump choice_298
        "Пройдете вперед, затем первый поворот направо, потом первый налево, а затем первый направо":
            jump choice_77

label choice_10:
    scene 10-1 with dissolve
    pause 0.5
    e "Вы попадаете в тупик."
    e "Придется вернуться и выбрать другой маршрут."
    e "По какому пути вы пойдете?"
    menu:
        "Пойдете прямо, никуда не сворачивая":
            jump choice_298
        "Второй поворот направо и дальше только вперед":
            jump choice_174
        "Первый поворот направо и дальше только вперед":
            jump choice_69

label choice_69:
    scene 69-1 with dissolve
    pause 0.5
    e "Вы попадаете в тупик, но вверху виден свет."
    e "Вы смотрите туда и видите свисающую веревку с ведром на конце!"
    e "Возможно, вы нашли заброшенный колодец!"
    e "Вы подпрыгиваете и хватаетесь за веревку."
    e "Вы начинаете длинный и утомительный подъем навстречу свету, теряете 2 очка Здоровья"
    $ health -= 2
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    if health <=0:
        jump game_over
    e "Но восстанавливаете 2 очка Удачи за то, что нашли выход из канализации"
    $ luck += 2
    s "Теперь уровень вашей удачи - {color=#FF00FF}[luck]{/color}"
    e "Наверху вы обнаруживаете, что действительно выбрались на поверхность через колодец."
    e "Вы отдыхаете"
    menu:
        "Продолжить путь к окраине Кхара":
            jump choice_319
        "Назад в сторону порта, чтобы исследовать здание, стоящее рядом на кладбище":
            jump choice_83

label choice_298:
    scene 298-1 with dissolve
    pause 0.5
    e "Вы попадаете в тупик"
    menu:
        "Повернетесь и на первой развилке повернете направо":
            jump choice_77
        "Повернетесь, на первой развилке налево, а затем второй поворот налево":
            jump choice_42
        "Повернетесь, на первой развилке налево, потом все время прямо":
            jump choice_174

label choice_77:
    scene 77-1 with dissolve
    pause 0.5
    e "Вы попадаете в тупик и останавливаетесь по колено в сточных водах."
    e "Пузырьки на поверхности жидкости перед вами заставляют насторожиться, а затем вы видите, как из воды поднимается нечто."
    e "Гладкая дряблая фигура – это же крупный Пожиратель Слизи."
    show SlimeEater
    e "Он видит вас и громко ревет, протягивая к вам свои склизкие руки."
    e "Придется сразиться с ним"
    $ current_enemy = {"name": "史莱姆吞噬者", "mastery": 7, "health": 11} # Пожиратель Слизи
    jump choice_77_fight

label choice_77_fight:
    if health <= 0:
        f "Твои силы иссякли в бою с [current_enemy['name']]! Его склизкие лапы одолевают тебя, и ты падаешь в сточные воды."
        jump game_over

    if current_enemy["health"] <= 0:
        f "Пожиратель Слизи повержен! Его тело растворяется в сточной воде, оставляя зловонный запах. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
        jump choice_196

    $ enemy_attack = renpy.random.randint(1, 12) + current_enemy["mastery"]
    $ player_attack = renpy.random.randint(1, 12) + mastery

    if enemy_attack == player_attack:
        f "Ты ([player_attack]) и [current_enemy['name']] ([enemy_attack]) атакуете одновременно, но оба уклоняетесь! Никто не ранен. Твое здоровье: {color=#FF00FF}[health]{/color}, здоровье врага: {color=#FF00FF}[current_enemy['health']]{/color}."
        jump choice_77_fight

    elif enemy_attack < player_attack:
        $ current_enemy["health"] -= 2
        if current_enemy["health"] > 0:
            f "Твой удар ([player_attack]) пробивает защиту [current_enemy['name']] ([enemy_attack])! Ты наносишь 2 урона. У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твое здоровье: {color=#FF00FF}[health]{/color}."
            if current_enemy["health"] <= 3 and magicalSelfLockingChain == 1:
                menu:
                    "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить [current_enemy['name']]":
                        $ current_enemy["health"] = 0
                        $ magicalSelfLockingChain = 0
                        f "Ты метаешь волшебную цепь! Она обвивается вокруг [current_enemy['name']], обездвиживая его. Ты наносишь решающий удар, и [current_enemy['name']] повержен! Цепь использована, и ты не можешь её снять."
                        jump choice_196
                    "Не использовать цепь":
                        pass
        else:
            f "Твой мощный удар ([player_attack]) сокрушает [current_enemy['name']] ([enemy_attack])! Враг повержен! Твое здоровье: {color=#FF00FF}[health]{/color}."

        menu:
            "Использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ current_enemy["health"] -= 2
                    $ luck -= 1
                    if current_enemy["health"] > 0:
                        f "Удача на твоей стороне! Ты наносишь [current_enemy['name']] дополнительный урон (2). У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                        if current_enemy["health"] <= 3 and magicalSelfLockingChain == 1:
                            menu:
                                "Использовать волшебную самозамыкающуюся цепь, чтобы обездвижить [current_enemy['name']]":
                                    $ current_enemy["health"] = 0
                                    $ magicalSelfLockingChain = 0
                                    f "Ты метаешь волшебную цепь! Она обвивается вокруг [current_enemy['name']], обездвиживая его. Ты наносишь решающий удар, и [current_enemy['name']] повержен! Цепь использована, и ты не можешь её снять."
                                    jump choice_196
                                "Не использовать цепь":
                                    pass
                    else:
                        f "Удача помогает тебе! Мощный дополнительный удар (2 урона) добивает [current_enemy['name']]! Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                        jump choice_196
                else:
                    $ current_enemy["health"] += 1
                    $ luck -= 1
                    f "Удача отвернулась! [current_enemy['name']] восстанавливает 1 здоровье (теперь {color=#FF00FF}[current_enemy['health']]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
            "Не использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                pass
        jump choice_77_fight

    else:
        $ health -= 2
        if health > 0:
            f "[current_enemy['name']] наносит тебе удар ([enemy_attack])! Твоя защита ([player_attack]) не справляется. Ты теряешь 2 здоровья, осталось {color=#FF00FF}[health]{/color}."
        else:
            f "[current_enemy['name']] наносит сокрушительный удар ([enemy_attack]) против твоей защиты ([player_attack])! Ты теряешь последние силы и падаешь."
            jump game_over

        menu:
            "Использовать удачу, чтобы смягчить урон":
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ health += 1
                    $ luck -= 1
                    f "Удача спасает тебя! Ты восстанавливаешь 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ health -= 1
                    $ luck -= 1
                    if health > 0:
                        f "Удача подвела! Ты теряешь дополнительное 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                    else:
                        f "Удача подвела, и ты теряешь последнее здоровье! [current_enemy['name']] добивает тебя."
                        jump game_over
            "Не использовать удачу, чтобы смягчить урон":
                pass
        jump choice_77_fight

label choice_196:
    scene 77-1
    e "Вам лучше уйти отсюда да побыстрее, так как Пожиратели Слизи обычно охотятся группами"
    e "Есть вероятность, что здесь есть и другие."
    e "По какому пути вы пойдете?"
    menu:
        "Сначала налево, а потом прямо":
            jump choice_298
        "Сначала направо, потом первый поворот налево, потом второй поворот налево, потом направо":
            jump choice_174
        "Сначала налево, потом направо, потом второй поворот налево":
            jump choice_42

label choice_42:
    scene 42-1 with dissolve
    pause 0.5
    e "Вы находитесь в тупике."
    e "Придется вернуться назад."
    e "По какому пути вы пойдете?"
    menu:
        "Прямо вперед, второй поворот направо, затем первый налево":
            jump choice_10
        "Прямо вперед, первый поворот направо, затем второй налево, потом первый направо":
            jump choice_77
        "Прямо вперед и первый поворот налево":
            jump choice_174

label choice_174:
    scene 174-1 with dissolve
    pause 0.5
    e "Вы попадаете в тупик, придется вернуться и выбрать другую дорогу."
    e "Как вы пойдете?"
    menu:
        "Первый поворот налево, затем первый направо, снова первый направо, затем первый налево и еще раз первый поворот направо":
            jump choice_298
        "Первый поворот направо":
            jump choice_42
        "Третий поворот налево, затем первый направо":
            jump choice_77

label choice_83:
    scene 83-1 with dissolve
    pause 0.5
    e "Идя дальше по улице, вы проходите мимо небольшого тенистого кладбища."
    e "Надгробия разбросаны в произвольном порядке вокруг стоящего в центре склепа."
    e "Надпись над входом в него гласит: «ЗДЕСЬ ПОКОИТСЯ ЛОРД ШИНВА – ПЯТЫЙ АРХОНТ КХАРА»."
    menu:
        "Зайдете в склеп":
            jump choice_47
        "Безопасней продолжить путь по улицам к окраине города":
            jump choice_127

label choice_47:
    scene 47-1 with dissolve
    pause 0.5
    e "Вы входите на кладбище и по заросшей тропинке следуете к склепу."
    e "На земле перед ним возник мерцающий темный круг, который вам надо пересечь, чтобы добраться до дверей."
    menu:
        "Вы пройдете сквозь него":
            jump choice_288
        "Вы перепрыгнете его":
            jump choice_258

label choice_288:
    scene 47-1
    e "Вы не касаетесь поверхности круга, он вас засасывает"
    scene 270-1 with dissolve
    pause 0.5
    e "Это портал-ловушка, и вы медленно падаете вниз в темноту"
    jump choice_270

label choice_258:
    scene 47-1
    e "Настало время испытать вышу удачу!"
    $ twodice = renpy.random.randint(1, 12)
    s "Уровень вашей удачи - {color=#FF00FF}[luck]{/color}, требуемый уровень удачи - {color=#FF00FF}[twodice]{/color}"
    if twodice <= luck:
        s "Вам повезло! Вы перепрыгнули круг и приземлились прямо у дверной арки."
        $ luck -= 1
        s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
        jump choice_317
    else:
        s "Вам не повезло! Вы приземлились внутри круга."
        $ luck -= 1
        s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
        jump choice_288

label choice_317:
    scene 47-1
    e "Теперь вы можете попытаться войти в склеп."
    menu:
        "Распахнете дверь и запрыгнете внутрь, чтобы застать врасплох того, кто может быть внутри":
            jump choice_249
        "Достанете из рюкзака что-нибудь полезное":
            jump choice_7

label choice_249:
    scene 249-1 with dissolve
    pause 0.5
    e "Дверь распахивается, и вы рывком заскакиваете внутрь. Склеп пуст!"
    e "У дальней стены узкие каменные ступени ведут вниз на следующий уровень."
    menu:
        "Вы спуститесь по лестнице":
            jump choice_164
        "С вас хватит этого места":
            jump choice_16

label choice_164:
    scene 164-1 with dissolve
    pause 0.5
    e "Вы осторожно спускаетесь по лестнице."
    e "Стены здесь влажные, а в воздухе стоит тяжелый запах гниения."
    e "Единственный звук, который вы можете услышать – это шум капель, падающих откуда-то сверху."
    e "У подножия лестницы расположено большое темное помещение."
    scene 164-2 with dissolve
    pause 0.5
    e "В центре комнаты лежит гроб, и вы подходите ближе, чтобы рассмотреть его."
    e "Громкий скрип заставляет ваше сердце остановиться!"
    e "Крышка гроба двигается!"
    e "Зачарованный, вы наблюдаете, как она приоткрывается на дюйм, а затем замечаете движение слева от вас."
    e "Из темной ниши появляется белая призрачная фигура и надвигается на вас!"
    menu:
        "Возьметесь за оружие":
            jump choice_99
        "Повернетесь и убежите":
            jump choice_16

label choice_99:
    scene 164-2
    menu:
        "Будете использовать меч":
            jump choice_151
        "Будете использовать топор":
            jump choice_125
        "Будете использовать лук и стрелы" if bowAndArrows > 0:
            jump choice_147

label choice_151:
    scene 151-1 with dissolve
    pause 0.5
    e "Вы выхватываете свое оружие и сходитесь с существом."
    e "Когда свет падает на его лицо, вы видите ужасный призрачный череп, который смотрит на вас."
    e "Вы наносите ему первый удар!"
    jump choice_189

label choice_189:
    scene 151-1
    e "Этой могучей нежити нельзя повредить обычным оружием, и оно злорадно хохочет, когда удар безвредно проходит сквозь него!"
    e "Продолжайте бой."
    e "Вы снова нановите удар своим оружием"
    e "Настало время испытать вышу удачу!"
    $ twodice = renpy.random.randint(1, 12)
    s "Уровень вашей удачи - {color=#FF00FF}[luck]{/color}, требуемый уровень удачи - {color=#FF00FF}[twodice]{/color}"
    if twodice <= luck:
        s "Вам повезло!"
        $ luck -= 1
        s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
        jump choice_38
    else:
        s "Вам не повезло!"
        $ luck -= 1
        s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
        e "Вы получили удар от призрака"
        $ health -= 2
        s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
        if health <=0:
            jump game_over
        e "Придется повторить удар, для этого запустим данный уровень снова!"
        jump choice_189


label choice_38:
    scene 151-1
    e "Вы догадываетесь, что этого призрака можно уничтожить серебряным оружием."
    menu:
        "Вытащить лук со стрелами с наконечниками из серебра" if bowAndArrows > 0:
            jump choice_147
        "Молиться Либре" if kharLibra == 0 and bowAndArrows == 0:
            jump choice_87
        "Пасть в бою":
            jump game_over

label choice_87:
    scene 151-1
    e "Существо продолжает свои атаки, и вы мало что можете с этим поделать."
    scene 87-1 with dissolve
    pause 0.5
    e "Внезапно он смотрит на луч света, падающий из лестничного колодца."
    e "Ваши глаза привыкли к темноте, и когда вы смотрите на свет, то не можете быть уверены в том, что видите."
    e "Светящаяся белая женская фигура, кажется, стоит в луче света."
    e "Она указывает на гроб."
    e "Призрак в ужасе стонет, и пятится к гробу, не в силах сопротивляться безмолвному приказу."
    e "Его движения становятся вялыми: кажется, что его жизненная сила истощается."
    e "С последним усилием он лезет внутрь гроба. Вы оглядываетесь на фигуру у лестницы."
    e "Она исчезла!"
    jump choice_209

label choice_209:
    scene 164-2 with dissolve
    pause 0.5
    e "Когда заканчиваете отдыхать после битвы, вы слышите звук, доносящийся из запертого гроба."
    scene 209-1 with dissolve
    pause 0.5
    e "Призрачная фигура снова предстает перед вами!"
    e "Но это не тот страшный призрак, которого вы одолели, а какой-то древний старик."
    osk "Кто здесь?"
    osk "Кто положил конец моим мучениям?"
    e "Он шарит глазами по склепу, пока его взгляд не упирается в вас."
    osk "Незнакомец, я в долгу перед вами"
    osk "Много лет назад меня прокляли живой смертью."
    osk "И теперь, наконец, моя душа может упокоиться с миром."
    osk "Чем я могу отплатить вам?"
    i "Мне нужно пересечь Кхар, чтобы попасть в Бакланд"
    i "Для этого мне нужно заклинание, отворяющее ворота на север."
    osk "Вы и правда никогда не покинете город без заклинания."
    osk "Сам я знаю только одну строку"
    osk "{color=#8B4513}А один под воротами скрыт{/color}"
    i "Моя миссия - мой крест"
    osk "Удачи вам"
    osk "Я больше ничем не могу вам помочь,"
    osk "Кроме, может быть, одного куплета, который я слышал в прежние дни."
    osk "У меня есть ощущение, что это пригодится вам."
    osk "{color=#800000}Чтобы усыпить Бессонного Юарана,{/color}"
    osk "{color=#800000}Ищи ту, кого зовут Шамом.{/color}"
    osk "Я не знаю, что значит этот совет, но имейте его в виду"
    e "Вы благодарите его и покидаете склеп, восстановите 2 очка Удачи"
    $ luck += 2
    s "Теперь уровень вашей удачи - {color=#FF00FF}[luck]{/color}"
    jump choice_16

label choice_125:
    scene 151-1
    $ axeselect = 1
    e "Существо плавно приближается, пока вы готовитесь к бою"
    jump choice_151

label choice_147:
    scene 151-1
    e "Вы уже держите в руках лук, то быстро натягиваете тетиву и пускаете стрелу прямо в отвратительный скалящийся череп нападающего."
    e "Проверьте ваше Мастерство"
    $ twodice = renpy.random.randint(1, 20)
    s "Уровень вашего мастерства - {color=#FF00FF}[mastery]{/color}, требуемый уровень мастерства - {color=#FF00FF}[twodice]{/color}"
    if twodice <= mastery:
        e "Враг теряет 2 очка Выносливости еще до того, как успевает вступить в бой!"
        $ hGhost -= 2
        s "Теперь уровень здоровья врага: {color=#FF00FF}[hGhost]{/color}"
    else:
        e "Ваше мастерство не позволило сделать задуманное! Вы зря потратили стрелу."
    e "Вы выбрали правильное оружие для боя с призраком, ведь ему может повредить только серебро, а наконечники ваших стрел из серебра."
    $ arrows = 10
    $ current_enemy = {"name": "死亡幽灵", "mastery": 9, "health": hGhost} # Призрак Смерти
    jump choice_147_fight

label choice_147_fight:
    if health <= 0:
        f "Твои силы иссякли в бою с [current_enemy['name']]! Его ужасающая мощь одолевает тебя, и ты падаешь, побежденный."
        jump game_over

    if arrows <= 0:
        f "У вас закончились стрелы! [current_enemy['name']] надвигается на тебя, и ты не можешь больше сопротивляться."
        jump game_over

    if current_enemy["health"] <= 0:
        f "[current_enemy['name']] повержен! Твоя последняя стрела пронзает его, и он рассеивается с жутким воплем. Осталось стрел: {color=#FF00FF}[arrows]{/color}. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
        jump choice_54

    $ enemy_attack = renpy.random.randint(1, 12) + current_enemy["mastery"]
    $ player_attack = renpy.random.randint(1, 12) + mastery
    $ arrows -= 1

    if enemy_attack == player_attack:
        f "Ты ([player_attack]) выпускаешь стрелу в [current_enemy['name']] ([enemy_attack]), но он уклоняется! Никто не ранен. Твое здоровье: {color=#FF00FF}[health]{/color}, здоровье врага: {color=#FF00FF}[current_enemy['health']]{/color}, осталось стрел: {color=#FF00FF}[arrows]{/color}."
        jump choice_147_fight

    elif enemy_attack < player_attack:
        $ current_enemy["health"] -= 2
        if current_enemy["health"] > 0:
            f "Твоя стрела ([player_attack]) попадает в [current_enemy['name']] ([enemy_attack])! Ты наносишь 2 урона. У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твое здоровье: {color=#FF00FF}[health]{/color}, осталось стрел: {color=#FF00FF}[arrows]{/color}."
        else:
            f "Твоя последняя стрела ([player_attack]) пронзает [current_enemy['name']] ([enemy_attack])! Враг повержен! Твое здоровье: {color=#FF00FF}[health]{/color}, осталось стрел: {color=#FF00FF}[arrows]{/color}."

        menu:
            "Использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ current_enemy["health"] -= 2
                    $ luck -= 1
                    $ arrows -= 1
                    if current_enemy["health"] > 0:
                        f "Удача на твоей стороне! Твоя следующая стрела наносит [current_enemy['name']] дополнительный урон (2). У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твоя удача снизилась до {color=#FF00FF}[luck]{/color}, осталось стрел: {color=#FF00FF}[arrows]{/color}."
                    else:
                        f "Удача помогает тебе! Мощный дополнительный выстрел (2 урона) добивает [current_enemy['name']]! Твоя удача снизилась до {color=#FF00FF}[luck]{/color}, осталось стрел: {color=#FF00FF}[arrows]{/color}."
                        jump choice_54
                else:
                    $ current_enemy["health"] += 1
                    $ luck -= 1
                    f "Удача отвернулась! [current_enemy['name']] восстанавливает 1 здоровье (теперь {color=#FF00FF}[current_enemy['health']]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}, осталось стрел: {color=#FF00FF}[arrows]{/color}."
            "Не использовать удачу, чтобы нанести дополнительный урон" if current_enemy["health"] > 0:
                pass
        jump choice_147_fight

    else:
        $ health -= 2
        if health > 0:
            f "[current_enemy['name']] наносит тебе удар ([enemy_attack])! Твоя защита ([player_attack]) не справляется. Ты теряешь 2 здоровья, осталось {color=#FF00FF}[health]{/color}, осталось стрел: {color=#FF00FF}[arrows]{/color}."
        else:
            f "[current_enemy['name']] наносит сокрушительный удар ([enemy_attack]) против твоей защиты ([player_attack])! Ты теряешь последние силы и падаешь."
            jump game_over

        menu:
            "Использовать удачу, чтобы смягчить урон":
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ health += 1
                    $ luck -= 1
                    f "Удача спасает тебя! Ты восстанавливаешь 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}, осталось стрел: {color=#FF00FF}[arrows]{/color}."
                else:
                    $ health -= 1
                    $ luck -= 1
                    if health > 0:
                        f "Удача подвела! Ты теряешь дополнительное 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}, осталось стрел: {color=#FF00FF}[arrows]{/color}."
                    else:
                        f "Удача подвела, и ты теряешь последнее здоровье! [current_enemy['name']] добивает тебя."
                        jump game_over
            "Не использовать удачу, чтобы смягчить урон":
                pass
        jump choice_147_fight

label choice_54:
    scene 164-2 with dissolve
    pause 0.5
    e "Одолев ужасное существо, вы бросаете его останки в гроб и захлопываете крышку."
    e "После битвы вы можете передохнуть и съесть порцию еды из ваших запасов."
    menu:
        "Поесть" if meal > 0:
            $ meal -= 1
            $ health += 2
            s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
            jump choice_209
        "Не есть":
            jump choice_209

label choice_7:
    scene 47-1
    e "Какой предмет вы хотите взять в руки?"
    menu:
        "Черную маску" if blackmask > 0:
            jump choice_249
        "Лук и стрелы" if bowAndArrows > 0:
            jump choice_249
        "Волшебную цепь" if magicalSelfLockingChain > 0:
            jump choice_249
        "Ничего":
            jump choice_249

label choice_116:
    scene 198-1 with dissolve
    pause 0.5
    cy "Ты что вчера родился, придурок?"
    e "Реагирует на ваш вопрос одно из существ. затем он поворачивается к вам и пристально «вглядывается»."
    cy "Чужак! Братья, у нас здесь чужой! А не повеселиться ли нам?"
    e "Остальные тоже поворачиваются к вам и видимо «смотрят» на вас своими закрытыми глазами."
    e "Они хватают вас и толкают в бассейн."
    e "Настало время испытать вышу удачу!"
    $ twodice = renpy.random.randint(1, 12)
    s "Уровень вашей удачи - {color=#FF00FF}[luck]{/color}, требуемый уровень удачи - {color=#FF00FF}[twodice]{/color}"
    if twodice <= luck:
        s "Вам повезло!"
        $ luck -= 1
        s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
        jump choice_290
    else:
        s "Вам не повезло!"
        $ luck -= 1
        s "Теперь ваш уровень удачи - {color=#FF00FF}[luck]{/color}"
        jump choice_330

label choice_290:
    scene 198-1
    e "Вам удается вырваться из их рук."
    e "Они поворачиваются к вам и явно не отпустят вас без драки."
    jump choice_309

label choice_309:
    scene 198-1
    e "Когда вы достаете оружие, один из них открывает глаза."
    scene 277-1 with dissolve
    pause 0.5
    e "За его веками горят два огненных шара, и, когда он встречается с вами взглядом, струя огня вылетает вам прямо в лицо."
    e "Вы кричите и подносите руки к глазам, но уже слишком поздно."
    e "Вечная слепота — это ваше наказание за то, что посмели связаться с Красными Глазами, и теперь вы не сможете продолжать свою миссию."
    jump game_over

label choice_330:
    scene 198-1
    e "Вы боретесь изо всех сил, но они держат вас крепко и толкают к бассейну."
    scene 277-1 with dissolve
    pause 0.5
    e "Вы ударяете одного из них по лицу, заставляя его на мгновение мигнуть, позволяя вам увидеть, что вместо глаз у него маленькие горящие огненные шары."
    e "Теперь вы поняли, что эти существа Красные Глаза."
    scene 204-1 with dissolve
    pause 0.5
    e "Они толкают вас в бассейн, но ожидаемого вами всплеска воды не происходит"
    jump choice_270

label choice_24:
    scene 132-1
    e "Они направляются к вам, а вы резко поворачиваете влево, на боковую улицу."
    e "Существа бросаются за вами."
    e "Они быстро бегают, и придется постараться, чтобы оторваться от них."
    menu:
        "Повернете в первый поворот направо, затем в первый налево, затем снова в первый направо":
            jump choice_232
        "Повернете в первый поворот направо, затем снова направо, а потом в первый налево":
            jump choice_41
        "Повернете в первый поворот налево, затем в первый направо и снова направо":
            jump choice_184

label choice_232:
    scene 232-1 with dissolve
    pause 0.5
    e "Вы повернули не туда и оказались в тупике."
    e "Шаги преследователей приближаются, бой неизбежен."
    e "Вы готовитесь к схватке, когда они показываются из-за угла"
    jump choice_103

label choice_41:
    scene 41-1 with dissolve
    pause 0.5
    e "Вы останавливаетесь возле хижины."
    e "Шаги позади вас становятся громче, и вы решаете спрятаться внутри"
    jump choice_324

label choice_184:
    scene 184-1 with dissolve
    pause 0.5
    e "Забежав за поворот, вы с замиранием сердца понимаете, что оказались в тупике."
    e "Шаги позади вас становятся ближе, когда существа повернут за угол, вам придется сразиться с ними"
    jump choice_103

label choice_89:
    scene 89-1 with dissolve
    pause 0.5
    e "Дальше по дороге вы попадаете на развилку, откуда можно повернуть направо или налево."
    e "Левая дорога ведет к городским окраинам, а правая ведет по короткой улице к большому зданию, на котором написано «Игорные Залы Влада»"
    e "На самой развилке стоит большая бронзовая статуя, а у ее ног - горшок с множеством золотых монет."
    e "Вы полагаете, что это, должно быть, один из богов-покровителей Кхара, а в этом горшке – подношения богу."
    menu:
        "Хотите продолжить путь по левой дороге":
            jump choice_104
        "Хотите повернуть направо и зайти в «Игорные Залы Влада»":
            jump choice_56
        "Взять горсть монет из горшка у ног статуи":
            jump choice_221

label choice_324:
    scene 324-1 with dissolve
    pause 0.5
    e "Вы входите в хижину, и ваши глаза расширяются от удивления."
    e "Комната внутри от пола до потолка завалена предметами, некоторые лежат на полках, некоторые подвешены к потолку, другие прислонены к стене."
    e "Хижина битком набита оружием, посудой, керамикой, украшениями, предметами домашнего обихода, магическими принадлежностями и т.д."
    e "На полу со скрещенными ногами сидит маленький бородатый гном, который потирает руки и приветствует вас, когда вы входите."
    lbg "Садись и поменяйся со мной предметами! Я не торгую. Я только меняюсь."
    menu:
        "Если вы хотите увидеть, что он может предложить":
            jump choice_264
        "Если не хотите меняться":
            jump choice_158

label choice_264:
    scene 324-1
    lbg "好极了，好极了！"
    lbg "让我们看看今天能做什么交易。"

    python:
        # --- БАРТЕР: двухъязычные названия предметов (RU + 中文) ---
        store.ru_names = {
            "blackmask": "Черная маска",
            "healingPotion": "Зелье здоровья",
            "bagWithThreeStones": "Мешочек с камнями",
            "servingOfSeaSand": "Морской песок",
            "braceletBones": "Костяной браслет",
            "dimChain": "Тусклая цепь",
            "goldFramedMirror": "Зеркало в золотой рамке",
            "scrollParchment": "Свиток пергамента",
            "bottleWithTheInscription": "Таинственное зелье",
            "honeycombWithBeeswax": "Пчелиный воск",
            "bottleDust": "Флакон с пылью",
            "goatCheese": "Козий сыр",
            "emptyWallet": "Пустой кошелек",
            "goodLuckCharm": "Талисман удачи",
            "poison": "Яд",
            "spirits": "Духи",
            "wig": "Парик",
            "bambooFlute": "Бамбуковая флейта",
            "goblinTeethBag": "Сумка с зубами гоблинов",
            "largeBackpack": "Большой рюкзак",
            "compass": "Зачарованный компас",
        }

        store.zh_names = {
            "blackmask": "黑色面具",
            "healingPotion": "治疗药水",
            "bagWithThreeStones": "石子袋",
            "servingOfSeaSand": "海沙",
            "braceletBones": "骨制手镯",
            "dimChain": "暗淡的链条",
            "goldFramedMirror": "金框镜子",
            "scrollParchment": "羊皮卷轴",
            "bottleWithTheInscription": "神秘药剂",
            "honeycombWithBeeswax": "蜂蜡",
            "bottleDust": "尘土小瓶",
            "goatCheese": "山羊奶酪",
            "emptyWallet": "空钱包",
            "goodLuckCharm": "幸运护符",
            "poison": "毒药",
            "spirits": "香水",
            "wig": "假发",
            "bambooFlute": "竹笛",
            "goblinTeethBag": "哥布林牙袋",
            "largeBackpack": "大背包",
            "compass": "附魔罗盘",
        }

        def item_bi(var_name):
            zh = store.zh_names.get(var_name, "")
            return zh if zh else var_name

        # делаем доступной в скрипте/экранах по имени item_bi(...)
        store.item_bi = item_bi

        # Собираем список предметов, которые есть у игрока.
        player_inventory_vars = [var for var in store.ru_names.keys() if getattr(store, var, 0) > 0]

        # Проверяем, есть ли у игрока хотя бы 4 предмета для обмена.
        if len(player_inventory_vars) < 4:
            renpy.say(lbg, "嗯，我看你手头的东西不够做笔像样的交换。等你更富了再来！")
            renpy.jump("choice_158")

        # --- ШАГ 1: ВЫБОР 4 ПРЕДМЕТОВ ИГРОКОМ ---
        renpy.say(lbg, "选择四样你想拿来交换的小玩意儿。只准四样，不多也不少！")

        store.selected_for_trade_vars = []
        available_to_select = list(player_inventory_vars)

        for i in range(4):
            menu_choices = [(item_bi(var), var) for var in available_to_select]
            menu_choices.append(("- 取消交换", "cancel_trade"))

            renpy.say(lbg, f"选择第 {i + 1} 件（共4件）：")
            chosen_var = renpy.display_menu(menu_choices)

            if chosen_var == "cancel_trade":
                renpy.jump("choice_158")

            store.selected_for_trade_vars.append(chosen_var)
            available_to_select.remove(chosen_var)

    lbg "嗯……提议不错。你想换什么？"

    # --- ШАГ 2: ВЫБОР ПРЕДМЕТА У ГНОМА ---
    menu:
        "[item_bi('bambooFlute')]":
            $ desired_item_var = "bambooFlute"
        "[item_bi('goblinTeethBag')]":
            $ desired_item_var = "goblinTeethBag"
        "[item_bi('goodLuckCharm')]":
            $ desired_item_var = "goodLuckCharm"
        "[item_bi('compass')]":
            $ desired_item_var = "compass"
        "[item_bi('largeBackpack')]":
            $ desired_item_var = "largeBackpack"
        "[item_bi('honeycombWithBeeswax')]":
            $ desired_item_var = "honeycombWithBeeswax"
        "算了，我改变主意了":
            jump choice_158

    $ desired_item_disp = item_bi(desired_item_var)

    lbg "所以，你想要「[desired_item_disp]」……让我想想……"
    e "矮人掷骰子，判断这笔交易对他有多划算。"

    # --- ШАГ 3: РАСЧЕТ СДЕЛКИ ---
    python:
        roll = renpy.random.randint(1, 6)

        selected_for_trade_vars = list(store.selected_for_trade_vars)
        player_inventory_vars = [var for var in store.ru_names.keys() if getattr(store, var, 0) > 0]

        if roll == 1:
            renpy.say(lbg, "不行不行！这四样东西我不感兴趣。")
            other_items_player_has = [var for var in player_inventory_vars if var not in selected_for_trade_vars]

            if not other_items_player_has:
                renpy.say(lbg, "你也没别的东西可拿来谈了……走吧！")
                renpy.jump("choice_158")
            else:
                renpy.say(lbg, "不过……我看你包里还有点别的。要不换个条件？")
                renegotiate_menu = [(item_bi(var), var) for var in other_items_player_has]
                renegotiate_menu.append(("- 不用了，我走了", "cancel_renegotiate"))

                renpy.say(lbg, f"我愿意用「{desired_item_disp}」换你其中一件。怎么样？")
                chosen_counter_offer_var = renpy.display_menu(renegotiate_menu)

                if chosen_counter_offer_var == "cancel_renegotiate":
                    renpy.jump("choice_158")
                else:
                    setattr(store, chosen_counter_offer_var, getattr(store, chosen_counter_offer_var, 0) - 1)
                    setattr(store, desired_item_var, getattr(store, desired_item_var, 0) + 1)
                    renpy.say(lbg, f"成交！你拿走「{desired_item_disp}」，我拿「{item_bi(chosen_counter_offer_var)}」。")
                    renpy.jump("barter_final_jump")

        elif 2 <= roll <= 5:
            item_to_lose_var = renpy.random.choice(selected_for_trade_vars)

            setattr(store, item_to_lose_var, getattr(store, item_to_lose_var, 0) - 1)
            setattr(store, desired_item_var, getattr(store, desired_item_var, 0) + 1)

            renpy.say(lbg, f"说定了！我拿走你的「{item_bi(item_to_lose_var)}」，你带走「{desired_item_disp}」。")
            renpy.jump("barter_final_jump")

        else:  # roll == 6
            renpy.say(lbg, f"嘿嘿，这可不够！像「{desired_item_disp}」这么值钱的东西，我要你两样小玩意儿！")
            renpy.call("barter_greedy_choice", desired_item_var=desired_item_var, selected_for_trade_vars=selected_for_trade_vars)
    return


label barter_greedy_choice(desired_item_var, selected_for_trade_vars):
    menu:
        "同意（交出2件随机物品）":
            python:
                items_to_lose_vars = renpy.random.sample(selected_for_trade_vars, 2)
                for var in items_to_lose_vars:
                    setattr(store, var, getattr(store, var, 0) - 1)

                setattr(store, desired_item_var, getattr(store, desired_item_var, 0) + 1)

                renpy.say(
                    lbg,
                    f"好选择！我拿走「{item_bi(items_to_lose_vars[0])}」和「{item_bi(items_to_lose_vars[1])}」。给你奖赏！"
                )
            jump barter_final_jump

        "拒绝这笔敲诈交易":
            lbg "随你便……那就谈不拢了。"
            jump choice_158
    return


label barter_final_jump:
    e "交易完成。你离开了矮人的小屋。"
    # --- ШАГ 7: ПЕРЕХОД ПОСЛЕ ПОЛУЧЕНИЯ ПРЕДМЕТА ---
    if desired_item_var == "bambooFlute":
        jump choice_304
    elif desired_item_var == "goblinTeethBag":
        jump choice_45
    elif desired_item_var == "goodLuckCharm":
        jump choice_20
    elif desired_item_var == "compass":
        jump choice_107
    elif desired_item_var == "largeBackpack":
        jump choice_166
    elif desired_item_var == "honeycombWithBeeswax":
        jump choice_200
    else:
        jump choice_158

# КОНЕЦ КОДА ДЛЯ СИСТЕМЫ БАРТЕРА



label choice_304:
    scene 324-1
    show BambooFlute
    $ countBarter += 1
    e "Флейта имеет довольно приятное звучание, но в остальном вполне обычный предмет."
    e "Она может пригодиться в вашем путешествии"
    if countBarter <= 2:
        jump choice_264
    else:
        jump choice_158

label choice_45:
    scene 324-1
    show GoblinTeethBag
    $ countBarter += 1
    $ goblinsTooth += 6
    $ giantsTooth += 1
    e "В сумке 6 зубов темных гоблинов."
    e "Вы пересыпаете их с ладони на ладонь и к вашей радости замечаете на дне сумки дополнительный бонус – зуб великана"
    e "Гном о нем, видимо, не знал"
    if countBarter <= 2:
        jump choice_264
    else:
        jump choice_158

label choice_20:
    scene 324-1
    show GoodLuckCharm
    e "Этот талисман настоящая находка."
    e "Он дает + 7 к уровню вашей удачи"
    $ luck += 7
    s "Теперь уровень вашей удачи - {color=#FF00FF}[luck]{/color}"
    if countBarter <= 2:
        jump choice_264
    else:
        jump choice_158

label choice_107:
    scene 324-1
    show EnchantedCompass
    e "Можете использовать этот артефакт, чтобы найти строки заклинания."
    e "Если последуете его указаниям, он сразу же приведет вас к человеку, который знает строчку заклинания."
    e "Но после этого он станет бесполезным."
    e "Вы решаете как можно скорее воспользоваться компасом"
    jump choice_319

label choice_166:
    scene 324-1
    $ largeBackpack += 1
    show LargeBackpack
    e "Этот рюкзак больше вашего, и вы можете заменить им свой старый рюкзак."
    e "В новый помещается больше предметов"
    e "Вы теперь не увидете сообщения о том, что из рюкзака нужно что-то выложить, чтобы что-то положить"
    if countBarter <= 2:
        jump choice_264
    else:
        jump choice_158

label choice_200:
    scene 324-1
    $ honeycombWithBeeswax += 50
    show HoneycombWithBeeswax
    e "Это приличный запас воска."
    e "Если будете использовать его при наложении заклинаний"
    e "Его хватит до самого конца приключения"
    if countBarter <= 2:
        jump choice_264
    else:
        jump choice_158

label choice_158:
    scene 158-1 with dissolve
    pause 0.5
    e "Вы осторожно выходите из хижины, но на улице никого нет."
    e "Вы можете спокойно продолжить свой путь"
    jump choice_89

label choice_56:
    scene 56-1 with dissolve
    pause 0.5
    e "Вы входите в Залы."
    e "Несмотря на раннее время суток, их заполняет шумная толпа."
    e "Никто не обращает на вас внимания, так как все заняты своими играми."
    e "Щелчок костей и стук Колеса Фортуны — это единственные звуки, которые можно четко различить над шумом толпы."
    menu:
        "Попытать счастья с Колесом Фортуны" if gold >= 1:
            jump choice_25
        "Попытать счастья за столом для игры в кости" if gold >= 1:
            jump choice_188
        "Покинуть Игорные Залы Влада":
            jump choice_39

label choice_25:
    scene 25-1 with dissolve
    pause 0.5
    e "Каждая игра в Колесо Фортуны обойдется вам 1 золотой."
    if gold < 1:
        e "У вас нет даже одной золотой монеты, чтобы сыграть. Вы решаете покинуть это место."
        jump choice_39

    e "Каждая игра в Колесо Фортуны обойдется вам в 1 золотую."
    $ gold -= 1
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    e "Сколько вы хотите попытаться выиграть?"
    menu:
        "5 золотых (1 проверка удачи, 1 мастерства)":
            $ checks_needed = 1
            $ prize = 5
            jump wheel_of_fortune_game
        "10 золотых (2 проверки удачи, 2 мастерства)":
            $ checks_needed = 2
            $ prize = 10
            jump wheel_of_fortune_game
        "20 золотых (3 проверки удачи, 3 мастерства)":
            $ checks_needed = 3
            $ prize = 20
            jump wheel_of_fortune_game
        "Я передумал":
            e "Вы решаете не рисковать и забираете свою монету обратно."
            $ gold += 1
            s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
            jump choice_39

label wheel_of_fortune_game:
    python:
        # Эта переменная будет отслеживать, прошли ли вы все проверки.
        all_tests_passed = True

        # --- Проверки Удачи ---
        renpy.say(e, "Сначала проверим вашу удачу!")
        for i in range(checks_needed):
            renpy.say(e, f"Испытание удачи {i+1} из {checks_needed}.")
            twodice = renpy.random.randint(1, 12)
            renpy.say(s, f"Уровень вашей удачи - {{color=#FF00FF}}{luck}{{/color}}, требуемый уровень удачи - {{color=#FF00FF}}{twodice}{{/color}}")

            if twodice <= luck:
                renpy.say(s, "Вам повезло! Колесо останавливается на выигрышном секторе.")
            else:
                renpy.say(s, "Вам не повезло! Стрелка проскакивает мимо нужного символа.")
                all_tests_passed = False

            luck -= 1
            renpy.say(s, f"Ваша удача немного истощилась. Теперь ее уровень - {{color=#FF00FF}}{luck}{{/color}}")

            # Если проверка провалена, нет смысла продолжать.
            if not all_tests_passed:
                break

        # --- Проверки Мастерства ---
        if all_tests_passed:
            renpy.say(e, "Теперь посмотрим на ваше мастерство!")
            for i in range(checks_needed):
                renpy.say(e, f"Испытание мастерства {i+1} из {checks_needed}.")
                twodice = renpy.random.randint(1, 20)
                renpy.say(s, f"Уровень вашего мастерства - {{color=#FF00FF}}{mastery}{{/color}}, требуемый уровень мастерства - {{color=#FF00FF}}{twodice}{{/color}}")

                if twodice <= mastery:
                    renpy.say(s, "Ваше мастерство позволило сделать задуманное! Вы точно знаете, когда остановить колесо.")
                else:
                    renpy.say(s, "Ваше мастерство не позволило сделать задуманное! Вы не смогли рассчитать нужный момент.")
                    all_tests_passed = False

                # Если проверка провалена, выходим из цикла.
                if not all_tests_passed:
                    break

    # --- Результат игры ---
    if all_tests_passed:
        e "Поздравляем! Вы прошли все испытания и выиграли [prize] золотых!"
        $ gold += prize
        s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    else:
        e "Увы, вы провалили одно из испытаний. В этот раз выигрыш ускользнул от вас."

    # --- Предложение сыграть снова ---
    menu:
        "Сыграть еще раз":
            jump choice_25
        "Покинуть игру":
            e "С вас достаточно азартных игр на сегодня."
            jump choice_39

label choice_188:
    scene 188-1 with dissolve
    pause 0.5
    $ dice = renpy.random.randint(1, 6)
    e "Стоимость игры составляет одну золотую"
    $ gold -= 1
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    e "Попробуйте угадать число, которое выпадет на кости"
    $ ans = renpy.input("试着猜出骰子将掷出的数字")
    $ ans = ans.strip()
    s "На кости выпало - {color=#FF00FF}[dice]{/color}"
    if ans == "1" and dice == 1:
        e "Вы выиграли!"
        $ gold += 10
        s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
        menu:
            "Сыграть еще раз":
                jump choice_188
            "Покинуть игровой зал":
                jump choice_39
    if ans == "2" and dice == 2:
        e "Вы выиграли!"
        $ gold += 10
        s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
        menu:
            "Сыграть еще раз":
                jump choice_188
            "Покинуть игровой зал":
                jump choice_39
    if ans == "3" and dice == 3:
        e "Вы выиграли!"
        $ gold += 10
        s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
        menu:
            "Сыграть еще раз":
                jump choice_188
            "Покинуть игровой зал":
                jump choice_39
    if ans == "4" and dice == 4:
        e "Вы выиграли!"
        $ gold += 10
        s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
        menu:
            "Сыграть еще раз":
                jump choice_188
            "Покинуть игровой зал":
                jump choice_39
    if ans == "5" and dice == 5:
        e "Вы выиграли!"
        $ gold += 10
        s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
        menu:
            "Сыграть еще раз":
                jump choice_188
            "Покинуть игровой зал":
                jump choice_39
    if ans == "6" and dice == 6:
        e "Вы выиграли!"
        $ gold += 10
        s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
        menu:
            "Сыграть еще раз":
                jump choice_188
            "Покинуть игровой зал":
                jump choice_39
    else:
        e "Вы проиграли!"
        menu:
            "Сыграть еще раз":
                jump choice_188
            "Покинуть игровой зал":
                jump choice_39

label choice_221:
    scene 221-1 with dissolve
    pause 0.5
    e "В горшке 18 золотых монет."
    e "Вы достаете их и берете себе."
    $ gold += 18
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    play sound "audio/221-1.mp3"
    pause 1
    e "Громкий скрип заставляет вас замереть на месте!"
    e "Статуя ожила, и ее рука опускается на вас!"
    e "Вы отпрыгиваете в сторону, избегая удара ладонью, и катитесь по земле."
    e "Встаете и видите, как бронзовый гигант спрыгивает со своего постамента и приближается к вам."
    jump choice_299

label choice_299:
    scene 299-1 with dissolve
    pause 0.5
    e "Вы атакуете существо."
    e "Статуя движется медленно, и вы легко подбегаете вплотную и наносите мощный удар ей в бок."
    e "Ваше оружие с лязгом врезается в бронзу и отскакивает назад"
    e "Статуя не пострадала, а вот вы едва не вывихнули запястье, теряете 1 очко Здоровья"
    $ health -= 1
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    if health <=0:
        jump game_over
    e "Бронзовая статуя замахивается рукой на вас, и, хотя вы отпрыгиваете в сторону, она слегка задевает вас."
    e "Теряете еще 2 очка Здоровья."
    $ health -= 2
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    if health <=0:
        jump game_over
    e "Вы наносите первый удар"
    jump choice_326

label choice_326:
    scene 299-1
    e "Вы не можете причинить вред этому огромному металлическому существу, просто нанося ему удары."
    e "Единственный способ победить - найти его единственное слабое место."
    e "Если вы внимательно следили за ним, то, возможно, поняли, где находится это слабое место."
    e "Куда нанесете удар?"
    menu:
        "Под правое колено":
            jump choice_265
        "В левую лодыжку":
            jump choice_278
        "В правое бедро":
            jump choice_35
        "Куда-нибудь еще":
            jump choice_93

label choice_265:
    scene 299-1
    e "Нет, это не слабое место статуи."
    e "Гигантское существо мощным ударом отбрасывает вас назад и сбивает с ног."
    e "Вы теряете 4 очка Здоровья."
    $ health -= 4
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    if health <=0:
        jump game_over
    e "Вы снова наносите удар по статуе!"
    jump choice_326

label choice_278:
    scene 299-1
    e "Нет, это не слабое место статуи."
    e "Гигантское существо пинком отбрасывает вас назад, подбрасывая в воздух, так что вы приземляетесь на его пьедестал."
    e "Вы теряете 3 очка Здоровья."
    $ health -= 3
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    if health <=0:
        jump game_over
    e "Вы снова наносите удар по статуе!"
    jump choice_326

label choice_35:
    scene 299-1
    e "Нет, это не слабое место статуи."
    e "Гигантское существо пинком отбрасывает вас назад."
    e "Вы теряете 4 очка Здоровья."
    $ health -= 4
    s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    if health <=0:
        jump game_over
    e "Вы снова наносите удар по статуе!"
    jump choice_326

label choice_93:
    scene 299-1
    menu:
        "Попробовать ее ударить: ниже пояса":
            jump choice_155
        "Попробовать ее ударить: под левое колено":
            jump choice_182

label choice_155:
    scene 299-1
    e "Вы наносите удар ниже пояса, но и там нет слабого места."
    e "Статуя подстерегает вас и хлопает руками, прижимая вас к своему телу."
    if health >= 10:
        e "Вы выдержали удар"
        e "Вы теряете 5 очка Здоровья."
        $ health -= 5
        s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
        if health <=0:
            jump game_over
        e "Вы понимаете, что со статуей вам не справиться."
        e "Ваш единственный шанс бросить все свое золото в горшок для пожертвований на пьедестале"
        $ gold = 0
        s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
        jump choice_146
    else:
        e "Удар оглушает вас, и бронзовая статуя растопчет вас, пока вы лежите на земле."
        jump game_over

label choice_182:
    scene 299-1
    e "Вы видите в этом месте заплатку на ноге!"
    e "Быстро, вы вставляете свое оружие в щель вокруг пластины и нажимаете, отрывая ее от тела."
    e "Прежде чем гигантское существо успевает среагировать"
    e "Металлическая пластина падает на землю, и из статуи вырывается струя газа."
    scene 182-1 with dissolve
    pause 0.5
    e "Оживляющий газ вытекает из гиганта, он покачивается и, наконец, падает на землю лицом вверх"
    e "Вы победили его и стали на 18 золотых богаче!"
    e "Восстановите 2 очка Удачи за это."
    $ luck += 2
    s "Теперь уровень вашей удачи - {color=#FF00FF}[luck]{/color}"
    menu:
        "Пойти налево к окраине города":
            jump choice_104
        "Пойти направо к Игорным Залам":
            jump choice_56

#label choice_214:

label choice_146:
    scene 221-1 with dissolve
    pause 0.5
    e "Бронзовая статуя смотрит, как вы бросаете свое золото в горшок."
    e "Она явно не знает, продолжать ли атаковать вас или вернуться на пьедестал."
    e "Пока она решает, вы можете сбежать по одной из улиц."
    menu:
        "Пойти налево к окраине города":
            jump choice_104
        "Пойти направо к Игорным Залам":
            jump choice_56

label choice_206:
    scene 192-2
    e "Дождавшись, когда стражник уйдет отдохнуть, вы открываете дверь и покидаете камеру"
    e "Забрав свои вещи и оружие, вы покидаете тюрьму и бежите прочь"
    show Elvin
    e "Эльвин сбегает вместе с вами, он очень вам благодарен и накладывает на вас заклинание везения"
    e "Восстановите свою Удачу до начального уровня."
    $ luck = 12
    s "Теперь уровень вашей удачи - {color=#FF00FF}[luck]{/color}"
    e "Вы оба продолжаете петлять по закоулкам некоторое время, но, в конце концов, расстаетесь"
    jump choice_135

label choice_50:
    scene 198-1
    e "Вы идете по краю площади, не сводя глаз с монумента"
    e "Когда вы проходите мимо очередной двери, вас хватают за руки и шею"
    cy "Похоже, у нас есть нарушитель!"
    cy "А мы, Красные Глаза, не любим злоумышленников."
    cy "Отправляйся в тюрьму к подобным тебе!"
    scene 192-1 with dissolve
    pause 0.5
    e "Вас волокут по боковым улочкам до большого квадратного здания"
    e "Заводят внутрь и запирают в камере"
    jump choice_143

label choice_275:
    scene 198-1
    e "Вы отступаете от монумента и осторожно идете вокруг него к дальней стороне площади"
    jump choice_135

label choice_319:
    scene 319-1 with dissolve
    pause 0.5
    e "Вы покидаете центральные районы города"
    if meal > 0:
        e "Вы присели на пень у дороги"
        e "Отдохнули и перекусили"
        $ meal -= 1
        s "Теперь количество вашей еды - {color=#FF00FF}[meal]{/color}"
        e "Ваш уровень здоровья увеличивется на два"
        $ health += 2
        s "Теперь ваш уровень здоровья - {color=#FF00FF}[health]{/color}"
    e "Рядом с хижинами слепой нищий просит подаяние."
    menu:
        "Бросить ему золотой" if gold > 0:
            jump choice_285
        "Пойти дальше к воротам":
            jump choice_148

label choice_285:
    scene 319-1
    e "Вы бросаете ему золотой, и он благодарит вас за доброту."
    $ gold -= 1
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    scene 285-1 with dissolve
    pause 0.5
    e "Присаживаетесь рядом, чтобы поговорить"
    play sound "audio/285-1.mp3"
    pause 1
    e "Но тут вы оба слышите визг, доносящийся сверху."
    pm "Нет!"
    pm "Только не эти проклятые гарпии!"
    pm "Неужели никогда не прекратятся мои мучения?"
    scene 285-2 with dissolve
    pause 0.5
    e "Взглянув на небо, вы видите двух крылатых тварей, парящих над вами"
    e "Это уродливые темнокожие существа с острыми когтями на руках и ногах"
    e "Вы оба вскакиваете на ноги"
    e "Пока вы раздумываете, что делать, нищий хватает свою клюку и начинает вслепую махать ею в воздухе"
    pm "Они хотят забрать мое золото!"
    pm "Разве вам не жалко слепого?"
    pm "Ох, незнакомец, ты же видишь эту мерзость?"
    pm "Ты поможешь мне?"
    scene 285-3 with dissolve
    pause 0.5
    e "Одна из гарпий стрелой бросается вниз и, вцепившись в голову нищего, бросает его на землю."
    menu:
        "Помочь ему":
            jump choice_97
        "Убежать прочь":
            jump choice_148

label choice_97:
    scene 285-3
    e "Вы вступаете в бой с крылатыми тварями"
    jump choice_118

label choice_118:
    scene 285-3
    e "Вы хватаетесь за свое оружие и наносите удары гарпиям, когда они спускаются вниз."
    $ enemies = [
        {"name": "第一鹰身女妖", "mastery": 7, "health": 6}, # Первая Гарпия
        {"name": "第二鹰身女妖", "mastery": 6, "health": 6} # Вторая Гарпия
    ]
    jump choice_118_fight

label choice_118_fight:
    if health <= 0:
        f "Твои силы иссякли в бою с гарпиями! Ты падаешь, сраженный их когтями."
        jump game_over

    $ living_harpies = [h for h in enemies if h["health"] > 0]
    if not living_harpies:
        f "Обе гарпии повержены! Ты стоишь над их телами, тяжело дыша. Твое здоровье: {color=#FF00FF}[health]{/color}, мастерство: {color=#FF00FF}[mastery]{/color}, удача: {color=#FF00FF}[luck]{/color}."
        jump choice_74

    $ current_enemy = renpy.random.choice(living_harpies)

    $ enemy_attack = renpy.random.randint(1, 12) + current_enemy["mastery"]
    $ player_attack = renpy.random.randint(1, 12) + mastery

    if enemy_attack == player_attack:
        f "Ты ([player_attack]) и [current_enemy['name']] ([enemy_attack]) скрещиваете оружие, но никто не ранен! Твое здоровье: {color=#FF00FF}[health]{/color}, здоровье врага: {color=#FF00FF}[current_enemy['health']]{/color}."
        jump choice_118_fight

    elif player_attack > enemy_attack:
        $ current_enemy["health"] -= 2
        if current_enemy["health"] > 0:
            f "Твой удар ([player_attack]) задевает [current_enemy['name']] ([enemy_attack])! Ты наносишь 2 урона. У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твое здоровье: {color=#FF00FF}[health]{/color}."
            if current_enemy["health"] <= 3 and magicalSelfLockingChain == 1:
                menu:
                    "Использовать волшебную цепь, чтобы обездвижить [current_enemy['name']]":
                        $ current_enemy["health"] = 0
                        $ magicalSelfLockingChain = 0
                        f "Ты метаешь волшебную цепь! Она обвивается вокруг ослабленной [current_enemy['name']], обездвиживая её. Ты наносишь решающий удар! Цепь использована."
                        jump choice_118_fight
                    "Продолжить бой без цепи":
                        pass
        else:
            f "Твой мощный удар ([player_attack]) сокрушает [current_enemy['name']] ([enemy_attack])! Враг повержен! Твое здоровье: {color=#FF00FF}[health]{/color}."
            jump choice_118_fight

        if current_enemy["health"] > 0:
            menu:
                "Использовать удачу для дополнительного урона":
                    $ luck_roll = renpy.random.randint(1, 12)
                    if luck_roll <= luck:
                        $ current_enemy["health"] -= 2
                        $ luck -= 1
                        if current_enemy["health"] > 0:
                            f "Удача на твоей стороне! Ты наносишь дополнительный урон (2). У врага осталось {color=#FF00FF}[current_enemy['health']]{/color} здоровья. Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                        else:
                            f "Удача помогает тебе! Мощный дополнительный удар (2 урона) добивает [current_enemy['name']]! Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                    else:
                        $ current_enemy["health"] += 1
                        $ luck -= 1
                        f "Удача отвернулась! [current_enemy['name']] восстанавливает 1 здоровье (теперь {color=#FF00FF}[current_enemy['health']]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                "Не использовать удачу":
                    pass
        jump choice_118_fight

    else: # player_attack < enemy_attack
        $ health -= 2
        if health > 0:
            f "[current_enemy['name']] наносит тебе удар ([enemy_attack])! Твоя защита ([player_attack]) не справляется. Ты теряешь 2 здоровья, осталось {color=#FF00FF}[health]{/color}."
        else:
            f "[current_enemy['name']] наносит сокрушительный удар ([enemy_attack])! Ты теряешь последние силы и падаешь."
            jump game_over

        menu:
            "Использовать удачу, чтобы смягчить урон":
                $ luck_roll = renpy.random.randint(1, 12)
                if luck_roll <= luck:
                    $ health += 1
                    $ luck -= 1
                    f "Удача спасает тебя! Ты восстанавливаешь 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                else:
                    $ health -= 1
                    $ luck -= 1
                    if health > 0:
                        f "Удача подвела! Ты теряешь дополнительное 1 здоровье (теперь {color=#FF00FF}[health]{/color}). Твоя удача снизилась до {color=#FF00FF}[luck]{/color}."
                    else:
                        f "Удача отвернулась в последний момент, и ты теряешь остатки сил!"
                        jump game_over
            "Не использовать удачу":
                pass
        jump choice_118_fight

label choice_74:
    jump choice_207

label choice_207:
    scene 207-1 with dissolve
    pause 0.5
    pm "Незнакомец, я не знаю как вас отблагодарить"
    pm "С тех пор, как я был проклят слепотой, меня мучили эти злобные демоны"
    e "Вы восстанавливаете дыхание"
    pm "Моя история печальна и поучительна"
    pm "Три года назад я был Седьмым Архонтом Кхара"
    pm "А потом на меня пало проклятие черных глаз…"
    i "Что вы знаете о заклинании, отпирающем Северные Врата?"
    pm "Да, я знаю о нем"
    pm "Потому что мне доверили хранить одну из строк"
    pm "Если ваш план состоит в том, чтобы покинуть город этим путем, я должен помочь вам"
    pm "Моя память уже не та, но, кажется, строка звучала так"
    pm "Грацией Курги и ..."
    pm "И чей-то гордостью."
    pm "Проклятье!"
    pm "Чья это была гордость?"
    pm "Одного из богов."
    pm "Грацией Курги и гордостью…"
    pm "Я сожалею, незнакомец"
    pm "Моя память подвела меня"
    pm "Не могу вспомнить имени этого бога"
    pm "Очевидно, вам придется пойти в храм Курги, он чуть дальше по дороге"
    pm "Там вы сможете поговорить с Богом Грации"
    pm "Но идти туда, означает рисковать своею жизнью!"
    pm "Я могу дать вам одну подсказку: левый глаз показывает путь"
    pm "Большего, я сказать не могу"
    i "Благодарю! Я бы хотел продолжить свой путь"
    pm "Если вы собираетесь попасть в Бакланд, я должен вам помочь"
    pm "Это было мое самое ценное имущество на протяжении последних лет"
    pm "Но я чувствую, что уже никогда не покину Кхар – а вам оно обязательно пригодится в вашем путешествии"
    show SnakeShapedRing
    e "Он отдает вам серебряное кольцо в форме змеи, обвивающейся вокруг пальца владельца."
    $ snakeShapedRing += 1
    e "Вы благодарите его еще раз и уходите"
    jump choice_148

label choice_148:
    scene 148-1 with dissolve
    pause 0.5
    e "Вы идете по дороге ведущей к Северным Вратам"
    e "Сейчас вы уже на самой окраине Кхара и можете увидеть впереди городскую Великую Стену, пересекающую ваш путь"
    e "Между вами и воротами остается только одно, но зато великолепное здание"
    e "Вы шагаете дальше и подходите к большому храму, стоящему у дороги"
    e "Это действительно впечатляющее зрелище"
    e "Тотемы древних богов выстроены в линию вдоль короткой дорожки перед входом"
    e "Само здание пирамидальное, его вершина упирается в небо"
    e "Фризы с горгульями и скульптурами из полированного металла опоясывают каждый этаж"
    e "Перед дверьми каменные скульптуры, изображающие невообразимых существ, сторожат вход"
    menu:
        "Войти в Святилище Курги":
            jump choice_73
        "Пройти к воротам":
            jump choice_109

label choice_73:
    scene 73-1 with dissolve
    pause 0.5
    e "Вы толкаете дверь, и она, скрипя петлями, распахивается"
    play sound "audio/73-1.mp3"
    pause 1
    e "Этот звук усиливается внутри полого храма, и его жуткое эхо не утихает еще несколько секунд"
    e "Вы осторожно всматриваетесь внутрь"
    e "Кажется, что здесь никого нет, не слышно никаких признаков чужой активности"
    e "Зайдя внутрь и закрыв за собой дверь, вы сталкиваетесь со зрелищем, от которого захватывает дух"
    e "Стены украшены яркими фресками, изображающими сцены из мифологии Кхара"
    e "Изысканные орнаменты из драгоценных металлов украшают ниши вокруг скамей, а богатые тканые гобелены покрывают каждую поверхность"
    e "Хитрая архитектура улавливает порывы ветра, и эфирный гул создает постоянный фоновый шум"
    play sound "audio/73-2.mp3"
    pause 5
    e "Четыре большие каменные горгульи с крыльями как у демонов наблюдают за святилищем со своих насестов"
    e "Высоко под потолком и в дальнем конце помещения видна важнейшая часть храма - алтарь"
    e "Ступени, ведущие к алтарю, кажется, были сделаны так, чтобы подчеркнуть центральную часть храма"
    e "С большим золотым идолом, изображающим Кургу"
    e "Интересная деталь - во всем мире Кургу почитают в женском обличии, и лишь в Кахабаде это божество считается мужчиной"
    menu:
        "Убедиться, что здесь никого нет":
            jump choice_168
        "Проверить святилище на наличие ловушек":
            jump choice_224
        "Посмотреть сможете ли вы найти здесь что-нибудь ценное, чтобы украсть":
            jump choice_205

label choice_168:
    scene 73-1
    e "Вы проверяете каждую нишу на наличие возможных укрытий и секретных проходов"
    e "Но ничего не находите"
    menu:
        "Осмотреть украшения на предмет чего-либо, что стоит украсть":
            jump choice_205
        "Подойти к алтарю":
            jump choice_122

label choice_122:
    scene 122-1 with dissolve
    pause 0.5
    e "Вы подходите к идолу"
    e "Он размером с взрослого человека"
    e "Ваше внимание привлекает доска с выгравированной надписью у него над головой"
    ta "{color=#7B68EE}Лицо Курги ты накрест поцелуй,{/color}"
    ta "{color=#7B68EE}Закончи на губах.{/color}"
    ta "{color=#7B68EE}Не ошибешься – обретешь ответ,{/color}"
    ta "{color=#7B68EE}Иначе превратишься в прах!{/color}"
    e "Кажется, это инструкция, выполнение которой позволит вам поговорить с богом."
    menu:
        "Рискнуть":
            jump choice_252
        "Покинуть храм":
            jump choice_109

label choice_252:
    scene 122-1
    e "Как следует из надписи, вы должны поцеловать идола в лицо"
    e "Но куда именно?"
    menu:
        "В лоб":
            jump choice_314
        "В правый глаз":
            jump choice_2
        "В левый глаз":
            jump choice_284
        "В правую щеку":
            jump choice_334
        "В левую щеку":
            jump choice_88
        "В нос":
            jump choice_296
        "В губы":
            jump choice_231

label choice_314:
    scene 122-1
    e "Теперь вы должны поцеловать его еще раз."
    e "Но куда?"
    menu:
        "В правый глаз":
            jump choice_2
        "В левый глаз":
            jump choice_163
        "В правую щеку":
            jump choice_334
        "В левую щеку":
            jump choice_88
        "В нос":
            jump choice_296
        "В губы":
            jump choice_231

label choice_163:
    scene 122-1
    e "Теперь вы должны поцеловать его еще раз."
    e "Но куда?"
    menu:
        "В лоб":
            jump choice_314
        "В правый глаз":
            jump choice_2
        "В правую щеку":
            jump choice_334
        "В левую щеку":
            jump choice_88
        "В нос":
            jump choice_296
        "В губы":
            jump choice_231

label choice_2:
    scene 122-1
    e "Теперь вы должны поцеловать его еще раз."
    e "Но куда?"
    menu:
        "В лоб":
            jump choice_314
        "В левый глаз":
            jump choice_163
        "В правую щеку":
            jump choice_334
        "В левую щеку":
            jump choice_88
        "В нос":
            jump choice_296
        "В губы":
            jump choice_231

label choice_284:
    scene 122-1
    e "Теперь вы должны поцеловать его еще раз."
    e "Но куда?"
    menu:
        "В лоб":
            jump choice_314
        "В правый глаз":
            jump choice_78
        "В правую щеку":
            jump choice_334
        "В левую щеку":
            jump choice_88
        "В нос":
            jump choice_296
        "В губы":
            jump choice_231

label choice_78:
    scene 122-1
    e "Теперь вы должны поцеловать его еще раз."
    e "Но куда?"
    menu:
        "В лоб":
            jump choice_52
        "В левый глаз":
            jump choice_163
        "В правую щеку":
            jump choice_334
        "В левую щеку":
            jump choice_88
        "В нос":
            jump choice_296
        "В губы":
            jump choice_231

label choice_52:
    scene 122-1
    e "Теперь вы должны поцеловать его еще раз."
    e "Но куда?"
    menu:
        "В правый глаз":
            jump choice_2
        "В левый глаз":
            jump choice_163
        "В правую щеку":
            jump choice_334
        "В левую щеку":
            jump choice_88
        "В нос":
            jump choice_296
        "В губы":
            jump choice_141

label choice_141:
    scene 122-1
    e "Вы целуете идола в губы, и он открывает глаза"
    e "Его губы не шевелятся, но вы слышите его мягкий голос"
    idd "Незнакомец, ты не из моей паствы"
    idd "Тем не менее, ты завершил ритуал и я должен ответить на один твой вопрос"
    e "Что вы спросите?"
    menu:
        "Кто знает заклинание, открывающее ворота на север?":
            jump choice_31
        "Что ждет вас в Бакланде?":
            jump choice_266
        "Как зовут бога гордости?":
            jump choice_101
        "Как пройти мимо стражников Северных Врат?":
            jump choice_193

label choice_334:
    scene 122-1
    e "Теперь вы должны поцеловать его еще раз."
    e "Но куда?"
    menu:
        "В лоб":
            jump choice_314
        "В правый глаз":
            jump choice_2
        "В левый глаз":
            jump choice_163
        "В левую щеку":
            jump choice_88
        "В нос":
            jump choice_296
        "В губы":
            jump choice_231

label choice_88:
    scene 122-1
    e "Теперь вы должны поцеловать его еще раз."
    e "Но куда?"
    menu:
        "В правый глаз":
            jump choice_2
        "В левый глаз":
            jump choice_163
        "В правую щеку":
            jump choice_334
        "В левую щеку":
            jump choice_88
        "В нос":
            jump choice_296
        "В губы":
            jump choice_231


label choice_296:
    scene 122-1
    e "Теперь вы должны поцеловать его еще раз."
    e "Но куда?"
    menu:
        "В лоб":
            jump choice_314
        "В правый глаз":
            jump choice_2
        "В левый глаз":
            jump choice_163
        "В правую щеку":
            jump choice_334
        "В левую щеку":
            jump choice_88
        "В губы":
            jump choice_231

label choice_231:
    scene 122-1
    e "Вы целуете губы идола, при этом вы слышите тихий щелчок"
    e "Ваши глаза широко открываются, когда вы получаете резкий удар в горло"
    scene 231-1 with dissolve
    pause 0.5
    e "Вы пытаетесь крикнуть, но быстродействующий яд на кончике дротика"
    e "Вылетевшего из золотого рта идола, уже парализовал ваши связки"
    e "Вы падаете на пол без сознания, и уже не проснетесь"
    e "Ваше путешествие заканчивается в этом храме"
    e "Такова цена ошибки в ритуале поцелуев Курги"
    jump game_over

label choice_224:
    scene 73-1
    e "Вы ищете любые признаки ловушек"
    scene 224-1 with dissolve
    pause 0.5
    e "Подойдя к ступеням алтаря"
    e "Вы останавливаетесь у большого причудливого круга, вплетенного в покрытие на полу"
    e "Чтобы подтвердить ваши подозрения, вы бросаете камешек в круг и улыбаетесь"
    e "Когда видите, как он исчезает"
    e "Вы обнаружили портал, который, без сомнения, поглотил бы вас, если бы зашли в него"
    e "Запомните, что надо избегать этого места"
    menu:
        "Убедиться, что здесь никого нет":
            jump choice_168
        "Посмотреть, сможете ли вы найти здесь что-нибудь ценное, чтобы украсть":
            jump choice_205
        "Изучить идола":
            jump choice_122

label choice_205:
    scene 73-1
    e "С чего бы начать?"
    e "Храм украшен таким количеством ценных артефактов, что у вас глаза разбегаются"
    e "Все взять с собой не получится, надо выбрать самое ценное"
    e "Скульптуры, блюда, подсвечники и щиты окружают вас, все из чистого золота"
    scene 205-1 with dissolve
    pause 0.5
    e "Вы подходите к столу, покрытому шелковой тканью, на котором стоят хрустальный графин и четыре золотых кубка"
    e "Вы берете один и крутите его в руках"
    e "Внезапно вы понимаете, что гул ветра стал громче"
    play sound "audio/73-2.mp3"
    pause 5
    e "Оглядываетесь по сторонам, гобелены развеваются как при сильном ветре, хотя раньше воздух был неподвижен"
    scene 205-2 with dissolve
    pause 0.5
    e "Вы бросаете взгляд на горгулий и немедленно ставите кубок обратно!"
    e "Все четверо уже повернулись к вам и медленно оживают, расправляя крылья за спиной."
    scene 73-1 with dissolve
    pause 0.5
    e "Когда вы возвращаете кубок на место, все успокаивается, и горгульи возвращаются на свои насесты"
    jump choice_122

label choice_109:
    scene 148-1
    e "Миновав храм, вы приближаетесь к границе города"
    e "Огромные Северные Врата нависают над вами"
    e "Они хорошо охраняются, и вам нужен план, чтобы миновать стражу"
    jump choice_175

label choice_175:
    scene 175-1 with dissolve
    pause 0.5
    e "Перед воротами группами по три человека патрулируют городские стражники"
    e "Вы стоите за деревом и ждете удобного момента"
    e "Вскоре один из патрулей останавливается между вами и Вратами"
    e "Они с пренебрежением смотрят на вас"
    sg "Ворота заперты, простак"
    sg "Так что поворачивай и вали обратно в город"
    e "Вы не решаетесь на бой с ними, другие патрули придут им на помощь"
    e "Вы решаете предложить им взятку"
    jump choice_157

label choice_31:
    scene 122-1
    e "Вы наклоняетесь к губам идола и слышите ответ"
    idd "Заклинание знает только Сансас, Первый Архонт Кхара"
    idd "Но тебе будет мало проку от этого знания, его сейчас нет в городе"
    idd "Он отплыл вверх по Джабаджи к озеру Лумле"
    e "Вы проклинаете себя за то, что задали явно не тот вопрос и получили бесполезный ответ"
    e "Покинув святилище Курги, вы поворачиваете к Северным Вратам"
    jump choice_109

label choice_266:
    scene 122-1
    e "Вы подносите ухо ко рту идола, чтобы услышать ответ бога"
    idd "Незнакомец"
    idd "Тебе не судьба попасть в Бакланд"
    idd "Ты не знаешь заклинание, открывающее Северные Врата"
    idd "Тебе лучше вернуться и начать свой путь заново"
    e "Этот ответ действительно разочаровывает"
    e "Вы можете начать это приключение заново (для этого начните новую игру)"
    e "Или отправиться на север к воротам в надежде, что бог ошибся"
    jump choice_109

label choice_101:
    scene 122-1
    e "Идол отвечает на ваш вопрос"
    idd "Бог Гордости – мой собственный брат"
    idd "Его зовут Дварга, он потерял благосклонность в нашем кругу божеств"
    idd "И народ Кхара почти целое столетие не поклоняется ему"
    e "Будет ли польза для вас от этой информации?"
    e "В любом случае вопрос был задан, и остается только покинуть храм"
    jump choice_109

label choice_193:
    scene 122-1
    e "Бог говорит с вами губами идола"
    idd "Стража Северных Врат – буйный сброд"
    idd "Горе тебе, если свяжешься с ними!"
    idd "Но они недобросовестны и больше заботятся о своих интересах, чем о безопасности города"
    idd "Можешь отвлечь их заклинанием или предложить по 3 золотых на брата, чтобы они отвернулись, пока ты идешь к воротам"
    e "Вы запоминаете эту информацию и покидаете храм"
    jump choice_109

label choice_157:
    scene 175-1
    if gold < 3:
        e "У вас нет денег на взятку, дальше вы не пройдете"
        jump game_over
    e "Сколько вы предложите?"
    menu:
        "1 золотая монета каждому" if gold >= 3:
            jump choice_80
        "По 3 золотых каждому" if gold >= 9:
            jump choice_287
        "По 5 золотых каждому" if gold >= 15:
            jump choice_113

label choice_80:
    scene 175-1
    e "Они смеются над вашим скудным предложением"
    sg "Нам предлагают взятку, братья, или этот путешественник просто подает нам милостыню?"
    e "Он хватает ваши три монеты и кладет себе в карман"
    $ gold -= 3
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    sg "Если мы ради тебя будем смотреть в другую сторону"
    sg "Тебе лучше сделать так, чтобы оно того стоило"
    sg "Дай нам еще по 5 золотых каждому!"
    if gold < 15:
        e "У вас нет денег на взятку, дальше вы не пройдете"
        jump game_over
    else:
        jump choice_113

label choice_287:
    scene 175-1
    e "Они смотрят друг на друга, явно пытаясь решить, смогут ли они получить от вас больше золота"
    sg "Хорошо, путешественник"
    sg "но то, что ты хочешь сделать, делай быстро"
    e "Они принимают ваше предложение и уходят прочь от ворот, предварительно получив от вас 9 золотых"
    $ gold -= 9
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    e "Теперь у вас есть немного времени, чтобы подойти к воротам и попробовать открыть их"
    jump choice_271

label choice_113:
    scene 175-1
    e "Их глаза загораются, когда вы достаете из своего кошелька 15 золотых монет"
    $ gold -= 15
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    sg "Должно быть, знатный человек, а, братья?"
    sg "Делай, что хочешь, путешественник."
    sg "У нас есть дела поважнее, не так ли?"
    e "Он уводит двух других вдоль стены, давая вам возможность подойти к воротам"
    jump choice_271

label choice_271:
    scene 271-1 with dissolve
    pause 0.5
    e "Вы подходите к темным Северным Вратам Кхара"
    e "В нескольких шагах от ворот вы останавливаетесь как вкопанный, услышав призрачный голос"
    ga "Стой, незнакомец!"
    e "Вы смотрите по сторонам, но никого не видно"
    e "Неужели сами ворота обращаются к вам!"
    ga "Ты не можешь пройти через эти ворота, они заперты с помощью волшебства"
    ga "Если не знаешь открывающего заклинания, следующий шаг вперед будет означать для тебя мгновенную смерть"
    e "Если вы знаете все четыре строки заклинания, разместите их в правильном порядке и прочитайте перед воротами"
    e "Три цифры скрыты внутри этих строк"
    $ ans = renpy.input("请输入咒语行中的数字")
    $ ans = ans.strip()
    if ans == "412":
        jump choice_412
    else:
        e "Вы не знаете или не поняли заклинания"
        e "Вы не сможете вовремя покинуть Кхар, ваша миссия провалена…"
        jump game_over

label choice_412:
    scene 271-1
    e "Затаив дыхание, вы ждете, чтобы увидеть, правильно ли произнесли заклинание"
    play sound "audio/412-1.mp3"
    pause 1
    e "Вы слышите скрип, который становится все громче"
    e "Подозревая ловушку, вы оглядываетесь вокруг, но бояться нечего:"
    e "Ворота слегка раздвинулись, открыв в середине узкий проход, из которого струится свет вечернего солнца!"
    e "Вам удалось открыть ворота, и эта часть вашего путешествия почти закончена"
    jump choice_511

label choice_511:
    scene 271-1
    scene 511-1 with dissolve
    pause 0.5
    e "Ворота медленно открываются перед вами"
    e "Вы преодолели опасности смертоносного города, первая половина вашего путешествия завершена"
    e "Через ворота вы можете увидеть огромные просторы Бакланда, раскинувшиеся перед вами"
    e "Великие равнины Бадду-Бак являются следующим этапом вашей миссии"
    e "Полученный вами опыт будет неоценимым подспорьем для вас в пути к озеру Илклала."
    e "Вы вспоминаете слова сержанта Старших Дозорных, сказанных вам в Форпостном Городке"
    show SeniorPatrolOfficerOutpostTown
    spoot "Миновав Кхар, вы должны пересечь Бакланд"
    spoot "Земли про которые мне ничего неизвестно"
    spoot "Но говорят, что день и ночь в Бакланде контролируются не солнцем"
    spoot "А сверхъестественными силами, также имейте в виду, что"
    spoot "После того как вы покинете Кхар, за вами наверняка будут следить"
    e "Звон доспехов позади выводит вас из задумчивости, стража возвращается"
    e "Бросив последний взгляд на город, вы шагаете через ворота"
    e "Впереди темные облака тяжело бегут по небу. Вы делаете первый шаг по земле Бакланда"
    e "Вы победили!"
    jump game_win

label choice_127:
    scene 127-1 with dissolve
    pause 0.5
    e "Следуя по улице, вы вскоре подходите к колодцу"
    e "С ворота вниз свисает веревка, и когда подходите ближе"
    e "Вы слышите поющий женский голос"
    e "Похоже, он доносится из колодца"
    ww "Хочешь узнать, что случиться с тобой?"
    ww "Брось мне в колодец один золотой"
    menu:
        "Бросить в колодец монету" if gold >= 1:
            jump choice_217
        "Пройти мимо":
            jump choice_319

label choice_217:
    scene 127-1
    e "Вы бросаете монету в колодец"
    $ gold -= 1
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    e "Лишь через несколько секунд слышите, как она падает в воду"
    e "Колодец, видимо, очень глубокий"
    e "Затем женский голос снова поет"
    ww "Если еще одну бросишь"
    ww "Выполню все, что попросишь!"
    menu:
        "Бросить еще один золотой" if gold >= 1:
            jump choice_152
        "Уйти":
            jump choice_319

label choice_152:
    scene 127-1
    $ gold -= 1
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    ww "Брось еще монету, милый."
    ww "За это дам я тебе больше силы"
    menu:
        "Бросить еще один золотой" if gold >= 1:
            jump choice_295
        "Уйти":
            jump choice_319

label choice_295:
    scene 127-1
    $ gold -= 1
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    ww "Если еще мне монету добудешь,"
    ww "Про боль и страдания ты позабудешь."
    menu:
        "Бросить еще один золотой" if gold >= 1:
            jump choice_315
        "Уйти":
            jump choice_319

label choice_315:
    scene 127-1
    $ gold -= 1
    s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
    ww "Последнюю монету у тебя я прошу,"
    ww "И все твои трудности мигом решу."
    menu:
        "Бросить еще один золотой" if gold >= 1:
            jump choice_152
        "Уйти":
            jump choice_319

label choice_16:
    scene 47-1 with dissolve
    pause 0.5
    e "Выходя из склепа, вы осторожно огибаете мерцающий круг и покидаете кладбище"
    jump choice_127

label choice_104:
    scene 104-1 with dissolve
    pause 0.5
    e "Вы продолжаете идти по дороге, пока странное зрелище не заставляет вас остановиться"
    e "Прямо посередине дороги лежит куча земли и камней высотой около восемнадцати дюймов"
    e "Она образует круг около трех футов в поперечнике, а его поверхность черная и блестящая"
    menu:
        "Рассмотреть кучу":
            jump choice_65
        "Пройти мимо":
            jump choice_319

label choice_65:
    scene 104-1
    e "Блестящая поверхность выглядит как лужа мерцающей черной жидкости"
    e "Пока вы вглядываетесь в нее, у вас за спиной раздаются шаги"
    iw "Так ты, незнакомец, интересуешься нашими порталами, а?"
    iw "Ну, вот в них мы сваливаем всякий мусор - и любых нежелательных незнакомцев!"
    e "Прежде чем успеваете обернуться, две руки толкают вас в круг"
    jump choice_270

label choice_39:
    scene 39-1 with dissolve
    pause 0.5
    e "На выходе из игорных залов вы проходите мимо двери с надписью «Комната портала»"
    menu:
        "Выяснить, что это такое":
            jump choice_112
        "Просто уйти":
            jump choice_197

label choice_112:
    scene 112-1 with dissolve
    pause 0.5
    e "Вы осторожно открываете дверь"
    e "Внутри вы видите небольшую комнату"
    e "А на полу в центре находится мерцающий черный круг, примерно три фута в поперечнике"
    e "Прежде чем вы успеваете среагировать"
    e "Вас хватает могучий охранник, стоящий прямо за дверью"
    show SecurityGuardOfGamblingHalls
    sggh "Еще один источник беспокойства, а?"
    e "Охранник толкает вас в центр комнаты"
    e "Вы ожидаете услышать какой-то всплеск, когда приземляетесь в черном круге"
    e "Но к вашему удивлению обнаруживаете, что в нем нет никакой жидкости"
    jump choice_270

label choice_197:
    scene 197-1 with dissolve
    play sound "audio/197-1.mp3"
    pause 5
    e "Снаружи шумит уличный рынок"
    menu:
        "Пройтись вдоль прилавков и посмотреть на товары":
            jump choice_226
        "Последовать по дороге к окраинам Кхара":
            jump choice_83

label choice_226:
    scene 197-1
    e "Еда, оружие и всевозможные побрякушки – вот что предлагает вам рынок"
    menu:
        "Купить еду (3 монеты за порцию)" if gold >= 3:
            $ gold -= 3
            s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
            $ meal += 1
            s "Теперь количество вашей еды - {color=#FF00FF}[meal]{/color}"
            jump choice_226_a
        "Купить лук и колчан со стрелами с серебряными наконечниками (5 монет)" if gold >= 5:
            $ gold -= 5
            s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
            $ bowAndArrows += 1
            jump choice_226_a
        "Купить превосходный двуручный меч (4 монет)" if gold >= 4:
            $ gold -= 4
            s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
            $ twoHandedSword += 1
            jump choice_226_a
        "Купить огниво для разжигания костров (2 монет)" if gold >= 2:
            $ flint += 1
            $ gold -= 2
            s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
            jump choice_226_a
        "Купить бутылку с антидотом от змеиного яда (3 монет)" if gold >= 3:
            $ antidoteSnakeVenom += 1
            $ gold -= 3
            s "Теперь количество вашего золота - {color=#FF00FF}[gold]{/color}"
            jump choice_226_a

label choice_226_a:
    scene 197-1
    menu:
        "Купить еще что-нибудь":
            jump choice_226
        "Двинуться дальше":
            jump choice_162

label choice_162:
    jump choice_83

label choice_135:
    scene 135-1 with dissolve
    pause 0.5
    e "Путь вперед ведет по улице, вдоль которой расположен рынок."
    menu:
        "Взглянуть, что здесь предлагают":
            jump choice_226
        "Пойти дальше":
            jump choice_83
        "Зайти в большое здание слева от вас, вывеска на котором гласит «Игорные Залы Влада»":
            jump choice_56

label game_win:
    show screen victory
    pause 5.0
    $ renpy.full_restart()
    return

    # Добавляем небольшую паузу для драматического эффекта
    pause 2.0

    # Это Python-блок, поэтому ставим знак $
    # Эта команда перезапускает игру и отправляет в главное меню
    $ renpy.full_restart()

label game_over:
    show screen game_over
    pause
    return

label show_interstitial_ad:
    python:
        # 1. Сбрасываем флаг перед вызовом
        persistent.ad_result = None

        # 2. Определяем Python-функцию, которая будет вызвана из JS по завершении
        def interstitial_finished_callback():
            persistent.ad_result = "finished"

        # 3. "Пробрасываем" эту функцию в JavaScript
        renpy.emscripten.run_script(
            'window.onInterstitialFinished = () => { renpy.python.interstitial_finished_callback(); };'
        )

        # 4. Вызываем JS-функцию для показа рекламы
        renpy.javascript("showInterstitial();")

    # 5. Ставим игру на паузу и ждем, пока JS не вызовет наш коллбэк
    $ renpy.pause(hard=True)
    while persistent.ad_result is None:
        $ renpy.pause(0.1)

    # 6. Сбрасываем флаг для будущих вызовов (хорошая практика)
    $ persistent.ad_result = None

    # 7. Просто возвращаемся к основному потоку игры
    return

label ad_closed_callback:
    # Этот код выполнится, когда закроется полноэкранная реклама.
    # Обычно здесь ничего делать не нужно, кроме возврата.
    return

label ad_error_callback:
    # Этот код выполнится, если реклама не загрузилась.
    # Мы тоже просто возвращаемся, чтобы игра не зависла.
    e "Не удалось загрузить рекламу. Продолжаем..."
    return
