# Level1_Design2 Verification
The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.
![Screenshot (176)](https://user-images.githubusercontent.com/109639328/181683501-e2d68161-469a-4714-8256-4ad01fe69f15.png)

# Verification Environment
The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes inputs  inp_bit,reset,clk  and gives 1-bit output seq_seen

The values are assigned to the input port using predefined list inputs consists only binary values.

The assert statement is used for comparing the mux's outut to the expected value.

The following error is seen:\
assert dut.seq_seen.value==output,f"Random est failed:dut.seq_seen.value=0,output=1"\
AssertionError: seq_detect_1011 design failed to detect 1011 sequence.

# Test Scenario
Test inputs: inp_list=[1,1,0,1,0,1,1,0,1,1] and reset=0\
Expected output: if (seq_1011_detected)
seq_seen = 1 
\
else 
seq_seen = 0
                 
Observed output in the DUT: DUT.seq_seen=0 even if seq_1011_detected\
\
Output mismatches for the above inputs proving that there is a design bug.

# Design Bug
case(inp_bit or current_state)\
SEQ_1011:  \
      begin\
        next_state = SEQ_10;              #bug \
      end

For the sequece detector design, the seq_seen should be 1'b1 when the seq_1011 detected instead of 1'b0 as in the design code.

# Design Fix

Updating the design and re-running the test makes the test pass.

![Screenshot (190)](https://user-images.githubusercontent.com/109639328/182080936-956f23ce-95f6-4c9b-b000-bf08adf0734e.png)
