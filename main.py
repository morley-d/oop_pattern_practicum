from mywindow import Window

if __name__ == "__main__":
    handle = Window()

    handle.title('DAW666')
    handle.geometry('1280x720')

    assert(handle is handle2)

    handle.mainloop()
