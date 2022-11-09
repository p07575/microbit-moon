basic.show_string("This is the moon!!!")
basic.pause(1000)

def on_forever():
    basic.show_leds("""
        . . . # .
                . . . # #
                . . . # #
                . . . # #
                . . . # .
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . # # .
                . . # # #
                . . # # #
                . . # # #
                . . # # .
    """)
    basic.pause(1000)
    basic.show_leds("""
        . # # # .
                . # # # #
                . # # # #
                . # # # #
                . # # # .
    """)
    basic.pause(1000)
    basic.show_leds("""
        . # # # .
                # # # # #
                # # # # #
                # # # # #
                . # # # .
    """)
    basic.pause(1000)
    basic.show_leds("""
        . # # # .
                # # # # .
                # # # # .
                # # # # .
                . # # # .
    """)
    basic.pause(1000)
    basic.show_leds("""
        . # # . .
                # # # . .
                # # # . .
                # # # . .
                . # # . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        . # . . .
                # # . . .
                # # . . .
                # # . . .
                . # . . .
    """)
    basic.pause(1000)
basic.forever(on_forever)
