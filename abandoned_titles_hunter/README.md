RU:
# Охотник на Заброшенные Тайтлы с MangaLib

Этот скрипт автоматизирует процесс поиска заброшенных манг на [MangaLib](https://mangalib.me), проверяя статус «Заброшен» или была ли глава опубликована более 3 месяцев назад. Если такая манга найдена, скрипт автоматически добавляет её в вашу коллекцию заброшенной манги на MangaLib.

---

## Фичи
- **Находит заброшенную мангу** на основе статуса «Заброшен».
- **Добавляет мангу со статусом «Продолжается»**, у которой последняя глава была опубликована более 3 месяцев назад.
- **Автоматически добавляет мангу** в вашу коллекцию брошенных тайтлов, используя функцию закладок MangaLib.
- **Сохраняет ссылки на заброшенные тайтлы** в определённый текстовик (на всяяякий случай).
- **Обход защиты Cloudflare** с помощью [Cloudscraper](https://github.com/VeNoMouS/cloudscraper) для отправки POST-запросов.
- **Автоматизация Playwright**: Использует [Playwright](https://playwright.dev/python/docs/intro) для навигации по MangaLib и сбора необходимой информации.

---

## Необходимые библиотеки

Скрипт использует следующие библиотеки Python:

### Требуемые библиотеки:
1. **Playwright** - Для автоматизации браузера.
2. **Cloudscraper** - для обхода защиты Cloudflare при отправке запросов.
3. **Asyncio** - Для управления асинхронными задачами.
4. **BeautifulSoup** - Для парсинга HTML (при необходимости).
5. **Datetime** - Для вычисления даты.

### Установка

Вы должны установить необходимые библиотеки с помощью следующих команд:

``pip install playwright`` <br>
``pip install cloudscraper``<br>
``pip install beautifulsoup4``<br>

Кроме того, вам потребуется установить браузеры Playwright. После установки Playwright выполните команду в cmd:<br>
``playwright install`` <br>
Это позволит загрузить и установить необходимые файлы браузеров, которые Playwright использует для автоматизации.

### Использование
Шаг 1: Скачайте архив и распакуйте всё в одну папку<br>
Для правильной работы скрипта вам нужен файл fixed_mangas.txt, содержащий информацию о манге (например, slug_url, manga_id и т. д.). Скрипт использует этот файл для поиска информации о манге при POST-запросах. Убедитесь, что этот файл отформатирован как JSON и находится в той же директории, что и скрипт.

Шаг 2: Установка cookie-файлов и статуса коллекции<br>
Перед запуском скрипта вам нужно вручную авторизоваться на MangaLib и извлечь свои сессионные куки (remember_web_md5hashhere, XSRF-TOKEN и mangalib_session). Вставьте эти куки в скрипт в самом верху. Для каждой куки есть отдельная переменная, вставляете в пустое место между ''.
```
async def set_cookies(page):
    cookies = [
        {
            'name': 'XSRF-TOKEN',
            'value': 'your_xsrf_token_value',  # Поменяйте на ваши куки XSRF
            ...
        },
        {
            'name': 'mangalib_session',
            'value': 'your_session_value',  # Поменяйте на ваши сессионные куки
            ...
        },
	{
            'name': 'remember_web_md5hashhere',
            'value': 'your_remember_web_cookie', # Поменяйте на ваши куки
            ...
        }
    ] 
```

Более того, вы должны поменять "status" в этой части кода идентификатором вашей коллекции.
```
    payload = {
        "manga_id": manga_id,
        "media_slug": media_slug,
        "status": throwmesomenumbers,  # Поменяйте на ваш id коллекции. Вы можете найти его у себя в профиле, нажав на нужную коллекцию, в конце ссылки будет номер коллекции. Обычно, это длинное число, типа 1337228. Например, https://mangalib.me/user/userid?folder=collectionid (coolectionid = "status" в этой строке)
        "site_id": "1"
    }
```
И ещё, тут надо поменять Cookie, x-csrf-token и x-xsrf-token. Вы можете вытащить их из запроса, его можно посмотреть через F12 - Network - добавляете тайтл в коллекцию - смотрите bookmark - достаёте все нужные поля (прям копипастите в скрипт)
```
    headers = {
        ...
        'Cookie': 'your_cookie_here', # Change it!!!           
        ...
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36', # You can set your own user agent
        'X-Csrf-Token': 'your_csrf_here', # Change it!!!
        'X-Requested-With': 'XMLHttpRequest',
        'X-Xsrf-Token': 'your_xsrf_here' # Change it!!!
        }
```

Шаг 3: Запустите скрипт<br>
После установки всех куки + статуса + xsrf/csrf вы можете запустить скрипт с помощью терминала или других программ, которые могут обработать Python, таких, как VSCode, Pycharm и т.д:
``python main.py``<br>

Работа скрипта: <br>
Перейдёт на случайные страницы манги - mangalib.me/random <br>
Проверит, заброшена ли манга по статусу «Заброшен» или старой залитой главе (более 3 месяцев назад). <br>
Автоматически добавит заброшенную мангу в вашу коллекцию MangaLib. <br>

Шаг 4: Смотрите на вывод и кайфуйте<br>
Как только скрипт найдёт заброшенную мангу, он выведет подробности в консоль и добавит мангу в вашу коллекцию. Все ошибки обрабатываются, если таковые возникнут, вы можете создать тему со всеми подробностями о том, как вы получили ошибку, а я постараюсь её исправить.

Устранение неполадок:<br>
Проблемы с CAPTCHA: Если Cloudflare CAPTCHA продолжает блокировать запросы, убедитесь, что вы используете действительные куки сессии, и попробуйте замедлить работу скрипта, увеличив время sleep между запросами.<br>
Ошибки 403: Это может произойти, если срок действия файлов cookie вашей сессии истёк. Вам нужно будет снова вручную войти в систему и обновить куки в скрипте.<br>

### Лицензия
Этот проект с открытым исходным кодом и лицензируется по лицензии GPL-3.0. Не стесняйтесь изменять и улучшать скрипт в соответствии с вашими потребностями. (но не монетизируйте его, это плохо!).

### Вклад
Если вы хотите внести свой вклад в этот проект, не стесняйтесь форкать репозиторий и отправлять запросы на исправления с вашими улучшениями.

### Автор
Скрипт создан m30wnat10n и моим старым добрым другом GPT-4o.<br>
Я обычный энтузиаст в области кибербезопасности, люблю крипту и мангу.<br>
--- ---

EN:
# MangaLib Abandoned Manga Hunter

This script automates the process of finding abandoned manga titles on [MangaLib](https://mangalib.me) by either checking for the "Заброшен" (abandoned) status or verifying if the last published chapter was more than 3 months old. If such a manga is found, the script automatically adds it to your abandoned manga collection on MangaLib.

---

## Features
- **Detects abandoned manga** based on the "Заброшен" status.
- **Checks for manga with "Продолжается" status** but last chapter was published more than 3 months ago.
- **Automatically adds manga** to your abandoned collection using the MangaLib bookmark feature.
- **Saves abandonded manga links** into .txt file (in case if you need to check it).
- **Bypasses Cloudflare protection** using [Cloudscraper](https://github.com/VeNoMouS/cloudscraper) to send POST requests.
- **Playwright Automation**: Uses [Playwright](https://playwright.dev/python/docs/intro) to navigate MangaLib and gather necessary details.

---

## Requirements

The script uses the following Python libraries:

### Required Libraries:
1. **Playwright** - For browser automation.
2. **Cloudscraper** - To bypass Cloudflare protection when sending requests.
3. **Asyncio** - For managing asynchronous tasks.
4. **BeautifulSoup** - For HTML parsing (if needed).
5. **Datetime** - For date calculations.

### Installation

You can install the required libraries using the following commands:

```
pip install playwright
pip install cloudscraper
pip install beautifulsoup4
```
Additionally, you will need to install the Playwright browsers. After installing Playwright, run:
``playwright install``<br>
This will download and install the necessary browser binaries that Playwright uses for automation.

### Usage
Step 1: Download the Manga JSON Data<br>
You need a fixed_mangas.txt file containing the manga information (like slug_url, manga_id, etc.). The script uses this file to find manga details for POST requests. Make sure this file is formatted as JSON and located in the same directory as the script.

Step 2: Set Your Cookies and Collection Status<br>
Before running the script, you need to manually authenticate on MangaLib and extract your session cookies (remember_web_md5hashhere, XSRF-TOKEN and mangalib_session). Insert these cookies into the script in appropriate variables on the top.
```
async def set_cookies(page):
    cookies = [
        {
            'name': 'XSRF-TOKEN',
            'value': 'your_xsrf_token_value',  # Replace with actual token
            ...
        },
        {
            'name': 'mangalib_session',
            'value': 'your_session_value',  # Replace with actual session value
            ...
        },
	{
            'name': 'remember_web_md5hashhere', 
            'value': 'your_remember_web_cookie', # Replace with actual cookie
            ....
        }
    ]
```

Additionally, you should change "status" in this part with your own collection identifier
```
    payload = {
        "manga_id": manga_id,
        "media_slug": media_slug,
        "status": throwmesomenumbers,  # You can check it in your profile, just click on the collection you need, and it will be on the link's end. Usually, it is a large number, like 1337228. For example, https://mangalib.me/user/userid?folder=collectionid (or "status" in my script)
        "site_id": "1"
    }
```

And you should change Cookie, x-csrf-token и x-xsrf-token here. You can extract all of these from request headers when you add smth into collection manually through F12 - Network - add test manga into collection - check "bookmark" request - copypaste all script needs.
```
    headers = {
        ...
        'Cookie': 'your_cookie_here', # Change it!!!           
        ...
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36', # You can set yours
        'X-Csrf-Token': 'your_csrf_here', # Change it!!!
        'X-Requested-With': 'XMLHttpRequest',
        'X-Xsrf-Token': 'your_xsrf_here' # Change it!!!
        }
```

Step 3: Run the Script<br>
After setting the cookies + status + xsrf/csrf and downloading the manga data file, you can run the script using terminal or anything like VSCode, Pycharm, etc:
``python main.py``<br>

The script will:<br>
Navigate to random manga pages - mangalib.me/random<br>
Check for abandoned manga based on the "Заброшен" or old chapter date.<br>
Automatically add any abandoned manga to your MangaLib collection.<br>

Step 4: Watch the Output and Chill<br>
Once the script finds an abandoned title, it will log the details and add the manga to your collection. All errors are handled, if there are any, you can create a topic with all the details on how you got an error.

### Troubleshooting
CAPTCHA Issues: If Cloudflare CAPTCHA keeps blocking requests, ensure you're using valid session cookies and try slowing down the script by increasing the sleep time between requests.<br>
403 Errors: This can happen if your session cookies expire. You will need to manually log in again and update your cookies in the script.<br>

### License
This project is open-source and licensed under the GPL-3.0 license. Feel free to modify and improve the script as per your needs. (but do not monetize it, it is bad!)

### Contributing
If you want to contribute to this project, feel free to fork the repository and submit pull requests with your improvements.

### Author
Script created by m30wnat10n and my good old friend GPT-4o.<br>
I'm an average cybersecurity enthusiast, crypto and manga enjoyer.
