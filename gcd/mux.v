module mux(mout,i0,i1,sel);

input [7:0]i0,i1;
input sel;

output reg [7:0]mout;

always @(i0 or i1 or sel)
     begin
	   if(sel==0)
	    mout<=i0;
		else
		 mout<=i1;
	  end
	  

endmodule
