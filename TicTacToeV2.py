import os
from Tab2 import check_beurt, check_for_win, draw_board;
# alle variables wat we nodig hebben
vakje = {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5', 
         6 : '6', 7 : '7',  8 : '8', 9 : '9'}
spelen, complete = True, False
beurt = 0
vorige_beurt = -1
# Game Loop
while spelen:
    # Reset het scherm
    os.system('cls' if os.name == 'nt' else 'clear')
    # tekent het speelvakje
    draw_board(vakje)
    # Als de speler een verkeerde input geeft, laat dit het de speler weten
    if vorige_beurt == beurt:
      print("De input was ongeldig, probeer opnieuw")
    vorige_beurt = beurt
    print("Speler " + str((beurt % 2) +1 ) + " is aan de beurt. Kies een vakje of druk op s om te stoppen")
    
    keuze = input()
    # Het spel stopt
    if keuze == 's':
        spelen = False
    elif str.isdigit(keuze) and int(keuze) in vakje:
      # Checken of het vakje al is ingenomen
      if not vakje[int(keuze)] in {"X", "O"}:
        # Als het niet is, update het vakje
        beurt += 1
        vakje[int(keuze)] = check_beurt(beurt)
      
    # Checken of het spel is geëindigd if the game has ended (and if someone won)
    if check_for_win(vakje): spelen, complete = False, True
    if beurt > 8: spelen = False
    
# Update het board nog 1 keer 
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(vakje)
# als er iemand gewonnen heeft,laat het zien
if complete:
  if check_beurt(beurt) == 'X': print("Speler 1 Wint!")
  else: print("Speler 2 Wint!")
else: 
  # Gelijkspel
  print("Geen winnaar")
  
print("Bedankt voor het spelen") 