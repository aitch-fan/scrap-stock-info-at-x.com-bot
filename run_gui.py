import sys
import os

# src 폴더를 PYTHONPATH에 추가하여 src 내부 모듈을 임포트할 수 있도록 함
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from gui import launch_gui

if __name__ == '__main__':
    launch_gui()