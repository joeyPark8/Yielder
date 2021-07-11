import os
import time
import tkinter as tk

scoretypes = []
scores = []
proportions = []
results = {}

scoreFilePath = 'C://Users//USER//Desktop//Yielder//data//score.txt'
proportionFilePath = 'C://Users//USER//Desktop//Yielder//data//proportion.txt'
resultFilePath = 'C://Users//USER//Desktop//Yielder//data//result.txt'

def onClickedStart():
    start_btn.destroy()
    title_lbl.destroy()

    # 국어
    korean_lbl.place(x=50, y=10)
    korean_mid_chk.place(x=50, y=30)
    korean_fin_chk.place(x=50, y=50)
    korean_per_lbl.place(x=50, y=75)
    korean_per_count.place(x=50, y=95)

    # 도덕
    moral_lbl.place(x=50, y=125)
    moral_mid_chk.place(x=50, y=145)
    moral_fin_chk.place(x=50, y=165)
    moral_per_lbl.place(x=50, y=190)
    moral_per_count.place(x=50, y=210)

    # 역사
    history_lbl.place(x=50, y=240)
    history_mid_chk.place(x=50, y=260)
    history_fin_chk.place(x=50, y=280)
    history_per_lbl.place(x=50, y=305)
    history_per_count.place(x=50, y=325)

    # 수학
    math_lbl.place(x=50, y=355)
    math_mid_chk.place(x=50, y=375)
    math_fin_chk.place(x=50, y=395)
    math_per_lbl.place(x=50, y=420)
    math_per_count.place(x=50, y=440)

    # 과학
    science_lbl.place(x=370, y=10)
    science_mid_chk.place(x=370, y=30)
    science_fin_chk.place(x=370, y=50)
    science_per_lbl.place(x=370, y=75)
    science_per_count.place(x=370, y=95)

    # 기가
    tech_lbl.place(x=370, y=125)
    tech_mid_chk.place(x=370, y=145)
    tech_fin_chk.place(x=370, y=165)
    tech_per_lbl.place(x=370, y=190)
    tech_per_count.place(x=370, y=210)

    # 영어
    english_lbl.place(x=370, y=240)
    english_mid_chk.place(x=370, y=260)
    english_fin_chk.place(x=370, y=280)
    english_per_lbl.place(x=370, y=305)
    english_per_count.place(x=370, y=325)

    # 한문
    chinese_lbl.place(x=370, y=355)
    chinese_mid_chk.place(x=370, y=375)
    chinese_fin_chk.place(x=370, y=395)
    chinese_per_lbl.place(x=370, y=420)
    chinese_per_count.place(x=370, y=440)

    # 체육
    pe_lbl.place(x=690, y=10)
    pe_mid_chk.place(x=690, y=30)
    pe_fin_chk.place(x=690, y=50)
    pe_per_lbl.place(x=690, y=75)
    pe_per_count.place(x=690, y=95)

    # 음악
    music_lbl.place(x=690, y=125)
    music_mid_chk.place(x=690, y=145)
    music_fin_chk.place(x=690, y=165)
    music_per_lbl.place(x=690, y=190)
    music_per_count.place(x=690, y=210)

    # 미술
    art_lbl.place(x=690, y=240)
    art_mid_chk.place(x=690, y=260)
    art_fin_chk.place(x=690, y=280)
    art_per_lbl.place(x=690, y=305)
    art_per_count.place(x=690, y=325)

    next_btn.place(x=690, y=385)


