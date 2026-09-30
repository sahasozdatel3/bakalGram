#!/usr/bin/env python3
"""Rebrand AyuGram Desktop sources to bakalGram.

Every replacement must match exactly the expected number of times, so if
upstream AyuGram changes these lines the script fails loudly instead of
silently skipping something. Run from the repository root, once, on a
clean AyuGram checkout (e.g. after merging a new AyuGram version, resolve
conflicts by keeping our side; the script is the record of what we change).
"""
import sys
from pathlib import Path

INCLUDE = '#include "bakal/bakal_brand.h"\n'

# (file, old, new, expected_count)
R = []


def r(path, old, new, count=1):
    R.append((path, old, new, count))


SF = 'Telegram/SourceFiles/'

# --- identity: names, data folder, exe name --------------------------------
r(SF + 'core/version.h',
  'AppNameOld = "AyuGram for Windows"_cs', 'AppNameOld = "bakalGram for Windows"_cs')
r(SF + 'core/version.h',
  'AppName = "AyuGram Desktop"_cs', 'AppName = "bakalGram Desktop"_cs')
r(SF + 'core/version.h',
  'AppFile = "AyuGram"_cs', 'AppFile = "bakalGram"_cs')
r(SF + 'core/launcher.cpp',
  'setApplicationName(u"AyuGramDesktop"_q)', 'setApplicationName(u"bakalGramDesktop"_q)')

r('Telegram/CMakeLists.txt',
  '"one.ayugram.AyuGramDesktop$<$<CONFIG:Debug>:Debug>"',
  '"one.bakalgram.bakalGramDesktop$<$<CONFIG:Debug>:Debug>"')
r('Telegram/CMakeLists.txt',
  '"one.ayugram.AyuGramDesktop")', '"one.bakalgram.bakalGramDesktop")')
r('Telegram/CMakeLists.txt',
  'set(output_name "AyuGram")', 'set(output_name "bakalGram")')
r('Telegram/CMakeLists.txt',
  'STREQUAL "AyuGram")', 'STREQUAL "bakalGram")')

r('Telegram/Resources/winrc/Telegram.rc',
  '"AyuGram Desktop"', '"bakalGram Desktop"', 2)
r('Telegram/Resources/winrc/Updater.rc',
  '"AyuGram Desktop Updater"', '"bakalGram Desktop Updater"')
r('Telegram/Resources/winrc/Updater.rc',
  '"AyuGram Desktop"', '"bakalGram Desktop"')

# --- Windows shell integration: taskbar id, shortcuts, autostart -----------
f = SF + 'platform/win/windows_app_user_model_id.cpp'
r(f, 'L"AyuGram.AyuGramDesktop.Store"', 'L"bakalGram.bakalGramDesktop.Store"')
r(f, 'L"AyuGram.AyuGramDesktop"', 'L"bakalGram.bakalGramDesktop"')
r(f, 'u"AyuGram.lnk"_q', 'u"bakalGram.lnk"_q', 2)
r(f, 'u"AyuGram Desktop/AyuGram.lnk"_q', 'u"bakalGram Desktop/bakalGram.lnk"_q')
r(f, 'u"AyuGram for Windows/AyuGram.lnk"_q', 'u"bakalGram for Windows/bakalGram.lnk"_q')
r(f, 'u"AyuGramAlpha.lnk"_q', 'u"bakalGramAlpha.lnk"_q')

r(SF + 'platform/win/specific_win.cpp', '"\\\\AyuGram.lnk"', '"\\\\bakalGram.lnk"', 2)

f = SF + 'ayu/utils/windows_utils.cpp'
r(f, 'TaskBar/AyuGram Desktop.lnk"', 'TaskBar/bakalGram Desktop.lnk"')
r(f, 'TaskBar/AyuGram.lnk"', 'TaskBar/bakalGram.lnk"')
r(f, 'u"AyuGram Desktop/AyuGram.lnk"_q', 'u"bakalGram Desktop/bakalGram.lnk"_q')
r(f, 'u"AyuGram/AyuGram.lnk"_q', 'u"bakalGram/bakalGram.lnk"_q')
r(f, 'u"AyuGram.lnk"_q', 'u"bakalGram.lnk"_q')

