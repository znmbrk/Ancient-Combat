import pygame, sprites, datetime, database, os

class GameComponents():
    def __init__(self):

        # Datetime
        self.now = datetime.datetime.now()
        self.year = "Current year: %d" % self.now.year
        self.month = "Current month: %d" % self.now.month
        self.day = "Current day: %d" % self.now.day
        self.date = self.now.strftime("%d-%m-%Y")

        # Setting the window and frames
        pygame.init()
        pygame.display.set_caption("Ancient Combat")
        self.window = pygame.display.set_mode((600, 380))
        self.clock = pygame.time.Clock() 
        self.font = pygame.font.SysFont("Arial", 32)
        self.scoreFont = pygame.font.SysFont("lazy-ride-sans-regular.ttf", 92)
        self.entry = ""
        self.rect = pygame.Rect(188, 163, 232, 35)
        self.isTextActive = False

        # Setter
        self.playGame = True
        self.soundEffects = "sound_on"
        self.gameControl = "controls_wasd"
        self.gameSpeed = 1
        self.gameAnnotation = "screen_annotation_on"
        self.result = ""

        self.bgCount = 0
        self.bgMoving = False
        self.tempTimer = 0
        self.timer = 0

        self.onlyOnce = False

    def dyingTimer(self):
        self.deathTempTimer = 0
        self.deathTimer = 0

    def winningTimer(self):
        self.wonTempTimer = 0
        self.wonTimer = 0
    
    def playBgMusic(self):
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/guile.wav")
        pygame.mixer.music.play(-1, 0, 13000)

    def playLevel1Music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/scary.wav")
        pygame.mixer.music.play(-1, 0, 1)

    def stopMusic(self):
        pygame.mixer.music.fadeout(4500)

game = GameComponents()

