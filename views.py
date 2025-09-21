from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # РІРїРёС€РёС‚Рµ РїСЂР°РІРёР»СЊРЅС‹Рµ Р°РґСЂРµСЃР° СЃС‚СЂР°РЅРёС†, РёСЃРїРѕР»СЊР·СѓСЏ
    # С„СѓРЅРєС†РёСЋ `reverse`
    pages = {
        'Р“Р»Р°РІРЅР°СЏ СЃС‚СЂР°РЅРёС†Р°': reverse('home'),
        'РџРѕРєР°Р·Р°С‚СЊ С‚РµРєСѓС‰РµРµ РІСЂРµРјСЏ': reverse('time'),
        'РџРѕРєР°Р·Р°С‚СЊ СЃРѕРґРµСЂР¶РёРјРѕРµ СЂР°Р±РѕС‡РµР№ РґРёСЂРµРєС‚РѕСЂРёРё': reverse('workdir')
    }

    # context Рё РїР°СЂР°РјРµС‚СЂС‹ render РјРµРЅСЏС‚СЊ РЅРµ РЅСѓР¶РЅРѕ
    # РїРѕРґР±СЂРѕР±РЅРµРµ Рѕ РЅРёС… РјС‹ РїРѕРіРѕРІРѕСЂРёРј РЅР° СЃР»РµРґСѓСЋС‰РёС… Р»РµРєС†РёСЏС…
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # РѕР±СЂР°С‚РёС‚Рµ РІРЅРёРјР°РЅРёРµ вЂ“ Р·РґРµСЃСЊ HTML С€Р°Р±Р»РѕРЅР° РЅРµС‚,
    # РІРѕР·РІСЂР°С‰Р°РµС‚СЃСЏ РїСЂРѕСЃС‚Рѕ С‚РµРєСЃС‚
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg = f'РўРµРєСѓС‰РµРµ РІСЂРµРјСЏ: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # РїРѕ Р°РЅР°Р»РѕРіРёРё СЃ `time_view`, РЅР°РїРёС€РёС‚Рµ РєРѕРґ,
    # РєРѕС‚РѕСЂС‹Р№ РІРѕР·РІСЂР°С‰Р°РµС‚ СЃРїРёСЃРѕРє С„Р°Р№Р»РѕРІ РІ СЂР°Р±РѕС‡РµР№
    # РґРёСЂРµРєС‚РѕСЂРёРё
    files = os.listdir('.')
    files_list = '<br>'.join(files)
    msg = f'РЎРѕРґРµСЂР¶РёРјРѕРµ СЂР°Р±РѕС‡РµР№ РґРёСЂРµРєС‚РѕСЂРёРё:<br>{files_list}'
    return HttpResponse(msg)