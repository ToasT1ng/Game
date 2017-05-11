def draw_snowman(screen, x, y):
    # Draw a circle for the head
    pygame.draw.ellipse(screen, WHITE, [35 + x, y, 25, 25])
    # Draw the middle snowman circle
    pygame.draw.ellipse(screen, WHITE, [23 + x, 20 + y, 50, 50])
    # Draw the bottom snowman circle
    pygame.draw.ellipse(screen, WHITE, [x, 65 + y, 100, 100])

# Snowman in upper left
draw_snowman(screen, 10, 10)
 
# Snowman in upper right
draw_snowman(screen, 300, 10)
 
# Snowman in lower left
draw_snowman(screen, 10, 300)