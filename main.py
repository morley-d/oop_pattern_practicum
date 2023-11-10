from mywindow import Window

if __name__ == "__main__":
    handle = Window()
    handle2 = Window()

    handle.title('DAW666')
    handle.geometry('1280x720')

    handle2.title('DAW')
    handle2.geometry('1280x720')

    assert(handle is handle2)

    handle.mainloop()
    handle2.mainloop()
