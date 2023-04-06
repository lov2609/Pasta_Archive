import toga
import aiohttp
from urllib.parse import urljoin
from toga.style import Pack
from toga.style.pack import COLUMN


class PastaArchive(toga.App):

    def startup(self):
        global api_token
        api_token = "040d0973c515d553c6fcc40cbed4c283ed7f5122"
        global username
        username = "LsVbadd07"
        pythonanywhere_host = "www.pythonanywhere.com"
        global api_base
        api_base = "https://{pythonanywhere_host}/api/v0/user/{username}/".format(
            pythonanywhere_host=pythonanywhere_host, username=username)

        self.main_box = toga.Box(style=Pack(direction=COLUMN, background_color='#00FFFF'))
        self.box_main = toga.Box(style=Pack(direction=COLUMN))
        self.box_int = toga.Box(style=Pack(direction=COLUMN))
        self.box_creepy = toga.Box(style=Pack(direction=COLUMN))
        self.box_cringe = toga.Box(style=Pack(direction=COLUMN))
        self.box_rofl_group = toga.Box(style=Pack(direction=COLUMN))
        self.box_rofl_aw = toga.Box(style=Pack(direction=COLUMN))
        self.box_rofl_cd = toga.Box(style=Pack(direction=COLUMN))
        self.box_rofl_dad = toga.Box(style=Pack(direction=COLUMN))
        self.box_rofl_mh = toga.Box(style=Pack(direction=COLUMN))
        self.box_rofl_lv = toga.Box(style=Pack(direction=COLUMN))
        self.box_rofl_mt = toga.Box(style=Pack(direction=COLUMN))
        self.box_rofl_ch = toga.Box(style=Pack(direction=COLUMN))
        self.box_rofl_wd = toga.Box(style=Pack(direction=COLUMN))
        self.box_others = toga.Box(style=Pack(direction=COLUMN))
        self.box_read_int = toga.Box(style=Pack(direction=COLUMN))
        self.box_read_creepy = toga.Box(style=Pack(direction=COLUMN))
        self.box_read_cringe = toga.Box(style=Pack(direction=COLUMN))
        self.box_read_rofl_group = toga.Box(style=Pack(direction=COLUMN))
        self.box_read_rofl_aw = toga.Box(style=Pack(direction=COLUMN))
        self.box_read_rofl_cd = toga.Box(style=Pack(direction=COLUMN))
        self.box_read_rofl_dad = toga.Box(style=Pack(direction=COLUMN))
        self.box_read_rofl_mh = toga.Box(style=Pack(direction=COLUMN))
        self.box_read_rofl_lv = toga.Box(style=Pack(direction=COLUMN))
        self.box_read_rofl_mt = toga.Box(style=Pack(direction=COLUMN))
        self.box_read_rofl_ch = toga.Box(style=Pack(direction=COLUMN))
        self.box_read_rofl_wd = toga.Box(style=Pack(direction=COLUMN))
        self.box_read_others = toga.Box(style=Pack(direction=COLUMN))
        self.box_error = toga.Box(style=Pack(direction=COLUMN, background_color='#FF4500'))

        self.int_button_1 = toga.Button('Похороны', on_press=self.recive_funeral, style=Pack(font_size=14, background_color='#98FB98'))
        self.int_button_2 = toga.Button('Харухи ИРЛ', on_press=self.recive_haruhi_irl, style=Pack(font_size=14, background_color='#98FB98'))
        self.int_button_3 = toga.Button('Спешите жить', on_press=self.recive_hurry_up, style=Pack(font_size=14, background_color='#98FB98'))
        self.int_button_4 = toga.Button('Клетка с обезьянами', on_press=self.recive_monkeys, style=Pack(font_size=14, background_color='#98FB98'))
        self.int_button_5 = toga.Button('Длинные тексты', on_press=self.recive_nosense, style=Pack(font_size=14, background_color='#98FB98'))
        self.int_button_6 = toga.Button('Волшебник И.Г. Inc', on_press=self.recive_sorcerer, style=Pack(font_size=14, background_color='#98FB98'))
        self.int_button_7 = toga.Button('Воришка снов', on_press=self.recive_steel_dream, style=Pack(font_size=14, background_color='#98FB98'))
        self.int_button_8 = toga.Button('Россиянин', on_press=self.recive_russian, style=Pack(font_size=14, background_color='#98FB98'))
        self.int_button_9 = toga.Button('Украина', on_press=self.recive_ukraine, style=Pack(font_size=14, background_color='#98FB98'))
        self.int_button_10 = toga.Button('Напрасное далеко', on_press=self.recive_waste, style=Pack(font_size=14, background_color='#98FB98'))
        self.int_back_button = toga.Button('Назад', on_press=self.back_screen_int, style=Pack(font_size=14, background_color='#FFC0CB'))
        self.box_int.add(self.int_button_1)
        self.box_int.add(self.int_button_2)
        self.box_int.add(self.int_button_3)
        self.box_int.add(self.int_button_4)
        self.box_int.add(self.int_button_5)
        self.box_int.add(self.int_button_6)
        self.box_int.add(self.int_button_7)
        self.box_int.add(self.int_button_8)
        self.box_int.add(self.int_button_9)
        self.box_int.add(self.int_button_10)
        self.box_int.add(self.int_back_button)

        self.creepy_button_1 = toga.Button('Чёрный снег', on_press=self.recive_black_snow, style=Pack(font_size=14, background_color='#98FB98'))
        self.creepy_button_2 = toga.Button('Энский маньяк', on_press=self.recive_maniac, style=Pack(font_size=14, background_color='#98FB98'))
        self.creepy_button_3 = toga.Button('Зеркала', on_press=self.recive_mirrors, style=Pack(font_size=14, background_color='#98FB98'))
        self.creepy_button_4 = toga.Button('НЕХ', on_press=self.recive_neh, style=Pack(font_size=14, background_color='#98FB98'))
        self.creepy_button_5 = toga.Button('Ночь на парковке', on_press=self.recive_night_auto, style=Pack(font_size=14, background_color='#98FB98'))
        self.creepy_button_6 = toga.Button('Ночь в деревне', on_press=self.recive_night_village, style=Pack(font_size=14, background_color='#98FB98'))
        self.creepy_button_7 = toga.Button('Нестареющие', on_press=self.recive_unage, style=Pack(font_size=14, background_color='#98FB98'))
        self.creepy_back_button = toga.Button('Назад', on_press=self.back_screen_creepy, style=Pack(font_size=14, background_color='#FFC0CB'))
        self.box_creepy.add(self.creepy_button_1)
        self.box_creepy.add(self.creepy_button_2)
        self.box_creepy.add(self.creepy_button_3)
        self.box_creepy.add(self.creepy_button_4)
        self.box_creepy.add(self.creepy_button_5)
        self.box_creepy.add(self.creepy_button_6)
        self.box_creepy.add(self.creepy_button_7)
        self.box_creepy.add(self.creepy_back_button)

        self.cringe_button_1 = toga.Button('На связь', on_press=self.recive_again, style=Pack(font_size=14, background_color='#98FB98'))
        self.cringe_button_2 = toga.Button('Огурцы', on_press=self.recive_cucumbers, style=Pack(font_size=14, background_color='#98FB98'))
        self.cringe_button_3 = toga.Button('Самка дельфина', on_press=self.recive_dolphin, style=Pack(font_size=14, background_color='#98FB98'))
        self.cringe_button_4 = toga.Button('Мечта', on_press=self.recive_dream_orig, style=Pack(font_size=14, background_color='#98FB98'))
        self.cringe_button_5 = toga.Button('Мечта 2(ch)', on_press=self.recive_dream_guro, style=Pack(font_size=14, background_color='#98FB98'))
        self.cringe_button_6 = toga.Button('Ненавижу рыжих', on_press=self.recive_hate_ging, style=Pack(font_size=14, background_color='#98FB98'))
        self.cringe_button_7 = toga.Button('Макдональдс', on_press=self.recive_macdonalds, style=Pack(font_size=14, background_color='#98FB98'))
        self.cringe_button_8 = toga.Button('Гель для мужчин', on_press=self.recive_mens_gel, style=Pack(font_size=14, background_color='#98FB98'))
        self.cringe_button_9 = toga.Button('Woman.ru', on_press=self.recive_womanru, style=Pack(font_size=14, background_color='#98FB98'))
        self.cringe_back_button = toga.Button('Назад', on_press=self.back_screen_cringe, style=Pack(font_size=14, background_color='#FFC0CB'))
        self.box_cringe.add(self.cringe_button_1)
        self.box_cringe.add(self.cringe_button_2)
        self.box_cringe.add(self.cringe_button_3)
        self.box_cringe.add(self.cringe_button_4)
        self.box_cringe.add(self.cringe_button_5)
        self.box_cringe.add(self.cringe_button_6)
        self.box_cringe.add(self.cringe_button_7)
        self.box_cringe.add(self.cringe_button_8)
        self.box_cringe.add(self.cringe_button_9)
        self.box_cringe.add(self.cringe_back_button)

        self.rofl_aw_button_1 = toga.Button('Эльфийская песнь', on_press=self.recive_elfen_lied, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_aw_button_2 = toga.Button('Врата Штейна', on_press=self.recive_steins_gate, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_aw_button_3 = toga.Button('Макото Синкай', on_press=self.recive_sinkai, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_aw_button_4 = toga.Button('Наруто', on_press=self.recive_naruto, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_aw_button_5 = toga.Button('Харухи', on_press=self.recive_haruhi, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_aw_button_6 = toga.Button('My Little Pony', on_press=self.recive_my_little_pony, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_aw_button_7 = toga.Button('Minecraft', on_press=self.recive_minecraft, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_aw_back_button = toga.Button('Назад', on_press=self.back_screen_rofl_aw, style=Pack(font_size=14, background_color='#FFC0CB'))
        self.box_rofl_aw.add(self.rofl_aw_button_1)
        self.box_rofl_aw.add(self.rofl_aw_button_2)
        self.box_rofl_aw.add(self.rofl_aw_button_3)
        self.box_rofl_aw.add(self.rofl_aw_button_4)
        self.box_rofl_aw.add(self.rofl_aw_button_5)
        self.box_rofl_aw.add(self.rofl_aw_button_6)
        self.box_rofl_aw.add(self.rofl_aw_button_7)
        self.box_rofl_aw.add(self.rofl_aw_back_button)

        self.rofl_cd_button_1 = toga.Button('Оригинал', on_press=self.recive_cd_orig, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_cd_button_2 = toga.Button('Мажор', on_press=self.recive_cd_major, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_cd_button_3 = toga.Button('WH40K', on_press=self.recive_cd_wh40k, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_cd_back_button = toga.Button('Назад', on_press=self.back_screen_rofl_cd, style=Pack(font_size=14, background_color='#FFC0CB'))
        self.box_rofl_cd.add(self.rofl_cd_button_1)
        self.box_rofl_cd.add(self.rofl_cd_button_2)
        self.box_rofl_cd.add(self.rofl_cd_button_3)
        self.box_rofl_cd.add(self.rofl_cd_back_button)

        self.rofl_dad_button_1 = toga.Button('Жареный суп', on_press=self.recive_dad_fried_soup, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_dad_button_2 = toga.Button('Изотопы', on_press=self.recive_dad_isotop, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_dad_button_3 = toga.Button('Эксперименты', on_press=self.recive_dad_experiments, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_dad_button_4 = toga.Button('Лекции', on_press=self.recive_dad_lections, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_dad_button_5 = toga.Button('Экономика', on_press=self.recive_dad_economy, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_dad_button_6 = toga.Button('Книги', on_press=self.recive_dad_books, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_dad_back_button = toga.Button('Назад', on_press=self.back_screen_rofl_dad, style=Pack(font_size=14, background_color='#FFC0CB'))
        self.box_rofl_dad.add(self.rofl_dad_button_1)
        self.box_rofl_dad.add(self.rofl_dad_button_2)
        self.box_rofl_dad.add(self.rofl_dad_button_3)
        self.box_rofl_dad.add(self.rofl_dad_button_4)
        self.box_rofl_dad.add(self.rofl_dad_button_5)
        self.box_rofl_dad.add(self.rofl_dad_button_6)
        self.box_rofl_dad.add(self.rofl_dad_back_button)

        self.rofl_mh_button_1 = toga.Button('Охотник', on_press=self.recive_mh_hunter, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_mh_button_2 = toga.Button('Фашист', on_press=self.recive_mh_fashist, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_mh_button_3 = toga.Button('Сэндвич', on_press=self.recive_mh_sandwich, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_mh_button_4 = toga.Button('Программист', on_press=self.recive_mh_programmer, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_mh_button_5 = toga.Button('Геймер', on_press=self.recive_mh_gamer, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_mh_button_6 = toga.Button('Священник', on_press=self.recive_mh_priest, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_mh_button_7 = toga.Button('Борец с наркотиками', on_press=self.recive_mh_drug_fighter, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_mh_button_8 = toga.Button('Алконавт', on_press=self.recive_mh_alconaut, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_mh_back_button = toga.Button('Назад', on_press=self.back_screen_rofl_mh, style=Pack(font_size=14, background_color='#FFC0CB'))
        self.box_rofl_mh.add(self.rofl_mh_button_1)
        self.box_rofl_mh.add(self.rofl_mh_button_2)
        self.box_rofl_mh.add(self.rofl_mh_button_3)
        self.box_rofl_mh.add(self.rofl_mh_button_4)
        self.box_rofl_mh.add(self.rofl_mh_button_5)
        self.box_rofl_mh.add(self.rofl_mh_button_6)
        self.box_rofl_mh.add(self.rofl_mh_button_7)
        self.box_rofl_mh.add(self.rofl_mh_button_8)
        self.box_rofl_mh.add(self.rofl_mh_back_button)

        self.rofl_lv_button_1 = toga.Button('Оригинал', on_press=self.recive_lv_original, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_lv_button_2 = toga.Button('Даб Стэп', on_press=self.recive_lv_dub_step, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_lv_button_3 = toga.Button('Россия', on_press=self.recive_lv_russia, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_lv_button_4 = toga.Button('Россия 2', on_press=self.recive_lv_russia_2, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_lv_button_5 = toga.Button('Нацистская Германия', on_press=self.recive_lv_nazi_germany, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_lv_button_6 = toga.Button('Warhammer40k', on_press=self.recive_lv_wh_40k, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_lv_button_7 = toga.Button('Майдан', on_press=self.recive_lv_maidan, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_lv_button_8 = toga.Button('Dota2', on_press=self.recive_lv_dota2, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_lv_button_9 = toga.Button('IOS-разработка', on_press=self.recive_lv_ios_dev, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_lv_button_10 = toga.Button('Ремонт', on_press=self.recive_lv_repair, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_lv_button_11 = toga.Button('Церковь', on_press=self.recive_lv_church, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_lv_button_12 = toga.Button('Матан', on_press=self.recive_lv_math, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_lv_button_13 = toga.Button('Больница', on_press=self.recive_lv_hospital, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_lv_back_button = toga.Button('Назад', on_press=self.back_screen_rofl_lv, style=Pack(font_size=14, background_color='#FFC0CB'))
        self.box_rofl_lv.add(self.rofl_lv_button_1)
        self.box_rofl_lv.add(self.rofl_lv_button_2)
        self.box_rofl_lv.add(self.rofl_lv_button_3)
        self.box_rofl_lv.add(self.rofl_lv_button_4)
        self.box_rofl_lv.add(self.rofl_lv_button_5)
        self.box_rofl_lv.add(self.rofl_lv_button_6)
        self.box_rofl_lv.add(self.rofl_lv_button_7)
        self.box_rofl_lv.add(self.rofl_lv_button_8)
        self.box_rofl_lv.add(self.rofl_lv_button_9)
        self.box_rofl_lv.add(self.rofl_lv_button_10)
        self.box_rofl_lv.add(self.rofl_lv_button_11)
        self.box_rofl_lv.add(self.rofl_lv_button_12)
        self.box_rofl_lv.add(self.rofl_lv_button_13)
        self.box_rofl_lv.add(self.rofl_lv_back_button)

        self.rofl_mt_button_1 = toga.Button('Оригинал', on_press=self.recive_mt_original, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_mt_button_2 = toga.Button('Религия', on_press=self.recive_mt_religion, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_mt_button_3 = toga.Button('Философия', on_press=self.recive_mt_philosophy, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_mt_button_4 = toga.Button('Древний Рим', on_press=self.recive_mt_ancient_rome, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_mt_button_5 = toga.Button('Космос', on_press=self.recive_mt_space, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_mt_button_6 = toga.Button('Семейные ценности', on_press=self.recive_mt_family_values, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_mt_button_7 = toga.Button('Либерализм', on_press=self.recive_mt_liberalism, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_mt_back_button = toga.Button('Назад', on_press=self.back_screen_rofl_mt, style=Pack(font_size=14, background_color='#FFC0CB'))
        self.box_rofl_mt.add(self.rofl_mt_button_1)
        self.box_rofl_mt.add(self.rofl_mt_button_2)
        self.box_rofl_mt.add(self.rofl_mt_button_3)
        self.box_rofl_mt.add(self.rofl_mt_button_4)
        self.box_rofl_mt.add(self.rofl_mt_button_5)
        self.box_rofl_mt.add(self.rofl_mt_button_6)
        self.box_rofl_mt.add(self.rofl_mt_button_7)
        self.box_rofl_mt.add(self.rofl_mt_back_button)

        self.rofl_ch_button_1 = toga.Button('Российская', on_press=self.recive_ch_svo_ru, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_ch_button_2 = toga.Button('Израильская', on_press=self.recive_ch_svo_iz, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_ch_button_3 = toga.Button('Айтишная', on_press=self.recive_ch_svo_it, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_ch_back_button = toga.Button('Назад', on_press=self.back_screen_rofl_ch, style=Pack(font_size=14, background_color='#FFC0CB'))
        self.box_rofl_ch.add(self.rofl_ch_button_1)
        self.box_rofl_ch.add(self.rofl_ch_button_2)
        self.box_rofl_ch.add(self.rofl_ch_button_3)
        self.box_rofl_ch.add(self.rofl_ch_back_button)

        self.rofl_wd_button_1 = toga.Button('Оригинал', on_press=self.recive_wd_windows, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_wd_button_2 = toga.Button('Школа', on_press=self.recive_wd_school, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_wd_button_3 = toga.Button('Девушка', on_press=self.recive_wd_girlfriend, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_wd_button_4 = toga.Button('Овуляха', on_press=self.recive_wd_ovul, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_wd_button_5 = toga.Button('Саске', on_press=self.recive_wd_sasuke, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_wd_button_6 = toga.Button('Старкрафт', on_press=self.recive_wd_sc, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_wd_back_button = toga.Button('Назад', on_press=self.back_screen_rofl_wd, style=Pack(font_size=14, background_color='#FFC0CB'))
        self.box_rofl_wd.add(self.rofl_wd_button_1)
        self.box_rofl_wd.add(self.rofl_wd_button_2)
        self.box_rofl_wd.add(self.rofl_wd_button_3)
        self.box_rofl_wd.add(self.rofl_wd_button_4)
        self.box_rofl_wd.add(self.rofl_wd_button_5)
        self.box_rofl_wd.add(self.rofl_wd_button_6)
        self.box_rofl_wd.add(self.rofl_wd_back_button)

        self.rofl_group_button_1 = toga.Button('После просмотра', on_press=self.next_screen_rofl_aw, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_group_button_2 = toga.Button('Трудное детство', on_press=self.next_screen_rofl_cd, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_group_button_3 = toga.Button('Мой батя', on_press=self.next_screen_rofl_dad, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_group_button_4 = toga.Button('Мой муж', on_press=self.next_screen_rofl_mh, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_group_button_5 = toga.Button('Лас-Вегас', on_press=self.next_screen_rofl_lv, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_group_button_6 = toga.Button('Мытищи', on_press=self.next_screen_rofl_mt, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_group_button_7 = toga.Button('Чернухин', on_press=self.next_screen_rofl_ch, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_group_button_8 = toga.Button('ШINDOWS', on_press=self.next_screen_rofl_wd, style=Pack(font_size=14, background_color='#98FB98'))
        self.rofl_group_back_button = toga.Button('Назад', on_press=self.back_screen_rofl_group, style=Pack(font_size=14, background_color='#FFC0CB'))
        self.box_rofl_group.add(self.rofl_group_button_1)
        self.box_rofl_group.add(self.rofl_group_button_2)
        self.box_rofl_group.add(self.rofl_group_button_3)
        self.box_rofl_group.add(self.rofl_group_button_4)
        self.box_rofl_group.add(self.rofl_group_button_5)
        self.box_rofl_group.add(self.rofl_group_button_6)
        self.box_rofl_group.add(self.rofl_group_button_7)
        self.box_rofl_group.add(self.rofl_group_button_8)
        self.box_rofl_group.add(self.rofl_group_back_button)

        self.others_button_1 = toga.Button('Ачивки турбиниста', on_press=self.recive_achieve_tec, style=Pack(font_size=14, background_color='#98FB98'))
        self.others_button_2 = toga.Button('Ачивки котельщика', on_press=self.recive_achieve_tec_2, style=Pack(font_size=14, background_color='#98FB98'))
        self.others_button_3 = toga.Button('Казино', on_press=self.recive_casino, style=Pack(font_size=14, background_color='#98FB98'))
        self.others_button_4 = toga.Button('Привет', on_press=self.recive_hi, style=Pack(font_size=14, background_color='#98FB98'))
        self.others_button_5 = toga.Button('Хуяк!', on_press=self.recive_huyak, style=Pack(font_size=14, background_color='#98FB98'))
        self.others_button_6 = toga.Button('Айфон', on_press=self.recive_iphone, style=Pack(font_size=14, background_color='#98FB98'))
        self.others_button_7 = toga.Button('Java', on_press=self.recive_java, style=Pack(font_size=14, background_color='#98FB98'))
        self.others_button_8 = toga.Button('Ла(м)почка', on_press=self.recive_lamp_girl, style=Pack(font_size=14, background_color='#98FB98'))
        self.others_button_9 = toga.Button('Настоящие мужики', on_press=self.recive_real_men, style=Pack(font_size=14, background_color='#98FB98'))
        self.others_button_10 = toga.Button('Хороший день', on_press=self.recive_today, style=Pack(font_size=14, background_color='#98FB98'))
        self.others_back_button = toga.Button('Назад', on_press=self.back_screen_others, style=Pack(font_size=14, background_color='#FFC0CB'))
        self.box_others.add(self.others_button_1)
        self.box_others.add(self.others_button_2)
        self.box_others.add(self.others_button_3)
        self.box_others.add(self.others_button_4)
        self.box_others.add(self.others_button_5)
        self.box_others.add(self.others_button_6)
        self.box_others.add(self.others_button_7)
        self.box_others.add(self.others_button_8)
        self.box_others.add(self.others_button_9)
        self.box_others.add(self.others_button_10)
        self.box_others.add(self.others_back_button)

        self.main_button_int = toga.Button('Интересные', on_press=self.next_screen_int, style=Pack(font_size=14, background_color='#98FB98'))
        self.main_button_creepy = toga.Button('Криповые', on_press=self.next_screen_creepy, style=Pack(font_size=14, background_color='#98FB98'))
        self.main_button_cringe = toga.Button('Кринжовые', on_press=self.next_screen_cringe, style=Pack(font_size=14, background_color='#98FB98'))
        self.main_button_rofl = toga.Button('Смехуечки', on_press=self.next_screen_rofl_group, style=Pack(font_size=14, background_color='#98FB98'))
        self.main_button_others = toga.Button('Прочие', on_press=self.next_screen_others, style=Pack(font_size=14, background_color='#98FB98'))
        self.box_main.add(self.main_button_int)
        self.box_main.add(self.main_button_creepy)
        self.box_main.add(self.main_button_cringe)
        self.box_main.add(self.main_button_rofl)
        self.box_main.add(self.main_button_others)

        self.read_place_int = toga.MultilineTextInput(readonly=True, style=Pack(font_size=14, flex=9))
        self.read_int_back_button = toga.Button('Назад', on_press=self.back_screen_read_int, style=Pack(flex=1, background_color='#FFC0CB'))
        self.box_read_int.add(self.read_place_int)
        self.box_read_int.add(self.read_int_back_button)

        self.read_place_creepy = toga.MultilineTextInput(readonly=True, style=Pack(font_size=14, flex=9))
        self.read_creepy_back_button = toga.Button('Назад', on_press=self.back_screen_read_creepy, style=Pack(flex=1, background_color='#FFC0CB'))
        self.box_read_creepy.add(self.read_place_creepy)
        self.box_read_creepy.add(self.read_creepy_back_button)

        self.read_place_cringe = toga.MultilineTextInput(readonly=True, style=Pack(font_size=14, flex=9))
        self.read_cringe_back_button = toga.Button('Назад', on_press=self.back_screen_read_cringe, style=Pack(flex=1, background_color='#FFC0CB'))
        self.box_read_cringe.add(self.read_place_cringe)
        self.box_read_cringe.add(self.read_cringe_back_button)

        self.read_place_rofl_aw = toga.MultilineTextInput(readonly=True, style=Pack(font_size=14, flex=9))
        self.read_rofl_aw_back_button = toga.Button('Назад', on_press=self.back_screen_read_rofl_aw, style=Pack(flex=1, background_color='#FFC0CB'))
        self.box_read_rofl_aw.add(self.read_place_rofl_aw)
        self.box_read_rofl_aw.add(self.read_rofl_aw_back_button)

        self.read_place_rofl_cd = toga.MultilineTextInput(readonly=True, style=Pack(font_size=14, flex=9))
        self.read_rofl_cd_back_button = toga.Button('Назад', on_press=self.back_screen_read_rofl_cd, style=Pack(flex=1, background_color='#FFC0CB'))
        self.box_read_rofl_cd.add(self.read_place_rofl_cd)
        self.box_read_rofl_cd.add(self.read_rofl_cd_back_button)

        self.read_place_rofl_dad = toga.MultilineTextInput(readonly=True, style=Pack(font_size=14, flex=9))
        self.read_rofl_dad_back_button = toga.Button('Назад', on_press=self.back_screen_read_rofl_dad, style=Pack(flex=1, background_color='#FFC0CB'))
        self.box_read_rofl_dad.add(self.read_place_rofl_dad)
        self.box_read_rofl_dad.add(self.read_rofl_dad_back_button)

        self.read_place_rofl_mh = toga.MultilineTextInput(readonly=True, style=Pack(font_size=14, flex=9))
        self.read_rofl_mh_back_button = toga.Button('Назад', on_press=self.back_screen_read_rofl_mh, style=Pack(flex=1, background_color='#FFC0CB'))
        self.box_read_rofl_mh.add(self.read_place_rofl_mh)
        self.box_read_rofl_mh.add(self.read_rofl_mh_back_button)

        self.read_place_rofl_lv = toga.MultilineTextInput(readonly=True, style=Pack(font_size=14, flex=9))
        self.read_rofl_lv_back_button = toga.Button('Назад', on_press=self.back_screen_read_rofl_lv, style=Pack(flex=1, background_color='#FFC0CB'))
        self.box_read_rofl_lv.add(self.read_place_rofl_lv)
        self.box_read_rofl_lv.add(self.read_rofl_lv_back_button)

        self.read_place_rofl_mt = toga.MultilineTextInput(readonly=True, style=Pack(font_size=14, flex=9))
        self.read_rofl_mt_back_button = toga.Button('Назад', on_press=self.back_screen_read_rofl_mt, style=Pack(flex=1, background_color='#FFC0CB'))
        self.box_read_rofl_mt.add(self.read_place_rofl_mt)
        self.box_read_rofl_mt.add(self.read_rofl_mt_back_button)

        self.read_place_rofl_ch = toga.MultilineTextInput(readonly=True, style=Pack(font_size=14, flex=9))
        self.read_rofl_ch_back_button = toga.Button('Назад', on_press=self.back_screen_read_rofl_ch, style=Pack(flex=1, background_color='#FFC0CB'))
        self.box_read_rofl_ch.add(self.read_place_rofl_ch)
        self.box_read_rofl_ch.add(self.read_rofl_ch_back_button)

        self.read_place_rofl_wd = toga.MultilineTextInput(readonly=True, style=Pack(font_size=14, flex=9))
        self.read_rofl_wd_back_button = toga.Button('Назад', on_press=self.back_screen_read_rofl_wd, style=Pack(flex=1, background_color='#FFC0CB'))
        self.box_read_rofl_wd.add(self.read_place_rofl_wd)
        self.box_read_rofl_wd.add(self.read_rofl_wd_back_button)

        self.read_place_others = toga.MultilineTextInput(readonly=True,  style=Pack(font_size=14, flex=9))
        self.read_others_back_button = toga.Button('Назад', on_press=self.back_screen_read_others, style=Pack(flex=1, background_color='#FFC0CB'))
        self.box_read_others.add(self.read_place_others)
        self.box_read_others.add(self.read_others_back_button)

        self.error_place = toga.MultilineTextInput(
            value='Не удается установить соединение с сервером. Проверьте подключение к интернету.', readonly=True,
            style=Pack(background_color='#FF4500', font_size=14, flex=9))
        self.error_back_button = toga.Button('ОК', on_press=self.back_screen_error, style=Pack(flex=1, background_color='#FFC0CB'))
        self.box_error.add(self.error_place)
        self.box_error.add(self.error_back_button)

        self.main_box.add(self.box_main)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    def next_screen_int(self, box):
        self.main_box.remove(self.box_main)
        self.main_box.add(self.box_int)

    def back_screen_int(self, box):
        self.main_box.remove(self.box_int)
        self.main_box.add(self.box_main)

    def next_screen_creepy(self, box):
        self.main_box.remove(self.box_main)
        self.main_box.add(self.box_creepy)

    def back_screen_creepy(self, box):
        self.main_box.remove(self.box_creepy)
        self.main_box.add(self.box_main)

    def next_screen_cringe(self, box):
        self.main_box.remove(self.box_main)
        self.main_box.add(self.box_cringe)

    def back_screen_cringe(self, box):
        self.main_box.remove(self.box_cringe)
        self.main_box.add(self.box_main)

    def next_screen_rofl_group(self, box):
        self.main_box.remove(self.box_main)
        self.main_box.add(self.box_rofl_group)

    def back_screen_rofl_group(self, box):
        self.main_box.remove(self.box_rofl_group)
        self.main_box.add(self.box_main)

    def next_screen_others(self, box):
        self.main_box.remove(self.box_main)
        self.main_box.add(self.box_others)

    def back_screen_others(self, box):
        self.main_box.remove(self.box_others)
        self.main_box.add(self.box_main)

    def next_screen_rofl_aw(self, box):
        self.main_box.remove(self.box_rofl_group)
        self.main_box.add(self.box_rofl_aw)

    def back_screen_rofl_aw(self, box):
        self.main_box.remove(self.box_rofl_aw)
        self.main_box.add(self.box_rofl_group)

    def next_screen_rofl_cd(self, box):
        self.main_box.remove(self.box_rofl_group)
        self.main_box.add(self.box_rofl_cd)

    def back_screen_rofl_cd(self, box):
        self.main_box.remove(self.box_rofl_cd)
        self.main_box.add(self.box_rofl_group)

    def next_screen_rofl_dad(self, box):
        self.main_box.remove(self.box_rofl_group)
        self.main_box.add(self.box_rofl_dad)

    def back_screen_rofl_dad(self, box):
        self.main_box.remove(self.box_rofl_dad)
        self.main_box.add(self.box_rofl_group)

    def next_screen_rofl_mh(self, box):
        self.main_box.remove(self.box_rofl_group)
        self.main_box.add(self.box_rofl_mh)

    def back_screen_rofl_mh(self, box):
        self.main_box.remove(self.box_rofl_mh)
        self.main_box.add(self.box_rofl_group)

    def next_screen_rofl_lv(self, box):
        self.main_box.remove(self.box_rofl_group)
        self.main_box.add(self.box_rofl_lv)

    def back_screen_rofl_lv(self, box):
        self.main_box.remove(self.box_rofl_lv)
        self.main_box.add(self.box_rofl_group)

    def next_screen_rofl_mt(self, box):
        self.main_box.remove(self.box_rofl_group)
        self.main_box.add(self.box_rofl_mt)

    def back_screen_rofl_mt(self, box):
        self.main_box.remove(self.box_rofl_mt)
        self.main_box.add(self.box_rofl_group)

    def next_screen_rofl_ch(self, box):
        self.main_box.remove(self.box_rofl_group)
        self.main_box.add(self.box_rofl_ch)

    def back_screen_rofl_ch(self, box):
        self.main_box.remove(self.box_rofl_ch)
        self.main_box.add(self.box_rofl_group)

    def next_screen_rofl_wd(self, box):
        self.main_box.remove(self.box_rofl_group)
        self.main_box.add(self.box_rofl_wd)

    def back_screen_rofl_wd(self, box):
        self.main_box.remove(self.box_rofl_wd)
        self.main_box.add(self.box_rofl_group)

    def next_screen_read_int(self, box):
        self.main_box.remove(self.box_int)
        self.main_box.add(self.box_read_int)

    def back_screen_read_int(self, box):
        self.main_box.remove(self.box_read_int)
        self.main_box.add(self.box_int)

    def next_screen_read_creepy(self, box):
        self.main_box.remove(self.box_creepy)
        self.main_box.add(self.box_read_creepy)

    def back_screen_read_creepy(self, box):
        self.main_box.remove(self.box_read_creepy)
        self.main_box.add(self.box_creepy)

    def next_screen_read_cringe(self, box):
        self.main_box.remove(self.box_cringe)
        self.main_box.add(self.box_read_cringe)

    def back_screen_read_cringe(self, box):
        self.main_box.remove(self.box_read_cringe)
        self.main_box.add(self.box_cringe)

    def next_screen_read_rofl_aw(self, box):
        self.main_box.remove(self.box_rofl_aw)
        self.main_box.add(self.box_read_rofl_aw)

    def back_screen_read_rofl_aw(self, box):
        self.main_box.remove(self.box_read_rofl_aw)
        self.main_box.add(self.box_rofl_aw)

    def next_screen_read_rofl_cd(self, box):
        self.main_box.remove(self.box_rofl_cd)
        self.main_box.add(self.box_read_rofl_cd)

    def back_screen_read_rofl_cd(self, box):
        self.main_box.remove(self.box_read_rofl_cd)
        self.main_box.add(self.box_rofl_cd)

    def next_screen_read_rofl_dad(self, box):
        self.main_box.remove(self.box_rofl_dad)
        self.main_box.add(self.box_read_rofl_dad)

    def back_screen_read_rofl_dad(self, box):
        self.main_box.remove(self.box_read_rofl_dad)
        self.main_box.add(self.box_rofl_dad)

    def next_screen_read_rofl_mh(self, box):
        self.main_box.remove(self.box_rofl_mh)
        self.main_box.add(self.box_read_rofl_mh)

    def back_screen_read_rofl_mh(self, box):
        self.main_box.remove(self.box_read_rofl_mh)
        self.main_box.add(self.box_rofl_mh)

    def next_screen_read_rofl_lv(self, box):
        self.main_box.remove(self.box_rofl_lv)
        self.main_box.add(self.box_read_rofl_lv)

    def back_screen_read_rofl_lv(self, box):
        self.main_box.remove(self.box_read_rofl_lv)
        self.main_box.add(self.box_rofl_lv)

    def next_screen_read_rofl_mt(self, box):
        self.main_box.remove(self.box_rofl_mt)
        self.main_box.add(self.box_read_rofl_mt)

    def back_screen_read_rofl_mt(self, box):
        self.main_box.remove(self.box_read_rofl_mt)
        self.main_box.add(self.box_rofl_mt)

    def next_screen_read_rofl_ch(self, box):
        self.main_box.remove(self.box_rofl_ch)
        self.main_box.add(self.box_read_rofl_ch)

    def back_screen_read_rofl_ch(self, box):
        self.main_box.remove(self.box_read_rofl_ch)
        self.main_box.add(self.box_rofl_ch)

    def next_screen_read_rofl_wd(self, box):
        self.main_box.remove(self.box_rofl_wd)
        self.main_box.add(self.box_read_rofl_wd)

    def back_screen_read_rofl_wd(self, box):
        self.main_box.remove(self.box_read_rofl_wd)
        self.main_box.add(self.box_rofl_wd)

    def next_screen_read_others(self, box):
        self.main_box.remove(self.box_others)
        self.main_box.add(self.box_read_others)

    def back_screen_read_others(self, box):
        self.main_box.remove(self.box_read_others)
        self.main_box.add(self.box_others)

    def connection_error_int(self, box):
        self.main_box.remove(self.box_int)
        self.main_box.add(self.box_error)

    def connection_error_creepy(self, box):
        self.main_box.remove(self.box_creepy)
        self.main_box.add(self.box_error)

    def connection_error_cringe(self, box):
        self.main_box.remove(self.box_cringe)
        self.main_box.add(self.box_error)

    def connection_error_rofl_aw(self, box):
        self.main_box.remove(self.box_rofl_aw)
        self.main_box.add(self.box_error)

    def connection_error_rofl_cd(self, box):
        self.main_box.remove(self.box_rofl_cd)
        self.main_box.add(self.box_error)

    def connection_error_rofl_dad(self, box):
        self.main_box.remove(self.box_rofl_dad)
        self.main_box.add(self.box_error)

    def connection_error_rofl_mh(self, box):
        self.main_box.remove(self.box_rofl_mh)
        self.main_box.add(self.box_error)

    def connection_error_rofl_lv(self, box):
        self.main_box.remove(self.box_rofl_lv)
        self.main_box.add(self.box_error)

    def connection_error_rofl_mt(self, box):
        self.main_box.remove(self.box_rofl_mt)
        self.main_box.add(self.box_error)

    def connection_error_rofl_ch(self, box):
        self.main_box.remove(self.box_rofl_ch)
        self.main_box.add(self.box_error)

    def connection_error_rofl_wd(self, box):
        self.main_box.remove(self.box_rofl_wd)
        self.main_box.add(self.box_error)

    def connection_error_others(self, box):
        self.main_box.remove(self.box_others)
        self.main_box.add(self.box_error)

    def back_screen_error(self, box):
        self.main_box.remove(self.box_error)
        self.main_box.add(self.box_main)

    async def recive_funeral(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/interesting/funeral.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_int.value = self.pasta
                    self.next_screen_read_int(self.pasta)
        except:
            self.connection_error_int(self.box_read_int)

    async def recive_haruhi_irl(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/interesting/haruhi_irl.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_int.value = self.pasta
                    self.next_screen_read_int(self.pasta)
        except:
            self.connection_error_int(self.box_read_int)

    async def recive_hurry_up(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/interesting/hurry_up.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_int.value = self.pasta
                    self.next_screen_read_int(self.pasta)
        except:
            self.connection_error_int(self.box_read_int)

    async def recive_monkeys(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/interesting/monkeys.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_int.value = self.pasta
                    self.next_screen_read_int(self.pasta)
        except:
            self.connection_error_int(self.box_read_int)

    async def recive_nosense(self, resp):
        async with aiohttp.ClientSession() as session:
            async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/interesting/nosense.txt".format(username=username)),
            headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                self.pasta = await self.resp.text()
                self.read_place_int.value = self.pasta
                self.next_screen_read_int(self.pasta)

    async def recive_russian(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/interesting/russian.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_int.value = self.pasta
                    self.next_screen_read_int(self.pasta)
        except:
            self.connection_error_int(self.box_read_int)

    async def recive_sorcerer(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/interesting/sorcerer.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_int.value = self.pasta
                    self.next_screen_read_int(self.pasta)
        except:
            self.connection_error_int(self.box_read_int)

    async def recive_steel_dream(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/interesting/steel_dream.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_int.value = self.pasta
                    self.next_screen_read_int(self.pasta)
        except:
            self.connection_error_int(self.box_read_int)

    async def recive_ukraine(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/interesting/ukraine.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_int.value = self.pasta
                    self.next_screen_read_int(self.pasta)
        except:
            self.connection_error_int(self.box_read_int)

    async def recive_waste(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/interesting/waste.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_int.value = self.pasta
                    self.next_screen_read_int(self.pasta)
        except:
            self.connection_error_int(self.box_read_int)

    async def recive_black_snow(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/creepy/black_snow.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_creepy.value = self.pasta
                    self.next_screen_read_creepy(self.pasta)
        except:
            self.connection_error_creepy(self.box_read_creepy)

    async def recive_maniac(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/creepy/maniac.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_creepy.value = self.pasta
                    self.next_screen_read_creepy(self.pasta)
        except:
            self.connection_error_creepy(self.box_read_creepy)

    async def recive_mirrors(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/creepy/mirrors.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_creepy.value = self.pasta
                    self.next_screen_read_creepy(self.pasta)
        except:
            self.connection_error_creepy(self.box_read_creepy)

    async def recive_neh(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/creepy/neh.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_creepy.value = self.pasta
                    self.next_screen_read_creepy(self.pasta)
        except:
            self.connection_error_creepy(self.box_read_creepy)

    async def recive_night_auto(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/creepy/night_auto.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_creepy.value = self.pasta
                    self.next_screen_read_creepy(self.pasta)
        except:
            self.connection_error_creepy(self.box_read_creepy)

    async def recive_night_village(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/creepy/night_village.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_creepy.value = self.pasta
                    self.next_screen_read_creepy(self.pasta)
        except:
            self.connection_error_creepy(self.box_read_creepy)

    async def recive_unage(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/creepy/unage.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_creepy.value = self.pasta
                    self.next_screen_read_creepy(self.pasta)
        except:
            self.connection_error_creepy(self.box_read_creepy)

    async def recive_again(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/cringe/again.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_cringe.value = self.pasta
                    self.next_screen_read_cringe(self.pasta)
        except:
            self.connection_error_cringe(self.box_read_cringe)

    async def recive_cucumbers(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/cringe/cucumbers.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_cringe.value = self.pasta
                    self.next_screen_read_cringe(self.pasta)
        except:
            self.connection_error_cringe(self.box_read_cringe)

    async def recive_dolphin(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/cringe/dolphin.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_cringe.value = self.pasta
                    self.next_screen_read_cringe(self.pasta)
        except:
            self.connection_error_cringe(self.box_read_cringe)

    async def recive_dream_guro(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/cringe/dream_guro.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_cringe.value = self.pasta
                    self.next_screen_read_cringe(self.pasta)
        except:
            self.connection_error_cringe(self.box_read_cringe)

    async def recive_dream_orig(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/cringe/dream_orig.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_cringe.value = self.pasta
                    self.next_screen_read_cringe(self.pasta)
        except:
            self.connection_error_cringe(self.box_read_cringe)

    async def recive_hate_ging(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/cringe/hate_ging.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_cringe.value = self.pasta
                    self.next_screen_read_cringe(self.pasta)
        except:
            self.connection_error_cringe(self.box_read_cringe)

    async def recive_macdonalds(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/cringe/macdonalds.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_cringe.value = self.pasta
                    self.next_screen_read_cringe(self.pasta)
        except:
            self.connection_error_cringe(self.box_read_cringe)

    async def recive_mens_gel(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/cringe/mens_gel.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_cringe.value = self.pasta
                    self.next_screen_read_cringe(self.pasta)
        except:
            self.connection_error_cringe(self.box_read_cringe)

    async def recive_womanru(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/cringe/womanru.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_cringe.value = self.pasta
                    self.next_screen_read_cringe(self.pasta)
        except:
            self.connection_error_cringe(self.box_read_cringe)

    async def recive_elfen_lied(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/after_watch/elfen_lied.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_aw.value = self.pasta
                    self.next_screen_read_rofl_aw(self.pasta)
        except:
            self.connection_error_rofl_aw(self.box_read_rofl_aw)

    async def recive_haruhi(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/after_watch/haruhi.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_aw.value = self.pasta
                    self.next_screen_read_rofl_aw(self.pasta)
        except:
            self.connection_error_rofl_aw(self.box_read_rofl_aw)

    async def recive_sinkai(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/after_watch/sinkai.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_aw.value = self.pasta
                    self.next_screen_read_rofl_aw(self.pasta)
        except:
            self.connection_error_rofl_aw(self.box_read_rofl_aw)

    async def recive_minecraft(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/after_watch/minecraft.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_aw.value = self.pasta
                    self.next_screen_read_rofl_aw(self.pasta)
        except:
            self.connection_error_rofl_aw(self.box_read_rofl_aw)

    async def recive_my_little_pony(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/after_watch/my_little_pony.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_aw.value = self.pasta
                    self.next_screen_read_rofl_aw(self.pasta)
        except:
            self.connection_error_rofl_aw(self.box_read_rofl_aw)

    async def recive_naruto(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/after_watch/naruto.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_aw.value = self.pasta
                    self.next_screen_read_rofl_aw(self.pasta)
        except:
            self.connection_error_rofl_aw(self.box_read_rofl_aw)

    async def recive_steins_gate(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/after_watch/steins_gate.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_aw.value = self.pasta
                    self.next_screen_read_rofl_aw(self.pasta)
        except:
            self.connection_error_rofl_aw(self.box_read_rofl_aw)

    async def recive_cd_orig(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/childhood/childhood_orig.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_cd.value = self.pasta
                    self.next_screen_read_rofl_cd(self.pasta)
        except:
            self.connection_error_rofl_cd(self.box_read_rofl_cd)

    async def recive_cd_wh40k(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/childhood/childhood_wh40k.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_cd.value = self.pasta
                    self.next_screen_read_rofl_cd(self.pasta)
        except:
            self.connection_error_rofl_cd(self.box_read_rofl_cd)

    async def recive_cd_major(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/childhood/childhood_major.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_cd.value = self.pasta
                    self.next_screen_read_rofl_cd(self.pasta)
        except:
            self.connection_error_rofl_cd(self.box_read_rofl_cd)

    async def recive_dad_fried_soup(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/dad/fried_soup.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_dad.value = self.pasta
                    self.next_screen_read_rofl_dad(self.pasta)
        except:
            self.connection_error_rofl_dad(self.box_read_rofl_dad)

    async def recive_dad_books(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/dad/books.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_dad.value = self.pasta
                    self.next_screen_read_rofl_dad(self.pasta)
        except:
            self.connection_error_rofl_dad(self.box_read_rofl_dad)

    async def recive_dad_economy(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/dad/economy.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_dad.value = self.pasta
                    self.next_screen_read_rofl_dad(self.pasta)
        except:
            self.connection_error_rofl_dad(self.box_read_rofl_dad)

    async def recive_dad_experiments(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/dad/experiments.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_dad.value = self.pasta
                    self.next_screen_read_rofl_dad(self.pasta)
        except:
            self.connection_error_rofl_dad(self.box_read_rofl_dad)

    async def recive_dad_isotop(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/dad/isotop.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_dad.value = self.pasta
                    self.next_screen_read_rofl_dad(self.pasta)
        except:
            self.connection_error_rofl_dad(self.box_read_rofl_dad)

    async def recive_dad_lections(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/dad/lections.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_dad.value = self.pasta
                    self.next_screen_read_rofl_dad(self.pasta)
        except:
            self.connection_error_rofl_dad(self.box_read_rofl_dad)

    async def recive_mh_alconaut(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/hunter/alconaut.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_mh.value = self.pasta
                    self.next_screen_read_rofl_mh(self.pasta)
        except:
            self.connection_error_rofl_mh(self.box_read_rofl_mh)

    async def recive_mh_drug_fighter(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/hunter/drug_fighter.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_mh.value = self.pasta
                    self.next_screen_read_rofl_mh(self.pasta)
        except:
            self.connection_error_rofl_mh(self.box_read_rofl_mh)

    async def recive_mh_fashist(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/hunter/fashist.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_mh.value = self.pasta
                    self.next_screen_read_rofl_mh(self.pasta)
        except:
            self.connection_error_rofl_mh(self.box_read_rofl_mh)

    async def recive_mh_gamer(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/hunter/gamer.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_mh.value = self.pasta
                    self.next_screen_read_rofl_mh(self.pasta)
        except:
            self.connection_error_rofl_mh(self.box_read_rofl_mh)

    async def recive_mh_hunter(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/hunter/hunter.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_mh.value = self.pasta
                    self.next_screen_read_rofl_mh(self.pasta)
        except:
            self.connection_error_rofl_mh(self.box_read_rofl_mh)

    async def recive_mh_priest(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/hunter/priest.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_mh.value = self.pasta
                    self.next_screen_read_rofl_mh(self.pasta)
        except:
            self.connection_error_rofl_mh(self.box_read_rofl_mh)

    async def recive_mh_programmer(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/hunter/programmer.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_mh.value = self.pasta
                    self.next_screen_read_rofl_mh(self.pasta)
        except:
            self.connection_error_rofl_mh(self.box_read_rofl_mh)

    async def recive_mh_sandwich(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/hunter/sandwich.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_mh.value = self.pasta
                    self.next_screen_read_rofl_mh(self.pasta)
        except:
            self.connection_error_rofl_mh(self.box_read_rofl_mh)

    async def recive_lv_church(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/las_vegas/church.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_lv.value = self.pasta
                    self.next_screen_read_rofl_lv(self.pasta)
        except:
            self.connection_error_rofl_lv(self.box_read_rofl_lv)

    async def recive_lv_dota2(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/las_vegas/dota2.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_lv.value = self.pasta
                    self.next_screen_read_rofl_lv(self.pasta)
        except:
            self.connection_error_rofl_lv(self.box_read_rofl_lv)

    async def recive_lv_dub_step(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/las_vegas/dub_step.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_lv.value = self.pasta
                    self.next_screen_read_rofl_lv(self.pasta)
        except:
            self.connection_error_rofl_lv(self.box_read_rofl_lv)

    async def recive_lv_hospital(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/las_vegas/hospital.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_lv.value = self.pasta
                    self.next_screen_read_rofl_lv(self.pasta)
        except:
            self.connection_error_rofl_lv(self.box_read_rofl_lv)

    async def recive_lv_ios_dev(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/las_vegas/ios_dev.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_lv.value = self.pasta
                    self.next_screen_read_rofl_lv(self.pasta)
        except:
            self.connection_error_rofl_lv(self.box_read_rofl_lv)

    async def recive_lv_maidan(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/las_vegas/maidan.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_lv.value = self.pasta
                    self.next_screen_read_rofl_lv(self.pasta)
        except:
            self.connection_error_rofl_lv(self.box_read_rofl_lv)

    async def recive_lv_math(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/las_vegas/math.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_lv.value = self.pasta
                    self.next_screen_read_rofl_lv(self.pasta)
        except:
            self.connection_error_rofl_lv(self.box_read_rofl_lv)

    async def recive_lv_nazi_germany(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/las_vegas/nazi_germany.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_lv.value = self.pasta
                    self.next_screen_read_rofl_lv(self.pasta)
        except:
            self.connection_error_rofl_lv(self.box_read_rofl_lv)

    async def recive_lv_original(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/las_vegas/original.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_lv.value = self.pasta
                    self.next_screen_read_rofl_lv(self.pasta)
        except:
            self.connection_error_rofl_lv(self.box_read_rofl_lv)

    async def recive_lv_repair(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/las_vegas/repair.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_lv.value = self.pasta
                    self.next_screen_read_rofl_lv(self.pasta)
        except:
            self.connection_error_rofl_lv(self.box_read_rofl_lv)

    async def recive_lv_russia(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/las_vegas/russia.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_lv.value = self.pasta
                    self.next_screen_read_rofl_lv(self.pasta)
        except:
            self.connection_error_rofl_lv(self.box_read_rofl_lv)

    async def recive_lv_russia_2(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/las_vegas/russia_2.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_lv.value = self.pasta
                    self.next_screen_read_rofl_lv(self.pasta)
        except:
            self.connection_error_rofl_lv(self.box_read_rofl_lv)

    async def recive_lv_wh_40k(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/las_vegas/wh_40k.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_lv.value = self.pasta
                    self.next_screen_read_rofl_lv(self.pasta)
        except:
            self.connection_error_rofl_lv(self.box_read_rofl_lv)

    async def recive_mt_ancient_rome(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/mytischy/ancient_rome.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_mt.value = self.pasta
                    self.next_screen_read_rofl_mt(self.pasta)
        except:
            self.connection_error_rofl_mt(self.box_read_rofl_mt)

    async def recive_mt_family_values(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/mytischy/family_values.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_mt.value = self.pasta
                    self.next_screen_read_rofl_mt(self.pasta)
        except:
            self.connection_error_rofl_mt(self.box_read_rofl_mt)

    async def recive_mt_liberalism(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/mytischy/liberalism.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_mt.value = self.pasta
                    self.next_screen_read_rofl_mt(self.pasta)
        except:
            self.connection_error_rofl_mt(self.box_read_rofl_mt)

    async def recive_mt_original(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/mytischy/original.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_mt.value = self.pasta
                    self.next_screen_read_rofl_mt(self.pasta)
        except:
            self.connection_error_rofl_mt(self.box_read_rofl_mt)

    async def recive_mt_philosophy(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/mytischy/philosophy.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_mt.value = self.pasta
                    self.next_screen_read_rofl_mt(self.pasta)
        except:
            self.connection_error_rofl_mt(self.box_read_rofl_mt)

    async def recive_mt_religion(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/mytischy/religion.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_mt.value = self.pasta
                    self.next_screen_read_rofl_mt(self.pasta)
        except:
            self.connection_error_rofl_mt(self.box_read_rofl_mt)

    async def recive_mt_space(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/mytischy/space.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_mt.value = self.pasta
                    self.next_screen_read_rofl_mt(self.pasta)
        except:
            self.connection_error_rofl_mt(self.box_read_rofl_mt)

    async def recive_ch_svo_it(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/svo/svo_it.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_ch.value = self.pasta
                    self.next_screen_read_rofl_ch(self.pasta)
        except:
            self.connection_error_rofl_ch(self.box_read_rofl_ch)

    async def recive_ch_svo_iz(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/svo/svo_iz.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_ch.value = self.pasta
                    self.next_screen_read_rofl_ch(self.pasta)
        except:
            self.connection_error_rofl_ch(self.box_read_rofl_ch)

    async def recive_ch_svo_ru(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/svo/svo_ru.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_ch.value = self.pasta
                    self.next_screen_read_rofl_ch(self.pasta)
        except:
            self.connection_error_rofl_ch(self.box_read_rofl_ch)

    async def recive_wd_girlfriend(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/wind/wind_girlfriend.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_wd.value = self.pasta
                    self.next_screen_read_rofl_wd(self.pasta)
        except:
            self.connection_error_rofl_wd(self.box_read_rofl_wd)

    async def recive_wd_ovul(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/wind/wind_ovul.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_wd.value = self.pasta
                    self.next_screen_read_rofl_wd(self.pasta)
        except:
            self.connection_error_rofl_wd(self.box_read_rofl_wd)

    async def recive_wd_sasuke(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/wind/wind_sasuke.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_wd.value = self.pasta
                    self.next_screen_read_rofl_wd(self.pasta)
        except:
            self.connection_error_rofl_wd(self.box_read_rofl_wd)

    async def recive_wd_sc(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/wind/wind_sc.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_wd.value = self.pasta
                    self.next_screen_read_rofl_wd(self.pasta)
        except:
            self.connection_error_rofl_wd(self.box_read_rofl_wd)

    async def recive_wd_school(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/wind/wind_school.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_rofl_wd.value = self.pasta
                    self.next_screen_read_rofl_wd(self.pasta)
        except:
            self.connection_error_rofl_wd(self.box_read_rofl_wd)

    async def recive_wd_windows(self, resp):
        async with aiohttp.ClientSession() as session:
            async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/jokes/wind/windows.txt".format(username=username)),
            headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                self.pasta = await self.resp.text()
                self.read_place_rofl_wd.value = self.pasta
                self.next_screen_read_rofl_wd(self.pasta)

    async def recive_achieve_tec(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/others/achieve_tec.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_others.value = self.pasta
                    self.next_screen_read_others(self.pasta)
        except:
            self.connection_error_others(self.box_read_others)

    async def recive_achieve_tec_2(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/others/achieve_tec_2.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_others.value = self.pasta
                    self.next_screen_read_others(self.pasta)
        except:
            self.connection_error_others(self.box_read_others)

    async def recive_casino(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/others/casino.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_others.value = self.pasta
                    self.next_screen_read_others(self.pasta)
        except:
            self.connection_error_others(self.box_read_others)

    async def recive_hi(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/others/hi.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_others.value = self.pasta
                    self.next_screen_read_others(self.pasta)
        except:
            self.connection_error_others(self.box_read_others)

    async def recive_huyak(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/others/huyak.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_others.value = self.pasta
                    self.next_screen_read_others(self.pasta)
        except:
            self.connection_error_others(self.box_read_others)

    async def recive_iphone(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/others/iphone.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_others.value = self.pasta
                    self.next_screen_read_others(self.pasta)
        except:
            self.connection_error_others(self.box_read_others)

    async def recive_java(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/others/java.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_others.value = self.pasta
                    self.next_screen_read_others(self.pasta)
        except:
            self.connection_error_others(self.box_read_others)

    async def recive_lamp_girl(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/others/lamp_girl.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_others.value = self.pasta
                    self.next_screen_read_others(self.pasta)
        except:
            self.connection_error_others(self.box_read_others)

    async def recive_real_men(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/others/real_men.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_others.value = self.pasta
                    self.next_screen_read_others(self.pasta)
        except:
            self.connection_error_others(self.box_read_others)

    async def recive_today(self, resp):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(urljoin(api_base, "files/path/home/{username}/a_rchive/others/today.txt".format(username=username)),
                headers={"Authorization": "Token {api_token}".format(api_token=api_token)}) as self.resp:
                    self.pasta = await self.resp.text()
                    self.read_place_others.value = self.pasta
                    self.next_screen_read_others(self.pasta)
        except:
            self.connection_error_others(self.box_read_others)


def main():
    return PastaArchive()
