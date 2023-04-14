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
                  <th class="text-left">
                    脚本名称
                  </th>
                  <th class="text-left">
                    脚本ID
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in desserts" :key="item.name">
                  <td>{{ item.name }}</td>
                  <td>{{ item.calories }}</td>
                </tr>
              </tbody>
            </v-table>
          </v-card>
        </v-col>
      </v-row>
      <div class="record-btn">
        <v-btn><span class="mdi mdi-timer-play micon"></span>
          录制脚本</v-btn>
        <v-btn style="margin-left: 17px;" color="indigo">
          <span class="mdi mdi-video-box micon"></span>
          视频教程
        </v-btn>
      </div>
    </v-container>
  </div>
</template>

<script>
  import {
    getCurrentInstance
  } from "vue";

  export default {
    data: () => ({
      desserts: [{
          name: 'Frozen Yogurt',
          calories: 159,
        },
        {
          name: 'Ice cream sandwich',
          calories: 237,
        },
        {
          name: 'Eclair',
          calories: 262,
        },
        {
          name: 'Cupcake',
          calories: 305,
        },
        {
          name: 'Gingerbread',
          calories: 356,
        },
        {
          name: 'Jelly bean',
          calories: 375,
        },
        {
          name: 'Lollipop',
          calories: 392,
        },
        {
          name: 'Honeycomb',
          calories: 408,
        },
        {
          name: 'Donut',
          calories: 452,
        },
        {
          name: 'KitKat',
          calories: 518,
        },
      ]
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
