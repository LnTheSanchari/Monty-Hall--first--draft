# -*- coding: utf-8 -*-

import random
from tqdm import tqdm

class MontyHall():

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

def generalized_monty_hall(trials,
        N_doors,
        phases, *,
        doors_opened_per_phase: list[int],
        user_choices: list[bool] ):
    """
    trials: Number of trials in this simulation.
    N_doors: Total number of doors.
    phases: The number of phases monty goes through.
    doors_opened_per_phase:
    Each index indicates number of doors monty opens in that phase.
    user_choices:
    Each index indicates whether the user switches after each phase.
    """
    
    # Note: user_choices is a boolean array indicating
    # whether the user switches after each phase.

    # since the game ends with exactly two doors remaining.
    assert len(user_choices) == phases

    # Each phase must specify how many doors Monty opens.
    assert len(doors_opened_per_phase) == phases

    # Monty opens all but two doors, leaving the user's door
    # and exactly one other unopened door.
    assert sum(doors_opened_per_phase) == N_doors - 2

    # Now we are good to go.
    success = 0

    # For each trial, go through each phase.
    for trial in tqdm(range(trials)):

        # Initialize a Monty Hall instance.
        monty_inst = MontyHall(N_doors)

        # User randomly picks a door.
        user_choice = random.choice(monty_inst.doors)

        for index in range(phases):

            # Open the specified number of doors in this phase.
            monty_inst.open_door(
                doors_opened_per_phase[index],
                user_choice
            )

           # After each phase, user decides whether to switch.
            if user_choices[index]:
                user_choice = monty_inst.exchange_door(user_choice)

        # Check whether the user's final choice is the car door.
        if user_choice == monty_inst.car_door:
            success += 1

    return success / trials
