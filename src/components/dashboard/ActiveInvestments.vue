<script setup lang="ts">
import {activeProjects} from '@/data/dashboard/dashboardData';
</script>
<template>
    <v-card elevation="10" class="overflow-auto">
        <v-card-item class="pa-6">
            <v-card-title class="text-h5 pt-sm-2 pb-7">Cosas bonitas deskover</v-card-title>
            <div>
                <v-table class="month-table" style="min-width:600px;">
                    <thead>
                        <tr>
                            <th class="text-subtitle-1 font-weight-bold">Id</th>
                            <th class="text-subtitle-1 font-weight-bold">Líder</th>
                            <th class="text-subtitle-1 font-weight-bold">Código Proyecto</th>
                            <th class="text-subtitle-1 font-weight-bold">Categoría</th>
                            <th class="text-subtitle-1 font-weight-bold">Progreso</th>
                            <th class="text-subtitle-1 font-weight-bold text-right">Inversión</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in activeProjects" :key="item.id" class="month-item">
                            <td>
                                <p class="text-15 font-weight-medium">{{ item.id }}</p>
                            </td>
                            <td>
                                <div class="">
                                    <h6 class="text-subtitle-1 font-weight-bold">{{ item.name }}</h6>
                                </div>
                            </td>
                            <td>
                                <h6 class="text-body-1 text-muted">{{ item.pname }}</h6>
                            </td>
                            <td>
                                <div>
                                    <h6 class="text-subtitle-1">{{ item.category }}</h6>
                                    <p class="text-13 mt-1 text-muted">{{ item.subcategory }}</p>
                                </div>
                            </td>
                            <td>
                                <td>
                                    <v-chip :style="{ backgroundColor: item.statuscolor }" color="black" size="small" >
                                        {{ item.status }}
                                    </v-chip>
                                </td>

                            </td>
                            <td>
                                <h6 class="text-h6 text-right">{{ item.budget }}</h6>
                            </td>
                        </tr>
                    </tbody>
                </v-table>
            </div>
        </v-card-item>
    </v-card>
</template>
<style scoped>
.notoverflow {
  overflow-x: auto;
}
</style>
