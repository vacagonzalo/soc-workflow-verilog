module mux (input wire a, b, s, output reg o);
    always @(a or b or s) begin
        if(s == 1'b1) begin
            o = a;
        end else begin
            o = b;
        end
    end

`ifdef COCOTB_SIM
initial begin
  $dumpfile ("mux.vcd");
  $dumpvars (0, mux);
  #1;
end
`endif

endmodule
