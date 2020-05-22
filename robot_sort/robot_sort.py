class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        
        # understand
        # this felt really complicated at first but we just have to sort this output somehow using the functions that are already aviable to me that are defined earlier in this robot class.

        # the buttom 3 methods seem useless, I can't find in the instructions why the light would want to be on? And the word 'light' is not anywhere in the test file, I can just ignore these.

        # I thought the top 2 method's were useless as well, as trying to move and checking to move both return False, so why would u ever check?
        # But then I realized I can turn the light on and off to signal to other functions to run or not run to help sort the nodes. And checking to see if you can move left or right, just checks if you are at the start or end of the array without having to try to move.

        # plan
        # I'm not going to assume we're lucky enough to start at the beginning of the array, even though thats the most likely scenario, we have no way of knowing our location, so i'm starting with the assumption we are in the middle of the array, and not holding an item. 
        # I'm going to use 3 while loops, the first one to turn the light on. The seconed one to run if we have a node that is greater than the last node and unsorted. And the third loop to do the same thing but with a lesser node. The 2nd and 3rd while loops check to see if the light from the first while loop is on before they run their functions, and turn the light off when they are finished so we know they have ran.

        # exicute
        while self.light_is_on() == False: # if the lights off, turn it on so we know we are NOT currently holding an unsorted node and we need the rest of the methods in this while loop to be performed.
            self.set_light_on() 
            
            while self.can_move_right() == True: # check if ur not at the end of the array. 
                self.swap_item() # if you are not, swap your item to pick one up. We don't want to pick up the last item in the array, so this makes sure we don't do that. And if this is the 2nd time this function is ran, we are picking up the bigger number.
                self.move_right() # and then actually move right while holding your item. If this is not the first time this is ran, then we know we are holding a number bigger than the previous number.

                # so lets check if its bigger than the new number in front of us since we just moved right.
                if self.compare_item() == 1: # if the compare item function returns 1, that means the item in our hand is greater than the item in front of us.
                    self.swap_item() # pick up the smaller node
                    self.set_light_off() # turn the light off to show that we are currently in the process of sorting, we are holding an unsorted node and other functions should not be ran until this number is in the next best position. This also restarts the while loop. And at the start, we will do a swap, so that will pick up the greater number that we just set down and then move it to the right, and then recompare it to the next number.

                # if self.compare_item() != 1 then the item in our hands is less than the one in front of us. I would specify this in code with an if statement, but we don't really need to because the while loop takes care of it, and if self.compare_item() == 0 then it doesn't matter what we do because the numbers are equal anyway.    
                self.move_left() # so lets go left since thats were the smaller numbers go
                self.swap_item() # then swap the items to set down the smaller number and pick up a new number
                self.move_right() # the move right so when the while loop restarts we can compare again.

                # so the goal of this first loop to always put down the greater node and always pick up the lesser node, but at the start, do a swap and move right, so the greater node is always moving right.
            
            # the 2nd loop is going to the do the same but to the right, and it will run if the light is still on, which means self.compare_item() returned less than 1. Which means we are holding a number that is currently greater than the one in front of us.
            while self.can_move_left(): # if you can move left
                self.swap_item() # put down the old item and pick up a new one.
                self.move_left() # and then actually move left
               
                if self.compare_item() == -1: # if the compare item function returns -1 that means the item in our hand is greater than the one in front of us.
                    self.swap_item() # pick up the greater node.
                    self.set_light_off() # turn the light off to show that we are currently in the process of sorting, we are holding an unsorted node and other functions should not be ran until this number is in the next best position. This also restarts the while loop.
                    
                self.move_right() # go back to the right
                self.swap_item() # set down the item we just got information about and pick up a new one.
                self.move_left() # go back to the left again, since the start of the while loop moves you right if you are able to, so we need to cancel that out when the loop restarts.
                

    # review 
    # I know there was probably a much easier way to do this and my head hurts, I spent most of the time during the sprint on this, but the only real hard part was not thinking about it so linearly. Since I started the while loop with checking and moving to the right, the rest of the code reflects and expects that, which was difficult to properly think through. 


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)