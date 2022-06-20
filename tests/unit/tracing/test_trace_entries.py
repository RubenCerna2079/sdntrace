"""
    Test tracing.trace_entries
"""
from unittest import TestCase

from napps.amlight.sdntrace.tracing.trace_entries import TraceEntries


class TestDpid(TestCase):
    """Test all combinations for DPID"""

    def setUp(self):
        self.trace_entries = TraceEntries()

    def test_incorrect_dpid_int(self):
        """DPID cannot be integer"""
        with self.assertRaises(ValueError):
            self.trace_entries.dpid = 0

    def test_incorrect_dpid_empty_str(self):
        """DPID cannot be an empty str"""
        with self.assertRaises(ValueError):
            self.trace_entries.dpid = ""

    def test_incorrect_dpid_invalid_characters_plus(self):
        """DPID cannot be a special character (only ':' is allowed)"""
        with self.assertRaises(ValueError):
            self.trace_entries.dpid = "+"

    def test_incorrect_dpid_invalid_characters_comma(self):
        """DPID cannot be a special character (only ':' is allowed)"""
        with self.assertRaises(ValueError):
            self.trace_entries.dpid = ","

    def test_incorrect_dpid_invalid_length(self):
        """DPID cannot be longer than 16 without ':'"""
        with self.assertRaises(ValueError):
            self.trace_entries.dpid = "00000000000000001"

    def test_correct_dpid_char(self):
        """Correct DPID with char"""
        self.trace_entries.dpid = "1"

    def test_read_dpid_char(self):
        """Read DPID '1'"""
        self.test_correct_dpid_char()
        self.assertEqual(self.trace_entries.dpid, "1")

    def test_correct_dpid_complete(self):
        """Correct DPID with colons, numbers, and letters"""
        self.trace_entries.dpid = "ab:cd:ef:ab:cd:ef:00:01"

    def test_read_dpid_complete(self):
        """Read DPID '1'"""
        self.test_correct_dpid_complete()
        self.assertEqual(self.trace_entries.dpid, "ab:cd:ef:ab:cd:ef:00:01")


class TestInPort(TestCase):
    """Test all combinations for IN_PORT"""

    def setUp(self):
        self.trace_entries = TraceEntries()

    def test_incorrect_in_port_char(self):
        """IN_PORT cannot be a char"""
        with self.assertRaises(ValueError):
            self.trace_entries.in_port = "1"

    def test_incorrect_in_port_negative(self):
        """IN_PORT cannot be negative"""
        with self.assertRaises(ValueError):
            self.trace_entries.in_port = -1

    def test_correct_in_port(self):
        """IN_PORT Correct"""
        self.trace_entries.in_port = 1

    def test_read_in_port(self):
        """Read DPID '1'"""
        self.test_correct_in_port()
        self.assertEqual(self.trace_entries.in_port, 1)


class TestDlSrc(TestCase):
    """Test all combinations for DL_SRC"""

    def setUp(self):
        self.trace_entries = TraceEntries()

    def test_incorrect_dl_src_int(self):
        """dl_src cannot be integer"""
        with self.assertRaises(ValueError):
            self.trace_entries.dl_src = 0

    def test_incorrect_dl_src_empty_str(self):
        """dl_src cannot be an empty str"""
        with self.assertRaises(ValueError):
            self.trace_entries.dl_src = ""

    def test_incorrect_dl_src_invalid_characters_plus(self):
        """dl_src only accepts ':' snd '-'"""
        with self.assertRaises(ValueError):
            self.trace_entries.dl_src = "+"

    def test_incorrect_dl_src_invalid_characters_comma(self):
        """dl_src cannot be a special character (only ':' is allowed)"""
        with self.assertRaises(ValueError):
            self.trace_entries.dl_src = ","

    def test_incorrect_dl_src_invalid_length(self):
        """dl_src cannot be longer than 16 without ':'"""
        with self.assertRaises(ValueError):
            self.trace_entries.dl_src = "000000000000000001"

    def test_correct_dl_src_char(self):
        """Correct dl_src with char"""
        self.trace_entries.dl_src = "ab:cd:ef:ab:cd:00"

    def test_read_dl_src_char(self):
        """Read dl_src '1'"""
        self.test_correct_dl_src_char()
        self.assertEqual(self.trace_entries.dl_src, "ab:cd:ef:ab:cd:00")


