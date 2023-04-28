<template>
  <div class="">
    <div class="view-log-btn">
      <v-btn size="small" text v-if="!showLog && !notDevice" @click="showLog = true">
        <span class="mdi mdi-eye-arrow-right-outline"></span>
        &nbsp;查看日志
      </v-btn>&nbsp;
      <a href="https://app.wequ.net/duck/device" target="_blank" style="color:#444;text-decoration:none">
      <v-btn size="small" text v-if="!showLog && !notDevice">
        <span class="mdi mdi-view-dashboard"></span>
        &nbsp;管理后台
      </v-btn>
      </a>
    </div>
    <div class="view-close-log-btn" v-if="showLog">
      <v-btn @click="showLog = false" density="compact" icon="mdi-eye-off-outline" size="small"></v-btn>
    </div>
    <div class="log" v-if="showLog">
      <p v-for="i in logList">{{ i.time }} - {{ i.msg }}</p>
    </div>
    <v-container style="height: 100%;">
      <v-row no-gutters>
        <v-col cols="12" md="8">
          <v-btn block @click="addDialog = true" v-if="notDevice" color="info">
            <span class="mdi mdi-plus"></span> 添加一个设备
          </v-btn>
          <v-card class="mx-auto device-card" prepend-icon="mdi-monitor-cellphone-star" elevation="5" v-if="!notDevice">
            <template v-slot:title>
              <div style="font-size: 15px;font-weight: 600;display: inline;">{{ this.deviceInfo.device_name }}</div>
              <div class="auto-online">
              <v-switch :label="deviceInfo.auto_online == 'yes' ? '自动连接打开' : '自动连接关闭'" true-value="yes" false-value="no"
                  v-model="deviceInfo.auto_online" color="info" @change="updateOnline"></v-switch></div>
            </template>
            <v-card-text>
              <div style="padding-left: 13px;">
                <span v-if="!deviceOnline">未连接到服务器，请点&nbsp;<span class="mdi mdi-cast-connected"></span>&nbsp;按钮连接</span>
                <span v-if="deviceOnline">已连接到服务器，点&nbsp;<span class="mdi mdi-web-off"></span>&nbsp;按钮可断开连接</span>
              </div>
              <div style="float: right;margin-bottom: 10px;">
                <v-btn v-bind="props" size="small" variant="text" v-if="!deviceOnline" @click="connectService">
                  <span class="mdi mdi-cast-connected" style="font-size: 1.8em;color: #fff;"></span>
                </v-btn>
                <v-tooltip text="强行断开，不会自动重连" location="start" v-if="deviceOnline">
                  <template v-slot:activator="{ props }">
                    <v-btn v-bind="props" size="small" variant="text" @click="dissConnect">
                      <span class="mdi mdi-web-off" style="font-size: 1.8em;color: #fff;"></span>
                    </v-btn>
                  </template>
                </v-tooltip>
                <v-tooltip text="编辑设备信息" location="bottom">
                  <template v-slot:activator="{ props }">
                    <v-btn v-bind="props" size="small" variant="text" @click="addDialogClick('update')">
                      <span class="mdi mdi-archive-edit" style="font-size: 1.8em;color: #fff;"></span>
                    </v-btn>
                  </template>
                </v-tooltip>
              </div>
            </v-card-text>
          </v-card>
          <div class="device-online" v-if="deviceOnline"></div>
          <div class="device-offline" v-if="!deviceOnline"></div>
        </v-col>
      </v-row>
    </v-container>
    <v-dialog max-width="480" v-model="addDialog" transition="dialog-top-transition">
      <v-card>
        <v-card-text>
          <br>
          <v-alert dense type="error" style="font-size: 14px;padding: 5px;margin-bottom: 4px;" v-if="addError">
            {{ addErrorText }}
          </v-alert>
          <v-text-field density="compact" placeholder="请输入设备ID" prepend-inner-icon="mdi-monitor-cellphone-star"
            variant="outlined" v-model="deviceInfo.device_id"></v-text-field>
          <v-text-field v-model="deviceInfo.device_password"
            :append-inner-icon="passwordVisible ? 'mdi-eye-off' : 'mdi-eye'" :type="passwordVisible ? 'text' : 'password'"
            density="compact" placeholder="请输入设备密码" prepend-inner-icon="mdi-lock-outline" variant="outlined"
            @click:append-inner="passwordVisible = !passwordVisible"></v-text-field>
          <v-switch label="自动连接" true-value="yes" false-value="no" v-model="deviceInfo.auto_online"
            color="brown lighten-5"></v-switch>
          <v-card class="mb-12" color="surface-variant" variant="tonal">
            <v-card-text class="text-medium-emphasis text-caption">
              设备id和设备密钥可在 <a href="https://app.wequ.net" target="_blank">设备管理后台</a> 上查看，如果你不会使用，建议你先看看视频教程进行学习！
            </v-card-text>
          </v-card>
          <v-btn color="info" block @click="addDevice" elevated :loading="addLoading">保存设备信息</v-btn>
          <br>
        </v-card-text>
      </v-card>
    </v-dialog>
    <v-dialog v-model="updateDialog" width="500" persistent>
      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          有新版本
        </v-card-title>
        <v-card-text>
          <h4>{{ updateName }}</h4>
          <p :v-html="updateContent"></p>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="updateDialog = false" v-if="!mustUpdate">
            不升级
          </v-btn>
          <v-btn color="info" text @click="updateApp">
            立刻升级
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
const v = 2
import { getCurrentInstance } from 'vue'

