import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType

# Вставьте ваш токен, полученный в настройках группы
token = "vk1.a.kloP8Rr-tp5OspSm8G8GyRiTN5rCw_JDZDSChkgFd3Qem3E3LabXAcTY5-C63_zhl7j1zPFqrMg-DSOU12thW4AY-VCBKl1Vr0tQYvC-D30zCy41aguWa0QOXHrGUA1wywe2iAf96HmC2VLqejsxc9tiaeGL4cQyL5ttj5GxMFczkQnZZJHPENOro0ly0EudO0_j67W2NZeZy6P25nGYZw"

# Авторизация
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


wordList = ["аэропОрты", "бАнты", "бОроду", "бухгАлтеров", "бухгАлтера", "вероисповЕдание", "водопровОд", "газопровОд", "граждАнство", "дефИс", "дешевИзна", "диспансЕр",  "договорЁнность", "докумЕнт", "досУг", "еретИк", "жалюзИ", "знАчимость", "Иксы", "каталОг", "квартАл", "киломЕтр", "кОнусов", "коРысть", "крАны", "кремЕнь", "кремнЯ", "лЕкторов","лОктя","лыжнЯ","мЕстостей","намЕрение","нЕдруг","недУг","некролОг","нЕнависть","нефтепровОд","новостЕй","нОгтя","Отрочество","партЕр","портфЕль","придАное","призЫв","свЁкла","сирОты","созЫв","сосредотОчение","срЕдства","стАтуя","столЯр","тамОжня","тОрты","тУфля","цемЕнт","цЕнтнер","цепОчка","шАрфы","шофЁр","экспЕрт","вернА","знАчимый","красИвее","красИвейший","кУхонный","оптОвый","прозорлИвый","прозорлИва","слИвовый","бралА","брАлась","взялА","взялАсь","влилАсь","ворволАсь","ворвАться","воспринЯть","воссоздАть","вручИт","гналА","гналАсь","добралА","дождалАсь","ждалА","закУпорить","занЯть","зАнял","занялА","зАняли","заперлА","запломбировАть","защемИт","звалА","звонИт","кАшлсянуть","клАла","клЕить","крАлась","кровоточИть","глалА","лилА","лилАсь","наделИт","надорвалАсь","надорвАться","назвалАсь","назвАться","накренИтся","налилА","нарвалА","начАть","нАчал","нАчала","нАчили","обзвонИт","облегчИть","облилАсь","обнялАсь","обогналА","ободралА","одолжИть","озлОбить","оклЕить","окружИт","опОшлить","освЕдомиться","отбылА","отдалА","откУпорить","отозвалА","отозвАться","перезвонИт","перелилА","плодоносИть","пломбировАть","повторИт","позвалА","понялА","послАла","прибЫть","прИбыл","прибылА","прИбыли","принЯть","рвалА","сверлИт","снялА","создалА","сорвалА","убралА","углубИть","укрепИт","чЕрпать", "щемИт","щЁлкать"]

print("Бот запущен...")


ochki = 0

series = 0
maxSeries = 0

currentWord = ""


hasWorld = False

wordListCurrent = wordList.copy()
errorWords = []



# Слушаем события (новые сообщения)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        # Получаем текст сообщения и ID пользователя
        user_message = event.text
        user_id = event.user_id
        
        # Логика ответов
        if "повтор" in user_message :
            vk.messages.send(user_id=user_id, message=f"ошибки: ".join(errorWords), random_id=0)
            continue

        if hasWorld:
            hasWorld = False
            
            if user_message == currentWord:
                
                series+=1
                ochki+=series
                
                vk.messages.send(user_id=user_id, message=f"Красава, всё верно: {currentWord}. Теперь у тебя {ochki}. Текущая серия {series} слов подряд! ", random_id=0)
                
            else:
                series = 0
                
                
                vk.messages.send(user_id=user_id, message=f"Не, фигня, правильно: {currentWord}", random_id=0)
                
                errorWords.append(currentWord)
        if hasWorld == False:
            currentWord = random.choice(wordListCurrent)
            currentWordL = currentWord.lower()
            wordListCurrent.remove(currentWord)
            
            if len(wordListCurrent) == 0:
                wordListCurrent = wordList.copy()
            
            if len(errorWords) !=0 and random.randint(0,3) == 2:
                currentWord = random.choice(errorWords)
                currentWordL = currentWord.lower()
                errorWords.remove(currentWord)
                
                
            vk.messages.send(user_id=user_id, message=f"Куда поставим ударение {currentWordL}?", random_id=0)
            
            hasWorld = True
            
                
