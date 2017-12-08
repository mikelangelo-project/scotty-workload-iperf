import logging

logger = logging.getLogger(__name__)


class Benchmark(object):
    def __init__(self, context):
        self.context = context
        self.iperf_endpoint = {
            'iperf-server': {
            'ip': '10.254.1.198',
            'user': 'scotty',
            'password': '1PV4JSP5'
          },
          'iperf-client': {
            'ip': '141.5.113.248'
            'user': 'scotty',
            'password': '1PV4JSP5'
          }
        }

    def run(self):
        logger.info('Run iperf client')
        self._execute_remote_iperf_client(
            self.iperf_endpoint['iperf-client']['ip'],
            self.iperf_endpoint['iperf-server']['ip'],
            self.iperf_endpoint['iperf-client']['user'],
            self.iperf_endpoint['iperf-client']['password']
        )

    def _execute_remote_iperf_client(self, iperf_client_ip, iperf_server_ip, iperf_user, iperf_password):
        with paramiko.SSHClient() as ssh
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(iperf_client_ip, username=iperf_scotty_user, password=iperf_scotty_password)
            cmd = "iperf -c {}".format(iperf_server_ip)
            stdin, stdout, stderr = ssh.exec_command(cmd)
            out = stdout.read()
        logger.info("IPerf:")
        logger.info(out)
