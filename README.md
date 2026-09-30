# bakalGram

Личный клиент Telegram для Windows. Это [AyuGram Desktop](https://github.com/AyuGram/AyuGramDesktop) со всеми его фишками, но под своим именем и с возможностью дописывать что угодно своё.

Всё, что умеет AyuGram, на месте: режим призрака, история удалённых и изменённых сообщений, фильтры сообщений, режим стримера, локальный Premium, переводчик, кастомизация шрифта и внешнего вида. Подробное описание функций — в [документации AyuGram](https://docs.ayugram.one/desktop/).

## Как скачать и запустить

1. Открой вкладку **[Releases](../../releases/latest)**.
2. Скачай `bakalGram-win64-….zip`, распакуй в любую папку (например, `C:\bakalGram`).
3. Запусти `bakalGram.exe` и войди в свой аккаунт Telegram, как в обычном клиенте.

Windows может показать синее окно «Система Windows защитила ваш компьютер» — это потому, что у сборки нет платной цифровой подписи. Нажми «Подробнее» → «Выполнить в любом случае».

bakalGram живёт отдельно от обычного Telegram и AyuGram: своя папка с данными, свой значок в панели задач, свои настройки. Их можно держать открытыми одновременно.

Автообновления нет специально (иначе он бы «обновился» до обычного AyuGram). Новые версии появляются в Releases.

## Как собирается

Готовый `.exe` собирает GitHub Actions — workflow [`bakalgram-windows.yml`](.github/workflows/bakalgram-windows.yml). Он запускается сам при каждом изменении в ветке `dev` и в конце публикует новый релиз.

Самая первая сборка долгая: GitHub с нуля компилирует Qt, ffmpeg, WebRTC и остальные библиотеки (обычно 5–10 часов, в несколько заходов — workflow сам перезапускает себя, пока не доделает). Библиотеки сохраняются в кэш, и дальше каждая сборка bakalGram занимает 2–4 часа.

Запустить сборку вручную: **Actions** → **bakalGram Windows** → **Run workflow**.

## Где что лежит

| Что | Где |
|---|---|
| Имя клиента, ссылки на репозиторий | [`Telegram/SourceFiles/bakal/bakal_brand.h`](Telegram/SourceFiles/bakal/bakal_brand.h) |
| Все места, где AyuGram заменён на bakalGram | [`bakal/rebrand.py`](bakal/rebrand.py) |
| Сборка под Windows | [`.github/workflows/bakalgram-windows.yml`](.github/workflows/bakalgram-windows.yml) |
| Функции AyuGram (призрак, фильтры, настройки) | `Telegram/SourceFiles/ayu/` |

Свои доработки удобно держать в `Telegram/SourceFiles/bakal/`, а в код AyuGram вносить минимальные правки с комментарием `// bakalGram:` — так проще подтягивать новые версии AyuGram.

## Свои API-ключи (по желанию)

По умолчанию используются ключи из [`docs/api_credentials.md`](docs/api_credentials.md), как в самом AyuGram. Если хочешь свои — получи `api_id` и `api_hash` на [my.telegram.org](https://my.telegram.org), добавь их в **Settings → Secrets and variables → Actions** как `TDESKTOP_API_ID` и `TDESKTOP_API_HASH` и перезапусти сборку.

## Лицензия и авторы

bakalGram распространяется под [GNU GPL v3](LICENSE), как AyuGram и Telegram Desktop, поэтому исходники открыты.

Основано на [AyuGram Desktop](https://github.com/AyuGram/AyuGramDesktop) от Radolyn Labs, который в свою очередь основан на [Telegram Desktop](https://github.com/telegramdesktop/tdesktop). Оригинальное описание AyuGram: [README-AyuGram-RU.md](README-AyuGram-RU.md).
