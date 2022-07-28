# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    #ip_bit=[1,0,1,0,1,1,0,1,1,0,0,1,1,0,1,1]
    #cocotb.log.info('#### CTB: Develop your test here! ######')
    l=[1,1,0,1,0,1,1,0,1,1];
    count=0
    output=0
    for i in l:
       dut.inp_bit.value=i
       if(count==0):
        if(i==1):
            count+=1
            output=0
        else:
            count=0
            output=0
       elif(count==1):
        if(i==0):
            count=2
            output=0
        else:
            count=0
            output=0
       elif(count==2):
        if(i==1):
            count=3
            output=0
        else:
            count=0
            output=0
       elif(count==3):
        if(i==1):
            count=1
            output=1
        else:
            count=0
            output=0
       else:
        count=0
        output=0
       await Timer(5,units="us")
       await FallingEdge(dut.clk)

       dut._log.info(f'in={i:01} output={output:01} seq_seen={int(dut.seq_seen.value):01}')
       assert dut.seq_seen.value==output,f"Random test failed with:"#{in} {seq_seen}"format(in=dut.input_bit.value,seq_seen=dut.seq_seen.value)
