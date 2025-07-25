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
arcade.set_background_color((255, 179, 186, 0))


# Get ready to draw
arcade.start_render()

# (The drawing code will go here.)

# Draw a rectangles which mak eup background colors
# First one: Left of 0, right of 599, bottom of 0, Top of 300,
arcade.draw_lrbt_rectangle_filled(0, 599, 0, 300, (186,255,201)) # green
arcade.draw_lrbt_rectangle_filled(0, 599, 150, 300, (255,255,186)) # yellow
arcade.draw_lrbt_rectangle_filled(0, 599, 300, 450, (255,223,186)) # orange


# Draw an ellipse, no outline rectangle needed
# if you set all parameters the same it makes a circle
# put this code before the lollipops so it is rendered first and the lollipos appear on top
# a center of (300, 300)
# width of 350
# height of 200
arcade.draw_ellipse_outline(300, 300, 450, 450, (255,247,0), 3)

arcade.draw_triangle_outline(125, 150, 475, 150, 300, 525, (255, 247, 0), 3)


# This part of the code makes the lollipop art

# Left lollipop
# Blue vertical bar for lollipop stem
arcade.draw_lrbt_rectangle_filled(116, 124, 199, 401, (255, 19, 240))
arcade.draw_lrbt_rectangle_filled(117, 123, 200, 400, (186, 225, 255))

# Lollipop top
arcade.draw_circle_filled(120, 375, 62, (255, 19, 240))
arcade.draw_circle_filled(120, 375, 60, (186, 255, 201))
arcade.draw_circle_filled(120, 375, 50, (168, 230, 207))
arcade.draw_circle_filled(120, 375, 40, (220, 237, 193))
arcade.draw_circle_filled(120, 375, 30, (255, 211, 182))
arcade.draw_circle_filled(120, 375, 20, (255, 170, 165))
arcade.draw_circle_filled(120, 375, 10, (255, 139, 148))

# Middle lollipop
# Blue vertical bar for lollipop stem
arcade.draw_lrbt_rectangle_filled(316, 324, 49, 251, (255, 19, 240))
arcade.draw_lrbt_rectangle_filled(317, 323, 50, 250, (186, 225, 255))

# Lollipop top
arcade.draw_circle_filled(320, 225, 62, (255, 19, 240))
arcade.draw_circle_filled(320, 225, 60, (186, 255, 201))
arcade.draw_circle_filled(320, 225, 50, (168, 230, 207))
arcade.draw_circle_filled(320, 225, 40, (220, 237, 193))
arcade.draw_circle_filled(320, 225, 30, (255, 211, 182))
arcade.draw_circle_filled(320, 225, 20, (255, 170, 165))
arcade.draw_circle_filled(320, 225, 10, (255, 139, 148))

# Right lollipop
# Blue vertical bar for lollipop stem
arcade.draw_lrbt_rectangle_filled(436, 444, 326, 526, (255, 19, 240))
arcade.draw_lrbt_rectangle_filled(437, 443, 327, 527, (186, 225, 255))

# Lollipop top
arcade.draw_circle_filled(440, 500, 62, (255, 19, 240))
arcade.draw_circle_filled(440, 500, 60, (186, 255, 201))
arcade.draw_circle_filled(440, 500, 50, (168, 230, 207))
arcade.draw_circle_filled(440, 500,  40, (220, 237, 193))
arcade.draw_circle_filled(440, 500,  30, (255, 211, 182))
arcade.draw_circle_filled(440, 500,  20, (255, 170, 165))
arcade.draw_circle_filled(440, 500, 10, (255, 139, 148))

#this code writes the message in the picture
arcade.draw_text("Lollipop Fun ",150, 450, (0, 0, 205), 50)
arcade.draw_text("is ",300, 250, (0, 0, 205), 50)
arcade.draw_text("best Fun",150, 50, (0, 0, 205), 50)


# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()