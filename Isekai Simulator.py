"""
Conor
2022-03-24 - 2022-03-25
Interactive Story
In Retrospect I couldve made variables with the messages and printed the variables
Same with the timers
Feelsbad Man
"""
#This import below makes the program capable of randomly selecting numbers
#from a sequence/range variable or generating them.
import random
#This import below makes the program capable of delaying statements (improving the flow)
import time
death=False
reincarnation=False
powers=False
harem=False #The Goal Is To Get All Of These To True To Get The Best Ending, I could implement something to write the number if it's true but im too lazy
print(   #Introduction
'''
 __________________________________________________
|Welcome To The Isekai Interactive Story           |
|You will be asked Questions on your Journey       |
|The Answers will Be "1" "2" or "#"                |
|# Represents Any Other Number Except For 1        |
|               Good Luck!                         |
|Ending Number Explanations are on the MindMap     |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
'''
)

a=False
b=False
c=False # These are so I can do "While" Statments to minimize Input Error Possibilities
"""
first decision, this changes the chance of RNG situations later on 
The reason why I chose sex is it's a reference to the lack of 
isekais with a female MC however the a majority that do have a harem 
and also the surplus of male losers isekaing and being "badass"
(change variation in the odds for an ending that is luck based)
"""
while not a: #this setup helps to minimize Value Error, you'll see it more
  time.sleep(2.5)
  sex=input( 
  '''
 ___________________________________________________ 
|You Are A 30YO Broke Gambling Addicted NEET        |
|          Living With Your Parents                 |
|   Gambling Your Lifesavings Away On Genshin       |
|Your Goal Is To Become Die And Become Reincarnated |
|          In A Better Life With Powers             |
| INPUT BELOW ARE YOU "1": A MALE OR "#" A FEMALE   |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    
  '''
  )
  try:
    sex=int(sex)
    a=True #preventing a loop
    if sex == 1: #checking if male
      time.sleep(1.5)
      print( # To Set the story a little
      '''
 __________________________________________________
|You Get A Text From Your Mother Telling You She's |
|Shed Enough Tears And You're Moving Out Within The|
|                     Week                         |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
      '''
      )
      while not b:
        time.sleep(1.5)
        truck_kun = input( #Decision 1 Techically 2
        '''
 _________________________________________________________
| You Are Walking Across The Street To Buy Instant Noodles|
| A Truck with the plate "Truck-Kun Is Headed Towards You |
|          DO YOU "1" LET THE TRUCK HIT YOU               |
|               DO YOU "#" KEEP WALKING                   |
|               INPUT YOUR ANSWER BELOW                   |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        '''
        )
        try:
          truck_kun = int(truck_kun)
          b = True #preventing a loop
          if truck_kun == 1: #if decision is to let the truck hit
            death=True #cause you die
            time.sleep(1.5)
            print(
            '''
 ___________________________________________________
| You See The Light Of The Truck Coming Towards You |
|       You Look Into The Driver's Seat             |
|               You See Noone There                 |
|    Right Before The Truck Hits You Hear Honking   |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            '''  
            )
            time.sleep(2.0)
            print(
            '''
 ______________________________________________________
|You Have Died, Rolling To See If You Have Reincarnated|
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            '''
            )
            reincarnationrng = [1,2,2]
            reincarnationrng = random.choice(reincarnationrng)
            if reincarnationrng == 1:
              reincarnation = True
              time.sleep(1.5)
              print(
              '''
 _________________________________________________________________
|   You See A Light In The Darkness And You Reach Out To Touch It |
|As You Approach To Touch It You Hear The Constellation's Voice   |
|                     "Come My Child"                             |
|         You Touch It And You Become Unconsious                  |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              '''
              )
              time.sleep(1.5)
              print(
              '''
 ___________________________________________________
|        You Successfully  Reincarnated!            |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              '''
              )
              while not c:
                time.sleep(1.5)
                gods_call = input( #Forgot to say Im sorry Im bad at typesetting. Also this is Decision 3 the last decision next is RNG
                '''
 _______________________________________________________
|        You Awaken To Find Yourself In A Room          |
|               With The Constellation                  |
|       They Tell You That You Were Summoned Here       |
|     To Save The People Of This Dimension From A       |
|     Tyranical Demon King And Other Demonic Beasts     |
|     DO YOU RESPOND WITH "1": "I'LL DO WHATEVER I WANT"|
|     DO YOU RESPOND WITH "2": "SEND ME HOME"           |
|     DO YOU RESPOND WITH "#": "I'LL HELP YOU SAVE THEM |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                '''
                )
                try:
                  gods_call = int(gods_call)
                  c = True
                  if gods_call == 1:
                    time.sleep(1.5)
                    print(
                    '''
 _______________________________________________________________________
| Enraged By Your Remarks The Constellation Sends You Into              |
| Demonic Territory Without Supplies Nor Clothes                        |
| Chased For Years By The Demons You Survive Off The Meat From Their    |
| Corpses Which Eventually Turns You Into One Of Them                   |
| For The Remainder Of Your Years You End Up Mindlessly Attacking People|
| Until One Of The Human Survivors Kills You In Revenge                 |
| The War Continues On For Another Decade Before Both Sides Are Extinct |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                    '''  
                    )
                    time.sleep(2.5)
                    print(
                    '''
 ____________________________________________
|  YOU HAVE ACHIEVED THE BLOODIEST ENDING    |
|               ENDING #2457-M               |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

                    '''
                    )
                  elif gods_call == 2:
                    death = False
                    powers = True
                    harem = True
                    time.sleep(1.5)
                    print(
                    '''
 _______________________________________________________________________________________
| The Constellation Feeling Mistaken About Their Belief That You Were                   |
| Worthy Of Becoming A Hero Sends You Back To Earth Into Your Now                       |
| Crippled Body In A Coma With Your Consious In A Fantasy World As An Apology For       |
| Putting You Into This Situation In This World You Have Many Partners and Superpowers  |
| You Spend Another Year Of Your Life Unaware Of Your Situation Until The Plug Is Pulled|
| When Your Mother Feels She Cannot Take The Pain Of Seeing You Like This Anymore       |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                    '''  
                    )
                    time.sleep(2.5)
                    print(
                    '''
 ____________________________________________
|  YOU HAVE ACHIEVED THE COMATOSE ENDING     |
|               ENDING #3568-M               |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

                    '''
                    )

                  else:
                    powers=True
                    time.sleep(1.5)
                    print(
                    '''
 ___________________________________________________
| Hearing Your Eagerness The Constellation Gifts You|
|                  Powers                           |
|       Rolling to See The Final Outcome            |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                    '''
                    )
                    finalrng = [1,1,2,3]
                    finalrng = random.choice(finalrng)
                    if finalrng == 1:
                      reincarnation= False
                      death = False
                      time.sleep(1.5)
                      print(
                      '''
 ___________________________________________________________
|After Almost A Year Of Combative Training You And          |
|The Final Army Of Humans Wage War Against The Demons       |
|During The Battle You Are Killed In Combat By An Orge      |
|And You Wake Up In A Hospital Bed Beside Your Mother Crying|
|You Realize You Saw A Possible Future And Capitalize On It |
|You Spend The Rest Of Your Life Turning Yourself Around    |
|And You Invent Many Important Things Going Down In History |
|                 As An Inspiration                         |
|But You Cant Sleep Because All You Can Think About Is The  |
|                 World You Left To Die                     |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                      '''  
                      )
                      time.sleep(2.5)
                      print(
                      '''
 ____________________________________________
| YOU HAVE ACHIEVED THE BITTERSWEET ENDING   |
|               ENDING #1346-M               |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                      '''
                      )
                    elif finalrng == 2:
                      time.sleep(1.5)
                      print(
                      '''
 ____________________________________________________________________
|   After Almost A Year Of Combative Training You And                |
|   The Final Army Of Humans Wage War Against The Demons             |
|During The Battle You Lead And Manage To Slay The Demon King        |
|    After The Battle, A Year Later, The Body Count Is In The        |
|                   Hundreds Of Thousands                            |
|              Most Of Which Were Killed By You                      |
|Many People Cheer You As The New Human King When You Pass           |
|But It's All A Mirage For Deep Down They Fear You More Than         |
|             They Feared The Demon King                             |
| You Die Lonely With No Friends Nor Family Beside You When You Are  |
|                 Executed By Revolutionaries                        |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                      '''
                      )
                      time.sleep(2.5)
                      print(
                      '''
 ____________________________________________
| YOU HAVE ACHIEVED THE "NIETZSCHE" ENDING   |
|               ENDING #4567-M               |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                      '''
                      )
                    else:
                      harem = True
                      time.sleep(1.5)
                      print(
                        '''
 ____________________________________________________________________
|After Almost A Year Of Combative Training You And                   |
|   The Final Army Of Humans Wage War Against The Demons             |
|  Very Quickly Into The War Through Seeing Countless Lives Shed     |
|You Realize You Should Be Going For A More Diplomatic Solution And  |
| You Arrange A Sitdown With The Demon King Creating A Cease Fire    |
| Ending The War And Creating Trade Between The Humans And The Demons|
| You And The Demon King Are Put Down In Historical Tales For A      |
| Thousand Years To Come As Genius Leaders And Whenever You See      |
|       People On The Street You Are Met With Respect              0  |
| You Have Many Partners And Manage To Die With Them At Your Side    |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                        '''
                      )
                      time.sleep(2.5)
                      print(
                        '''
 ____________________________________________
| YOU HAVE ACHIEVED THE "BEST" ENDING        |
|               ENDING #5678-M               |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                        '''
                      )
                except ValueError:
                  print(
                  '''
 ______________________________________________________
| PLEASE INPUT OPTION "1", OPTION "2" or OPTION "#"    |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                  '''  
                  )
            else:
              time.sleep(1.5)
              print(
              '''
 _________________________________________________________________
|   You See A Light In The Darkness And You Reach Out To Touch It |
|  As You Approach To Touch It You Hear The Constellation Voice   |
|           "Sinner Of The Sloth, You Are Not Welcome"            |
|   You Are Sent Flying Away and You Become Unconsious            |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              '''
              )
              time.sleep(2.5)
              print(
              '''
 ____________________________________________________
|  You Are Trapped As A Spirit In Between Dimensions |
|  You Spend Eternity Thinking Of What Sin They Meant|
|  You Have Achieved "Dead" Ending #1247-M           |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              '''  
              )
          else:
            time.sleep(1.5)
            print( #more Story
            '''
 ______________________________________________
|  You Are Kicked Out Of Your Home And Spend   |
|   Five Years In And Out Of Public Housing    |
|   Until You Are Charged And Registered As    |
|                A Sex Offender                |
|  You Spend Your Life Lonely And Miserable    |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            '''
            )
            time.sleep(2.5)
            print( #End Of Code
            '''
 ____________________________________________
|      YOU HAVE ACHIEVED THE WORST ENDING    |
|               ENDING #1234-M               |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            '''
            )
        except ValueError:
          print(
          '''
 ______________________________________________________
|            PLEASE INPUT OPTION "1" or OPTION "#"     |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
          '''  
          )
    else: # if the answer is female
      time.sleep(1.5)
      print( # To Set the story a little
      '''
 __________________________________________________
|You Get A Text From Your Father Telling You He's  |
|Shed Enough Tears And You're Moving Out Within The|
|                     Week                         |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
      '''
      )
      while not b:
        time.sleep(1.5)
        truck_kun = input( #Decision 1 Techically 2
        '''
 _________________________________________________________
| You Are Walking Across The Street To Buy Instant Noodles|
| A Truck with the plate "Truck-Kun Is Headed Towards You |
|          DO YOU "1" LET THE TRUCK HIT YOU               |
|               DO YOU "#" KEEP WALKING                   |
|               INPUT YOUR ANSWER BELOW                   |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        '''
        )
        try:
          truck_kun = int(truck_kun)
          b = True #preventing a loop
          if truck_kun == 1: #if decision is to let the truck hit
            death=True #cause you die
            time.sleep(1.5)
            print(
            '''
 ______________________________________________________
|You Have Died, Rolling To See If You Have Reincarnated|
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            '''
            )
            reincarnationrng = [1,2,2,2]
            reincarnationrng = random.choice(reincarnationrng)
            if reincarnationrng == 1:
              reincarnation = True
              time.sleep(1.5)
              print(
              '''
 _________________________________________________________________
|   You See A Light In The Darkness And You Reach Out To Touch It |
|As You Approach To Touch It You Hear The Constellation's Voice   |
|                     "Come My Child"                             |
|         You Touch It And You Become Unconsious                  |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              '''
              )
              time.sleep(1.5)
              print(
              '''
 ___________________________________________________
|        You Successfully  Reincarnated!            |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              '''
              )
              while not c:
                time.sleep(1.5)
                gods_call = input( #Forgot to say Im sorry Im bad at typesetting. Also this is Decision 3 the last decision next is RNG
                '''
 _______________________________________________________
|        You Awaken To Find Yourself In A Room          |
|               With The Constellation                  |
|       They Tell You That You Were Summoned Here       |
|     To Save The People Of This Dimension From A       |
|     Tyranical Demon King And Other Demonic Beasts     |
|     DO YOU RESPOND WITH "1": "I'LL DO WHATEVER I WANT"|
|     DO YOU RESPOND WITH "2": "SEND ME HOME"           |
|     DO YOU RESPOND WITH "#": "I'LL HELP YOU SAVE THEM |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                '''
                )
                try:
                  gods_call = int(gods_call)
                  c = True
                  if gods_call == 1:
                    time.sleep(1.5)
                    print(
                    '''
 _______________________________________________________________________
| Enraged By Your Remarks The Constellation Sends You Into              |
| Demonic Territory Without Supplies Nor Clothes                        |
| Chased For Years By The Demons You Survive Off The Meat From Their    |
| Corpses Which Eventually Turns You Into One Of Them                   |
| For The Remainder Of Your Years You End Up Mindlessly Attacking People|
| Until One Of The Human Survivors Kills You In Revenge                 |
| The War Continues On For Another Decade Before Both Sides Are Extinct |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                    '''  
                    )
                    time.sleep(2.5)
                    print(
                    '''
 ____________________________________________
|  YOU HAVE ACHIEVED THE BLOODIEST ENDING    |
|               ENDING #2457-F               |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

                    '''
                    )
                  elif gods_call == 2:
                    death = False
                    powers = True
                    harem = True
                    time.sleep(1.5)
                    print(
                    '''
 _______________________________________________________________________________________
| The Constellation Feeling Mistaken About Their Belief That You Were                   |
| Worthy Of Becoming A Hero Sends You Back To Earth Into Your Now                       |
| Crippled Body In A Coma With Your Consious In A Fantasy World As An Apology For       |
| Putting You Into This Situation In This World You Have Many Partners and Superpowers  |
| You Spend Another Year Of Your Life Unaware Of Your Situation Until The Plug Is Pulled|
| When Your Father Feels He Cannot Take The Pain Of Seeing You Like This Anymore        |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                    '''  
                    )
                    time.sleep(2.5)
                    print(
                    '''
 ____________________________________________
|  YOU HAVE ACHIEVED THE COMATOSE ENDING     |
|               ENDING #3568-F               |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

                    '''
                    )

                  else:
                    powers=True
                    time.sleep(1.5)
                    print(
                    '''
 ___________________________________________________
| Hearing Your Eagerness The Constellation Gifts You|
|                  Powers                           |
|       Rolling to See The Final Outcome            |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                    '''
                    )
                    finalrng = [1,2,3]
                    finalrng = random.choice(finalrng)
                    if finalrng == 1:
                      reincarnation= False
                      death = False
                      time.sleep(1.5)
                      print(
                      '''
 ___________________________________________________________
|After Almost A Year Of Combative Training You And          |
|The Final Army Of Humans Wage War Against The Demons       |
|During The Battle You Are Killed In Combat By An Orge      |
|And You Wake Up In A Hospital Bed Beside Your Father Crying|
|You Realize You Saw A Possible Future And Capitalize On It |
|You Spend The Rest Of Your Life Turning Yourself Around    |
|And You Invent Many Important Things Going Down In History |
|                 As An Inspiration                         |
|But You Cant Sleep Because All You Can Think About Is The  |
|                 World You Left To Die                     |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                      '''  
                      )
                      time.sleep(2.5)
                      print(
                      '''
 ____________________________________________
| YOU HAVE ACHIEVED THE BITTERSWEET ENDING   |
|               ENDING #1346-F               |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                      '''
                      )
                    elif finalrng == 2:
                      time.sleep(1.5)
                      print(
                      '''
 ____________________________________________________________________
|   After Almost A Year Of Combative Training You And                |
|   The Final Army Of Humans Wage War Against The Demons             |
|During The Battle You Lead And Manage To Slay The Demon King        |
|    After The Battle, A Year Later, The Body Count Is In The        |
|                   Hundreds Of Thousands                            |
|              Most Of Which Were Killed By You                      |
|Many People Cheer You As The New Human King When You Pass           |
|But It's All A Mirage For Deep Down They Fear You More Than         |
|             They Feared The Demon King                             |
| You Die Lonely With No Friends Nor Family Beside You When You Are  |
|                 Executed By Revolutionaries                        |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                      '''
                      )
                      time.sleep(2.5)
                      print(
                      '''
 ____________________________________________
| YOU HAVE ACHIEVED THE "NIETZSCHE" ENDING   |
|               ENDING #4567-F               |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                      '''
                      )
                    else:
                      harem = True
                      time.sleep(1.5)
                      print(
                        '''
 ____________________________________________________________________
|After Almost A Year Of Combative Training You And                   |
|   The Final Army Of Humans Wage War Against The Demons             |
|  Very Quickly Into The War Through Seeing Countless Lives Shed     |
|You Realize You Should Be Going For A More Diplomatic Solution And  |
| You Arrange A Sitdown With The Demon King Creating A Cease Fire    |
| Ending The War And Creating Trade Between The Humans And The Demons|
| You And The Demon King Are Put Down In Historical Tales For A      |
| Thousand Years To Come As Genius Leaders And Whenever You See      |
|       People On The Street You Are Met With Respect                |
| You Have Many Partners And Manage To Die With Them At Your Side    |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                        '''
                      )
                      time.sleep(2.5)
                      print(
                        '''
 ____________________________________________
| YOU HAVE ACHIEVED THE "BEST" ENDING        |
|               ENDING #5678-F               |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                        '''
                      )
                except ValueError:
                  time.sleep(1.5)
                  print(
                  '''
 ______________________________________________________
| PLEASE INPUT OPTION "1", OPTION "2" or OPTION "#"    |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                  '''  
                  )
            else:
              time.sleep(1.5)
              print(
              '''
 _________________________________________________________________
|   You See A Light In The Darkness And You Reach Out To Touch It |
|As You Approach To Touch It You Hear The Constellation's Voice   |
|           "Sinner Of The Sloth, You Are Not Welcome"            |
|   You Are Sent Flying Away and You Become Unconsious            |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              '''
              )
              time.sleep(2.5)
              print(
              '''
 ____________________________________________________
|  You Are Trapped As A Spirit In Between Dimensions |
|  You Spend Eternity Thinking Of What Sin They Meant|
|  You Have Achieved "Dead" Ending #1247-F           |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              '''  
              )
          else:
            time.sleep(1.5)
            print(
            '''
 ______________________________________________
|  You Are Kicked Out Of Your Home And Spend   |
|   Five Years In And Out Of Public Housing    |
|   Until You Are Charged And Registered As    |
|                A Sex Offender                |
|  You Spend Your Life Lonely And Miserable    |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            '''
            )
            time.sleep(2.5)
            print(
            '''
 ____________________________________________
|      YOU HAVE ACHIEVED THE WORST ENDING    |
|               ENDING #1234-F               |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            '''
            )
        except ValueError:
          time.sleep(1.5)
          print(
          '''
 ______________________________________________________
|            PLEASE INPUT OPTION "1" or OPTION "#"     |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
          '''  
          )
  except ValueError:
    time.sleep(1.5)
    print(
    '''
 ___________________________________________________
|PLEASE INPUT IF YOU ARE "1": A MALE OR "#" A FEMALE|
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    '''
    )