class Screens():
    # Constructor Method
    def __init__(self):
        self.screenStatus = "splash"
        self.currentChar = "player"
        
        # Loading background images:
        self.bgimages = [pygame.image.load("images/Screens/Backgrounds/{}.png".format(i)).convert_alpha() for i in ["game_over", "splash_screen", "menu", "instructions", "highscores", "settings", "character_select", "level_1", "ask_name", "game_won"]]
        
        # Store all the loaded buttons for the menu and settings screens
        self.menuButtons = [pygame.image.load("images/Screens/Menu/{}.png".format(i)).convert_alpha() for i in ["start_down",  "glow", "instructions_down", "highscore_down", "settings_down", "exit_down"]]
        self.ySelectorMenu = 115

        self.settingsButtonsText = [i for i in ["sound_on", "sound_off", "controls_wasd", "controls_arrows", "speed_slow", "speed_medium", "speed_fast", "screen_annotation_on", "screen_annotation_off", "glow"]]
        self.settings_buttons = [pygame.image.load("images/Screens/Settings/{}.png".format(i)).convert_alpha() for i in ["sound_on", "sound_off", "controls_wasd", "controls_arrows", "speed_slow", "speed_medium", "speed_fast", "screen_annotation_on", "screen_annotation_off", "glow"]]
        self.ySelectorSettings = 115      
        
        self.optionChosenSounds = 0  
        self.settingIndexSounds = 0
        self.selectedSound = self.settingsButtonsText[self.optionChosenSounds]

        self.optionChosenControls = 2
        self.settingIndexControls = 0
        self.selectedControl = self.settingsButtonsText[self.optionChosenControls]

        self.optionChosenSpeed = 5
        self.settingIndexSpeed = 0
        self.selectedSpeed = self.settingsButtonsText[self.optionChosenSpeed]
        
        self.optionChosenAnnotation = 7
        self.settingIndexAnnotation = 0
        self.selectedAnnotation = self.settingsButtonsText[self.optionChosenAnnotation]


        # Storing highscore page subtitles
        self.highscoreSubtitles = [pygame.image.load("images/Screens/Highscores/{}.png".format(i)).convert_alpha() for i in ["rank", "date", "name", "score"]]

        # Character select image
        self.characterSelectArrow = pygame.image.load("images/Screens/Character Select/{}.png".format("arrow")).convert_alpha()
        self.yCharacterSelect = 110

        # Health bar images
        self.playerHealthbar = [pygame.image.load("images/Characters/{}.png".format(i)).convert_alpha() for i in ["healthbar0", "healthbar1", "healthbar2", "healthbar3", "healthbar4", "healthbar5", "healthbar6", "healthbar7", "healthbar8", "healthbar9", "healthbar10"]]
        self.enemyHealthbar = [pygame.image.load("images/Opponents/{}.png".format(i)).convert_alpha() for i in ["enemyHealthbar0", "enemyHealthbar1", "enemyHealthbar2", "enemyHealthbar3", "enemyHealthbar4", "enemyHealthbar5", "enemyHealthbar6", "enemyHealthbar7", "enemyHealthbar8", "enemyHealthbar9", "enemyHealthbar10"]]

        # Special move bar images
        self.playersmBar = [pygame.image.load("images/Characters/{}.png".format(i)).convert_alpha() for i in ["smBar0", "smBar1", "smBar2", "smBar3", "smBar4", "smBar5"]]
        self.enemysmBar = [pygame.image.load("images/Opponents/{}.png".format(i)).convert_alpha() for i in ["EnemysmBar0", "EnemysmBar1", "EnemysmBar2", "EnemysmBar3", "EnemysmBar4", "EnemysmBar5"]]
        
        # Other images
        self.advancingArrow = pygame.image.load("images/Screens/Backgrounds/advance.png").convert_alpha()

    # Displaying Screens Methods:
    def splashDisplay(self):
        # game.playBgMusic()
        game.window.blit(self.bgimages[1], (0,20))

    # Menu screen
    def menuDisplay(self):
        game.window.blit(self.bgimages[2], (-25,-30))
        game.window.blit(self.menuButtons[0], (205,120))
        game.window.blit(self.menuButtons[1], (163,self.ySelectorMenu))
        game.window.blit(self.menuButtons[2], (200,165))
        game.window.blit(self.menuButtons[3], (183,215))
        game.window.blit(self.menuButtons[4], (240,265))
        game.window.blit(self.menuButtons[5], (273,315))

    # Menu screen button change
    def buttonSelectMenu(self, yCoord, end_point):
        if keys[pygame.K_s]:
            game.clock.tick(5)
            self.ySelectorMenu += yCoord
            if self.ySelectorMenu >= end_point:
                self.ySelectorMenu = end_point
        elif keys[pygame.K_w]:
            game.clock.tick(5)
            self.ySelectorMenu -= yCoord
            if self.ySelectorMenu <= 115:
                self.ySelectorMenu = 115
        if keys[pygame.K_RETURN] and self.screenStatus == "menu":
            self.screenStatus = {115: "character select", 165: "instructions", 215: "highscores", 265: "settings", 315: "exit"}[self.ySelectorMenu]
        if self.screenStatus == "exit":
            game.playGame = False

    # Settings screen
    def settingsDisplay(self):
        game.window.blit(self.bgimages[5], (-7,10))
        game.window.blit(self.settings_buttons[self.optionChosenSounds], (182,120))
        game.window.blit(self.settings_buttons[self.optionChosenControls], (190,165))
        game.window.blit(self.settings_buttons[self.optionChosenSpeed], (165,215))
        game.window.blit(self.settings_buttons[self.optionChosenAnnotation], (135,265))
        game.window.blit(self.settings_buttons[-1], (118,self.ySelectorSettings))

    # Settings screen button change
    def buttonSelectSettings(self, yCoord, end_point):
        if keys[pygame.K_s]:
            game.clock.tick(4)
            self.ySelectorSettings += yCoord
            if self.ySelectorSettings >= end_point:
                self.ySelectorSettings = end_point
                
        elif keys[pygame.K_w]:
            game.clock.tick(4)
            self.ySelectorSettings -= yCoord
            if self.ySelectorSettings <= 115:
                self.ySelectorSettings = 115
            
        elif keys[pygame.K_SPACE] and self.screenStatus == "settings":
            self.settingCoords = {115: [0,1], 165: [2,3], 215: [4,5,6], 265: [7,8]}
            game.clock.tick(4)
            
            if self.ySelectorSettings == 115:
                self.settingIndexSounds +=1
                if self.settingIndexSounds >1:
                    self.settingIndexSounds = 0
                self.optionChosenSounds = self.settingCoords[115][self.settingIndexSounds]
                self.selectedSound = self.settingsButtonsText[self.optionChosenSounds]

            if self.selectedSound == "sound_on":
                game.playBgMusic()
            elif self.selectedSound == "sound_off":
                game.stopMusic()

            if self.ySelectorSettings == 165:
                self.settingIndexControls +=1
                if self.settingIndexControls >1:
                    self.settingIndexControls = 0
                self.optionChosenControls= self.settingCoords[165][self.settingIndexControls]
                self.selectedControl = self.settingsButtonsText[self.optionChosenControls]

            if self.ySelectorSettings == 215:
                self.settingIndexSpeed +=1
                if self.settingIndexSpeed >2:
                    self.settingIndexSpeed = 0
                self.optionChosenSpeed = self.settingCoords[215][self.settingIndexSpeed]
                self.selectedSpeed = self.settingsButtonsText[self.optionChosenSpeed]

            # Game speed code
            if self.selectedSpeed == "speed_slow":
                game.gameSpeed = 0.5
            elif self.selectedSpeed == "speed_medium":
                game.gameSpeed = 1
            elif self.selectedSpeed == "speed_fast":
                game.gameSpeed = 2

            if self.ySelectorSettings == 265:
                self.settingIndexAnnotation +=1
                if self.settingIndexAnnotation >1:
                    self.settingIndexAnnotation = 0
                self.optionChosenAnnotation= self.settingCoords[265][self.settingIndexAnnotation]
                self.selectedAnnotation = self.settingsButtonsText[self.optionChosenAnnotation]

    def instructionsDisplay(self):
        game.window.blit(self.bgimages[3], (0,10))

    def highscoresDisplay(self):
        game.window.blit(self.bgimages[4], (-15,10))
        x = 75
        for subtitle in self.highscoreSubtitles:
            x += 80
            game.window.blit(subtitle, (x,110))

        dataY = 150
        rank = 1

        users = database.sortByScore()
        for user in users:
            userData = "{}   {}   {}".format(user.date, user.name, user.score)
            displayData = game.font.render(userData, True, (0,0,0))
            game.window.blit(displayData, (205, dataY))
            displayRank = game.font.render(str(rank), True, (0,0,0))
            game.window.blit(displayRank, (170, dataY))
            dataY += 38
            rank += 1

    def characterSelectDisplay(self):
        game.window.blit(self.bgimages[6], (-5,12))
        self.selectCharacterArrow()

    def selectCharacterArrow(self):

        if keys[pygame.K_s]:
            game.clock.tick(4)
            self.yCharacterSelect += 150
            if self.yCharacterSelect >= 260:
                self.yCharacterSelect = 260
                
        elif keys[pygame.K_w]:
            game.clock.tick(4)
            self.yCharacterSelect -= 150
            if self.yCharacterSelect <= 110:
                self.yCharacterSelect = 110

        if keys[pygame.K_SPACE] and self.screenStatus == "character select":
            game.clock.tick(4)
            if self.yCharacterSelect == 110:
                self.screenStatus = "ask_name"
                self.currentChar = "player"

            elif self.yCharacterSelect == 260:
                self.screenStatus = "ask_name"
                self.currentChar = "Eiji"

        game.window.blit(self.characterSelectArrow, (10, self.yCharacterSelect))

    def askName(self):
        game.timer = 0
        
    def askNameDisplay(self):
        game.window.blit(self.bgimages[8], (-18, 0))
        self.askName()

    def levelDisplay(self, playerXCoord, healthCount, enemyHealthCount, playersmBarCount, enemysmBarCount):
        game.window.blit(self.bgimages[7], (playerXCoord,0))
        game.window.blit(self.playerHealthbar[healthCount], (60, 30))
        game.window.blit(self.enemyHealthbar[enemyHealthCount], (340, 30))
        game.window.blit(self.playersmBar[playersmBarCount], (156, 50))
        game.window.blit(self.enemysmBar[enemysmBarCount], (425, 50))

    def gameOverDisplay(self):
        game.window.blit(self.bgimages[0], (-15, 0))

    def gameWonDisplay(self):
        game.window.blit(self.bgimages[9], (-20, 20))

    def advanceArrow(self):
        game.window.blit(self.advancingArrow, (450, 80))

