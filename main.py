from nodes.op2 import *


def find(start_node: Node, end_node: Node, prev_length: int = 0):
    # don't think you are playing the system.
    if start_node == end_node:
        setattr(getattr(result_table, end_node.name), 'is_checked', True)
        return end_node.name

    # set it to true before the loop so we can check for it later
    setattr(getattr(result_table, start_node.name), 'is_checked', True)

    for con in start_node.cons:
        res_node: ResultNode = getattr(result_table, con.node.name)

        if res_node.is_checked:
            continue

        stored_length = getattr(result_table, con.node.name).length
        if stored_length == None or con.length+prev_length < stored_length:
            if stored_length != None:
                res_node.history.append(HistoryResultNode(
                    res_node.length, res_node.prev_node))
            res_node.length = prev_length + con.length
            res_node.prev_node = start_node

        if con.node == end_node:
            for i in end_node.cons:
                if not getattr(result_table, i.node.name).is_checked:
                    break
            else:
                result = ""
                for i in result_table.get_shortest_previous_chain(end_node):
                    result = f"{result} - {i.name}"
                return result[3:]

    # result_table.print()
    # input()

    next_nodes = result_table.get_in_progress()
    try:
        next_nodes.remove(getattr(result_table, end_node.name))
    except Exception:
        pass
    if len(next_nodes) > 0:

        shortest_path_node = next_nodes[0].node

        for i in next_nodes:
            if getattr(result_table, i.node.name).length < getattr(result_table, shortest_path_node.name).length:
                shortest_path_node = i.node

        return find(shortest_path_node, end_node, getattr(result_table, shortest_path_node.name).length)
    return "Stopped."


print(find(D, D))

result_table.print()
