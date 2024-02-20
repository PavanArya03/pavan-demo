def outer():
    name="pavan"
    def inner():
        nonlocal name
        print(name)
        name="Bharadwaj"
        
    inner()
    print(name)

outer()    
   
    