screen = Screens()

# Sound effects for the two main characters
class PlayerSounds():

    tizocSounds = ["sounds/TizocSounds/" + i + ".wav" for i in ["punch", "kick", "block", "jump", "special", "hurt", "dead"]]
    eijiSounds = ["sounds/EijiSounds/" + i + ".wav" for i in ["punch", "kick", "block", "jump", "special", "hurt", "dead"]]

    def playOtherSounds(self, soundName):
        pygame.mixer.init()
        pygame.mixer.music.load(soundName)
        pygame.mixer.music.play(1)

    def stopOtherSounds(self):
        pygame.mixer.music.quit()

playerSounds = PlayerSounds()


# Instantiating the various sprites in my game
tizoc = sprites.Tizoc(5, 15, 180, "right", 128, 120, 100)
player = tizoc

eiji = sprites.Eiji(5, 30, 200, "right", 112, 80, 100)
chin = sprites.Chin(1.2, 500, 210, "left", 96, 64, 20)
duo = sprites.Duo(3, 1000, 210, "left", 120, 96, 20)
tung = sprites.Tung(2, 1000, 190, "left", 96, 96, 20)
dustbin = sprites.Bin(700, 215, 81, 60, 10)
box = sprites.Box(1100, 215, 66, 60, 10)
fireball = sprites.Fireball()

def playerMoves(enemyName):

    playerAnimation(player, enemyName)

    # Controls for the two main players
    if keys[pygame.K_w]:
        player.isIdle = False
        player.isJumping = True

        if player == tizoc:
            playerSounds.playOtherSounds(playerSounds.tizocSounds[3])
        else:
            playerSounds.playOtherSounds(playerSounds.eijiSounds[3])

    elif keys[pygame.K_d]:
        player.xCoord += player.velocity * game.gameSpeed

        player.isIdle = False
        player.isWalking = True
        player.facing = "right"
        player.isActive = True
        game.bgMoving = True
        
    elif keys[pygame.K_a]:
        player.xCoord -= player.velocity * game.gameSpeed

        player.isIdle = False 
        player.isWalking = True
        player.facing = "left"
        player.isActive = True
        game.bgMoving = True

    elif keys[pygame.K_s]:
        player.isIdle = False 
        player.isBlocking = True
        player.isActive = False
        game.bgMoving = False 

        if player == tizoc:
            playerSounds.playOtherSounds(playerSounds.tizocSounds[2])
        elif player == eiji:
            playerSounds.playOtherSounds(playerSounds.eijiSounds[2]) 
    
    elif keys[pygame.K_k]:
        player.isIdle = False 
        player.isKicking = True
        player.isActive = False
        game.bgMoving = False 

        if player == tizoc:
            if game.onlyOnce == False:
                playerSounds.playOtherSounds(playerSounds.tizocSounds[1])
                game.onlyOnce = True
        elif player == eiji:
            playerSounds.playOtherSounds(playerSounds.eijiSounds[1])

    elif keys[pygame.K_l]:
        player.isIdle = False 
        player.isPunching = True
        player.isActive = False
        game.bgMoving = False 

        if player == tizoc:
            playerSounds.playOtherSounds(playerSounds.tizocSounds[0])
        elif player == eiji:
            playerSounds.playOtherSounds(playerSounds.eijiSounds[0])
    
    elif keys[pygame.K_j]:
        player.eijiSM = True
        player.isIdle = False 
        player.isSpecialMove = True
        player.isActive = False
        game.bgMoving = False 

        if player == tizoc:
            playerSounds.playOtherSounds(playerSounds.tizocSounds[4])
        elif player == eiji:
            playerSounds.playOtherSounds(playerSounds.eijiSounds[4])  

