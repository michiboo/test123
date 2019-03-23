import unittest
import testinfra

class docker_Test(unittest.TestCase):
    
    def setUp(self):
        self.host = testinfra.get_host("docker://micky@[id]")

    def test_puppet_is_installed(host):
        puppet = host.package("puppet")
        assert puppet.is_installed

    def test_puppet_ser_is_installed(host):
        puppet_ser = host.package("puppetserver")
        assert puppet_ser.is_installed

    def test_rsyslog_running_and_enabled(host):
        rsyslog = host.service("rsyslog")
        assert rsyslog.is_running
        assert rsyslog.is_enabled

    def test_ssh_running_and_enabled(host):
        ssh = host.service("ssh")
        assert ssh.is_running
        assert ssh.is_enabled
if __name__ == "__main__":
    unittest.main()
