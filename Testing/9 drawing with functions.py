
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_the_ground():
        """drawing grass"""
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT / 3, arcade.color.AIR_SUPERIORITY_BLUE)

def draw_snow_person(x, y):
    """draws a snow person made of three white balls and 2 eyes"""
    # Snow
    arcade.draw_circle_filled(x , y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y + 80, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y + 140, 40, arcade.color.WHITE)
    # Eyes
    arcade.draw_circle_filled(x - 15, y + 150, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, y + 150, 5, arcade.color.BLACK)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    # Draw the ground
    draw_the_ground()

    # Draw a snow person
    draw_snow_person(300, 200)
    draw_snow_person(150, 100)
    draw_snow_person(700, 200)
    draw_snow_person(500, 225)


    #  Finish and run
    arcade.finish_render()
    arcade.run()

# call main function to run the program
main()
