#  ===========================================================================
#  This is an example for Hover. 
#  
#  Hover is a development kit that lets you control your Arduino projects in a whole new way.  
#  Wave goodbye to physical buttons. Hover detects hand movements in the air for touch-less interaction.  
#  It also features five touch-sensitive regions for even more options.
#  Hover uses I2C and 2 digital pins. It is compatible with Arduino, Raspberry pi and more.
#
#  Hover can be purchased from here: http://www.justhover.com
#
#  Written by Emran Mahbub and Jonathan Li for Gearseven Studios.  
#  BSD license, all text above must be included in any redistribution
#  ===========================================================================
#
#  HOOKUP GUIDE (For Raspberry Pi)
#  
#    =============================
#   | 1 2 3 4 5 6 7               |                               
#   |                      HOVER  |
#   |                             |
#   | +++++++++++++++++++++++++++ |
#   | +                         + |
#   | +                         + |
#   | *                         + |
#   | *                         + |
#   | *                         + |
#   |_+++++++++++++++++++++++++++_|
#   
#  PIN 1 - HOST_V+    ----    3V3 pin 
#  PIN 2 - RESET      ----    Any Digital Pin.  This example uses GPIO 24 (BCM Mode). 
#  PIN 3 - SCL        ----    SCL pin
#  PIN 4 - SDA        ----    SDA pin
#  PIN 5 - GND        ----    Ground Pin
#  PIN 6 - 3V3        ----    3V3 pin
#  PIN 7 - TS         ----    Any Digital Pin.  This example uses GPIO 23 (BCM Mode).
#   
#  HISTORY
#  v1.0  -  Initial Release
#  
#  INSTALLATION
#  Place the Hover_library.py file in the same folder as the Hover_example.py file.
#  Then run Hover_example.py by typing: sudo python Hover_example.py
#
#  SUPPORT
#  For questions and comments, email us at support@gearseven.com


import pygame
import time
from Hover_library import Hover

hover = Hover(address=0x42, ts=23, reset=24)

pygame.mixer.init()

kick = pygame.mixer.Sound('samples/kick.wav')
clap = pygame.mixer.Sound('samples/clap.wav')
cymbal = pygame.mixer.Sound('samples/cymbal.wav')
snare = pygame.mixer.Sound('samples/snare.wav')
champion = pygame.mixer.Sound('samples/champion.wav')
closed = pygame.mixer.Sound('samples/closed.wav')
ahems = pygame.mixer.Sound('samples/ahem.wav')
doit = pygame.mixer.Sound('samples/doit.wav')
force = pygame.mixer.Sound('samples/force.wav')

try: 
  while True:

    # Check if hover is ready to send gesture or touch events
    if (hover.getStatus() == 0):
      # Read i2c data and print the type of gesture or touch event
      message = hover.getEvent() 
      type(message)
      if (message == "01000010"):  
        kick.play()  #west
      elif (message == "01010000"):
        snare.play() #center
      elif (message == "01001000"):
        closed.play() #east
      elif (message == "01000001"):
        cymbal.play() #south
      elif (message == "01000100"):
        clap.play() #north
      elif (message == "00100010"):
        champion.play() #swipe right
      elif (message == "00100100"):
        ahems.play() #swipe left
      elif (message == "00110000"):
        force.play() #swipe down
      elif (message == "00101000"):
        doit.play()

      # Release the ts pin until Hover is ready to send the next event
      hover.setRelease()
    time.sleep(0.0008)   #sleep for 1ms

except KeyboardInterrupt:
  print "Exiting..."
  hover.end()

except:
  print "Something has gone wrong..."
  hover.end()