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

#вызов класса и запуск прилоения
if __name__ == "__main__": #если имя соответсвует мейну
    app = App() #функция отображения приложения
    app.mainloop() #запуск отображения