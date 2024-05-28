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
    def exit_form(self):#функция выхода
        self.destroy()

    def change_scaling_event(self, new_scaling: str):#функция выбора разрешения приложения (масштаб)
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float) #для изменения размера всех виджетов

    def change_appearance_mode_event(self, new_appearance_mode):  # функция смены цвета темы для приложения
        customtkinter.set_appearance_mode(new_appearance_mode)

    def what(self):  # функция вставки выбора "Что такое VR"
        self.chto.configure(state='normal')
        self.chto.delete('1.0', 'end')
        self.chto.insert(0.0,
                         "VR шлем (Virtual Reality helmet) - это устройство, которое создает среду виртуальной реальности для пользователя."
                         " У него есть экран и линзы, которые обеспечивают трехмерное изображение, а также\nдатчики, которые отслеживают движения "
                         "головы пользователя и позволяют ему взаимодействовать с виртуальным миром. Шлем может быть подключен к компьютеру или "
                         "игровой консоли,\nа может быть автономным устройством с собственной вычислительной мощностью и хранилищем контента."
                         "Главное преимущество VR-шлема заключается в том, что он позволяет пользователю пол-\nностью погрузиться в виртуальную среду,"
                         " которую можно использовать для различных целей."
                         "\n\nИсторию VR-гарнитур можно проследить до первых экспериментов в виртуальной реальности, проведенных учеными и изобретателями"
                         " в 19 веке. Один из первых известных прототипов гарнитуры вир-туальной реальности был создан Чарльзом Уитстоуном в 1837 году."
                         " Он назывался 'стереоскоп' и позволял пользователям просматривать два изображения под немного разными углами, создавая ил-\nлюзию"
                         " глубины. Эта технология заложила основу для современных гарнитур виртуальной реальности."
                         "\n\nВ 20 веке исследователи продолжали экспериментировать с виртуальной реальностью, разрабатывая новые технологии, которые"
                         " могли бы имитировать реалистичную окружающую среду. В 1957 году Мортон Хейлиг создал первый симулятор виртуальной реальности,"
                         " который он назвал 'Сенсорама'. Он был разработан для того, чтобы обеспечить пользователям эффект погружения с помощью неско-\nльких"
                         " проекторов, громкоговорителей и даже нюхательных машин. Однако из-за сложности и дороговизны технологии Sensorama никогда не имела коммерческого успеха."
                         "\n\nПервым практическим применением виртуальной реальности стал шлем виртуальной реальности созданный Бобом Смитом в 1968 году. В нем использовался"
                         " графический процессор 3D для отображения реалистичного ландшафта. Несмотря на то, что шлем виртуальной реальности не обеспечивает полного погружения,"
                         " как современные гарнитуры виртуальной реальности, он продемонстрировал \nпотенциал виртуальной реальности."
                         "\n\nСледующий значительный прорыв в технологии виртуальной реальности произошел в конце 1970-х годов с изобретением первого полноцветного дисплея прямого"
                         " обзора, устанавливаемого на голову \n(HMD) компанией R&D Lab, Inc. Однако гарнитура была громоздкой и дорогой, и ей не удалось получить широкого распространения."
                         "\n\nВ 1980-х годах было разработано несколько иммерсивных систем виртуальной реальности, включая первое портативное устройство виртуальной реальности"
                         " - язык виртуального программирования \nVPL-1. Созданный Чарльзом Розенбергом, VPL-1 позволял пользователям работать в базовой виртуальной среде с"
                         " помощью одного сенсорного экрана. Хотя VPL-1 и не является полноценным HMD, он\nпроложил путь для будущих портативных устройств виртуальной реальности."
                         "\n\n1990-е годы принесли первую массовую гарнитуру виртуальной реальности с появлением гарнитуры VR-1 от Jaron Lanier. Однако это был неуклюжий костюм"
                         " на все тело, а не легкий HMD"
                         "\n\nВ 21 веке разработка более совершенных HMD привела к созданию современных гарнитур виртуальной реальности. В 2006 году Nvidia представила гарнитуру"
                         " Eye-T, которая была разработана для ис-\nпользования с ПК и могла отображать до 20 000 изображений в секунду. Oculus Rift, ставший коммерчески успешным,"
                         " был представлен в 2012 году."
                         "\n\nВ 2016 году индустрия виртуальной реальности сделала важный шаг вперед, выпустив HTC Vive, первый коммерческий HMD, предназначенный для использования"
                         " с широким спектром приложений, \nвключая игры и обучение в виртуальной реальности. В том же году PlayStation VR, HMD, разработанная Sony, была выпущена"
                         " в качестве сопутствующего устройства для PlayStation 4."
                         "\n\nС тех пор индустрия виртуальной реальности продолжала расти и развиваться, благодаря внедрению более иммерсивных HMD-устройств и растущему числу"
                         " приложений в различных секторах")
        self.chto.configure(state='disabled')

    def history(self):  # функция вставки выбора "История VR"
        self.chto.configure(state='normal')
        self.chto.delete('1.0', 'end')
        self.chto.insert(0.0, "Историю виртуальной реальности (VR) можно проследить до 19 века, с изобретением стереоскопов, которые позволили людям"
                              "просматривать трехмерные изображения. Однако концепция погружения в виртуальный мир была популяризирована в научно-фантастической"
                              "литературе, такой как Стэнли Дж. Рассказ Вайнбаума 1935 года 'Очки Пигмалиона', в котором описывается устройство, позволяющее\n"
                              "пользователям входить в виртуальный мир и взаимодействовать с его обитателями."
                              "\n\nВ 1960-х годах ученый-компьютерщик Айвен Сазерленд разработал первую гарнитуру виртуальной реальности под названием 'Sword of Damocles', "
                              "которая состояла из шлема со стереодисплеем и \nдатчиками, отслеживающими движения головы пользователя. Эта технология заложила фундамент"
                              "для современной индустрии виртуальной реальности."
                              "\n\nВ 1980-х годах появились более совершенные гарнитуры виртуальной реальности, такие как Virtual Glove и Interphase 550. Эти системы"
                              "позволяли пользователям контролировать среду, в которую они были погружены, открывая новые возможности для интерактивного виртуального опыта."
                              "\n\n1990-е годы привел к выпуску Virtual Boy, первой портативной системы виртуальной реальности, которая отличалась цветным дисплеем с высоким"
                              "разрешением и датчиками движения. Эта технология, наряду с развитием онлайн-игр, проложила путь к массовому внедрению технологии виртуальной реальности на рынке."
                              "\n\nВ 21 веке появились различные платформы виртуальной реальности, такие как Oculus Rift, HTC Vive и PlayStation VR. "
                              "Эти системы сделали технологию виртуальной реальности более доступной для\nширокой публики, что привело к появлению огромного "
                              "количества нового контента и приложений, включая иммерсивные игры, образовательные симуляторы и художественные инсталляции виртуаль-ной реальности."
                              "\n\nХотя концепция виртуальной реальности существует уже несколько десятилетий, только с появлением мощных и недорогих компьютеров и гарнитур "
                              "эта технология стала мейнстримом. Сегодня\nвиртуальная реальность продолжает быстро развиваться благодаря достижениям в области аппаратного"
                              "обеспечения, программного обеспечения и создания контента. Будущее виртуальной реальности\nвыглядит еще более ярким, с потенциалом для еще "
                              "более захватывающего и интерактивного опыта, а также новые приложения в таких областях, как здравоохранение, развлечения и коммуникация.")
        self.chto.configure(state='disabled')

    def check_tip(self, event):#функция функция бывора типа шлема
        self.txtbox.configure(state='normal')
        self.an = self.n.get()
        if self.an == "Автономный":
            self.img_label1.configure(image=self.image1)
            self.img_label2.configure(image=self.image2)
            self.img_label3.configure(image=self.image3)
            self.txtbox.delete('1.0', 'end')
            self.txtbox.insert(0.0, "Автономные VR шлемы - это устройства, которые не требуют подключения к компьютеру или консоли для работы. Они имеют свои преимущества и недостатки."
                                            "\n\nПреимущества автономных VR шлемов:"
                                            "\n1. Меньшие цены: Автономные VR шлемы обычно дешевле, чем их стационарные аналоги, поскольку они не требуют покупки отдельного компьютера или консоли."
                                            "\n2. Бесшовность: Благодаря отсутствию кабелей, autoномные VR шлемы обеспечивают более плавный и бесшовный опыт использования, чем другие виды VR."
                                            "\n3. Компактность: Они имеют небольшие размеры и могут быть легко перенесены, что делает их идеальными для путешествий или простого использования в другом месте."
                                            "\n4. Виртуальные вещи: Автономные VR шлемы могут создавать виртуальные объекты и предметы, что позволяет пользователям манипулировать ими, как будто они находятся в реальном мире."
                                            "\n\nМинусы автономных VR шлемов:"
                                            "\n1. Ограниченное количество игр: Игры для автономных VR шлемов все еще развиваются, и на данный момент доступно не так много игр, как для станционных компьютеров или консолей."
                                            "\n2. Проблемы с разрешением: В некоторых случаях автономные VR шлемы могут испытывать проблемы с разрешением, что может снизить качество отображения."
                                            "\n3. Быстроe устаревание: Автономные VR шлемы быстро устаревают, поскольку их аппаратное обеспечение обновляется ежегодно или даже"
                                            " ежеквартально. Это может потребовать постоянного обновления оборудования, чтобы поддерживать лучшее качество работы."
                                            "\n4. Стоимость поддержания: Хотя автономные VR шлемы имеют меньшие начальные затраты, их поддержание может быть дорогим, особенно в плане затрат на аппаратное обеспечение и аккумуляторы."
                                            "\n\nВ целом, автономные VR шлемы предлагают привлекательный и бесшовный опыт, который идеально подходит для просмотра видео,"
                                            " обучения или развлечения. Однако они все еще имеют определенные ограничения, такие как ограниченное количество доступных игр и устаревание быстро.")

        elif self.an == "Проводной":
            self.img_label1.configure(image=self.image4)
            self.img_label2.configure(image=self.image5)
            self.img_label3.configure(image=self.image6)
            self.txtbox.delete('1.0', 'end')
            self.txtbox.insert(0.0,
                               "Стационарные или проводные VR-шлемы обладают рядом преимуществ и недостатков по сравнению с мобильными VR-гарнитурами:"
                                    "\n\nПреимущества:"
                                    "\n1. Более высокая производительность: Статические гарнитуры виртуальной реальности подключаются к мощному компьютеру или"
                                    " игровой консоли, что обеспечивает более высокий уровень произво-\nдительности и лучшее качество графики по сравнению с мобильными устройствами."
                                    "\n2. Улучшенное отслеживание: Статические гарнитуры виртуальной реальности, как правило, имеют более совершенные системы отслеживания,"
                                    " которые обеспечивают более точные перемещения и \nдействия в виртуальной реальности. Это особенно важно для игр и приложений, требующих точного"
                                    " отслеживания движений рук или всего тела."
                                    "\n3. Эффект погружения: Статические гарнитуры виртуальной реальности обеспечивают более глубокое погружение благодаря своей способности"
                                    " полностью блокировать внешний мир и окружать пользователя виртуальной средой с высоким разрешением."
                                    "\n4. Более длительное время воспроизведения: Поскольку статические гарнитуры виртуальной реальности подключены к источнику питания,"
                                    " у них нет таких ограничений по времени автономной работы, как у мобильных устройств. Это позволяет продлить время воспроизведения без"
                                    " необходимости подзарядки."
                                    "\n\nНедостатки:"
                                    "\n1. Стоимость: Статические гарнитуры виртуальной реальности, как правило, стоят дороже мобильных устройств, в первую очередь из-за"
                                    " того, что для их работы требуется более мощный компьютер или игровая консоль."
                                    "\n2. Большая область настройки: Настройка статической гарнитуры виртуальной реальности может быть трудоемким процессом, поскольку"
                                    " для этого требуется значительное пространство для гарнитуры, компьютера и необходимых кабелей. Это может быть особенно сложной задачей"
                                    " в небольших жилых помещениях или в строго ограниченных пространствах."
                                    "\n3. Привязан к определенному компьютеру: В отличие от мобильных гарнитур виртуальной реальности, статические гарнитуры виртуальной"
                                    " реальности тесно привязаны к определенному компьютеру или игровой консоли. Это означает, что если компьютер пользователя выйдет из строя"
                                    " или возникнут проблемы с производительностью, это может негативно сказаться на работе виртуальной реальности."
                                    "\n4. Менее портативные: Как уже упоминалось, статические гарнитуры виртуальной реальности требуют источника питания и значительного"
                                    " времени на настройку, что делает их менее портативными по сравнению с мобильными устройствами."
                                    "\n\nВ заключение, хотя статические гарнитуры виртуальной реальности обладают рядом преимуществ, таких как высокая производительность,"
                                    " расширенное отслеживание и опыт погружения, у них также есть ряд недостатков, включая стоимость, трудности настройки и недостаточную мобильность."
                                    " Эти факторы следует тщательно учитывать при определении наилучшего типа гарнитуры виртуальной реальности для конкретного приложения или пользователя.")
        self.txtbox.configure(state='disabled')
    def combo(self): #функция измениения списка(удаление из второго списка выбранный вариант в первом и наоборот)
        self.k = 0
        self.name = self.a.get()
        self.name1 = self.b.get()
        if self.name != " " and self.name1 != " ":
            self.combo_second_vibor.configure(state="normal")
            if self.name in self.vals:
                self.vals = ["Pico 4", "Oculus Quest3",
                             "Pimax crystal", "HTC Vive Pro",
                             "Playstation VR 2", "Valve Index VRkit"]
                self.k = (self.vals.index(self.name))
                self.vals.remove(self.vals[self.k])
                self.combo_second_vibor.configure(values=self.vals)
            elif self.name1 in self.vals:
                self.vals = ["Pico 4", "Oculus Quest3",
                             "Pimax crystal", "HTC Vive Pro",
                             "Playstation VR 2", "Valve Index VRkit"]
                self.k = (self.vals.index(self.name1))
                self.vals.remove(self.vals[self.k])
                self.combo_first_vibor.configure(values=self.vals)


    def vibor_combo(self, event): #функция заполнения таблицы при выбере 2 шлемов
        self.name = self.a.get() #переменная name получает знаечение переменной а
        self.name1 = self.b.get() #переменная name1 получает знаечение переменной b


        #--------------------------------------------------------------------------------------------------------------
        # значения которые будут проставляться в таблицу
        self.ozu = "Минимальные требования к компьютеру - 8Гб ОЗУ"
        no_battery = "подключается к источнику питания"
        col1 = 1
        col2 = 2
        connect_wire = "Проводной"
        connect_nonwire = "Без проводной"
        # --------------------------------------------------------------------------------------------------------------
        # если шлем выбран в левом выборе
        if self.name == "Pico 4":
            self.combo() #вызывает функцию комбо
            self.table.insert(1, col1, "Pico 4")
            self.table.insert(2, col1, connect_nonwire)
            self.table.insert(3, col1, "4320 x 2160")
            self.table.insert(4, col1, "105°")
            self.table.insert(5, col1, "5300 mAh")
            self.table.insert(6, col1, "586")
            self.table.insert(7, col1, "90")
            self.table.insert(8, col1, 8)
            self.table.insert(9, col1, "54 000")
            self.photo_left_vibor.configure(image=self.photo1) #подгон нужной фотки
        elif self.name == "Oculus Quest3":
            self.combo()
            self.table.insert(1, col1, "Oculus Quest3")
            self.table.insert(2, col1, connect_nonwire)
            self.table.insert(3, col1, "4416 x 2064")
            self.table.insert(4, col1, "110°")
            self.table.insert(5, col1, "5300 mAh")
            self.table.insert(6, col1, "503")
            self.table.insert(7, col1, "90")
            self.table.insert(8, col1, 8)
            self.table.insert(9, col1, "70 000")
            self.photo_left_vibor.configure(image=self.photo2)
        elif self.name == "Pimax crystal":
            self.combo()
            self.table.insert(1, col1, "Pimax crystal")
            self.table.insert(2, col1, connect_nonwire)
            self.table.insert(3, col1, "5760 x 2880")
            self.table.insert(4, col1, "120°")
            self.table.insert(5, col1, "6000 mAh")
            self.table.insert(6, col1, "840")
            self.table.insert(7, col1, "150")
            self.table.insert(8, col1, 8)
            self.table.insert(9, col1, "от 143 000")
            self.photo_left_vibor.configure(image=self.photo3)
        elif self.name == "HTC Vive Pro":
            self.combo()
            self.table.insert(1, col1, "HTC Vive Pro")
            self.table.insert(2, col1, connect_wire)
            self.table.insert(3, col1, "2880 x 1600")
            self.table.insert(4, col1, "110°")
            self.table.insert(5, col1, no_battery)
            self.table.insert(6, col1, "520")
            self.table.insert(7, col1, "90")
            self.table.insert(8, col1, self.ozu)
            self.table.insert(9, col1, "107 000")
            self.photo_left_vibor.configure(image=self.photo4)
        elif self.name == "Playstation VR 2":
            self.combo()
            self.table.insert(1, col1, "Playstation VR 2")
            self.table.insert(2, col1, connect_wire)
            self.table.insert(3, col1, "4000 x 2040")
            self.table.insert(4, col1, "110°")
            self.table.insert(5, col1, no_battery)
            self.table.insert(6, col1, "600")
            self.table.insert(7, col1, "120")
            self.table.insert(8, col1, "Подключается только к playstation 5")
            self.table.insert(9, col1, "75 000")
            self.photo_left_vibor.configure(image=self.photo5)
        elif self.name == "Valve Index VRkit":
            self.combo()
            self.table.insert(2, col1, connect_wire)
            self.table.insert(1, col1, "Valve Index VRkit")
            self.table.insert(3, col1, "2880 x 1600")
            self.table.insert(4, col1, "130°")
            self.table.insert(5, col1, no_battery)
            self.table.insert(6, col1, "810")
            self.table.insert(7, col1, "144")
            self.table.insert(8, col1, self.ozu)
            self.table.insert(9, col1, "180 000")
            self.photo_left_vibor.configure(image=self.photo6)
        else:
            pass #ничего не делать при отсутствии выбора 1 шлема
        # если шлем выбран в правом выборе
        if self.name1 == "Pico 4":
            self.combo()
            self.table.insert(1, col2, "Pico 4")
            self.table.insert(2, col2, connect_nonwire)
            self.table.insert(3, col2, "4320 x 2160")
            self.table.insert(4, col2, "105°")
            self.table.insert(5, col2, "5300 mAh")
            self.table.insert(6, col2, "586")
            self.table.insert(7, col2, "90")
            self.table.insert(8, col2, "90")
            self.table.insert(8, col2, 8)
            self.table.insert(9, col2, "54 000")
            self.photo_right_vibor.configure(image=self.photo1)
        elif self.name1 == "Oculus Quest3":
            self.combo()
            self.table.insert(1, col2, "Oculus Quest3")
            self.table.insert(2, col2, connect_nonwire)
            self.table.insert(3, col2, "4416 x 2064")
            self.table.insert(4, col2, "110°")
            self.table.insert(5, col2, "5300 mAh")
            self.table.insert(6, col2, "503")
            self.table.insert(7, col2, "90")
            self.table.insert(8, col2, 8)
            self.table.insert(9, col2, "70 000")
            self.photo_right_vibor.configure(image=self.photo2)
        elif self.name1 == "Pimax crystal":
            self.combo()
            self.table.insert(1, col2, "Pimax crystal")
            self.table.insert(2, col2, connect_nonwire)
            self.table.insert(3, col2, "5760 x 2880")
            self.table.insert(4, col2, "120°")
            self.table.insert(5, col2, "6000 mAh")
            self.table.insert(6, col2, "840")
            self.table.insert(7, col2, "150")
            self.table.insert(8, col2, 8)
            self.table.insert(9, col2, "от 143 000")
            self.photo_right_vibor.configure(image=self.photo3)
        elif self.name1 == "HTC Vive Pro":
            self.combo()
            self.table.insert(1, col2, "HTC Vive Pro")
            self.table.insert(2, col2, connect_wire)
            self.table.insert(3, col2, "2880 x 1600")
            self.table.insert(4, col2, "110°")
            self.table.insert(5, col2, no_battery)
            self.table.insert(6, col2, "520")
            self.table.insert(7, col2, "90")
            self.table.insert(8, col2, self.ozu)
            self.table.insert(9, col2, "от 107 000")
            self.photo_right_vibor.configure(image=self.photo4)
        elif self.name1 == "Playstation VR 2":
            self.combo()
            self.table.insert(1, col2, "Playstation VR 2")
            self.table.insert(2, col2, connect_wire)
            self.table.insert(3, col2, "4000 x 2040")
            self.table.insert(4, col2, "110°")
            self.table.insert(5, col2, no_battery)
            self.table.insert(6, col2, "600")
            self.table.insert(7, col2, "120")
            self.table.insert(8, col2, "Подключается только к playstation 5")
            self.table.insert(9, col2, "75 000")
            self.photo_right_vibor.configure(image=self.photo5)
        elif self.name1 == "Valve Index VRkit":
            self.combo()
            self.table.insert(1, col2, "Valve Index VRkit")
            self.table.insert(2, col2, connect_wire)
            self.table.insert(3, col2, "2880 x 1600")
            self.table.insert(4, col2, "130°")
            self.table.insert(5, col2, no_battery)
            self.table.insert(6, col2, "810")
            self.table.insert(7, col2, "144")
            self.table.insert(8, col2, self.ozu)
            self.table.insert(9, col2, "180 000")
            self.photo_right_vibor.configure(image=self.photo6)
        else:
            pass #ничего не делать при отсутствии выборе второго шлема
        if self.name != "" and self.name1 != "": # вызов функций сравнения шлема
            self.sravn_pico()
            self.sravn_oculus()
            self.sravn_pimax()
            self.sravn_htc()
            self.sravn_playstation()
            self.sravn_valve()


    def sravn_pico(self):# функция сравнения для шлема Pico 4
        luchshe="Лучше"
        huje="Хуже"
        ravni="Равны"
        OtPC="Зависит от компьютера"
        if self.name == "Pico 4" and self.name1 == "Oculus Quest3":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, luchshe)
            self.table.insert(4, 3, huje)
            self.table.insert(5, 3, ravni)
            self.table.insert(6, 3, ravni)
            self.table.insert(7, 3, ravni)
            self.table.insert(8, 3, ravni)
            self.table.insert(9, 3, luchshe)
        elif self.name == "Pico 4" and self.name1 == "Pimax crystal":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, huje)
            self.table.insert(4, 3, huje)
            self.table.insert(5, 3, huje)
            self.table.insert(6, 3, luchshe)
            self.table.insert(7, 3, huje)
            self.table.insert(8, 3, ravni)
            self.table.insert(9, 3, luchshe)
        elif self.name == "Pico 4" and self.name1 == "HTC Vive Pro":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, luchshe)
            self.table.insert(4, 3, huje)
            self.table.insert(5, 3, luchshe)
            self.table.insert(6, 3, huje)
            self.table.insert(7, 3, ravni)
            self.table.insert(8, 3, OtPC)
            self.table.insert(9, 3, luchshe)
        elif self.name == "Pico 4" and self.name1 == "Playstation VR 2":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, luchshe)
            self.table.insert(4, 3, huje)
            self.table.insert(5, 3, luchshe)
            self.table.insert(6, 3, luchshe)
            self.table.insert(7, 3, huje)
            self.table.insert(8, 3, OtPC)
            self.table.insert(9, 3, luchshe)
        elif self.name == "Pico 4" and self.name1 == "Valve Index VRkit":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, luchshe)
            self.table.insert(4, 3, huje)
            self.table.insert(5, 3, luchshe)
            self.table.insert(6, 3, luchshe)
            self.table.insert(7, 3, huje)
            self.table.insert(8, 3, OtPC)
            self.table.insert(9, 3, luchshe)
    
    def sravn_oculus(self):# функция сравнения для шлема Pico 4
        luchshe="Лучше"
        huje="Хуже"
        ravni="Равны"
        OtPC="Зависит от компьютера"
        if self.name == "Oculus Quest3" and self.name1 == "Pico 4":
            self.table.insert(1, 3, "-")
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, huje)
            self.table.insert(4, 3, luchshe)
            self.table.insert(5, 3, ravni)
            self.table.insert(6, 3, ravni)
            self.table.insert(7, 3, ravni)
            self.table.insert(8, 3, ravni)
            self.table.insert(9, 3, huje)
        elif self.name == "Oculus Quest3" and self.name1 == "Pimax crystal":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, huje)
            self.table.insert(4, 3, huje)
            self.table.insert(5, 3, huje)
            self.table.insert(6, 3, luchshe)
            self.table.insert(7, 3, huje)
            self.table.insert(8, 3, ravni)
            self.table.insert(9, 3, luchshe)
        elif self.name == "Oculus Quest3" and self.name1 == "HTC Vive Pro":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, luchshe)
            self.table.insert(4, 3, ravni)
            self.table.insert(5, 3, luchshe)
            self.table.insert(6, 3, luchshe)
            self.table.insert(7, 3, ravni)
            self.table.insert(8, 3, OtPC)
            self.table.insert(9, 3, luchshe)
        elif self.name == "Oculus Quest3" and self.name1 == "Playstation VR 2":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, luchshe)
            self.table.insert(4, 3, ravni)
            self.table.insert(5, 3, luchshe)
            self.table.insert(6, 3, luchshe)
            self.table.insert(7, 3, huje)
            self.table.insert(8, 3, OtPC)
            self.table.insert(9, 3, luchshe)
        elif self.name == "Oculus Quest3" and self.name1 == "Valve Index VRkit":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, luchshe)
            self.table.insert(4, 3, huje)
            self.table.insert(5, 3, luchshe)
            self.table.insert(6, 3, luchshe)
            self.table.insert(7, 3, huje)
            self.table.insert(8, 3, OtPC)
            self.table.insert(9, 3, luchshe)

    def sravn_pimax(self):# функция сравнения для шлема Pico 4
        luchshe="Лучше"
        huje="Хуже"
        ravni="Равны"
        OtPC="Зависит от компьютера"
        if self.name == "Pimax crystal" and self.name1 == "Pico 4":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, luchshe)
            self.table.insert(4, 3, luchshe)
            self.table.insert(5, 3, luchshe)
            self.table.insert(6, 3, huje)
            self.table.insert(7, 3, luchshe)
            self.table.insert(8, 3, ravni)
            self.table.insert(9, 3, huje)
        elif self.name == "Pimax crystal" and self.name1 == "Oculus Quest3":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, luchshe)
            self.table.insert(4, 3, luchshe)
            self.table.insert(5, 3, luchshe)
            self.table.insert(6, 3, huje)
            self.table.insert(7, 3, luchshe)
            self.table.insert(8, 3, ravni)
            self.table.insert(9, 3, huje)
        elif self.name == "Pimax crystal" and self.name1 == "HTC Vive Pro":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, luchshe)
            self.table.insert(4, 3, luchshe)
            self.table.insert(5, 3, luchshe)
            self.table.insert(6, 3, huje)
            self.table.insert(7, 3, luchshe)
            self.table.insert(8, 3, OtPC)
            self.table.insert(9, 3, huje)
        elif self.name == "Pimax crystal" and self.name1 == "Playstation VR 2":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, luchshe)
            self.table.insert(4, 3, luchshe)
            self.table.insert(5, 3, luchshe)
            self.table.insert(6, 3, huje)
            self.table.insert(7, 3, luchshe)
            self.table.insert(8, 3, OtPC)
            self.table.insert(9, 3, huje)
        elif self.name == "Pimax crystal" and self.name1 == "Valve Index VRkit":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, luchshe)
            self.table.insert(4, 3, huje)
            self.table.insert(5, 3, luchshe)
            self.table.insert(6, 3, huje)
            self.table.insert(7, 3, luchshe)
            self.table.insert(8, 3, OtPC)
            self.table.insert(9, 3, luchshe)

    def sravn_htc(self):# функция сравнения для шлема Pico 4
        luchshe = "Лучше"
        huje = "Хуже"
        ravni = "Равны"
        OtPC = "Зависит от компьютера"
        if self.name == "HTC Vive Pro" and self.name1 == "Pico 4":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, huje)
            self.table.insert(4, 3, luchshe)
            self.table.insert(5, 3, huje)
            self.table.insert(6, 3, luchshe)
            self.table.insert(7, 3, ravni)
            self.table.insert(8, 3, OtPC)
            self.table.insert(9, 3, huje)
        elif self.name == "HTC Vive Pro" and self.name1 == "Oculus Quest3":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, huje)
            self.table.insert(4, 3, ravni)
            self.table.insert(5, 3, huje)
            self.table.insert(6, 3, huje)
            self.table.insert(7, 3, ravni)
            self.table.insert(8, 3, OtPC)
            self.table.insert(9, 3, huje)
        elif self.name == "HTC Vive Pro" and self.name1 == "Pimax crystal":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, huje)
            self.table.insert(4, 3, huje)
            self.table.insert(5, 3, huje)
            self.table.insert(6, 3, luchshe)
            self.table.insert(7, 3, huje)
            self.table.insert(8, 3, OtPC)
            self.table.insert(9, 3, luchshe)
        elif self.name == "HTC Vive Pro" and self.name1 == "Playstation VR 2":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, huje)
            self.table.insert(4, 3, ravni)
            self.table.insert(5, 3, ravni)
            self.table.insert(6, 3, luchshe)
            self.table.insert(7, 3, huje)
            self.table.insert(8, 3, ravni)
            self.table.insert(9, 3, huje)
        elif self.name == "HTC Vive Pro" and self.name1 == "Valve Index VRkit":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, ravni)
            self.table.insert(4, 3, huje)
            self.table.insert(5, 3, ravni)
            self.table.insert(6, 3, luchshe)
            self.table.insert(7, 3, huje)
            self.table.insert(8, 3, ravni)
            self.table.insert(9, 3, luchshe)
            
    def sravn_playstation(self):# функция сравнения для шлема Pico 4
        luchshe = "Лучше"
        huje = "Хуже"
        ravni = "Равны"
        OtPC = "Зависит от компьютера"
        if self.name == "Playstation VR 2" and self.name1 == "Pico 4":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, huje)
            self.table.insert(4, 3, luchshe)
            self.table.insert(5, 3, huje)
            self.table.insert(6, 3, huje)
            self.table.insert(7, 3, luchshe)
            self.table.insert(8, 3, OtPC)
            self.table.insert(9, 3, huje)
        elif self.name == "HPlaystation VR 2" and self.name1 == "Oculus Quest3":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, huje)
            self.table.insert(4, 3, ravni)
            self.table.insert(5, 3, huje)
            self.table.insert(6, 3, huje)
            self.table.insert(7, 3, ravni)
            self.table.insert(8, 3, OtPC)
            self.table.insert(9, 3, huje)
        elif self.name == "Playstation VR 2" and self.name1 == "Pimax crystal":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, huje)
            self.table.insert(4, 3, huje)
            self.table.insert(5, 3, huje)
            self.table.insert(6, 3, luchshe)
            self.table.insert(7, 3, huje)
            self.table.insert(8, 3, OtPC)
            self.table.insert(9, 3, luchshe)
        elif self.name == "Playstation VR 2" and self.name1 == "HTC Vive Pro":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, luchshe)
            self.table.insert(4, 3, ravni)
            self.table.insert(5, 3, ravni)
            self.table.insert(6, 3, huje)
            self.table.insert(7, 3, luchshe)
            self.table.insert(8, 3, ravni)
            self.table.insert(9, 3, luchshe)
        elif self.name == "Playstation VR 2" and self.name1 == "Valve Index VRkit":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, luchshe)
            self.table.insert(4, 3, huje)
            self.table.insert(5, 3, ravni)
            self.table.insert(6, 3, luchshe)
            self.table.insert(7, 3, huje)
            self.table.insert(8, 3, ravni)
            self.table.insert(9, 3, luchshe)
            
    def sravn_valve(self):# функция сравнения для шлема Pico 4
        luchshe = "Лучше"
        huje = "Хуже"
        ravni = "Равны"
        OtPC = "Зависит от компьютера"
        if self.name == "Valve Index VRkit" and self.name1 == "Pico 4":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, huje)
            self.table.insert(4, 3, luchshe)
            self.table.insert(5, 3, huje)
            self.table.insert(6, 3, huje)
            self.table.insert(7, 3, luchshe)
            self.table.insert(8, 3, OtPC)
            self.table.insert(9, 3, huje)
        elif self.name == "Valve Index VRkit" and self.name1 == "Oculus Quest3":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, huje)
            self.table.insert(4, 3, luchshe)
            self.table.insert(5, 3, huje)
            self.table.insert(6, 3, huje)
            self.table.insert(7, 3, luchshe)
            self.table.insert(8, 3, OtPC)
            self.table.insert(9, 3, huje)
        elif self.name == "Valve Index VRkit" and self.name1 == "Pimax crystal":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, huje)
            self.table.insert(4, 3, luchshe)
            self.table.insert(5, 3, huje)
            self.table.insert(6, 3, luchshe)
            self.table.insert(7, 3, huje)
            self.table.insert(8, 3, OtPC)
            self.table.insert(9, 3, huje)
        elif self.name == "Valve Index VRkit" and self.name1 == "HTC Vive Pro":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, ravni)
            self.table.insert(4, 3, luchshe)
            self.table.insert(5, 3, ravni)
            self.table.insert(6, 3, huje)
            self.table.insert(7, 3, luchshe)
            self.table.insert(8, 3, ravni)
            self.table.insert(9, 3, huje)
        elif self.name == "Valve Index VRkit" and self.name1 == "Playstation VR 2":
            self.table.insert(1, 3, "-")
            self.table.insert(2, 3, ravni)
            self.table.insert(3, 3, huje)
            self.table.insert(4, 3, luchshe)
            self.table.insert(5, 3, ravni)
            self.table.insert(6, 3, huje)
            self.table.insert(7, 3, luchshe)
            self.table.insert(8, 3, ravni)
            self.table.insert(9, 3, huje)


#вызов класса и запуск прилоения
if __name__ == "__main__": #если имя соответсвует мейну
    app = App() #функция отображения приложения
    app.mainloop() #запуск отображения