class TestDlDst(TestCase):
    """Test all combinations for DL_DST"""

    def setUp(self):
        self.trace_entries = TraceEntries()

    def test_incorrect_dl_dst_int(self):
        """dl_dst cannot be integer"""
        with self.assertRaises(ValueError):
            self.trace_entries.dl_dst = 0

    def test_incorrect_dl_dst_empty_str(self):
        """dl_dst cannot be an empty str"""
        with self.assertRaises(ValueError):
            self.trace_entries.dl_dst = ""

    def test_incorrect_dl_dst_invalid_characters_plus(self):
        """dl_dst only accepts ':' snd '-'"""
        with self.assertRaises(ValueError):
            self.trace_entries.dl_dst = "+"

    def test_incorrect_dl_dst_invalid_characters_comma(self):
        """dl_dst cannot be a special character (only ':' is allowed)"""
        with self.assertRaises(ValueError):
            self.trace_entries.dl_dst = ","

    def test_incorrect_dl_dst_invalid_length(self):
        """dl_dst cannot be longer than 16 without ':'"""
        with self.assertRaises(ValueError):
            self.trace_entries.dl_dst = "000000000000000001"

    def test_correct_dl_dst_char(self):
        """Correct dl_dst with char"""
        self.trace_entries.dl_dst = "ab:cd:ef:ab:cd:00"

    def test_read_dl_dst_char(self):
        """Read dl_dst '1'"""
        self.test_correct_dl_dst_char()
        self.assertEqual(self.trace_entries.dl_dst, "ab:cd:ef:ab:cd:00")


class TestDlVlan(TestCase):
    """Test all combinations for DL_VLAN"""

    def setUp(self):
        self.trace_entries = TraceEntries()

    def test_incorrect_dl_vlan_char(self):
        """dl_vlan cannot be a char"""
        with self.assertRaises(ValueError):
            self.trace_entries.dl_vlan = "1"

    def test_incorrect_dl_vlan_negative(self):
        """dl_vlan cannot be negative"""
        with self.assertRaises(ValueError):
            self.trace_entries.dl_vlan = -1

    def test_incorrect_dl_vlan_too_big(self):
        """dl_vlan cannot be bigger than 4095"""
        with self.assertRaises(ValueError):
            self.trace_entries.dl_vlan = 4096

    def test_correct_dl_vlan(self):
        """dl_vlan Correct"""
        self.trace_entries.dl_vlan = 1

    def test_read_dl_vlan(self):
        """Read DPID '1'"""
        self.test_correct_dl_vlan()
        self.assertEqual(self.trace_entries.dl_vlan, 1)


class TestDlType(TestCase):
    """Test all combinations for dl_type"""

    def setUp(self):
        self.trace_entries = TraceEntries()

    def test_incorrect_dl_type_char(self):
        """dl_type cannot be a char"""
        with self.assertRaises(ValueError):
            self.trace_entries.dl_type = "1"

    def test_incorrect_dl_type_negative(self):
        """dl_type cannot be negative"""
        with self.assertRaises(ValueError):
            self.trace_entries.dl_type = -1

    def test_incorrect_dl_type_too_big(self):
        """dl_type cannot be bigger than 4095"""
        with self.assertRaises(ValueError):
            self.trace_entries.dl_type = 65536

    def test_correct_dl_type(self):
        """dl_type Correct"""
        self.trace_entries.dl_type = 1

    def test_read_dl_type(self):
        """Read DPID '1'"""
        self.test_correct_dl_type()
        self.assertEqual(self.trace_entries.dl_type, 1)


class TestDlVlanPcp(TestCase):
    """Test all combinations for dl_vlan_pcp"""

    def setUp(self):
        self.trace_entries = TraceEntries()

    def test_incorrect_dl_vlan_pcp_char(self):
        """dl_vlan_pcp cannot be a char"""
        with self.assertRaises(ValueError):
            self.trace_entries.dl_vlan_pcp = "1"

    def test_incorrect_dl_vlan_pcp_negative(self):
        """dl_vlan_pcp cannot be negative"""
        with self.assertRaises(ValueError):
            self.trace_entries.dl_vlan_pcp = -1

    def test_incorrect_dl_vlan_pcp_too_big(self):
        """dl_vlan_pcp cannot be bigger than 7"""
        with self.assertRaises(ValueError):
            self.trace_entries.dl_vlan_pcp = 8

    def test_correct_dl_vlan_pcp(self):
        """dl_vlan_pcp Correct"""
        self.trace_entries.dl_vlan_pcp = 1

    def test_read_dl_vlan_pcp(self):
        """Read DPID '1'"""
        self.test_correct_dl_vlan_pcp()
        self.assertEqual(self.trace_entries.dl_vlan_pcp, 1)


