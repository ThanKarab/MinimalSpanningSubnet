import pytest
from main import find_minimal_spanning_subnet


@pytest.mark.parametrize(
    "ips,expected",
    [
        (["255.255.255.255", "255.255.255.255"], "255.255.255.255"),
        (["192.168.1.1", "192.168.1.1"], "192.168.1.1"),
        (["192.168.0.1", "192.168.1.1"], "192.168.0.0"),
        (["192.168.0.1", "192.168.1.1", "192.1.1.1"], "192.0.0.0"),
        (["1.168.0.1", "192.168.1.1"], "0.0.0.0"),
        (["1.168.0.1", "192.168.1.1", "192.168.1.1", "192.168.1.1"], "0.0.0.0"),
        (["0.0.0.1", "0.0.0.1", "0.0.0.1", "0.0.0.1"], "0.0.0.1"),
    ]
)
def test_find_minimal_spanning_tree(ips, expected):
    ip_gen = (ip for ip in ips)
    assert find_minimal_spanning_subnet(ip_gen) == expected
