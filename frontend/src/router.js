import Vue from 'vue'
import Router from 'vue-router'

import HomeView from './views/HomeView'
import LoginView from './views/LoginView'
import RegistrationView from './views/RegistrationView'
import ToDoView from './views/ToDoView'


Vue.use(Router)

function guardRoute(to, from, next)
{
  if(localStorage.getItem('time_set')) {
    next(); // allow to enter route
    return;
  }
  next('/login'); // go to '/login';
}

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
    path: '/register',
    name: 'Register',
    component: RegistrationView
  },
  {
    path: '/todo',
    name: 'To Do',
    component: ToDoView,
    beforeEnter: guardRoute
  }
]


export default new Router({
  mode: 'history',
  routes: routes
})