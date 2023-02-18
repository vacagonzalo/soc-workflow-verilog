`timescale 1ns/1ns
`include "adder.v"

module adder_tb;

parameter DATA_WIDTH = 32;

reg [DATA_WIDTH-1:0]A;
reg [DATA_WIDTH-1:0]B;
reg CI;
wire [DATA_WIDTH-1:0]O;
wire CO;

adder uut(A, B, CI, O, CO);
defparam uut.DATA_WIDTH = DATA_WIDTH;

integer i;

initial begin
    $dumpfile("adder_tb.vcd");
    $dumpvars(0, adder_tb);

    A = 32'd34;
    B = 32'd19;
    CI = 1;
    #20;

    $display("End of test");
end
endmodule
