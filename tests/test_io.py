from conftest import MockSMBus


def test_inputs(gpio, smbus2):
    import cap1xxx

    smbus2.SMBus.return_value = MockSMBus(1, default_registers={
        cap1xxx.R_PRODUCT_ID: cap1xxx.PID_CAP1208,
        cap1xxx.R_INPUT_STATUS: 0b10101010
    })

    cap1208 = cap1xxx.Cap1208()
    assert cap1208.get_input_status() == [ "none", "press", "none", "press", "none", "press", "none", "press"]


def test_outputs(gpio, smbus2):
    import cap1xxx

    mock = MockSMBus(1, default_registers={
        cap1xxx.R_PRODUCT_ID: cap1xxx.PID_CAP1188,
        cap1xxx.R_INPUT_STATUS: 0b10101010
    })

    smbus2.SMBus.return_value = mock

    cap1188 = cap1xxx.Cap1188()
    cap1188.set_led_state(0, True)

    assert mock.read_byte_data(cap1xxx.DEFAULT_ADDR, cap1xxx.R_LED_OUTPUT_CON) == 0b00000001


def test_sensitivity(gpio, smbus2):
    import cap1xxx

    mock = MockSMBus(1, default_registers={
        cap1xxx.R_PRODUCT_ID: cap1xxx.PID_CAP1188
    })

    smbus2.SMBus.return_value = mock

    cap1188 = cap1xxx.Cap1188()

    assert cap1188.get_sensitivity() == 2

    for sensitivity in cap1xxx.SENSITIVITY.keys():
        cap1188.set_sensitivity(sensitivity)
        assert cap1188.get_sensitivity() == sensitivity
