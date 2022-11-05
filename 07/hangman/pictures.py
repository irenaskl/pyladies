
def picture(fail_try):
    if fail_try == 0:
        game_picture = open('picture_zero.txt', 'r')
        return draw_picture(game_picture)
    elif fail_try == 1:
        game_picture = open('picture_one.txt', 'r')
        return draw_picture(game_picture)
    elif fail_try == 2:
        game_picture = open('picture_two.txt', 'r')
        return draw_picture(game_picture)
    elif fail_try == 3:
        game_picture = open('picture_three.txt', 'r')
        return draw_picture(game_picture)
    elif fail_try == 4:
        game_picture = open('picture_four.txt', 'r')
        return draw_picture(game_picture)
    elif fail_try == 5:
        game_picture = open('picture_five.txt', 'r')
        return draw_picture(game_picture)
    elif fail_try == 6:
        game_picture = open('picture_six.txt', 'r')
        return draw_picture(game_picture)
    elif fail_try == 7:
        game_picture = open('picture_seven.txt', 'r')
        return draw_picture(game_picture)
    elif fail_try == 8:
        game_picture = open('picture_eight.txt', 'r')
        return draw_picture(game_picture)
    elif fail_try == 9:
        game_picture = open('picture_nine.txt', 'r')
        return draw_picture(game_picture)


def draw_picture(game_picture):
    for line in game_picture:
        print(line, end='')
