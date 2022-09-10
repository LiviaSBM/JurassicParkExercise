#Student Name: Livia Menezes
#POO Exercise - Luiza Code Python Bootcamp

dinodictionary = {1: ["Tyrannosaurus Rex","theropod","Cretaceous","bipedal carnivore","North America","T. rex could grow to lengths of over 12.4 m (40.7 ft), up to 3.66–3.96 m (12–13 ft) tall at the hips, and 8.87 metric tons (9.78 short tons) in body mass.[2] Although other theropods rivaled or exceeded Tyrannosaurus rex in size, it is still among the largest known land predators and is estimated to have exerted the strongest bite force among all terrestrial animals."], 2: ["Velociraptor","theropod","Cretaceous","bipedal carnivore","North America","Smaller than other dromaeosaurids like Deinonychus and Achillobator, Velociraptor was about 1.5–2.07 m (4.9–6.8 ft) long with a body mass between 15–18.3 kg (33–40 lb), roughly the size of a turkey. However, it's believed to have been a smart dinosaur and have had good communication skills."], 3: ["Brachiosaurus","sauropod","late Jurassic","herbivorous","North America","Brachiosaurus is estimated to have been between 18 and 22 meters (59 and 72 ft) long. It had a disproportionately long neck, small skull, and large overall size, all of which are typical for sauropods. Atypically, Brachiosaurus had longer forelimbs than hindlimbs, which resulted in a steeply inclined trunk, and a proportionally shorter tail."], 4: ["Triceratops","ceratopsid","Late Cretaceous","herbivorous","North America","The name Triceratops, which literally means 'three-horned face'. Triceratops is one of the most recognizable of all dinosaurs and the most well-known ceratopsid. It was also one of the largest, up to 8–9 metres (26–30 ft) long and 5–9 metric tons (5.5–9.9 short tons) in body mass."], 5: ["Dilophosaurus","theropod","Early Jurassic","bipedal carnivore","North America","At about 7 m (23 ft) in length, with a weight of about 400 kg (880 lb), Dilophosaurus was one of the earliest large predatory dinosaurs and the largest known land-animal in North America at the time."], 6: ["Compsognathus","theropod","Jurassic","bipedal carnivore","Europe","Many presentations still describe Compsognathus as chicken-sized dinosaurs because of the size of the German specimen, which is now believed to be a juvenile. Compsognathus longipes is one of the few dinosaur species whose diet is known with certainty: the remains of small, agile lizards are preserved in the bellies of both specimens"], 7: ["Gallimimus","theropod","Late Creataceous","bipedal herbivorous","Asia","Gallimimus is the largest known ornithomimid; adults were about 6 metres (20 ft) long, 1.9 metres (6 ft 3 in) tall at the hip and weighed about 440–450 kilograms (970–990 lb)."], 8: ["Stegosaurus","armored dinosaur","Late Jurassic","herbivorous quadrupeds","Europe and North America","Due to their distinctive combination of broad, upright plates and tail tipped with spikes, Stegosaurus is one of the most recognizable kinds of dinosaurs. The function of this array of plates and spikes has been the subject of much speculation among scientists. Today, it is generally agreed that their spiked tails were most likely used for defense against predators, while their plates may have been used primarily for display, and secondarily for thermoregulatory functions."] }

print("Welcome to Jurassic Park interactive system\n")
name = input("Please inform your name: \n")
user = input("Please, indicate whether you are a Visitor or an Employee:\n")

class MenuRoll: #Ok - Aloca o Visitante/Funcionario pro MainMenu certo
    def __init__(self,user):
        self.user = user

    def execute(self):
        if self.user=="visitor" or self.user=="Visitor":
            user=MainMenu(name)
            return user.menuvisitor()
        elif self.user=="employee" or self.user=="Employee":
            user=MainMenu(name)
            return user.menuemployee()

class MainMenu: #Ok - Pergunta qual item do menu o usuario quer
    def __init__(self,name):
        self.name = name

    def menuemployee(self):
        print(f"Welcome, {self.name}. What would you like to check?\nMenu:\n1.Payment information\n2.Mr DNA Lab\n")
        
        choice = int(input("Please choose either 1 or 2 as per the options shown above:\n"))
        while choice !=1 and choice !=2:
            choice = int(input("Invalid option. Please choose either 1 or 2 as per the options shown above:\n"))
        return choice

    def menuvisitor(self):
        print(f"Hello {self.name}. Welcome to Jurassic Park. What would you like to check today?\nMenu:\n1.Know the Park\n2.Dinosaur catalogue and information\n3.Jurassic Park attactions\n")
        
        choice = int(input("Please choose either 1, 2 or 3 as per the options shown above:\n"))
        while choice !=1 and choice !=2 and choice != 3:
            choice = int(input("Invalid option. Please choose either 1, 2 or 3 as per the options shown above:\n"))
        return choice

execucao = MenuRoll(user) #-TESTE DAS CLASSES ANTERIORES
#print(execucao.execute())

class VisitorsMenu: #Ok - Executa opcoes do Visitante
    def __init__(self, choice):
        self.choice = choice
        
    def visitor1_knowthepark(self):
        print("\nThe park is divided in 4 main areas. The carnivores are located at the east and west zones, whereas the herbivores are in the North and South.\nThe Helicopter ride is located at the South shore.\nThe Port is at the East shore.\nThe Visitor center is at the West island.\nYou can get a map with all locations and attractions at the Visitor Center.\n")

        askifrestart = Restart(user)
        return askifrestart.restart()

    def visitor2_dinosaurcatalogue(self,dino):
        species=int(input("Jurassic Park has currently 8 different species of dinosaurus.\nPlease choose the number below of the one you'd like to read about:\n1.T-Rex\n2.Velociraptor\n3.Brachiosaurus\n4.Triceratops\n5.Compsognatus\n6.Gallimimus\n7.Stegosaurus\n8.Stegosaurus\n"))

        print(f"The {dino[species][0]} is a {dino[species][1]} from {dino[species][2]} period. It's a {dino[species][3]} that used to live in {dino[species][4]}. {dino[species][5]}")
        
        askifrestart = Restart(user)
        return askifrestart.restart()

    def visitor3_attractions(self):
        print("\nJurassic Park has many options for its visitors. Please find below some of them\n1.Park Ride\n2.Lab Cinema with Mr DNA\n3.Helicopter Ride\n4.Above ride with Jurassic Monorail\n5.Museum\nMany others! Get our Booklet in the Visitor Center and explore all options of Jurassic Park!\n")

        askifrestart = Restart(user)
        return askifrestart.restart()

    def visitor_execucao(self):
        if self.choice == 1:
            return self.visitor1_knowthepark()
        elif self.choice ==2:
            return self.visitor2_dinosaurcatalogue(dinodictionary)
        else:
            return self.visitor3_attractions()

class Restart: #Ok - Pergunta se quer continuar navegando
    def __init__(self,user):
        self.user = user
    
    def restart(self):
        finish = input("Would you like to navegate anymore through our sistem? Answer Yes or No\n")
        if finish == "yes" or finish == "Yes" or finish == "YES":
            rollmenuagain = MenuRoll(self.user)
            return rollmenuagain.execute()

        else:
            return "Thank you for using Jurassic Park's interactive system"

teste3=VisitorsMenu(execucao.execute())
print(teste3.visitor_execucao())