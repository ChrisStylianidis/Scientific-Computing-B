
#def TDeriv():#edw vazeis tin epitaxinsi(a)(tin paragogo aftou pou thes)

def Euler(V0, t0, t, dt):
    time     = t0        
    v        = V0            
    Velocity = []            
    Time     = []           
    while time < t:        
        Velocity.append(v)    
        Time.append(time)
        dudt = TDeriv()                
        v = v + dudt * dt                  
        time = time + dt
    return Time, Velocity

def EulerCromer(Vinit, t0, tfin, dt):
    time     = t0
    v        = Vinit     
    Velocity = []          
    Time     = []            
    while time < tfin:        
        Velocity.append(v)    
        Time.append(time)
        dudt    = TDeriv(v)               
        v_new   = v + dudt * dt               
        dudt    = TDeriv(v_new)            
        v       = v + dudt * dt                 
        time = time + dt                      

    return Time,Velocity
