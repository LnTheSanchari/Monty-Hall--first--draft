# -*- coding: utf-8 -*-

import random
from tqdm import tqdm

class monty_hall():

    def __init__(self, k:int) -> None:
        """
        Instance of monty hall has following attributes:
            
        doors: list of closed doors.
        car_door: which numbered door has car behind it.
        info: info of doors.
        """
        doors = [i for i in range(1, k+1)] # list of doors.
        car_door = random.choice(doors)
        info = {num:'car' if car_door==num else 'goat' for num in doors}
        self.doors = doors
        self.car_door = car_door
        self.info = info


    def open_door(self, r:int, user_choice:int) -> None:
        """
        On a given instance of monty hall, we randomly open 'r' doors.
        Care must be taken, because must not open car door.
        """
        assert 0 < r <= len(self.doors)-2, 'Monty opens at most 2 less than current avail doors.'
        if user_choice == self.car_door:
            valid_choice = [i for i in self.doors
                            if (i != self.car_door)
                            ]
            monty_choice = random.sample(valid_choice, k=r)
        else:
            #user choice is differnt from car door.
            valid_choice = [i for i in self.doors
                            if (i != user_choice and i!=self.car_door)
                            ]
            monty_choice = random.sample(valid_choice, k=r)
        #Now remove those doors in monty_choice.
        #this is equivalent to monty opening those doors.
        for door in monty_choice:
            (self.doors).remove(door)

    #method for user to change the user choice.
    def exchange_door(self, user_choice) -> int:
        #except his choice all other valid choices.
        valid_choice = [i for i in self.doors if i != user_choice]
        return random.choice(valid_choice)

    def __repr__(self):
        return f"monty_hall(doors: {self.doors})"

def monty_expt(trials, switch1: bool, switch2):
    # In each trial we get an instance of monty hall.
    success=0
    for trial in tqdm(range(trials)):
        monty_inst = monty_hall(10)
        user_choice = random.choice(monty_inst.doors)
        #one user made his choice, monty opens the door.
        monty_inst.open_door(4, user_choice)
        #in this version, monty opens only one door.
        if switch1:
            user_choice = monty_inst.exchange_door(user_choice)
        #first phase is done.

        #monty opens second set of 4 doors.
        monty_inst.open_door(4, user_choice)

        if switch2:
            user_choice = monty_inst.exchange_door(user_choice)
        #second phase is done.

        #at this point, monty open user choice, if it's car door then success

        if user_choice == monty_inst.car_door:
            success+=1
    return success/trials

# monty_expt(3_00_000, True, False) #Theo: 18%

# monty_expt(3_00_000, True, True) #Theo: 82%

# monty_expt(3_00_000, False, True) #Theo: 90%

# monty_expt(3_00_000, False, False) #Theo: 10%