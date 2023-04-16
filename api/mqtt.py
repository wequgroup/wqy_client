import paho.mqtt.client as mqtt
import time
import json
import _thread
from threading import Event
from api import g


class MQTT:

    def __init__(self, user_name, password, host, port, auto_online=False, win=None):
        self.client = mqtt.Client(client_id=user_name)
        self.client.keep_alive = 60
        self.client.username_pw_set(username=user_name, password=password)
        self.host = host
        self.port = port
        self.auto_online = auto_online
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.username = user_name
        self.stop = False
        self.win = win
        self.stop = False
        self.event = Event()
        _thread.start_new_thread(self.stop_mq, ())

    # 定义连接断开的回调函数
    def on_disconnect(self, rc, a, b):
        while rc != 0 and rc != 5:
            time.sleep(5)
            try:
                rc = self.client.reconnect()
            except:
                print("Failed to reconnect to MQTT broker")
                time.sleep(15)

    def on_connect(self, client, userdata, rc, msg):
        if msg == 5:
            print("鉴权失败，不重连")
            self.auto_online = False
            self.stop = True
            log = {"msg": "登录失败，可能设备在其他地方登录，或设备信息错误"}
            self.win.evaluate_js(f"writeLog('{json.dumps(log)}')")
            self.client.loop_stop()
        if msg == 0:
            data = {"online": "success"}
            self.win.evaluate_js(f"connectSuccess('{json.dumps(data)}')")
            self.write_log("设备连接服务端成功")

    def on_message(self, client, userdata, rc):
        """收到消息了"""
        msg = rc.payload  # 将信息转换成json格式
        try:
            params = json.loads(msg)
            self.write_log(params["shellContent"])
        except:
            return False
        return True

    def write_log(self, msg):
        log = {"msg": msg, "time": time.strftime('%H:%M:%S')}
        self.win.evaluate_js(f"writeLog('{json.dumps(log)}')")

    def ping(self):
        """50秒发个心跳"""
        while True:
            if self.stop is True:
                break
            else:
                print("ping bang")
                self.client.publish("0", "1")
                self.event.wait(50)

    def start(self):
        # 连接到MQTT服务器
        self.write_log("连接服务器中...")
        rc = self.client.connect(self.host, self.port)
        if rc == 0:
            self.client.subscribe(topic=str("duck/" + self.username), qos=0)
            self.client.loop_start()
            self.ping()
        else:
            self.write_log("连接失败")
            pass

    def stop_mq(self):
        while True:
            if g.STOP_MQ:
                self.stop = True
                self.client.disconnect()
                self.client.loop_stop()
                self.event.set()
                g.STOP_MQ = False
                self.write_log("设备已下线.")
                break
            time.sleep(0.2)
