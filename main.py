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



#вызов класса и запуск прилоения
if __name__ == "__main__": #если имя соответсвует мейну
    app = App() #функция отображения приложения
    app.mainloop() #запуск отображения