def onClickedNext():
    next_btn.destroy()

    save(1)

    korean_lbl.destroy()
    korean_mid_chk.destroy()
    korean_fin_chk.destroy()
    korean_per_lbl.destroy()
    korean_per_count.destroy()

    moral_lbl.destroy()
    moral_mid_chk.destroy()
    moral_fin_chk.destroy()
    moral_per_lbl.destroy()
    moral_per_count.destroy()

    history_lbl.destroy()
    history_mid_chk.destroy()
    history_fin_chk.destroy()
    history_per_lbl.destroy()
    history_per_count.destroy()

    math_lbl.destroy()
    math_mid_chk.destroy()
    math_fin_chk.destroy()
    math_per_lbl.destroy()
    math_per_count.destroy()

    science_lbl.destroy()
    science_mid_chk.destroy()
    science_fin_chk.destroy()
    science_per_lbl.destroy()
    science_per_count.destroy()

    tech_lbl.destroy()
    tech_mid_chk.destroy()
    tech_fin_chk.destroy()
    tech_per_lbl.destroy()
    tech_per_count.destroy()

    english_lbl.destroy()
    english_mid_chk.destroy()
    english_fin_chk.destroy()
    english_per_lbl.destroy()
    english_per_count.destroy()

    chinese_lbl.destroy()
    chinese_mid_chk.destroy()
    chinese_fin_chk.destroy()
    chinese_per_lbl.destroy()
    chinese_per_count.destroy()

    pe_lbl.destroy()
    pe_mid_chk.destroy()
    pe_fin_chk.destroy()
    pe_per_lbl.destroy()
    pe_per_count.destroy()

    music_lbl.destroy()
    music_mid_chk.destroy()
    music_fin_chk.destroy()
    music_per_lbl.destroy()
    music_per_count.destroy()

    art_lbl.destroy()
    art_mid_chk.destroy()
    art_fin_chk.destroy()
    art_per_lbl.destroy()
    art_per_count.destroy()

    instruction_lbl.pack()

    korean_lbl2.place(x=50, y=35)
    if scoretypes[0]['mid']:
        korean_mid_lbl.place(x=50, y=55)
        korean_mid_proportion.place(x=105, y=55)
    if scoretypes[0]['fin']:
        korean_fin_lbl.place(x=50, y=75)
        korean_fin_proportion.place(x=105, y=75)
    if not scoretypes[0]['per'] == 0:
        korean_per_lbl2.place(x=50, y=95)
        korean_per_proportion.place(x=105, y=95)

    moral_lbl2.place(x=50, y=125)
    if scoretypes[1]['mid']:
        moral_mid_lbl.place(x=50, y=145)
        moral_mid_proportion.place(x=105, y=145)
    if scoretypes[1]['fin']:
        moral_fin_lbl.place(x=50, y=165)
        moral_fin_proportion.place(x=105, y=165)
    if not scoretypes[1]['per'] == 0:
        moral_per_lbl2.place(x=50, y=185)
        moral_per_proportion.place(x=105, y=185)

    history_lbl2.place(x=50, y=215)
    if scoretypes[2]['mid']:
        history_mid_lbl.place(x=50, y=235)
        history_mid_proportion.place(x=105, y=235)
    if scoretypes[2]['fin']:
        history_fin_lbl.place(x=50, y=255)
        history_fin_proportion.place(x=105, y=255)
    if not scoretypes[2]['per'] == 0:
        history_per_lbl2.place(x=50, y=275)
        history_per_proportion.place(x=105, y=275)

    math_lbl2.place(x=50, y=305)
    if scoretypes[3]['mid']:
        math_mid_lbl.place(x=50, y=325)
        math_mid_proportion.place(x=105, y=325)
    if scoretypes[3]['fin']:
        math_fin_lbl.place(x=50, y=345)
        math_fin_proportion.place(x=105, y=345)
    if not scoretypes[3]['per'] == 0:
        math_per_lbl2.place(x=50, y=365)
        math_per_proportion.place(x=105, y=365)

    science_lbl2.place(x=320, y=35)
    if scoretypes[4]['mid']:
        science_mid_lbl.place(x=320, y=55)
        science_mid_proportion.place(x=375, y=55)
    if scoretypes[4]['fin']:
        science_fin_lbl.place(x=320, y=75)
        science_fin_proportion.place(x=375, y=75)
    if not scoretypes[4]['per'] == 0:
        science_per_lbl2.place(x=320, y=95)
        science_per_proportion.place(x=375, y=95)

    tech_lbl2.place(x=320, y=125)
    if scoretypes[5]['mid']:
        tech_mid_lbl.place(x=320, y=145)
        tech_mid_proportion.place(x=375, y=145)
    if scoretypes[5]['fin']:
        tech_fin_lbl.place(x=320, y=165)
        tech_fin_proportion.place(x=375, y=165)
    if not scoretypes[5]['per'] == 0:
        tech_per_lbl2.place(x=320, y=185)
        tech_per_proportion.place(x=375, y=185)

    english_lbl2.place(x=320, y=215)
    if scoretypes[6]['mid']:
        english_mid_lbl.place(x=320, y=235)
        english_mid_proportion.place(x=375, y=235)
    if scoretypes[6]['fin']:
        english_fin_lbl.place(x=320, y=255)
        english_fin_proportion.place(x=375, y=255)
    if not scoretypes[6]['per'] == 0:
        english_per_lbl2.place(x=320, y=275)
        english_per_proportion.place(x=375, y=275)

    chinese_lbl2.place(x=320, y=305)
    if scoretypes[7]['mid']:
        chinese_mid_lbl.place(x=320, y=325)
        chinese_mid_proportion.place(x=375, y=325)
    if scoretypes[7]['fin']:
        chinese_fin_lbl.place(x=320, y=345)
        chinese_fin_proportion.place(x=375, y=345)
    if not scoretypes[7]['per'] == 0:
        chinese_per_lbl2.place(x=320, y=365)
        chinese_per_proportion.place(x=375, y=365)

    pe_lbl2.place(x=590, y=35)
    if scoretypes[8]['mid']:
        pe_mid_lbl.place(x=590, y=55)
        pe_mid_proportion.place(x=645, y=55)
    if scoretypes[8]['fin']:
        pe_fin_lbl.place(x=590, y=75)
        pe_fin_proportion.place(x=645, y=75)
    if not scoretypes[8]['per'] == 0:
        pe_per_lbl2.place(x=590, y=95)
        pe_per_proportion.place(x=645, y=95)

    music_lbl2.place(x=590, y=125)
    if scoretypes[9]['mid']:
        music_mid_lbl.place(x=590, y=145)
        music_mid_proportion.place(x=645, y=145)
    if scoretypes[9]['fin']:
        music_fin_lbl.place(x=590, y=165)
        music_fin_proportion.place(x=645, y=165)
    if not scoretypes[9]['per'] == 0:
        music_per_lbl2.place(x=590, y=185)
        music_per_proportion.place(x=645, y=185)

    art_lbl2.place(x=590, y=215)
    if scoretypes[10]['mid']:
        art_mid_lbl.place(x=590, y=235)
        art_mid_proportion.place(x=645, y=235)
    if scoretypes[10]['fin']:
        art_fin_lbl.place(x=590, y=255)
        art_fin_proportion.place(x=645, y=255)
    if not scoretypes[10]['per'] == 0:
        art_per_lbl2.place(x=590, y=275)
        art_per_proportion.place(x=645, y=275)

    next_btn2.place(x=645, y=385)


