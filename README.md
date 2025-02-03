# AOCS-tasks-23AE30011-
Task 1.1: Developing a PID controller for a complex system
The below shows the step by step process that I used to try to build a 1D speed controller for a motorboat. 
Step1: PID control of a DC motor

Where, 
ea = Applied voltage to the motor
Ra = Armature resistance of motor
La = Armature inductance of motor
J = Moment of inertia of armature coil (Armature is the rotating part. Thus, J is the moment of inertia of the armature coil) 
eb = Back EMF
KT = Torque constant of motor
B = Motor damping coefficient
Tm = Motor torque

On taking the Laplace transform of the above equations, we get the following.


Simplifying the above equations, we get
 

The below is the entire model of the DC motor PID control.



The below are the PID coefficients.




The following are the system response vs ramp input, unit step input, pulse input and sinusoidal input respectively.


Step2: Modelling the angular velocity the propeller to linear velocity of the boat and taking laplace transform on both sides,


Step3:  Modelling the transfer function for the boat 


Taking Laplace transform on both sides.


After implementing these in Simulink, this is what the model looks like.






The constants used in the above model are defined in a separate .m file
However, the above did not work. The step response of the system was diverging as time increased.

Alternative approach:
The below are my handwritten equations. These equations were directly modelled in Simulink.



This is the Simulink model.
 

This is the Motorboat dynamics subsystem from the previous picture.


These are the system parameters. 

The following are the system response vs unit step input, ramp step input, and sinusoidal input impulse input respectively.



There is a problem here. When the desired speed is of the form of a step function, the system response follows it for half a cycle and then it stays at zero. I am unable to think of a reason and fix it.

Whereas, in the case of an impulse function, the system response has a lot of oscillations. 














Task 1.2: Deriving the transfer function for a higher order system








Task 1.3: Designing a PID controller for a given system
The transfer function of the given plant is 
𝐺(𝑠) = 1/(𝑠3 + 3𝑠2 + 5𝑠 + 1)
The task is done with the help of the control module in python.
The complex frequency variable is first defined, followed by the transfer function and the feedback loop.
This feedback loop is used to obtain the step response. The function, control.step_response() returns two arrays 
Gaussian noise is added which makes the fluctuations symmetric about the mean. 
