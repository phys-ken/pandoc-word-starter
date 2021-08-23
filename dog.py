#!/usr/bin/env python
from __future__ import print_function

import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


watch_dir_path = "./"
watch_file = "01_input.md"


class MyHandler(PatternMatchingEventHandler):
    def __init__(self,  patterns):
        super(MyHandler, self).__init__(patterns=patterns)

    def _run_command(self):
        subprocess.run(["pandoc" , "-d" , "defaults.yml" ])
        subprocess.run(["echo" , "変更を検知して、変換しました。" ])

    def on_moved(self, event):
        self._run_command()

    def on_created(self, event):
        self._run_command()

    def on_deleted(self, event):
        self._run_command()

    def on_modified(self, event):
        self._run_command()


def watch(path, extension):
    event_handler = MyHandler( ["*"+extension])
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
  print(watch_dir_path + "/" + watch_file + "を監視します。ワンワン。")
  watch(watch_dir_path , watch_file)