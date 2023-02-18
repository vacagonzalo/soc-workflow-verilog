import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock

PERIOD = 8  # ns


async def reset_dut(srst):
    srst.value = 1
    await Timer(2 * PERIOD, "ns")
    srst.value = 0
    await Timer(2 * PERIOD, "ns")


@cocotb.test()
async def test_reset(dut):
    """Testing the reset condition"""
    cocotb.start_soon(Clock(dut.CLK, period=PERIOD, units="ns").start())
    dut.SRST.value = 1
    dut.EN.value = 1
    dut.D.value = 1
    await Timer(2 * PERIOD, "ns")
    assert dut.Q.value == 0, "The output is not zero."


@cocotb.test()
async def test_disabled(dut):
    """Testing the disabled condition"""
    cocotb.start_soon(Clock(dut.CLK, period=PERIOD, units="ns").start())
    dut.D.value = 0
    await reset_dut(dut.SRST)
    dut.EN.value = 0
    await Timer(2 * PERIOD, "ns")
    dut.D.value = 1
    await Timer(2 * PERIOD, "ns")
    assert dut.Q.value == 0, "The output is not zero."
