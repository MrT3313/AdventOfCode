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

    const file = try std.fs.cwd().openFile(file_path, .{});
    defer file.close();

    const allocator = std.heap.page_allocator;
    return file.readToEndAlloc(allocator, 1024 * 1024);
}

pub const Node = struct {
    id: u32,
    children: std.ArrayList(*Node),
    allocator: std.mem.Allocator,

    // Constructor method for creating a new Node
    pub fn init(allocator: std.mem.Allocator, id: u32) Node {
        return Node{
            .id = id,
            .children = std.ArrayList(*Node).init(allocator),
            .allocator = allocator,
        };
    }

    // Method to add a child node
    pub fn addChild(self: *Node, child_node: *Node) !void {
        try self.children.append(child_node);
    }

    // Cleanup method to free memory
    pub fn deinit(self: *Node) void {
        self.children.deinit();
    }
};

pub const Graph = struct {
    nodes: std.ArrayList(*Node),
    node_map: std.AutoHashMap(u32, *Node),
    allocator: std.mem.Allocator,

    pub fn init(allocator: std.mem.Allocator) Graph {
        return Graph{
            .nodes = std.ArrayList(*Node).init(allocator),
            .node_map = std.AutoHashMap(u32, *Node).init(allocator),
            .allocator = allocator,
        };
    }

    pub fn getNodeById(self: *Graph, id: u32) ?*Node {
        return self.node_map.get(id);
    }

    pub fn addNode(self: *Graph, node: *Node) !void {
        try self.nodes.append(node);
        try self.node_map.put(node.id, node);
    }

    // Cleanup method to free memory
    pub fn deinit(self: *Graph) void {
        for (self.nodes.items) |node| {
            node.deinit();
            self.allocator.destroy(node);
        }
        self.nodes.deinit();
        self.node_map.deinit();
    }
};

pub fn organize_ordering_rules(allocator: std.mem.Allocator, page_ordering_rules: []const []const u8) !Graph {

    // Initialize Graph
    var graph = Graph.init(allocator);

    // Initialize node map to store actual nodes, not pointers
    var node_map = std.StringHashMap(*Node).init(allocator);
    defer node_map.deinit();

    for (page_ordering_rules) |rule| {
        std.debug.print("🔄🔄🔄🔄\n", .{});

        var parts = std.mem.split(u8, rule, "|");
        const parent_name = std.mem.trim(u8, parts.next() orelse continue, " ");
        const child_name = std.mem.trim(u8, parts.next() orelse continue, " ");

        std.debug.print("parent_name: {s}\n", .{parent_name});
        std.debug.print("child_name: {s}\n", .{child_name});

        // Create parent node if it doesn't exist
        if (!node_map.contains(parent_name)) {
            const new_parent_node = try allocator.create(Node);

            const new_node_id = try std.fmt.parseInt(u32, parent_name, 10);
            new_parent_node.* = Node.init(allocator, new_node_id);

            try node_map.put(parent_name, new_parent_node);
            try graph.addNode(new_parent_node);
        }

        // Create child node if it doesn't exist
        if (!node_map.contains(child_name)) {
            const new_child_node = try allocator.create(Node);

            const new_node_id = try std.fmt.parseInt(u32, child_name, 10);
            new_child_node.* = Node.init(allocator, new_node_id);

            try node_map.put(child_name, new_child_node);
            try graph.addNode(new_child_node);
        }

        // Add child to parent's children
        if (node_map.get(parent_name)) |parent| {
            if (node_map.get(child_name)) |child| {
                try parent.addChild(child);
            }
        }

        // Print parent node info
        if (node_map.get(parent_name)) |parent_node| {
            std.debug.print("[PARENT] Name: {s} (ID: {d}, Children: {d})\n", .{
                parent_name,
                parent_node.id,
                parent_node.children.items.len,
            });
        }

        // Print child node info
        if (node_map.get(child_name)) |child_node| {
            std.debug.print("[CHILD] Name: {s} (ID: {d}, Children: {d})\n", .{
                child_name,
                child_node.id,
                child_node.children.items.len,
            });
        }
    }

    // Debug print
    std.debug.print("Graph created with {d} nodes\n", .{graph.nodes.items.len});

    return graph;
}

