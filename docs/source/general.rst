General API
-----------

.. py:method:: aa_find_devices(devices):

    Get a list of ports to which Aardvark devices are attached.

    :param devices: Number of devices to find
    :return: Returns the number of devices found, regardless of the array size

    :error codes:

    :details:
        Each element of the array is written with the port number. Devices that are in use are ORed with **AA_PORT_NOT_FREE** ( 0x8000 ).

        Example:

        Devices are attached to port 0, 1, 2
        ports 0 and 2 are available, and port 1 is in-use.
        array => 0x0000, 0x8001, 0x0002;
        If the input array is NULL, it is not filled with any values.

        If there are more devices than the array size (as specified by nelem ), only the first nelem port numbers will be written into the array.

    :notes:

        - Each element of the array is written with the port number.Devices that are in-use are ORed with **AA_PORT_NOT_FREE** (0x8000).
        - If the array is NULL, it is not filled with any values. If there are more devices than the array size, only the first nmemb port numbers will be written into the array.

.. py:method:: aa_find_devices_ext(devices, unique_ids):

    Get a list of ports to which Aardvark devices are attached.

    :param devices: Number of devices to find
    :param unique_ids: Number of unique IDs
    :return: This function returns the number of devices found, regardless of the array sizes.

    :error codes:

    :details:

    :notes:

        - This function is the same as aa_find_devices() except that it returns the unique IDs of each Aardvark device.
        - The IDs are guaranteed to be non-zero if valid.

.. py:method:: aa_open(port_number):

    Open the Aardvark port.

    :param port_number: The port is the same as the one obtained from function aa_find_devices.
                        It is a zero-based number.
    :return: This function returns an Aardvark handle, which is guaranteed to be greater than zero if valid.

    :error codes:

        - **AA_UNABLE_TO_OPEN**
                The specified port is not connected to an Aardvark device or the port is already in use.

        - **AA_INCOMPATIBLE_DEVICE**
                There is a version mismatch between the DLL and the firmware.
                The DLL is not of a sufficient version for interoperability with the firmware version or vice versa.
                See aa_open_ext() for more information.

    :details:

    :notes:

        - The port number is the same as that obtained from the aa_find_devices() function.
        - Returns an Aardvark handle, which is guaranteed to be greater than zero if it is valid
        - This function is recommended for use in simple applications where extended information is not required.
        - For more complex applications, the use of aa_open_ext() is recommended

.. py:method:: aa_open_ext(port_number):

    Open the Aardvark port, returning extended information

    :param port_number: The port number is a zero-indexed integer.
    :return: Aardvark handle and feature

    :error codes:

    :notes:

        - This function is recommended for use in complex applications where extended information is required.
        - For more simple applications, the use of aa_open() is recommended.

.. py:method:: aa_port(aardvark):

    Return the port for this Aardvark handle.

    :param aardvark: Aardvark handle
    :return: the port for this Aardvark handle

    :error codes:

    :details:

    :notes:

.. py:method:: aa_features(aardvark):

    Return Aardvark adapter features.

    :param aardvark: Aardvark handle
    :return: Adapter Features

    :error codes:

    :details:

    :notes:

.. py:method:: aa_unique_id(aardvark):

    Return the unique ID for this Aardvark adapter.

    :param aardvark: Aardvark handle
    :return: Unique ID

    :error codes:

    :details:

    :notes:

        - IDs are guaranteed to be non-zero if valid.
        - The ID is the unsigned integer representation of the
        - 10-digit serial number

.. py:method:: aa_status_string(status)

    Return the status string for the given status code.

    :param: status code
    :return: status string

    :error codes:

    :details:

    :notes:

        - If the code is not valid or the library function cannot be loaded, return a NULL string.

.. py:method:: aa_log(aardvark, level, handle)

    Enable logging to a file

    :param aardvark: Aardvark handle
    :param level: The logging detail level as described below
    :param handle: file handler descriptor
    :return: An Aardvark status code is returned with **AA_OK** on success.

    :error codes:

    :details:

        The handle must be standard file descriptor. In C, a file descriptor can be obtained by using the ANSI C
        function "open" or by using the function "fileno" on a FILE* stream. A FILE* stream obtained using fopen or can
        correspond to the common stdout or stderr available when including stdlib.h.

        The logging detail level can be one of the following options.

        #.  none
        #.  error
        #.  warning
        #.  info
        #.  debug

        Note that if the handle is invalid, the application can crash during a logging operation.

        Due to inconsistencies arising from how Microsoft handles linkage to the C runtime library, logging to a file
        may not work in Windows. However, logging to stdout and stderr is still supported. As a convenience, the
        following two constants are defined and can be passed as the handle argument.

        - AA_LOG_STDOUT
        - AA_LOG_STDERR

    :notes:

.. py:method:: aa_version(aardvark)

    Return the version matrix for the device attached to the given handle

    :param aardvark: Aardvark handle
    :return: version matrix

    :error codes:

    :details:

        If the handle is 0 or invalid, only the software version is set.
        See the details of aa_open_ext for the definition of AardvarkVersion.

    :notes:

.. py:method:: aa_configure(aardvark, config)

    Configure the device by enabling/disabling I2C, SPI, and GPIO functions.

    :param aardvark: Aardvark handle
    :param config: Configuration enum
    :return: The current configuration on the Aardvark adapter will be returned. The configuration will be described by
             the same values in AardvarkConfig.

    :error codes:
        - **AA_CONFIG_ERROR**
            The I2C or SPI subsystem is currently active and the new configuration requires the subsystem to be deactivated.

    :details:

        If either the I2C or SPI subsystems have been disabled by this API call, all other API functions that interact
        with I2C or SPI will return AA_CONFIG_ERROR.

        If configurations are switched, the subsystem specific parameters will be preserved. For example if the SPI
        bitrate is set to 500 kHz and the SPI system is disabled and then enabled, the bitrate will remain at 500 kHz.
        This also holds for other parameters such as the SPI mode, SPI slave response, I2C bitrate, I2C slave response, etc.

        However, if a subsystem is shut off, it will be restarted in a quiescent mode. That is to say, the I2C slave
        function will not be reactivated after re-enabling the I2C subsystem, even if the I2C slave function was active
        before first disabling the I2C subsystem.

    :notes:

        Whenever the configure command is executed and GPIO lines are enabled, the GPIO lines will be momentarily
        switched to high-Z before their direction and pullup configurations are executed.

.. py:method:: aa_target_power(aardvark, power_mask)

    Configure the target power pins.

    :param aardvark: Aardvark handle
    :param power_mask: Power configuration enum
    :return: status

    :error codes:

    :details:

    :notes:

.. py:method::  aa_sleep_ms(milliseconds)

    Sleep for the specified number of milliseconds

    :param milliseconds: Number of milliseconds to sleep
    :return: number of milliseconds slept

    :error codes:

    :details:

    :notes: - Accuracy depends on the operating system scheduler

.. py:method::  aa_async_poll(aardvark, timeout)

    Polling function to check if there are any asynchronous messages pending for processing

    :param aardvark: Aardvark handle
    :param timeout: timeout (milliseconds)
    :return: Async message

    :error codes:

    :details:

    :notes: - If the timeout is < 0, the function will block until data is received.  If the timeout is 0, the function will perform a non-blocking check.


