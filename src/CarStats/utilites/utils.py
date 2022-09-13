import sys

def unmask(label, *args, **kwargs):
    """Check arguments and return some arbitrary data with the label 'label'.
    to FIX!
    """

    data = kwargs.get(label, None)
    
    return data

def check(name, select, *options):                                      
    """Check if a select is in the list of options. If not raise ValueError     
                                                                                
    **Arguments:**                                                              
                                                                                
    name                                                                        
         The name of the argument.                                              
                                                                                
    select                                                                      
         The value of the argument.                                             
                                                                                
    options                                                                     
         A list of allowed options.                                             
    """                                                                         
    if select not in options:                                                   
        formatted = ", ".join([f"'{option}'" for option in options])            
        raise ValueError(f"The argument '{name}' must be one of: {formatted}") 
    
