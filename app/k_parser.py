def parse_resp(resp_str):
    def parse_bulk_string(lines, index):
        length = int(lines[index][1:])
        value = lines[index + 1][:length]
        return value, index + 2

    def parse_array(lines, index):
        count = int(lines[index][1:])
        result = []
        index += 1
        for _ in range(count):
            type_indicator = lines[index][0]
            if type_indicator == '$':
                value, index = parse_bulk_string(lines, index)
            elif type_indicator == '*':
                value, index = parse_array(lines, index)
            elif type_indicator == ':':
                value = int(lines[index][1:])
                index += 1
            elif type_indicator == '-':
                value = lines[index][1:]
                index += 1
            else:
                raise ValueError("Unsupported RESP format inside array")
            result.append(value)
        return result, index

    lines = resp_str.strip().split('\r\n')
    type_indicator = lines[0][0]

    if type_indicator == '*':
        return parse_array(lines, 0)[0]
    elif type_indicator == '$':
        return parse_bulk_string(lines, 0)[0]
    elif type_indicator == ':':
        return int(lines[0][1:])
    elif type_indicator == '-':
        return lines[0][1:]
    elif type_indicator == '+':
        return lines[0][1:]
    else:
        raise ValueError("Unsupported RESP format")

# # Example usage
# resp_command = "*4\r\n$3\r\nSET\r\n$3\r\nfoo\r\n$3\r\nbar\r\n$2\r\nPX\r\n$3\r\n100\r\n"
# parsed_command = parse_resp(resp_command)
# print(parsed_command)

# # For an integer response
# resp_integer = ":1234\r\n"
# parsed_integer = parse_resp(resp_integer)
# print(parsed_integer)


# For an integer response
resp_integer = "+PONG\r\n"
parsed_integer = parse_resp(resp_integer)
print(parsed_integer)


# # For an error response
# resp_error = "-ERR something went wrong\r\n"
# parsed_error = parse_resp(resp_error)
# print(parsed_error)