def onClickedNext2():
    save(2)

    korean_mid_proportion.destroy()
    korean_fin_proportion.destroy()
    korean_per_proportion.destroy()
    moral_mid_proportion.destroy()
    moral_fin_proportion.destroy()
    moral_per_proportion.destroy()
    history_mid_proportion.destroy()
    history_fin_proportion.destroy()
    history_per_proportion.destroy()
    math_mid_proportion.destroy()
    math_fin_proportion.destroy()
    math_per_proportion.destroy()
    science_mid_proportion.destroy()
    science_fin_proportion.destroy()
    science_per_proportion.destroy()
    tech_mid_proportion.destroy()
    tech_fin_proportion.destroy()
    tech_per_proportion.destroy()
    english_mid_proportion.destroy()
    english_fin_proportion.destroy()
    english_per_proportion.destroy()
    chinese_mid_proportion.destroy()
    chinese_fin_proportion.destroy()
    chinese_per_proportion.destroy()
    pe_mid_proportion.destroy()
    pe_fin_proportion.destroy()
    pe_per_proportion.destroy()
    music_mid_proportion.destroy()
    music_fin_proportion.destroy()
    music_per_proportion.destroy()
    art_mid_proportion.destroy()
    art_fin_proportion.destroy()
    art_per_proportion.destroy()

    instruction_lbl.config(text='각 평가의 점수를 적어 주세요. (수행은 한칸 안에 띄어쓰기 없이 ,로 구분)')

    if scoretypes[0]['mid']: korean_mid_score.place(x=105, y=55)
    if scoretypes[0]['fin']: korean_fin_score.place(x=105, y=75)
    if not scoretypes[0]['per'] == 0: korean_per_score.place(x=105, y=95)

    if scoretypes[1]['mid']: moral_mid_score.place(x=105, y=145)
    if scoretypes[1]['fin']: moral_fin_score.place(x=105, y=165)
    if not scoretypes[1]['per'] == 0: moral_per_score.place(x=105, y=185)

    if scoretypes[2]['mid']: history_mid_score.place(x=105, y=235)
    if scoretypes[2]['fin']: history_fin_score.place(x=105, y=255)
    if not scoretypes[2]['per'] == 0: history_per_score.place(x=105, y=275)

    if scoretypes[3]['mid']: math_mid_score.place(x=105, y=325)
    if scoretypes[3]['fin']: math_fin_score.place(x=105, y=345)
    if not scoretypes[3]['per'] == 0: math_per_score.place(x=105, y=365)

    if scoretypes[4]['mid']: science_mid_score.place(x=375, y=55)
    if scoretypes[4]['fin']: science_fin_score.place(x=375, y=75)
    if not scoretypes[4]['per'] == 0: science_per_score.place(x=375, y=95)

    if scoretypes[5]['mid']: tech_mid_score.place(x=375, y=145)
    if scoretypes[5]['fin']: tech_fin_score.place(x=375, y=165)
    if not scoretypes[5]['per'] == 0: tech_per_score.place(x=375, y=185)

    if scoretypes[6]['mid']: english_mid_score.place(x=375, y=235)
    if scoretypes[6]['fin']: english_fin_score.place(x=375, y=255)
    if not scoretypes[6]['per'] == 0: english_per_score.place(x=375, y=275)

    if scoretypes[7]['mid']: chinese_mid_score.place(x=375, y=325)
    if scoretypes[7]['fin']: chinese_fin_score.place(x=375, y=345)
    if not scoretypes[7]['per'] == 0: chinese_per_score.place(x=375, y=365)

    if scoretypes[8]['mid']: pe_mid_score.place(x=645, y=55)
    if scoretypes[8]['fin']: pe_fin_score.place(x=645, y=75)
    if not scoretypes[8]['per'] == 0: pe_per_score.place(x=645, y=95)

    if scoretypes[9]['mid']: music_mid_score.place(x=645, y=145)
    if scoretypes[9]['fin']: music_fin_score.place(x=645, y=165)
    if not scoretypes[9]['per'] == 0: music_per_score.place(x=645, y=185)

    if scoretypes[10]['mid']: art_mid_score.place(x=645, y=235)
    if scoretypes[10]['fin']: art_fin_score.place(x=645, y=255)
    if not scoretypes[10]['per'] == 0: art_per_score.place(x=645, y=275)

    calculate_btn.place(x=645, y=385)


