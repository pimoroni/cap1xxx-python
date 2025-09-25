import pytest


def test_setup(gpio, smbus2):
    import cap1xxx

    smbus2.SMBus(1).read_byte_data.return_value = cap1xxx.PID_CAP1208
    cap1208 = cap1xxx.Cap1208()
    assert cap1208.number_of_leds == 8

    smbus2.SMBus(1).read_byte_data.return_value = cap1xxx.PID_CAP1188
    cap1188 = cap1xxx.Cap1188()
    assert cap1188.number_of_leds == 8

    smbus2.SMBus(1).read_byte_data.return_value = cap1xxx.PID_CAP1166
    cap1166 = cap1xxx.Cap1166()
    assert cap1166.number_of_leds == 6


def test_setup_invalid_pid(gpio, smbus2):
    import cap1xxx

    smbus2.SMBus(1).read_byte_data.return_value = 0x00

    with pytest.raises(RuntimeError):
        _ = cap1xxx.Cap1208()