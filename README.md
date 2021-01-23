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
