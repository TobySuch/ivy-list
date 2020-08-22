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

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
