# CCW backwards
# CW forwards
strip: neopixel.Strip = None

def on_button_pressed_a():
    music.play_melody("C - C F C B A G ", 120)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    global strip
    strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
    strip.show_color(neopixel.colors(NeoPixelColors.INDIGO))
    basic.show_leds("""
                . # # # .
                # # . . .
                # . # . .
                # . . # .
                . . . . #
    """)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 40)
    if input.compass_heading() == 90:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 60)
basic.forever(on_forever)
