module substractor(s1,a,b);

input [7:0] a,b;
output reg [7:0]s1;

always @(a or b)
     begin
	   s1=a-b;
	  end
endmodule
