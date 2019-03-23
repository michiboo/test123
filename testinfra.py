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

    def test_rsyslog_running(self):
        assert self.host.check_output('pgrep rsyslogd')  

    def test_ssh_running(self):
        assert self.host.check_output('pgrep sshd')  
if __name__ == "__main__":
    unittest.main()
