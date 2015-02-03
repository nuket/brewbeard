# Shorthand

SENSOR_MAPPING = {
    'temperature': {
        'mash-lauter-tun': '/dev/sensorX',
        'boil-kettle':     '/dev/sensorY',
        'fermentor-a':     '/dev/sensorF',
        'fermentor-b':     '/dev/sensorB'
    }
    
}

RELAY_MAPPING = {
    'boil-kettle-1': '/dev/gpio/Y',
    'boil-kettle-2': '/dev/gpio/1',
    'boil-kettle-3': '/dev/gpio/3',
    'chugger-pump':  '/dev/gpio/X',
    'vent-fan-1':    '/dev/gpio/VF1',
    'vent-fan-2':    '/dev/gpio/VF2'
}
