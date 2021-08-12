import pygame, random, math

class Character():
    def __init__(self, velocity, xCoord, yCoord, facing, height, width, health):
        self.velocity = velocity
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.facing = facing
        self.height = height
        self.width = width
        self.health = health
        self.healthCount = 0
        self.avatar = [pygame.image.load("images/Characters/tizochealth.png").convert_alpha(), pygame.image.load("images/Characters/eijihealth.png").convert_alpha(), pygame.image.load("images/Opponents/chinhealth.png").convert_alpha(), pygame.image.load("images/Opponents/duohealth.png").convert_alpha(), pygame.image.load("images/Opponents/tunghealth.png").convert_alpha()]
        self.enemyHealthCount = 0
        self.isDead = False
        self.isIdle = True
        self.isKicking = False
        self.isPunching = False
        self.isWalking = False
        self.isJumping = False
        self.isBlocking = False
        self.isActive = False
        self.walkingImagesLeft = []
        self.walkingImagesRight = []
        self.standingImagesLeft = []
        self.standingImagesRight = []
        self.kickingImagesLeft = []
        self.kickingimagesRight = []
        self.kickingCount = 0
        self.punchingimagesLeft = []
        self.punchingImagesRight = []
        self.jumpingimagesLeft = []
        self.jumpingimagesRight = []
        self.jumpingCount = 10
        self.specialJumpingCount = 8
        self.blockingImagesLeft = []
        self.blockingImagesRight = []
        self.specialMoveImagesLeft = []
        self.specialMoveImagesRight = []
        self.smHappening = False
        self.smDown = False
        self.playersmBarCount = 0
        self.enemysmBarCount = 0
        self.isAttacking = False
        self.isSpecialMove = False
        self.statusCount = 0
        self.imageTimer = 0
        self.playerPoints = 0
        self.eijiSM = False

    def jumpMove(self):
        if self.jumpingCount >= 0:
            self.yCoord -= (self.jumpingCount**2) * 0.3
            self.jumpingCount -= 1
        elif self.jumpingCount >= -10:
            self.yCoord += (self.jumpingCount**2) * 0.3
            self.jumpingCount -= 1
        else:
            self.jumpingCount = 10
            self.statusCount = 0
            self.isSpecialMove = False
            self.isJumping = False
            self.isIdle = True

    def controllingCharacter(self, game, imagesArrayLeft, imagesArrayRight, target, floorDivideCount):
        if self.statusCount == len(imagesArrayLeft)*floorDivideCount:
            self.statusCount = 0
            self.numGenDefense = random.randint(1, 15)
            self.numGenOffense = random.randint(1, 15)
            self.isIdle = True
            self.isWalking = False
            self.isBlocking = False
            self.isKicking = False
            self.isPunching = False
            self.isSpecialMove = False

        self.characterAnimation(game, imagesArrayLeft, imagesArrayRight, target, floorDivideCount)

        if self.isJumping:
            self.jumpMove()

    def characterAnimation(self, game, imagesArrayLeft, imagesArrayRight, target, floorDivideCount):
        # Displaying the left and right images
        try:
            if self.facing == "left":
                game.window.blit(imagesArrayLeft[self.statusCount//floorDivideCount], (self.xCoord, self.yCoord))
                self.statusCount += 1  
                self.imageTimer += 1

            if self.facing == "right":
                game.window.blit(imagesArrayRight[self.statusCount//floorDivideCount], (self.xCoord, self.yCoord))
                self.statusCount += 1
                self.imageTimer += 1
        except:
            game.window.blit(imagesArrayRight[0], (self.xCoord, self.yCoord))
    

class Tizoc(Character):
    def __init__(self, velocity, xCoord, yCoord, facing, height, width, health):
        super().__init__(velocity, xCoord, yCoord, facing, height, width, health)
    
        self.standingImagesLeft = [pygame.image.load("images/Characters/tizoc_1/standing/Tizoc_0L.png"), pygame.image.load("images/Characters/tizoc_1/standing/Tizoc_1L.png"), pygame.image.load("images/Characters/tizoc_1/standing/Tizoc_2L.png"), pygame.image.load("images/Characters/tizoc_1/standing/Tizoc_3L.png"), pygame.image.load("images/Characters/tizoc_1/standing/Tizoc_4L.png"), pygame.image.load("images/Characters/tizoc_1/standing/Tizoc_5L.png"), pygame.image.load("images/Characters/tizoc_1/standing/Tizoc_6L.png")]
        self.standingImagesRight = [pygame.image.load("images/Characters/tizoc_1/standing/Tizoc_0R.png"), pygame.image.load("images/Characters/tizoc_1/standing/Tizoc_1R.png"), pygame.image.load("images/Characters/tizoc_1/standing/Tizoc_2R.png"), pygame.image.load("images/Characters/tizoc_1/standing/Tizoc_3R.png"), pygame.image.load("images/Characters/tizoc_1/standing/Tizoc_4R.png"), pygame.image.load("images/Characters/tizoc_1/standing/Tizoc_5R.png"), pygame.image.load("images/Characters/tizoc_1/standing/Tizoc_6R.png")]
        self.walkingImagesLeft = [pygame.image.load("images/Characters/tizoc_1/walking/Tizoc_7L.png"), pygame.image.load("images/Characters/tizoc_1/walking/Tizoc_8L.png"), pygame.image.load("images/Characters/tizoc_1/walking/Tizoc_9L.png"), pygame.image.load("images/Characters/tizoc_1/walking/Tizoc_10L.png"), pygame.image.load("images/Characters/tizoc_1/walking/Tizoc_11L.png"), pygame.image.load("images/Characters/tizoc_1/walking/Tizoc_12L.png"), pygame.image.load("images/Characters/tizoc_1/walking/Tizoc_13L.png"), pygame.image.load("images/Characters/tizoc_1/walking/Tizoc_14L.png")]
        self.walkingImagesRight = [pygame.image.load("images/Characters/tizoc_1/walking/Tizoc_7R.png"), pygame.image.load("images/Characters/tizoc_1/walking/Tizoc_8R.png"), pygame.image.load("images/Characters/tizoc_1/walking/Tizoc_9R.png"), pygame.image.load("images/Characters/tizoc_1/walking/Tizoc_10R.png"), pygame.image.load("images/Characters/tizoc_1/walking/Tizoc_11R.png"), pygame.image.load("images/Characters/tizoc_1/walking/Tizoc_12R.png"), pygame.image.load("images/Characters/tizoc_1/walking/Tizoc_13R.png"), pygame.image.load("images/Characters/tizoc_1/walking/Tizoc_14R.png")]
        self.blockingImagesLeft = [pygame.image.load("images/Characters/tizoc_1/blocking/Tizoc_31L.png"), pygame.image.load("images/Characters/tizoc_1/blocking/Tizoc_29L.png"), pygame.image.load("images/Characters/tizoc_1/blocking/Tizoc_30L.png"), pygame.image.load("images/Characters/tizoc_1/blocking/Tizoc_31L.png")]
        self.blockingImagesRight = [pygame.image.load("images/Characters/tizoc_1/blocking/Tizoc_31R.png"), pygame.image.load("images/Characters/tizoc_1/blocking/Tizoc_29R.png"), pygame.image.load("images/Characters/tizoc_1/blocking/Tizoc_30R.png"), pygame.image.load("images/Characters/tizoc_1/blocking/Tizoc_31R.png")]
        self.kickingImagesLeft = [pygame.image.load("images/Characters/tizoc_1/kicking/Tizoc_88L.png"), pygame.image.load("images/Characters/tizoc_1/kicking/Tizoc_89L.png"), pygame.image.load("images/Characters/tizoc_1/kicking/Tizoc_90L.png"), pygame.image.load("images/Characters/tizoc_1/kicking/Tizoc_91L.png"), pygame.image.load("images/Characters/tizoc_1/kicking/Tizoc_92L.png"), pygame.image.load("images/Characters/tizoc_1/kicking/Tizoc_93L.png"), pygame.image.load("images/Characters/tizoc_1/kicking/Tizoc_94L.png")]
        self.kickingImagesRight = [pygame.image.load("images/Characters/tizoc_1/kicking/Tizoc_88R.png"), pygame.image.load("images/Characters/tizoc_1/kicking/Tizoc_89R.png"), pygame.image.load("images/Characters/tizoc_1/kicking/Tizoc_90R.png"), pygame.image.load("images/Characters/tizoc_1/kicking/Tizoc_91R.png"), pygame.image.load("images/Characters/tizoc_1/kicking/Tizoc_92R.png"), pygame.image.load("images/Characters/tizoc_1/kicking/Tizoc_93R.png"), pygame.image.load("images/Characters/tizoc_1/kicking/Tizoc_94R.png")]
        self.punchingImagesLeft = [pygame.image.load("images/Characters/tizoc_1/punching/Tizoc_149L.png"), pygame.image.load("images/Characters/tizoc_1/punching/Tizoc_150L.png"), pygame.image.load("images/Characters/tizoc_1/punching/Tizoc_151L.png"), pygame.image.load("images/Characters/tizoc_1/punching/Tizoc_152L.png"), pygame.image.load("images/Characters/tizoc_1/punching/Tizoc_153L.png"), pygame.image.load("images/Characters/tizoc_1/punching/Tizoc_154L.png"), pygame.image.load("images/Characters/tizoc_1/punching/Tizoc_155L.png")]
        self.punchingImagesRight = [pygame.image.load("images/Characters/tizoc_1/punching/Tizoc_149R.png"), pygame.image.load("images/Characters/tizoc_1/punching/Tizoc_150R.png"), pygame.image.load("images/Characters/tizoc_1/punching/Tizoc_151R.png"), pygame.image.load("images/Characters/tizoc_1/punching/Tizoc_152R.png"), pygame.image.load("images/Characters/tizoc_1/punching/Tizoc_153R.png"), pygame.image.load("images/Characters/tizoc_1/punching/Tizoc_154R.png"), pygame.image.load("images/Characters/tizoc_1/punching/Tizoc_155R.png")]
        self.jumpingImagesLeft = [pygame.image.load("images/Characters/tizoc_1/jumping/Tizoc_15L.png"), pygame.image.load("images/Characters/tizoc_1/jumping/Tizoc_16L.png"), pygame.image.load("images/Characters/tizoc_1/jumping/Tizoc_17L.png"), pygame.image.load("images/Characters/tizoc_1/jumping/Tizoc_18L.png"), pygame.image.load("images/Characters/tizoc_1/jumping/Tizoc_19L.png"), pygame.image.load("images/Characters/tizoc_1/jumping/Tizoc_20L.png"), pygame.image.load("images/Characters/tizoc_1/jumping/Tizoc_21L.png"), pygame.image.load("images/Characters/tizoc_1/jumping/Tizoc_22L.png")]
        self.jumpingImagesRight = [pygame.image.load("images/Characters/tizoc_1/jumping/Tizoc_15R.png"), pygame.image.load("images/Characters/tizoc_1/jumping/Tizoc_16R.png"), pygame.image.load("images/Characters/tizoc_1/jumping/Tizoc_17R.png"), pygame.image.load("images/Characters/tizoc_1/jumping/Tizoc_18R.png"), pygame.image.load("images/Characters/tizoc_1/jumping/Tizoc_19R.png"), pygame.image.load("images/Characters/tizoc_1/jumping/Tizoc_20R.png"), pygame.image.load("images/Characters/tizoc_1/jumping/Tizoc_21R.png"), pygame.image.load("images/Characters/tizoc_1/jumping/Tizoc_22R.png")]
        self.specialMoveImagesLeft = [pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_197L.png"), pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_198L.png"), pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_199L.png"), pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_200L.png"), pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_201L.png"), pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_202L.png"), pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_202L.png"), pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_203L.png"), pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_204L.png"), pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_205L.png")]
        self.specialMoveImagesRight = [pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_197R.png"), pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_198R.png"), pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_199R.png"), pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_200R.png"), pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_201R.png"), pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_202R.png"), pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_202R.png"), pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_203R.png"), pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_204R.png"), pygame.image.load("images/Characters/tizoc_1/special move/Special Move 1/Tizoc_205R.png")]

    def characterAnimation(self, game, imagesArrayLeft, imagesArrayRight, target, floorDivideCount):
        try:
            if imagesArrayLeft == self.specialMoveImagesLeft and not (((self.xCoord >= target.xCoord - 200) and (self.xCoord <= target.xCoord + 200))):
                game.window.blit(imagesArrayRight[0], (self.xCoord, self.yCoord))
                self.isSpecialMove = False
                self.isIdle = True
            else:
                if self.facing == "left":
                    game.window.blit(imagesArrayLeft[self.statusCount//floorDivideCount], (self.xCoord, self.yCoord))
                    self.statusCount += 1  
                    self.imageTimer += 1

                if self.facing == "right":
                    game.window.blit(imagesArrayRight[self.statusCount//floorDivideCount], (self.xCoord, self.yCoord))
                    self.statusCount += 1
                    self.imageTimer += 1
        except:
            game.window.blit(imagesArrayRight[0], (self.xCoord, self.yCoord))

        # Tizoc's piledriver special move
        if self.isSpecialMove and (self.xCoord >= target.xCoord - 600) and (self.xCoord <= target.xCoord + 600):
            
            self.smHappening = True

            if self.specialJumpingCount >= 0:
                self.yCoord -= (self.specialJumpingCount**2) * 0.3
                target.yCoord -=(self.specialJumpingCount**2) * 0.3
                self.specialJumpingCount -= 1
                target.obstacleDown = False
                target.obstacleUp = True
                self.smHappening = True
                self.smDown = False
            elif self.specialJumpingCount >= -8:
                self.yCoord += (self.specialJumpingCount**2) * 0.3
                target.yCoord +=(self.specialJumpingCount**2) * 0.3
                self.specialJumpingCount -= 1
                target.obstacleDown = True
                target.obstacleUp = False
                self.smHappening = True
                self.smDown = True
            else:
                self.yCoord = 180
                self.specialJumpingCount = 8
                self.statusCount = 0
                self.isSpecialMove = False
                self.isJumping = False
                self.isIdle = True
                target.obstacleDown = False
                target.obstacleUp = True
                self.smHappening = False
                self.smDown = False

class Eiji(Character):
    def __init__(self, velocity, xCoord, yCoord, facing, height, width, health):
        super().__init__(velocity, xCoord, yCoord, facing, height, width, health)

        self.standingImagesLeft = [pygame.image.load("images/Characters/eiji_2/standing/eiji_0L.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_1L.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_2L.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_3L.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_4L.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_5L.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_6L.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_7L.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_8L.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_9L.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_10L.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_11L.png")]
        self.standingImagesRight = [pygame.image.load("images/Characters/eiji_2/standing/eiji_0R.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_1R.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_2R.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_3R.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_4R.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_5R.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_6R.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_7R.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_8R.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_9R.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_10R.png"), pygame.image.load("images/Characters/eiji_2/standing/eiji_11R.png")]
        self.walkingImagesLeft = [pygame.image.load("images/Characters/eiji_2/walking/eiji_49L.png"), pygame.image.load("images/Characters/eiji_2/walking/eiji_50L.png"), pygame.image.load("images/Characters/eiji_2/walking/eiji_51L.png"), pygame.image.load("images/Characters/eiji_2/walking/eiji_52L.png"), pygame.image.load("images/Characters/eiji_2/walking/eiji_53L.png"), pygame.image.load("images/Characters/eiji_2/walking/eiji_54L.png"), pygame.image.load("images/Characters/eiji_2/walking/eiji_54L.png"), pygame.image.load("images/Characters/eiji_2/walking/eiji_54L.png")]
        self.walkingImagesRight = [pygame.image.load("images/Characters/eiji_2/walking/eiji_49R.png"), pygame.image.load("images/Characters/eiji_2/walking/eiji_50R.png"), pygame.image.load("images/Characters/eiji_2/walking/eiji_51R.png"), pygame.image.load("images/Characters/eiji_2/walking/eiji_52R.png"), pygame.image.load("images/Characters/eiji_2/walking/eiji_53R.png"), pygame.image.load("images/Characters/eiji_2/walking/eiji_54R.png"), pygame.image.load("images/Characters/eiji_2/walking/eiji_54R.png"), pygame.image.load("images/Characters/eiji_2/walking/eiji_54R.png")]
        self.blockingImagesLeft = [pygame.image.load("images/Characters/eiji_2/blocking/eiji_45L.png"), pygame.image.load("images/Characters/eiji_2/blocking/eiji_46L.png"), pygame.image.load("images/Characters/eiji_2/blocking/eiji_47L.png"), pygame.image.load("images/Characters/eiji_2/blocking/eiji_47L.png")]
        self.blockingImagesRight = [pygame.image.load("images/Characters/eiji_2/blocking/eiji_45R.png"), pygame.image.load("images/Characters/eiji_2/blocking/eiji_46R.png"), pygame.image.load("images/Characters/eiji_2/blocking/eiji_47R.png"), pygame.image.load("images/Characters/eiji_2/blocking/eiji_47R.png")]
        self.kickingImagesLeft = [pygame.image.load("images/Characters/eiji_2/kicking/eiji_178L.png"), pygame.image.load("images/Characters/eiji_2/kicking/eiji_179L.png"), pygame.image.load("images/Characters/eiji_2/kicking/eiji_180L.png"), pygame.image.load("images/Characters/eiji_2/kicking/eiji_181L.png"), pygame.image.load("images/Characters/eiji_2/kicking/eiji_182L.png"), pygame.image.load("images/Characters/eiji_2/kicking/eiji_183L.png"), pygame.image.load("images/Characters/eiji_2/kicking/eiji_184L.png"), pygame.image.load("images/Characters/eiji_2/kicking/eiji_185L.png"), pygame.image.load("images/Characters/eiji_2/kicking/eiji_186L.png")]
        self.kickingImagesRight = [pygame.image.load("images/Characters/eiji_2/kicking/eiji_178R.png"), pygame.image.load("images/Characters/eiji_2/kicking/eiji_179R.png"), pygame.image.load("images/Characters/eiji_2/kicking/eiji_180R.png"), pygame.image.load("images/Characters/eiji_2/kicking/eiji_181R.png"), pygame.image.load("images/Characters/eiji_2/kicking/eiji_182R.png"), pygame.image.load("images/Characters/eiji_2/kicking/eiji_183R.png"), pygame.image.load("images/Characters/eiji_2/kicking/eiji_184R.png"), pygame.image.load("images/Characters/eiji_2/kicking/eiji_185R.png"), pygame.image.load("images/Characters/eiji_2/kicking/eiji_186R.png")]
        self.punchingImagesLeft = [pygame.image.load("images/Characters/eiji_2/punching/eiji_92L.png"), pygame.image.load("images/Characters/eiji_2/punching/eiji_93L.png"), pygame.image.load("images/Characters/eiji_2/punching/eiji_94L.png"), pygame.image.load("images/Characters/eiji_2/punching/eiji_95L.png"), pygame.image.load("images/Characters/eiji_2/punching/eiji_96L.png"), pygame.image.load("images/Characters/eiji_2/punching/eiji_97L.png"), pygame.image.load("images/Characters/eiji_2/punching/eiji_98L.png"), pygame.image.load("images/Characters/eiji_2/punching/eiji_99L.png")]
        self.punchingImagesRight = [pygame.image.load("images/Characters/eiji_2/punching/eiji_92R.png"), pygame.image.load("images/Characters/eiji_2/punching/eiji_93R.png"), pygame.image.load("images/Characters/eiji_2/punching/eiji_94R.png"), pygame.image.load("images/Characters/eiji_2/punching/eiji_95R.png"), pygame.image.load("images/Characters/eiji_2/punching/eiji_96R.png"), pygame.image.load("images/Characters/eiji_2/punching/eiji_97R.png"), pygame.image.load("images/Characters/eiji_2/punching/eiji_98R.png"), pygame.image.load("images/Characters/eiji_2/punching/eiji_99R.png")]
        self.jumpingImagesLeft = [pygame.image.load("images/Characters/eiji_2/jumping/eiji_20L.png"), pygame.image.load("images/Characters/eiji_2/jumping/eiji_21L.png"), pygame.image.load("images/Characters/eiji_2/jumping/eiji_22L.png"), pygame.image.load("images/Characters/eiji_2/jumping/eiji_23L.png"), pygame.image.load("images/Characters/eiji_2/jumping/eiji_24L.png"), pygame.image.load("images/Characters/eiji_2/jumping/eiji_25L.png"), pygame.image.load("images/Characters/eiji_2/jumping/eiji_25L.png"), pygame.image.load("images/Characters/eiji_2/jumping/eiji_25L.png")]
        self.jumpingImagesRight = [pygame.image.load("images/Characters/eiji_2/jumping/eiji_20R.png"), pygame.image.load("images/Characters/eiji_2/jumping/eiji_21R.png"), pygame.image.load("images/Characters/eiji_2/jumping/eiji_22R.png"), pygame.image.load("images/Characters/eiji_2/jumping/eiji_23R.png"), pygame.image.load("images/Characters/eiji_2/jumping/eiji_24R.png"), pygame.image.load("images/Characters/eiji_2/jumping/eiji_25R.png"), pygame.image.load("images/Characters/eiji_2/jumping/eiji_25R.png"), pygame.image.load("images/Characters/eiji_2/jumping/eiji_25R.png")]
        self.specialMoveImagesLeft = [pygame.image.load("images/Characters/eiji_2/special move/eiji_201L.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_202L.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_203L.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_204L.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_205L.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_206L.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_207L.png")]
        self.specialMoveImagesRight = [pygame.image.load("images/Characters/eiji_2/special move/eiji_201R.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_202R.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_203R.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_204R.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_205R.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_206R.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_207R.png")]

class Chin(Character):
    def __init__(self, velocity, xCoord, yCoord, facing, height, width, health):
        super().__init__(velocity, xCoord, yCoord, facing, height, width, health)

        self.standingImagesLeft = [pygame.image.load("images/Opponents/Chin/standing/chin_0L.png"), pygame.image.load("images/Opponents/Chin/standing/chin_1L.png"), pygame.image.load("images/Opponents/Chin/standing/chin_2L.png"), pygame.image.load("images/Opponents/Chin/standing/chin_3L.png"), pygame.image.load("images/Opponents/Chin/standing/chin_4L.png"), pygame.image.load("images/Opponents/Chin/standing/chin_5L.png"), pygame.image.load("images/Opponents/Chin/standing/chin_6L.png"), pygame.image.load("images/Opponents/Chin/standing/chin_7L.png"), pygame.image.load("images/Opponents/Chin/standing/chin_8L.png"), pygame.image.load("images/Opponents/Chin/standing/chin_9L.png")]
        self.standingImagesRight = [pygame.image.load("images/Opponents/Chin/standing/chin_0R.png"), pygame.image.load("images/Opponents/Chin/standing/chin_1R.png"), pygame.image.load("images/Opponents/Chin/standing/chin_2R.png"), pygame.image.load("images/Opponents/Chin/standing/chin_3R.png"), pygame.image.load("images/Opponents/Chin/standing/chin_4R.png"), pygame.image.load("images/Opponents/Chin/standing/chin_5R.png"), pygame.image.load("images/Opponents/Chin/standing/chin_6R.png"), pygame.image.load("images/Opponents/Chin/standing/chin_7R.png"), pygame.image.load("images/Opponents/Chin/standing/chin_8R.png"), pygame.image.load("images/Opponents/Chin/standing/chin_9R.png")]
        self.walkingImagesLeft = [pygame.image.load("images/Opponents/Chin/walking/chin_10L.png"), pygame.image.load("images/Opponents/Chin/walking/chin_11L.png"), pygame.image.load("images/Opponents/Chin/walking/chin_12L.png"), pygame.image.load("images/Opponents/Chin/walking/chin_13L.png"), pygame.image.load("images/Opponents/Chin/walking/chin_14L.png"), pygame.image.load("images/Opponents/Chin/walking/chin_15L.png")]
        self.walkingImagesRight = [pygame.image.load("images/Opponents/Chin/walking/chin_10R.png"), pygame.image.load("images/Opponents/Chin/walking/chin_11R.png"), pygame.image.load("images/Opponents/Chin/walking/chin_12R.png"), pygame.image.load("images/Opponents/Chin/walking/chin_13R.png"), pygame.image.load("images/Opponents/Chin/walking/chin_14R.png"), pygame.image.load("images/Opponents/Chin/walking/chin_15R.png")]
        self.blockingImagesLeft = [pygame.image.load("images/Opponents/Chin/blocking/chin_36L.png"), pygame.image.load("images/Opponents/Chin/blocking/chin_36L.png"), pygame.image.load("images/Opponents/Chin/blocking/chin_37L.png"), pygame.image.load("images/Opponents/Chin/blocking/chin_38L.png"), pygame.image.load("images/Opponents/Chin/blocking/chin_39L.png"), pygame.image.load("images/Opponents/Chin/blocking/chin_39L.png"), pygame.image.load("images/Opponents/Chin/blocking/chin_39L.png"), pygame.image.load("images/Opponents/Chin/blocking/chin_39L.png")]
        self.blockingImagesRight = [pygame.image.load("images/Opponents/Chin/blocking/chin_36R.png"), pygame.image.load("images/Opponents/Chin/blocking/chin_36R.png"), pygame.image.load("images/Opponents/Chin/blocking/chin_37R.png"), pygame.image.load("images/Opponents/Chin/blocking/chin_38R.png"), pygame.image.load("images/Opponents/Chin/blocking/chin_39R.png"), pygame.image.load("images/Opponents/Chin/blocking/chin_39R.png"), pygame.image.load("images/Opponents/Chin/blocking/chin_39R.png"), pygame.image.load("images/Opponents/Chin/blocking/chin_39R.png")]
        self.kickingImagesLeft = [pygame.image.load("images/Opponents/Chin/kicking/chin_61L.png"), pygame.image.load("images/Opponents/Chin/kicking/chin_61L.png"), pygame.image.load("images/Opponents/Chin/kicking/chin_62L.png"), pygame.image.load("images/Opponents/Chin/kicking/chin_63L.png"), pygame.image.load("images/Opponents/Chin/kicking/chin_64L.png"), pygame.image.load("images/Opponents/Chin/kicking/chin_64L.png"), pygame.image.load("images/Opponents/Chin/kicking/chin_64L.png"), pygame.image.load("images/Opponents/Chin/kicking/chin_64L.png")]
        self.kickingImagesRight = [pygame.image.load("images/Opponents/Chin/kicking/chin_61R.png"), pygame.image.load("images/Opponents/Chin/kicking/chin_61R.png"), pygame.image.load("images/Opponents/Chin/kicking/chin_62R.png"), pygame.image.load("images/Opponents/Chin/kicking/chin_63R.png"), pygame.image.load("images/Opponents/Chin/kicking/chin_64R.png"), pygame.image.load("images/Opponents/Chin/kicking/chin_64R.png"), pygame.image.load("images/Opponents/Chin/kicking/chin_64R.png"), pygame.image.load("images/Opponents/Chin/kicking/chin_64R.png")]
        self.punchingImagesLeft = [pygame.image.load("images/Opponents/Chin/punching/chin_50L.png"), pygame.image.load("images/Opponents/Chin/punching/chin_50L.png"), pygame.image.load("images/Opponents/Chin/punching/chin_51L.png"), pygame.image.load("images/Opponents/Chin/punching/chin_52L.png"), pygame.image.load("images/Opponents/Chin/punching/chin_53L.png"), pygame.image.load("images/Opponents/Chin/punching/chin_53L.png"), pygame.image.load("images/Opponents/Chin/punching/chin_53L.png"), pygame.image.load("images/Opponents/Chin/punching/chin_53L.png")]
        self.punchingImagesRight = [pygame.image.load("images/Opponents/Chin/punching/chin_50R.png"), pygame.image.load("images/Opponents/Chin/punching/chin_50R.png"), pygame.image.load("images/Opponents/Chin/punching/chin_51R.png"), pygame.image.load("images/Opponents/Chin/punching/chin_52R.png"), pygame.image.load("images/Opponents/Chin/punching/chin_53R.png"), pygame.image.load("images/Opponents/Chin/punching/chin_53R.png"), pygame.image.load("images/Opponents/Chin/punching/chin_53R.png"), pygame.image.load("images/Opponents/Chin/punching/chin_53R.png")]
        self.jumpingImagesLeft = [pygame.image.load("images/Opponents/Chin/jumping/chin_22L.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_23L.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_24L.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_25L.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_26L.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_27L.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_28L.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_29L.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_30L.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_31L.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_32L.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_33L.png")]
        self.jumpingImagesRight = [pygame.image.load("images/Opponents/Chin/jumping/chin_22R.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_23R.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_24R.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_25R.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_26R.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_27R.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_28R.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_29R.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_30R.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_31R.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_32R.png"), pygame.image.load("images/Opponents/Chin/jumping/chin_33R.png")]
        self.specialMoveImagesLeft = [pygame.image.load("images/Opponents/Chin/special move/chin_89L.png"), pygame.image.load("images/Opponents/Chin/special move/chin_90L.png"), pygame.image.load("images/Opponents/Chin/special move/chin_91L.png"), pygame.image.load("images/Opponents/Chin/special move/chin_92L.png"), pygame.image.load("images/Opponents/Chin/special move/chin_93L.png"), pygame.image.load("images/Opponents/Chin/special move/chin_94L.png")]
        self.specialMoveImagesRight = [pygame.image.load("images/Opponents/Chin/special move/chin_89R.png"), pygame.image.load("images/Opponents/Chin/special move/chin_90R.png"), pygame.image.load("images/Opponents/Chin/special move/chin_91R.png"), pygame.image.load("images/Opponents/Chin/special move/chin_92R.png"), pygame.image.load("images/Opponents/Chin/special move/chin_93R.png"), pygame.image.load("images/Opponents/Chin/special move/chin_94R.png")]
        self.stillImage = [self.standingImagesLeft[0]]
        self.upsideDown = [pygame.image.load("images/Opponents/Chin/standing/chin_0U.png")]
        self.deadImage = [pygame.image.load("images/Opponents/Chin/dead/chin_215L.png")]


class Duo(Character):
    def __init__(self, velocity, xCoord, yCoord, facing, height, width, health):
        super().__init__(velocity, xCoord, yCoord, facing, height, width, health)

        self.standingImagesLeft = [pygame.image.load("images/Opponents/Duo/standing/duo_0L.png"), pygame.image.load("images/Opponents/Duo/standing/duo_1L.png"), pygame.image.load("images/Opponents/Duo/standing/duo_2L.png"), pygame.image.load("images/Opponents/Duo/standing/duo_3L.png"), pygame.image.load("images/Opponents/Duo/standing/duo_4L.png"), pygame.image.load("images/Opponents/Duo/standing/duo_5L.png"), pygame.image.load("images/Opponents/Duo/standing/duo_6L.png"), pygame.image.load("images/Opponents/Duo/standing/duo_7L.png")]
        self.standingImagesRight = [pygame.image.load("images/Opponents/Duo/standing/duo_0R.png"), pygame.image.load("images/Opponents/Duo/standing/duo_1R.png"), pygame.image.load("images/Opponents/Duo/standing/duo_2R.png"), pygame.image.load("images/Opponents/Duo/standing/duo_3R.png"), pygame.image.load("images/Opponents/Duo/standing/duo_4R.png"), pygame.image.load("images/Opponents/Duo/standing/duo_5R.png"), pygame.image.load("images/Opponents/Duo/standing/duo_6R.png"), pygame.image.load("images/Opponents/Duo/standing/duo_7R.png")]
        self.walkingImagesLeft = [pygame.image.load("images/Opponents/Duo/walking/duo_53L.png"), pygame.image.load("images/Opponents/Duo/walking/duo_54L.png"), pygame.image.load("images/Opponents/Duo/walking/duo_55L.png"), pygame.image.load("images/Opponents/Duo/walking/duo_56L.png"), pygame.image.load("images/Opponents/Duo/walking/duo_57L.png"), pygame.image.load("images/Opponents/Duo/walking/duo_58L.png")]
        self.walkingImagesRight = [pygame.image.load("images/Opponents/Duo/walking/duo_53R.png"), pygame.image.load("images/Opponents/Duo/walking/duo_54R.png"), pygame.image.load("images/Opponents/Duo/walking/duo_55R.png"), pygame.image.load("images/Opponents/Duo/walking/duo_56R.png"), pygame.image.load("images/Opponents/Duo/walking/duo_57R.png"), pygame.image.load("images/Opponents/Duo/walking/duo_58R.png")]
        self.blockingImagesLeft = [pygame.image.load("images/Opponents/Duo/blocking/duo_452L.png"), pygame.image.load("images/Opponents/Duo/blocking/duo_453L.png"), pygame.image.load("images/Opponents/Duo/blocking/duo_454L.png"), pygame.image.load("images/Opponents/Duo/blocking/duo_455L.png"), pygame.image.load("images/Opponents/Duo/blocking/duo_456L.png")]
        self.blockingImagesRight = [pygame.image.load("images/Opponents/Duo/blocking/duo_452R.png"), pygame.image.load("images/Opponents/Duo/blocking/duo_453R.png"), pygame.image.load("images/Opponents/Duo/blocking/duo_454R.png"), pygame.image.load("images/Opponents/Duo/blocking/duo_455R.png"), pygame.image.load("images/Opponents/Duo/blocking/duo_456R.png")]
        self.kickingImagesLeft = [pygame.image.load("images/Opponents/Duo/kicking/duo_146L.png"), pygame.image.load("images/Opponents/Duo/kicking/duo_147L.png"), pygame.image.load("images/Opponents/Duo/kicking/duo_148L.png"), pygame.image.load("images/Opponents/Duo/kicking/duo_149L.png"), pygame.image.load("images/Opponents/Duo/kicking/duo_150L.png"), pygame.image.load("images/Opponents/Duo/kicking/duo_151L.png")]
        self.kickingImagesRight = [pygame.image.load("images/Opponents/Duo/kicking/duo_146R.png"), pygame.image.load("images/Opponents/Duo/kicking/duo_147R.png"), pygame.image.load("images/Opponents/Duo/kicking/duo_148R.png"), pygame.image.load("images/Opponents/Duo/kicking/duo_149R.png"), pygame.image.load("images/Opponents/Duo/kicking/duo_150R.png"), pygame.image.load("images/Opponents/Duo/kicking/duo_151R.png")]
        self.punchingImagesLeft = [pygame.image.load("images/Opponents/Duo/punching/duo_160L.png"), pygame.image.load("images/Opponents/Duo/punching/duo_161L.png"), pygame.image.load("images/Opponents/Duo/punching/duo_162L.png"), pygame.image.load("images/Opponents/Duo/punching/duo_163L.png"), pygame.image.load("images/Opponents/Duo/punching/duo_164L.png"), pygame.image.load("images/Opponents/Duo/punching/duo_165L.png"), pygame.image.load("images/Opponents/Duo/punching/duo_166L.png"), pygame.image.load("images/Opponents/Duo/punching/duo_167L.png"), pygame.image.load("images/Opponents/Duo/punching/duo_168L.png"), pygame.image.load("images/Opponents/Duo/punching/duo_169L.png"), pygame.image.load("images/Opponents/Duo/punching/duo_170L.png"), pygame.image.load("images/Opponents/Duo/punching/duo_171L.png")]
        self.punchingImagesRight = [pygame.image.load("images/Opponents/Duo/punching/duo_160R.png"), pygame.image.load("images/Opponents/Duo/punching/duo_161R.png"), pygame.image.load("images/Opponents/Duo/punching/duo_162R.png"), pygame.image.load("images/Opponents/Duo/punching/duo_163R.png"), pygame.image.load("images/Opponents/Duo/punching/duo_164R.png"), pygame.image.load("images/Opponents/Duo/punching/duo_165R.png"), pygame.image.load("images/Opponents/Duo/punching/duo_166R.png"), pygame.image.load("images/Opponents/Duo/punching/duo_167R.png"), pygame.image.load("images/Opponents/Duo/punching/duo_168R.png"), pygame.image.load("images/Opponents/Duo/punching/duo_169R.png"), pygame.image.load("images/Opponents/Duo/punching/duo_170R.png"), pygame.image.load("images/Opponents/Duo/punching/duo_171R.png")]
        self.jumpingImagesLeft = [pygame.image.load("images/Opponents/Duo/jumping/duo_24L.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_25L.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_26L.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_27L.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_28L.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_29L.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_30L.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_31L.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_32L.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_33L.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_34L.png")]
        self.jumpingImagesRight = [pygame.image.load("images/Opponents/Duo/jumping/duo_24R.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_25R.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_26R.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_27R.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_28R.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_29R.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_30R.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_31R.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_32R.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_33R.png"), pygame.image.load("images/Opponents/Duo/jumping/duo_34R.png")]
        self.specialMoveImagesLeft = [pygame.image.load("images/Opponents/Duo/special move/duo_201L.png"), pygame.image.load("images/Opponents/Duo/special move/duo_202L.png"), pygame.image.load("images/Opponents/Duo/special move/duo_203L.png"), pygame.image.load("images/Opponents/Duo/special move/duo_204L.png"), pygame.image.load("images/Opponents/Duo/special move/duo_205L.png"), pygame.image.load("images/Opponents/Duo/special move/duo_206L.png"), pygame.image.load("images/Opponents/Duo/special move/duo_207L.png"), pygame.image.load("images/Opponents/Duo/special move/duo_208L.png"), pygame.image.load("images/Opponents/Duo/special move/duo_209L.png"), pygame.image.load("images/Opponents/Duo/special move/duo_210L.png"), pygame.image.load("images/Opponents/Duo/special move/duo_211L.png"), pygame.image.load("images/Opponents/Duo/special move/duo_212L.png"), pygame.image.load("images/Opponents/Duo/special move/duo_213L.png"), pygame.image.load("images/Opponents/Duo/special move/duo_214L.png"), pygame.image.load("images/Opponents/Duo/special move/duo_215L.png"), pygame.image.load("images/Opponents/Duo/special move/duo_216L.png"), pygame.image.load("images/Opponents/Duo/special move/duo_217L.png"), pygame.image.load("images/Opponents/Duo/special move/duo_218L.png"), pygame.image.load("images/Opponents/Duo/special move/duo_219L.png")]
        self.specialMoveImagesRight = [pygame.image.load("images/Opponents/Duo/special move/duo_201R.png"), pygame.image.load("images/Opponents/Duo/special move/duo_202R.png"), pygame.image.load("images/Opponents/Duo/special move/duo_203R.png"), pygame.image.load("images/Opponents/Duo/special move/duo_204R.png"), pygame.image.load("images/Opponents/Duo/special move/duo_205R.png"), pygame.image.load("images/Opponents/Duo/special move/duo_206R.png"), pygame.image.load("images/Opponents/Duo/special move/duo_207R.png"), pygame.image.load("images/Opponents/Duo/special move/duo_208R.png"), pygame.image.load("images/Opponents/Duo/special move/duo_209R.png"), pygame.image.load("images/Opponents/Duo/special move/duo_210R.png"), pygame.image.load("images/Opponents/Duo/special move/duo_211R.png"), pygame.image.load("images/Opponents/Duo/special move/duo_212R.png"), pygame.image.load("images/Opponents/Duo/special move/duo_213R.png"), pygame.image.load("images/Opponents/Duo/special move/duo_214R.png"), pygame.image.load("images/Opponents/Duo/special move/duo_215R.png"), pygame.image.load("images/Opponents/Duo/special move/duo_216R.png"), pygame.image.load("images/Opponents/Duo/special move/duo_217R.png"), pygame.image.load("images/Opponents/Duo/special move/duo_218R.png"), pygame.image.load("images/Opponents/Duo/special move/duo_219R.png")]
        self.stillImage = [self.standingImagesLeft[0]]
        self.upsideDown = [pygame.image.load("images/Opponents/Duo/standing/duo_0U.png")]
        self.deadImage = [pygame.image.load("images/Opponents/Duo/dead/duo_468L.png")]

class Tung(Character):
    def __init__(self, velocity, xCoord, yCoord, facing, height, width, health):
        super().__init__(velocity, xCoord, yCoord, facing, height, width, health)
        
        self.standingImagesLeft = [pygame.image.load("images/Opponents/Tung/standing/tung_0L.png"), pygame.image.load("images/Opponents/Tung/standing/tung_1L.png"), pygame.image.load("images/Opponents/Tung/standing/tung_2L.png"), pygame.image.load("images/Opponents/Tung/standing/tung_3L.png"), pygame.image.load("images/Opponents/Tung/standing/tung_4L.png"), pygame.image.load("images/Opponents/Tung/standing/tung_5L.png")]
        self.standingImagesRight = [pygame.image.load("images/Opponents/Tung/standing/tung_0R.png"), pygame.image.load("images/Opponents/Tung/standing/tung_1R.png"), pygame.image.load("images/Opponents/Tung/standing/tung_2R.png"), pygame.image.load("images/Opponents/Tung/standing/tung_3R.png"), pygame.image.load("images/Opponents/Tung/standing/tung_4R.png"), pygame.image.load("images/Opponents/Tung/standing/tung_5R.png")]
        self.walkingImagesLeft = [pygame.image.load("images/Opponents/Tung/walking/tung_13L.png"), pygame.image.load("images/Opponents/Tung/walking/tung_14L.png"), pygame.image.load("images/Opponents/Tung/walking/tung_15L.png"), pygame.image.load("images/Opponents/Tung/walking/tung_16L.png"), pygame.image.load("images/Opponents/Tung/walking/tung_17L.png"), pygame.image.load("images/Opponents/Tung/walking/tung_18L.png"), pygame.image.load("images/Opponents/Tung/walking/tung_19L.png")]
        self.walkingImagesRight = [pygame.image.load("images/Opponents/Tung/walking/tung_13R.png"), pygame.image.load("images/Opponents/Tung/walking/tung_14R.png"), pygame.image.load("images/Opponents/Tung/walking/tung_15R.png"), pygame.image.load("images/Opponents/Tung/walking/tung_16R.png"), pygame.image.load("images/Opponents/Tung/walking/tung_17R.png"), pygame.image.load("images/Opponents/Tung/walking/tung_18R.png"), pygame.image.load("images/Opponents/Tung/walking/tung_19R.png")]
        self.blockingImagesLeft = [pygame.image.load("images/Opponents/Tung/blocking/tung_65L.png"), pygame.image.load("images/Opponents/Tung/blocking/tung_66L.png"), pygame.image.load("images/Opponents/Tung/blocking/tung_67L.png"), pygame.image.load("images/Opponents/Tung/blocking/tung_68L.png"), pygame.image.load("images/Opponents/Tung/blocking/tung_69L.png"), pygame.image.load("images/Opponents/Tung/blocking/tung_70L.png"), pygame.image.load("images/Opponents/Tung/blocking/tung_71L.png")]
        self.blockingImagesRight = [pygame.image.load("images/Opponents/Tung/blocking/tung_65R.png"), pygame.image.load("images/Opponents/Tung/blocking/tung_66R.png"), pygame.image.load("images/Opponents/Tung/blocking/tung_67R.png"), pygame.image.load("images/Opponents/Tung/blocking/tung_68R.png"), pygame.image.load("images/Opponents/Tung/blocking/tung_69R.png"), pygame.image.load("images/Opponents/Tung/blocking/tung_70R.png"), pygame.image.load("images/Opponents/Tung/blocking/tung_71R.png")]
        self.kickingImagesLeft = [pygame.image.load("images/Opponents/Tung/kicking/tung_152L.png"), pygame.image.load("images/Opponents/Tung/kicking/tung_159L.png"), pygame.image.load("images/Opponents/Tung/kicking/tung_160L.png"), pygame.image.load("images/Opponents/Tung/kicking/tung_161L.png"), pygame.image.load("images/Opponents/Tung/kicking/tung_162L.png")]
        self.kickingImagesRight = [pygame.image.load("images/Opponents/Tung/kicking/tung_152R.png"), pygame.image.load("images/Opponents/Tung/kicking/tung_159R.png"), pygame.image.load("images/Opponents/Tung/kicking/tung_160R.png"), pygame.image.load("images/Opponents/Tung/kicking/tung_161R.png"), pygame.image.load("images/Opponents/Tung/kicking/tung_162R.png")]
        self.punchingImagesLeft = [pygame.image.load("images/Opponents/Tung/punching/tung_127L.png"), pygame.image.load("images/Opponents/Tung/punching/tung_128L.png"), pygame.image.load("images/Opponents/Tung/punching/tung_129L.png"), pygame.image.load("images/Opponents/Tung/punching/tung_130L.png"), pygame.image.load("images/Opponents/Tung/punching/tung_131L.png"), pygame.image.load("images/Opponents/Tung/punching/tung_132L.png"), pygame.image.load("images/Opponents/Tung/punching/tung_133L.png"), pygame.image.load("images/Opponents/Tung/punching/tung_134L.png"), pygame.image.load("images/Opponents/Tung/punching/tung_135L.png")]
        self.punchingImagesRight = [pygame.image.load("images/Opponents/Tung/punching/tung_127R.png"), pygame.image.load("images/Opponents/Tung/punching/tung_128R.png"), pygame.image.load("images/Opponents/Tung/punching/tung_129R.png"), pygame.image.load("images/Opponents/Tung/punching/tung_130R.png"), pygame.image.load("images/Opponents/Tung/punching/tung_131R.png"), pygame.image.load("images/Opponents/Tung/punching/tung_132R.png"), pygame.image.load("images/Opponents/Tung/punching/tung_133R.png"), pygame.image.load("images/Opponents/Tung/punching/tung_134R.png"), pygame.image.load("images/Opponents/Tung/punching/tung_135R.png")]
        self.jumpingImagesLeft = [pygame.image.load("images/Opponents/Tung/jumping/tung_153L.png"), pygame.image.load("images/Opponents/Tung/jumping/tung_154L.png"), pygame.image.load("images/Opponents/Tung/jumping/tung_155L.png"), pygame.image.load("images/Opponents/Tung/jumping/tung_156L.png"), pygame.image.load("images/Opponents/Tung/jumping/tung_157L.png"), pygame.image.load("images/Opponents/Tung/jumping/tung_158L.png")]
        self.jumpingImagesRight = [pygame.image.load("images/Opponents/Tung/jumping/tung_153R.png"), pygame.image.load("images/Opponents/Tung/jumping/tung_154R.png"), pygame.image.load("images/Opponents/Tung/jumping/tung_155R.png"), pygame.image.load("images/Opponents/Tung/jumping/tung_156R.png"), pygame.image.load("images/Opponents/Tung/jumping/tung_157R.png"), pygame.image.load("images/Opponents/Tung/jumping/tung_158R.png")]
        self.specialMoveImagesLeft = [pygame.image.load("images/Opponents/Tung/special move/tung_217L.png"), pygame.image.load("images/Opponents/Tung/special move/tung_218L.png"), pygame.image.load("images/Opponents/Tung/special move/tung_219L.png"), pygame.image.load("images/Opponents/Tung/special move/tung_220L.png"), pygame.image.load("images/Opponents/Tung/special move/tung_221L.png"), pygame.image.load("images/Opponents/Tung/special move/tung_222L.png"), pygame.image.load("images/Opponents/Tung/special move/tung_223L.png"), pygame.image.load("images/Opponents/Tung/special move/tung_224L.png"), pygame.image.load("images/Opponents/Tung/special move/tung_225L.png")]
        self.specialMoveImagesRight = [pygame.image.load("images/Opponents/Tung/special move/tung_217R.png"), pygame.image.load("images/Opponents/Tung/special move/tung_218R.png"), pygame.image.load("images/Opponents/Tung/special move/tung_219R.png"), pygame.image.load("images/Opponents/Tung/special move/tung_220R.png"), pygame.image.load("images/Opponents/Tung/special move/tung_221R.png"), pygame.image.load("images/Opponents/Tung/special move/tung_222R.png"), pygame.image.load("images/Opponents/Tung/special move/tung_223R.png"), pygame.image.load("images/Opponents/Tung/special move/tung_224R.png"), pygame.image.load("images/Opponents/Tung/special move/tung_225R.png")]
        self.stillImage = [self.standingImagesLeft[0]]
        self.upsideDown = [pygame.image.load("images/Opponents/Tung/standing/tung_0U.png")]
        self.deadImage = [pygame.image.load("images/Opponents/Tung/dead/tung_112L.png")]


class Fireball():
    def __init__(self):
        self.fireballCount = 0
        self.is_fireball = False
        self.xCoord = 0
        self.yCoord = 200
        self.height = 60
        self.fireballImagesLeft = [pygame.image.load("images/Characters/eiji_2/special move/eiji_208L.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_209L.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_210L.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_211L.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_212L.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_213L.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_214L.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_215L.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_216L.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_217L.png")]
        self.fireballImagesRight = [pygame.image.load("images/Characters/eiji_2/special move/eiji_208R.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_209R.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_210R.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_211R.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_212R.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_213R.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_214R.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_215R.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_216R.png"), pygame.image.load("images/Characters/eiji_2/special move/eiji_217R.png")]

    def is_fireball_collision(self, target):
        if target.facing == 'right':
            xDistance = (self.xCoord - target.xCoord - (target.height - self.height))**2
        if target.facing == "left":
            xDistance = (self.xCoord - target.xCoord)**2

        yDistance = (self.yCoord - target.yCoord)**2
        absWidth = 70

        collisionPoint = math.sqrt(xDistance + yDistance)

        if collisionPoint < absWidth:
            return True
        else:
            return False

    def fireballAnimation(self, game, characterName, enemyName):
        if characterName.eijiSM and characterName.playersmBarCount == 5:
            is_colliding = self.is_fireball_collision(enemyName)

            if is_colliding:
                self.is_fireball = False
                characterName.eijiSM = False
            if (self.xCoord >= 460 or self.xCoord <= 0): 
                    self.is_fireball = False
                    characterName.eijiSM = False
            if not is_colliding and not (self.xCoord >= 460 or self.xCoord <= 0):
                self.is_fireball = True 

        if self.is_fireball:
            if characterName.facing == "right":
                self.xCoord += 8
                if self.fireballCount == len(self.fireballImagesRight)*6:
                    self.fireballCount = 54
                    game.window.blit(self.fireballImagesRight[self.fireballCount//6], (self.xCoord + 15, self.yCoord))
                else:
                    game.window.blit(self.fireballImagesRight[self.fireballCount//6], (self.xCoord + 15, self.yCoord))
                    self.fireballCount += 1 

            if characterName.facing == "left":
                self.xCoord -= 8
                if self.fireballCount == len(self.fireballImagesLeft)*6:
                    self.fireballCount = 54
                    game.window.blit(self.fireballImagesLeft[self.fireballCount//6], (self.xCoord + 15, self.yCoord))
                else:
                    game.window.blit(self.fireballImagesLeft[self.fireballCount//6], (self.xCoord + 15, self.yCoord))
                    self.fireballCount += 1 

        if not self.is_fireball:
            characterName.playersmBarCount = 0

class Obstacle():
    def __init__(self, xCoord, yCoord, height, width, health):
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.height = height
        self.width = width    

        self.obstacleUp = True
        self.obstacleDown = False
        self.obstacleDying = False
        self.obstacleDead = False  

    def obstacleAnimation(self, obstacleImageUp, obstacleImageDown, obstacleDyingImage, obstacleDeadImage, game):

        if self.obstacleUp:
            game.window.blit(obstacleImageUp, (self.xCoord, self.yCoord)) 

        elif self.obstacleDown:
            game.window.blit(obstacleImageDown, (self.xCoord, self.yCoord))
        
        if self.obstacleDying:
            game.window.blit(obstacleDyingImage, (self.xCoord, self.yCoord)) 

        if self.obstacleDead:
            game.window.blit(obstacleDeadImage, (self.xCoord, self.yCoord)) 

            
class Bin(Obstacle):
    def __init__(self, xCoord, yCoord, height, width, health):
        super().__init__(xCoord, yCoord, height, width, health)

        self.health = health

        self.dustBinUp = pygame.image.load("images/Obstacles/dustbin.png")
        self.dustBinDown = pygame.image.load("images/Obstacles/dustbinDown.png")
        self.dustbinDying = pygame.image.load("images/Obstacles/dustbinDying.png")
        self.dustbinDead = pygame.image.load("images/Obstacles/dustbinDead.png")

class Box(Obstacle):
    def __init__(self, xCoord, yCoord, height, width, health):
        super().__init__(xCoord, yCoord, height, width, health)

        self.health = health
        
        self.boxUp = pygame.image.load("images/Obstacles/box.png")
        self.boxDown = pygame.image.load("images/Obstacles/box.png")
        self.boxDying = pygame.image.load("images/Obstacles/boxDying.png")
        self.boxDead = pygame.image.load("images/Obstacles/boxDead.png")
