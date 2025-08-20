import numpy as np

#gaussian_noise = np.random.normal(mean, std_deviation, shape)



#Creating an independent variable

x = np.arange(0,100,1)



#Use a linear function to obtain the dependent variable

y = 0.3*x + 0.6

#Noise generation
noise = np.random.normal(0,2,len(x))



#Add the noise to the data

y_noised = y + noise



print(x)


print(y)


print(y_noised)