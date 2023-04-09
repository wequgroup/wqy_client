<template>
  <v-container style="padding: 0">
    <v-row dense>
      <v-col cols="24">
        <v-card class="mx-auto" max-width="600" elevation="0" style="border-radius: 0!important;">
          <v-img src="@/assets/login.png" height="150px"></v-img>
          <v-card-title>
            登录您的WEQU账户
          </v-card-title>
          <v-card-subtitle>
            1,020+ 用户正在使用
          </v-card-subtitle>
          <v-form ref="form" v-model="valid" lazy-validation class="login">
            <v-text-field v-model="email" :rules="emailRules" label="你的邮箱" required></v-text-field>
            <v-text-field v-model="password" :rules="passwordRules" label="你的密码" type="password" required></v-text-field>
            <v-checkbox v-model="checkbox" label="记住我?" required style="margin-top: -24px;"></v-checkbox>
            <div class="loginBtn">
              <v-btn :disabled="!valid" color="success" class="mr-4" @click="verificationCode">
                立刻登录
              </v-btn>

              <v-btn color="error" class="mr-4" @click="reset">
                注册新账号
              </v-btn>
            </div>
          </v-form>

          <v-expand-transition>
            <div style="text-align: center">
              <v-divider></v-divider>
              <v-card-actions>
                <div style="color: #666;font-size: 13px;">Copyright © 2023 WEQU.NET</div>
                <v-spacer></v-spacer>
              </v-card-actions>
            </div>
          </v-expand-transition>
        </v-card>
      </v-col>
    </v-row>
    <v-snackbar v-model="snackbar" vertical location="top">
      <div class="text-subtitle-1 pb-2">发生了错误</div>
      <p>{{ tips }}</p>
      <template v-slot:actions>
        <v-btn color="pink" variant="text" @click="snackbar = false">
          关闭
        </v-btn>
      </template>
    </v-snackbar>
    <v-dialog v-model="login" hide-overlay persistent width="300">
      <v-card color="primary" dark>
        <v-card-text>
          <span style="font-size: 12px;letter-spacing: 2px;vertical-align: 10px;">正在登录到WEQU.NET ...</span>
          <v-progress-linear indeterminate color="white" class="mb-0"></v-progress-linear>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-container>
</template>
<script>
import { getCurrentInstance } from "vue";

export default {

  data: () => ({
    login: false,
    r: getCurrentInstance()?.appContext.config.globalProperties.$router,
    tips: "",
    snackbar: false,
    valid: true,
    password: null,
    apiPost: getCurrentInstance()?.appContext.config.globalProperties.$post,
    passwordRules: [
      v => !!v || '密码必须输入',
      v => (v && v.length >= 6),
    ],
    email: null,
    emailRules: [
      v => !!v || '好像不是正确的邮箱格式',
      v => /.+@.+\..+/.test(v) || '请输入正确的邮箱',
    ],
    checkbox: false,
  }),

  methods: {
    verificationCode() {
      let _this = this
      let captchaId = "2096394456"; //腾讯滑块验证码appid
      const captcha = new TencentCaptcha(captchaId, function (res) {
        if (res.ret === 0) {
          _this.login = true
          const data = {
            ticket: res.ticket,
            randStr: res.randstr,
            username: _this.email,
            password: _this.password
          }
          _this.apiPost("/login", data).then(res => {
            if (res.code === 200) {
              localStorage.setItem("token", res.token)
              if (_this.checkbox === true) {
                localStorage.setItem("username", _this.email)
                localStorage.setItem("password", _this.password)
                localStorage.setItem("checkbox", "true")
              } else {
                localStorage.removeItem("username")
                localStorage.removeItem("password")
                localStorage.setItem("checkbox", "false")
              }
              _this.$router.push({
                path: '/device'
              })
            } else {
              _this.login = false
              _this.snackbar = true
              _this.tips = res.msg
            }
          })
        }
      });
      captcha.langFun();
      // 滑块显示
      captcha.show();
    },
    validate() {
      this.$refs.form.validate()
    },
    reset() {
      this.$refs.form.reset()
    }
  },
  mounted() {
    if (localStorage.getItem("checkbox") === "true") {
      this.checkbox = true
      this.email = localStorage.getItem("username")
      this.password = localStorage.getItem("password")
    }
  }
}
</script>
<style scoped>
.login {
    padding: 100px;
    margin-top: -80px;
    margin-bottom: -76px;
}

:deep(.v-img__img--contain) {
  object-fit: cover;
}

:deep(.v-card-actions) {
  display: inline-flex;
}

.loginBtn {
  text-align: center;
  margin-bottom: 10px;
  margin-top: -18px;
}
</style>
