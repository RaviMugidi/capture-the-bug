module register(rnout,clk,rst,load,rin);

input [7:0] rin;
input clk,rst,load;

output reg [7:0] rnout;

always @(posedge clk)
     begin
	  if(rst==1)
	    rnout<=0;
		else if(load==1)
		 rnout<=rin;
	  end
	  
endmodule
