const std = @import("std");

pub fn main() void {
    std.debug.print("Hello {s}", .{"World"}); // This line is correct
}
