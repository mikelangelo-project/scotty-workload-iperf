import logging

import paramiko
from scotty import utils

logger = logging.getLogger(__name__)


class Benchmark(object):
    def __init__(self, context):
        self.context = context
        workload = context.v1.workload
        exp_helper = utils.ExperimentHelper(context)
        resource_name = workload.resources['iperf']
        logger.debug("Resource name: {}".format(resource_name))
        resource = exp_helper.get_resource(resource_name)
        self.iperf_endpoint = resource.endpoint
        
    def run(self):
        logger.info('Run iperf client')
        self._execute_remote_iperf_client(
            self.iperf_endpoint['iperf-client']['ip'],
            self.iperf_endpoint['iperf-server']['ip'],
            self.iperf_endpoint['iperf-client']['user'],
            self.iperf_endpoint['iperf-client']['password']
        )

    def _execute_remote_iperf_client(self, iperf_client_ip, iperf_server_ip, iperf_user, iperf_password):
        with paramiko.SSHClient() as ssh:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(iperf_client_ip, username=iperf_user, password=iperf_password)
            cmd = "iperf -c {}".format(iperf_server_ip)
            stdin, stdout, stderr = ssh.exec_command(cmd)
            out = stdout.read()
        logger.info("IPerf:\r\n{}".format(out))
