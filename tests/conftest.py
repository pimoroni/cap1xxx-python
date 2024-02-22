import sys

import mock
import pytest


# MockSMbus borrowed from https://github.com/pimoroni/i2cdevice-python
class MockSMBus:
    def __init__(self, i2c_bus, default_registers=None):
        self.regs = [0 for _ in range(255)]
        if default_registers is not None:
            for index in default_registers.keys():
                self.regs[index] = default_registers.get(index)

    def write_i2c_block_data(self, i2c_address, register, values):
        self.regs[register:register + len(values)] = values

    def read_i2c_block_data(self, i2c_address, register, length):
        return self.regs[register:register + length]

    def read_byte_data(self, i2c_address, register):
        return self.read_i2c_block_data(i2c_address, register, 1)[0]

    def write_byte_data(self, i2c_address, register, value):
        self.write_i2c_block_data(i2c_address, register, [value])


@pytest.fixture(scope="function", autouse=True)
def cleanup():
    yield
    del sys.modules["cap1xxx"]


@pytest.fixture(scope="function")
def smbus2():
    sys.modules["smbus2"] = mock.MagicMock()
    yield sys.modules["smbus2"]
    del sys.modules["smbus2"]


@pytest.fixture(scope="function")
def gpio():
    sys.modules["RPi"] = mock.Mock()
    sys.modules["RPi.GPIO"] = mock.MagicMock()
    yield
    del sys.modules["RPi"]
    del sys.modules["RPi.GPIO"]