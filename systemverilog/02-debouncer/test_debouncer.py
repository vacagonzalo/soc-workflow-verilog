import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock

PERIOD = 8  # ns


async def reset_dut(srst):
    srst.value = 1
    await Timer(2 * PERIOD, "ns")
    srst.value = 0


@cocotb.test()
async def test_reset(dut):
    """Testing the reset condition"""
    cocotb.start_soon(Clock(dut.clk, period=PERIOD, units="ns").start())
    dut.rst.value = 1
    dut.en.value = 1
    dut.i.value = 1
    await Timer(4 * PERIOD, "ns")
    assert dut.o.value == 0, "The output is not zero."


@cocotb.test()
async def test_disabled(dut):
    """Testing the disabled condition"""
    cocotb.start_soon(Clock(dut.clk, period=PERIOD, units="ns").start())
    dut.rst.value = 0
    dut.en.value = 0
    dut.i.value = 0
    await reset_dut(dut.rst)
    dut.i.value = 1
    await Timer(4 * PERIOD, "ns")
    assert dut.o.value == 0, "The output is not zero."


@cocotb.test()
async def test_noise(dut):
    """Testing the disabled condition"""
    cocotb.start_soon(Clock(dut.clk, period=PERIOD, units="ns").start())
    dut.rst.value = 0
    dut.en.value = 0
    dut.i.value = 0
    await reset_dut(dut.rst)
    dut.en.value = 1
    await Timer(2 * PERIOD, "ns")
    dut.i.value = 1
    await Timer(2, "ns")
    assert dut.o.value == 0, "The output is not zero."

@cocotb.test()
async def test_pressed(dut):
    """Testing the disabled condition"""
    cocotb.start_soon(Clock(dut.clk, period=PERIOD, units="ns").start())
    dut.rst.value = 0
    dut.en.value = 0
    dut.i.value = 0
    await reset_dut(dut.rst)
    dut.en.value = 1
    await Timer(2 * PERIOD, "ns")
    dut.i.value = 1
    await Timer(2 * PERIOD, "ns")
    assert dut.o.value == 1, "The output is not one."
