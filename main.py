#Импортирование библиотек
import customtkinter #графическая библиотке для визуального отображения
from PIL import Image #графическое отображение (возможность импорта картинки)
from CTkTable import * #таблица customtkinter
from ctypes import * #системная библиотека для считывания системной темы

customtkinter.set_appearance_mode("System")#Установка системной темы по умолчанию
customtkinter.set_default_color_theme("dark-blue")#Установка стандартного цвета виджетам тёмно-синий


class App(customtkinter.CTk): #создание класса приложения (взято из офиц документации)
    def __init__(self): #создание функции инит(нулевая функция-базовая функция которая отвечает за стандартное отображение чего либо)
        super().__init__() #объявление которое делает функцию глобальной, все классы внутри будут дочерними

        self.title("Выбор VR шлема для новичков.py") #оглавление
        x = windll.user32.GetSystemMetrics(0) #получение количества метриков пользователя по x координате (чтобы было на полный экран вне зависимости от формата монитора)
        y = windll.user32.GetSystemMetrics(1) #получение количества метриков пользователя по y координате
        #Размер окна
        self.geometry(f"{x}x{y}") #выставляется по метрикам
        #установка размера приложения в полноэкранный режим
        self.wm_attributes('-f', True) # -F фулскрин, а тру запускает функцию


        self.grid_rowconfigure(0, weight=1) #сетка расположения для нее делается вес для корректного отображения всех элементов по иксу и по игрику
        self.grid_columnconfigure(1, weight=1)
         # загрузка фото для основных кнопок
        self.history_image = customtkinter.CTkImage(light_image=Image.open("home_dark.png"),
                                                    dark_image=Image.open("home_light.png"), size=(20, 20)) #загружает фото в переменную self image
        self.type_image = customtkinter.CTkImage(light_image=Image.open("vopros_light.png"),
                                                 dark_image=Image.open("vopros_dark.png"),
                                                 size=(25, 20)) #загружает фото в переменную type image (окно с выбором типа виар шлема)
        self.sravn_image = customtkinter.CTkImage(light_image=Image.open("sravn_dark.png"),
                                                  dark_image=Image.open("sravn_light.png"),
                                                  size=(30, 30)) #загружает фото в переменную сравнения image (сравнение виар)
        self.exit_image = customtkinter.CTkImage(light_image=Image.open("exit_light.png"),
                                                 dark_image=Image.open("exit_dark.png"),
                                                 size=(70, 20)) #загружает фото в переменную фото для кнопки выхода

        # создание навигационного окна
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0) #окно навигации (без обводки)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew") #расположение с помощью размерной сетки ввиде таблицы и ее выравнивание
        self.navigation_frame.grid_rowconfigure(4, weight=1) #добавляем строки в grid
        # Титульное имя
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Всё о VR",
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold")) #текст навигационного окна, выравнивание и присвоение нужного шрифта
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20) #задаем расположение на окне grid
         # Кнопка с иторией VR
        self.frame_1_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, #отступ от границ кнопки для текста
                                                      text="История и что такое VR",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      image=self.history_image,
                                                      hover_color=("gray70", "gray30"), #обводка для фотки
                                                      anchor="w", command=self.home_button_event) #выравнивание 
        self.frame_1_button.grid(row=1, column=0, sticky="ew") #расположение с помощью размерной сетки ввиде таблицы и ее выравнивание (sticky = выравнивание)
        # Кнопка со вторым окном(Тип VR)
        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Какими бывают VR шлемы?",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      image=self.type_image,
                                                      hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")
        # Кнопка с третьим окном(Сравнение Шлемов)
        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Сравнение топ 3 \nшлема из категории",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      anchor="w", image=self.sravn_image,
                                                      command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew") #расположение с помощью размерной сетки ввиде таблицы и ее выравнивание (sticky = выравнивание)
 # Кнопка выхода
        self.exit = customtkinter.CTkButton(master=self.navigation_frame, text="", command=self.exit_form, #мастер - это где кнопка будет распологаться (в каком окне)
                                            image=self.exit_image, height=30, fg_color="transparent") #будет совпадать с цветом формы
        self.exit.grid(row=5, column=0, padx=20, pady=20, sticky="s") #расположение с помощью размерной сетки ввиде таблицы и ее выравнивание (sticky = выравнивание)\ pad - это отступ

        # кнопка разрешения
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 20)) #расположение с помощью размерной сетки ввиде таблицы и ее выравнивание (sticky = выравнивание)\ pad - это отступ
        # Кнопка смены темы
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["System", "Dark", "Light"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=20, sticky="s") #расположение с помощью размерной сетки ввиде таблицы и ее выравнивание (sticky = выравнивание)\ pad - это отступ
  # создание 1-ого окна
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        # Текст
        self.chto = customtkinter.CTkTextbox(master=self.main_frame, width=1280, height=500)
        self.chto.configure(state='disabled')
        self.chto.grid(row=1, column=0, padx=20, pady=10, columnspan=2)
         # Кнопка истории
        self.button_history = customtkinter.CTkButton(master=self.main_frame, text="Показать Историю Vr",
                                                      command=self.history)
        self.button_history.grid(row=2, column=0, pady=10, ipadx=15)
        # Кнопка Что такое VR шлем
        self.button_what = customtkinter.CTkButton(master=self.main_frame,
                                                   text="Показать Что такое Vr шлем и его история",
                                                   command=self.what)
        self.button_what.grid(row=2, column=1, pady=10, padx=50, ipadx=5)

        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # создание 2-ого окна
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)
        self.n = customtkinter.StringVar(value="")  # Создания переменной
        # Окно для картинок
        self.img_frame = customtkinter.CTkFrame(master=self.second_frame, fg_color="transparent")
        self.img_frame.grid(row=4, column=0, ipady=10, ipadx=10, padx=60, sticky="nsew")
          # Варианты типов шлемов
        self.tip = customtkinter.CTkComboBox(master=self.second_frame, variable=self.n,
                                             values=["Автономный", "Проводной"], command=self.check_tip, width=160,
                                             height=40)
        self.tip.grid(row=1, column=0, pady=15, padx=10, sticky=customtkinter.NE)
        # Многострочный текст для 2-ого окна
        self.txtbox = customtkinter.CTkTextbox(master=self.second_frame, width=1280, height=400)
        self.txtbox.configure(state='disabled')
        self.txtbox.grid(row=2, column=0, padx=10, pady=15, columnspan=3)
        # текстовая метка с объяснением
        self.img_label = customtkinter.CTkLabel(master=self.second_frame, fg_color="transparent",
                                                text="Примеры Vr шлемов выбранной категории:")
        self.img_label.grid(row=3, column=0, ipady=10, ipadx=10)
        # переменные для размера картинок
        self.sizex_2 = 350
        self.sizey_2 = 350
        # картинки для 2-го окна
        self.image1 = customtkinter.CTkImage(Image.open("pico4.png"), size=(self.sizex_2, self.sizey_2))
        self.image2 = customtkinter.CTkImage(Image.open("oculus_quest3.png"), size=(self.sizex_2, self.sizey_2))
        self.image3 = customtkinter.CTkImage(Image.open("pimax_crystal.png"), size=(self.sizex_2, self.sizey_2))
        self.image4 = customtkinter.CTkImage(Image.open("htc_vive_pro.png"), size=(self.sizex_2, self.sizey_2))
        self.image5 = customtkinter.CTkImage(Image.open("playstation-vr2.png"), size=(self.sizex_2, self.sizey_2))
        self.image6 = customtkinter.CTkImage(Image.open("valve_index_vrkit.png"), size=(self.sizex_2, self.sizey_2))
        # Текстовые метки для фоток
        self.img_label1 = customtkinter.CTkLabel(master=self.img_frame, fg_color="transparent", text="")
        self.img_label1.grid(row=4, column=0, ipady=10, padx=25, sticky=customtkinter.NSEW)
        self.img_label2 = customtkinter.CTkLabel(master=self.img_frame, fg_color="transparent", text="")
        self.img_label2.grid(row=4, column=1, ipady=10, padx=25, sticky=customtkinter.NSEW)
        self.img_label3 = customtkinter.CTkLabel(master=self.img_frame, fg_color="transparent", text="")
        self.img_label3.grid(row=4, column=2, ipady=10, padx=25, sticky=customtkinter.NSEW)
         # создание 3-ого окна
        self.third_fr = customtkinter.CTkFrame(master=self, corner_radius=0, fg_color="transparent")
        self.third_fr.grid_columnconfigure(0, weight=1) #занимает все оставшиеся колонки до конца экрана
        #вставка окон для выбора шлема
        self.combo_left1 = customtkinter.CTkFrame(master=self.third_fr, corner_radius=0, fg_color="transparent")
        self.combo_left1.grid(row=2, column=0, ipady=10, ipadx=20, sticky="nsew") #отступ отладка слева
        self.combo_left = customtkinter.CTkFrame(master=self.third_fr, corner_radius=0, fg_color="transparent")
        self.combo_left.grid(row=2, column=1, ipady=10, ipadx=20, sticky="nsew") #создаёт выпадающий список
        self.combo_right = customtkinter.CTkFrame(master=self.third_fr, corner_radius=0, fg_color="transparent")
        self.combo_right.grid(row=2, column=2, ipady=10, ipadx=10, sticky="nsew") #создаёт выпадающий список
        self.combo_right1 = customtkinter.CTkFrame(master=self.third_fr, corner_radius=0, fg_color="transparent")
        self.combo_right1.grid(row=2, column=3, ipady=10, ipadx=10, sticky="nsew") #отступ отладка справа
        self.combo_right2 = customtkinter.CTkFrame(master=self.third_fr, corner_radius=0, fg_color="transparent")
        self.combo_right2.grid(row=2, column=4, ipady=10, ipadx=10, sticky="nsew") #отступ отладка справа
        self.tabview = customtkinter.CTkTabview(self, width=250) #таблица сравнения

        # переменные для 3-ого окна
        self.a = customtkinter.StringVar(value="") #переменная которая ничего в себе не хранит, но может быть изменена
        self.b = customtkinter.StringVar(value="") #переменная которая ничего в себе не хранит, но может быть изменена (выбранный шлем)
        self.name = customtkinter.StringVar(value=" ") #хранит в себе изменённый вид self a
        self.name1 = customtkinter.StringVar(value=" ") #хранит в себе изменённый вид self b

        # размер фоток
        self.sizex_3 = 250 #создание переменной которая хранит в себе размер фотки по иксу
        self.sizey_3 = 250
          # фотки шлемов
        self.photo1 = customtkinter.CTkImage(Image.open("pico4.png"), size=(self.sizex_3, self.sizey_3)) #загрузка фотографий
        self.photo2 = customtkinter.CTkImage(Image.open("oculus_quest3.png"), size=(self.sizex_3, self.sizey_3))  #загрузка фотографий
        self.photo3 = customtkinter.CTkImage(Image.open("pimax_crystal.png"), size=(self.sizex_3, self.sizey_3))  #загрузка фотографий
        self.photo4 = customtkinter.CTkImage(Image.open("htc_vive_pro.png"), size=(self.sizex_3, self.sizey_3))  #загрузка фотографий
        self.photo5 = customtkinter.CTkImage(Image.open("playstation-vr2.png"), size=(self.sizex_3, self.sizey_3))  #загрузка фотографий
        self.photo6 = customtkinter.CTkImage(Image.open("valve_index_vrkit.png"), size=(self.sizex_3, self.sizey_3)) #загрузка фотографий
        #Метка пояснения
        self.label_title = customtkinter.CTkLabel(master=self.third_fr,
                                                  text="Выберите один из представленных шлемов для сравнения")
        self.label_title.grid(row=0, column=0, ipady=10, ipadx=10, columnspan=4) #сколько столбцов будет занимать
        #Переменная для значения списка со шлемами
        self.vals = ["Pico 4", "Oculus Quest3",
                     "Pimax crystal", "HTC Vive Pro",
                     "Playstation VR 2", "Valve Index VRkit"] #задаём список шлемов
        # Созднания левого и правого выбора(выпадающего списка)
        self.combo_first_vibor = customtkinter.CTkComboBox(master=self.combo_left, variable=self.a, #переменная которая хранит в себе значение списка
                                                           values=self.vals,
                                                           command=self.vibor_combo)
        self.combo_first_vibor.grid(row=1, column=0, ipadx=5, pady=5, padx=40)  #расположение с помощью размерной сетки ввиде таблицы и ее выравнивание (sticky = выравнивание)\ pad - это отступ
        self.combo_second_vibor = customtkinter.CTkComboBox(master=self.combo_right, variable=self.b, #переменная которая хранит в себе значение списка
                                                            values=self.vals,
                                                            command=self.vibor_combo, state="disabled") #выключена до выбора первого шлема
        self.combo_second_vibor.grid(row=1, column=1, ipadx=5, pady=5, padx=40, sticky="ne")  #расположение с помощью размерной сетки ввиде таблицы и ее выравнивание (sticky = выравнивание)\ pad - это отступ
        #создание меток для выбранного шлема
        self.photo_left_vibor = customtkinter.CTkLabel(master=self.combo_left, text="") #левая фотка
        self.photo_left_vibor.grid(row=2, column=0, ipady=10, ipadx=10, padx=10, sticky="nsew")  #расположение с помощью размерной сетки ввиде таблицы и ее выравнивание (sticky = выравнивание)\ pad - это отступ
        self.photo_right_vibor = customtkinter.CTkLabel(master=self.combo_right, text="") #правая фотка
        self.photo_right_vibor.grid(row=2, column=1, ipady=10, ipadx=10, sticky="nsew")  #расположение с помощью размерной сетки ввиде таблицы и ее выравнивание (sticky = выравнивание)\ pad - это отступ
        #Текстовая метка с пояснением
        self.pos = customtkinter.CTkLabel(master=self.third_fr, text="Сравнение идёт с 1 и 2 шлемом") #текст пояснения
        self.pos.grid(row=3, column=0, columnspan=4)  #расположение с помощью размерной сетки ввиде таблицы и ее выравнивание (sticky = выравнивание)\ pad - это отступ
        #Стоковые значения таблицы (стандартное)
        self.value = [["Характеристика", "Шлем 1", "Шлем 2", "Лучше/Хуже/Равны"],
                      ["Имя выбранного шлема", " ", " ", " "],
                      ["Тип подключения", " ", " ", " "],
                      ["Разрешение (в px)", " ", " ", " "],
                      ["Поле зрения", " ", " ", " "],
                      ["Размер батареи ", " ", " ", " "],
                      ["Вес (в граммах)", " ", " ", " "],
                      ["Частота обновления экрана (в гц)", " ", " ", " "],
                      ["Оперативная память (в ГБ)", " ", " ", " "],
                      ["Цена (в руб)", " ", " ", " "]]
        #Создание таблицы сравнения
        self.table = CTkTable(master=self.third_fr, row=10, column=4, values=self.value) #создание таблицы
        self.table.grid(row=4, column=0, padx=20, pady=20, ipadx=10, columnspan=4, ipady=10)  #расположение с помощью размерной сетки ввиде таблицы и ее выравнивание (sticky = выравнивание)\ pad - это отступ

        # выбор стандартного окна
        self.select_frame_by_name("main_frame")
        
    def select_frame_by_name(self, name_frame):  # функция выбора окна для отрисовки
        # смена цвета при наведении на кнопку выбора окна
        self.frame_1_button.configure(fg_color=("gray75", "gray25") if name_frame == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name_frame == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name_frame == "frame_3" else "transparent")

        # отрисовка выбранного окна
        if name_frame == "main_frame":
            self.main_frame.grid(row=0, column=1, sticky="nsew")
        else:  # если не подходит по условию
            self.main_frame.grid_forget()  # забываем
        if name_frame == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name_frame == "frame_3":
            self.third_fr.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_fr.grid_forget()

    def home_button_event(self):  # функция выбора 1-ого окна
        self.select_frame_by_name("main_frame")

    def frame_2_button_event(self):  # функция выбора 2-ого окна
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):  # функция выбора 3-ого окна
        self.select_frame_by_name("frame_3")



#вызов класса и запуск прилоения
if __name__ == "__main__": #если имя соответсвует мейну
    app = App() #функция отображения приложения
    app.mainloop() #запуск отображения