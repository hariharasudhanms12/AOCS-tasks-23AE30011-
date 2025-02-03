import control
import matplotlib.pyplot as plt
import numpy
import math

# noise addition (gaussian noise)
def noise_adder(y_arr):
    for i in range(0,len(y_arr)):
        noise = numpy.random.normal(0, 0.02)
        #print(noise)
        y_arr[i] += noise

def ramp_input(slope, y_intercept, time):
    output = []
    for x in range(len(time)):
        output.append(slope*time[x] + y_intercept)
    return output

# defining complex frequency
s = control.TransferFunction.s

# defining the given transfer function
system_tf = 1/(s**3 + (3*s**2) + 5*s + 1)

# gain parameters

# # the below gain parameters make the system stable but they have a significant phase lag
# Kp = 4.5
# Ki = 1
# Kd = 1.1

# the below gain parameters reduce phase lag but make the system overshoot a bit more
Kp = 17
Ki = 30
Kd = 11

controller_tf = Kp + (Ki/s) + s*Kd

# H is closed loop transfer function
closed_tf = control.feedback(controller_tf*system_tf, 1)

t = numpy.linspace(1,10,500) # this creates 500 equally spaced datapoints between 1 and 10 
t,y = control.step_response(closed_tf, T = t) # gives the step response of the function
noise_adder(y)

t,y1 = control.forced_response(closed_tf, T = t, U = t) # gives the step response of the function
noise_adder(y1)

t,y2 = control.forced_response(closed_tf, T = t, U = numpy.sin(t)) # gives the step response of the function
noise_adder(y2)

orig_sine = numpy.sin(t)
orig_ramp = ramp_input(1, 0, t)
orig_step = [1 for c in range(0, len(t))]

plt.figure(figsize=(20,10))
plt.plot(t, y, label = 'step response')
plt.plot(t, y1, label = 'ramp response')
plt.plot(t, y2, label  = 'sinusoidal response')
plt.plot(t, orig_sine, label = 'original sine wave')
plt.plot(t, orig_ramp, label = 'original ramp input')
plt.plot(t, orig_step, label = 'original step')
plt.xlabel('time (in s)')
plt.ylabel('response')
plt.grid()
plt.show()


# integral = 0

# def pid_controller(error_now,error_prev,kp,ki,kd):
#     global integral
#     timestep = 30/1500
#     proportional = kp*error_now
#     integral += ki*error_now*timestep
#     derivative = kd*(error_now - error_prev)/timestep
#     u = proportional + integral + derivative

#     return u

# s = control.TransferFunction.s

# plant_tf = 1/(s**3 + (3*s**2) + 5*s + 1)

# Kp = 1
# Ki = 3
# Kd = 1

# t = numpy.linspace(1,30,1500)

# t,y = control.step_response(plant_tf, T = t)

# setpoint = 1
# error = []

# for i in range(0,len(y)):
#     noise = numpy.random.normal(0, 0.001)
#     print(noise)
#     y[i] += noise
#     error.append(setpoint - y[i])
#     if i == 0:
#         y[i] += pid_controller(error[i], error[i], Kp, Ki, Kd)
#     else:
#         y[i] += pid_controller(error[i], error[i-1],Kp, Ki, Kd)


# plt.figure(figsize = (16,8))
# plt.plot(t,y, label = 'unit step response')
# plt.xlabel('time (in s)')
# plt.ylabel('response')
# plt.grid()
# plt.show()