class TestNwTos(TestCase):
    """Test all combinations for nw_tos"""

    def setUp(self):
        self.trace_entries = TraceEntries()

    def test_incorrect_nw_tos_char(self):
        """nw_tos cannot be a char"""
        with self.assertRaises(ValueError):
            self.trace_entries.nw_tos = "1"

    def test_incorrect_nw_tos_negative(self):
        """nw_tos cannot be negative"""
        with self.assertRaises(ValueError):
            self.trace_entries.nw_tos = -1

    def test_incorrect_nw_tos_too_big(self):
        """nw_tos cannot be bigger than 7"""
        with self.assertRaises(ValueError):
            self.trace_entries.nw_tos = 8

    def test_correct_nw_tos(self):
        """nw_tos Correct"""
        self.trace_entries.nw_tos = 1

    def test_read_nw_tos(self):
        """Read DPID '1'"""
        self.test_correct_nw_tos()
        self.assertEqual(self.trace_entries.nw_tos, 1)


class TestNwSrc(TestCase):
    """Test all combinations for NW_SRC"""

    def setUp(self):
        self.trace_entries = TraceEntries()

    def test_incorrect_nw_src_int(self):
        """nw_src cannot be integer"""
        with self.assertRaises(ValueError):
            self.trace_entries.nw_src = 0

    def test_incorrect_nw_src_empty_str(self):
        """nw_src cannot be an empty str"""
        with self.assertRaises(ValueError):
            self.trace_entries.nw_src = ""

    def test_incorrect_nw_src_invalid_characters_plus(self):
        """nw_src only accepts '.'"""
        with self.assertRaises(ValueError):
            self.trace_entries.nw_src = "+"

    def test_incorrect_nw_src_256(self):
        """Correct nw_src with char"""
        with self.assertRaises(ValueError):
            self.trace_entries.nw_src = "0.0.0.256"

    def test_correct_nw_src_zeroed(self):
        """Correct nw_src with char"""
        self.trace_entries.nw_src = "0.0.0.0"

    def test_read_nw_src_char(self):
        """Read nw_src '1'"""
        self.test_correct_nw_src_zeroed()
        self.assertEqual(self.trace_entries.nw_src, "0.0.0.0")

    def test_correct_nw_src_255(self):
        """Correct nw_src with char"""
        self.trace_entries.nw_src = "255.255.255.255"

    def test_read_nw_src_char_255(self):
        """Read nw_src '1'"""
        self.test_correct_nw_src_255()
        self.assertEqual(self.trace_entries.nw_src, "255.255.255.255")


class TestNwDst(TestCase):
    """Test all combinations for NW_DST"""

    def setUp(self):
        self.trace_entries = TraceEntries()

    def test_incorrect_nw_dst_int(self):
        """nw_dst cannot be integer"""
        with self.assertRaises(ValueError):
            self.trace_entries.nw_dst = 0

    def test_incorrect_nw_dst_empty_str(self):
        """nw_dst cannot be an empty str"""
        with self.assertRaises(ValueError):
            self.trace_entries.nw_dst = ""

    def test_incorrect_nw_dst_invalid_characters_plus(self):
        """nw_dst only accepts '.'"""
        with self.assertRaises(ValueError):
            self.trace_entries.nw_dst = "+"

    def test_incorrect_nw_dst_256(self):
        """Correct nw_dst with char"""
        with self.assertRaises(ValueError):
            self.trace_entries.nw_dst = "0.0.0.256"

    def test_correct_nw_dst_zeroed(self):
        """Correct nw_dst with char"""
        self.trace_entries.nw_dst = "0.0.0.0"

    def test_read_nw_dst_char(self):
        """Read nw_dst '1'"""
        self.test_correct_nw_dst_zeroed()
        self.assertEqual(self.trace_entries.nw_dst, "0.0.0.0")

    def test_correct_nw_dst_255(self):
        """Correct nw_dst with char"""
        self.trace_entries.nw_dst = "255.255.255.255"

    def test_read_nw_dst_char_255(self):
        """Read nw_dst '1'"""
        self.test_correct_nw_dst_255()
        self.assertEqual(self.trace_entries.nw_dst, "255.255.255.255")


