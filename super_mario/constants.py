

SCREEN_HEIGHT=600
SCREEN_WIDTH=800

SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

ORIGINAL_CAPTION = "Super Mario Bros 1-1"

## COLORS ##

#            R    G    B
GRAY         = (100, 100, 100)
NAVYBLUE     = ( 60,  60, 100)
WHITE        = (255, 255, 255)
RED          = (255,   0,   0)
GREEN        = (  0, 255,   0)
FOREST_GREEN = ( 31, 162,  35)
BLUE         = (  0,   0, 255)
SKY_BLUE     = ( 39, 145, 251)
YELLOW       = (255, 255,   0)
ORANGE       = (255, 128,   0)
PURPLE       = (255,   0, 255)
CYAN         = (  0, 255, 255)
BLACK        = (  0,   0,   0)
NEAR_BLACK    = ( 19,  15,  48)
COMBLUE      = (233, 232, 255)
GOLD         = (255, 215,   0)

BGCOLOR = WHITE

SIZE_MULTIPLIER = 2.5
BRICK_SIZE_MULTIPLIER = 2.69
BACKGROUND_MULTIPLER = 2.679
GROUND_HEIGHT = SCREEN_HEIGHT - 62

#MARIO FORCES
WALK_ACCEL = .15
RUN_ACCEL = 20
SMALL_TURNAROUND = .35

GRAVITY = 1.01
JUMP_GRAVITY = .31
JUMP_VEL = -10
FAST_JUMP_VEL = -12.5
MAX_Y_VEL = 11

MAX_RUN_SPEED = 800
MAX_WALK_SPEED = 6

#Mario States

STAND = 'standing'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
SMALL_TO_BIG = 'small to big'
BIG_TO_FIRE = 'big to fire'
BIG_TO_SMALL = 'big to small'
FLAGPOLE = 'flag pole'
WALKING_TO_CASTLE = 'walking to castle'
END_OF_LEVEL_FALL = 'end of level fall'