r(SF + '_other/startup_task_win.cpp', 'L"\\\\AyuGram.exe"', 'L"\\\\bakalGram.exe"')
r(SF + '_other/updater_win.cpp', 'L"AyuGram.exe"', 'L"bakalGram.exe"', 4)

r(SF + 'core/application.cpp',
  'return u"https://github.com/AyuGram/AyuGramDesktop/releases"_q;',
  'return Bakal::ReleasesUrl();')
r(SF + 'core/application.cpp',
  '.shortAppName = u"AyuGram"_q,', '.shortAppName = Bakal::ShortName(),')

# --- visible UI ------------------------------------------------------------
r(SF + 'window/main_window.cpp', 'u"AyuGram"_q : user', 'Bakal::ShortName() : user')
r(SF + 'tray.cpp', '.replace("Telegram", "AyuGram")', '.replace("Telegram", Bakal::ShortName())', 2)
r(SF + 'intro/intro_widget.cpp',
  'QString("AyuGram Desktop v%1")', 'QString(Bakal::FullName() + " v%1")')
r(SF + 'window/window_main_menu.cpp',
  'u"AyuGram Desktop"_q,\n\t\tu"https://ayugram.one"_q',
  'Bakal::FullName(),\n\t\tBakal::RepoUrl()')
r(SF + 'window/notifications_manager_default.cpp',
  'TextWithEntities{ u"AyuGram Desktop"_q }', 'TextWithEntities{ Bakal::FullName() }')
r(SF + 'settings/sections/settings_notifications.cpp',
  'elided(u"AyuGram Desktop"_q,', 'elided(Bakal::FullName(),')
r(SF + 'history/history_item_helpers.cpp',
  '.replace("Telegram", "AyuGram")', '.replace("Telegram", Bakal::ShortName())', 2)
r(SF + 'ayu/ui/settings/settings_main.cpp',
  'QString("AyuGram Desktop v")', 'Bakal::FullName() + QString(" v")')
r(SF + 'ayu/ui/settings/settings_main.cpp',
  '.title = rpl::single(QString("AyuGram")),', '.title = rpl::single(Bakal::ShortName()),')
r(SF + 'ayu/ui/settings/settings_ayu.cpp', '.title = u"AyuGram"_q,', '.title = Bakal::ShortName(),')
r(SF + 'ayu/ui/settings/settings_ayu.cpp',
  'rpl::single(QString("AyuGram"))', 'rpl::single(Bakal::ShortName())')
r(SF + 'ayu/ui/context_menu/context_menu.cpp', '.text = u"AyuGram"_q,', '.text = Bakal::ShortName(),')
r(SF + 'export/output/export_output_html.cpp',
  '"of AyuGram Desktop. Please update', '"of bakalGram Desktop. Please update')
r(SF + 'core/update_checker.cpp',
  'return "https://t.me/AyuGramReleases";',
  'return "https://github.com/sahasozdatel3/bakalGram/releases";')

f = SF + 'core/crash_report_window.cpp'
r(f, 'u"AyuGram"_q : title', 'Bakal::ShortName() : title')
r(f, 'u"Could not start AyuGram Desktop!', 'u"Could not start bakalGram Desktop!')
r(f, 'u"Last time AyuGram Desktop was not closed properly."_q', 'u"Last time bakalGram Desktop was not closed properly."_q', 2)
r(f, 'u"Last time AyuGram Desktop crashed :("_q', 'u"Last time bakalGram Desktop crashed :("_q')
r(f, 'u"GET THE LATEST VERSION OF AYUGRAM DESKTOP"_q', 'u"GET THE LATEST VERSION OF BAKALGRAM DESKTOP"_q')
r(f, 'openUrl(u"https://github.com/AyuGram/AyuGramDesktop"_q)', 'openUrl(Bakal::ReleasesUrl())')
r(f, 'u"AyuGram Crash Report"_q', 'u"bakalGram Crash Report"_q')
r(SF + 'core/crash_reports.cpp',
  '"AyuGram Desktop launch was not finished', '"bakalGram Desktop launch was not finished')

# About box: our name and repo, plus credit to AyuGram.
f = SF + 'boxes/about_box.cpp'
r(f, '"https://github.com/AyuGram/AyuGramDesktop/blob/dev/LICENSE"',
  'Bakal::RepoUrl() + "/blob/dev/LICENSE"')
