import logging


class PrependingFileHandler(logging.FileHandler):
    """
    A custom logging handler that prepends logs to the beginning of the file
    rather than appending to it.
    """

    def emit(self, record):
        # Convert the log record to string
        log_entry = self.format(record) + '\n'

        # Open the file in 'r+' mode to allow reading and writing
        with open(self.baseFilename, 'r+') as log_file:
            # Read the current content of the log file
            current_content = log_file.read()

            # Move to the beginning of the file and write the new log entry
            log_file.seek(0, 0)
            log_file.write(log_entry + current_content)
