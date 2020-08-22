import Vue from 'vue'
import Router from 'vue-router'

import HomeView from './views/HomeView'
import LoginView from './views/LoginView'
import ToDoView from './views/ToDoView'


Vue.use(Router)

let routes = [
  {
    path: '',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'Log In',
    component: LoginView
  },
  {
    path: '/todo',
    name: 'To Do',
    component: ToDoView
  }
]


export default new Router({
  mode: 'history',
  routes: routes
})