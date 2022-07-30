module Universal_Reg(clk,serial_in,sel,in,out);
	
  input clk;
	input serial_in;
	input [3:0]in;
	input [1:0]sel;
  
  output reg [3:0]out;
	
	
	always@(posedge clk)
	begin
	  case(sel)
	      2'b00: out <= out;
	      2'b01: out <= {out[2:0],serial_in};
			  2'b10: out <= {serial_in,out[3:1]};
			  2'b11: out <= in;
	  endcase
	end
endmodule
