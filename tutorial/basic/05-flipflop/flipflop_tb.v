`timescale 1ns/1ns
`include "flipflop.v"

module flipflop_tb;
    reg CLK = 0;
    reg D = 0;
    wire Q;
    flipflop uut(CLK, D, Q);

    always begin
        CLK = ~CLK; #10;
    end

    initial begin
        $dumpfile("flipflop_tb.vcd");
        $dumpvars(0, flipflop_tb);
        D = 1; #41;
        D = 0; #37;
        D = 1; #41;
        D = 0; #37;
        $finish;
    end

endmodule
