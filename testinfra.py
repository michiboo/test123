# for some reason path variable is not same container if connect from testinfra and it has to renew path variable everytime
# need to run as sudo
path = 'export PATH="/usr/sue/sbin:/usr/sue/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/puppetlabs/bin" && '

import unittest
import testinfra
class docker_Test(unittest.TestCase):
    
    def setUp(self):
        self.host = testinfra.get_host("docker://root@[id]") #id for basic_config_master container

    def test_puppet_is_installed(self):
        assert self.host.check_output(path + 'puppet --version') == "5.5.10"

    def test_puppet_ser_is_installed(self):
        assert self.host.check_output(path + 'puppet agent --version') == "5.5.10"
        assert self.host.check_output(path + 'puppet master --version') == "5.5.10"

    def test_rsyslog_running(self):
        assert self.host.check_output(path + 'pgrep -x rsyslogd')  

    def test_ssh_running(self):
        assert self.host.check_output(path + 'pgrep -x sshd')  
if __name__ == "__main__":
    unittest.main()
