import logging

import iperf.workload.Benchmark

logger = logging.getLogger(__name__)

def run(context):
    logger.info('Run iperf workload with scotty')
    iperf_benchmark = iperf.workload.Benchmark(context)
    iperf_benchmark.run()

def clean(context):
    pass