def enemyAnimation(enemyName):
    enemyName.isIdle = False
    enemyName.isWalking = True

    if not enemyName.isDead:
        if player.xCoord > enemyName.xCoord:
            enemyName.xCoord += enemyName.velocity * game.gameSpeed
            enemyName.facing = "right"
        if player.xCoord < enemyName.xCoord:
            enemyName.xCoord -= enemyName.velocity * game.gameSpeed
            enemyName.facing = "left"

    collidingChinPlayer = is_collision(enemyName, player)

    if collidingChinPlayer:

        if player == tizoc:
            playerSounds.playOtherSounds(playerSounds.tizocSounds[2])
        else:
            playerSounds.playOtherSounds(playerSounds.eijiSounds[2])

        enemyName.isWalking = False
        enemyName.isIdle = True

        block = 12
        jump = 8
        idle = 1

        punch = 10
        kick = 5
        special = 1

        if player.isAttacking:
            if enemyName.numGenDefense >= block:
                enemyName.isBlocking = True
                enemyName.isIdle = False
            elif enemyName.numGenDefense >= jump:
                enemyName.isJumping = True
                enemyName.isIdle = False
            else:
                enemyName.isIdle = True

            if enemyName.facing == "right" and player.facing == "left":
                enemyName.xCoord -= 50
                player.xCoord += 2
            elif enemyName.facing == "left" and player.facing == "right":
                enemyName.xCoord += 50
                player.xCoord -= 2
            player.isAttacking = False

            if (player.isPunching or player.isKicking) and not (enemyName.isBlocking or enemyName.isJumping):
                enemyName.health -= 2
                player.playersmBarCount += 1
                player.playerPoints += 15
                if player.playersmBarCount >= 5:
                    player.playersmBarCount = 5
                if enemyName.health <= 0:
                    enemyName.health = 0
            
            elif player.isSpecialMove and not (enemyName.isBlocking or enemyName.isJumping):
                player.playerPoints += 25
                enemyName.health -= 6     
                if enemyName.health <= 0:
                    enemyName.health = 0                                                                                            

            if enemyName.health % 2 == 0:
                if enemyName.health == 20:
                    enemyName.enemyHealthCount = 0
                elif enemyName.health == 18:
                    enemyName.enemyHealthCount = 1
                elif enemyName.health == 16:
                    enemyName.enemyHealthCount = 2
                elif enemyName.health == 14:
                    enemyName.enemyHealthCount = 3
                elif enemyName.health == 12:
                    enemyName.enemyHealthCount = 4
                elif enemyName.health == 10:
                    enemyName.enemyHealthCount = 5
                elif enemyName.health == 8:
                    enemyName.enemyHealthCount = 6
                elif enemyName.health == 6:
                    enemyName.enemyHealthCount = 7
                elif enemyName.health == 4:
                    enemyName.enemyHealthCount = 8
                elif enemyName.health == 2:
                    enemyName.enemyHealthCount = 9
                elif enemyName.health == 0:
                    enemyName.enemyHealthCount = 10
                screen.levelDisplay(-game.bgCount, player.healthCount, enemyName.enemyHealthCount, player.playersmBarCount, enemyName.enemysmBarCount)

        if not player.isAttacking:
            if enemyName.numGenOffense >= punch:
                enemyName.isPunching = True
                enemyName.isIdle = False
            elif enemyName.numGenOffense >= kick - 1:
                enemyName.isKicking = True
                enemyName.isIdle = False
            else:
                if enemyName.enemysmBarCount == 5:
                    enemyName.isSpecialMove = True
                    enemyName.isIdle = False
                else: 
                    enemyName.isIdle = True

            if (enemyName.isPunching or enemyName.isKicking) and not (player.isBlocking or player.isJumping) and player.xCoord != 10:
                player.health -= 2
                enemyName.enemysmBarCount += 1 
                if enemyName.enemysmBarCount >= 5:
                    enemyName.enemysmBarCount = 5
                if player.health <= 0:
                    player.health = 0

                if player == tizoc:
                    playerSounds.playOtherSounds(playerSounds.tizocSounds[5])
                else:
                    playerSounds.playOtherSounds(playerSounds.eijiSounds[5])  

            elif enemyName.isSpecialMove and not (player.isBlocking or player.isJumping) and player.xCoord != 10:
                player.health -= 6     
                if player.health <= 0:
                    player.health = 0   

                if player == tizoc:
                    playerSounds.playOtherSounds(playerSounds.tizocSounds[5])
                else:
                    playerSounds.playOtherSounds(playerSounds.eijiSounds[5])                                                                                           

            if player.healthCount >= 10:
                player.healthCount = 10

            if player.health % 10 == 0 :
                if player.health == 100:
                    player.healthCount = 0
                elif player.health == 90:
                    player.healthCount = 1
                elif player.health == 80:
                    player.healthCount = 2
                elif player.health == 70:
                    player.healthCount = 3
                elif player.health == 60:
                    player.healthCount = 4
                elif player.health == 50:
                    player.healthCount = 5
                elif player.health == 40:
                    player.healthCount = 6
                elif player.health == 30:
                    player.healthCount = 7
                elif player.health == 20:
                    player.healthCount = 8
                elif player.health == 10:
                    player.healthCount = 9
                elif player.health == 0:
                    player.healthCount = 10
            screen.levelDisplay(-game.bgCount, player.healthCount, enemyName.enemyHealthCount, player.playersmBarCount, enemyName.enemysmBarCount)

            if player.isBlocking:
                player.playersmBarCount += 1
                if player.playersmBarCount >= 5:
                    player.playersmBarCount = 5 

    if not player.smHappening:      
        if enemyName.isSpecialMove and enemyName.enemysmBarCount == 5:
            enemyName.controllingCharacter(game, enemyName.specialMoveImagesLeft, enemyName.specialMoveImagesRight, None, 2)
            enemyName.isAttacking = True
            enemyName.enemysmBarCount = 0

        elif enemyName.isIdle:
            enemyName.controllingCharacter(game, enemyName.standingImagesLeft, enemyName.standingImagesRight, None, 2)
        elif enemyName.isDead:
            enemyName.controllingCharacter(game, enemyName.deadImage, enemyName.deadImage, None, 2)
            enemyName.isIdle = False
        elif enemyName.isWalking:
            enemyName.controllingCharacter(game, enemyName.walkingImagesLeft, enemyName.walkingImagesRight, None, 2)
        elif enemyName.isJumping:
            enemyName.controllingCharacter(game, enemyName.jumpingImagesLeft, enemyName.jumpingImagesRight, None, 2)
        elif enemyName.isBlocking:
            enemyName.controllingCharacter(game, enemyName.blockingImagesLeft, enemyName.blockingImagesRight, None, 2) 
        elif enemyName.isKicking:
            enemyName.controllingCharacter(game, enemyName.kickingImagesLeft, enemyName.kickingImagesRight, None, 2)
            enemyName.isAttacking = True
        elif enemyName.isPunching:
            enemyName.controllingCharacter(game, enemyName.punchingImagesLeft, enemyName.punchingImagesRight, None, 2)
            enemyName.isAttacking = True

    if enemyName.isAttacking:
        if player.facing == "right" and enemyName.facing == "left":
            player.xCoord -= 12
            enemyName.xCoord += 2
        elif player.facing == "left" and enemyName.facing == "right":
            player.xCoord += 12
            enemyName.xCoord -= 2
        enemyName.isAttacking = False

