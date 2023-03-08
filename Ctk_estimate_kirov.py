import customtkinter as Ctk
from tkinter import *
from tkinter import messagebox
import tkintermapview as tkm
import re
import numpy as np
import datetime
import pickle
import catboost
from catboost import CatBoostRegressor

class App(Ctk.CTk):
    def __init__(self):
        super().__init__()

        Ctk.set_appearance_mode("System")  #Modes: "System" (standard), "Dark", "Light"
        #Ctk.set_default_color_theme("blue")  #Themes: "blue" (standard), "green", "dark-blue"
        #Ctk.set_widget_scaling(1.5)

        model = pickle.load(open("cat_model.pkl", "rb")) #подгружаем модель
        now = datetime.datetime.now()

        self.geometry("820x590") #размер окна
        self.title("Оценка стоимости квартир") #название программы
        self.resizable(False, False) #запрет на изменение размера формы

        self.frame = Ctk.CTkFrame(master = self) #fg_color = "transparent"
        self.frame.grid(row = 1, column = 0, padx = (10, 5), pady = (10, 10), sticky = "nsew")

        self.label_os = Ctk.CTkLabel(master = self.frame, 
                                     text = "Общая площадь:",
                                     width = 100,
                                     height = 25,
                                     fg_color = "transparent",
                                     corner_radius = 8)
        self.label_os.grid(row = 0, column = 0, pady = (10, 10))

        self.label_sk = Ctk.CTkLabel(master = self.frame, 
                                     text = "Площадь кухни:",
                                     width = 100,
                                     height = 25,
                                     fg_color = "transparent",
                                     corner_radius = 8)
        self.label_sk.grid(row = 1, column = 0, pady = (10, 10))

        self.label_sj = Ctk.CTkLabel(master = self.frame, 
                                     text = "Жилая площадь:",
                                     width = 100,
                                     height = 25,
                                     fg_color = "transparent",
                                     corner_radius = 8)
        self.label_sj.grid(row = 2, column = 0, pady = (10, 10))

        self.label_fh = Ctk.CTkLabel(master = self.frame, 
                                     text = "Этажность дома:",
                                     width = 100,
                                     height = 25,
                                     fg_color = "transparent",
                                     corner_radius = 8)
        self.label_fh.grid(row = 3, column = 0, pady = (10, 10))

        self.label_yh = Ctk.CTkLabel(master = self.frame, 
                                     text = "Год постройки дома:",
                                     width = 100,
                                     height = 25,
                                     fg_color = "transparent",
                                     corner_radius = 8)
        self.label_yh.grid(row = 5, column = 0, pady = (10, 10))

        self.label_br = Ctk.CTkLabel(master = self.frame, 
                                     text = "Тип санузла:",
                                     width = 100,
                                     height = 25,
                                     fg_color = "transparent",
                                     corner_radius = 8)
        self.label_br.grid(row = 7, column = 0, pady = (20, 10))

        self.label_nr = Ctk.CTkLabel(master = self.frame, 
                                     text = "Количество комнат:",
                                     width = 100,
                                     height = 25,
                                     fg_color = "transparent",
                                     corner_radius = 8)
        self.label_nr.grid(row = 8, column = 0, pady = (20, 10))

        self.label_lf = Ctk.CTkLabel(master = self.frame, 
                                     text = "Этаж расположения:",
                                     width = 100,
                                     height = 25,
                                     fg_color = "transparent",
                                     corner_radius = 8)
        self.label_lf.grid(row = 9, column = 0, pady = (20, 10))

        self.label_wm = Ctk.CTkLabel(master = self.frame, 
                                     text = "Материал стен:",
                                     width = 100,
                                     height = 25,
                                     fg_color = "transparent",
                                     corner_radius = 8)
        self.label_wm.grid(row = 10, column = 0, pady = (20, 10))

        self.label_fl = Ctk.CTkLabel(master = self.frame, 
                                     text = "Уровень отделки:",
                                     width = 100,
                                     height = 25,
                                     fg_color = "transparent",
                                     corner_radius = 8)
        self.label_fl.grid(row = 11, column = 0, pady = (20, 10))

        def validate_os(action, value_if_allowed, text):
            result = re.match("^[1-9]{1,3}(\.(\d{1,2})?)?$", value_if_allowed) is not None #регулярное выражение!!
            #print(result)
            #print(action)
            #^\d{1,6}(\.\d{1,2})?$
            if (action == '1'):
                if text in '0123456789.':
                    if not result or float(value_if_allowed) > 317: #диапазон площади!!
                        try:
                            messagebox.showwarning(title = "Предупреждение", message = "Некорректный ввод! Общая площадь квартиры должна находиться в диапазоне от 12 кв.м до 317 кв.м!")
                            #self.entry_os.delete(0, END)
                            return False
                        except ValueError:
                            return False
                    else:
                        try:
                            float(value_if_allowed)
                            return True
                        except ValueError:
                            return False
                else:
                    return False
            else:
                return True
            #print(vcmd)
            #return new_value == "" or new_value.isnumeric()
            #validate(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name)
            #vcmd = (self.register(validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        def validate_sk(action, value_if_allowed, text):
            result = re.match("^[1-9]{1,3}(\.(\d{1,2})?)?$", value_if_allowed) is not None #регулярное выражение!!
            #print(result)
            #print(action)
            #^\d{1,6}(\.\d{1,2})?$
            if (action == '1'):
                if text in '0123456789.':
                    if not result or float(value_if_allowed) > 61: #диапазон площади!!
                        try:
                            messagebox.showwarning(title = "Предупреждение", message = "Некорректный ввод! Площадь кухни должна находиться в диапазоне от 2 кв.м до 61 кв.м!")
                            #self.entry_os.delete(0, END)
                            return False
                        except ValueError:
                            return False
                    else:
                        try:
                            float(value_if_allowed)
                            return True
                        except ValueError:
                            return False
                else:
                    return False
            else:
                return True
        
        def validate_sj(action, value_if_allowed, text):
            result = re.match("^[1-9]{1,3}(\.(\d{1,2})?)?$", value_if_allowed) is not None #регулярное выражение!!
            #print(result)
            #print(action)
            #^\d{1,6}(\.\d{1,2})?$
            if (action == '1'):
                if text in '0123456789.' or float(value_if_allowed) > 90:
                    if not result: #диапазон площади!! or len(value_if_allowed) > 5
                        try:
                            messagebox.showwarning(title = "Предупреждение", message = "Некорректный ввод! Жилая площадь квартиры должна находиться в диапазоне от 4 кв.м до 90 кв.м!")
                            #self.entry_os.delete(0, END)
                            return False
                        except ValueError:
                            return False
                    else:
                        try:
                            float(value_if_allowed)
                            return True
                        except ValueError:
                            return False
                else:
                    return False
            else:
                return True
        
        vcmd_os = (self.register(validate_os), '%d', '%P', '%S')
        vcmd_sk = (self.register(validate_sk), '%d', '%P', '%S')
        vcmd_sj = (self.register(validate_sj), '%d', '%P', '%S')

        #Общая площадь
        self.entry_os = Ctk.CTkEntry(master = self.frame, 
                                     width = 55, 
                                     justify = Ctk.CENTER,
                                     font = ("Times", 14), 
                                     validate = 'key', 
                                     validatecommand = vcmd_os)
        self.entry_os.grid(row = 0, column = 1, padx = (0, 20))
        #self.entry_os.insert(3, '0.00')
        #self.entry_os.pack()
        #so = self.entry_os.get()
        #self.entry_os.bind('', lambda e: "break" if self.entry_os.keysym not in(list("1234567890-.")+['BackSpace','Delete','Left','Right']) else "")

        #Площадь кухни
        self.entry_sk = Ctk.CTkEntry(master = self.frame, 
                                     width = 55, 
                                     justify = Ctk.CENTER,
                                     font = ("Times", 14), 
                                     validate = 'key', 
                                     validatecommand = vcmd_sk)
        self.entry_sk.grid(row = 1, column = 1, padx = (0, 20))

        #Жилая площадь
        self.entry_sj = Ctk.CTkEntry(master = self.frame, 
                                     width = 55, 
                                     justify = Ctk.CENTER,
                                     font = ("Times", 14), 
                                     validate = 'key', 
                                     validatecommand = vcmd_sj)
        self.entry_sj.grid(row = 2, column = 1, padx = (0, 20))
        
        #Этажность дома
        self.slider_fh = Ctk.CTkSlider(master = self.frame, 
                                       from_ = 1, 
                                       to = 27, 
                                       number_of_steps = 27, 
                                       width = 130,
                                       #border_width = 20,
                                       command = self.slider_callback_fh)
        #self.slider_fh.grid(row = 4, column = 0, padx = (0, 20))
        self.slider_fh.place(relx = 0.040, rely = 0.325) #anchor = Ctk.CENTER
        self.slider_fh.set(5)

        self.entry_fh = Ctk.CTkEntry(master = self.frame, #сделать ее не доступной!
                                     width = 45, 
                                     justify = Ctk.CENTER,
                                     font = ("Times", 14),
                                     #state = "readonly"
                                     ) #disabled - блокировка
        self.entry_fh.grid(row = 4, column = 1, padx = (0, 20))
        self.entry_fh.bind("<Key>", lambda e: "break") #запрет на ввод данных с клавиатуры, значение изменяется только через slider
        self.entry_fh.insert(0, "5")
        
        #Год постройки дома
        self.slider_yh = Ctk.CTkSlider(master = self.frame, 
                                       from_ = 1890, 
                                       to = now.year, 
                                       number_of_steps = now.year - 1890, 
                                       width = 130,
                                       #border_width = 20,
                                       command = self.slider_callback_yh)
        #self.slider_fh.grid(row = 4, column = 0, padx = (0, 20))
        self.slider_yh.place(relx = 0.040, rely = 0.455) #anchor = Ctk.CENTER
        self.slider_yh.set(2000)

        self.entry_yh = Ctk.CTkEntry(master = self.frame, #сделать ее не доступной!
                                     width = 45, 
                                     justify = Ctk.CENTER,
                                     font = ("Times", 14),
                                     #state = "readonly"
                                     ) #disabled - блокировка
        self.entry_yh.grid(row = 6, column = 1, padx = (0, 20))
        self.entry_yh.bind("<Key>", lambda e: "break") #запрет на ввод данных с клавиатуры, значение изменяется только через slider
        self.entry_yh.insert(0, "2000")

        #Местоположение (координаты)
        self.frame_map = Ctk.CTkFrame(master = self) #fg_color = "transparent"
        self.frame_map.grid(row = 1, column = 1, padx = (5, 10), pady = (10, 10), sticky = "nsew")

        self.map_widget = tkm.TkinterMapView(self.frame_map, 
                                             width = 480, 
                                             height = 418, 
                                             corner_radius = 8)
        self.map_widget.grid(row = 1, column = 0, columnspan = 3, padx = (10, 10), pady = (0, 10))
        #self.map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.map_widget.set_position(58.603595, 49.668023)  #Киров
        self.map_widget.set_zoom(15)
        marker_1 = self.map_widget.set_marker(58.603595, 49.668023, 
                                              #text = "Киров"
                                              )
        #def add_marker_event(coords):
        #    print("Add marker:", coords)
        #    new_marker = self.map_widget.set_marker(coords[0], coords[1], text="new marker")
        
        #self.map_widget.add_right_click_menu_command(label = "Add Marker",
        #                                        command = add_marker_event,
        #                                        pass_coords = True)

        self.label_map = Ctk.CTkLabel(master = self.frame_map, 
                                      text = "Местоположение квартиры:",
                                      width = 120,
                                      height = 25,
                                      fg_color = "transparent",
                                      anchor = "nw",
                                      corner_radius = 8)
        self.label_map.grid(row = 0, column = 0, padx = (5, 5), pady = (10, 0))

        def validate_map(value_if_allowed):
            result = re.match("^([1-9]{0,2}(\.(\d{1,7})?)?)(,)?(\s*([1-9]{0,2}(\.(\d{1,7})?)?)?)?$", value_if_allowed) is not None #регулярное выражение!!
            if not result:
                messagebox.showwarning(title = "Предупреждение", message = "Некорректный ввод! Координаты имеют следующую маску - 58.603595, 49.668023. Вы можете скопировать координаты с карты ниже или Yndex_map.")
                return False
            else:
                return result
        
        vcmd_map = (self.register(validate_map), '%P')

        self.entry_map = Ctk.CTkEntry(master = self.frame_map,
                                      width = 200, 
                                      justify = Ctk.CENTER,
                                      font = ("Times", 14),
                                      validate = 'key',
                                      validatecommand = vcmd_map
                                      #state = "readonly"
                                      ) #disabled - блокировка
        self.entry_map.grid(row = 0, column = 1, padx = (0, 10), pady = (10, 10))
        #self.entry_map.bind("<Key>", lambda e: "break") #запрет на ввод данных с клавиатуры, значение изменяется только через slider
        #self.entry_map.insert(0, "2000")

        #Функция по вставке координат, показывает местоположение
        def show_map():
            #global Lat, Lon
            if self.entry_map.get() == "":
                messagebox.showwarning(title = "Предупреждение", message = "Укажите координаты местоположения квартиры!")
            else:
                marker_1.delete() #удаляем первоначальный маркер
                k = self.entry_map.get() #получаем строку из self.entry_map
                k = k.replace(',', '') #запятую меняем на пробел, это необходимо чтобы координаты с Ya были сопоставимы с tkm
                Lat = float(k.split(' ')[0]) #разделянем строку по признаку пробела
                Lon = float(k.split(' ')[1].strip()) #strip убирает пробелы в начале и конце строки
                #print(Lat)
                #print(Lon)
                self.map_widget.set_position(Lat, Lon) #устанавливаем новую позицию
                self.map_widget.set_zoom(15)
                marker_2 = self.map_widget.set_marker(Lat, Lon) #ставим маркер
                return Lat, Lon
                #pass

        self.button_map = Ctk.CTkButton(master = self.frame_map,
                                        width = 70,
                                        text = "Показать",
                                        corner_radius = 8, 
                                        command = show_map)
        self.button_map.grid(row = 0, column = 2, padx = (0, 10), pady = (10, 10))

        #self.frame_map_option_menu = Ctk.CTkFrame(master = self) #fg_color = "transparent"
        #self.frame_map_option_menu.grid(row = 2, column = 1, padx = (5, 10), pady = (1, 1), sticky = "nsew")

        self.map_option_menu = Ctk.CTkOptionMenu(self.frame_map, 
                                                 values = ["OpenStreetMap", "Google satellite"],
                                                 anchor = "nw",
                                                 command = self.change_map)
        #self.map_option_menu.grid(row = 2, column = 0, padx = (4, 4), pady = (1, 1))
        self.map_option_menu.place(relx = 0.020, rely = 0.834)

        #Тип санузла
        self.optionmenu_br = Ctk.CTkOptionMenu(master = self.frame,
                                               #width = 50,
                                               font = ("Times", 14),
                                               values = ["совмещенный", "раздельный"],
                                               #anchor = "nw",
                                               command = self.change_br
                                               )
        self.optionmenu_br.grid(row = 7, column = 1, padx = (0, 4), pady = (20, 10))

        #Количество комнат
        self.optionmenu_nr = Ctk.CTkOptionMenu(master = self.frame,
                                               #width = 50,
                                               font = ("Times", 14),
                                               values = ["1к", "2к", "3к", "4к и более", "студия"],
                                               #anchor = "nw",
                                               command = self.change_nr
                                               )
        self.optionmenu_nr.grid(row = 8, column = 1, padx = (0, 4), pady = (20, 10))
        self.optionmenu_nr.set("2к")

        #Этаж расположения
        self.optionmenu_lf = Ctk.CTkOptionMenu(master = self.frame,
                                               #width = 50,
                                               font = ("Times", 14),
                                               values = ["первый", "средний", "последний"],
                                               #anchor = "nw",
                                               command = self.change_lf
                                               )
        self.optionmenu_lf.grid(row = 9, column = 1, padx = (0, 4), pady = (20, 10))
        self.optionmenu_lf.set("средний")

        #Материал стен
        self.optionmenu_wm = Ctk.CTkOptionMenu(master = self.frame,
                                               #width = 50,
                                               font = ("Times", 14),
                                               values = ["кирпичный", "панельный", "монолитный", "деревянный"],
                                               #anchor = "nw",
                                               command = self.change_wm
                                               )
        self.optionmenu_wm.grid(row = 10, column = 1, padx = (0, 4), pady = (20, 10))
        self.optionmenu_wm.set("панельный")

        #Уровень отделки
        self.optionmenu_fl = Ctk.CTkOptionMenu(master = self.frame,
                                               #width = 50,
                                               font = ("Times", 14),
                                               values = ["требует ремонта", "стандартный", "евроремонт", "дизайнерский"],
                                               #anchor = "nw",
                                               command = self.change_fl
                                               )
        self.optionmenu_fl.grid(row = 11, column = 1, padx = (0, 4), pady = (20, 10))
        self.optionmenu_fl.set("стандартный")

        self.name_cost = Ctk.CTkLabel(master = self.frame_map, 
                                     text = "Стоимость квартиры:",
                                     #width = 100,
                                     #height = 25,
                                     fg_color = "transparent",
                                     corner_radius = 8)
        self.name_cost.place(relx = 0.30, rely = 0.933)

        self.cost = Ctk.CTkLabel(master = self.frame_map, 
                                 text = "",
                                 #width = 100,
                                 #height = 25,
                                 fg_color = "transparent",
                                 corner_radius = 8)
        self.cost.place(relx = 0.58, rely = 0.933)

        self.cost_kv = Ctk.CTkLabel(master = self.frame_map, 
                                 text = "",
                                 #width = 100,
                                 #height = 25,
                                 fg_color = "transparent",
                                 corner_radius = 8)
        self.cost_kv.place(relx = 0.73, rely = 0.933)

        def predict():
            if self.entry_os.get() == "":
                messagebox.showwarning(title = "Предупреждение", message = "Укажите общую площадь квартиры, она должна находиться в диапазоне от 12 кв.м до 317 кв.м!")
                return
            elif float(self.entry_os.get()) < 12:
                messagebox.showwarning(title = "Предупреждение", message = "Некорректный ввод! Общая площадь квартиры должна находиться в диапазоне от 12 кв.м до 317 кв.м!")
                return
            
            if self.entry_sk.get() == "":
                messagebox.showwarning(title = "Предупреждение", message = "Укажите площадь кухни, она должна находиться в диапазоне от 2 кв.м до 61 кв.м!")
                return
            elif float(self.entry_sk.get()) < 2:
                messagebox.showwarning(title = "Предупреждение", message = "Некорректный ввод! Площадь кухни должна находиться в диапазоне от 2 кв.м до 61 кв.м!")
                return

            if self.entry_sj.get() == "":
                messagebox.showwarning(title = "Предупреждение", message = "Укажите жилую площадь квартиры, она должна находиться в диапазоне от 4 кв.м до 90 кв.м!")
                return
            elif float(self.entry_sj.get()) < 4:
                messagebox.showwarning(title = "Предупреждение", message = "Некорректный ввод! Жилая площадь квартиры должна находиться в диапазоне от 4 кв.м до 90 кв.м!")
                return
            
            if float(self.entry_os.get()) < float(self.entry_sj.get()) or float(self.entry_os.get()) < float(self.entry_sk.get()):
                messagebox.showwarning(title = "Предупреждение", message = "Некорректный ввод! Общая площадь не может быть меньше жилой площади или площади кухни!")
                return
            #???if float(self.entry_sj.get()) < float(self.entry_sk.get()):
                #return messagebox.showwarning(title = "Предупреждение", message = "Некорректный ввод! Жилая площадь не может быть меньше площади кухни!")

            if self.entry_map.get() == "":
                messagebox.showwarning(title = "Предупреждение", message = "Укажите координаты местоположения квартиры!")
                return
            
            input_so = np.log(float(self.entry_os.get())) #логарифм площади
            input_sk = float(self.entry_sk.get()) #площадь кухни
            input_sj = float(self.entry_sj.get()) #общая площадь
            input_fh = int(self.entry_fh.get()) #этажность дома
            input_yh = now.year - int(self.entry_yh.get()) + 1 #хронологический возраст дома
            input_lon = show_map()[1] #долгота
            input_lat = show_map()[0] #широта
            br = self.change_br(self.optionmenu_br.get()) #тип санузла
            input_br = br #тип санузла
            #input_br
            nr = self.change_nr(self.optionmenu_nr.get()) #количество комнат
            input_nr_1 = nr[0] #1к
            input_nr_2 = nr[1] #2к
            input_nr_3 = nr[2] #3к
            input_nr_4 = nr[3] #4к и более
            input_nr_5 = nr[4] #студия
            lf = self.change_lf(self.optionmenu_lf.get()) #этаж расположения
            input_lf_1 = lf[0] #первый
            input_lf_2 = lf[1] #последний
            input_lf_3 = lf[2] #средний
            wm = self.change_wm(self.optionmenu_wm.get()) #материал стен 
            input_wm_1 = wm[0] #деревянный
            input_wm_2 = wm[1] #кирпичный
            input_wm_3 = wm[2] #монолитный
            input_wm_4 = wm[3] #панельный
            fl = self.change_fl(self.optionmenu_fl.get()) #уровень ремонта
            input_fl_1 = fl[0] #дизайнерский
            input_fl_2 = fl[1] #евроремонт
            input_fl_3 = fl[2] #стандартный
            input_fl_4 = fl[3] #требует ремонта

            try:
                arr = np.array([[input_so, input_sk, input_sj, input_fh, input_yh, input_lon, input_lat, input_br, 
                                input_nr_1, input_nr_2, input_nr_3, input_nr_4, input_nr_5, input_lf_1, input_lf_2, input_lf_3, 
                                input_wm_1, input_wm_2, input_wm_3, input_wm_4, input_fl_1, input_fl_2, input_fl_3, input_fl_4]])
                pred = np.round(np.exp(model.predict(arr)), -3)
                pred_kv = np.round(pred[0]/float(self.entry_os.get()), 2) #float(self.entry_os.get()) - площадь
                pred_kv = '{0:,}'.format(pred_kv).replace(',', ' ') #округление и разрядность
                pred = '{0:,}'.format(pred[0]).replace(',', ' ') #округление и разрядность
                pred_kv = '(' + pred_kv + ')'
                self.cost.configure(text = pred) #выводим стоимость
                self.cost_kv.configure(text = pred_kv) #выводим удельную стоимость, если не строка text=str(pred_kv)
                print(pred)
                print(pred_kv) 
            except:
                self.cost.configure(text = "error") #выводим стоимость
                self.cost_kv.configure(text = "") #выводим удельную стоимость, если не строка text=str(pred_kv)
        

        #Предсказание стоимости
        self.button_predict = Ctk.CTkButton(master = self.frame_map, 
                                            text = "Рассчитать",
                                            corner_radius = 8,
                                            #fg_color = "green",
                                            command = predict)
        #self.button_predict.grid(row = 12, column = 0, padx = (4, 4), pady = (10, 10))
        self.button_predict.place(relx = 0.02, rely = 0.933)
        #button_1.pack(pady=10, padx=10)

        #self.frame_n = Ctk.CTkFrame(master = self) #fg_color = "transparent"
        #self.frame_n.grid(row = 3, column = 1, padx = (5, 10), pady = (10, 10), sticky = "nsew")

        #self.frame_c = Ctk.CTkFrame(master = self)
        #self.frame_c.grid(row = 3, column = 1, padx = (20, 20), pady = (20, 0), sticky = "nsew")
        
        self.appearance_mode_option_menu = Ctk.CTkOptionMenu(self.frame_map, 
                                                             values = ["Dark", "Light", "System"], 
                                                             command = self.change_appearance_mode_event)
        #self.appearance_mode_option_menu.grid(row = 2, column = 0, padx = (4, 4), pady = (10, 10))
        self.appearance_mode_option_menu.place(relx = 0.31, rely = 0.834)
        self.appearance_mode_option_menu.set("System")

        self.colors_menu = Ctk.CTkOptionMenu(self.frame_map, 
                                             values = ["blue", "green"],
                                             command = self.colors)
        #self.colors_menu.grid(row = 2, column = 1, padx = (4, 4), pady = (10, 10))
        self.colors_menu.place(relx = 0.60, rely = 0.834)
        self.colors_menu.set("blue")
        
    def colors(self, col: str):
        #print(col)
        if col == "blue":
            self.slider_fh.configure(button_color = "#3b8ed0")
            self.slider_fh.configure(button_hover_color = "#36719f")
            self.slider_yh.configure(button_color = "#3b8ed0")
            self.slider_yh.configure(button_hover_color = "#36719f")

            self.optionmenu_br.configure(fg_color = "#3b8ed0")
            self.optionmenu_br.configure(button_color = "#36719f")
            self.optionmenu_br.configure(button_hover_color = "#27577d")

            self.optionmenu_nr.configure(fg_color = "#3b8ed0")
            self.optionmenu_nr.configure(button_color = "#36719f")
            self.optionmenu_nr.configure(button_hover_color = "#27577d")

            self.optionmenu_lf.configure(fg_color = "#3b8ed0")
            self.optionmenu_lf.configure(button_color = "#36719f")
            self.optionmenu_lf.configure(button_hover_color = "#27577d")

            self.optionmenu_wm.configure(fg_color = "#3b8ed0")
            self.optionmenu_wm.configure(button_color = "#36719f")
            self.optionmenu_wm.configure(button_hover_color = "#27577d")

            self.optionmenu_fl.configure(fg_color = "#3b8ed0")
            self.optionmenu_fl.configure(button_color = "#36719f")
            self.optionmenu_fl.configure(button_hover_color = "#27577d")

            self.map_option_menu.configure(fg_color = "#3b8ed0")
            self.map_option_menu.configure(button_color = "#36719f")
            self.map_option_menu.configure(button_hover_color = "#27577d")

            self.appearance_mode_option_menu.configure(fg_color = "#3b8ed0")
            self.appearance_mode_option_menu.configure(button_color = "#36719f")
            self.appearance_mode_option_menu.configure(button_hover_color = "#27577d")

            self.colors_menu.configure(fg_color = "#3b8ed0")
            self.colors_menu.configure(button_color = "#36719f")
            self.colors_menu.configure(button_hover_color = "#27577d")

            self.button_map.configure(fg_color = "#3b8ed0")
            self.button_map.configure(hover_color = "#36719f")
            self.button_predict.configure(fg_color = "#3b8ed0")
            self.button_predict.configure(hover_color = "#36719f")
        elif col == "green":
            self.slider_fh.configure(button_color = "#00a100")
            self.slider_fh.configure(button_hover_color = "#008000")
            self.slider_yh.configure(button_color = "#00a100")
            self.slider_yh.configure(button_hover_color = "#008000")

            self.optionmenu_br.configure(fg_color = "#00a100")
            self.optionmenu_br.configure(button_color = "#008000")
            self.optionmenu_br.configure(button_hover_color = "#006c00")

            self.optionmenu_nr.configure(fg_color = "#00a100")
            self.optionmenu_nr.configure(button_color = "#008000")
            self.optionmenu_nr.configure(button_hover_color = "#006c00")

            self.optionmenu_lf.configure(fg_color = "#00a100")
            self.optionmenu_lf.configure(button_color = "#008000")
            self.optionmenu_lf.configure(button_hover_color = "#006c00")

            self.optionmenu_wm.configure(fg_color = "#00a100")
            self.optionmenu_wm.configure(button_color = "#008000")
            self.optionmenu_wm.configure(button_hover_color = "#006c00")

            self.optionmenu_fl.configure(fg_color = "#00a100")
            self.optionmenu_fl.configure(button_color = "#008000")
            self.optionmenu_fl.configure(button_hover_color = "#006c00")

            self.map_option_menu.configure(fg_color = "#00a100")
            self.map_option_menu.configure(button_color = "#008000")
            self.map_option_menu.configure(button_hover_color = "#006c00")

            self.appearance_mode_option_menu.configure(fg_color = "#00a100")
            self.appearance_mode_option_menu.configure(button_color = "#008000")
            self.appearance_mode_option_menu.configure(button_hover_color = "#006c00")

            self.colors_menu.configure(fg_color = "#00a100")
            self.colors_menu.configure(button_color = "#008000")
            self.colors_menu.configure(button_hover_color = "#006c00")
            
            self.button_map.configure(fg_color = "#00a100")
            self.button_map.configure(hover_color = "#008000")
            self.button_predict.configure(fg_color = "#00a100") 
            self.button_predict.configure(hover_color = "#008000") #006c00
        #Ctk.set_default_color_theme(col)

    def change_appearance_mode_event(self, new_appearance_mode):
        #print(new_appearance_mode)
        Ctk.set_appearance_mode(new_appearance_mode)
    
    def slider_callback_fh(self, value):
        self.entry_fh.delete(0, "end")
        self.entry_fh.insert(0, int(value))

    def slider_callback_yh(self, value):
        self.entry_yh.delete(0, "end")
        self.entry_yh.insert(0, int(value))
    
    def change_map(self, new_map: str):
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        #elif new_map == "Google normal":
        #    self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom = 15)
        elif new_map == "Google satellite":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom = 15)
    
    def change_br(self, new_br: str):
        #print(self.optionmenu_br.get())
        if new_br == "совмещенный":
            input_br = 1
        else: 
            input_br = 0
        #print(input_br)
        return input_br
        #pass

    def change_nr(self, new_nr: str):
        if new_nr == "1к":
            input_nr_1 = 1
            input_nr_2 = 0
            input_nr_3 = 0
            input_nr_4 = 0
            input_nr_5 = 0
        elif new_nr == "2к":
            input_nr_1 = 0
            input_nr_2 = 1
            input_nr_3 = 0
            input_nr_4 = 0
            input_nr_5 = 0
        elif new_nr == "3к":
            input_nr_1 = 0
            input_nr_2 = 0
            input_nr_3 = 1
            input_nr_4 = 0
            input_nr_5 = 0
        elif new_nr == "4к и более":
            input_nr_1 = 0
            input_nr_2 = 0
            input_nr_3 = 0
            input_nr_4 = 1
            input_nr_5 = 0
        else:
            input_nr_1 = 0
            input_nr_2 = 0
            input_nr_3 = 0
            input_nr_4 = 0
            input_nr_5 = 1
        return input_nr_1, input_nr_2, input_nr_3, input_nr_4, input_nr_5
        #pass

    def change_lf(self, new_lf: str):
        if new_lf == "первый":
            input_lf_1 = 1
            input_lf_2 = 0
            input_lf_3 = 0
        elif new_lf == "последний":
            input_lf_1 = 0
            input_lf_2 = 1
            input_lf_3 = 0
        else:
            input_lf_1 = 0
            input_lf_2 = 0
            input_lf_3 = 1
        return input_lf_1, input_lf_2, input_lf_3
    
    def change_wm(self, new_wm: str):
        if new_wm == "деревянный":
            input_wm_1 = 1
            input_wm_2 = 0
            input_wm_3 = 0
            input_wm_4 = 0
        elif new_wm == "кирпичный":
            input_wm_1 = 0
            input_wm_2 = 1
            input_wm_3 = 0
            input_wm_4 = 0
        elif new_wm == "монолитный":
            input_wm_1 = 0
            input_wm_2 = 0
            input_wm_3 = 1
            input_wm_4 = 0
        else:
            input_wm_1 = 0
            input_wm_2 = 0
            input_wm_3 = 0
            input_wm_4 = 1
        return input_wm_1, input_wm_2, input_wm_3, input_wm_4
        #pass
    
    def change_fl(self, new_fl: str):
        if new_fl == "дизайнерский":
            input_fl_1 = 1
            input_fl_2 = 0
            input_fl_3 = 0
            input_fl_4 = 0
        elif new_fl == "евроремонт":
            input_fl_1 = 0
            input_fl_2 = 1
            input_fl_3 = 0
            input_fl_4 = 0
        elif new_fl == "стандартный":
            input_fl_1 = 0
            input_fl_2 = 0
            input_fl_3 = 1
            input_fl_4 = 0
        else:
            input_fl_1 = 0
            input_fl_2 = 0
            input_fl_3 = 0
            input_fl_4 = 1
        return input_fl_1, input_fl_2, input_fl_3, input_fl_4
        #pass


if __name__ == "__main__":
    app = App()
    app.mainloop()