export default {
  data: () => ({
    apiGet: getCurrentInstance()?.appContext.config.globalProperties.$get,
    deviceInfo: { "device_id": "", "device_name": '加载中...', "device_password": "", "auto_online": 'no' },
    showLog: false,
    addDialog: false,
    notDevice: true,
    passwordVisible: false,
    deviceId: '',
    devicePassword: '',
    autoOnline: 'no',
    addError: false,
    addLoading: false,
    addErrorText: '',
    deviceOnline: false,
    update: false,
    logList: [],
    updateDialog: false,
    updateName: '升级提示',
    updateContent: '',
    updateUrl: '',
    mustUpdate: false
  }),
  methods: {
    addDialogClick(action) {
      if (action == "update") {
        this.update = true
      }
      this.addDialog = true
    },
    updateApp(){
      window.open(this.updateUrl)
    },
    getAppUpdate() {
      this.apiGet("/duck/post/2").then(res => {
         let data = res.data
         this.updateName = data.name
         let value  = JSON.parse(data.value)
         if(value[0]['num'] > v){
          this.updateDialog = true
         }
         this.updateContent = value[0]['content']
         this.updateUrl = value[0]['download']
         this.mustUpdate = value[0]['update']
      })
    },
    updateOnline(){
      this.update = true
      this.addDevice()
    },
    goDash(){
    console.log("ddd")
    window.open(`https://www.cnblogs.com/guorongtao/`)
    },
    addDevice() {
      if (this.deviceInfo.device_id.length != 8 || this.deviceInfo.device_password.length < 6) {
        this.addError = true
        this.addErrorText = "请输入设备ID和设备密码"
      }
      this.addLoading = true
      this.apiGet("/duck/device/client/" + this.deviceInfo.device_id + "/" + this.deviceInfo.device_password).then(res => {
        if (res.data == null) {
          this.addErrorText = "无法查询到该设备信息"
          this.addError = true
          this.addLoading = false
        } else {
          this.deviceInfo.device_name = res.data.deviceName
          setTimeout(() => {
            if (this.update == true) {
              this.deviceInfo.action = "update"
            } else {
              this.deviceInfo.action = "add"
            }
            console.log(this.deviceInfo)
            window.pywebview.api.add_device(this.deviceInfo).then((res) => {
              this.update == false
              if (res == "ok") {
                this.addDialog = false
                this.notDevice = false
              } else {
                this.addErrorText = "添加设备失败"
                this.addError = true
              }
              this.addLoading = false
            })
          }, 200)
        }
      })
    },
    getDevice() {
      window.pywebview.api.get_device().then((res) => {
        if (res == null) {
          this.notDevice = true
        } else {
          this.deviceInfo = res
          if (this.deviceInfo.auto_online == "yes") {
            this.connectService(this.deviceInfo)
          }
          this.notDevice = false
        }
      })
    },
    connectService(res) {
      window.pywebview.api.connect(this.deviceInfo.device_id, this.deviceInfo.device_password).then((res) => {
        console.log(res)
      })
    },
    dissConnect() {
      window.pywebview.api.diss_connect().then((res) => {
        if (res == "ok") {
          this.deviceOnline = false
        }
      })
    },
    connectSuccess() {
      window['connectSuccess'] = (resJson) => {
        const res = JSON.parse(resJson)
        if (res.online === 'success') {
          this.showLog = true
          this.deviceOnline = true
        }
      }
    },
    writeLog() {
      window['writeLog'] = (resJson) => {
        const res = JSON.parse(resJson)
        console.log(res)
        this.logList.unshift(res)
      }
    }
  },
  mounted() {
    this.getAppUpdate()
    let _this = this
     setTimeout(() => {
     this.getDevice()
     },400)
    this.connectSuccess()
    this.writeLog()
  },
  created() {

  }
}
</script>
<style>
.v-switch .v-label{
  font-size:14px;
  margin-left: -3px
}
.device-card {
  background-color: #0093E9;
  background-image: linear-gradient(160deg, #0093E9 0%, #80D0C7 100%);
  color: #fff;
}

.device-card i.mdi-monitor-cellphone-star.mdi.v-icon.notranslate.v-theme--light.v-icon--size-default {
  color: #fff;
}

.auto-online {
  width: 130px;
  position: absolute;
  right: 10px;
  top: 0px;
}

.device-online {
  height: 360px;
  margin-top: 43px;
  background-repeat: no-repeat;
  background-size: 301px;
  background-position: center;
  background-image: url(@/assets/device_online.png);
}

.device-offline {
  height: 360px;
  margin-top: 44px;
  background-repeat: no-repeat;
  background-size: 300px;
  background-position: center;
  background-image: url(@/assets/device_offline.png);
  -webkit-filter: grayscale(100%);
  filter: grayscale(100%);
}

.log {
  position: absolute;
  z-index: 888;
  top: 160px;
  left: 74px;
  background: black;
  height: 430px;
  width: 500px;
  opacity: 0.4;
  color: #fff;
  padding: 10px;
  font-size: 14px;
  overflow-y: scroll;
  overflow-x: scroll;
  border-radius: 5px;
}

.view-log-btn {
  position: absolute;
  top: 170px;
  left: 73px;
  z-index: 99
}

.view-close-log-btn {
  position: absolute;
  top: 155px;
  right: 18px;
  z-index: 999;
}

/* .v-input__details {
    display: none;
} */
</style>
