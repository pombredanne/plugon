# Plugon

Plugon is a lightweight and simple loop engine which is made for building efficient and clean architecture for applications such as servers, clients, bots, etc.



## Installation
 
 
```sh
$ pip install plugon
```



## How it works?

Functions will be contained by Plug objects. Plug objects will be registered to System object.


```python
from plugon import System, Plug

class Application():

    def __init__(self):
        self.system = System()
        
        self.system.register(
            plug = Plug(self.first, urgency = 1, repeatable = False),
        )
        
        self.system.register(
            plug = Plug(self.second, urgency = 2, repeat = 5),
        )
        
        self.system.register(
            plug = Plug(self.third, urgency = 3),
        )
    
    def first(self):
        pass
    
    def second(self):
        pass
    
    def third(self):
        pass
    
    def main(self):
        self.system.run()
```



### Plug parameters

- function (FunctionType): Function will be contained by Plug object. (Required)
- args (tuple): Function args. (Default: ())
- kwargs (dict): Function kwargs. (Default: {})
- urgency (int): Plugs which are registered to system will be ordered by urgency (ASC) before loop. (Default: 10)
- repeatable (bool): If repeatable is False, plug will run only once. (Default: True)
- repeat (int): Plug's repetition count. (Default: None)



## License

MIT
