import logging
import os
import time


class SimulationLogger:
    def __init__(self, log_dir):
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = os.path.join(log_dir, 'simulation.log')
        logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    @staticmethod
    def log_blank_line():
        logging.info("")

    @staticmethod
    def log_params(params):
        logging.info("Simulation Parameters:")
        for key, value in params.items():
            logging.info(f"{key}: {value}")
        logging.info("")

    @staticmethod
    def log_progress(current_step, total_steps):
        logging.info(f"Progress: {current_step}/{total_steps}")

    @staticmethod
    def log_result_summary(result_summary):
        logging.info("Simulation Result Summary:")
        for key, value in result_summary.items():
            logging.info(f"{key}: {value}")
            logging.info("")

    @staticmethod
    def log_error(message):
        logging.error(message)
        logging.info("")

    @staticmethod
    def log_runtime(start):
        end = time.time()
        runtime_seconds = end - start
        logging.info(f"Simulation Runtime: {runtime_seconds:.2f} seconds")
        logging.info("")