def onClickedCal():
    save(3)

    korean_lbl2.destroy()
    korean_mid_lbl.destroy()
    korean_fin_lbl.destroy()
    korean_per_lbl2.destroy()
    korean_mid_score.destroy()
    korean_fin_score.destroy()
    korean_per_score.destroy()

    moral_lbl2.destroy()
    moral_mid_lbl.destroy()
    moral_fin_lbl.destroy()
    moral_per_lbl2.destroy()
    moral_mid_score.destroy()
    moral_fin_score.destroy()
    moral_per_score.destroy()

    history_lbl2.destroy()
    history_mid_lbl.destroy()
    history_fin_lbl.destroy()
    history_per_lbl2.destroy()
    history_mid_score.destroy()
    history_fin_score.destroy()
    history_per_score.destroy()

    math_lbl2.destroy()
    math_mid_lbl.destroy()
    math_fin_lbl.destroy()
    math_per_lbl2.destroy()
    math_mid_score.destroy()
    math_fin_score.destroy()
    math_per_score.destroy()

    science_lbl2.destroy()
    science_mid_lbl.destroy()
    science_fin_lbl.destroy()
    science_per_lbl2.destroy()
    science_mid_score.destroy()
    science_fin_score.destroy()
    science_per_score.destroy()

    tech_lbl2.destroy()
    tech_mid_lbl.destroy()
    tech_fin_lbl.destroy()
    tech_per_lbl2.destroy()
    tech_mid_score.destroy()
    tech_fin_score.destroy()
    tech_per_score.destroy()

    english_lbl2.destroy()
    english_mid_lbl.destroy()
    english_fin_lbl.destroy()
    english_per_lbl2.destroy()
    english_mid_score.destroy()
    english_fin_score.destroy()
    english_per_score.destroy()

    chinese_lbl2.destroy()
    chinese_mid_lbl.destroy()
    chinese_fin_lbl.destroy()
    chinese_per_lbl2.destroy()
    chinese_mid_score.destroy()
    chinese_fin_score.destroy()
    chinese_per_score.destroy()

    pe_lbl2.destroy()
    pe_mid_lbl.destroy()
    pe_fin_lbl.destroy()
    pe_per_lbl2.destroy()
    pe_mid_score.destroy()
    pe_fin_score.destroy()
    pe_per_score.destroy()

    music_lbl2.destroy()
    music_mid_lbl.destroy()
    music_fin_lbl.destroy()
    music_per_lbl2.destroy()
    music_mid_score.destroy()
    music_fin_score.destroy()
    music_per_score.destroy()

    art_lbl2.destroy()
    art_mid_lbl.destroy()
    art_fin_lbl.destroy()
    art_per_lbl2.destroy()
    art_mid_score.destroy()
    art_fin_score.destroy()
    art_per_score.destroy()

    calculate_btn.destroy()

    os.startfile(r"C://Users//USER//Desktop//Yielder//Project28.exe")

    time.sleep(3)

    load()

    results_str = ''
    for i in results:
        results_str += i + ': ' + results[i] + '\n'

    result_lbl.config(text=results_str)
    result_lbl.place(x=400, y=300)


