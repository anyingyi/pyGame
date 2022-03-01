import pygame as pg
import setup
import constants as c

class Mario(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__()
        self.sprite_sheet=setup.GFX['mario_bros']

    def setup_forces(self):
        self.x_vel=0
        self.y_vel=0
        self.max_x_vel=c.MAX_WALK_SPEED
        self.max_y_val=c.MAX_Y_VEL
        self.x_accel=c.WALK_ACCEL
        self.jump_vel=c.JUMP_VEL
        self.gravity=c.GRAVITY

    def get_image(self,x,y,width,height):
        image=pg.Surface([width,height])
        rect=image.get_rect()

        image.blit(self.sprite_sheet,(0,0),(x,y,width,height))
        image.set_colorkey(c.BLACK)
        image=pg.transform.scale(image,
                                 (int(rect.width*c.SIZE_MULTIPLIER),int(rect.height*c.SIZE_MULTIPLIER)))

        return image

    def load_images_from_sheet(self):
        self.right_frames = []
        self.left_frames = []

        self.right_small_normal_frames = []
        self.left_small_normal_frames = []

        self.right_small_normal_frames.append(
            self.get_image(178,32,12,16))
        self.right_small_normal_frames.append(
            self.get_image(80,32,15,16))
        self.right_small_normal_frames.append(
            self.get_image(96, 32, 16, 16))  # Right walking 2 [2]
        self.right_small_normal_frames.append(
            self.get_image(112, 32, 16, 16))  # Right walking 3 [3]
        self.right_small_normal_frames.append(
            self.get_image(144, 32, 16, 16))  # Right jump [4]
        self.right_small_normal_frames.append(
            self.get_image(130, 32, 14, 16))  # Right skid [5]
        self.right_small_normal_frames.append(
            self.get_image(160, 32, 15, 16))  # Death frame [6]
        self.right_small_normal_frames.append(
            self.get_image(320, 8, 16, 24))  # Transition small to big [7]
        self.right_small_normal_frames.append(
            self.get_image(241, 33, 16, 16))  # Transition big to small [8]
        self.right_small_normal_frames.append(
            self.get_image(194, 32, 12, 16))  # Frame 1 of flag pole Slide [9]
        self.right_small_normal_frames.append(
            self.get_image(210, 33, 12, 16))  # Frame 2 of flag pole slide [10]

        for frame in self.right_small_normal_frames:
            new_image=pg.transform.flip(frame,True,False)
            self.left_small_normal_frames.append(new_image)

        self.normal_small_frames=[self.right_small_normal_frames,self.left_small_normal_frames]

        self.right_frames = self.normal_small_frames[0]
        self.left_frames = self.normal_small_frames[1]

    def update(self, keys):
        if self.state==c.WALK:
            self.walking(keys)
        elif self.state==c.JUMP:
            self.jumping(keys)

    def walking(self,keys):
        pass

    def jumping(self,keys,fire_group):
        self.allow_jump=False
        self.gravity=c.JUMP_GRAVITY
        self.y_vel+=self.gravity

        if self.y_vel>=0 and self.y_vel<self.max_y_val:
            self.gravity=c.GRAVITY
            self.state=c.FALL

