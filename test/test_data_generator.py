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
    cocotb.start_soon(Clock(dut.clock, period=PERIOD, units="ns").start())
    dut.srst.value = 1
    dut.enable.value = 1
    dut.read.value = 0
    await Timer(2 * PERIOD, "ns")
    dut.read.value = 1
    await Timer(2 * PERIOD, "ns")
    dut.read.value = 0
    await Timer(2 * PERIOD, "ns")
    dut.read.value = 1
    await Timer(2 * PERIOD, "ns")
    dut.read.value = 0
    await Timer(2 * PERIOD, "ns")
    assert dut.data.value == 0, "The output is not zero."


@cocotb.test()
async def test_disabled(dut):
    """Testing the disabled condition"""
    cocotb.start_soon(Clock(dut.clock, period=PERIOD, units="ns").start())
    await reset_dut(dut.srst)
    dut.srst.value = 0
    dut.enable.value = 0
    dut.read.value = 0
    await Timer(2 * PERIOD, "ns")
    dut.read.value = 1
    await Timer(2 * PERIOD, "ns")
    dut.read.value = 0
    await Timer(2 * PERIOD, "ns")
    dut.read.value = 1
    await Timer(2 * PERIOD, "ns")
    dut.read.value = 0
    await Timer(2 * PERIOD, "ns")
    assert dut.data.value == 0, "The output is not zero."


@cocotb.test()
async def test_read(dut):
    """Testing the reading condition"""
    cocotb.start_soon(Clock(dut.clock, period=PERIOD, units="ns").start())
    await reset_dut(dut.srst)
    dut.srst.value = 0
    dut.enable.value = 1
    dut.read.value = 0
    await Timer(2 * PERIOD, "ns")
    dut.read.value = 1
    await Timer(2 * PERIOD, "ns")
    dut.read.value = 0
    await Timer(2 * PERIOD, "ns")
    dut.read.value = 1
    await Timer(2 * PERIOD, "ns")
    dut.read.value = 0
    await Timer(2 * PERIOD, "ns")
    assert dut.data.value == 2, "The output is not two."
