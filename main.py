def on_button_pressed_a():
    global score1, time, High_Score, sprite
    if sprite.get(LedSpriteProperty.X) == 2:
        game.add_score(1)
        score1 += 1
        time += -20
        music.play_tone(262, music.beat(BeatFraction.SIXTEENTH))
    else:
        sprite.delete()
        music.start_melody(music.built_in_melody(Melodies.DADADADUM),
            MelodyOptions.ONCE)
        for index in range(2):
            basic.show_icon(IconNames.SAD)
        for index2 in range(2):
            basic.show_number(score1)
        if score1 > High_Score:
            High_Score = score1
        score1 = 0
        sprite = game.create_sprite(2, 2)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_number(High_Score)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

High_Score = 0
score1 = 0
sprite: game.LedSprite = None
basic.show_icon(IconNames.HAPPY)
sprite = game.create_sprite(2, 2)
time = 500
score1 = 0
move_by = 1
High_Score = 0

def on_forever():
    sprite.if_on_edge_bounce()
    basic.pause(time)
    sprite.move(move_by)
basic.forever(on_forever)
