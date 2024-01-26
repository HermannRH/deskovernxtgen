import { createRouter, createWebHistory } from 'vue-router';
import LoginForm from '@/views/loginform.vue';

export const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: LoginForm,
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/',
    },
  ],
});