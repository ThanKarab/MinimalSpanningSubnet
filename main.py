"""
For the given set of IPv4 addresses find a minimal spanning subnet.
Implementation must be efficient from CPU and memory perspective.
Reasonable test coverage is a plus.
"""


def find_minimal_spanning_subnet(ip_gen):
    first_ip = next(ip_gen)

    # Parse ipv4 str to integer
    first_ip_int = 0
    for ip_part in first_ip.split('.'):
        first_ip_int = first_ip_int << 8
        first_ip_int += int(ip_part)

    ips_bitwise_and = first_ip_int
    ips_bitwise_or = first_ip_int
    for cur_ip in ip_gen:
        # Parse ipv4 str to integer
        cur_ip_int = 0
        for ip_part in cur_ip.split('.'):
            cur_ip_int = cur_ip_int << 8
            cur_ip_int += int(ip_part)

        # Compare ipv4 ints with AND and OR
        ips_bitwise_and = ips_bitwise_and & cur_ip_int
        ips_bitwise_or = ips_bitwise_or | cur_ip_int

    # Get the point where the AND and OR ops differ and keep the left part
    similar_bits = 32
    for i in range(31, -1, -1):
        if (ips_bitwise_and & 1) != (ips_bitwise_or & 1):
            similar_bits = i
        ips_bitwise_and = ips_bitwise_and >> 1
        ips_bitwise_or = ips_bitwise_or >> 1
    subnet_int = (first_ip_int >> 32-similar_bits) << 32-similar_bits

    # Convert the int to ipv4 string
    ip_parts = []
    for _ in range(4):
        ip_part = str(subnet_int & 255)
        ip_parts.insert(0, ip_part)
        subnet_int = subnet_int >> 8
    subnet = '.'.join(ip_parts)
    return subnet


if __name__ == "__main__":
    ips = open('ips.txt', 'r')
    print(find_minimal_spanning_subnet(ips))
