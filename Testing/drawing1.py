"""
multi line comment
important to mote down what code does
line3
"""

# single line comment

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color((255, 179, 186))


# Get ready to draw
arcade.start_render()

# (The drawing code will go here.)

# Draw a rectangle
# Left of 0, right of 599
# Top of 300, bottom of 0
arcade.draw_lrbt_rectangle_filled(0, 599, 0, 300, (186,255,201))


# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()