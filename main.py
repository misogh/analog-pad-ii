dir2 = ""
P2 = 0
P1 = 0
radio.set_group(1)

def on_forever():
    global P1, P2, dir2
    P1 = pins.analog_read_pin(AnalogReadWritePin.P1)
    P2 = pins.analog_read_pin(AnalogReadWritePin.P2)
    if P2 > 550 and (P1 > 400 and P1 < 600):
        dir2 = "F"
    elif P2 < 450 and (P1 > 400 and P1 < 600):
        dir2 = "B"
    elif P1 > 550 and (P2 > 400 and P2 < 600):
        dir2 = "R"
    elif P1 < 450 and (P2 > 400 and P2 < 600):
        dir2 = "L"
    else:
        dir2 = "S"
    basic.show_string(dir2)
    radio.send_string(dir2)
basic.forever(on_forever)
