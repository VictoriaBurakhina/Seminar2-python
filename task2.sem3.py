#Задача 2.В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

text = "Борис Сергеевич рассмеялся:Очень интересно! Ну-ка, поведай тайну своей души. Теперь твоя очередь, принимай эстафету.\'"\
       "Итак, начинай! Что же ты любишь?Мишка поёрзал на подоконнике, потом откашлялся:Я люблю булки, плюшки, батоны и кекс! \'" \
       "Я люблю хлеб, и торт, и пирожные, и пряники — хоть тульские, хоть медовые, хоть глазированные. Сушки люблю тоже, и баранки,\'" \
       " бублики, пирожки с мясом, повидлой, капустой и с рисом. Я горячо люблю пельмени, и особенно ватрушки, если они свежие, но чёрствые тоже ничего. \'" \
       "Можно овсяное печенье и ванильные сухари.А ещё я люблю кильки, сайру, судака в маринаде, бычки в томате, частик в собственном, соку, икру баклажанную, \'" \
       "кабачки ломтиками и жареную картошку.Варёную колбасу люблю прямо безумно! Если докторская — на спор съем хоть целое кило! И столовую люблю, и чайную, и зельц,\'" \
       " и копчёную, и полукопчёную, и сырокопчёную! Эту вообще я люблю больше всех. Очень люблю макароны с маслом, вермишель с маслом, рожки с маслом, сыр с дырочками и без дырочек,\'" \
       " с красной коркой или с белой — всё равно.Люблю вареники с творогом, творог солёный, сладкий, кислый, люблю яблоки тёртые с сахаром, а то яблоки одни, самостоятельно, а если яблоки очищенные,\'" \
       " то люблю сначала съесть яблочко, а уж потом, на закуску — кожуру!Люблю печёнку, котлеты, селёдку, фасолевый суп, зелёный горошек, варёное мясо, ириски, сахар, чай, джем, боржом, газировку с сиропом, \'" \
       "яйца всмятку, вкрутую, в мешочек, могу и сырые. Бутерброды люблю, прямо с чем попало, особенно если толсто намазать картофельным пюре или пшённой кашей. Так... Ну, про халву — говорить не буду. Кто её не любит? \'" \
       "А ещё я люблю утятину, гусятину, индятину... Ах, да! Я всей душой люблю мороженое. За семь, за девять, за тринадцать, за пятнадцать, за девятнадцать. За двадцать две и за двадцать восемь.\'" \
       "Мишка обвёл глазами потолок и перевёл дыхание. Видно, он уже здорово устал. Но Борис Сергеевич пристально смотрел на него, и Мишка поехал дальше. \'" \
       "Он бормотал:Крыжовник, морковку, кету, горбушу, репу, борщ, пельмени, хотя пельмени я уже говорил, бульон, бананы, хурму, компот, сосиски, вареники, колбасу, хотя колбасу уже тоже говорил...\'" \
       "Мишка выдохся и замолчал. По его глазам было видно, что он ждёт, когда Борис Сергеевич его похвалит. Но тот смотрел на Мишку немного недовольно и даже как будто строго.\'" \
       " Он тоже словно ждал чего-то от Мишки, что, мол, Мишка ещё скажет. Но Мишка молчал. У них получилось, что они друг от друга чего-то ждали и молчали.\'" \
       "Первый не выдержал Борис Сергеевич:Что ж, Миша, — сказал он, — ты многое любишь, спору нет, но всё, что ты любишь, оно какое-то одинаковое, чересчур съедобное, что ли. Получается, что ты любишь целый продуктовый магазин. И только... А люди? Кого ты любишь? Или из животных?\'" \
       "Тут Мишка весь встрепенулся и покраснел:Ой, — сказал он смущённо, — чуть не забыл! Ещё — котят! И бабушку!"

text = "".join([i for i in text.lower() if i.isalpha() or i == " "])
text = text.split()

n = 10
myText = dict()
for i in text:
    myText[i] = myText.get(i, 0) + 1
# сортировка по количеству и по алфавиту
sortWord = sorted(myText.items(), key=lambda x: (-x[1], x[0]))[:n]
for word, count in sortWord:
    print(f"Слово {word} встречается {count} раз")