def save(num):
    if num == 1:
        scoretypes.append({'name': 'korean', 'mid': korean_mid_boolean.get(), 'fin': korean_fin_boolean.get(), 'per': int(korean_per_count.get())})
        scoretypes.append({'name': 'moral', 'mid': moral_mid_boolean.get(), 'fin': moral_fin_boolean.get(), 'per': int(moral_per_count.get())})
        scoretypes.append({'name': 'history', 'mid': history_mid_boolean.get(), 'fin': history_fin_boolean.get(), 'per': int(history_per_count.get())})
        scoretypes.append({'name': 'math', 'mid': math_mid_boolean.get(), 'fin': math_fin_boolean.get(), 'per': int(math_per_count.get())})
        scoretypes.append({'name': 'science', 'mid': science_mid_boolean.get(), 'fin': science_fin_boolean.get(), 'per': int(science_per_count.get())})
        scoretypes.append({'name': 'tech', 'mid': tech_mid_boolean.get(), 'fin': tech_fin_boolean.get(), 'per': int(tech_per_count.get())})
        scoretypes.append({'name': 'english', 'mid': english_mid_boolean.get(), 'fin': english_fin_boolean.get(), 'per': int(english_per_count.get())})
        scoretypes.append({'name': 'chinese', 'mid': chinese_mid_boolean.get(), 'fin': chinese_fin_boolean.get(), 'per': int(chinese_per_count.get())})
        scoretypes.append({'name': 'pe', 'mid': pe_mid_boolean.get(), 'fin': pe_fin_boolean.get(), 'per': int(pe_per_count.get())})
        scoretypes.append({'name': 'music', 'mid': music_mid_boolean.get(), 'fin': music_fin_boolean.get(), 'per': int(music_per_count.get())})
        scoretypes.append({'name': 'art', 'mid': art_mid_boolean.get(), 'fin': art_fin_boolean.get(), 'per': int(art_per_count.get())})
    elif num == 2:
        proportions.append({'name': 'korean',
                            'mid': int(korean_mid_proportion.get()) if scoretypes[0]['mid'] else 0,
                            'fin': int(korean_fin_proportion.get()) if scoretypes[0]['fin'] else 0,
                            'per': korean_per_proportion.get().split(',') if scoretypes[0]['per'] else ''})
        proportions.append({'name': 'moral',
                            'mid': int(moral_mid_proportion.get()) if scoretypes[1]['mid'] else 0,
                            'fin': int(moral_fin_proportion.get()) if scoretypes[1]['fin'] else 0,
                            'per': moral_per_proportion.get().split(',') if scoretypes[1]['per'] else ''})
        proportions.append({'name': 'history',
                            'mid': int(history_mid_proportion.get()) if scoretypes[2]['mid'] else 0,
                            'fin': int(history_fin_proportion.get()) if scoretypes[2]['fin'] else 0,
                            'per': history_per_proportion.get().split(',') if scoretypes[2]['per'] else ''})
        proportions.append({'name': 'math',
                            'mid': int(math_mid_proportion.get()) if scoretypes[3]['mid'] else 0,
                            'fin': int(math_fin_proportion.get()) if scoretypes[3]['fin'] else 0,
                            'per': math_per_proportion.get().split(',') if scoretypes[3]['per'] else ''})
        proportions.append({'name': 'science',
                            'mid': int(science_mid_proportion.get()) if scoretypes[4]['mid'] else 0,
                            'fin': int(science_fin_proportion.get()) if scoretypes[4]['fin'] else 0,
                            'per': science_per_proportion.get().split(',') if scoretypes[4]['per'] else ''})
        proportions.append({'name': 'tech',
                            'mid': int(tech_mid_proportion.get()) if scoretypes[5]['mid'] else 0,
                            'fin': int(tech_fin_proportion.get()) if scoretypes[5]['fin'] else 0,
                            'per': tech_per_proportion.get().split(',') if scoretypes[5]['per'] else ''})
        proportions.append({'name': 'english',
                            'mid': int(english_mid_proportion.get()) if scoretypes[6]['mid'] else 0,
                            'fin': int(english_fin_proportion.get()) if scoretypes[6]['fin'] else 0,
                            'per': english_per_proportion.get().split(',') if scoretypes[6]['per'] else ''})
        proportions.append({'name': 'chinese',
                            'mid': int(chinese_mid_proportion.get()) if scoretypes[7]['mid'] else 0,
                            'fin': int(chinese_fin_proportion.get()) if scoretypes[7]['fin'] else 0,
                            'per': chinese_per_proportion.get().split(',') if scoretypes[7]['per'] else ''})
        proportions.append({'name': 'pe',
                            'mid': int(pe_mid_proportion.get()) if scoretypes[8]['mid'] else 0,
                            'fin': int(pe_fin_proportion.get()) if scoretypes[8]['fin'] else 0,
                            'per': pe_per_proportion.get().split(',') if scoretypes[8]['per'] else ''})
        proportions.append({'name': 'music',
                            'mid': int(music_mid_proportion.get()) if scoretypes[9]['mid'] else 0,
                            'fin': int(music_fin_proportion.get()) if scoretypes[9]['fin'] else 0,
                            'per': music_per_proportion.get().split(',') if scoretypes[9]['per'] else ''})
        proportions.append({'name': 'art',
                            'mid': int(art_mid_proportion.get()) if scoretypes[10]['mid'] else 0,
                            'fin': int(art_fin_proportion.get()) if scoretypes[10]['fin'] else 0,
                            'per': art_per_proportion.get().split(',') if scoretypes[10]['per'] else ''})

        with open(proportionFilePath, 'w') as file:
            for i in proportions:
                text = ''
                for j in i['per']:
                    text += j + ' '
                file.write('{} {} {}\n'.format(i['mid'], i['fin'], text))
    elif num == 3:
        scores.append({'name': 'korean',
                        'mid': int(korean_mid_score.get()) if scoretypes[0]['mid'] else 0,
                        'fin': int(korean_fin_score.get()) if scoretypes[0]['fin'] else 0,
                        'per': korean_per_score.get().split(',') if scoretypes[0]['per'] else ''})
        scores.append({'name': 'moral',
                        'mid': int(moral_mid_score.get()) if scoretypes[1]['mid'] else 0,
                        'fin': int(moral_fin_score.get()) if scoretypes[1]['fin'] else 0,
                        'per': moral_per_score.get().split(',') if scoretypes[1]['per'] else ''})
        scores.append({'name': 'history',
                        'mid': int(history_mid_score.get()) if scoretypes[2]['mid'] else 0,
                        'fin': int(history_fin_score.get()) if scoretypes[2]['fin'] else 0,
                        'per': history_per_score.get().split(',') if scoretypes[2]['per'] else ''})
        scores.append({'name': 'math',
                        'mid': int(math_mid_score.get()) if scoretypes[3]['mid'] else 0,
                        'fin': int(math_fin_score.get()) if scoretypes[3]['fin'] else 0,
                        'per': math_per_score.get().split(',') if scoretypes[3]['per'] else ''})
        scores.append({'name': 'science',
                        'mid': int(science_mid_score.get()) if scoretypes[4]['mid'] else 0,
                        'fin': int(science_fin_score.get()) if scoretypes[4]['fin'] else 0,
                        'per': science_per_score.get().split(',') if scoretypes[4]['per'] else ''})
        scores.append({'name': 'tech',
                        'mid': int(tech_mid_score.get()) if scoretypes[5]['mid'] else 0,
                        'fin': int(tech_fin_score.get()) if scoretypes[5]['fin'] else 0,
                        'per': tech_per_score.get().split(',') if scoretypes[5]['per'] else ''})
        scores.append({'name': 'english',
                        'mid': int(english_mid_score.get()) if scoretypes[6]['mid'] else 0,
                        'fin': int(english_fin_score.get()) if scoretypes[6]['fin'] else 0,
                        'per': english_per_score.get().split(',') if scoretypes[6]['per'] else ''})
        scores.append({'name': 'chinese',
                        'mid': int(chinese_mid_score.get()) if scoretypes[7]['mid'] else 0,
                        'fin': int(chinese_fin_score.get()) if scoretypes[7]['fin'] else 0,
                        'per': chinese_per_score.get().split(',') if scoretypes[7]['per'] else ''})
        scores.append({'name': 'pe',
                        'mid': int(pe_mid_score.get()) if scoretypes[8]['mid'] else 0,
                        'fin': int(pe_fin_score.get()) if scoretypes[8]['fin'] else 0,
                        'per': pe_per_score.get().split(',') if scoretypes[8]['per'] else ''})
        scores.append({'name': 'music',
                        'mid': int(music_mid_score.get()) if scoretypes[9]['mid'] else 0,
                        'fin': int(music_fin_score.get()) if scoretypes[9]['fin'] else 0,
                        'per': music_per_score.get().split(',') if scoretypes[9]['per'] else ''})
        scores.append({'name': 'art',
                        'mid': int(art_mid_score.get()) if scoretypes[10]['mid'] else 0,
                        'fin': int(art_fin_score.get()) if scoretypes[10]['fin'] else 0,
                        'per': art_per_score.get().split(',') if scoretypes[10]['per'] else ''})

        with open(scoreFilePath, 'w') as file:
            for i in scores:
                text = ''
                for j in i['per']:
                    text += j + ' '
                file.write('{} {} {}\n'.format(i['mid'], i['fin'], text))


