print('Surfire Fish Folk')
one_up=input('Character Name...')
print('Welcome '+one_up)
print('1up... You are a skilled warrior born and raised in a fishing village with no name near.\nThis village is on a mountain with a sea and fresh water spring. You grow up move out build a house of logs.\n One night when all was safe and sound on one of the holidays\n when the guards took the night off. There was much feasting and cheering and ballads sung to and about the gods.\n...And then the Ogres made their plans.\n They smashed, killed, destroyed, and swallowed whole all the people and houses.\n In the end there was destruction and fire as far as the eye could see.\n The Ogres were gone now because they would turn to dust in sunlight. But the destruction lingered.\n The only one left alive was...\n '+one_up)
print ('and from here you begin you begin your journey. To defeat Ogres and bring justice to your people.')
print('instrucions- input the number of choice you would like. ONLY THE NUMBER.')
q1=input('1-build a tent from cow hides found in the leather workings. 2-build a house from the debris.')
if q1=='1':
    print('you build a light portable tent to take on the journey, as the night comes')

else:
    print('Your building skills were terrible. so you built an easy tent, before the sun sets. Then you try to collect supplies.')
q2=input('1-Find weapons and food 2-Quit.')

if q2=='1':
    print("You quickly collect food, go to the armoury but take ages to find a weapon the Ogres didn't take")
    print('So you sleep uncomfortable on rocks that night')
    print('you awake and are knee deep in water you get out quick and you can not remeber where your tent is.')
    q3=input('1-Kill buffaloe for skins 2-Kill lamas for wool')
    if q3=='1':
        print('\nYou kill buffaloe with the weapons you collected.\n')
        q5=input('1-cook the meat first 2-stretch the skins and make a tent.\n')
        if q5=='1':
            print('You make a fire. Smoke fills the air before you know it ogres snatch you.')
            print('-GAME OVER-')
        else:
            print('You build a tent rest up and awake. You hear leaking.')
            q4=input('1-Investigate leak 2-Ignore leak')
            if q4=='1':
                print('you come back to the armoury. you spot a leak. while blocking it you spot iron.')
                q9=input('1-Pick up iron 2- head back up.')
                if q9=='1':
                    print('You pull on the iron until it comes free. You find it is actually a musket, and behind it is plenty of powder and ammo. You graab as much as you can carry and head back up.')
                    q11=input('1-Venture out East 2-go west')
            else:
                print('You head back up with nothing left to do you decide to venture out.')
                q10=input('1-Head East 2-Head west')
                if q10=='1':
                    print('You travel East for many days. Finally you come across a stream with bamboo sprouts, So you stock up on resources.')
    else:
        print('You set up your wool tent, and sort the meat.')
        q7=input('1-make a fire and cook the meat 2-eat rations.')
        if q7=='1':
            print('You start a fire but your tent catches on fire. this commotion causes nearby ogres to eat you.')
            print('-GAME OVER-')
        else:
            print('You awake fresh. You hear leaking.')
            q8=input('1-investigate leak 2-Ingnore leak')
            if q8=='1':
                print('you come back to the armoury. you spot a leak. while blocking it you spot iron.')
                q9=input('1-Pick up iron 2- head back up.')
                if q9=='1':
                    print('You pull on the iron until it comes free. You find it is actually a musket, and behind it is plenty of powder and ammo. You graab as much as you can carry and head back up.')
                    q12=input('1-Head East 2-Head West')
            else:
                print('with nothing to do you decide to head out.')
                q8=input('1-Head East 2-Head west')
