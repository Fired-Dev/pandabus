# PandaBus

This library provided a simple event bus.

## Using Example

### #1：Basic Using

```python
from pandabus import bus

# Create to event listener(printb should called after printa)
@bus.listen("print")
def printa(ent):
    print(f"hello from printa")
@bus.listen("print",after="printa")
def printb(ent):
    print(f'hello from printb')



# send event
bus.send("print")
```

### #2：Pro Using

```python
from pandabus import bus, Event


class StaticEvent(Event, static=True):
    msg: str
class DynaEvent(Event, cancelable=True):
    msg:str

# Create to event listener(printb should called after printa,printc)
@bus.listen(StaticEvent)
def printa(ent):
    print(f"{ent.msg} from printa")
@bus.listen(StaticEvent)
def printb(ent):
    print(f"{ent.msg} from printb")
@bus.listen(StaticEvent, after=["printa","printb"])
def printc(ent):
    print(f'{ent.msg} from printc')
@bus.listen(DynaEvent)
def printd(ent):
    print(f"{ent.msg} from printd")
    ent.cancel()
@bus.listen(DynaEvent,after="printd")
def printe(ent):
    print(f"{ent.msg} from printe")



# send event
bus.send(StaticEvent,"hello")
bus.send(DynaEvent,"hello again")
```

### #3：Own Bus?

```python
from pandabus import buses, Bus

bus1 = buses.bus1  # Simplely get a own bus.
bus2 = Bus("bus2")  # Work too.
```