def playerAnimation(charName, enemyName):
    # Calling controllingCharacter
    if charName.isSpecialMove and charName == tizoc:
        if ((charName.xCoord >= dustbin.xCoord - 100) and (charName.xCoord <= dustbin.xCoord + 100)) and charName.playersmBarCount == 5:
            charName.controllingCharacter(game, charName.specialMoveImagesLeft, charName.specialMoveImagesRight, dustbin, 3)
            if player.smHappening == True:
                game.bgMoving = False
                charName.isAttacking = True
            if player.smHappening == False:
                charName.playersmBarCount = 0

        elif ((charName.xCoord >= box.xCoord - 100) and (charName.xCoord <= box.xCoord + 100)) and charName.playersmBarCount == 5:
            charName.controllingCharacter(game, charName.specialMoveImagesLeft, charName.specialMoveImagesRight, box, 3)
            if player.smHappening == True:
                game.bgMoving = False
                charName.isAttacking = True
            if player.smHappening == False:
                charName.playersmBarCount = 0

        elif ((charName.xCoord >= enemyName.xCoord - 200) and (charName.xCoord <= enemyName.xCoord + 200)) and charName.playersmBarCount == 5:
            charName.controllingCharacter(game, charName.specialMoveImagesLeft, charName.specialMoveImagesRight, enemyName, 3)
            if player.smHappening == True:
                game.bgMoving = False
                charName.isAttacking = True
                enemyName.isIdle = False
                if not charName.smDown:
                    enemyName.controllingCharacter(game, enemyName.stillImage, enemyName.stillImage, None, 3)
                else:
                    enemyName.controllingCharacter(game, enemyName.upsideDown, enemyName.upsideDown, None, 3)
            if player.smHappening == False:
                charName.playersmBarCount = 0
                enemyName.isIdle = True
                enemyName.controllingCharacter(game, enemyName.standingImagesLeft, enemyName.standingImagesRight, None, 2)

        else:
            charName.controllingCharacter(game,  charName.standingImagesLeft, charName.standingImagesRight, box, 3)
            dustbin.yCoord = 215
            dustbin.obstacleUp = True
            dustbin.dustbinDying = False
            dustbin.dustbinDead = False
            box.yCoord = 215
            box.obstacleUp = True
            box.boxDying = False
            box.boxDead = False
            charName.playersmBarCount = 0
        
    elif charName.isSpecialMove:
        if charName.playersmBarCount == 5 and charName.eijiSM:
            charName.controllingCharacter(game, charName.specialMoveImagesLeft, charName.specialMoveImagesRight, None, 3)
            game.bgMoving = False
            charName.isAttacking = True
        else:
            enemyName.isIdle = True
            charName.controllingCharacter(game,  charName.standingImagesLeft, charName.standingImagesRight, None, 3)
            charName.isAttacking = True
            charName.eijiSM = False
            charName.playersmBarCount = 0

    elif charName.isIdle:
        charName.controllingCharacter(game,  charName.standingImagesLeft, charName.standingImagesRight, None, 3)
        game.bgMoving = False
        player.isActive = False
        game.onlyOnce = False
    elif charName.isWalking:
        charName.controllingCharacter(game, charName.walkingImagesLeft, charName.walkingImagesRight, None, 3)
    elif charName.isJumping:
        charName.controllingCharacter(game, charName.jumpingImagesLeft, charName.jumpingImagesRight, None, 3)
    elif charName.isBlocking:
        charName.controllingCharacter(game, charName.blockingImagesLeft, charName.blockingImagesRight, None, 3) 
        game.bgMoving = False   
    elif charName.isKicking:
        charName.controllingCharacter(game, charName.kickingImagesLeft, charName.kickingImagesRight, None, 3)
        game.bgMoving = False
        charName.isAttacking = True
    elif charName.isPunching:
        charName.controllingCharacter(game, charName.punchingImagesLeft, charName.punchingImagesRight, None, 3)
        game.bgMoving = False
        charName.isAttacking = True

    # Eiji's fireball animation
    if not charName.eijiSM:
            fireball.xCoord = charName.xCoord

    if charName.eijiSM == True and charName != tizoc:
        fireball.fireballAnimation(game, charName, enemyName)
        
