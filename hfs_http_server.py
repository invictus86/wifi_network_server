# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import logging
from airtest.core.settings import Settings
from airtest.utils.logger import get_logger

logger = get_logger("airtest")
logger.setLevel(logging.INFO)  # airtest日志级别
# logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                    filename='./log/hfs_http_server.log',
                    filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    # a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    # 日志格式
                    )

Settings.THRESHOLD = 0.9
Settings.THRESHOLD_STRICT = 0.9
Settings.FIND_TIMEOUT = 5


def reset_to_hfs_menu():
    if not cli_setup():
        auto_setup(__file__, devices=[
            "Windows:///?title_re=HFS ~ HTTP*"])


def set_hfs_limit(limit_speed):
    try:
        reset_to_hfs_menu()
        assert_exists(Template(r"./images/HFS.png"))
        touch(Template(r"./images/HFS_menu.png", threshold=0.9))
        time.sleep(1)
        touch(Template(r"./images/HFS_limits.png", threshold=0.9))
        time.sleep(1)
        touch(Template(r"./images/HFS_speed_limit.png", threshold=0.9))
        time.sleep(1)
        text(str(limit_speed))
        time.sleep(1)
        keyevent("{ENTER}")
        logging.info('set_hfs_limit success')
    except:
        logging.info('set_hfs_limit fail')


def set_hfs_switch_off():
    try:
        start_time = time.time()
        reset_to_hfs_menu()
        try:
            assert_exists(Template(r"./images/HFS.png", threshold=0.9))
            assert_exists(Template(r"./images/HFS_port_80.png", threshold=0.9))
            time.sleep(1)
            keyevent("{F4}")
            time.sleep(1)
            assert_exists(Template(r"./images/HFS_switch_off.png", threshold=0.9))
        except:
            assert_exists(Template(r"./images/HFS.png", threshold=0.9))
            assert_exists(Template(r"./images/HFS_switch_off.png", threshold=0.9))
        end_time = time.time()
        logging.info('set_hfs_switch_off success')
        return end_time - start_time
    except:
        logging.info('set_hfs_switch_off fail')
        return 0


def set_hfs_switch_on():
    try:
        start_time = time.time()
        reset_to_hfs_menu()
        try:
            assert_exists(Template(r"./images/HFS.png", threshold=0.9))
            assert_exists(Template(r"./images/HFS_switch_off.png", threshold=0.9))
            time.sleep(1)
            keyevent("{F4}")
            time.sleep(1)
            assert_exists(Template(r"./images/HFS_port_80.png", threshold=0.9))
        except:
            assert_exists(Template(r"./images/HFS.png", threshold=0.9))
            assert_exists(Template(r"./images/HFS_port_80.png", threshold=0.9))
        end_time = time.time()
        logging.info('set_hfs_switch_on success')
        return end_time - start_time
    except:
        logging.info('set_hfs_switch_on fail')
        return 0


def set_hfs_external_network():
    try:
        reset_to_hfs_menu()
        assert_exists(Template(r"./images/HFS.png"))
        touch(Template(r"./images/HFS_menu.png", threshold=0.9))
        time.sleep(1)
        touch(Template(r"./images/HFS_ip_address.png", threshold=0.9))
        time.sleep(1)
        touch(Template(r"./images/HFS_speed_external_ip.png", threshold=0.9))
        logging.info('set_hfs_external_network success')
    except:
        logging.info('set_hfs_external_network fail')


if __name__ == '__main__':
    # set_hfs_limit(10000)
    # set_hfs_switch_off()
    set_hfs_external_network()
