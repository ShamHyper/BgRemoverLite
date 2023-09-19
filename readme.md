# BgRemoverLite
Програма для удаления заднего фона картинки с помощью нейросети u2net и библиотеки rembg
## Установка
### Способ #1:
С помощью Git:
```git clone https://github.com/ShamHyper/BgRemoverLite/```
### Способ #2:
Ручная установка из https://github.com/ShamHyper/BgRemoverLite/releases 
(файл LastRelease.zip)
## Требования
1. Python 3.10+ (https://www.python.org/downloads/)
2. ПК с Windows 10 и выше
## Запуск
1. После клонирования/распаковки програмы в удобное место запускаем файл **run.bat**
2. Ожидайте установки всех необходимых библиотек
3. Напишите + или - в зависимости от того, что вам нужно: "+" будет брать исходные картинки из папки input, а "-" потребует указание пути к исходным картинкам
4. После выбора, вам нужно будет подождать загрузки модели ИИ для удаления фона
5. Подождите завершение удаления фонов с картинок
## Ссылки, информация, ответы на частые вопросы
Модель u2net - https://github.com/xuebinqin/U-2-Net

Библиотека rembg - https://pypi.org/project/rembg/

> [!IMPORTANT]
> Вопрос: удаляются ли исходники картинок?
> Ответ: нет, не удаляются

> [!IMPORTANT]
> Вопрос: какие форматы картинок поддерживаются?
> Ответ: по идее, все самые распространёные, так как в конечном итоге картинка конвертируется в формат .png

> [!IMPORTANT]
> Вопрос: что используется для рендера картинок?
> Ответ: пока что только процессор, в будущем планируется переход на GPU версию

> [!IMPORTANT]
> Вопрос: как можно связаться с тобой если я столкнусь с проблемой?
> Ответ: можно оставить запрос в - https://github.com/ShamHyper/BgRemoverLite/issues или написать сообщение на моём дискорд сервере - https://discord.gg/xbZEbdakB6




