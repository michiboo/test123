def test_puppet_is_installed(host):
    nginx = host.package("puppet")
    assert nginx.is_installed

def test_puppet_ser_is_installed(host):
    nginx = host.package("puppetserver")
    assert nginx.is_installed

def test_rsyslog_running_and_enabled(host):
    rsyslog = host.service("rsyslog")
    assert rsyslog.is_running
    assert rsyslog.is_enabled

def test_ssh_running_and_enabled(host):
    ssh = host.service("ssh")
    assert ssh.is_running
    assert ssh.is_enabled