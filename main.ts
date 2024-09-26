let dir = ""
let P2 = 0
let P1 = 0
radio.setGroup(1)
basic.forever(function () {
    P1 = pins.analogReadPin(AnalogReadWritePin.P1)
    P2 = pins.analogReadPin(AnalogReadWritePin.P2)
    if (P2 > 550 && (P1 > 400 && P1 < 600)) {
        dir = "F"
    } else if (P2 < 450 && (P1 > 400 && P1 < 600)) {
        dir = "B"
    } else if (P1 > 550 && (P2 > 400 && P2 < 600)) {
        dir = "R"
    } else if (P1 < 450 && (P2 > 400 && P2 < 600)) {
        dir = "L"
    } else {
        dir = "S"
    }
    radio.sendString(dir)
})