r(f, '"GitHub",\n\t\t\t"https://github.com/AyuGram/AyuGramDesktop")),\n\t\ttr::marked);',
  '"GitHub",\n\t\t\tBakal::RepoUrl())),\n\t\ttr::marked\n\t) | rpl::map([](TextWithEntities text) {\n'
  '\t\t// bakalGram: credit the client we are built on.\n'
  '\t\treturn text\n'
  '\t\t\t.append(u"\\n\\n"_q)\n'
  '\t\t\t.append(Bakal::ShortName() + u" is based on "_q)\n'
  '\t\t\t.append(Ui::Text::Link(\n'
  '\t\t\t\tBakal::UpstreamName(),\n'
  '\t\t\t\tBakal::UpstreamRepoUrl()))\n'
  '\t\t\t.append(u" by Radolyn Labs."_q);\n'
  '\t});')
r(f, 'box->setTitle(rpl::single(u"AyuGram Desktop"_q));', 'box->setTitle(rpl::single(Bakal::FullName()));')

# Linux / macOS menus (not built by our CI, kept consistent anyway).
r(SF + 'platform/linux/main_window_linux.cpp', 'u"AyuGram"_q', 'Bakal::ShortName()', 2)
r(SF + 'platform/mac/global_menu_mac.mm', 'u"About AyuGram"_q', 'u"About "_q + Bakal::ShortName()')
r(SF + 'platform/mac/global_menu_mac.mm', 'addMenu(u"AyuGram"_q)', 'addMenu(Bakal::ShortName())')
r(SF + 'platform/mac/window_title_mac.mm', 'u"AyuGram"_q, style::al_center', 'Bakal::ShortName(), style::al_center')

# Strings loaded from AyuGram's online translations (e.g. Russian).
r(SF + 'ayu/ayu_lang.cpp',
  '\t\tif (key.endsWith("_PC")) {\n\t\t\tkey = key.replace("_PC", "");\n\t\t}\n',
  '\t\tif (key.endsWith("_PC")) {\n\t\t\tkey = key.replace("_PC", "");\n\t\t}\n\n'
  '\t\t// bakalGram: show our name in translated AyuGram strings too.\n'
  '\t\tif (!Bakal::IsAttributionKey(key.section(\'#\', 0, 0))) {\n'
  '\t\t\tval = Bakal::Rebrand(val);\n\t\t}\n')


def add_include(text):
    if INCLUDE in text:
        return text
    # right after the file's own header (the first, unconditional include)
    lines = text.splitlines(keepends=True)
    first = next(i for i, l in enumerate(lines) if l.startswith('#include'))
    lines.insert(first + 1, INCLUDE)
    return ''.join(lines)


def rebrand_lang_strings():
    """English defaults for AyuGram's own strings (keys starting ayu_)."""
    import re
    path = Path('Telegram/Resources/langs/lang.strings')
    attribution = {
        'ayu_SettingsWatermark', 'ayu_SupporterPopup',
        'ayu_OfficialResourcePopup', 'ayu_ExteraChatsAlert',
    }
    brand = re.compile(r'AyuGram(?![A-Za-z0-9_])')
    changed = 0
    out = []
    for line in path.read_text(encoding='utf-8').splitlines(keepends=True):
        m = re.match(r'"(ayu_[A-Za-z0-9_#]+)" = ', line)
        if m and m.group(1).split('#')[0] not in attribution:
            head, value = line[:m.end()], line[m.end():]
            new = brand.sub('bakalGram', value)
            if new != value:
                changed += 1
                line = head + new
        out.append(line)
    if changed < 10:
        sys.exit(f'lang.strings: only {changed} strings rebranded, check upstream')
    path.write_text(''.join(out), encoding='utf-8')
    print(f'lang.strings: {changed} strings rebranded')


def main():
    files = {}
    for path, old, new, count in R:
        text = files.get(path) or Path(path).read_text(encoding='utf-8')
        found = text.count(old)
        if found != count:
            sys.exit(f'{path}: expected {count} of {old!r}, found {found}')
        files[path] = text.replace(old, new)
    for path, text in files.items():
        if 'Bakal::' in text and not path.endswith(('.txt', '.rc', '.h')):
            text = add_include(text)
        Path(path).write_text(text, encoding='utf-8')
    print(f'{len(R)} replacements in {len(files)} files')
    rebrand_lang_strings()


if __name__ == '__main__':
    main()
