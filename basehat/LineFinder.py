# for LineFinder, follow this code (search for LineSensor):
# https://github.com/gpiozero/gpiozero/blob/master/gpiozero/input_devices.py

# For most of these, you will simply just need to rename the class to make the name simpler.
# You may change property namees/functions to be more consistent or easier to remember, but 
# that is not 100% necessary all the time.
# If you are confused on how the class works, consider changing it to be more intuitive
# so it is also easier for students

<<<<<<< HEAD
from gpiozero import LineFinder
from signal import pause

class LineFinder(SmoothedInputDevice):
    """
    Extends :class:`SmoothedInputDevice` and represents a single pin line
    sensor like the TCRT5000 infra-red proximity sensor found in the `CamJam #3
    EduKit`_.

    A typical line sensor has a small circuit board with three pins: VCC, GND,
    and OUT. VCC should be connected to a 3V3 pin, GND to one of the ground
    pins, and finally OUT to the GPIO specified as the value of the *pin*
    parameter in the constructor.

    The following code will print a line of text indicating when the sensor
    detects a line, or stops detecting a line::

        from gpiozero import LineSensor
        from signal import pause

        sensor = LineSensor(4)
        sensor.when_line = lambda: print('Line detected')
        sensor.when_no_line = lambda: print('No line detected')
        pause()

    :type pin: int or str
    :param pin:
        The GPIO pin which the sensor is connected to. See :ref:`pin-numbering`
        for valid pin numbers. If this is :data:`None` a :exc:`GPIODeviceError`
        will be raised.

    :type pull_up: bool or None
    :param pull_up:
        See description under :class:`InputDevice` for more information.

    :type active_state: bool or None
    :param active_state:
        See description under :class:`InputDevice` for more information.

    :param int queue_len:
        The length of the queue used to store values read from the sensor. This
        defaults to 5.

    :param float sample_rate:
        The number of values to read from the device (and append to the
        internal queue) per second. Defaults to 100.

    :param float threshold:
        Defaults to 0.5. When the average of all values in the internal queue
        rises above this value, the sensor will be considered "active" by the
        :attr:`~SmoothedInputDevice.is_active` property, and all appropriate
        events will be fired.

    :param bool partial:
        When :data:`False` (the default), the object will not return a value
        for :attr:`~SmoothedInputDevice.is_active` until the internal queue has
        filled with values.  Only set this to :data:`True` if you require
        values immediately after object construction.

    :type pin_factory: Factory or None
    :param pin_factory:
        See :doc:`api_pins` for more information (this is an advanced feature
        which most users can ignore).

    .. _CamJam #3 EduKit: http://camjam.me/?page_id=1035
    """
    def __init__(self, pin=None, *, pull_up=False, active_state=None,
                 queue_len=5, sample_rate=100, threshold=0.5, partial=False,
                 pin_factory=None):
        super().__init__(
            pin, pull_up=pull_up, active_state=active_state,
            threshold=threshold, queue_len=queue_len,
            sample_wait=1 / sample_rate, partial=partial,
            pin_factory=pin_factory)
        self._queue.start()

    @property
    def value(self):
        """
        Returns a value representing the average of the queued values. This
        is nearer 0 for black under the sensor, and nearer 1 for white under
        the sensor.
        """
        return super().value

    @property
    def line_detected(self):
        return not self.is_active



LineSensor.when_line = LineSensor.when_deactivated
LineSensor.when_no_line = LineSensor.when_activated
LineSensor.wait_for_line = LineSensor.wait_for_inactive
LineSensor.wait_for_no_line = LineSensor.wait_for_active

=======
# Noah
>>>>>>> 34df1b802ac43b94d01cac23be360f40d9e50010
