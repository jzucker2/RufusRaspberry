# RufusRaspberry

## Prereqs

Raspberry Pi is currently installing python 3.7.3 by default.

### Set up

```
pip install -r requirements.txt
```

## Example Usage

```
python3 http_cli.py all-off

```

## Example URI

```
http://10.0.1.104:5000/api/v1/activities/all-off?kitchen=0&dining_room=0
```

### Raspberry Pi References

For how to handle buttons, click [here](https://gpiozero.readthedocs.io/en/stable/recipes.html#button)

For [headless pi setup, I'm using the rc.local method here](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/)

#### Headless Pi

Make sure to add to `/etc/rc.local` the following:

```
# living room
sudo python3 /home/pi/Documents/RufusRaspberry/living_room_cli.py &

# dining room
sudo python3 /home/pi/Documents/RufusRaspberry/dining_room_cli.py &

# kitchen
sudo python3 /home/pi/Documents/RufusRaspberry/kitchen_cli.py &
```

#### Pin References

![GPIOZero pin reference diagram](https://gpiozero.readthedocs.io/en/stable/_images/pin_layout.svg)

[Source from here for pin references for GPIOZero](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering)