def load():
    with open(resultFilePath, 'r') as file:
        while True:
            line = file.readline()
            if not line: break

            splited = line.split()

            results[splited[0]] = splited[1]


window = tk.Tk()
window.title('Yielder')
window.geometry("800x600+200+100")
window.resizable(False, False)

#page1
title_lbl = tk.Label(window, text='ㅅㅊㅈ', font=("Arial", 60))
title_lbl.place(x=300, y=100)

start_btn = tk.Button(window, text='시작하기', command=onClickedStart)
start_btn.place(x=380, y=290)

#page2
korean_mid_boolean = tk.BooleanVar()
korean_fin_boolean = tk.BooleanVar()

moral_mid_boolean = tk.BooleanVar()
moral_fin_boolean = tk.BooleanVar()

history_mid_boolean = tk.BooleanVar()
history_fin_boolean = tk.BooleanVar()

math_mid_boolean = tk.BooleanVar()
math_fin_boolean = tk.BooleanVar()

science_mid_boolean = tk.BooleanVar()
science_fin_boolean = tk.BooleanVar()

tech_mid_boolean = tk.BooleanVar()
tech_fin_boolean = tk.BooleanVar()

english_mid_boolean = tk.BooleanVar()
english_fin_boolean = tk.BooleanVar()

chinese_mid_boolean = tk.BooleanVar()
chinese_fin_boolean = tk.BooleanVar()

pe_mid_boolean = tk.BooleanVar()
pe_fin_boolean = tk.BooleanVar()

music_mid_boolean = tk.BooleanVar()
music_fin_boolean = tk.BooleanVar()

art_mid_boolean = tk.BooleanVar()
art_fin_boolean = tk.BooleanVar()

korean_lbl = tk.Label(window, text='국어')
korean_mid_chk = tk.Checkbutton(window, text='중간고사', variable=korean_mid_boolean)
korean_fin_chk = tk.Checkbutton(window, text='기말고사', variable=korean_fin_boolean)
korean_per_lbl = tk.Label(window, text='수행평가 개수')
korean_per_count = tk.Entry(window, width=5)

