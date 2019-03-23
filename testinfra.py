import unittest
import testinfra
# need to add RUN yum -y install initscripts
class docker_Test(unittest.TestCase):
    
    def setUp(self):
        self.host = testinfra.get_host("docker://[user]@[id]") #id for basic_config_master container

    def test_puppet_is_installed(self):
        assert self.host.check_output('puppet -v') == "5.5.10"

    def test_puppet_ser_is_installed(self):
        assert self.host.check_output('puppet agent --version') == "5.5.10"
        assert self.host.check_output('puppet master --version') == "5.5.10"

    def test_rsyslog_running_and_enabled(self):
        rsyslog = self.host.service("rsyslog")
        assert rsyslog.is_running
        assert rsyslog.is_enabled

    def test_ssh_running_and_enabled(self):
        ssh = self.host.service("ssh")
        assert ssh.is_running
        assert ssh.is_enabled
if __name__ == "__main__":
    unittest.main()
