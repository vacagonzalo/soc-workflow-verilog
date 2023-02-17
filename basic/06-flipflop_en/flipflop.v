module flipflop(
    input CLK,
    input SRST,
    input EN,
    input D,
    output reg Q);

    always @(posedge CLK, SRST) begin
        if(SRST)
            Q = 0;
        else if (EN)
            Q = D;
    end

`ifdef COCOTB_SIM
initial begin
  $dumpfile ("flipflop.vcd");
  $dumpvars (0, flipflop);
  #1;
end

`endif
endmodule