moral_lbl = tk.Label(window, text='도덕')
moral_mid_chk = tk.Checkbutton(window, text='중간고사', variable=moral_mid_boolean)
moral_fin_chk = tk.Checkbutton(window, text='기말고사', variable=moral_fin_boolean)
moral_per_lbl = tk.Label(window, text='수행평가 개수')
moral_per_count = tk.Entry(window, width=5)

history_lbl = tk.Label(window, text='역사')
history_mid_chk = tk.Checkbutton(window, text='중간고사', variable=history_mid_boolean)
history_fin_chk = tk.Checkbutton(window, text='기말고사', variable=history_fin_boolean)
history_per_lbl = tk.Label(window, text='수행평가 개수')
history_per_count = tk.Entry(window, width=5)

math_lbl = tk.Label(window, text='수학')
math_mid_chk = tk.Checkbutton(window, text='중간고사', variable=math_mid_boolean)
math_fin_chk = tk.Checkbutton(window, text='기말고사', variable=math_fin_boolean)
math_per_lbl = tk.Label(window, text='수행평가 개수')
math_per_count = tk.Entry(window, width=5)

science_lbl = tk.Label(window, text='과학')
science_mid_chk = tk.Checkbutton(window, text='중간고사', variable=science_mid_boolean)
science_fin_chk = tk.Checkbutton(window, text='기말고사', variable=science_fin_boolean)
science_per_lbl = tk.Label(window, text='수행평가 개수')
science_per_count = tk.Entry(window, width=5)

tech_lbl = tk.Label(window, text='기가')
tech_mid_chk = tk.Checkbutton(window, text='중간고사', variable=tech_mid_boolean)
tech_fin_chk = tk.Checkbutton(window, text='기말고사', variable=tech_fin_boolean)
tech_per_lbl = tk.Label(window, text='수행평가 개수')
tech_per_count = tk.Entry(window, width=5)

english_lbl = tk.Label(window, text='영어')
english_mid_chk = tk.Checkbutton(window, text='중간고사', variable=english_mid_boolean)
english_fin_chk = tk.Checkbutton(window, text='기말고사', variable=english_fin_boolean)
english_per_lbl = tk.Label(window, text='수행평가 개수')
english_per_count = tk.Entry(window, width=5)

chinese_lbl = tk.Label(window, text='한문')
chinese_mid_chk = tk.Checkbutton(window, text='중간고사', variable=chinese_mid_boolean)
chinese_fin_chk = tk.Checkbutton(window, text='기말고사', variable=chinese_fin_boolean)
chinese_per_lbl = tk.Label(window, text='수행평가 개수')
chinese_per_count = tk.Entry(window, width=5)

pe_lbl = tk.Label(window, text='체육')
pe_mid_chk = tk.Checkbutton(window, text='중간고사', variable=pe_mid_boolean)
pe_fin_chk = tk.Checkbutton(window, text='기말고사', variable=pe_fin_boolean)
pe_per_lbl = tk.Label(window, text='수행평가 개수')
pe_per_count = tk.Entry(window, width=5)

music_lbl = tk.Label(window, text='음악')
music_mid_chk = tk.Checkbutton(window, text='중간고사', variable=music_mid_boolean)
music_fin_chk = tk.Checkbutton(window, text='기말고사', variable=music_fin_boolean)
music_per_lbl = tk.Label(window, text='수행평가 개수')
music_per_count = tk.Entry(window, width=5)

art_lbl = tk.Label(window, text='미술')
art_mid_chk = tk.Checkbutton(window, text='중간고사', variable=art_mid_boolean)
art_fin_chk = tk.Checkbutton(window, text='기말고사', variable=art_fin_boolean)
art_per_lbl = tk.Label(window, text='수행평가 개수')
art_per_count = tk.Entry(window, width=5)

next_btn = tk.Button(window, text='다음', command=onClickedNext)

#page3
instruction_lbl = tk.Label(window, text='각 평가의 반영비율을 적어 주세요. (수행은 한칸 안에 띄어쓰기 없이 ,로 구분)', font=("", 13))

korean_lbl2 = tk.Label(window, text='국어')
korean_mid_lbl = tk.Label(window, text='중간고사')
korean_mid_proportion = tk.Entry(window)
korean_fin_lbl = tk.Label(window, text='기말고사')
korean_fin_proportion = tk.Entry(window)
korean_per_lbl2 = tk.Label(window, text='수행평가')
korean_per_proportion = tk.Entry(window)

moral_lbl2 = tk.Label(window, text='도덕')
moral_mid_lbl = tk.Label(window, text='중간고사')
moral_mid_proportion = tk.Entry(window)
moral_fin_lbl = tk.Label(window, text='기말고사')
moral_fin_proportion = tk.Entry(window)
moral_per_lbl2 = tk.Label(window, text='수행평가')
moral_per_proportion = tk.Entry(window)

history_lbl2 = tk.Label(window, text='역사')
history_mid_lbl = tk.Label(window, text='중간고사')
history_mid_proportion = tk.Entry(window)
history_fin_lbl = tk.Label(window, text='기말고사')
history_fin_proportion = tk.Entry(window)
history_per_lbl2 = tk.Label(window, text='수행평가')
history_per_proportion = tk.Entry(window)

