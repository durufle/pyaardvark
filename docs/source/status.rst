Status Code
===========

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
.. py:data:: AA_I2C_NOT_AVAILABLE
    :value: -100
.. py:data:: AA_I2C_NOT_ENABLED
    :value: -101
.. py:data:: AA_I2C_READ_ERROR
    :value: -102
.. py:data:: AA_I2C_WRITE_ERROR
    :value: -103
.. py:data:: AA_I2C_SLAVE_BAD_CONFIG
    :value: -104
.. py:data:: AA_I2C_SLAVE_READ_ERROR
    :value: -105
.. py:data:: AA_I2C_SLAVE_TIMEOUT
    :value: -106
.. py:data:: AA_I2C_DROPPED_EXCESS_BYTES
    :value: -107
.. py:data:: AA_I2C_BUS_ALREADY_FREE
    :value: -108

SPI codes (-200 to -299)
------------------------

.. py:data:: AA_SPI_NOT_AVAILABLE
    :value:-200
.. py:data:: AA_SPI_NOT_ENABLED
    :value:-201
.. py:data:: AA_SPI_WRITE_ERROR
    :value: -202
.. py:data:: AA_SPI_SLAVE_READ_ERROR
    :value: -203
.. py:data:: AA_SPI_SLAVE_TIMEOUT
    :value: -204
.. py:data:: AA_SPI_DROPPED_EXCESS_BYTES
    :value: -205


Configurations
--------------

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


Async Message Polling
---------------------

.. py:data:: AA_ASYNC_NO_DATA
    :value: 0x00000000
.. py:data:: AA_ASYNC_I2C_READ
    :value: 0x00000001
.. py:data:: AA_ASYNC_I2C_WRITE
    :value: 0x00000002
.. py:data:: AA_ASYNC_SPI
    :value: 0x00000004
.. py:data:: AA_ASYNC_I2C_MONITOR
    :value: 0x00000008

Aardvark I2C Flags
------------------

.. py:data:: AA_I2C_NO_FLAGS
    :value: 0x00
.. py:data:: AA_I2C_10_BIT_ADDR
    :value: 0x01
.. py:data:: AA_I2C_COMBINED_FMT
    :value: 0x02
.. py:data:: AA_I2C_NO_STOP
    :value: 0x04
.. py:data:: AA_I2C_SIZED_READ
    :value: 0x10
.. py:data:: AA_I2C_SIZED_READ_EXTRA1
    :value: 0x20

Aardvark I2C Status
-------------------

.. py:data:: AA_I2C_STATUS_OK = 0
    :value: 0
.. py:data:: AA_I2C_STATUS_BUS_ERROR
    :value: 1
.. py:data:: AA_I2C_STATUS_SLA_ACK
    :value: 2
.. py:data:: AA_I2C_STATUS_SLA_NACK
    :value: 3
.. py:data:: AA_I2C_STATUS_DATA_NACK
    :value: 4
.. py:data:: AA_I2C_STATUS_ARB_LOST
    :value: 5
.. py:data:: AA_I2C_STATUS_BUS_LOCKED
    :value: 6
.. py:data:: AA_I2C_STATUS_LAST_DATA_ACK
    :value: 7
