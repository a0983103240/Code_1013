def on_forever():
    for X in range(5):
        for Y in range(5):
            led.plot(X, Y)
            basic.pause(500)
    basic.clear_screen()
basic.forever(on_forever)
