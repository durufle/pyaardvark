API Documentation
#################

Status Code
***********
All API functions return an integer which is the result of the transaction, or a status code if negative.
The status codes are defined as follows:
- enum AardvarkStatus
- General codes (0 to -99)

General Code (0 to -99)
-----------------------
.. py:data:: AA_OK
    :value: 0
.. py:data:: AA_UNABLE_TO_LOAD_LIBRARY
    :value: -1
.. py:data:: AA_UNABLE_TO_LOAD_DRIVER
    :value: -2
.. py:data:: AA_UNABLE_TO_LOAD_FUNCTION
    :value: -3
.. py:data:: AA_INCOMPATIBLE_LIBRARY
    :value: -4
.. py:data:: AA_INCOMPATIBLE_DEVICE
    :value: -5
.. py:data:: AA_COMMUNICATION_ERROR
    :value: -6
.. py:data:: AA_UNABLE_TO_OPEN
    :value: -7
.. py:data:: AA_UNABLE_TO_CLOSE
    :value: -8
.. py:data:: AA_INVALID_HANDLE
    :value: -9
.. py:data:: AA_CONFIG_ERROR
    :value: -10

I2C codes (-100 to -199)
------------------------

.. _config:

Configurations
**************
.. py:data:: AA_CONFIG_GPIO_ONLY
    :value: 0x00
.. py:data:: AA_CONFIG_SPI_GPIO
    :value: 0x01
.. py:data:: AA_CONFIG_GPIO_I2C
    :value: 0x02
.. py:data:: AA_CONFIG_SPI_I2C
    :value: 0x03
.. py:data:: AA_CONFIG_QUERY
    :value: 0x04

Methods
*******
.. py:method:: aa_find_devices(devices):

    Get a list of ports to which Aardvark devices are attached.

    :param devices: Number of devices to find
    :return: Returns the number of devices found, regardless of the array size

    :notes:

    - Each element of the array is written with the port number.Devices that are in-use are ORed with AA_PORT_NOT_FREE (0x8000).
    - If the array is NULL, it is not filled with any values. If there are more devices than the array size, only the first nmemb port numbers will be written into the array.


.. py:method:: aa_find_devices_ext(devices, unique_ids):

    Get a list of ports to which Aardvark devices are attached.

    :param devices: Number of devices to find
    :param unique_ids: Number of unique IDs

    :notes:

    - This function is the same as aa_find_devices() except that it returns the unique IDs of each Aardvark device.
    - The IDs are guaranteed to be non-zero if valid.

.. py:method:: aa_open(port_number):

    Open the Aardvark port.

    :param port_number: The port number is a zero-indexed integer.
    :return: Aardvark handle

    :notes:

    - The port number is the same as that obtained from the aa_find_devices() function.
    - Returns an Aardvark handle, which is guaranteed to be greater than zero if it is valid
    - This function is recommended for use in simple applications where extended information is not required.
      For more complex applications, the use of aa_open_ext() is recommended

.. py:method:: aa_open_ext(port_number):

    Open the Aardvark port, returning extended information

    :param port_number: The port number is a zero-indexed integer.
    :return: Aardvark handle and feature

    :notes: This function is recommended for use in complex applications where extended information is required. For more simple applications, the use of aa_open() is recommended.

.. py:method:: aa_port(aardvark):

    Return the port for this Aardvark handle.

    :param aardvark: Aardvark handle
    :return: the port for this Aardvark handle


.. py:method:: aa_unique_id(aardvark):

    Return the unique ID for this Aardvark adapter.

    :param aardvark: Aardvark handle
    :return: Unique ID

    :notes:

    - IDs are guaranteed to be non-zero if valid.
    - The ID is the unsigned integer representation of the
    - 10-digit serial number

.. py:method:: aa_status_string(status)

    Return the status string for the given status code.

    :param: status code
    :return: status string

    :notes:

        If the code is not valid or the library function cannot be loaded, return a NULL string.

.. py:method:: aa_version(aardvark)

    Return the version matrix for the device attached to the given handle

    :param aardvark: Aardvark handle
    :return: version matrix

    :notes:

    If the handle is 0 or invalid, only the software and required api versions are set.

.. py:method:: aa_configure(aardvark, config)

    Configure the device by enabling/disabling I2C, SPI, and GPIO functions.

    :param aardvark: Aardvark handle
    :param config: Configuration enum

    :return: status

    :ref:

.. py:method:: aa_target_power(aardvark, power_mask)

    Configure the target power pins.

    :param aardvark: Aardvark handle
    :param power_mask: Power configuration enum

    :return: status

.. py:method::  aa_sleep_ms(milliseconds)

    Sleep for the specified number of milliseconds

    :param milliseconds: Number of milliseconds to sleep
    :return: number of milliseconds slept

    :notes: Accuracy depends on the operating system scheduler
