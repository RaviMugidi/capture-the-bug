# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    in0=0
    in1=1
    in2=2
    in3=3
    in4=1
    in5=2
    in6=3
    in7=0
    in8=1
    in9=2
    in10=3
    in11=0
    in12=1
    in13=2
    in14=3
    in15=0
    in16=1
    in17=2
    in18=3
    in19=0
    in20=1
    in21=2
    in22=3
    in23=3
    in24=0
    in25=1
    in26=2
    in27=3
    in28=0
    in29=1
    in30=2
    
    Sel=12

    dut.inp0.value=in0
    dut.inp1.value=in1
    dut.inp2.value=in2
    dut.inp3.value=in3
    dut.inp4.value=in4
    dut.inp5.value=in5
    dut.inp6.value=in6
    dut.inp7.value=in7
    dut.inp8.value=in8
    dut.inp9.value=in9
    dut.inp10.value=in10
    dut.inp11.value=in11
    dut.inp12.value=in12
    dut.inp13.value=in13
    dut.inp14.value=in14
    dut.inp15.value=in15
    dut.inp16.value=in16
    dut.inp17.value=in17
    dut.inp18.value=in18
    dut.inp19.value=in19
    dut.inp20.value=in20
    dut.inp21.value=in21
    dut.inp22.value=in22
    dut.inp23.value=in23
    dut.inp24.value=in24
    dut.inp25.value=in25
    dut.inp26.value=in26
    dut.inp27.value=in27
    dut.inp28.value=in28
    dut.inp29.value=in29
    dut.inp30.value=in30

    dut.sel.value=Sel


    if (Sel==0):
        Out=in0
    elif (Sel==1):
        Out=in1
    elif (Sel==2):
        Out=in2
    elif (Sel==3):
        Out=in3
    elif (Sel==4):
        Out=in4
    elif (Sel==5):
        Out=in5
    elif (Sel==6):
        Out=in6
    elif (Sel==7):
        Out=in7
    elif (Sel==8):
        Out=in8
    elif (Sel==9):
        Out=in9
    elif (Sel==10):
        Out=in11
    elif (Sel==12):
        Out=in12
    elif (Sel==13):
        Out=in13
    elif (Sel==14):
        Out=in14
    elif (Sel==15):
        Out=in15
    elif (Sel==16):
        Out=in16
    elif (Sel==17):
        Out=in17
    elif (Sel==18):
        Out=in18
    elif (Sel==19):
        Out=in19
    elif (Sel==20):
        Out=in20
    elif (Sel==21):
        Out=in21
    elif (Sel==22):
        Out=in22
    elif (Sel==23):
        Out=in23
    elif (Sel==24):
        Out=in24
    elif (Sel==25):
        Out=in25
    elif (Sel==26):
        Out=in26
    elif (Sel==27):
        Out=in27
    elif (Sel==28):
        Out=in28
    elif (Sel==29):
        Out=in29
    elif (Sel==30):
        Out=in30
    
    await Timer(2,units="ns")
    dut._log.info(f'sel={Sel:05} out={Out:05} DUT={int(dut.out.value):05}')
    assert dut.out.value==Out,f"mux result is incorrect"
   
@cocotb.test()
async def mux_randomised_test(dut):
    """Test for multiplexing using random inputs """
    in0=random.randint(0,3)
    in1=random.randint(0,3)
    in2=random.randint(0,3)
    in3=random.randint(0,3)
    in4=random.randint(0,3)
    in5=random.randint(0,3)
    in6=random.randint(0,3)
    in7=random.randint(0,3)
    in8=random.randint(0,3)
    in9=random.randint(0,3)
    in10=random.randint(0,3)
    in11=random.randint(0,3)
    in12=random.randint(0,3)
    in13=random.randint(0,3)
    in14=random.randint(0,3)
    in15=random.randint(0,3)
    in16=random.randint(0,3)
    in17=random.randint(0,3)
    in18=random.randint(0,3)
    in19=random.randint(0,3)
    in20=random.randint(0,3)
    in21=random.randint(0,3)
    in22=random.randint(0,3)
    in23=random.randint(0,3)
    in24=random.randint(0,3)
    in25=random.randint(0,3)
    in26=random.randint(0,3)
    in27=random.randint(0,3)
    in28=random.randint(0,3)
    in29=random.randint(0,3)
    in30=random.randint(0,3)
    
    Sel=random.randint(0,30)

    dut.inp0.value=in0
    dut.inp1.value=in1
    dut.inp2.value=in2
    dut.inp3.value=in3
    dut.inp4.value=in4
    dut.inp5.value=in5
    dut.inp6.value=in6
    dut.inp7.value=in7
    dut.inp8.value=in8
    dut.inp9.value=in9
    dut.inp10.value=in10
    dut.inp11.value=in11
    dut.inp12.value=in12
    dut.inp13.value=in13
    dut.inp14.value=in14
    dut.inp15.value=in15
    dut.inp16.value=in16
    dut.inp17.value=in17
    dut.inp18.value=in18
    dut.inp19.value=in19
    dut.inp20.value=in20
    dut.inp21.value=in21
    dut.inp22.value=in22
    dut.inp23.value=in23
    dut.inp24.value=in24
    dut.inp25.value=in25
    dut.inp26.value=in26
    dut.inp27.value=in27
    dut.inp28.value=in28
    dut.inp29.value=in29
    dut.inp30.value=in30

    dut.sel.value=Sel


    if (Sel==0):
        Out=in0
    elif (Sel==1):
        Out=in1
    elif (Sel==2):
        Out=in2
    elif (Sel==3):
        Out=in3
    elif (Sel==4):
        Out=in4
    elif (Sel==5):
        Out=in5
    elif (Sel==6):
        Out=in6
    elif (Sel==7):
        Out=in7
    elif (Sel==8):
        Out=in8
    elif (Sel==9):
        Out=in9
    elif (Sel==10):
        Out=in11
    elif (Sel==12):
        Out=in12
    elif (Sel==13):
        Out=in13
    elif (Sel==14):
        Out=in14
    elif (Sel==15):
        Out=in15
    elif (Sel==16):
        Out=in16
    elif (Sel==17):
        Out=in17
    elif (Sel==18):
        Out=in18
    elif (Sel==19):
        Out=in19
    elif (Sel==20):
        Out=in20
    elif (Sel==21):
        Out=in21
    elif (Sel==22):
        Out=in22
    elif (Sel==23):
        Out=in23
    elif (Sel==24):
        Out=in24
    elif (Sel==25):
        Out=in25
    elif (Sel==26):
        Out=in26
    elif (Sel==27):
        Out=in27
    elif (Sel==28):
        Out=in28
    elif (Sel==29):
        Out=in29
    elif (Sel==30):
        Out=in30
    
    await Timer(2,units="ns")
    dut._log.info(f'sel={Sel:05} out={Out:05} DUT={int(dut.out.value):05}')
    assert dut.out.value==Out,f"mux result is incorrect"
