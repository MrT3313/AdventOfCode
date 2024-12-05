// NOTES
// Check File Permissions: ls -l ./2024-Day5-Part1.zig
// Make File Executable: chmod +x ./2024-Day5-Part1.zig
// Compile Zig Source File: zig build-exe 2024-Day5-Part1.zig

const std = @import("std");

pub fn readInputFile(test_input: bool) ![]const u8 {
    const file_path: []const u8 = if (test_input)
        "../test_input.txt"
    else
        "../input.txt";

    // Open the file in the current working directory for reading.
    const file = try std.fs.cwd().openFile(file_path, .{});
    defer file.close();

    // Use a memory allocator to allocate space for the file's contents.
    const allocator = std.heap.page_allocator;

    // Read the entire file contents
    return file.readToEndAlloc(allocator, 1024 * 1024);
}

pub fn part1(data: []const []const u8) ![]const u8 {
    const allocator = std.heap.page_allocator;
    var result = std.ArrayList(u8).init(allocator);
    defer result.deinit();

    for (data) |line| {
        try result.appendSlice(line);
        try result.append(' ');
    }

    return result.toOwnedSlice();
}

pub fn main() !void {
    const args = try std.process.argsAlloc(std.heap.page_allocator);
    defer std.heap.page_allocator.free(args);
    std.debug.print("Arguments: ", .{});
    for (args) |arg| {
        std.debug.print("{s} ", .{arg});
    }
    std.debug.print("\n", .{});

    const test_input = args.len > 1 and std.mem.eql(u8, args[1], "test");
    std.debug.print("Test Input: {}\n", .{test_input});

    const content = try readInputFile(test_input);
    std.debug.print("File Contents: {s}\n", .{content});

    // Split content into lines
    var lines = std.ArrayList([]const u8).init(std.heap.page_allocator);
    defer lines.deinit();

    var line_iterator = std.mem.split(u8, content, "\n");
    while (line_iterator.next()) |line| {
        try lines.append(line);
    }

    const result = try part1(lines.items);
    std.debug.print("Part1 Result: {s}\n", .{result});

    std.debug.print("Result: {s}\n", .{result});
}
