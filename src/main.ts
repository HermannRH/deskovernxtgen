import { createApp } from 'vue';
import App from './App.vue';
import { router } from './router';
import vuetify from './plugins/vuetify';
import './scss/style.scss';
import PerfectScrollbar from 'vue3-perfect-scrollbar';
import VueApexCharts from 'vue3-apexcharts';
import VueTablerIcons from 'vue-tabler-icons';
import Notifications from '@kyvg/vue3-notification'

const app = createApp(App);
app.use(Notifications)
app.use(router);
app.use(PerfectScrollbar);
app.use(VueTablerIcons);
app.use(VueApexCharts);
app.use(vuetify);

app.mount('#app');

app.config.warnHandler = function (msg, vm, trace) {
  // Check if the warning message matches "[Vuetify UPGRADE] globally"
  if (msg.includes('[Vuetify UPGRADE]')) {
    // Mute the warning
    return;
  }

  // Default behavior for other warning messages
  console.warn(msg, vm, trace);
};

  