import os 
import unittest
from torswitch import TorProtocol

class TestTorProtocol(unittest.TestCase):

    def setUp(self) -> None:
        self.tor = TorProtocol()
        return super().setUp()
    
    def test_start(self):
        
        self.assertIsNone(self.tor.session)
        self.tor.Start()
        self.assertIsNotNone(self.tor.session)
        self.tor.Stop()
        

    def test_current_ip(self):
        self.tor.Start()
        current_ip = self.tor.CurrentIp()
        self.assertIsNotNone(current_ip)
        self.tor.Stop()

    def test_current_tor_ip(self):    
        self.tor.Start()
        current_tor_ip = self.tor.CurrentTorIp()
        self.assertIsNotNone(current_tor_ip)
        self.tor.Stop()

    def test_new_tor_ip(self):
        self.tor.Start()     
        current_tor_ip = self.tor.CurrentTorIp()
        new_tor_ip = self.tor.NewTorIp()
        self.assertNotEqual(current_tor_ip, new_tor_ip)
        self.tor.Stop()
       

    def test_absolute_new_tor_ip(self):
        self.tor.Start()
        current_tor_ip = self.tor.CurrentTorIp()
        absolute_new_tor_ip = self.tor.AbsoluteNewTorIp()
        self.assertNotEqual(current_tor_ip, absolute_new_tor_ip)
        self.tor.Stop()
       

    def test_tor_ip_rotation(self):
        self.tor.Start()
        initial_tor_ip = self.tor.CurrentTorIp()
        self.tor.TorIpRotation(delay=1, limit=3)
        final_tor_ip = self.tor.CurrentTorIp()
        self.assertNotEqual(initial_tor_ip, final_tor_ip)
        self.tor.Stop()
        

    def test_stop(self):
        self.tor.Stop()
        self.assertIsNone(self.tor.session)
    
    def tearDown(self):
        os.system('kill $(pgrep tor)')
        return super().setUp()
        

if __name__ == '__main__':
    unittest.main()
