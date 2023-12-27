<script setup lang="ts">
import { RouterView } from 'vue-router';
import MainView from './Main.vue';
</script>

<template>
    <v-locale-provider >
        <v-app>
            <div>
                <MainView />
                <RouterView />
            </div>


                    <div>
                        
                    </div>


        </v-app>
    </v-locale-provider>
</template>
