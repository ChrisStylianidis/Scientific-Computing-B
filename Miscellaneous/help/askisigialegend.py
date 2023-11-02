
legd = ['dx=0.05','dx=0.10','dx=0.15','dx=0.20']
comm = ['b--',     'm--',     'g-',   'k--']
for i in range(ntries):
        plt.plot(xvalues,yvalues,comm[i],label=legd[i]) 
    
plt.title("Solution to the differential equation: $\frac{dy}{dx} = y^2+1$")


plt.legend(loc='best')
plt.show()

