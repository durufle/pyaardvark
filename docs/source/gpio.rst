GPIO API
-------
The following enumerated type maps the named lines on the Aardvark I2C/SPI line to bit positions in the GPIO API.
All GPIO API functions will index these lines through an 8-bit masked value.  Thus, each bit position in the mask
can be referred back its corresponding line through the enumerated type.

.. py:method::  aa_gpio_direction(aardvark, direction_mask)

    Configure the GPIO, specifying the direction of each bit.

    :param aardvark: Aardvark handle
    :param direction_mask: Direction mask bit
    :return: status

    :notes: A call to this function will not change the value of the pullup mask in the Aardvark.
            This is illustrated by the following

            example:
                (1) Direction mask is first set to 0x00
                (2) Pullup is set to 0x01
                (3) Direction mask is set to 0x01
                (4) Direction mask is later set back to 0x00.

                The pullup will be active after (4).

                On Aardvark power-up, the default value of the direction mask is 0x00.

.. py:method::  aa_gpio_pullup(aardvark, pullup_mask)

    Enable an internal pullup on any of the GPIO input lines.

    :param aardvark: Aardvark handle
    :param pullup_mask: Pullup mask bit
    :return: status

    :notes: If a line is configured as an output, the pullup bit for that line will be ignored,
            though that pullup bit will be cached in case the line is later configured as an input.
            By default the pullup mask is 0x00.