def obstacleAnimation():
    if player.xCoord >= 470 and player.isActive:
        if game.bgCount % 5 == 0:
            dustbin.xCoord -= 5   
    if dustbin.xCoord < -100:
        dustbin.xCoord = 700
        dustbin.obstacleUp = True
        dustbin.obstacleDead = False
        dustbin.obstacleDying = False
        dustbin.health = 10
    if player.xCoord <= 10 and player.isActive and game.bgCount >= 10:
        if game.bgCount % 5 == 0:
            dustbin.xCoord += 5 
    if dustbin.xCoord > 1000:
        dustbin.xCoord = -100

    if player.xCoord >= 470 and player.isActive:
        if game.bgCount % 5 == 0:
            box.xCoord -= 5  
    if box.xCoord < -50:
        box.xCoord = dustbin.xCoord + 600
        box.obstacleUp = True
        box.obstacleDead = False
        box.obstacleDying = False
        box.health = 10
    if player.xCoord <= 100 and player.isActive and game.bgCount >= 10:
        if game.bgCount % 5 == 0:
            box.xCoord += 5 
    if box.xCoord > 1400:
        box.xCoord = -10

    if (player.isPunching or player.isKicking) and ((player.xCoord >= box.xCoord - 50) and (player.xCoord <= box.xCoord + 50)):
        box.health -= 2
        if box.health <= 6 and box.health >= 1:
            box.obstacleDying = True
            box.obstacleDead = False
            box.obstacleUp = False
        if box.health <= 0:
            box.health = 0
            box.obstacleDying = False 
            box.obstacleUp = False
            box.obstacleDead = True

    if (player.isPunching or player.isKicking) and ((player.xCoord >= dustbin.xCoord - 50) and (player.xCoord <= dustbin.xCoord + 50)):
        dustbin.health -= 2
        if dustbin.health <= 6 and dustbin.health >= 1:
            dustbin.obstacleDying = True
            dustbin.obstacleDead = False
            dustbin.obstacleUp = False
        if dustbin.health <= 0:
            dustbin.health = 0
            dustbin.obstacleDying = False
            dustbin.obstacleUp = False
            dustbin.obstacleDead = True
    
    dustbin.obstacleAnimation(dustbin.dustBinUp, dustbin.dustBinDown, dustbin.dustbinDying, dustbin.dustbinDead, game)
    box.obstacleAnimation(box.boxUp, box.boxDown, box.boxDying, box.boxDead, game)

def is_collision(character, target):
    import math
    if target.facing == 'right':
        xDistance = (character.xCoord - target.xCoord - (target.height - character.height))**2
    if target.facing == "left":
        xDistance = (character.xCoord - target.xCoord)**2

    #target is always the person being attacked

    yDistance = (character.yCoord - target.yCoord)**2
    absWidth = 70

    collisionPoint = math.sqrt(xDistance + yDistance)

    if collisionPoint < absWidth:
        return True
    else:
        return False

