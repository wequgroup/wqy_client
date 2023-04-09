import axios from 'axios';
import QS from 'qs';

axios.defaults.baseURL = 'http://localhost:8080'

axios.interceptors.request.use( //响应拦截
        async config => {
            config.headers.Authorization = 'Bearer ' + sessionStorage.getItem('token')
            return config;
        },
        error => {
            return Promise.error(error);
        })
    // 响应拦截器
axios.interceptors.response.use(
    response => {
        if (response.status === 200) {
            return Promise.resolve(response); //进行中
        } else {
            return Promise.reject(response); //失败
        }
    },
    // 服务器状态码不是200的情况
    error => {
        if (error.response.status) {
            switch (error.response.status) {

                case 401:
                    break

                case 403:
                    sessionStorage.clear()
                    break
                    // 404请求不存在
                case 404:
                    break;
                default:
            }
            return Promise.reject(error.response);
        }
    }
);
/**
 * get方法，对应get请求
 * @param {String} url [请求的url地址]
 * @param {Object} params [请求时携带的参数]
 */
const $get = (url, params) => {
        return new Promise((resolve, reject) => {
            axios.get(url, {
                    params: params,
                })
                .then(res => {
                    resolve(res.data);
                })
                .catch(err => {
                    reject(err.data)
                })
        });
    }
    /**
     * post方法，对应post请求
     * @param {String} url [请求的url地址]
     * @param {Object} params [请求时携带的参数]
     */
const $post = (url, params) => {
        return new Promise((resolve, reject) => {
            axios.post(url, params) //是将对象 序列化成URL的形式，以&进行拼接
                .then(res => {
                    resolve(res.data);
                })
                .catch(err => {
                    reject(err.data)
                })
        });
    }
    //下面是vue3必须加的，vue2不需要，只需要暴露出去get，post方法就可以
export default {
    install: (app) => {
        app.config.globalProperties['$get'] = $get;
        app.config.globalProperties['$post'] = $post;
        app.config.globalProperties['$axios'] = axios;
    }
}
