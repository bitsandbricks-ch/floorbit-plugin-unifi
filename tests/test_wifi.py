"""UniFi as a Wi-Fi source: access points, radios and client counts for the Wi-Fi view."""
from floorbit import wifi


def test_unifi_wifi_aps(make):
    plugin = make(url="https://unifi.example.com", username="floorbit", password="example-password")
    plugin._get = lambda what: [
        {'type': 'usw', 'name': 'sw-1'},
        {'type': 'uap', 'name': 'ap-hall-01', 'model': 'U6PRO', 'state': 1, 'num_sta': 21,
         'radio_table': [{'radio': 'ng', 'ht': '20'}, {'radio': 'na', 'ht': '80'}],
         'radio_table_stats': [{'radio': 'ng', 'channel': 1, 'cu_total': 55, 'num_sta': 5},
                               {'radio': 'na', 'channel': 44, 'cu_total': 20, 'num_sta': 16}]},
        {'type': 'uap', 'name': 'ap-hall-02', 'state': 0}]
    aps = [wifi.clean_ap(a) for a in plugin.wifi_aps()]
    assert [a['name'] for a in aps] == ['ap-hall-01', 'ap-hall-02']
    assert aps[0]['radios'][1] == {'band': '5', 'channel': 44, 'width': 80, 'utilization': 20, 'clients': 16}
    assert aps[0]['clients'] == 21 and aps[1]['status'] == 'down'
