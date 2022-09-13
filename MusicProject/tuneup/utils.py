
def cast(model_instance):
    """ Casts model instance to last class in the inheritance hierarchy. """
    
    instance = None
    inheritance = model_instance.__class__.__subclasses__()
    
    for model in inheritance:
        
        label = model._meta.label_lower.split('.')[-1]
        
        instance = getattr(model_instance, label, None)
        
        if instance is not None:
            break
    
    return cast(instance) if instance else model_instance