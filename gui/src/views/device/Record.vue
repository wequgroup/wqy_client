<template>
  <div class="record">
    <v-container fluid>
      <v-row>
        <v-col cols="12" style="text-align: center">
          <v-alert dense outlined type="info" style="text-align: left">
            此功能可以录制你的自动化脚本，通过语音、文字、后台等地方即可触发！第一次使用请看视频教程！
          </v-alert>
        </v-col>
        <div class="tip-icon">
          <v-chip class="ma-2" color="pink" label text-color="white">
            <span class="mdi mdi-restart-alert micon"></span>
            点击&nbsp;<strong>录制脚本</strong>&nbsp;开始录制
          </v-chip>
          <v-chip class="ma-2" color="pink" label text-color="white">
            <span class="mdi mdi-restart-off micon"></span>
            按下&nbsp;<strong>Esc</strong>&nbsp;键退出录制
          </v-chip>
        </div>
        <v-col cols="12" class="record-list">
          <v-card>
            <v-table height="200px" density="compact" fixed-header>
              <thead>
                <tr>
                  <th class="text-left" style="width: 170px;">
                    ID
                  </th>
                  <th class="text-left" style="width: 270px;">
                    脚本名称
                  </th>
                  <th class="text-left" style="width: 100px;">
                    操作
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in desserts" :key="item.record_id">
                  <td>{{ item.record_id }}</td>
                  <td>{{ item.record_name }}</td>
                  <td><span class="mdi mdi-delete-outline" style="font-size: 1.3em;color: black;cursor: pointer;"
                      @click="deleteRecord(item.record_id)"></span>&nbsp;
                    <span class="mdi mdi-play-circle-outline" style="font-size: 1.3em;color: black;cursor: pointer;"
                      @click="runRecord(item.record_id)"></span>
                  </td>
                </tr>
              </tbody>
            </v-table>
          </v-card>
        </v-col>
      </v-row>
      <div class="record-btn">
        <v-btn @click="setRecordNameDialog = true"><span class="mdi mdi-timer-play micon"></span>
          录制脚本</v-btn>
        <v-btn style="margin-left: 17px;" color="indigo">
          <span class="mdi mdi-video-box micon"></span>
          视频教程
        </v-btn>
      </div>
    </v-container>
    <v-dialog v-model="setRecordNameDialog" width="auto">
      <v-card>
        <v-card-text>
          <v-alert density="compact" type="warning" title="请看这里"
            text="点击开始录制后，此窗口会被隐藏，此时所有的操作都会记录，按下 Esc 键后退出录制"></v-alert>
          <v-form @submit.prevent style="margin-top: 4px;">
            <v-text-field v-model="recordName" :rules="rules" label="输入录制名称"></v-text-field>
            <v-btn type="submit" block class="mt-2" @click="setRecord">点击开始录制</v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>
    <v-snackbar v-model="snackbar" :timeout="4000">
      {{ tipsText }}
      <template v-slot:actions>
        <v-btn color="blue" variant="text" @click="snackbar = false">
          关闭
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
import {
  getCurrentInstance
} from "vue";

export default {
  data: () => ({
    tipsText: "",
    desserts: [],
    snackbar: false,
    setRecordNameDialog: false,
    recordName: '',
    rules: [
      value => {
        if (value) return true
        return '名称便于识别，必须设置一个'
      },
    ],
  }),
  methods: {
    setRecordOk() {
      window['setRecordOk'] = (resJson) => {
        console.log("ddd")
        this.tipsText = "很好，你的脚本已经录制完成！"
      }
    },
    setRecord() {
      window.pywebview.api.set_record(this.recordName).then((res) => {
        this.setRecordNameDialog = false
        this.getRecord()
        this.tipsText = "很好，你的脚本已经录制完成！"
        this.snackbar = true
      })
    },
    deleteRecord(id) {
      window.pywebview.api.delete_record(id).then((res) => {
        this.getRecord()
      })
    },
    getRecord() {
      window.pywebview.api.get_record().then((res) => {
        this.desserts = res
      })
    },
    runRecord(id) {
      window.pywebview.api.run_record(id).then((res) => {
        this.tipsText = "测试已经完成，还满意吗！"
        this.snackbar = true
      })
    }
  },
  mounted() {
    let _this = this
    window.addEventListener('pywebviewready', function () {
      _this.getRecord()
    })
    this.setRecordOk()
  }
}
</script>

<style>
.record {
  font-size: 14px;
}

.record-btn {
  text-align: center;
  margin-top: 50px;
}

.micon {
  font-size: 20px;
  font-weight: bold;
  margin-right: 3px;
  vertical-align: -1px;
}

.tip-icon {
  margin-left: 3px;
  margin-top: -10px;
}
</style>
