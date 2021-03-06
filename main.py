# The Clinic.Inc 馃彞
# by Maja & Janek
 
from Doctor import Doctor
from Queue import Queue
from mainHelpers import Helpers
from LearningStuff.projekt import Classifier
import matplotlib.pyplot as plt
import numpy as np
import time

# Documentation !

#      WSZYSTKO JEST SKROCONE 
# __ WSZYSTKO DZIEL PRZEZ 100 __
#       8h = 28 800 sekund
#       288 sek ~ 4.8 minuty

# Za艂o偶enia odno艣nie pacjent贸w
# Doktor, kt贸rego: Pacjent ze zdefiniowanym lekkim przebiegiem choroby b臋dzie potrzebowa艂 10 min przy odpowiadaj膮cym mu okienku. Czas dotarcia do okienka b臋dzie wynosi艂 10sek.
# Doktor, kt贸rego: Pacjent ze zdefiniowanym 艣rednim przebiegiem choroby b臋dzie potrzebowa艂 20 min przy odpowiadaj膮cym mu okienku. Czas dotarcia do okienka b臋dzie wynosi艂 20sek.
# Doktor, kt贸rego: Pacjent ze zdefiniowanym ci臋偶kim przebiegiem choroby b臋dzie potrzebowa艂 30 min przy odpowiadaj膮cym mu okienku. Czas dotarcia do okienka b臋dzie wynosi艂 30sek.
# Doktor multi, kt贸rego: Pacjent b臋dzie potrzebowa艂 15 min przy odpowiadaj膮cym mu okienku. Czas dotarcia do okienka b臋dzie wynosi艂 20sek.

