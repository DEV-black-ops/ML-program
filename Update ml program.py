


import plotly.graph_objs as go
import numpy as np

#sine wave with frequency 10hz 
F = 10
T = 2/F
Fs = 200
Ts = 1/Fs
N = int(T/Ts)

t = np.linspace(0, T, N)
signal = np.sin(2*np.pi*F*t)






#ploting sine wave 

sig = np.array(signal)
time= np.array(t)

fig = go.Figure()         
fig.add_trace(go.add_Scatter(x = time, y = sig, name = 'Sine wave', mode = 'lines', xaxis_title='time',yaxise_title= 'values')) 

fig.show()




#ploting local maximum of sine with green color

a=[0.025,0.128]
a=np.array(a)
b=[0.999,0.999]
b=np.array(b)

fig = go.Figure()         
fig.add_trace(go.add_Scatter(x = a, y = b, mode='marker', marker= 'Circle', marker_color= 'Green'))
fig.show()

#ploting local minimum of sine wave with red color

c=[0.076,0.174]
c=np.array(c)
d=[-0.999,-0.999]
d=np.array(d)

fig = go.Figure()         
fig.add_trace(go.add_Scatter(x = c, y = d, mode='marker', marker= 'Diamond', marker_color= 'Red'))
fig.show()

#ploting x intercepte with sine wave  
e=sin*0

fig = go.Figure()         
fig.add_trace(go.add_Scatter(x = time, y = e, mode='marker', marker= 'Square', marker_color= 'Black'))
fig.show()


fig.update_layout(
    title="Plot Title",
    xaxis_title="Time",
    yaxis_title="Values",
    
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="Black")



    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"))
    


fig.show()

