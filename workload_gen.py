import logging

import iperf.workload

logger = logging.getLogger(__name__)

def run(context):
    logger.info('Run iperf workload with scotty')
    iperf_benchmark = iperf.workload.Benchmark(context)
    reduce_logging()
    iperf_benchmark.run()

def clean(context):
    pass

def reduce_logging():
    reduce_loggers = {
        'paramiko',
        'paramiko.transport'
    }
    for logger in reduce_loggers:
        logging.getLogger(logger).setLevel(logging.WARNING)
