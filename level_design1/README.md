# Level1_Design1 Verification
The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.
![Screenshot (169)](https://user-images.githubusercontent.com/109639328/181598210-7c2f25d2-bfab-4882-91bb-725c76d53ecd.png)

# Verification Environment
The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in 2-bit inputs from inp0 to inp30, 5-bit input as sel and gives 2-bit output out

The values are assigned to the input port using random inputs.

The assert statement is used for comparing the mux's outut to the expected value.

The following error is seen:
```
assert dut.out.value==Out,f"mux result is incorrect"
AssertionError: mux result is incorrect.
```

# Test Scenario(Important)
Test inputs: inp13=0 and sel=13\
Expected output: out=1\
Observed output in the DUT: DUT.out=0\
\
Output mismatches for the above inputs proving that there is a design bug.

# Design Bug
```
case(sel)
   begin 
     //remaining code//
     5'b01101: out=inp12  #bug
     //remaining  code//
   end 
 ```
For the mux design, the selection should be 5'b01100 to select inp12 instead of 5'b01101 as in the design code.

# Design Fix

Updating the design and re-running the test makes the test pass.

![Screenshot (188)](https://user-images.githubusercontent.com/109639328/182080315-6e446c42-3771-4004-9883-54a18db410b4.png)
