input.onButtonPressed(Button.A, function () {
    if (sprite.get(LedSpriteProperty.X) == 2) {
        game.addScore(1)
        score1 += 1
        time += -20
    } else {
        sprite.delete()
        music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
        for (let index = 0; index < 2; index++) {
            basic.showIcon(IconNames.Sad)
        }
        for (let index = 0; index < 2; index++) {
            basic.showNumber(score1)
        }
        if (score1 > High_Score) {
            High_Score = score1
        }
        score1 = 0
        sprite = game.createSprite(2, 2)
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(High_Score)
})
let High_Score = 0
let score1 = 0
let sprite: game.LedSprite = null
basic.showIcon(IconNames.Happy)
sprite = game.createSprite(2, 2)
let time = 500
score1 = 0
let move_by = 1
High_Score = 0
basic.forever(function () {
    sprite.move(move_by)
    sprite.ifOnEdgeBounce()
    basic.pause(time)
})