pub fn validate_updates(graph: *Graph, updates: []const []const u8) !u32 {
    var result = std.ArrayList([]const u8).init(graph.allocator);
    errdefer result.deinit();

    var sum: u32 = 0;

    // Loop through each update (page set to process)
    for (updates) |update| {
        std.debug.print("====================\n", .{});
        std.debug.print("CURRENT UPDATE:\n{s}\n", .{update});

        var number_iterator = std.mem.split(u8, update, ",");

        // Get the first number to start the validation
        const first_num_str = number_iterator.next() orelse continue;
        const first_page_id = try std.fmt.parseInt(u32, first_num_str, 10);
        var current_node = graph.getNodeById(first_page_id);

        var is_valid_sequence = true;

        // Validate the sequence
        while (number_iterator.next()) |next_num_str| {
            const next_page_id = try std.fmt.parseInt(u32, next_num_str, 10);

            // Check if current_node exists and contains next_page_id as a child
            if (current_node) |node| {
                var found_child = false;
                for (node.children.items) |child| {
                    if (child.id == next_page_id) {
                        found_child = true;
                        current_node = graph.getNodeById(next_page_id);
                        break;
                    }
                }

                if (!found_child) {
                    is_valid_sequence = false;
                    std.debug.print("Invalid sequence: {d} is not a child of {d}\n", .{
                        next_page_id,
                        node.id,
                    });
                    break;
                }
            } else {
                is_valid_sequence = false;
                std.debug.print("Invalid sequence: Node not found\n", .{});
                break;
            }
        }

        if (is_valid_sequence) {
            // Get middle number from the valid sequence
            var numbers = std.ArrayList(u32).init(graph.allocator);
            defer numbers.deinit();

            var number_iter = std.mem.split(u8, update, ",");
            while (number_iter.next()) |num_str| {
                const num = try std.fmt.parseInt(u32, num_str, 10);
                try numbers.append(num);
            }

            // Calculate middle index
            const middle_idx = numbers.items.len / 2;
            sum += numbers.items[middle_idx];

            try result.append(update);
        }
    }

    return sum;
}

pub fn part1(allocator: std.mem.Allocator, page_ordering_rules: []const []const u8, pages_to_produce: []const []const u8) ![]const u8 {
    std.debug.print("PART 1\n\tRules:\n\t{s}\n\tPages:\n\t{s}\n", .{ page_ordering_rules, pages_to_produce });

    // ORGANIZE: page_ordering_rules
    var rules_graph = try organize_ordering_rules(allocator, page_ordering_rules);
    defer rules_graph.deinit();

    // Debug print the graph structure
    std.debug.print("Graph Analysis:\n", .{});

    for (rules_graph.nodes.items) |node| {
        std.debug.print("Node ID: {d}, Children count: {d}\n", .{ node.id, node.children.items.len });
        for (node.children.items) |child| {
            std.debug.print("\tChild ID: {d}\n", .{child.id});
        }
    }

    if (rules_graph.getNodeById(97)) |node| {
        std.debug.print("Found node 97! Children count: {d}\n", .{node.children.items.len});
    } else {
        std.debug.print("Node 97 not found\n", .{});
    }

    // PROCESS: pages_to_produce
    std.debug.print("WHAT ARE THE PAGES TO PRODUCE\n{s}", .{pages_to_produce});
    const sum = try validate_updates(&rules_graph, pages_to_produce);

    return try std.fmt.allocPrint(allocator, "{d}", .{sum});
}

pub fn main() !void {
    const allocator = std.heap.page_allocator;

    // Parse arguments
    const args = try std.process.argsAlloc(allocator);
    defer allocator.free(args);

    const test_input = args.len > 1 and std.mem.eql(u8, args[1], "test");

    // Read input file
    const content = try readInputFile(test_input);
    std.debug.print("CONTENT: {s}\n", .{content});

    // Split content into two parts
    var sections = std.mem.split(u8, content, "\n\n");
    const first_section = sections.next() orelse return error.InvalidInput;
    const second_section = sections.next() orelse return error.InvalidInput;

    // ALLOCATE: memory?
    // ALLOCATE: memory? > SECTION 1 : page ordering rules
    var page_ordering_rules = std.ArrayList([]const u8).init(allocator);
    defer page_ordering_rules.deinit(); // The defer means that .deinit() will be automatically called when the current scope ends, regardless of how the scope is exited

    // ALLOCATE: memory? > SECTION 2 : pages to produce
    var pages_to_produce = std.ArrayList([]const u8).init(allocator);
    defer pages_to_produce.deinit(); // The defer means that .deinit() will be automatically called when the current scope ends, regardless of how the scope is exited

    // ITERATORS
    // ITERATORS > rules
    var rule_iterator = std.mem.split(u8, first_section, "\n");
    // ITERATORS > pages
    var page_iterator = std.mem.split(u8, second_section, "\n");

    // PROCESS
    // PROCESS > rules
    while (rule_iterator.next()) |rule| {
        if (rule.len > 0) {
            try page_ordering_rules.append(rule);
        }
    }

    // PROCESS > pages
    while (page_iterator.next()) |page| {
        if (page.len > 0) {
            try pages_to_produce.append(page);
        }
    }

    const result_string = try part1(allocator, page_ordering_rules.items, pages_to_produce.items);
    defer allocator.free(result_string);

    std.debug.print("Part1 Result: {s}\n", .{result_string});
}
