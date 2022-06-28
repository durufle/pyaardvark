I2C API
-------

.. py:method::  aa_i2c_free_bus(aardvark)

    Free the I2C bus.

    :param aardvark: Aardvark handle
    :return: status

    :notes:

.. py:method::  aa_i2c_bitrate(aardvark, bitrate_khz)

    Set the I2C bit rate in kilohertz.

    :param aardvark: Aardvark handle
    :return: status

    :notes: - If a zero is passed as the bitrate, the bitrate is unchanged and the current bitrate is returned.

.. py:method::  aa_i2c_bus_timeout(aardvark, timeout_ms)

    Set the bus lock timeout.

    :param aardvark: Aardvark handle
    :param timeout: timeout (milliseconds)
    :return: status

    :notes: - If a zero is passed as the timeout, the timeout is unchanged and the current timeout is returned.


.. py:method::  aa_i2c_read(aardvark, slave_addr, flags, data_in)

    Read a stream of bytes from the I2C slave device

    :param aardvark: Aardvark handle
    :param slave_addr: slave address
    :param flags: I2C Flags
    :param data_in: input data buffer
    :return: status, data in tuple

    :notes: All arrays can be passed into the API as an ArrayType object or as a tuple (array, length), where array
            is an ArrayType object and length is an integer.  The user-specified length would then serve as the length argument to
            the API funtion (please refer to the product datasheet).  If only the array is provided, the array's intrinsic length is
            used as the argument to the underlying API function.

            Additionally, for arrays that are filled by the API function, an integer can be passed in place of the array
            argument and the API will automatically create an array of that length.  All output arrays, whether passed in or
            generated, are passed back in the returned tuple.

.. py:method::  aa_i2c_read_ext(aardvark, slave_addr, flags, data_in)

    Read a stream of bytes from the I2C slave device.

    This API function returns the number of bytes read into the num_read variable.  The return value of the function
    is a status code.
    :param aardvark: Aardvark handle
    :param slave_addr: slave address
    :param flags: I2C Flags
    :param data_in: input data buffer
    :return: status, data in and number of byte in tuple

    :notes: All arrays can be passed into the API as an ArrayType object or as a tuple (array, length), where array
            is an ArrayType object and length is an integer.  The user-specified length would then serve as the length argument to
            the API funtion (please refer to the product datasheet).  If only the array is provided, the array's intrinsic length is
            used as the argument to the underlying API function.

            Additionally, for arrays that are filled by the API function, an integer can be passed in place of the array
            argument and the API will automatically create an array of that length.  All output arrays, whether passed in or
            generated, are passed back in the returned tuple.

.. py:method::  aa_i2c_write(aardvark, slave_addr, flags, data_out)

    Write a stream of bytes to the I2C slave device.

    :param aardvark: Aardvark handle
    :param slave_addr: slave address
    :param flags: I2C Flags
    :param data_in: output data buffer
    :return: status

.. py:method::  aa_i2c_write_ext(aardvark, slave_addr, flags, data_out)

    Write a stream of bytes to the I2C slave device.

    :param aardvark: Aardvark handle
    :param slave_addr: slave address
    :param flags: I2C Flags
    :param data_in: output data buffer
    :return: status

    :notes: This API function returns the number of bytes written into the num_written variable.
            The return value of the function is a status code.

