<template>
    <div class="script">
      <v-container fluid>
        <v-row>
          <v-col cols="12" style="text-align: center">
            <v-alert dense outlined type="info" style="text-align: left">
              此功能可以录制你的自动化脚本，通过语音、文字、后台等地方即可触发！第一次使用请看视频教程！
            </v-alert>
          </v-col>
        </v-row>
      </v-container>
    </div>
</template>

<script>
import {getCurrentInstance} from "vue";

export default {
  data: () => ({

  }),
  methods: {
    setScript() {
      window.pywebview.api.record().then((res) => {
        console.log(res)
      })
    }
  }
}
</script>

<style>
</style>
