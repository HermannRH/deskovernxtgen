import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from '@/views/start.vue';
import LoginForm from '@/views/loginform.vue';

export const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: Dashboard,
    },
    {
      path: '/login',
      component: LoginForm,
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/',
    },
  ],
});