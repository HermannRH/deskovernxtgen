const MainRoutes = {
    path: '/main',
    meta: {
      requiresAuth: true
    },
    redirect: '/main',
    component: () => import('@/layouts/full/FullLayout.vue'),
    children: [
      {
        name: 'Dashboard',
        path: '/',
        component: () => import('@/views/components/dashboard.vue')
      },
      {
        name: 'Calendario',
        path: '/ui/calendario',
        component: () => import('@/views/components/calendario.vue')
      },
      {
        name: 'Gestión de Labores',
        path: '/ui/gestion-de-labores',
        component: () => import('@/views/components/gestion-de-labores.vue')
      },
      {
        name: 'Finanzas',
        path: '/ui/finanzas',
        component: () => import('@/views/components/finanzas.vue')
      },
      {
        name: 'Geovisualizador',
        path: '/ui/geovisualizador',
        component: () => import('@/views/components/geovisualizador.vue')
      },
      {
        name: 'Radar Legal',
        path: '/ui/radar-legal',
        component: () => import('@/views/components/radar-legal.vue')
      },
      {
        name: 'Redes Sociales',
        path: '/ui/redes-sociales',
        component: () => import('@/views/components/redes-sociales.vue')
      },
      {
        name: 'WhatsApp',
        path: '/ui/whatsapp',
        component: () => import('@/views/components/whatsapp.vue')
      },
      {
        name: 'Teléfonos',
        path: '/ui/telefonos',
        component: () => import('@/views/components/telefonos.vue')
      },
      {
        name: 'Voluntarios',
        path: '/ui/voluntarios',
        component: () => import('@/views/components/voluntarios.vue')
      },
      {
        name: 'Promovidos',
        path: '/ui/promovidos',
        component: () => import('@/views/components/promovidos.vue')
      },
      {
        name: 'Coordinadores',
        path: '/ui/coordinadores',
        component: () => import('@/views/components/coordinadores.vue')
      },
      {
        name: 'RGS y RCS',
        path: '/ui/rgs-y-rcs',
        component: () => import('@/views/components/rgs-y-rcs.vue')
      },
      {
        name: 'VIPs',
        path: '/ui/vips',
        component: () => import('@/views/components/vips.vue')
      },
      {
        name: 'Mapas',
        path: '/ui/mapas',
        component: () => import('@/views/components/mapas.vue')
      },
      {
        name: 'Social Listening',
        path: '/ui/social-listening',
        component: () => import('@/views/components/social-listening.vue')
      },
      {
        name: 'Mediciones',
        path: '/ui/mediciones',
        component: () => import('@/views/components/mediciones.vue')
      },
      {
        name: 'Informes',
        path: '/ui/informes',
        component: () => import('@/views/components/informes.vue')
      },
      {
        name: 'Dossier',
        path: '/ui/dossier',
        component: () => import('@/views/components/dossier.vue')
      },
      {
        name: 'Plataforma Política',
        path: '/ui/plataforma-politica',
        component: () => import('@/views/components/plataforma-politica.vue')
      }
    ]
  };
  
  export default MainRoutes;
