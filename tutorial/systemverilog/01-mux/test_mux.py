import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock

PERIOD = 8  # ns


@cocotb.test()
async def test_logic(dut):
    """Test logic"""
    dut.a.value = 1
    dut.b.value = 0
    dut.s.value = 1
    await Timer(2 * PERIOD, "ns")
    assert dut.o.value == 1, "The output is not one."

    dut.a.value = 1
    dut.b.value = 0
    dut.s.value = 0
    await Timer(2 * PERIOD, "ns")
    assert dut.o.value == 0, "The output is not zero."
