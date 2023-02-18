module flipflop(
    input CLK,
    input D,
    output reg Q);

    always @(posedge CLK) begin
        Q = D;
    end

endmodule