def playerDeath(enemyName):
    if game.deathTimer <= 5:
        screen.screenStatus = "game_over"
        game.deathTempTimer += 1
        if game.deathTempTimer % 27 == 0:
            game.deathTimer += 1

        points_text = game.scoreFont.render(str(player.playerPoints), True, (235, 171, 52))
        game.window.blit(points_text, (270, 170))

        if game.onlyOnce == False:
            database.addEntry(game.date, game.entry, player.playerPoints)
            game.onlyOnce = True

    elif game.deathTimer > 5:
        screen.screenStatus = "menu"
        player.health = 100
        player.healthCount = 0
        player.playersmBarCount = 0
        player.playerPoints = 0
        player.xCoord = 15
        enemyName.health = 20
        enemyName.enemyHealthCount = 0
        enemyName.xCoord = 500
        game.bgCount = 0
        dustbin.xCoord = 700
        box.xCoord = 1100

def enemyDeath(enemyName):
    if game.deathTimer <= 5:
        game.deathTempTimer += 1
        if game.deathTempTimer % 27 == 0:
            game.deathTimer += 1

        enemyName.isDead = True
        enemyName.isIdle = False
        enemyName.yCoord = 275

        screen.advanceArrow()

        if player.xCoord >= 470 and player.isActive:
            if game.bgCount % 5 == 0:
                enemyName.xCoord -= 5  

        if player.xCoord <= 10 and player.isActive and game.bgCount >= 10:
            if game.bgCount % 5 == 0:
                enemyName.xCoord += 5
                
    if game.deathTimer > 5:
        enemyName.isDead = False
        enemyName.isIdle = True
        enemyName.yCoord = 210
        enemyName.xCoord = 1000
        enemyName.health = 20
        enemyName.enemyHealthCount = 0
        enemyName.enemysmBarCount = 0

def gameWon(enemyName):
    if game.onlyOnce == False:
        database.addEntry(game.date, game.entry, player.playerPoints)
        game.onlyOnce = True

    if game.wonTimer <= 5:
        screen.screenStatus = "game_won"
        game.wonTempTimer += 1
        if game.wonTempTimer % 27 == 0:
            game.wonTimer += 1

        points_text = game.scoreFont.render(str(player.playerPoints), True, (235, 171, 52))
        game.window.blit(points_text, (270, 170))

    if game.wonTimer > 5:
        screen.screenStatus = "menu"
        player.health = 100
        player.healthCount = 0
        player.playersmBarCount = 0
        player.playerPoints = 0
        player.xCoord = 15
        enemyName.health = 20
        enemyName.enemyHealthCount = 0
        enemyName.xCoord = 500
        game.bgCount = 0
        dustbin.xCoord = 700
        box.xCoord = 1100

def levelFinished(enemyName):
    if game.deathTimer <= 5:
        game.deathTempTimer += 1
        if game.deathTempTimer % 27 == 0:
            game.deathTimer += 1

        enemyName.isDead = True
        enemyName.isIdle = False
        enemyName.yCoord = 275

        screen.advanceArrow()

        if player.xCoord >= 470 and player.isActive:
            if game.bgCount % 5 == 0:
                enemyName.xCoord -= 5  

        if player.xCoord <= 10 and player.isActive and game.bgCount >= 10:
            if game.bgCount % 5 == 0:
                enemyName.xCoord += 5

    if enemyName == chin:
        enemyName = duo
    elif enemyName == duo:
        enemyName = tung

    if game.deathTimer > 5:
        nextLevel(enemyName)

def nextLevel(enemyName):
    enemyName.isDead = False
    enemyName.isIdle = True
    enemyName.enemyHealthCount = 0
    enemyName.enemysmBarCount = 0

    enemyAnimation(enemyName)

def gameTimer(enemyName):
    game.tempTimer += 1
    if game.tempTimer % 27 == 0:
        game.timer += 1
    
    if game.timer >= 360:
        if not game.timer >= 365:
            screen.screenStatus = "game_over"
            game.deathTempTimer += 1
        if game.deathTempTimer % 27 == 0:
            game.deathTimer += 1

        points_text = game.scoreFont.render(str(player.playerPoints), True, (235, 171, 52))
        game.window.blit(points_text, (270, 170))

        if game.onlyOnce == False:
            database.addEntry(game.date, game.entry, player.playerPoints)
            game.onlyOnce = True

        if game.deathTimer > 5:
            screen.screenStatus = "menu"
            player.health = 100
            player.healthCount = 0
            player.playersmBarCount = 0
            player.playerPoints = 0
            player.xCoord = 15
            enemyName.health = 20
            enemyName.enemyHealthCount = 0
            enemyName.xCoord = 500
            game.bgCount = 0
            dustbin.xCoord = 700
            box.xCoord = 1100

def characterPoints(playerPoints):
    points_text = game.font.render(str(playerPoints), True, (0,0,0))
    game.window.blit(points_text, (118, 52))

