# CCW backwards
# CW forwards

def on_forever():
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 255)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)
basic.forever(on_forever)
