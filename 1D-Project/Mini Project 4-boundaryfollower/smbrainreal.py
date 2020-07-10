from pythymiodw import *
from pythymiodw import io
from pythymiodw.sm import *
from libdw import sm
from boxworld import thymio_world


class MySMClass(sm.SM):
    start_state = 0

    def get_next_values(self, state, inp):
        # These two lines is to stop the robot
        # by pressing the backward button.
        # This only works when using the real robot.
        # It will not work in simulator.
        if inp.button_backward:
            return 'halt', io.Action(0, 0) # (forward velocity, rotational velocity)
        #####################################

        # ground = inp.prox_ground.reflected
        # ground = inp.prox_ground.ambiant

        ground = inp.prox_ground.delta
        print(ground)
        try:
            left = ground[0]
            right = ground[1]
        except:
            left = -1
            right = -1
        print(left,right)
        print(state)
        
        if left >= 255 and right >= 255:
            if state == 0:
                return 0, io.Action(fv=0.05, rv=0.0)
            else:
                return 3, io.Action(fv=0.0, rv=-1)

        if left < 255:
            return 1, io.Action(fv=0.0, rv = 1)

        if left >= 255 and right < 255:
            return 2, io.Action(fv=0.05, rv=0.0)

    #########################################
    # Don't modify the code below.
    # this is to stop the state machine using
    # inputs from the robot
    #########################################
    def done(self, state):
        if state == 'halt':
            return True
        else:
            return False

MySM = MySMClass()

############################

m = ThymioSMReal(MySM, thymio_world)#, scale=2)
try:
    m.start()
except KeyboardInterrupt:
    m.stop()
