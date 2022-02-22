# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 15:58:16 2020

"""

from pycipher import Bifid


msg = 'snbwmuotwodwvcywfgmruotoozaiwghlabvuzmfobhtywftopmtawyhifqgtsiowetrksrzgrztkfctxnrswnhxshylyehtatssukfvsnztyzlopsv'
keys = ['mrocktvquizphdbagsfewlynx',
'ocknymphswaqfdrugvexblitz',
'crwthvoxzapsqigymfeldbunk',
'hmfordwaltzcinqbuskpyxveg',
'phavfyxbugstonqmilkzdcrew',
'hesaidbcfgklmnopqrtuvwxyz',
'enqvahlbidgumkrwcfpostxyz',
'emilyqungschwarzkopfxtvbd',
'ohnfezcamrwsputyxigkqblvd',
'qtipforsuvnzxylemdcbaghwk',
'umblingvextfrowzyhackspdq',
'qvandzstruckmybigfoxwhelp',
'lumpydrabcgqvzinksfoxthew',
'heyiamnopqrstuvwxzbcdfgkl',
'quizvbmwlynxstockderpaghf',
'pledbigczarunksmyvwfoxthq',
'waltzgbquickfordsvexnymph',
'qwertyuioplkhgfdsazxcvbnm',
'zyxwvutsrqponmlkihgfedcba',
'aquickbrownfxmpsvethlzydg',
]

for i in range(len(keys)):
    key = keys[len(keys)-i-1]
    msg = Bifid(key,5).decipher(msg)
    print(str.lower(msg).replace('x', ' '))