class TestTpSrc(TestCase):
    """Test all combinations for tp_src"""

    def setUp(self):
        self.trace_entries = TraceEntries()

    def test_incorrect_tp_src_char(self):
        """tp_src cannot be a char"""
        with self.assertRaises(ValueError):
            self.trace_entries.tp_src = "1"

    def test_incorrect_tp_src_negative(self):
        """tp_src cannot be negative"""
        with self.assertRaises(ValueError):
            self.trace_entries.tp_src = -1

    def test_incorrect_tp_src_too_big(self):
        """tp_src cannot be bigger than 4095"""
        with self.assertRaises(ValueError):
            self.trace_entries.tp_src = 65536

    def test_correct_tp_src(self):
        """tp_src Correct"""
        self.trace_entries.tp_src = 1

    def test_read_tp_src(self):
        """Read DPID '1'"""
        self.test_correct_tp_src()
        self.assertEqual(self.trace_entries.tp_src, 1)


class TestTpDst(TestCase):
    """Test all combinations for tp_dst"""

    def setUp(self):
        self.trace_entries = TraceEntries()

    def test_incorrect_tp_dst_char(self):
        """tp_dst cannot be a char"""
        with self.assertRaises(ValueError):
            self.trace_entries.tp_dst = "1"

    def test_incorrect_tp_dst_negative(self):
        """tp_dst cannot be negative"""
        with self.assertRaises(ValueError):
            self.trace_entries.tp_dst = -1

    def test_incorrect_tp_dst_too_big(self):
        """tp_dst cannot be bigger than 4095"""
        with self.assertRaises(ValueError):
            self.trace_entries.tp_dst = 65536

    def test_correct_tp_dst(self):
        """tp_dst Correct"""
        self.trace_entries.tp_dst = 1

    def test_read_tp_dst(self):
        """Read DPID '1'"""
        self.test_correct_tp_dst()
        self.assertEqual(self.trace_entries.tp_dst, 1)


class TestLoadEntries(TestCase):
    """Now, load all entries at once"""

    def setUp(self):
        self.trace_entries = TraceEntries()

    def test_missing_trace(self):
        """key trace is mandatory"""
        with self.assertRaises(ValueError):
            entries = {}
            self.trace_entries.load_entries(entries)

    def test_trace_non_dict(self):
        """key trace has to be a dict"""
        with self.assertRaises(ValueError):
            entries = {"trace:": 0}
            self.trace_entries.load_entries(entries)

    def test_missing_switch(self):
        """key trace/switch is mandatory"""
        with self.assertRaises(ValueError):
            entries = {"trace": {}}
            self.trace_entries.load_entries(entries)

    def test_missing_dpid(self):
        """key trace/switch is mandatory"""
        with self.assertRaises(ValueError):
            dpid = {}
            switch = {"switch": dpid}
            entries = {"trace": switch}
            self.trace_entries.load_entries(entries)

    def test_missing_in_port(self):
        """key trace/switch is mandatory"""
        with self.assertRaises(ValueError):
            dpid = {"dpid": "a"}
            switch = {"switch": dpid}
            entries = {"trace": switch}
            self.trace_entries.load_entries(entries)

    def test_missing_eth(self):
        """key trace/switch is mandatory"""
        with self.assertRaises(ValueError):
            eth = 0
            dpid = {"dpid": "a", "in_port": 1}
            switch = {"switch": dpid, "eth": eth}
            entries = {"trace": switch}
            self.trace_entries.load_entries(entries)

    def test_minimally_correct(self):
        """key trace/switch is mandatory"""
        eth = {"dl_vlan": 100}
        dpid = {"dpid": "a", "in_port": 1}
        switch = {"switch": dpid, "eth": eth}
        entries = {"trace": switch}
        self.trace_entries.load_entries(entries)
