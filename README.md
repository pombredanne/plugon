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

| Name | Type | Description | Default |
| :----- | :----- | :----- | :----- |
| function | `FunctionType` | Function will be contained by Plug object. | Required |
| args | `tuple` | Function args. | `()` |
| kwargs | `dict` | Function kwargs. | `{}` |
| urgency | `int` | Plugs which are registered to system will be ordered by urgency (ASC) before loop. | `10` |
| repeatable | `bool` | If repeatable is False, plug will run only once. | `True` |
| repeat | `int` | Plug's repetition count. | `None` |



## License

```
The MIT License (MIT)

Copyright (c) 2016 Ertuğrul Keremoğlu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```