def askNameInput():
    textDisplay = game.font.render(str(game.entry), True, (0,0,0))
    game.window.blit(textDisplay, (game.rect.x + 95, game.rect.y + 5))
    pygame.draw.rect(game.window, (0,0,0), game.rect, 2)

while game.playGame:

    game.clock.tick(27) 

    if screen.screenStatus == "splash":
        screen.splashDisplay()
    elif screen.screenStatus == "menu":
        game.dyingTimer()
        game.winningTimer()
        game.timer = -10000
        game.onlyOnce = False
        screen.menuDisplay()
    elif screen.screenStatus == "instructions":
        screen.instructionsDisplay()
    elif screen.screenStatus == "highscores":
        screen.highscoresDisplay()
    elif screen.screenStatus == "settings":
        screen.settingsDisplay()
    elif screen.screenStatus == "character select":
        screen.characterSelectDisplay()
    elif screen.screenStatus == "ask_name":
        screen.askNameDisplay()
        askNameInput()
    elif screen.screenStatus == "game_over":
        screen.gameOverDisplay()
    elif screen.screenStatus == "game_won":
        screen.gameWonDisplay()

    # Username code

    events = pygame.event.get()
    for event in events:
        
        if event.type == pygame.QUIT:
            game.playGame = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game.rect.collidepoint(event.pos):
                game.isTextActive = True
        if event.type == pygame.KEYDOWN and len(game.entry) <= 2:
            if game.isTextActive:
                if event.key == pygame.K_LEFT:
                    game.entry = game.entry[:-1]
                else:
                    game.entry += event.unicode.upper()

        if event.type == pygame.KEYDOWN and len(game.entry) >= 2:
            if game.isTextActive:
                if event.key == pygame.K_LEFT:
                    game.entry = game.entry[:-1]

        if screen.screenStatus == "ask_name":
            if len(game.entry) < 3:
                if keys[pygame.K_RETURN]:
                    screen.screenStatus = "ask_name"
            if len(game.entry) >= 3:
                if keys[pygame.K_RETURN]:
                    screen.screenStatus = "level 1"

    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            game.playGame = False 
        if screen.screenStatus == "splash" and keys[pygame.K_RETURN]:
            game.clock.tick(5)
            screen.screenStatus = "menu"
        elif screen.screenStatus == "menu":
            screen.buttonSelectMenu(50, 315)
        elif screen.screenStatus == "settings":
            screen.buttonSelectSettings(50, 265)

        elif screen.screenStatus == "level 1": 
            game.stopMusic()

            if screen.currentChar == "Eiji":
                player = eiji
                avatarIndx = 1
            else:
                player = tizoc
                avatarIndx = 0

            # Boundaries for where the player can walk on the screen

            if player.xCoord >= 470:
                player.xCoord = 470

            elif player.xCoord <= 10:
                player.xCoord = 10

            if player.xCoord <= 10 and game.bgMoving == True:
                game.bgCount -= player.velocity*game.gameSpeed

            elif player.xCoord >= 470 and game.bgMoving == True:
                game.bgCount += player.velocity*game.gameSpeed

            if game.bgCount <= 0:
                game.bgCount = 0

            elif game.bgCount >= 5250:
                game.bgCount = 5250

            # Displaying the health bars
            if player.playerPoints < 150:
                screen.levelDisplay(-game.bgCount, player.healthCount, chin.enemyHealthCount, player.playersmBarCount, chin.enemysmBarCount)
                game.window.blit(player.avatar[2], (530, 10))
            if player.playerPoints >= 150 and player.playerPoints < 300:
                screen.levelDisplay(-game.bgCount, player.healthCount, duo.enemyHealthCount, player.playersmBarCount, duo.enemysmBarCount)
                game.window.blit(player.avatar[3], (530, 13))
            if player.playerPoints >= 300:
                screen.levelDisplay(-game.bgCount, player.healthCount, tung.enemyHealthCount, player.playersmBarCount, tung.enemysmBarCount)
                game.window.blit(player.avatar[4], (520, 10))

            # Images next to the healthbar indicating what character you are playing as (tizoc and eiji)
            game.window.blit(player.avatar[avatarIndx], (3, 12))

            obstacleAnimation()

            # The three game levels
            if player.playerPoints < 150:
                enemyAnimation(chin)
                playerMoves(chin)
            if player.playerPoints >= 150 and player.playerPoints < 300:
                levelFinished(chin)
                playerMoves(duo)
            if player.playerPoints >= 300:
                levelFinished(duo)
                playerMoves(tung)

            characterPoints(player.playerPoints)

            counting_text = game.font.render(str(game.timer), True, (0,0,0))
            game.window.blit(counting_text, (291, 30))

        # Upon death
        if player.health == 0:
            playerDeath(chin)

        if tung.health == 0:
            enemyDeath(tung)

        if player.playerPoints >= 450:
            gameWon(chin)

        if (screen.screenStatus != "menu" and screen.screenStatus != "splash") and keys[pygame.K_BACKSPACE]:
            screen.screenStatus = "menu"
    
    gameTimer(chin)
    pygame.display.update()

pygame.quit()