import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_GCD(dut):
    """Test for verify GCD """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    
    # go
      dut.go.value = 0
      await FallingEdge(dut.clk)
      dut.go.value = 1
      await FallingEdge(dut.clk)

    #ip_bit=[1,0,1,0,1,1,0,1,1,0,0,1,1,0,1,1]
    #cocotb.log.info('#### CTB: Develop your test here! ######')

    a=random.randint(1,127)
    b=random.randint(1,127)
    dut.in1.value = a
    dut.in2.value = b
    
    while(a!=b):
        if(a>b):
          a=a-b
          done=0
        elif(b>a):
          b=b-a
          done=0
    if(a==b):
       gcd=a
       done=1
       dut._log.info(f'in1={a:02} in2={b:04} gcd={gcd:04} GCD={int(dut.out.value):04}')
       assert dut.done.value==done,f"Random test failed "
