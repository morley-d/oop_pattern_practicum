from mywindow import Window

if __name__ == "__main__":
    # создаем окно
    handle = Window()

    # заголовок для окна
    handle.title('DAW666')

    # размеры окна
    handle.geometry('1280x720')

    handle.mainloop()
