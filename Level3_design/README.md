# Level1_Design1 Verification
The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.
![Screenshot (185)](https://user-images.githubusercontent.com/109639328/182077963-39b7b1a0-ced6-4cce-a125-aceda614dc08.png)

# Verification Environment
The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in inputs clk, reset, serial_in as s, 4-bit paralel load as inp,2-bit selection mode as sel and generates outpu out.

The values are assigned to the input port using random inputs.

The assert statement is used for comparing the universal shift register's outut to the expected value.

The following error is seen:\
assert int(dut.out.value)==int(out,2),f"Random test failed"\
AssertionError: Random test failed

# Test Scenario
Test inputs: inp=0011 sel=0003 serial_in=1\
Expected output: output=0003\
Observed output in the DUT: DUT.out=0000\
\
Output mismatches for the above inputs proving that there is a design bug.

# Design Bug

case(sel)\
	    2'b11: out <= inp;\
endcase\
For the universal shift register design, the selection should be 4-bit parallel load  for the selection mode sel=3 instead of 4'd0 as in the design code.

# Design Fix

Updating the design and re-running the test makes the test pass.
![Screenshot (186)](https://user-images.githubusercontent.com/109639328/182078063-3835e90c-718a-4969-b6e7-7943f85dbcf3.png)