if __name__ == "__main__":

    # Helpers
    helpers = Helpers()

    # Stats
    examinatedStats = []
    NOT_ExaminatedStats = []
    simulantsStats = []
    firstQTotalStats = []
    secondQTotalStats = []
    thirdQTotalStats = []
    fourthQTotalStats = []

    # Making the 5/7 work week iteration
    week_label = ['Monday', 'Tuesaday', 'Wednesday', 'Thursday', 'Friday']

    for day in range(5):

        print("--------------------------------")
        print(f"馃尀 Starting {week_label[day]} 馃寵")
        print("--------------------------------")

        # Classifier
        print("馃 The group of people is gathering. Beata is classifing now...")
        time.sleep(3)
        classifier = Classifier()
        model = classifier.create_model()
        classifiedPatientsAll = classifier.get_patient(model)
        print("Beata classified them, some of them are symuluj膮cy 馃ジ")
        print("Beata is kicking out symuluj膮cych 馃Φ馃徎")
        time.sleep(5)
        classifiedPatientsFiltered = [x for x in classifiedPatientsAll if x != 0]
        patientsSimulants = len(classifiedPatientsAll) - len(classifiedPatientsFiltered)
        print("Patients are ready to be przebadani!")
        time.sleep(5)
        print("----[]-----[]-----[]----[]--<-<-\(+_+)/")

        #Define time counters for each queue
        firstTimer = 0
        secondTimer = 0
        thirdTimer = 0
        fourthTimer = 0

        # Doctors
        # Lekarze randomowo obs艂uguja r贸nych pacjent贸w
        firstDoctor = Doctor()
        secondDoctor = Doctor()
        thirdDoctor = Doctor()
        forthDoctor = Doctor()

        doctorsColletion = [
            firstDoctor,
            secondDoctor,
            thirdDoctor,
            forthDoctor
        ]

        #Queue
        firstQueue = Queue(queue=[])
        secondQueue = Queue(queue=[])
        thirdQueue = Queue(queue=[])
        forthQueue = Queue(queue=[])

        queueColection = [
            firstQueue,
            secondQueue,
            thirdQueue,
            forthQueue
        ]

        # Given all of the patients the right identity
        IdentifiedPatients = [helpers.convertPatient(x) for x in classifiedPatientsFiltered]

        def sortValue(p):
            return p.serviceTotalTime

        IdentifiedPatients.sort(key=sortValue)

        # Moving patients to right queue
        firstQueue.queue = IdentifiedPatients[0::4]
        del IdentifiedPatients[0::4]

        secondQueue.queue = IdentifiedPatients[0::3]
        del IdentifiedPatients[0::3]

        thirdQueue.queue = IdentifiedPatients[0::2]
        del IdentifiedPatients[0::2]

        forthQueue.queue = IdentifiedPatients

        # Starting work day
        end_time = helpers.defineWorkingHours()
        while(time.time() < end_time):

            if firstDoctor.isFreeToTakeNewPatient() and helpers.isAnyoneInQueue(firstQueue.queue):
                patient = firstQueue.takeFirstToDoctor(doctor=firstDoctor)
                firstTimer += patient.serviceTotalTime
                print(f"- (D1 馃懆馃徎鈥嶁殨锔?) Currently the patient {patient.name} is badany -")
            
            if secondDoctor.isFreeToTakeNewPatient() and helpers.isAnyoneInQueue(secondQueue.queue):
                patient = secondQueue.takeFirstToDoctor(doctor=secondDoctor)
                secondTimer += patient.serviceTotalTime
                print(f"- (D2 馃懆馃徔鈥嶁殨锔?) Currently the patient {patient.name} is badany -")
            
            if thirdDoctor.isFreeToTakeNewPatient() and helpers.isAnyoneInQueue(thirdQueue.queue):
                patient = thirdQueue.takeFirstToDoctor(doctor=thirdDoctor)
                thirdTimer += patient.serviceTotalTime
                print(f"- (D3 馃懇馃徏鈥嶁殨锔?) Currently the patient {patient.name} is badany -")
            
            if forthDoctor.isFreeToTakeNewPatient() and helpers.isAnyoneInQueue(forthQueue.queue):
                patient = forthQueue.takeFirstToDoctor(doctor=forthDoctor)
                fourthTimer += patient.serviceTotalTime
                print(f"- (D4 馃懇馃従鈥嶁殨锔?) Currently the patient {patient.name} is badany -")

        # Define the ending 
        print("The badania has finished, tasks completed.")

        totalOfPatientPrzebadanych = 0
        for doctor in doctorsColletion:
            totalOfPatientPrzebadanych += doctor.patientCount
        
        patientUnserviced = (len(classifiedPatientsAll) - (totalOfPatientPrzebadanych + patientsSimulants))
        print("--------SUMARRY--------------------------------------------")
        print(f"Total of patient przebadanych: {totalOfPatientPrzebadanych}")
        print(f"Total of patient NIEprzebadanych: {patientUnserviced}")
        print(f"Total of patient symulant贸w: {patientsSimulants}")
        print(f"1 - First queue total time: {firstTimer}")
        print(f"2 - Second queue total time: {secondTimer}")
        print(f"3 - Third queue total time: {thirdTimer}")
        print(f"4 - Fourth queue total time: {fourthTimer}")

        examinatedStats.append(totalOfPatientPrzebadanych)
        NOT_ExaminatedStats.append(patientUnserviced)
        simulantsStats.append(patientsSimulants)
        firstQTotalStats.append(firstTimer)
        secondQTotalStats.append(secondTimer)
        thirdQTotalStats.append(thirdTimer)
        fourthQTotalStats.append(fourthTimer)

    # Plotting all the data from 5/7
    print("FINISHED")
    n=5
    r = np.arange(n)
    width = 0.25

    plt.bar(r, examinatedStats,
        width = width, edgecolor = 'black', label='Examined')
    
    plt.bar(r + width*2, simulantsStats,
        width = width, edgecolor = 'black', label='Simulants')
    
    plt.bar(r + width, NOT_ExaminatedStats,
        width = width, edgecolor = 'black', label='Not_Examined')
 
    plt.xlabel('Work day')
    plt.ylabel('Patients')
    plt.title('Stats of patients')
    plt.legend()

    plt.show()