math_lbl2 = tk.Label(window, text='수학')
math_mid_lbl = tk.Label(window, text='중간고사')
math_mid_proportion = tk.Entry(window)
math_fin_lbl = tk.Label(window, text='기말고사')
math_fin_proportion = tk.Entry(window)
math_per_lbl2 = tk.Label(window, text='수행평가')
math_per_proportion = tk.Entry(window)

science_lbl2 = tk.Label(window, text='과학')
science_mid_lbl = tk.Label(window, text='중간고사')
science_mid_proportion = tk.Entry(window)
science_fin_lbl = tk.Label(window, text='기말고사')
science_fin_proportion = tk.Entry(window)
science_per_lbl2 = tk.Label(window, text='수행평가')
science_per_proportion = tk.Entry(window)

tech_lbl2 = tk.Label(window, text='기가')
tech_mid_lbl = tk.Label(window, text='중간고사')
tech_mid_proportion = tk.Entry(window)
tech_fin_lbl = tk.Label(window, text='기말고사')
tech_fin_proportion = tk.Entry(window)
tech_per_lbl2 = tk.Label(window, text='수행평가')
tech_per_proportion = tk.Entry(window)

english_lbl2 = tk.Label(window, text='영어')
english_mid_lbl = tk.Label(window, text='중간고사')
english_mid_proportion = tk.Entry(window)
english_fin_lbl = tk.Label(window, text='기말고사')
english_fin_proportion = tk.Entry(window)
english_per_lbl2 = tk.Label(window, text='수행평가')
english_per_proportion = tk.Entry(window)

chinese_lbl2 = tk.Label(window, text='한문')
chinese_mid_lbl = tk.Label(window, text='중간고사')
chinese_mid_proportion = tk.Entry(window)
chinese_fin_lbl = tk.Label(window, text='기말고사')
chinese_fin_proportion = tk.Entry(window)
chinese_per_lbl2 = tk.Label(window, text='수행평가')
chinese_per_proportion = tk.Entry(window)

pe_lbl2 = tk.Label(window, text='체육')
pe_mid_lbl = tk.Label(window, text='중간고사')
pe_mid_proportion = tk.Entry(window)
pe_fin_lbl = tk.Label(window, text='기말고사')
pe_fin_proportion = tk.Entry(window)
pe_per_lbl2 = tk.Label(window, text='수행평가')
pe_per_proportion = tk.Entry(window)

music_lbl2 = tk.Label(window, text='음악')
music_mid_lbl = tk.Label(window, text='중간고사')
music_mid_proportion = tk.Entry(window)
music_fin_lbl = tk.Label(window, text='기말고사')
music_fin_proportion = tk.Entry(window)
music_per_lbl2 = tk.Label(window, text='수행평가')
music_per_proportion = tk.Entry(window)

art_lbl2 = tk.Label(window, text='미술')
art_mid_lbl = tk.Label(window, text='중간고사')
art_mid_proportion = tk.Entry(window)
art_fin_lbl = tk.Label(window, text='기말고사')
art_fin_proportion = tk.Entry(window)
art_per_lbl2 = tk.Label(window, text='수행평가')
art_per_proportion = tk.Entry(window)

next_btn2 = tk.Button(window, text='다음', command=onClickedNext2)

#page4
korean_mid_score = tk.Entry(window)
korean_fin_score = tk.Entry(window)
korean_per_score = tk.Entry(window)

moral_mid_score = tk.Entry(window)
moral_fin_score = tk.Entry(window)
moral_per_score = tk.Entry(window)

history_mid_score = tk.Entry(window)
history_fin_score = tk.Entry(window)
history_per_score = tk.Entry(window)

math_mid_score = tk.Entry(window)
math_fin_score = tk.Entry(window)
math_per_score = tk.Entry(window)

science_mid_score = tk.Entry(window)
science_fin_score = tk.Entry(window)
science_per_score = tk.Entry(window)

tech_mid_score = tk.Entry(window)
tech_fin_score = tk.Entry(window)
tech_per_score = tk.Entry(window)

english_mid_score = tk.Entry(window)
english_fin_score = tk.Entry(window)
english_per_score = tk.Entry(window)

chinese_mid_score = tk.Entry(window)
chinese_fin_score = tk.Entry(window)
chinese_per_score = tk.Entry(window)

pe_mid_score = tk.Entry(window)
pe_fin_score = tk.Entry(window)
pe_per_score = tk.Entry(window)

music_mid_score = tk.Entry(window)
music_fin_score = tk.Entry(window)
music_per_score = tk.Entry(window)

art_mid_score = tk.Entry(window)
art_fin_score = tk.Entry(window)
art_per_score = tk.Entry(window)

calculate_btn = tk.Button(window, text='완료', command=onClickedCal)

#page5
result_title_lbl = tk.Label(window, text='결과', font=("", 13))
result_lbl = tk.Label(window)


window.mainloop()
