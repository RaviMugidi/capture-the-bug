# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_universal_shift_reg(dut):
    """Test for universal shift register """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    s=random.randint(0,1)
    dut.serial_in.value=s
    s=bin(s)[2:]
    inp=random.randint(0,15)
    dut.inp.value=inp
    inp=bin(inp)[2:]
    inp=inp.zfill(4)
    sel=random.randint(0,3)
    dut.sel.value=sel
    out=bin(0)[2:]
    out=out.zfill(4)

    if(sel==0):
       out=out
    elif(sel==1):
       out=out[:3]+s
    elif(sel==2):
       out=s+out[1:]
    else:
       out=inp
    await Timer(5,units="us")
    await FallingEdge(dut.clk)   
    
    dut._log.info(f'inp={int(inp):04} sel={sel:04} serial_in={int(s,2):01} output={int(out,2):04} out={int(dut.out.value):04}')
    assert int(dut.out.value)==int(out,2),f"Random test failed" 
        
        
