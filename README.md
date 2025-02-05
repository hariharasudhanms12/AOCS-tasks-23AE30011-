# Task 1.3: Designing a PID controller for a given system
The transfer function of the given plant is 
𝐺(𝑠) = 1/(𝑠3 + 3𝑠2 + 5𝑠 + 1)

The task is done with the help of the control module in python. The complex frequency variable is first defined, followed by the transfer function of the system, transfer function of the controller and the feedback loop. This feedback loop is used to obtain the step response. 

The function, control.step_response() returns two arrays which denote the time and system step response output. Similarly, the function, control.forced_response() is used to obtain the unit ramp and sinusoidal reponses.

Noise is added to the system output which makes the fluctuations symmetric about the mean.

The updated system output along with input signals (unit step, unit ramp, sinusoidal) is then plotted using matplotlib.

# Alternative approach (that did not work)
This approach obtains the open loop system output for a unit step response and stores it in an array. Noise is added to this array of open loop outputs. 

Then a separate pid_controller function is defined which calculates the PID input using the updated array (array was updated with noise) and the setpoint (1 for unit step response).

However, this approach did not work. The derivative term in the PID output amplified the noise and thus caused irregular oscillations in the system response.

For detailed documentation of other tasks, refer https://docs.google.com/document/d/1H4a6S2VNPJjz3OR8h_iWlZKPtPQp9CI9E5nP6w5oi8U/edit?tab=t.0
