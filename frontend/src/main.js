import Vue from 'vue'
import App from './App.vue'
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';
import VueAxios from 'vue-axios'
import router from './router.js'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faBars } from '@fortawesome/free-solid-svg-icons'
import { faCaretDown } from '@fortawesome/free-solid-svg-icons'
import { faCaretUp } from '@fortawesome/free-solid-svg-icons'
import { faCheck } from '@fortawesome/free-solid-svg-icons'
import { faTimes } from '@fortawesome/free-solid-svg-icons'
import { faPencilAlt } from '@fortawesome/free-solid-svg-icons'
import { faTrashAlt } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faBars)
library.add(faCaretDown)
library.add(faCaretUp)
library.add(faCheck)
library.add(faTimes)
library.add(faPencilAlt)
library.add(faTrashAlt)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.use(VueAxios, axios)

Vue.config.productionTip = false

axios.defaults.baseURL = 'http://127.0.0.1:8000';

axios.interceptors.response.use(response => response, error => {
  if (error.response.status == 401 && "Authorization" in error.config.headers) {
    return axios.post("/token/refresh/",
        JSON.stringify({
          refresh: localStorage.getItem("refresh_token")
        }),
        {
          headers: {
            'Content-Type': 'application/json'
          }
        }).then((response) => {
          localStorage.access_token = response.data.access;
          let config = error.config;
          config.headers.Authorization = "Bearer " + response.data.access;
          return axios.request(config);
        });
  } else if (error.response.config.url === "/token/refresh/") {
    router.push('/login');
  }
  return Promise.reject(error);
})


Vue.mixin({
  methods: {
    refresh_token: function() {
      return axios.post("/token/refresh/",
        JSON.stringify({
          refresh: localStorage.getItem("refresh_token")
        }),
        {
          headers: {
            'Content-Type': 'application/json'
          }
        }).then((response) => {
          localStorage.access_token = response.data.access;
        });
    },
    login: function(email, password) {
      let payload = {
        email: email,
        password: password
      }

      axios.post("/token/",
        JSON.stringify(payload),
        {
          headers: {
            'Content-Type': 'application/json'
          }
        }).then((response) => {
          localStorage.access_token = response.data.access;
          localStorage.refresh_token = response.data.refresh;
          localStorage.time_set = Date.now();
          this.$emit('login');
      });
    }
  }
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
